"""
induct.py — the induction sweep (funnel stage 5, redesign §5).

The only place new laws enter the encyclopedia. An induction sweep gathers the
current law inventory, the pool of unconsumed seeds, and the reads accumulated
since the last sweep, and asks the model (Sonnet) to do exactly one of three
things with each candidate pattern: draft a NEW LAW, attach EVIDENCE to an
existing law, or LEAVE the material in the seed pool (the default).

The epistemic bar lives entirely in ``prompts/induct.md`` (written by Fable,
supervisor-editable). This module is the harness: fill the prompt's slots, call
the model, parse the YAML verdict, and apply it through ``agent/laws.py`` (the
stage machine) and ``agent/bibliography.py`` (source linking). Zero new laws is a
normal, respectable outcome — most sweeps should produce evidence attachments
and nothing else.

Usage:
    python3 -m agent.humboldt induct
    python3 -m agent.humboldt induct --dry-run      # call the model, apply nothing
    python3 -m agent.humboldt induct --since 2026-07-01   # override the read cursor
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import yaml
from ruamel.yaml.scalarstring import FoldedScalarString

from agent import bibliography as bib
from agent import funnel_log
from agent import law_notify
from agent import laws as laws_mod

_ROOT = Path(__file__).parent.parent
_SEEDS_DIR = _ROOT / "laws" / "seeds"
_SHALLOW_DIR = _ROOT / "bibliography" / "shallow-reads"
_NOTES_DIR = _ROOT / "bibliography" / "notes"
_IDENTITY = _ROOT / "IDENTITY.md"
_PROMPT = _ROOT / "prompts" / "induct.md"
_CURSOR = _SEEDS_DIR.parent / ".induct-cursor"   # laws/.induct-cursor

INDUCT_MODEL = "claude-sonnet-4-6"   # §5 stage 5 tier; supervisor-editable
# A truncated sweep is a wasted sweep: the YAML never closes, nothing parses, and
# the whole prompt is paid for twice. Raised from 8000 on 2026-08-10, when
# requiring both lifecycle triggers per new law pushed a normal 4-law verdict
# past the old ceiling.
INDUCT_MAX_TOKENS = 16000
_MAX_SEEDS = 60          # bound the prompt; the seed pool can grow unbounded
_MAX_SHALLOW = 20
_MAX_DEEP = 5


# ── Input gathering ───────────────────────────────────────────────────────────

def _load_open_seeds() -> list[dict]:
    """Every seed still in the pool (status open or unset), newest first."""
    seeds = []
    for f in sorted(_SEEDS_DIR.glob("seed-*.yaml")):
        try:
            s = yaml.safe_load(f.read_text()) or {}
        except Exception:
            continue
        if s.get("status", "open") == "open":
            s["_file"] = f
            seeds.append(s)
    seeds.sort(key=lambda s: str(s.get("surfaced", "")), reverse=True)
    return seeds


def _cursor_date(override: str | None) -> str:
    if override:
        return override
    if _CURSOR.exists():
        return _CURSOR.read_text().strip()
    return ""   # empty → first sweep, fall back to most-recent-N


def _recent_shallow(since: str) -> list[Path]:
    """Shallow-read summaries dated on/after the cursor (by filename prefix).
    On the first sweep (no cursor) take the most recent handful."""
    dated = []
    for f in sorted(_SHALLOW_DIR.glob("*.md")):
        if f.name.startswith("_"):
            continue
        m = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
        fdate = m.group(1) if m else ""
        dated.append((fdate, f))
    dated.sort(reverse=True)
    if since:
        picked = [f for d, f in dated if d >= since]
    else:
        picked = [f for _, f in dated]
    return picked[:_MAX_SHALLOW]


def _uncited_deep_notes() -> list[Path]:
    """Deep-read notes whose bibliography entry is not yet cited by any law —
    the richest unconsumed material for the sweep to fold into laws."""
    paths = []
    for e in bib.load():
        if e.get("read_depth") == "deep" and not e.get("laws") and e.get("notes"):
            p = _ROOT / e["notes"]
            if p.exists():
                paths.append(p)
    return paths[:_MAX_DEEP]


def _format_inventory(laws: list) -> str:
    if not laws:
        return "(no laws yet — the encyclopedia is empty)"
    lines = []
    for law in laws:
        stmt = str(law.get("statement", "")).strip().replace("\n", " ")
        lines.append(
            f"- {law['id']} [{law.get('stage')}/{law.get('status')}] "
            f"{law.get('title', '')}\n    {stmt[:220]}"
        )
    return "\n".join(lines)


def _format_seeds(seeds: list[dict]) -> str:
    if not seeds:
        return "(seed pool empty)"
    out = []
    for s in seeds[:_MAX_SEEDS]:
        text = str(s.get("text", "")).strip().replace("\n", " ")
        out.append(f"- {s.get('id')}: {s.get('title', '')}\n    {text[:300]}")
    extra = len(seeds) - _MAX_SEEDS
    if extra > 0:
        out.append(f"  (+{extra} more open seeds not shown)")
    return "\n".join(out)


def _format_reads(shallow: list[Path], deep: list[Path]) -> str:
    parts = []
    for p in shallow:
        parts.append(f"### shallow · {p.name}\n{p.read_text().strip()[:1400]}")
    for p in deep:
        parts.append(f"### deep (uncited) · {p.name}\n{p.read_text().strip()[:1800]}")
    return "\n\n".join(parts) if parts else "(no new reads since the last sweep)"


def _identity_excerpt() -> str:
    if not _IDENTITY.exists():
        return "You are Humboldt, an artificial researcher investigating laws of the new nature."
    return _IDENTITY.read_text().strip()[:2000]


def _build_prompt(laws: list, seeds: list[dict], shallow: list[Path], deep: list[Path]) -> str:
    tmpl = _PROMPT.read_text()
    return (
        tmpl.replace("{{IDENTITY_EXCERPT}}", _identity_excerpt())
            .replace("{{LAW_INVENTORY}}", _format_inventory(laws))
            .replace("{{SEEDS}}", _format_seeds(seeds))
            .replace("{{RECENT_READS}}", _format_reads(shallow, deep))
    )


# ── Model call + parse ────────────────────────────────────────────────────────

def _strip_fences(text: str) -> str:
    """Drop a ```yaml opening fence and any closing fence — tolerant of a
    truncated response that opened a fence but never closed it."""
    text = text.strip()
    m = re.match(r"^```(?:yaml)?\s*\n", text)
    if m:
        text = text[m.end():]
        text = re.sub(r"\n```\s*$", "", text)
    return text


def _parse_yaml(text: str) -> dict:
    """Extract the YAML block from a model response (tolerant of ``` fences)."""
    data = yaml.safe_load(_strip_fences(text))
    if not isinstance(data, dict):
        raise ValueError("induction response did not parse to a mapping")
    return data


# ── Verdict application ───────────────────────────────────────────────────────

def _folded(text: str) -> FoldedScalarString:
    return FoldedScalarString(str(text).strip() + "\n")


def _clip(text: str, limit: int = 160) -> str:
    """Trim a history ``detail`` to a readable length at a word boundary.

    History details are read by humans in ``humboldt laws show`` and on the
    encyclopedia timeline; a hard character slice cuts mid-word ("…the mechani").
    """
    s = " ".join(str(text or "").split())
    if len(s) <= limit:
        return s
    cut = s[:limit]
    space = cut.rfind(" ")
    if space > limit * 0.6:          # don't strip back to almost nothing
        cut = cut[:space]
    return cut.rstrip(" ,;:—-") + "…"


# Fallback triggers, used only when the model omits them despite the prompt
# requiring both. A generic trigger is a poor trigger — but a law with an empty
# trigger can never be assessed at all, so this keeps the funnel unblocked and
# leaves an obviously-placeholder string for the supervisor to rewrite.
_DEFAULT_ADVANCE = (
    "PLACEHOLDER (auto-filled at induction — supervisor to rewrite): the "
    "mechanism confirmed by evidence from 2+ genuinely independent domains, with "
    "the falsification condition stated in checkable terms."
)
_DEFAULT_CHALLENGE = (
    "PLACEHOLDER (auto-filled at induction — supervisor to rewrite): a documented "
    "case matching the law's stated conditions in which the predicted regularity "
    "does not hold, and which survives one assessment pass."
)


def _reject_reason(nl: dict) -> str | None:
    """Why this proposed law should NOT become a record, or None to proceed.

    Added 2026-09-02 after a sweep created L-018 as a hollow shell: the model had
    worked out mid-generation that its own proposal duplicated L-014, wrote
    "RETRACTED — this duplicates L-014. Filing as evidence instead." into the
    justification, and correctly filed the evidence onto L-014 — but ``_apply_new_law``
    created the record anyway, with empty mechanism, empty falsification and no
    examples. Nothing downstream caught it: ``laws validate`` passed it, the site
    published it, and the ingest embedded it.

    Two independent guards, because they fail differently:
      * an explicit self-retraction in the justification — the model knows it was wrong
      * an empty mechanism or falsification — a claim with no stated mechanism and no
        way to be wrong is not a candidate law under METHOD.md, whatever the model
        called it
    """
    justification = str(nl.get("justification") or "")
    if re.match(r"\s*RETRACTED\b", justification, re.I):
        return f"self-retracted by induction: {_clip(justification, 120)}"

    missing = [f for f in ("mechanism", "falsification")
               if not str(nl.get(f) or "").strip()]
    if missing:
        return (f"no {' and no '.join(missing)} — a law needs a stated mechanism and a "
                "way to be wrong (METHOD.md)")
    return None


def _apply_triggers(law, nl: dict) -> bool:
    """Set the law's advance/challenge triggers from the induction verdict.

    Returns True if either trigger fell back to a placeholder — the caller warns,
    because a placeholder trigger means the next assessment is evaluating boilerplate
    rather than this law's actual promotion condition.
    """
    drafted = nl.get("triggers") or {}
    advance = str(drafted.get("advance") or "").strip()
    challenge = str(drafted.get("challenge") or "").strip()
    fell_back = not advance or not challenge
    law["triggers"] = {
        "advance": _folded(advance or _DEFAULT_ADVANCE),
        "challenge": _folded(challenge or _DEFAULT_CHALLENGE),
    }
    return fell_back


def _mark_seed_consumed(seed_id: str, law_id: str) -> None:
    for f in list(_SEEDS_DIR.glob(f"{seed_id}-*.yaml")) + list(_SEEDS_DIR.glob(f"{seed_id}.yaml")):
        try:
            s = yaml.safe_load(f.read_text()) or {}
        except Exception:
            continue
        s["status"] = "promoted"
        s["promoted_to"] = law_id
        f.write_text(yaml.dump(s, sort_keys=False, allow_unicode=True))
        return


def _split_origin(raw: str) -> tuple[str, str | None]:
    """`imported (Goodhart)` → ('imported', 'Goodhart'); else ('discovered', None)."""
    raw = (raw or "discovered").strip()
    if raw.lower().startswith("imported"):
        m = re.search(r"\(([^)]+)\)|imported[:\s-]+(.+)", raw, re.I)
        source = (m.group(1) or m.group(2)).strip() if m else None
        return "imported", source
    return "discovered", None


def _apply_new_law(nl: dict) -> str:
    origin, parenthetical = _split_origin(nl.get("origin", "discovered"))
    # Imports must name a source; accept it from an explicit `source` field, else
    # from a parenthetical in the origin string (`imported (Goodhart)`).
    imp_source = str(nl.get("source") or "").strip() or parenthetical
    seeds_consumed = [str(s) for s in (nl.get("seeds_consumed") or [])]
    examples = nl.get("examples") or []
    refs = sorted({str(ex.get("source")) for ex in examples
                   if str(ex.get("source", "")).startswith("bib-")})

    law = laws_mod.create(
        title=str(nl.get("title", "untitled")).strip(),
        statement=str(nl.get("statement", "")).strip(),
        stage="exploration",
        origin=origin,
        source=imp_source,
        seeds=seeds_consumed,
        references=refs,
        detail=f"induction sweep — {_clip(nl.get('justification', ''))}",
    )
    law["mechanism"] = _folded(nl.get("mechanism", ""))
    law["justification"] = _folded(nl.get("justification", ""))
    law["falsification"] = _folded(nl.get("falsification", ""))
    law["examples"] = [
        {"domain": ex.get("domain", ""), "description": ex.get("description", ""),
         "source": ex.get("source", "")}
        for ex in examples
    ]
    if _apply_triggers(law, nl):
        print(f"    ! {law['id']}: induction omitted a trigger — placeholder written; "
              "supervisor should rewrite before the next assess pass.")
    laws_mod.save(law)

    for bib_id in refs:
        bib.link_law(bib_id, law["id"])
    for seed_id in seeds_consumed:
        _mark_seed_consumed(seed_id, law["id"])

    funnel_log.law_event("law-created", law["id"], detail=law["title"],
                         stage="exploration", origin=origin)
    law_notify.queue("created", law)
    return law["id"]


def _apply_evidence(ev: dict) -> str | None:
    law_id = str(ev.get("law", "")).strip()
    try:
        law = laws_mod.load(law_id)
    except FileNotFoundError:
        print(f"    ! evidence targets unknown law {law_id!r} — skipped")
        return None
    kind = str(ev.get("kind", "example")).strip().lower()
    bears = str(ev.get("bears_on", "")).strip()
    src = str(ev.get("source", "")).strip()
    item = {"domain": ev.get("domain", ""), "description": ev.get("description", ""),
            "source": src}

    if kind == "counterexample":
        item["resolution"] = "OPEN"
        law.setdefault("counterexamples", []).append(item)
        laws_mod.add_history(law, "counterexample",
                             f"{bears}: {_clip(item['description'])}")
        funnel_log.law_event("counterexample", law["id"], detail=bears)
    elif kind == "reference":
        if src.startswith("bib-") and src not in (law.get("references") or []):
            law.setdefault("references", []).append(src)
        laws_mod.add_history(law, "evidence", f"reference {src}: {_clip(bears, 140)}")
        funnel_log.law_event("evidence", law["id"], detail=f"reference {src}")
    else:  # example (default)
        law.setdefault("examples", []).append(item)
        laws_mod.add_history(law, "evidence", f"{bears}: {_clip(item['description'])}")
        funnel_log.law_event("evidence", law["id"], detail=bears)

    laws_mod.save(law)
    if src.startswith("bib-"):
        bib.link_law(src, law["id"])
    return law["id"]


# ── Entry point ───────────────────────────────────────────────────────────────

def induct(dry_run: bool = False, since: str | None = None) -> None:
    from dotenv import load_dotenv
    from agent import synthesizer as synth

    load_dotenv(_ROOT / ".env")

    laws = laws_mod.load_all()
    seeds = _load_open_seeds()
    cursor = _cursor_date(since)
    shallow = _recent_shallow(cursor)
    deep = _uncited_deep_notes()

    print(f"Induction sweep — {len(laws)} laws, {len(seeds)} open seeds, "
          f"{len(shallow)} recent shallow reads, {len(deep)} uncited deep notes"
          f"{f' (since {cursor})' if cursor else ' (first sweep)'}")
    if not seeds and not shallow and not deep:
        print("Nothing to induct from. Exiting.")
        return

    prompt = _build_prompt(laws, seeds, shallow, deep)

    text, stop_reason = synth.synthesize_full(
        system=prompt,
        user="Perform the induction sweep now. Return only the YAML block.",
        model=INDUCT_MODEL,
        max_tokens=INDUCT_MAX_TOKENS,
        operation="induct",
    )
    if stop_reason == "max_tokens":
        print("! warning: response hit max_tokens — output may be truncated; "
              "review before trusting new laws.")

    try:
        result = _parse_yaml(text)
    except Exception as e:  # noqa: BLE001
        print(f"! could not parse induction response: {e}\n\n{text[:1500]}")
        return

    proposed = result.get("new_laws") or []
    evidence = result.get("evidence") or []
    left = result.get("leave") or []

    # Drop proposals that should never become records (self-retracted, or with no
    # mechanism / no falsification). Their evidence attachments are unaffected —
    # they are applied separately below, which is where a retracted duplicate's
    # material is supposed to land anyway.
    new_laws, rejected = [], []
    for nl in proposed:
        reason = _reject_reason(nl)
        (rejected if reason else new_laws).append((nl, reason) if reason else nl)

    print(f"\nDecision: {len(new_laws)} new law(s), {len(evidence)} evidence attachment(s), "
          f"{len(left)} seed(s) deliberately left"
          + (f", {len(rejected)} proposal(s) rejected." if rejected else "."))
    for nl in new_laws:
        trig = nl.get("triggers") or {}
        missing = [k for k in ("advance", "challenge")
                   if not str(trig.get(k) or "").strip()]
        flag = f"  [! no {'/'.join(missing)} trigger — placeholder]" if missing else ""
        print(f"  + NEW: {nl.get('title', '')}{flag}")
    for nl, reason in rejected:
        print(f"  ✗ REJECTED: {nl.get('title', '')}\n      {reason}")
    for ev in evidence:
        print(f"  ~ EVIDENCE → {ev.get('law')}: {ev.get('kind')} — {str(ev.get('bears_on',''))[:60]}")

    if dry_run:
        print("\n(dry-run — no files written)")
        return

    created, attached = [], []
    for nl in new_laws:
        try:
            created.append(_apply_new_law(nl))
        except Exception as e:  # noqa: BLE001
            print(f"    ! failed to create law {nl.get('title','?')!r}: {e}")
    for ev in evidence:
        lid = _apply_evidence(ev)
        if lid:
            attached.append(lid)

    _CURSOR.write_text(date.today().isoformat())

    law_notify.flush()

    summary = (f"Induction sweep: created {len(created)} law(s) "
               f"({', '.join(created) or 'none'}), attached {len(attached)} evidence item(s).")
    funnel_log.behavior_visit("induct", "sensemaking", note=summary)
    from agent.pre_notebook import append as pn_append
    pn_append(process="induct", summary=summary,
              detail={"created": created, "evidence": attached, "left": len(left),
                      "seeds_seen": len(seeds), "reads_seen": len(shallow) + len(deep)})

    print(f"\n{summary}")
    if created:
        print("  → run `humboldt assess <L-NNN>` on new laws, and `humboldt ingest` "
              "to embed them.")
