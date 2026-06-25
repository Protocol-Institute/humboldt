"""Persistent daemon state — tracks what has been checked and posted."""

import json
from pathlib import Path

_STATE_PATH = Path(__file__).parent / "state.json"

_DEFAULTS: dict = {
    "last_notebook_commit": None,
    "notebook_entries_posted": [],
    "last_new_nature_message_id": None,
    "last_new_nature_activity": None,   # ISO timestamp of last human message seen
    "last_feed_check": None,
    "last_conversation_review": None,   # YYYY-MM-DD of last review pass
    "last_proactive_post_date": None,   # YYYY-MM-DD of last self-initiated #new-nature post
    # Restart-safety fields
    "responded_mention_ids": [],        # Discord message IDs already replied to (capped at 500)
    "last_startup": None,               # ISO timestamp of most recent daemon startup
    "last_clean_shutdown": None,        # ISO timestamp of last graceful shutdown (missing = crash)
}


def load() -> dict:
    if _STATE_PATH.exists():
        try:
            return {**_DEFAULTS, **json.loads(_STATE_PATH.read_text())}
        except Exception:
            pass
    return dict(_DEFAULTS)


def save(state: dict) -> None:
    _STATE_PATH.write_text(json.dumps(state, indent=2, default=str))


def record_responded_mention(state: dict, message_id: str) -> None:
    """Add a message ID to the responded-mentions set and cap it at 500 entries."""
    ids: list = state.setdefault("responded_mention_ids", [])
    if message_id not in ids:
        ids.append(message_id)
    if len(ids) > 500:
        state["responded_mention_ids"] = ids[-500:]
