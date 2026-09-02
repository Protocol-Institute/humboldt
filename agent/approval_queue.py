"""
approval_queue.py — the supervisor approval queue (redesign §6.3, §7 view 4).

Every change to how Humboldt works enters here before it runs. Two intake shapes,
both defined by ``behaviors/definition-rubric.md``:

    SIMPLE  Claude drafts the complete registry entry; the supervisor approves,
            edits-then-approves, or rejects. On approval the draft is applied to
            behaviors/registry.yaml verbatim.
    HARD    A structured brief goes to the supervisor design queue instead. Nothing
            is auto-applied — answering the brief's ``questions`` typically demotes
            the request to SIMPLE, which is the bottleneck-killer the rubric is for.

The invariant this module exists to enforce: **nothing a behavior drafts runs before
supervisor approval.** ``apply_approved`` is the only path from queue to registry, it
refuses anything not explicitly approved, and it refuses HARD entries outright — a
HARD request must be re-filed as SIMPLE with the supervisor's answers as constraints,
so the record shows a human made the epistemic call.

Storage is ``behaviors/queue.yaml``, round-tripped with ruamel so supervisor comments
and hand-edits survive a programmatic write (same reason ``laws.py`` uses it).
"""

from __future__ import annotations

import io
from datetime import date
from pathlib import Path

from ruamel.yaml import YAML

_ROOT = Path(__file__).parent.parent
_QUEUE_PATH = _ROOT / "behaviors" / "queue.yaml"
_REGISTRY_PATH = _ROOT / "behaviors" / "registry.yaml"

KINDS = {"simple", "hard"}
STATUSES = {"pending", "approved", "rejected", "applied"}

# Registry fields a SIMPLE draft must carry to be applicable (§6.2 schema).
_REQUIRED_DRAFT_FIELDS = ["id", "name", "phase", "status", "defined_by", "trigger",
                          "action", "produces"]


def _yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.width = 100
    y.indent(mapping=2, sequence=4, offset=2)
    return y


def today() -> str:
    return date.today().isoformat()


# ── Load / save ──────────────────────────────────────────────────────────────

def load() -> dict:
    if not _QUEUE_PATH.exists():
        return {"version": 1, "queue": []}
    data = _yaml().load(_QUEUE_PATH.read_text()) or {}
    data.setdefault("queue", [])
    return data


def save(data: dict) -> None:
    buf = io.StringIO()
    _yaml().dump(data, buf)
    _QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _QUEUE_PATH.write_text(buf.getvalue())


def next_id(data: dict | None = None) -> str:
    data = data if data is not None else load()
    nums = []
    for entry in data.get("queue", []):
        qid = str(entry.get("id", ""))
        if qid.startswith("q-"):
            try:
                nums.append(int(qid[2:]))
            except ValueError:
                pass
    return f"q-{max(nums, default=0) + 1:04d}"


def get(qid: str, data: dict | None = None) -> dict | None:
    data = data if data is not None else load()
    for entry in data.get("queue", []):
        if entry.get("id") == qid:
            return entry
    return None


# ── Filing ───────────────────────────────────────────────────────────────────

def file_simple(draft: dict, need: str, why_simple: str, precedent: str,
                relieves: str, origin: str, filed_by: str) -> str:
    """File a SIMPLE behavior request — a complete drafted registry entry.

    ``relieves`` is the anti-accumulation rule from the rubric: every request names
    the behavior it relieves, replaces, or feeds. A request that adds a node without
    connecting to the funnel is rejected by default — unconnected additions are what
    the 26-behavior stub graveyard grew from.
    """
    if not relieves:
        raise ValueError(
            "anti-accumulation rule: a request must name the behavior it relieves, "
            "replaces, or feeds (behaviors/definition-rubric.md)")

    data = load()
    qid = next_id(data)
    data["queue"].append({
        "id": qid,
        "kind": "simple",
        "status": "pending",
        "filed": today(),
        "filed_by": filed_by,
        "origin": origin,
        "title": draft.get("name", draft.get("id", "untitled")),
        "relieves": relieves,
        "rationale": {"need": need, "why_simple": why_simple, "precedent": precedent},
        "draft": draft,
        "decision": {"on": None, "by": None, "rationale": None},
    })
    save(data)
    return qid


def file_hard(request: str, why_hard: list[str], claude_would: str,
              questions: list[str], relieves: str, origin: str, filed_by: str) -> str:
    """File a HARD request — a structured brief for the supervisor design queue."""
    if not relieves:
        raise ValueError(
            "anti-accumulation rule: a request must name the behavior it relieves, "
            "replaces, or feeds (behaviors/definition-rubric.md)")
    if not why_hard:
        raise ValueError("a HARD brief must name which HARD criteria it hits")

    data = load()
    qid = next_id(data)
    data["queue"].append({
        "id": qid,
        "kind": "hard",
        "status": "pending",
        "filed": today(),
        "filed_by": filed_by,
        "origin": origin,
        "title": request[:80],
        "relieves": relieves,
        "brief": {
            "request": request,
            "why_hard": why_hard,
            "claude_would": claude_would,
            "questions": questions,
        },
        "decision": {"on": None, "by": None, "rationale": None},
    })
    save(data)
    return qid


# ── Decisions ────────────────────────────────────────────────────────────────

def approve(qid: str, by: str = "supervisor", rationale: str = "",
            edits: dict | None = None) -> dict:
    """Approve a queue entry, optionally with supervisor edits to the draft.

    Approval alone does not change the registry — ``apply_approved`` does, so that an
    approval can be reviewed (and reverted) before it takes effect.
    """
    data = load()
    entry = get(qid, data)
    if entry is None:
        raise KeyError(f"no queue entry {qid}")
    if entry["status"] != "pending":
        raise ValueError(f"{qid} is {entry['status']}, not pending")

    if edits:
        if entry["kind"] != "simple":
            raise ValueError("edits apply to SIMPLE drafts only")
        entry["draft"].update(edits)
        entry.setdefault("edited", True)

    entry["status"] = "approved"
    entry["decision"] = {"on": today(), "by": by, "rationale": rationale}
    save(data)
    return entry


def reject(qid: str, by: str = "supervisor", rationale: str = "") -> dict:
    data = load()
    entry = get(qid, data)
    if entry is None:
        raise KeyError(f"no queue entry {qid}")
    if entry["status"] != "pending":
        raise ValueError(f"{qid} is {entry['status']}, not pending")
    entry["status"] = "rejected"
    entry["decision"] = {"on": today(), "by": by, "rationale": rationale}
    save(data)
    return entry


# ── Application ──────────────────────────────────────────────────────────────

def validate_draft(draft: dict) -> list[str]:
    """Check a SIMPLE draft against the §6.2 registry schema. Returns problems."""
    problems = []
    for field in _REQUIRED_DRAFT_FIELDS:
        if field not in draft or draft[field] in (None, "", []):
            problems.append(f"missing required field: {field}")

    action = draft.get("action")
    if not isinstance(action, dict):
        problems.append("action must be a mapping with entrypoint/model/prompt")
    elif not action.get("entrypoint"):
        problems.append("action.entrypoint is required")

    if draft.get("status") not in (None, "active", "proposed", "retired"):
        problems.append(f"status must be active|proposed|retired, got {draft['status']!r}")

    # A drafted behavior enters as `proposed`, never `active` — the code it names
    # does not exist yet at drafting time.
    if draft.get("status") == "active":
        problems.append("a newly drafted behavior must enter as `proposed`, not `active`")

    existing = {b.get("id") for b in _load_registry_behaviors()}
    if draft.get("id") in existing:
        problems.append(f"behavior id {draft.get('id')!r} already in the registry")

    return problems


def _load_registry_behaviors() -> list:
    if not _REGISTRY_PATH.exists():
        return []
    data = _yaml().load(_REGISTRY_PATH.read_text()) or {}
    return data.get("behaviors", []) or []


def apply_approved(qid: str) -> str:
    """Apply an approved SIMPLE draft to behaviors/registry.yaml.

    The only queue → registry path. Refuses anything not approved, and refuses HARD
    entries entirely: a HARD request re-enters as SIMPLE once the supervisor has
    answered its brief, so the applied record always reflects a human decision.
    """
    data = load()
    entry = get(qid, data)
    if entry is None:
        raise KeyError(f"no queue entry {qid}")
    if entry["status"] != "approved":
        raise ValueError(
            f"{qid} is {entry['status']} — only approved entries can be applied")
    if entry["kind"] != "simple":
        raise ValueError(
            f"{qid} is a HARD brief; it must be re-filed as SIMPLE with the "
            "supervisor's answers as constraints before anything is applied")

    draft = entry["draft"]
    problems = validate_draft(draft)
    if problems:
        raise ValueError(f"{qid} draft fails validation: " + "; ".join(problems))

    y = _yaml()
    registry = y.load(_REGISTRY_PATH.read_text())
    registry.setdefault("behaviors", [])
    registry["behaviors"].append(draft)

    buf = io.StringIO()
    y.dump(registry, buf)
    _REGISTRY_PATH.write_text(buf.getvalue())

    entry["status"] = "applied"
    entry.setdefault("decision", {})["applied_on"] = today()
    save(data)
    return draft["id"]


# ── CLI ──────────────────────────────────────────────────────────────────────

_KIND_ICON = {"simple": "○", "hard": "◆"}
_STATUS_ICON = {"pending": "…", "approved": "✓", "rejected": "✗", "applied": "●"}


def cmd_list(status: str | None = None) -> None:
    data = load()
    entries = data.get("queue", [])
    if status:
        entries = [e for e in entries if e.get("status") == status]
    if not entries:
        print("Approval queue is empty." if not status
              else f"No {status} entries in the approval queue.")
        return

    pending = sum(1 for e in data["queue"] if e.get("status") == "pending")
    print(f"Approval queue — {len(entries)} shown, {pending} pending\n")
    for e in entries:
        k = _KIND_ICON.get(e.get("kind"), "?")
        s = _STATUS_ICON.get(e.get("status"), "?")
        print(f"  {s} {k} {e.get('id'):8s} {e.get('title', '')[:56]}")
        print(f"        {e.get('kind')}/{e.get('status')} · filed {e.get('filed')} "
              f"by {e.get('filed_by')} · relieves: {e.get('relieves', '—')}")


def cmd_show(qid: str) -> None:
    entry = get(qid)
    if entry is None:
        print(f"No queue entry {qid}")
        return
    buf = io.StringIO()
    _yaml().dump(entry, buf)
    print(buf.getvalue())
