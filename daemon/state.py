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
