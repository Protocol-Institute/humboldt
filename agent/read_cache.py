"""
read_cache.py — on-disk cache for Pinecone query results
(plan: read-outage-2026-08 §4 Step 4, "cache retrieval results per query hash").

The corpus is near-static: the c3po namespaces change only when someone ingests
new PI material, but the same questions arrive against them over and over —
Discord threads re-query near-identical text on every turn, and `assess` re-runs
the same law-derived queries on every sweep. Each of those repeats paid full
egress for a byte-identical answer.

Caching is keyed at **namespace granularity**, not at the caller's namespace
*set*, so a Discord reply (5 namespaces) and an `assess` pass (6) share every
namespace they have in common.

TTLs differ by what the namespace is:

  humboldt  — Humboldt's own artifacts, re-ingested daily. A stale answer here
              means Humboldt cannot see work it did yesterday, which is worse
              than the egress it saves. Short TTL.
  corpus    — PI material, changes on the order of weeks. Long TTL.

This also turns out to be the practical form of the plan's "hydrate text from
disk" idea. Two-stage query-then-``fetch`` cannot work: Pinecone's ``fetch``
has no ``include_values`` switch and always returns the 1024-float vector,
which is *larger* than the chunk text it would save. A self-populating disk
cache gets the same "pay for a chunk once" property without that trap.

Cache lives in ``data/read-cache/`` (gitignored, like all runtime state).
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_DIR = _ROOT / "data" / "read-cache"

# Seconds. See module docstring for why these differ.
TTL_CORPUS = 30 * 86400
TTL_HUMBOLDT = 86400
_HUMBOLDT_NS = "humboldt"

# Cache entries are only worth keeping for repeated *identical* queries; a
# runaway corpus of one-shot queries should not grow without bound.
MAX_ENTRIES = 4000


def _ttl_for(namespace: str) -> int:
    return TTL_HUMBOLDT if namespace == _HUMBOLDT_NS else TTL_CORPUS


def _key(query: str, namespace: str, top_k: int, filter: dict | None) -> str:
    raw = json.dumps(
        [query, namespace, top_k, filter or {}],
        sort_keys=True, default=str,
    )
    return hashlib.sha256(raw.encode()).hexdigest()[:24]


def get(query: str, namespace: str, top_k: int,
        filter: dict | None = None) -> list[dict] | None:
    """Cached results for this exact query, or None on miss/expiry.

    Returns ``[]`` only if the cached answer genuinely was empty — an outage is
    never cached, so this cannot reintroduce the empty-list-means-outage
    confusion that hid the 2026-08 failure.
    """
    path = _DIR / f"{_key(query, namespace, top_k, filter)}.json"
    if not path.exists():
        return None
    try:
        entry = json.loads(path.read_text())
    except Exception:  # noqa: BLE001
        return None
    if time.time() - entry.get("ts", 0) > _ttl_for(namespace):
        return None
    return entry.get("matches")


def put(query: str, namespace: str, top_k: int, matches: list[dict],
        filter: dict | None = None) -> None:
    """Store one namespace query's results. Failures are swallowed — a cache
    that cannot write must degrade to "no cache", never to a failed read."""
    try:
        _DIR.mkdir(parents=True, exist_ok=True)
        path = _DIR / f"{_key(query, namespace, top_k, filter)}.json"
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps({"ts": time.time(), "ns": namespace,
                                   "matches": matches}))
        tmp.replace(path)  # atomic — daemon and CLI write concurrently
    except Exception:  # noqa: BLE001
        pass


def prune(max_entries: int = MAX_ENTRIES) -> int:
    """Drop expired entries, then the oldest ones past ``max_entries``.
    Returns the number removed."""
    if not _DIR.exists():
        return 0
    now = time.time()
    entries = []
    removed = 0
    for path in _DIR.glob("*.json"):
        try:
            entry = json.loads(path.read_text())
            if now - entry.get("ts", 0) > _ttl_for(entry.get("ns", "")):
                path.unlink()
                removed += 1
            else:
                entries.append((entry.get("ts", 0), path))
        except Exception:  # noqa: BLE001
            path.unlink(missing_ok=True)
            removed += 1
    for _, path in sorted(entries)[:max(0, len(entries) - max_entries)]:
        path.unlink(missing_ok=True)
        removed += 1
    return removed


def stats() -> dict:
    """Entry count and on-disk size, for `read-status`."""
    if not _DIR.exists():
        return {"entries": 0, "bytes": 0}
    paths = list(_DIR.glob("*.json"))
    return {"entries": len(paths), "bytes": sum(p.stat().st_size for p in paths)}


def clear() -> int:
    """Drop every cached entry. Returns the number removed."""
    if not _DIR.exists():
        return 0
    paths = list(_DIR.glob("*.json"))
    for path in paths:
        path.unlink(missing_ok=True)
    return len(paths)
