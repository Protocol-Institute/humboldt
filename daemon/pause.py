"""
pause.py — simple offline pause for Humboldt's Discord presence.

While paused, the daemon does not post proactively (new-nature ticks, weekly
digest) and does not run retrieval/generation for @mentions — it replies with
a fixed offline notice instead. State lives in the normal daemon state.json
(`paused_until`), so it takes effect immediately on the running daemon with
no restart required, and clears itself once the date passes.
"""

from datetime import date

from . import state as st


def set_pause(until: str) -> None:
    """Pause posting/querying up to and including the given YYYY-MM-DD date."""
    date.fromisoformat(until)  # raises ValueError if malformed
    state = st.load()
    state["paused_until"] = until
    st.save(state)


def clear_pause() -> None:
    state = st.load()
    state["paused_until"] = None
    st.save(state)


def paused_until() -> str | None:
    """Return the pause end date (YYYY-MM-DD) if currently paused, else None."""
    until = st.load().get("paused_until")
    if not until:
        return None
    if date.today() > date.fromisoformat(until):
        return None  # pause window has elapsed
    return until


def is_paused() -> bool:
    return paused_until() is not None


def offline_message() -> str:
    until = paused_until()
    return f"Humboldt is currently offline until {until}. Query again after that date."
