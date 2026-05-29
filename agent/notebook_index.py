"""
notebook_index.py — canonical metadata for all lab notebook entries.

notebook/index.yaml is the source of truth for entry titles, timestamps,
and Discord thread IDs.  It is read by publish.py, discord_client.py, and
thread_farmer.py, and written by all three.

Schema per entry:
  date                  YYYY-MM-DD
  timestamp             ISO 8601 datetime (first commit time for existing entries)
  title                 First ## heading, or session title
  tagline               Italic subtitle line, if present
  file                  Relative path from repo root
  anchor                HTML id attribute value (always "entry-{date}")
  discord_announcement_id   str message ID or null
  discord_thread_id         str thread channel ID or null
  thread_last_farmed    ISO 8601 datetime of last thread comment harvest, or null
"""

import re
import subprocess
from pathlib import Path

import yaml

_ROOT = Path(__file__).parent.parent
_INDEX_PATH = _ROOT / "notebook" / "index.yaml"
_NOTEBOOK_URL_BASE = "https://protocol-institute.org/humboldt-notebook/"


# ── URL helpers ───────────────────────────────────────────────────────────────

def entry_anchor(date: str) -> str:
    return f"entry-{date}"


def entry_url(date: str) -> str:
    return f"{_NOTEBOOK_URL_BASE}#{entry_anchor(date)}"


# ── Read / write ──────────────────────────────────────────────────────────────

def load() -> list[dict]:
    if not _INDEX_PATH.exists():
        return []
    try:
        data = yaml.safe_load(_INDEX_PATH.read_text()) or []
        return data if isinstance(data, list) else []
    except Exception:
        return []


def save(entries: list[dict]) -> None:
    _INDEX_PATH.write_text(
        yaml.dump(entries, default_flow_style=False, allow_unicode=True, sort_keys=False)
    )


def get_entry(date: str) -> dict | None:
    for e in load():
        if e.get("date") == date:
            return e
    return None


def upsert_entry(date: str, **fields) -> dict:
    """Add or update an entry; keeps list sorted by date."""
    entries = load()
    for entry in entries:
        if entry.get("date") == date:
            entry.update(fields)
            save(entries)
            return entry
    new_entry = {"date": date, **fields}
    entries.append(new_entry)
    entries.sort(key=lambda e: e.get("date", ""))
    save(entries)
    return new_entry


# ── Metadata extraction ───────────────────────────────────────────────────────

def _extract_metadata(md_path: Path) -> tuple[str, str]:
    """Return (title, tagline) from a notebook markdown file."""
    raw = md_path.read_text()
    tagline = ""
    title = ""
    for line in raw.split("\n")[1:]:
        stripped = line.strip()
        if not tagline and stripped.startswith("*") and stripped.endswith("*") and len(stripped) > 2:
            tagline = stripped[1:-1]
        if not title and stripped.startswith("## "):
            title = stripped[3:].strip()
        if title and tagline:
            break
    return title or f"Session {md_path.stem}", tagline


def _git_first_commit_timestamp(md_path: Path) -> str | None:
    result = subprocess.run(
        ["git", "log", "--diff-filter=A", "--pretty=format:%aI", "--",
         str(md_path.relative_to(_ROOT))],
        cwd=_ROOT, capture_output=True, text=True,
    )
    ts = result.stdout.strip().split("\n")[0] if result.returncode == 0 else None
    return ts or None


# ── Bootstrap ─────────────────────────────────────────────────────────────────

def build_from_git(verbose: bool = False) -> None:
    """
    Populate index.yaml from existing notebook/*.md files and git history.
    Safe to run multiple times — only adds entries that are not yet indexed.
    """
    nb_dir = _ROOT / "notebook"
    for md_path in sorted(nb_dir.glob("????-??-??.md")):
        date = md_path.stem
        if get_entry(date):
            continue
        timestamp = _git_first_commit_timestamp(md_path)
        title, tagline = _extract_metadata(md_path)
        upsert_entry(
            date,
            timestamp=timestamp,
            title=title,
            tagline=tagline,
            file=f"notebook/{date}.md",
            anchor=entry_anchor(date),
            discord_announcement_id=None,
            discord_thread_id=None,
            thread_last_farmed=None,
        )
        if verbose:
            print(f"  Indexed {date}: {title}")
