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
the behaviour transition counts. The law record's own append-only ``history``
remains the per-law source of truth — events.jsonl is the cross-law view.

**The split is now permanent** (operator decision 2026-09-09, plan §8 "Decisions
locked"). This docstring previously said Phase 4 would unify the spine; it will
not. A ``run_id`` minted per sweep and carried onto that sweep's law events gives
the causality unification was wanted for, without putting three different units in
one file. Rows written before that date carry no ``run_id``.

Instrumentation (session 35, Phase 4): every active behavior now calls
``behavior_visit`` exactly once per invocation — one sweep or run, not one item and
not one API call (decision 1). ``outputs`` is a dict of counts keyed by the
behavior's registry ``produces:`` types (decision 2); an invocation that produced
nothing passes ``{}`` or omits keys that did not fire, so ``sum(outputs.values())
== 0`` is a meaningful prune signal rather than an artifact of always listing every
key at zero. Cost is deliberately not stored here — ``analytics/op-behavior-map.yaml``
already attributes ``daemon/costs.jsonl`` by op label.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_LOG = _ROOT / "behaviors" / "log.jsonl"
_EVENTS = _ROOT / "analytics" / "events.jsonl"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_run_id() -> str:
    """Mint a run id for one sweep, to carry onto that sweep's behavior_visit and
    any law_event calls it makes (decision 3) — the causality a unified spine was
    wanted for, without unifying the spine."""
    return uuid.uuid4().hex[:12]


def behavior_visit(behavior_id: str, phase: str, note: str | None = None,
                   outputs: dict[str, int] | None = None,
                   run_id: str | None = None) -> None:
    """Record one funnel-behavior invocation in the MDP log (same shape as
    ``agent/behaviors.py`` cmd_log_visit, so the supervisory reader consumes it)."""
    entry = {
        "timestamp": _now(),
        "behavior_id": behavior_id,
        "phase": phase,
        "arc_id": None,
        "note": note,
        "outputs": outputs or {},
        "run_id": run_id,
    }
    _LOG.parent.mkdir(parents=True, exist_ok=True)
    with _LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def law_event(event: str, law_id: str, detail: str = "", run_id: str | None = None,
              **extra) -> None:
    """Record one law lifecycle event on the analytics timeline. ``event`` is a
    free-form label (``law-created``, ``promoted``, ``demoted``, ``evidence``,
    ``challenged``, ``assessed-hold`` …); ``extra`` carries stage/confidence etc."""
    entry = {"timestamp": _now(), "event": event, "law": law_id, "detail": detail,
              "run_id": run_id}
    entry.update(extra)
    _EVENTS.parent.mkdir(parents=True, exist_ok=True)
    with _EVENTS.open("a") as f:
        f.write(json.dumps(entry) + "\n")
