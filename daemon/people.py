"""
people.py — persistent memory of Discord interlocutors.

Tracks two signals:
  1. Interactions — when Humboldt talks with someone (daemon, on_message)
  2. Contributions — when someone supplies ideas/links that survive inbox triage

Trust score = useful contribution count (items that received a shallow-read note).
Discarded contributions are tracked as context but don't reduce trust.

After NOTEBOOK_THRESHOLD interactions, signals that a notebook entry should be
written treating the person as a research conversation.

File: daemon/people.json (gitignored)
"""

import json
from datetime import date, datetime, timezone
from pathlib import Path

_PEOPLE_FILE = Path(__file__).parent / "people.json"

# After this many interactions, write a notebook entry about the person
NOTEBOOK_THRESHOLD = 3

# Handles that should never be tracked as contributors
_SKIP_HANDLES = {"humboldt", "unknown", ""}


def load() -> dict:
    if _PEOPLE_FILE.exists():
        try:
            return json.loads(_PEOPLE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save(data: dict) -> None:
    _PEOPLE_FILE.write_text(json.dumps(data, indent=2, default=str))


def record_interaction(
    username: str,
    user_id: str,
    message_snippet: str,
    channel: str = "#new-nature",
) -> dict:
    """
    Record one interaction with a Discord user.

    Returns the updated person record. Engaging with Humboldt at all is
    high-value signal — interaction_count crossing NOTEBOOK_THRESHOLD also
    triggers a person notebook entry (see needs_person_notebook_entry).
    """
    data = load()
    now = datetime.now(timezone.utc).isoformat()

    if username not in data:
        data[username] = {
            "user_id": user_id,
            "first_seen": now[:10],
            "last_seen": now[:10],
            "interaction_count": 0,
            "channels": [],
            "recent_messages": [],
            "notebook_entry_written": False,
            "useful_contributions": 0,
            "discarded_contributions": 0,
            "contribution_history": [],
            "person_notebook_entry_written": False,
        }

    person = data[username]
    person.setdefault("person_notebook_entry_written", False)
    person.setdefault("useful_contributions", 0)
    person.setdefault("discarded_contributions", 0)
    person.setdefault("contribution_history", [])

    person["user_id"] = user_id
    person["last_seen"] = now[:10]
    person["interaction_count"] += 1

    if channel not in person["channels"]:
        person["channels"].append(channel)

    person["recent_messages"].append({
        "date": now[:10],
        "channel": channel,
        "snippet": message_snippet[:200],
    })
    person["recent_messages"] = person["recent_messages"][-10:]

    save(data)
    return person


def get_person_context(username: str) -> str | None:
    """
    Return a short context block about a known interlocutor for prompt injection.

    Returns None for first-time or one-time interactions (nothing useful to say yet).
    """
    data = load()
    person = data.get(username)
    if not person or person["interaction_count"] < 2:
        return None

    count = person["interaction_count"]
    first = person["first_seen"][:10]
    recent = person["recent_messages"][-4:]

    lines = [
        f"## Known interlocutor: @{username}",
        f"You have spoken with @{username} {count} time(s), first on {first}.",
        "What they've raised in recent exchanges:",
    ]
    for m in recent:
        lines.append(f"  [{m['date']}] {m['snippet']}")
    lines.append(
        "\nAcknowledge this history naturally if relevant — you know this person. "
        "Don't force it if it adds nothing."
    )
    return "\n".join(lines)


def needs_notebook_entry(username: str) -> bool:
    """True if interaction count has hit threshold and no notebook entry written yet."""
    data = load()
    person = data.get(username)
    if not person:
        return False
    return (
        person["interaction_count"] >= NOTEBOOK_THRESHOLD
        and not person.get("notebook_entry_written", False)
    )


def needs_person_notebook_entry(username: str) -> bool:
    """
    True if this person warrants a notebook entry based on either signal:
    - useful_contributions >= NOTEBOOK_THRESHOLD, or
    - interaction_count >= NOTEBOOK_THRESHOLD (engaging with Humboldt is high-value signal)
    ...and no person notebook entry has been written yet.
    """
    data = load()
    person = data.get(username)
    if not person:
        return False
    if person.get("person_notebook_entry_written", False):
        return False
    return (
        person.get("useful_contributions", 0) >= NOTEBOOK_THRESHOLD
        or person.get("interaction_count", 0) >= NOTEBOOK_THRESHOLD
    )


def mark_notebook_entry_written(username: str) -> None:
    """Call after writing a (interaction-based) notebook entry for this person."""
    data = load()
    if username in data:
        data[username]["notebook_entry_written"] = True
        save(data)


def get_all() -> dict:
    """Return the full people store (for inspection / notebook generation)."""
    return load()


# ── Contribution tracking ────────────────────────────────────────────────────
# Called by the inbox pipeline (shallow_read, inbox archive-discards) to record
# when a person's inbox submission was useful or discarded.

def record_contribution(
    handle: str,
    decision: str,       # "shallow" (useful) or "discard"
    item_type: str,      # "idea", "link", "feed"
    title: str,
    connection: str = "",
    contribution_date: str | None = None,
) -> bool:
    """
    Record one contribution. Returns True if this call just crossed the
    notebook-entry threshold (useful_contributions went from N-1 to N where
    N == NOTEBOOK_THRESHOLD), so the caller can trigger entry generation.
    """
    handle = handle.strip().lstrip("@")
    if handle.lower() in _SKIP_HANDLES:
        return False

    data = load()
    today = contribution_date or date.today().isoformat()

    if handle not in data:
        data[handle] = {
            "user_id": None,
            "first_seen": today,
            "last_seen": today,
            "interaction_count": 0,
            "channels": [],
            "recent_messages": [],
            "notebook_entry_written": False,
            "useful_contributions": 0,
            "discarded_contributions": 0,
            "contribution_history": [],
            "person_notebook_entry_written": False,
        }

    person = data[handle]
    person["last_seen"] = today
    person.setdefault("useful_contributions", 0)
    person.setdefault("discarded_contributions", 0)
    person.setdefault("contribution_history", [])
    person.setdefault("person_notebook_entry_written", False)

    before = person["useful_contributions"]
    if decision == "shallow":
        person["useful_contributions"] += 1
    elif decision == "discard":
        person["discarded_contributions"] += 1

    person["contribution_history"].append({
        "date": today,
        "item_type": item_type,
        "title": title[:100],
        "decision": decision,
        "connection": connection,
    })

    save(data)

    # Signal threshold crossing: just hit NOTEBOOK_THRESHOLD useful contributions
    # and entry not yet written
    just_crossed = (
        decision == "shallow"
        and before < NOTEBOOK_THRESHOLD
        and person["useful_contributions"] >= NOTEBOOK_THRESHOLD
        and not person["person_notebook_entry_written"]
    )
    return just_crossed


def record_contributions_for_authors(
    author_string: str,
    decision: str,
    item_type: str,
    title: str,
    connection: str = "",
    contribution_date: str | None = None,
) -> list[str]:
    """
    Parse a comma-separated author string and record for each author.
    Returns list of handles that just crossed the notebook-entry threshold.
    """
    crossed = []
    for handle in author_string.split(","):
        handle = handle.strip()
        if record_contribution(
            handle=handle,
            decision=decision,
            item_type=item_type,
            title=title,
            connection=connection,
            contribution_date=contribution_date,
        ):
            crossed.append(handle)
    return crossed


def mark_person_notebook_entry_written(handle: str) -> None:
    """Call after writing a person notebook entry for this handle."""
    data = load()
    handle = handle.strip().lstrip("@")
    if handle in data:
        data[handle]["person_notebook_entry_written"] = True
        save(data)


def trust_score(person: dict) -> int:
    """Trust = number of useful contributions supplied."""
    return person.get("useful_contributions", 0)


def contribution_summary() -> str:
    data = load()
    contributors = {
        handle: p for handle, p in data.items()
        if p.get("useful_contributions", 0) > 0 or p.get("discarded_contributions", 0) > 0
    }
    if not contributors:
        return "No contribution data yet."

    people = sorted(contributors.values(), key=trust_score, reverse=True)
    lines = [f"Contribution trust model — {len(people)} contributor(s)\n"]
    for p in people:
        useful = p.get("useful_contributions", 0)
        discarded = p.get("discarded_contributions", 0)
        total = useful + discarded
        lines.append(
            f"  {p['discord_handle'] if 'discord_handle' in p else list(data.keys())[list(data.values()).index(p)]:<22}"
            f"  trust={trust_score(p)}  ({useful}/{total} useful)  last seen {p.get('last_seen', '?')}"
        )
    return "\n".join(lines)


def person_contribution_detail(handle: str) -> str:
    data = load()
    handle = handle.strip().lstrip("@")
    if handle not in data:
        return f"No model for '{handle}'."

    p = data[handle]
    useful = p.get("useful_contributions", 0)
    discarded = p.get("discarded_contributions", 0)
    lines = [
        f"\n{handle}",
        f"  Trust score  : {trust_score(p)}",
        f"  Useful       : {useful}",
        f"  Discarded    : {discarded}",
        f"  First seen   : {p.get('first_seen', '?')}",
        f"  Last seen    : {p.get('last_seen', '?')}",
        f"  Interactions : {p.get('interaction_count', 0)} (daemon messages)",
        "",
        "  Contribution history:",
    ]
    for c in p.get("contribution_history", []):
        marker = "✓" if c["decision"] == "shallow" else "✗"
        lines.append(f"    [{c['date']}] {marker} [{c['item_type']}] {c['title'][:65]}")
        if c.get("connection") and c["connection"] not in ("none", ""):
            lines.append(f"         → {c['connection']}")
    return "\n".join(lines)
