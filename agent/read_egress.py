"""
read_egress.py — monthly accounting for Pinecone read egress
(plan: read-outage-2026-08 §4 Step 4).

The 2026-08 outage was not "a quota was too small". It was that 1GB/month of
read egress was being spent invisibly: nothing anywhere in this system reported
how many bytes a query pulled back, so the only signal that the budget existed
at all was the 429 that arrived after it was gone. This module makes the spend
countable *before* exhaustion, which is the whole point of Step 4 — the
September reset without this is just a fresh clock on the same blind spend.

What is measured: the serialized size of the metadata returned per match. That
is the payload that actually dominates — every match carries up to 2000
characters of chunk text (see agent/ingest.py), so egress is essentially
``matches returned x chunk size``, and the number of matches returned is the
only lever we control.

**This is an estimate, and deliberately a lower bound.** It excludes HTTP
framing, ids and scores, and it cannot see the Cloudflare Worker at all — the
public site chat in ``humboldt-site/functions/chat.js`` queries Pinecone from a
separate runtime and spends from the same account quota. The Worker keeps its
own counter in KV (see that file); the two must be added by hand to get a true
account total. Treat the number here as "the floor of what Python spent", good
for trend and for catching a runaway path, not for reconciling against
Pinecone's own billing page.

Ledger: ``data/read-egress.jsonl`` — one line per namespace query, append-only,
the same shape as daemon/costs.jsonl. Append-only because the daemon and CLI
both write concurrently and a read-modify-write JSON file would silently lose
counts.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).parent.parent
_PATH = _ROOT / "data" / "read-egress.jsonl"

# Pinecone Starter monthly caps, as observed in the two 2026 outages. Either one
# takes all reads offline on its own.
EGRESS_CAP_BYTES = 1_000_000_000        # hit 2026-08-17
READ_UNIT_CAP = 1_000_000               # hit 2026-07-22 (not counted here — the
                                        # client does not report read units)

# Fraction of the monthly cap at which status lines start shouting.
WARN_FRACTION = 0.70


def month_key(ts: datetime | None = None) -> str:
    """Pinecone quotas reset at the calendar month boundary, in UTC."""
    return (ts or datetime.now(timezone.utc)).strftime("%Y-%m")


def measure(matches: list) -> int:
    """Estimated wire bytes for a list of Pinecone matches.

    Counts metadata only: it is the part that scales with chunk text and the
    part we can shrink. Values are not requested (include_values defaults to
    False) so they cost nothing.
    """
    total = 0
    for m in matches:
        # Accepts both raw Pinecone matches and the normalized dicts we cache.
        md = (m.get("metadata") if isinstance(m, dict)
              else getattr(m, "metadata", None)) or {}
        try:
            total += len(json.dumps(md, default=str))
        except Exception:  # noqa: BLE001 — accounting must never break a read
            total += 0
    return total


def record(namespace: str, n_matches: int, n_bytes: int, *,
           op: str = "query", cached: bool = False) -> None:
    """Append one query's egress to the ledger.

    ``cached=True`` records a query that was served from the local read cache
    and therefore spent *nothing* — kept in the ledger so the cache's savings
    are visible rather than merely asserted.
    """
    record_ = {
        "ts":     datetime.now(timezone.utc).isoformat(),
        "ns":     namespace,
        "op":     op,
        "n":      n_matches,
        "bytes":  n_bytes,
        "cached": cached,
    }
    try:
        _PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(_PATH, "a") as f:
            f.write(json.dumps(record_) + "\n")
    except Exception:  # noqa: BLE001
        pass  # accounting is never worth failing a retrieval over


def summary(month: str | None = None) -> dict:
    """Aggregate the ledger for one month (default: current)."""
    month = month or month_key()
    out = {
        "month": month,
        "bytes": 0, "matches": 0, "queries": 0,
        "saved_bytes": 0, "cache_hits": 0,
        "by_namespace": {}, "by_op": {},
    }
    if not _PATH.exists():
        return out

    with open(_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                if not r.get("ts", "").startswith(month):
                    continue
                nbytes = r.get("bytes", 0)
                if r.get("cached"):
                    out["cache_hits"] += 1
                    out["saved_bytes"] += nbytes
                    continue
                out["queries"] += 1
                out["matches"] += r.get("n", 0)
                out["bytes"] += nbytes
                ns = r.get("ns") or "(default)"
                out["by_namespace"][ns] = out["by_namespace"].get(ns, 0) + nbytes
                op = r.get("op", "query")
                out["by_op"][op] = out["by_op"].get(op, 0) + nbytes
            except Exception:  # noqa: BLE001
                pass

    out["by_namespace"] = dict(sorted(out["by_namespace"].items(), key=lambda x: -x[1]))
    out["by_op"] = dict(sorted(out["by_op"].items(), key=lambda x: -x[1]))
    out["fraction"] = out["bytes"] / EGRESS_CAP_BYTES
    return out


def _mb(n: int) -> str:
    """Scale the unit — early in a month the interesting numbers are kilobytes,
    and rounding those to '0.0MB' is how spend stays invisible."""
    if n < 1_000_000:
        return f"{n / 1_000:.0f}KB"
    return f"{n / 1_000_000:.1f}MB"


def status_line(month: str | None = None) -> str:
    """One-line summary for `daemon status`, `read-status` and the weekly digest."""
    s = summary(month)
    if s["queries"] == 0 and s["cache_hits"] == 0:
        return f"read egress {s['month']}: nothing recorded yet"
    pct = s["fraction"] * 100
    flag = "  ** over warn threshold **" if s["fraction"] >= WARN_FRACTION else ""
    saved = f", {_mb(s['saved_bytes'])} saved by cache" if s["cache_hits"] else ""
    return (f"read egress {s['month']}: ~{_mb(s['bytes'])} of "
            f"{_mb(EGRESS_CAP_BYTES)} ({pct:.0f}%, Python only{saved}){flag}")
