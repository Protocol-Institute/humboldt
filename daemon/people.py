"""
people.py — persistent memory of Discord interlocutors.

Tracks who Humboldt has spoken with, how many times, and what topics came up.
Gitignored: this is personal/relational data, not part of the research record.

After NOTEBOOK_THRESHOLD interactions, signals that a notebook entry should be
written treating the person as a research conversation.

File: daemon/people.json
"""

import json
from datetime import datetime, timezone
from pathlib import Path

_PEOPLE_FILE = Path(__file__).parent / "people.json"

# After this many interactions, write a notebook entry about the person
NOTEBOOK_THRESHOLD = 3


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

    Returns the updated person record (useful for callers checking thresholds).
    """
    data = load()
    now = datetime.now(timezone.utc).isoformat()

    if username not in data:
        data[username] = {
            "user_id": user_id,
            "first_seen": now,
            "last_seen": now,
            "interaction_count": 0,
            "channels": [],
            "recent_messages": [],
            "notebook_entry_written": False,
        }

    person = data[username]
    person["user_id"] = user_id  # update in case snowflake changed (unlikely but safe)
    person["last_seen"] = now
    person["interaction_count"] += 1

    if channel not in person["channels"]:
        person["channels"].append(channel)

    # Keep rolling window of last 10 message snippets for context injection
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
    """True if this person has hit the threshold and no notebook entry has been written yet."""
    data = load()
    person = data.get(username)
    if not person:
        return False
    return (
        person["interaction_count"] >= NOTEBOOK_THRESHOLD
        and not person.get("notebook_entry_written", False)
    )


def mark_notebook_entry_written(username: str) -> None:
    """Call after writing a notebook entry for this person."""
    data = load()
    if username in data:
        data[username]["notebook_entry_written"] = True
        save(data)


def get_all() -> dict:
    """Return the full people store (for inspection / notebook generation)."""
    return load()
