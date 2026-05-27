"""API cost tracking and daily budget enforcement for the daemon."""

import json
from datetime import datetime, timezone
from pathlib import Path

_COSTS_PATH = Path(__file__).parent / "costs.jsonl"

# USD per million tokens
_PRICING: dict[str, dict[str, float]] = {
    "claude-sonnet-4-6":        {"input": 3.00,  "output": 15.00},
    "claude-haiku-4-5-20251001": {"input": 0.80,  "output":  4.00},
}


def log_call(operation: str, model: str, input_tokens: int, output_tokens: int) -> float:
    """Record one API call; return cost in USD."""
    prices = _PRICING.get(model, {"input": 3.00, "output": 15.00})
    cost = (input_tokens * prices["input"] + output_tokens * prices["output"]) / 1_000_000
    record = {
        "ts":    datetime.now(timezone.utc).isoformat(),
        "op":    operation,
        "model": model,
        "in":    input_tokens,
        "out":   output_tokens,
        "usd":   round(cost, 6),
    }
    with open(_COSTS_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")
    return cost


class BudgetExceeded(Exception):
    """Raised when today's API spend has reached the configured daily limit."""
    pass


def today_usd() -> float:
    """Sum API costs recorded today (local calendar date)."""
    if not _COSTS_PATH.exists():
        return 0.0
    today_local = datetime.now().strftime("%Y-%m-%d")  # local time date boundary
    total = 0.0
    with open(_COSTS_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                # Records are UTC; convert to local date for midnight-reset semantics
                ts_local = datetime.fromisoformat(r["ts"]).astimezone().strftime("%Y-%m-%d")
                if ts_local == today_local:
                    total += r.get("usd", 0.0)
            except Exception:
                pass
    return round(total, 6)


def configured_limit() -> float:
    """Read daily_limit_usd from daemon/config.yaml (default $5)."""
    config_path = Path(__file__).parent / "config.yaml"
    if config_path.exists():
        try:
            import yaml
            config = yaml.safe_load(config_path.read_text()) or {}
            return float(config.get("budget", {}).get("daily_limit_usd", 5.0))
        except Exception:
            pass
    return 5.0


def check_budget(limit_usd: float | None = None) -> None:
    """
    Raise BudgetExceeded if today's spending has reached the daily limit.

    Reads the limit from config.yaml if limit_usd is not provided.
    Call this before every Claude API invocation. Resets at local midnight.
    """
    if limit_usd is None:
        limit_usd = configured_limit()
    spent = today_usd()
    if spent >= limit_usd:
        raise BudgetExceeded(f"${spent:.4f} spent today (limit ${limit_usd:.2f})")


def totals() -> dict:
    """Aggregate all logged costs from costs.jsonl."""
    if not _COSTS_PATH.exists():
        return {"calls": 0, "input_tokens": 0, "output_tokens": 0, "total_usd": 0.0, "by_operation": {}}

    calls = input_tokens = output_tokens = 0
    total_usd = 0.0
    by_op: dict[str, float] = {}

    with open(_COSTS_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
                calls += 1
                input_tokens += r.get("in", 0)
                output_tokens += r.get("out", 0)
                total_usd += r.get("usd", 0.0)
                op = r.get("op", "unknown")
                by_op[op] = by_op.get(op, 0.0) + r.get("usd", 0.0)
            except Exception:
                pass

    return {
        "calls":        calls,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_usd":    round(total_usd, 4),
        "by_operation": {k: round(v, 4) for k, v in sorted(by_op.items(), key=lambda x: -x[1])},
    }
