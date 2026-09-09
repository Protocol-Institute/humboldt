"""
read_budget.py — the corpus-read circuit breaker (plan: read-outage-2026-08 §4 Step 2).

Pinecone enforces two independent monthly caps on reads — read units and egress
bytes — and either one takes *all* queries offline account-wide while leaving
upserts and describe_index_stats working normally. That asymmetry is why the
2026-08 outage went unnoticed for weeks: every health signal we looked at was a
write or a stat, and the read paths swallowed their 429s.

This module is the state for a deliberate degraded mode:

  paused   → corpus reads are unavailable; callers must disclose that rather
             than silently emit ungrounded output.
  clear    → normal operation.

Deliberately distinct from ``daemon/pause.py``. That one means "don't speak"
(the daemon goes quiet on operator command). This one means "you may speak, but
you have no corpus" — it applies to CLI commands as much as the daemon, which is
why the state lives in ``data/read-pause.json`` rather than daemon state.json.
The two compose: pause silences, read-pause degrades-with-disclosure.

The breaker trips two ways:
  - automatically, when agent/retrieval.py sees a quota 429 (so the *next*
    exhaustion announces itself the same day instead of being found by accident
    a month later);
  - manually, via ``humboldt read-pause <YYYY-MM-DD>``.

It self-clears once the date passes, the same shape as daemon/pause.py.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_PATH = _ROOT / "data" / "read-pause.json"

# Substrings that identify a *quota* 429 as opposed to ordinary rate limiting.
# Both observed in production: read units 2026-07-22, egress bytes 2026-08-17.
QUOTA_MARKERS = ("egress limit", "read unit limit")


class RetrievalUnavailable(Exception):
    """Corpus reads are offline.

    Raised — never returned as an empty result — so no caller can mistake an
    outage for "the corpus genuinely has nothing on this". Every call site must
    make an explicit decision about what to do without a corpus.
    """

    def __init__(self, reason: str, until: str | None = None):
        self.reason = reason
        self.until = until
        suffix = f" until {until}" if until else ""
        super().__init__(f"corpus reads unavailable{suffix}: {reason}")


def _next_month_start(today: date | None = None) -> str:
    """Pinecone quotas are monthly, so an auto-trip runs to the 1st of next month."""
    d = today or date.today()
    return date(d.year + (d.month == 12), (d.month % 12) + 1, 1).isoformat()


def load() -> dict:
    if _PATH.exists():
        try:
            return json.loads(_PATH.read_text())
        except Exception:  # noqa: BLE001
            pass
    return {}


def set_pause(until: str, reason: str) -> None:
    date.fromisoformat(until)  # raises ValueError if malformed
    _PATH.parent.mkdir(parents=True, exist_ok=True)
    _PATH.write_text(json.dumps(
        {"until": until, "reason": reason,
         "tripped": datetime.now(timezone.utc).isoformat()},
        indent=2,
    ))


def clear() -> None:
    if _PATH.exists():
        _PATH.unlink()


def paused_until() -> str | None:
    """Pause end date (YYYY-MM-DD) if reads are currently paused, else None."""
    until = load().get("until")
    if not until:
        return None
    try:
        if date.today() > date.fromisoformat(until):
            return None  # window elapsed — self-clearing
    except ValueError:
        return None
    return until


def is_paused() -> bool:
    return paused_until() is not None


def reason() -> str:
    return load().get("reason", "corpus reads paused")


def is_quota_error(exc: Exception) -> bool:
    """True when an exception is a Pinecone monthly-quota 429 (not a transient
    rate limit, which we do want to retry rather than trip the breaker on)."""
    text = str(exc).lower()
    return "429" in text and any(m in text for m in QUOTA_MARKERS)


def trip(exc: Exception) -> str:
    """Record a quota exhaustion detected in the wild. Returns the pause date."""
    until = _next_month_start()
    set_pause(until, f"pinecone quota exhausted: {str(exc)[:200]}")
    print(f"  ! CORPUS READS OFFLINE — quota exhausted; reads paused until {until}.")
    return until


def status_line() -> str:
    """One-line summary for `daemon status` / digests."""
    until = paused_until()
    if not until:
        return "corpus reads: available"
    return f"corpus reads: OFFLINE until {until} ({reason()[:80]})"
