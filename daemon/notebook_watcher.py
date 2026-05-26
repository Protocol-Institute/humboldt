"""Detect new lab notebook entries via git log."""

import subprocess
from pathlib import Path

_ROOT = Path(__file__).parent.parent


def get_new_notebook_entries(since_commit: str | None) -> list[dict]:
    """
    Return notebook entries committed after since_commit.
    If since_commit is None, returns entries from the last 20 commits.
    Each entry: {commit, date, path, github_url}
    """
    if since_commit:
        rev_range = f"{since_commit}..HEAD"
    else:
        rev_range = "-20"

    result = subprocess.run(
        ["git", "log", "--name-only", "--pretty=format:%H", rev_range],
        capture_output=True, text=True, cwd=_ROOT,
    )
    if result.returncode != 0:
        return []

    entries = []
    current_commit = None
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        if len(line) == 40 and all(c in "0123456789abcdef" for c in line):
            current_commit = line
        elif line.startswith("notebook/") and line.endswith(".md") and "README" not in line:
            stem = Path(line).stem
            path = _ROOT / line
            entries.append({
                "commit": current_commit,
                "date": stem,
                "path": path,
                "github_url": f"https://github.com/Protocol-Institute/humboldt/blob/main/{line}",
            })

    # Deduplicate by date, keep first (most recent commit wins)
    seen = set()
    deduped = []
    for e in entries:
        if e["date"] not in seen:
            seen.add(e["date"])
            deduped.append(e)
    return deduped


def get_head_commit() -> str | None:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True, text=True, cwd=_ROOT,
    )
    return result.stdout.strip() if result.returncode == 0 else None
