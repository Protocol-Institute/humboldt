"""
Triage inbox/feed-*.md items against current laws and hypotheses.

Each feed item gets a decision: discard | shallow | deep
- discard: not meaningfully relevant to any law or hypothesis
- shallow: relevant — worth a 1-paragraph synthesis note in bibliography/shallow-reads/
- deep: exceptional — full M-003 deep read warranted (very high bar)

Produces a ranked report for operator review. Does not modify inbox items.

Usage:
    python3 -m agent.humboldt triage-feed
    python3 -m agent.humboldt triage-feed --output inbox/triage-YYYY-MM-DD.md
"""

import os
import re
from datetime import date
from pathlib import Path

import yaml

_ROOT = Path(__file__).parent.parent
_TRIAGE_MODEL = "claude-haiku-4-5-20251001"
_BATCH_SIZE = 15


def _load_laws() -> list[dict]:
    laws_dir = _ROOT / "research" / "laws"
    laws = []
    for f in sorted(laws_dir.glob("*.yaml")):
        try:
            laws.append(yaml.safe_load(f.read_text()))
        except Exception:
            pass
    return laws


def _load_hypotheses() -> list[dict]:
    hyp_dir = _ROOT / "research" / "hypotheses"
    hyps = []
    for f in sorted(hyp_dir.glob("*.yaml")):
        try:
            h = yaml.safe_load(f.read_text())
            if h.get("status") == "active":
                hyps.append(h)
        except Exception:
            pass
    return hyps


def _load_feed_items() -> list[dict]:
    inbox_dir = _ROOT / "inbox"
    items = []
    for f in sorted(inbox_dir.glob("feed-*.md")):
        text = f.read_text()
        title_m = re.match(r"^#\s+(.+)$", text, re.MULTILINE)
        url_m = re.search(r"\*\*URL:\*\*\s*(.+)$", text, re.MULTILINE)
        relevance_m = re.search(r"\*\*Relevance:\*\*\s*(.+)$", text, re.MULTILINE)
        summary_m = re.search(r"## Summary\s*\n(.+?)(?=\n##|\Z)", text, re.DOTALL)
        items.append({
            "file": f.name,
            "title": title_m.group(1).strip() if title_m else f.stem,
            "url": url_m.group(1).strip() if url_m else "",
            "relevance": relevance_m.group(1).strip() if relevance_m else "",
            "summary": (summary_m.group(1).strip()[:400] if summary_m else ""),
        })
    return items


def _research_context(laws: list[dict], hyps: list[dict]) -> str:
    law_lines = [
        f"  {law.get('id')}: {law.get('name')} — {str(law.get('statement', ''))[:100]}"
        for law in laws
    ]
    hyp_lines = [
        f"  {h.get('id')}: {str(h.get('question', ''))[:100]}"
        for h in hyps
    ]
    return (
        "LAWS (established or candidate):\n" + "\n".join(law_lines) +
        "\n\nACTIVE HYPOTHESES:\n" + "\n".join(hyp_lines)
    )


def _triage_batch(
    items: list[dict],
    context: str,
    client,
) -> list[dict]:
    item_block = ""
    for i, item in enumerate(items):
        item_block += (
            f"\n[{i + 1}] {item['title']}\n"
            f"Abstract: {item['summary'][:300]}\n"
        )

    prompt = f"""You are triaging research papers for an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

{context}

For each paper below, output EXACTLY one line:
[N] DECISION | CONNECTION | RATIONALE

- DECISION: discard | shallow
  discard = not meaningfully relevant to any law or hypothesis
  shallow = relevant — worth a synthesis note (all relevant papers go here; depth decisions happen during reading)
- CONNECTION: law/hypothesis IDs most relevant, e.g. "H-001, L-003" (or "none")
- RATIONALE: one sentence, max 15 words

{item_block}
Output only the numbered lines."""

    from daemon import costs
    costs.check_budget()

    resp = client.messages.create(
        model=_TRIAGE_MODEL,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )
    costs.log_call("triage_feed", _TRIAGE_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)

    results = []
    for line in resp.content[0].text.strip().splitlines():
        m = re.match(
            r"\[(\d+)\]\s+(discard|shallow|deep)\s*\|\s*([^|]+?)\s*\|\s*(.+)",
            line, re.IGNORECASE,
        )
        if m:
            idx = int(m.group(1)) - 1
            if 0 <= idx < len(items):
                results.append({
                    "file": items[idx]["file"],
                    "title": items[idx]["title"],
                    "url": items[idx]["url"],
                    "decision": m.group(2).lower(),
                    "connection": m.group(3).strip(),
                    "rationale": m.group(4).strip(),
                })
    return results


def _build_report(all_results: list[dict], n_items: int) -> str:
    today = date.today().isoformat()
    by = {"shallow": [], "discard": []}
    for r in all_results:
        bucket = r["decision"] if r["decision"] in by else "shallow"
        by[bucket].append(r)

    counts = f"{len(by['shallow'])} shallow, {len(by['discard'])} discard"
    lines = [
        f"# Feed Triage Report — {today}",
        f"\n{n_items} items triaged: {counts}\n",
    ]
    for decision, label in [("shallow", "SHALLOW READ"), ("discard", "DISCARD")]:
        group = by.get(decision, [])
        if not group:
            continue
        lines.append(f"\n## {label} ({len(group)})\n")
        for r in group:
            lines.append(f"- **{r['title']}**")
            lines.append(f"  {r['connection']} — {r['rationale']}")
            lines.append(f"  `{r['file']}`")
            if r["url"]:
                lines.append(f"  <{r['url']}>")
            lines.append("")
    return "\n".join(lines)


def triage_feed(output_path: str | None = None) -> None:
    from dotenv import load_dotenv
    import anthropic

    load_dotenv(_ROOT / ".env")

    items = _load_feed_items()
    if not items:
        print("No feed items in inbox/.")
        return

    print(f"Triaging {len(items)} feed items against current laws and hypotheses…")

    laws = _load_laws()
    hyps = _load_hypotheses()
    context = _research_context(laws, hyps)
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    all_results: list[dict] = []
    for i in range(0, len(items), _BATCH_SIZE):
        batch = items[i : i + _BATCH_SIZE]
        print(f"  Scoring {i + 1}–{min(i + _BATCH_SIZE, len(items))} of {len(items)}…")
        all_results.extend(_triage_batch(batch, context, client))

    report = _build_report(all_results, len(items))

    if output_path:
        Path(output_path).write_text(report)
        print(f"\nReport written to: {output_path}")
    else:
        print("\n" + report)
