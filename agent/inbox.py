"""
Inbox management — archive, cleanup, and status.

archive-discards: move discard items from a triage report to inbox/processed/
                  with a YYYY-MM-DD- prefix for retention tracking; updates
                  people model with discard signal for discord items
cleanup:          delete inbox/processed/ items older than 30 days
status:           show unprocessed inbox composition
"""

import re
import shutil
from datetime import date, timedelta
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_INBOX = _ROOT / "inbox"
_PROCESSED = _INBOX / "processed"
_RETENTION_DAYS = 30


def _parse_discard_items(report_path: Path) -> list[dict]:
    text = report_path.read_text()
    items = []
    for section in re.finditer(
        r"^## DISCARD\b.*?\n(.*?)(?=^## |\Z)",
        text, re.MULTILINE | re.DOTALL,
    ):
        for item_m in re.finditer(
            r"- \*\*(.+?)\*\*\n\s+([^\n]+) — ([^\n]+)\n\s+`([^`]+)`(?:\n\s+<([^>]+)>)?",
            section.group(1),
        ):
            items.append({
                "title": item_m.group(1).strip(),
                "connection": item_m.group(2).strip(),
                "rationale": item_m.group(3).strip(),
                "file": item_m.group(4).strip(),
            })
    return items


def _read_discord_meta(path: Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text()
    author_m = re.search(r"\*\*Author:\*\*\s*(.+)$", text, re.MULTILINE)
    type_m = re.search(r"\*\*Type:\*\*\s*(.+)$", text, re.MULTILINE)
    return {
        "author": author_m.group(1).strip() if author_m else "",
        "item_type": type_m.group(1).strip() if type_m else "unknown",
    }


def archive_discards(report_path: str) -> None:
    from daemon import people as ppl

    report = Path(report_path)
    if not report.exists():
        print(f"Report not found: {report_path}")
        return

    items = _parse_discard_items(report)
    if not items:
        print("No discard items found in report.")
        return

    _PROCESSED.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    moved = 0
    already_gone = 0

    print(f"Archiving {len(items)} discard items from {report.name}…")
    for item in items:
        src = _INBOX / item["file"]
        if not src.exists():
            already_gone += 1
            continue

        meta = _read_discord_meta(src)
        dest = _PROCESSED / f"{today}-{item['file']}"
        shutil.move(str(src), str(dest))
        moved += 1

        if meta.get("author"):
            ppl.record_contributions_for_authors(
                author_string=meta["author"],
                decision="discard",
                item_type=meta.get("item_type", "unknown"),
                title=item["title"],
                connection=item["connection"],
                contribution_date=today,
            )

    print(f"Done: {moved} archived to inbox/processed/  ({already_gone} already absent)")


def cleanup(older_than_days: int = _RETENTION_DAYS) -> None:
    if not _PROCESSED.exists():
        print("inbox/processed/ is empty — nothing to clean up.")
        return

    cutoff = date.today() - timedelta(days=older_than_days)
    deleted = 0
    kept = 0

    for f in sorted(_PROCESSED.iterdir()):
        if f.name.startswith(".") or f.is_dir():
            continue
        date_m = re.match(r"(\d{4}-\d{2}-\d{2})-", f.name)
        if not date_m:
            kept += 1
            continue
        if date.fromisoformat(date_m.group(1)) <= cutoff:
            f.unlink()
            deleted += 1
        else:
            kept += 1

    print(f"Cleanup: {deleted} deleted (>{older_than_days}d old), {kept} retained")


def status() -> None:
    by_type: dict[str, int] = {}
    triage_reports = []

    for f in sorted(_INBOX.iterdir()):
        if f.is_dir() or f.name == "README.md":
            continue
        name = f.name
        if name.startswith("triage"):
            triage_reports.append(name)
            continue
        if name.startswith("discord-idea"):
            key = "discord-idea"
        elif name.startswith("discord-link"):
            key = "discord-link"
        elif name.startswith("feed"):
            key = "feed"
        elif name.startswith("thread"):
            key = "thread"
        else:
            key = "other"
        by_type[key] = by_type.get(key, 0) + 1

    total = sum(by_type.values())
    print(f"\nInbox: {total} unprocessed items\n")
    for t in ["feed", "discord-idea", "discord-link", "thread", "other"]:
        if t in by_type:
            print(f"  {t:<18}  {by_type[t]}")
    if triage_reports:
        print(f"\n  Triage reports : {', '.join(sorted(triage_reports))}")
    if _PROCESSED.exists():
        n = sum(1 for f in _PROCESSED.iterdir() if not f.name.startswith(".") and not f.is_dir())
        print(f"  inbox/processed/: {n} archived (will be deleted after {_RETENTION_DAYS}d)")
    print()
