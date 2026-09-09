"""
analytics.py — per-behavior utilization from the ledgers that already exist (redesign §8).

Phase 4's premise was that utilization is blind because only induct and assess call
funnel_log.behavior_visit. That is true of *invocations*. It is not true of API traffic:
daemon/costs.jsonl has recorded every model call with an `op` label since May, 8,089 of
them, and analytics/op-behavior-map.yaml joins those labels to registry behavior ids.
That gives months of retrospective utilization now, which is what the flag thresholds
need in order to be calibrated rather than guessed.

Three sources, three different units — kept separate on purpose, because collapsing them
produces a number that looks authoritative and means nothing:

  calls    daemon/costs.jsonl      one model API call. A sweep makes several.
  visits   behaviors/log.jsonl     one behavior invocation. Only induct/assess emit these.
  events   analytics/events.jsonl  one law lifecycle event. The §8 KPI series.

`calls` is a proxy for how busy a behavior is, never for how often it ran, and for
deep-read and supervisory it is structurally zero — they make no model calls at all. Do
not let a prune heuristic read that zero as disuse; see behaviors_without_ops in the map.

This module deliberately stops at aggregation. The §8 flag heuristics (prune/split/stall)
are the [OPUS] half of Phase 4 and need supervisor review of the thresholds before they
ship, precisely because this data is what they should be calibrated against.
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

_ROOT = Path(__file__).parent.parent
_COSTS = _ROOT / "daemon" / "costs.jsonl"
_LOG = _ROOT / "behaviors" / "log.jsonl"
_EVENTS = _ROOT / "analytics" / "events.jsonl"
_MAP = _ROOT / "analytics" / "op-behavior-map.yaml"
_REGISTRY = _ROOT / "behaviors" / "registry.yaml"


# ── loading ───────────────────────────────────────────────────────────────────

def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue          # a torn final line during an append; skip, don't crash
    return out


def load_map() -> tuple[dict[str, str | None], dict[str, str]]:
    """Returns (op -> behavior_id-or-None, behavior_id -> why-it-has-no-ops)."""
    spec = yaml.safe_load(_MAP.read_text())
    ops = {op: (rec or {}).get("behavior") for op, rec in (spec.get("ops") or {}).items()}
    return ops, spec.get("behaviors_without_ops") or {}


def _registry() -> list[dict]:
    spec = yaml.safe_load(_REGISTRY.read_text())
    bs = spec.get("behaviors") or spec
    if isinstance(bs, dict):
        bs = [dict(id=k, **v) for k, v in bs.items()]
    return bs


def _ts(rec: dict, key: str = "ts") -> datetime | None:
    raw = rec.get(key) or rec.get("timestamp")
    if not raw:
        return None
    try:
        d = datetime.fromisoformat(raw)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


# ── aggregation ───────────────────────────────────────────────────────────────

def utilization(days: int | None = 90) -> dict:
    """Per-behavior calls / spend / visits over the trailing `days` (None = all time)."""
    op_map, no_ops = load_map()
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)) if days else None

    calls: dict[str, int] = defaultdict(int)
    spend: dict[str, float] = defaultdict(float)
    first: dict[str, datetime] = {}
    last: dict[str, datetime] = {}
    unknown_ops: dict[str, int] = defaultdict(int)
    by_op: dict[str, dict] = defaultdict(lambda: {"calls": 0, "usd": 0.0})

    for r in _read_jsonl(_COSTS):
        t = _ts(r)
        if t is None or (cutoff and t < cutoff):
            continue
        op = r.get("op")
        if op not in op_map:
            unknown_ops[op] += 1
            continue
        bid = op_map[op]
        by_op[op]["calls"] += 1
        by_op[op]["usd"] += r.get("usd", 0.0)
        if bid is None:                       # mapped, but deliberately not a behavior
            continue
        calls[bid] += 1
        spend[bid] += r.get("usd", 0.0)
        if bid not in first or t < first[bid]:
            first[bid] = t
        if bid not in last or t > last[bid]:
            last[bid] = t

    visits: dict[str, int] = defaultdict(int)
    for r in _read_jsonl(_LOG):
        t = _ts(r)
        if t is None or (cutoff and t < cutoff):
            continue
        visits[r.get("behavior_id")] += 1

    events: dict[str, int] = defaultdict(int)
    for r in _read_jsonl(_EVENTS):
        t = _ts(r)
        if t is None or (cutoff and t < cutoff):
            continue
        events[r.get("event")] += 1

    rows = []
    for b in _registry():
        bid = b.get("id")
        rows.append({
            "id": bid,
            "phase": b.get("phase"),
            "status": b.get("status"),
            "calls": calls.get(bid, 0),
            "usd": round(spend.get(bid, 0.0), 4),
            "visits": visits.get(bid, 0),
            "first": first.get(bid),
            "last": last.get(bid),
            # Distinguishes "no model calls by construction" from "never observed".
            "blind": bid in no_ops,
            "blind_reason": no_ops.get(bid, "").strip(),
        })
    rows.sort(key=lambda r: (-r["calls"], -r["visits"], r["id"]))

    return {
        "days": days,
        "behaviors": rows,
        "by_op": dict(by_op),
        "events": dict(events),
        "unknown_ops": dict(unknown_ops),
        "total_usd": round(sum(spend.values()), 4),
    }


def monthly_spend() -> dict[str, dict[str, float]]:
    """behavior -> {YYYY-MM: usd}, all time. The trend the split heuristic needs."""
    op_map, _ = load_map()
    out: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    for r in _read_jsonl(_COSTS):
        t = _ts(r)
        bid = op_map.get(r.get("op"))
        if t is None or bid is None:
            continue
        out[bid][t.strftime("%Y-%m")] += r.get("usd", 0.0)
    return {b: {m: round(v, 4) for m, v in sorted(ms.items())} for b, ms in out.items()}


# ── CLI ───────────────────────────────────────────────────────────────────────

def _fmt_day(d: datetime | None) -> str:
    return d.strftime("%m-%d") if d else "—"


def cmd_utilization(days: int | None = 90) -> None:
    u = utilization(days)
    window = f"trailing {days} days" if days else "all time"
    print(f"\nPer-behavior utilization — {window}\n")
    print(f"  {'behavior':<14}{'phase':<15}{'status':<10}"
          f"{'calls':>7}{'USD':>9}{'visits':>8}   {'first':<7}{'last':<7}")
    print("  " + "─" * 78)
    for r in u["behaviors"]:
        note = "  ← no model calls by construction" if r["blind"] else ""
        print(f"  {r['id']:<14}{str(r['phase']):<15}{str(r['status']):<10}"
              f"{r['calls']:>7}{r['usd']:>9.2f}{r['visits']:>8}   "
              f"{_fmt_day(r['first']):<7}{_fmt_day(r['last']):<7}{note}")
    print("  " + "─" * 78)
    print(f"  {'total':<39}{sum(r['calls'] for r in u['behaviors']):>7}"
          f"{u['total_usd']:>9.2f}{sum(r['visits'] for r in u['behaviors']):>8}")

    op_map, _ = load_map()
    unmapped = [(op, d) for op, d in u["by_op"].items() if op_map.get(op) is None]
    if unmapped:
        print("\n  Mapped to no behavior (real work the registry does not account for):")
        for op, d in sorted(unmapped, key=lambda x: -x[1]["calls"]):
            print(f"    {op:<24}{d['calls']:>6} calls  ${d['usd']:>7.2f}")

    if u["unknown_ops"]:
        print("\n  ⚠ Ops absent from op-behavior-map.yaml (add them):")
        for op, n in sorted(u["unknown_ops"].items(), key=lambda x: -x[1]):
            print(f"    {op:<24}{n:>6} calls")

    if u["events"]:
        print("\n  Law events in window: "
              + ", ".join(f"{k} {v}" for k, v in sorted(u["events"].items())))
    print()


def cmd_monthly() -> None:
    ms = monthly_spend()
    months = sorted({m for d in ms.values() for m in d})
    print(f"\nMonthly spend by behavior (USD)\n")
    print(f"  {'behavior':<14}" + "".join(f"{m[-5:]:>10}" for m in months))
    print("  " + "─" * (14 + 10 * len(months)))
    for b in sorted(ms, key=lambda b: -sum(ms[b].values())):
        print(f"  {b:<14}" + "".join(f"{ms[b].get(m, 0):>10.2f}" for m in months))
    print()


def cmd_analytics(subcmd: str, rest: list[str]) -> None:
    if subcmd in ("utilization", "util"):
        days: int | None = 90
        if rest:
            days = None if rest[0] in ("all", "--all") else int(rest[0])
        cmd_utilization(days)
    elif subcmd == "monthly":
        cmd_monthly()
    else:
        print("usage: humboldt analytics utilization [DAYS|all] | monthly")
