"""
Pre-notebook activity log — machine-generated records from all automated processes.

Every automated process (shallow_read, ingest, triage, daemon tasks) appends an entry
here. When Humboldt writes a notebook entry (in-session or daemon), it reads pending
entries, synthesizes them into a narrative, and advances the cursor.

Files:
  notebook/pre-notebook.jsonl    — append-only activity log
  notebook/.pre-notebook-cursor  — ISO timestamp of last consumed entry
"""

import json
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_LOG = _ROOT / "notebook" / "pre-notebook.jsonl"
_CURSOR = _ROOT / "notebook" / ".pre-notebook-cursor"


def append(process: str, summary: str, detail: dict | None = None) -> None:
    """Append one activity record. Safe to call from any process."""
    entry: dict = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "process": process,
        "summary": summary,
    }
    if detail:
        entry["detail"] = detail
    _LOG.parent.mkdir(parents=True, exist_ok=True)
    with _LOG.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def get_pending() -> list[dict]:
    """Return all entries after the cursor (unconsumed)."""
    if not _LOG.exists():
        return []
    cursor_ts: str | None = _CURSOR.read_text().strip() if _CURSOR.exists() else None
    entries = []
    for line in _LOG.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
            if cursor_ts is None or entry["ts"] > cursor_ts:
                entries.append(entry)
        except Exception:
            pass
    return entries


def mark_consumed() -> None:
    """Advance cursor to the latest pending entry. Call after writing a notebook entry."""
    all_entries: list[dict] = []
    if not _LOG.exists():
        return
    for line in _LOG.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            all_entries.append(json.loads(line))
        except Exception:
            pass
    if not all_entries:
        return
    latest_ts = max(e["ts"] for e in all_entries)
    _CURSOR.write_text(latest_ts)


def show_pending() -> None:
    """Print pending entries in human-readable form for Track 1 startup orientation."""
    entries = get_pending()
    if not entries:
        print("No pending pre-notebook entries.")
        return

    print(f"Pre-notebook queue — {len(entries)} pending entr{'y' if len(entries) == 1 else 'ies'} since last notebook:\n")
    for e in entries:
        ts = e["ts"][:16].replace("T", " ")
        process = e["process"]
        summary = e["summary"]
        print(f"  [{ts}] {process}")
        print(f"    {summary}")
        detail = e.get("detail", {})
        if detail:
            for k, v in detail.items():
                if isinstance(v, list) and v:
                    print(f"    {k}: {', '.join(str(x) for x in v[:5])}" +
                          (f" … (+{len(v)-5})" if len(v) > 5 else ""))
                elif v:
                    print(f"    {k}: {v}")
        print()
