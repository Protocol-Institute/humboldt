#!/usr/bin/env python3
"""A/B the site chat's answer model (answer-path playbook item 3).

Asks the same questions of AB_VARIANTS a and b in chat.js (same retrieval, same
prompt), records time / words / usage, and writes both answers side by side to
data/ab-YYYY-MM-DD.md for reading in Humboldt's own voice. Costs a few dollars.

    .venv/bin/python bin/ab_model.py [--variants a,b] [--n 10]
"""
from __future__ import annotations

import argparse
import statistics
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from chat_common import ROOT, admin_key, ask  # noqa: E402

QUESTIONS = [
    "What is the strongest law in your inventory, and why do you trust it?",
    "Which of your laws do you think is most likely to be wrong?",
    "How does protocol ossification relate to Gall's law?",
    "Explain L-012 to someone who has never heard of Goodhart's law.",
    "What would it take to promote L-006 to the next stage?",
    "Are L-022 and L-023 really distinct laws?",
    "What did you get wrong in your Symposium talk?",
    "How do you decide what to read next?",
    "What is the Protocol Institute's view of AI agents as protocol participants?",
    "Do protocols have a lifecycle? Give me your best current model.",
]
PRICES = {"claude-sonnet-4-6": (3, 3.75, 0.30, 15), "claude-sonnet-5-5": (2, 2.5, 0.10, 10)}


def usd(model, u):
    p = PRICES[model]
    return (u.get("input_tokens", 0) * p[0] + u.get("cache_creation_input_tokens", 0) * p[1]
            + u.get("cache_read_input_tokens", 0) * p[2] + u.get("output_tokens", 0) * p[3]) / 1e6


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variants", default="a,b")
    ap.add_argument("--n", type=int, default=len(QUESTIONS))
    a = ap.parse_args()
    key = admin_key()
    variants = a.variants.split(",")
    rows = {v: [] for v in variants}
    md = [f"# Site chat A/B — {date.today()}\n"]
    for q in QUESTIONS[: a.n]:
        md.append(f"\n## {q}\n")
        for v in variants:
            r = ask(q, key=key, variant=v)
            words = len(r["answer"].split())
            cost = usd(r["_model"], r["_usage"])
            rows[v].append((r["_ms"] / 1000, words, cost))
            md.append(f"\n### {v} — {r['_model']} — {r['_ms']/1000:.1f}s, {words} words, ${cost:.4f}\n\n{r['answer']}\n")
            print(f"{v} {r['_ms']/1000:5.1f}s {words:4d}w ${cost:.4f}  {q[:50]}")
    print()
    for v in variants:
        t, w, c = zip(*rows[v])
        print(f"{v}: median {statistics.median(t):.1f}s, {statistics.median(w):.0f} words, "
              f"${statistics.median(c):.4f}/answer")
    out = ROOT / "data" / f"ab-{date.today()}.md"
    out.write_text("".join(md))
    print(f"\nAnswers side by side: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
