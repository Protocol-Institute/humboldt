#!/usr/bin/env python3
"""Saved probe for the public site chat (answer-path playbook item 0).

Each case in bin/chat_probe_cases.json names what the LIVE chat must do:
  sources_any    — at least one returned source label/title/url contains one of these
  answer_has_any — the answer contains at least one of these (case-insensitive)
  answer_lacks   — the answer contains none of these
  now            — replay a date (admin `now`)
A case with only source checks runs retrieval-only (no model cost).
Exits non-zero on any failure. Run after every change to chat.js or the prompt.

    .venv/bin/python bin/chat_probe.py [--variant b] [-k substring]
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from chat_common import admin_key, ask  # noqa: E402

CASES = Path(__file__).with_name("chat_probe_cases.json")


def run_case(case: dict, key: str, variant: str | None) -> tuple[str, list[str]]:
    needs_answer = "answer_has_any" in case or "answer_lacks" in case
    r = ask(case["q"], key=key, variant=variant, now=case.get("now"),
            sources_only=not needs_answer)
    fails = []
    if "sources_any" in case:
        blob = json.dumps(r.get("sources", [])).lower()
        if not any(s.lower() in blob for s in case["sources_any"]):
            fails.append(f"no source matching {case['sources_any']}")
    ans = (r.get("answer") or "").lower()
    if "answer_has_any" in case and not any(s.lower() in ans for s in case["answer_has_any"]):
        fails.append(f"answer lacks all of {case['answer_has_any']}")
    for s in case.get("answer_lacks", []):
        if s.lower() in ans:
            fails.append(f"answer contains forbidden {s!r}")
    if r.get("corpusOffline"):
        fails.append("corpus offline")
    return case["q"], fails


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant")
    ap.add_argument("-k", help="only cases whose question contains this")
    a = ap.parse_args()
    key = admin_key()
    cases = json.loads(CASES.read_text())
    if a.k:
        cases = [c for c in cases if a.k.lower() in c["q"].lower()]
    with ThreadPoolExecutor(6) as ex:
        results = list(ex.map(lambda c: run_case(c, key, a.variant), cases))
    bad = 0
    for q, fails in results:
        print(("FAIL " if fails else "ok   ") + q[:70])
        for f in fails:
            print("       -", f)
        bad += bool(fails)
    print(f"\n{len(results) - bad}/{len(results)} passed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
