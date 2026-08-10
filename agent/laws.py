"""
laws.py — the law record: CRUD, validation, stage machine, history.

The law record (``laws/L-NNN-<slug>.yaml``) is the single research artifact
type in the 2026-08 redesign — it replaces the C/H/CL/T/F typed-artifact
system. This module is the programmatic gateway to it: loading, validating
against the ``laws/_schema.yaml`` semantics, appending history, and moving a
law through the Double Freytag stage machine (plan §3.1).

Files are round-tripped with ruamel.yaml so hand-authored formatting — folded
scalars, inline ``# why`` comments on ``related``/``seeds`` — survives
programmatic writes (history appends, stage changes). The supervisor console
writes these same files; git is the audit trail and undo.

CLI (wired in humboldt.py):
  humboldt laws list [--stage S] [--status S]   # inventory table
  humboldt laws show L-003                       # full record
  humboldt laws validate [L-003 | all]           # schema + stage-machine check
"""

from __future__ import annotations

import io
import re
import sys
from datetime import date
from pathlib import Path

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import FoldedScalarString

_ROOT = Path(__file__).parent.parent
_LAWS_DIR = _ROOT / "laws"

# ── Stage machine constants (mirror laws/_schema.yaml, definitive) ────────────

STAGES = ["exploration", "sensemaking", "valley", "heavy-lift", "retrospective"]
STATUSES = {"active", "challenged", "falsified"}
ORIGINS = {"discovered", "imported"}
CONFIDENCE = ["speculative", "provisional", "supported", "unfalsified"]

# Confidence is capped by stage (schema rule 4).
STAGE_CONFIDENCE_CAP = {
    "exploration": "speculative",
    "sensemaking": "provisional",
    "valley": "provisional",
    "heavy-lift": "supported",
    "retrospective": "unfalsified",
}

HISTORY_EVENTS = {
    "created", "evidence", "counterexample", "promoted", "demoted",
    "challenged", "resolved", "edited", "migrated", "falsified", "published",
}

# Fields written for a freshly-created record, in schema order.
_FIELD_ORDER = [
    "id", "title", "slug", "stage", "status", "origin", "source", "confidence",
    "statement", "mechanism", "justification", "examples", "counterexamples",
    "open_questions", "falsification", "references", "seeds", "related",
    "triggers", "history",
]


# ── YAML round-trip plumbing ──────────────────────────────────────────────────

def _yaml() -> YAML:
    """A round-trip YAML configured to match the hand-authored law files."""
    y = YAML()
    y.preserve_quotes = True
    y.width = 90          # keeps folded scalars from re-wrapping tighter than authored
    y.indent(mapping=2, sequence=4, offset=2)  # block seqs: "  - " under their key
    # Render None as the explicit `null` the hand-authored files use, not empty.
    y.representer.add_representer(
        type(None),
        lambda r, d: r.represent_scalar("tag:yaml.org,2002:null", "null"),
    )
    return y


def stage_index(stage: str) -> int:
    return STAGES.index(stage)


def confidence_index(conf: str) -> int:
    return CONFIDENCE.index(conf)


# ── Load / save ───────────────────────────────────────────────────────────────

def _law_files() -> list[Path]:
    return sorted(p for p in _LAWS_DIR.glob("L-*.yaml") if not p.name.startswith("_"))


def path_for(law_id: str) -> Path | None:
    """Resolve an ``L-NNN`` id (or a filename) to its file path."""
    law_id = law_id.strip()
    if law_id.endswith(".yaml"):
        p = (_LAWS_DIR / law_id) if "/" not in law_id else Path(law_id)
        return p if p.exists() else None
    # Normalise L-3 → L-003
    m = re.fullmatch(r"[Ll]-?(\d+)", law_id)
    if m:
        law_id = f"L-{int(m.group(1)):03d}"
    matches = list(_LAWS_DIR.glob(f"{law_id}-*.yaml")) + list(_LAWS_DIR.glob(f"{law_id}.yaml"))
    return matches[0] if matches else None


def load(law_id: str):
    """Load one law record (ruamel CommentedMap). Raises if not found."""
    p = path_for(law_id)
    if not p:
        raise FileNotFoundError(f"No law record for {law_id!r}")
    return _yaml().load(p.read_text())


def load_all() -> list:
    """All law records, sorted by id. Skips files that fail to parse (logged)."""
    y = _yaml()
    out = []
    for p in _law_files():
        try:
            out.append(y.load(p.read_text()))
        except Exception as e:  # noqa: BLE001 — surface, don't crash the sweep
            print(f"  ! failed to parse {p.name}: {e}", file=sys.stderr)
    out.sort(key=lambda law: law.get("id", ""))
    return out


def dumps(law) -> str:
    """Render a law record as YAML text without writing it — for prompts and
    previews that need a record the file does not (yet) contain."""
    buf = io.StringIO()
    _yaml().dump(law, buf)
    return buf.getvalue()


def save(law) -> Path:
    """Write a law record back to its canonical ``L-NNN-<slug>.yaml`` path."""
    law_id = law["id"]
    slug = law.get("slug") or _slugify(law.get("title", law_id))
    dest = _LAWS_DIR / f"{law_id}-{slug}.yaml"
    # If the slug changed, drop any stale file at the old path.
    existing = path_for(law_id)
    if existing and existing != dest:
        existing.unlink()
    buf = io.StringIO()
    _yaml().dump(law, buf)
    dest.write_text(buf.getvalue())
    return dest


# ── Ids, dates, slugs ─────────────────────────────────────────────────────────

def _slugify(text: str) -> str:
    text = re.sub(r"^the\s+", "", text.strip(), flags=re.I)
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text


def next_id() -> str:
    """Lowest unused ``L-NNN`` id (ids are never reused, never renumbered)."""
    used = set()
    for p in _law_files():
        m = re.match(r"L-(\d+)", p.name)
        if m:
            used.add(int(m.group(1)))
    n = 1
    while n in used:
        n += 1
    return f"L-{n:03d}"


def today() -> str:
    return date.today().isoformat()


# ── History and lifecycle mutations ───────────────────────────────────────────

def add_history(law, event: str, detail: str, on: str | None = None) -> None:
    """Append an append-only history entry. Nothing is ever removed."""
    if event not in HISTORY_EVENTS:
        raise ValueError(f"Unknown history event {event!r}")
    law.setdefault("history", [])
    law["history"].append({"date": on or today(), "event": event, "detail": detail})


def _clamp_confidence_to_stage(law) -> str | None:
    """Lower confidence to the stage cap if it exceeds it. Returns note or None."""
    cap = STAGE_CONFIDENCE_CAP[law["stage"]]
    if confidence_index(law.get("confidence", "speculative")) > confidence_index(cap):
        old = law["confidence"]
        law["confidence"] = cap
        return f"confidence {old} → {cap} (stage cap)"
    return None


def advance(law, detail: str, on: str | None = None):
    """Promote exactly one stage forward (schema rule 1). Records ``promoted``."""
    i = stage_index(law["stage"])
    if i >= len(STAGES) - 1:
        raise ValueError(f"{law['id']} is already at the terminal stage ({law['stage']})")
    new_stage = STAGES[i + 1]
    law["stage"] = new_stage
    law["status"] = "active"
    add_history(law, "promoted", f"{STAGES[i]} → {new_stage}. {detail}", on)
    return law


def cycle_back(law, target_stage: str, detail: str, on: str | None = None):
    """Demote to an earlier stage after a surviving challenge (schema rule 2).

    ``target_stage`` is set by what the challenge broke: evidence → valley,
    mechanism → sensemaking, statement → exploration. Confidence is re-clamped
    to the new (lower) stage cap.
    """
    if target_stage not in STAGES:
        raise ValueError(f"Unknown stage {target_stage!r}")
    if stage_index(target_stage) >= stage_index(law["stage"]):
        raise ValueError(f"cycle_back target {target_stage!r} is not earlier than {law['stage']!r}")
    old = law["stage"]
    law["stage"] = target_stage
    law["status"] = "active"
    note = _clamp_confidence_to_stage(law)
    detail = f"{old} → {target_stage}. {detail}" + (f" ({note})" if note else "")
    add_history(law, "demoted", detail, on)
    return law


def mark_challenged(law, detail: str, on: str | None = None):
    """Flag a live challenge (status only) pending an assessment pass."""
    law["status"] = "challenged"
    add_history(law, "challenged", detail, on)
    return law


def mark_falsified(law, detail: str, on: str | None = None):
    """Falsified is a status, not a stage — the record stays published, labeled."""
    law["status"] = "falsified"
    add_history(law, "falsified", detail, on)
    return law


def set_confidence(law, conf: str, detail: str, on: str | None = None):
    """Set confidence, clamped to the current stage cap. Records ``edited``."""
    if conf not in CONFIDENCE:
        raise ValueError(f"Unknown confidence {conf!r}")
    cap = STAGE_CONFIDENCE_CAP[law["stage"]]
    if confidence_index(conf) > confidence_index(cap):
        raise ValueError(
            f"confidence {conf!r} exceeds the {law['stage']} stage cap ({cap})"
        )
    old = law.get("confidence")
    law["confidence"] = conf
    add_history(law, "edited", f"confidence {old} → {conf}. {detail}", on)
    return law


# ── Creation ──────────────────────────────────────────────────────────────────

def create(
    title: str,
    statement: str,
    *,
    stage: str = "exploration",
    origin: str = "discovered",
    source: str | None = None,
    seeds: list[str] | None = None,
    references: list[str] | None = None,
    detail: str = "created",
) -> object:
    """Scaffold a new exploration-stage law, write it, and return the record.

    Used by the induction sweep (Phase 2) and by hand. Fields absent at
    creation are stubbed empty so the schema shape is always complete.
    """
    if stage not in STAGES:
        raise ValueError(f"Unknown stage {stage!r}")
    law_id = next_id()
    y = _yaml()
    law = y.load(io.StringIO("{}")) or y.map()
    law["id"] = law_id
    law["title"] = title
    law["slug"] = _slugify(title)
    law["stage"] = stage
    law["status"] = "active"
    law["origin"] = origin
    law["source"] = source
    law["confidence"] = STAGE_CONFIDENCE_CAP[stage] if stage != "exploration" else "speculative"
    law["statement"] = FoldedScalarString(statement.strip() + "\n")
    law["mechanism"] = ""
    law["justification"] = ""
    law["examples"] = []
    law["counterexamples"] = []
    law["open_questions"] = []
    law["falsification"] = ""
    law["references"] = list(references or [])
    law["seeds"] = list(seeds or [])
    law["related"] = []
    law["triggers"] = {"advance": "", "challenge": ""}
    law["history"] = [{"date": today(), "event": "created", "detail": detail}]
    save(law)
    return law


# ── Validation ────────────────────────────────────────────────────────────────

def validate(law) -> list[str]:
    """Return a list of schema / stage-machine problems (empty == valid)."""
    problems: list[str] = []
    lid = law.get("id", "?")

    for field in ("id", "title", "slug", "stage", "status", "origin", "confidence", "statement"):
        if not law.get(field):
            problems.append(f"{lid}: missing required field {field!r}")

    stage = law.get("stage")
    if stage and stage not in STAGES:
        problems.append(f"{lid}: invalid stage {stage!r}")
    if law.get("status") not in STATUSES:
        problems.append(f"{lid}: invalid status {law.get('status')!r}")
    if law.get("origin") not in ORIGINS:
        problems.append(f"{lid}: invalid origin {law.get('origin')!r}")

    conf = law.get("confidence")
    if conf and conf not in CONFIDENCE:
        problems.append(f"{lid}: invalid confidence {conf!r}")
    elif stage in STAGE_CONFIDENCE_CAP and conf in CONFIDENCE:
        cap = STAGE_CONFIDENCE_CAP[stage]
        if confidence_index(conf) > confidence_index(cap):
            problems.append(f"{lid}: confidence {conf!r} exceeds {stage} cap ({cap})")

    if law.get("origin") == "imported" and not law.get("source"):
        problems.append(f"{lid}: imported law missing `source`")

    # From sensemaking onward, mechanism + falsification are required.
    if stage in STAGES and stage_index(stage) >= stage_index("sensemaking"):
        if not str(law.get("mechanism", "")).strip():
            problems.append(f"{lid}: {stage} law missing `mechanism`")
        if not str(law.get("falsification", "")).strip():
            problems.append(f"{lid}: {stage} law missing `falsification`")

    for i, h in enumerate(law.get("history", []) or []):
        if not isinstance(h, dict) or not {"date", "event", "detail"} <= set(h):
            problems.append(f"{lid}: history[{i}] must have date/event/detail")
        elif h["event"] not in HISTORY_EVENTS:
            problems.append(f"{lid}: history[{i}] invalid event {h['event']!r}")

    return problems


def validate_all() -> dict[str, list[str]]:
    """Validate every record. Returns {law_id: [problems]} for laws with issues."""
    out = {}
    for law in load_all():
        probs = validate(law)
        if probs:
            out[law.get("id", "?")] = probs
    return out


# ── CLI ───────────────────────────────────────────────────────────────────────

_STAGE_ICON = {
    "exploration": "○", "sensemaking": "◔", "valley": "◑",
    "heavy-lift": "◕", "retrospective": "●",
}


def cmd_list(stage: str | None = None, status: str | None = None) -> None:
    laws = load_all()
    if stage:
        laws = [l for l in laws if l.get("stage") == stage]
    if status:
        laws = [l for l in laws if l.get("status") == status]
    if not laws:
        print("No law records match.")
        return
    print(f"\nLaw inventory — {len(laws)} record(s)\n")
    for law in laws:
        icon = _STAGE_ICON.get(law.get("stage"), "?")
        flag = "" if law.get("status") == "active" else f" [{law.get('status')}]"
        print(f"  {icon} {law['id']}  {law.get('title', '')}{flag}")
        print(f"       {law.get('stage')} · {law.get('confidence')} · {law.get('origin')}")
    print()


def cmd_show(law_id: str) -> None:
    p = path_for(law_id)
    if not p:
        print(f"No law record for {law_id!r}")
        sys.exit(1)
    print(p.read_text())


def cmd_validate(target: str = "all") -> None:
    if target == "all":
        issues = validate_all()
        if not issues:
            n = len(load_all())
            print(f"✓ all {n} law records valid.")
            return
        for lid, probs in issues.items():
            for p in probs:
                print(f"  ✗ {p}")
        print(f"\n{len(issues)} law(s) with problems.")
        sys.exit(1)
    else:
        law = load(target)
        probs = validate(law)
        if not probs:
            print(f"✓ {law['id']} valid.")
        else:
            for p in probs:
                print(f"  ✗ {p}")
            sys.exit(1)
