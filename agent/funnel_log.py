"""
funnel_log.py — the event spine for the funnel engines (redesign §8).

Two append-only sinks, deliberately kept separate for now:

  behaviors/log.jsonl     — one behavior-visit line per sweep. This is what the
                            MDP supervisory analysis in agent/behaviors.py reads;
                            it indexes ``entry["behavior_id"]`` and ``["phase"]``
                            directly, so every line there must carry those keys.
  analytics/events.jsonl  — one line per *law event* (created / promoted /
                            challenged / …): the denormalised timeline the KPI
                            chart and analytics.py (Phase 4) will aggregate.

Why two files rather than the single log.jsonl §8 envisions: the current
supervisory reader would KeyError on a law-event line lacking ``behavior_id``,
and folding many per-law events into log.jsonl as pseudo-visits would inflate
the behaviour transition counts. Phase 4 (analytics.py) unifies the spine; until
then this keeps both readers honest. The law record's own append-only ``history``
remains the per-law source of truth — events.jsonl is the cross-law view.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_LOG = _ROOT / "behaviors" / "log.jsonl"
_EVENTS = _ROOT / "analytics" / "events.jsonl"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def behavior_visit(behavior_id: str, phase: str, note: str | None = None) -> None:
    """Record one funnel-behavior invocation in the MDP log (same shape as
    ``agent/behaviors.py`` cmd_log_visit, so the supervisory reader consumes it)."""
    entry = {
        "timestamp": _now(),
        "behavior_id": behavior_id,
        "phase": phase,
        "arc_id": None,
        "note": note,
    }
    _LOG.parent.mkdir(parents=True, exist_ok=True)
    with _LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def law_event(event: str, law_id: str, detail: str = "", **extra) -> None:
    """Record one law lifecycle event on the analytics timeline. ``event`` is a
    free-form label (``law-created``, ``promoted``, ``demoted``, ``evidence``,
    ``challenged``, ``assessed-hold`` …); ``extra`` carries stage/confidence etc."""
    entry = {"timestamp": _now(), "event": event, "law": law_id, "detail": detail}
    entry.update(extra)
    _EVENTS.parent.mkdir(parents=True, exist_ok=True)
    with _EVENTS.open("a") as f:
        f.write(json.dumps(entry) + "\n")
