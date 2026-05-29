"""
Perform shallow reads on inbox items from a triage report.

Humboldt reads each non-discard item and writes a synthesis note to
bibliography/shallow-reads/. During the read, Humboldt decides whether
to escalate to a full M-003 deep read or store as shallow only.

Escalation criteria (applied strictly — should be rare):
- Primary source with a sustained argument, not just a measurement or case study
- Directly challenges, substantially extends, or grounds an established law/hypothesis
- Introduces a mechanism not captured by current inventory
- Cross-domain generality beyond the specific case studied

Usage:
    python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md
    python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md --dry-run
"""

import os
import re
from datetime import date
from pathlib import Path

import yaml

_ROOT = Path(__file__).parent.parent
_MODEL = "claude-haiku-4-5-20251001"


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


def _research_context(laws: list[dict], hyps: list[dict]) -> str:
    law_lines = [
        f"  {law.get('id')}: {law.get('name')} — {str(law.get('statement', ''))[:120]}"
        for law in laws
    ]
    hyp_lines = [
        f"  {h.get('id')}: {str(h.get('question', ''))[:120]}"
        for h in hyps
    ]
    return (
        "ESTABLISHED LAWS:\n" + "\n".join(law_lines) +
        "\n\nACTIVE HYPOTHESES:\n" + "\n".join(hyp_lines)
    )


def _parse_triage_report(report_path: Path) -> list[dict]:
    """Extract all non-discard items from a triage report (handles both 2- and 3-category formats)."""
    text = report_path.read_text()
    items = []
    # Grab SHALLOW READ and DEEP READ sections (DEEP READ is legacy; treat same as shallow)
    for section in re.finditer(
        r"^## (SHALLOW READ|DEEP READ)\b.*?\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    ):
        section_text = section.group(2)
        for item_m in re.finditer(
            r"- \*\*(.+?)\*\*\n\s+([^\n]+) — ([^\n]+)\n\s+`([^`]+)`(?:\n\s+<([^>]+)>)?",
            section_text,
        ):
            items.append({
                "title": item_m.group(1).strip(),
                "connection": item_m.group(2).strip(),
                "rationale": item_m.group(3).strip(),
                "file": item_m.group(4).strip(),
                "url": (item_m.group(5) or "").strip(),
            })
    return items


def _read_inbox_item(filename: str) -> dict:
    path = _ROOT / "inbox" / filename
    if not path.exists():
        return {}
    text = path.read_text()
    title_m = re.match(r"^#\s+(.+)$", text, re.MULTILINE)
    url_m = re.search(r"\*\*URL:\*\*\s*(.+)$", text, re.MULTILINE)
    source_m = re.search(r"\*\*Source:\*\*\s*(.+)$", text, re.MULTILINE)
    summary_m = re.search(r"## Summary\s*\n(.+?)(?=\n##|\Z)", text, re.DOTALL)
    type_m = re.search(r"\*\*Type:\*\*\s*(.+)$", text, re.MULTILINE)
    relevance_m = re.search(r"\*\*Relevance:\*\*\s*(.+)$", text, re.MULTILINE)
    hypothesis_m = re.search(r"\*\*Hypothesis:\*\*\s*(.+)$", text, re.MULTILINE)
    author_m = re.search(r"\*\*Author:\*\*\s*(.+)$", text, re.MULTILINE)
    return {
        "title": title_m.group(1).strip() if title_m else filename,
        "url": url_m.group(1).strip() if url_m else "",
        "source": source_m.group(1).strip() if source_m else "",
        "summary": summary_m.group(1).strip()[:600] if summary_m else "",
        "item_type": type_m.group(1).strip() if type_m else "feed",
        "relevance": relevance_m.group(1).strip() if relevance_m else "",
        "hypothesis": hypothesis_m.group(1).strip() if hypothesis_m else "",
        "author": author_m.group(1).strip() if author_m else "",
    }


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60]


def _output_filename(title: str) -> str:
    return f"{date.today().isoformat()}-{_slugify(title)}.md"


def _make_prompt(item: dict, inbox: dict, context: str) -> str:
    item_type = inbox.get("item_type", "feed")
    if item_type == "idea":
        return _make_idea_prompt(item, inbox, context)
    if item_type == "link":
        return _make_link_prompt(item, inbox, context)
    return _make_feed_prompt(item, inbox, context)


def _make_feed_prompt(item: dict, inbox: dict, context: str) -> str:
    title = inbox.get("title") or item["title"]
    source = inbox.get("source", "")
    url = inbox.get("url") or item["url"]
    summary = inbox.get("summary", "")
    source_ref = f"{source} — {url}".strip(" —") if source or url else url

    return f"""You are Humboldt, an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

You are doing a shallow read of a paper. Write a focused synthesis note, then decide whether this warrants a full M-003 deep read.

ESCALATION CRITERIA — apply strictly, escalation should be rare:
- This is a primary source presenting a sustained theoretical or empirical argument (not a benchmark, tool paper, or case study)
- It directly challenges, substantially extends, or provides foundational grounding for an established law or active hypothesis
- It introduces a mechanism genuinely absent from the current research inventory
- The pattern generalizes beyond the specific domain studied
If fewer than two of these apply, store as shallow only.

CURRENT RESEARCH CONTEXT:
{context}

PAPER:
Title: {title}
Source: {source_ref}
Triage note: {item['connection']} — {item['rationale']}

Abstract/Summary:
{summary}

Write a shallow read note in EXACTLY this format:

# {title}

**Source:** {source_ref}
**Date read:** {date.today().isoformat()}
**Connected to:** {item['connection']}
**Escalation:** [store-only OR escalate-to-deep]
**Escalation rationale:** [one sentence if escalating; leave blank if store-only]

## What this is

[1–2 sentences: type of work, main argument, primary domain.]

## What I took from it

[1–2 paragraphs: what is relevant to the new nature research agenda. Not a general summary — focus on the intersection with current laws and hypotheses. What does this confirm, challenge, or open?]

## Research connections

[bullet per relevant law or hypothesis: "- **ID:** one sentence on the connection"]

## Candidate laws or signals

[If this work suggests a pattern worth tracking as a candidate law, note it as "CL-Source-N: statement". Write "none" if nothing stands out.]"""


def _make_idea_prompt(item: dict, inbox: dict, context: str) -> str:
    title = inbox.get("title") or item["title"]
    # Strip leading "Idea: " prefix if present
    idea_text = re.sub(r"^Idea:\s*", "", title, flags=re.IGNORECASE)
    relevance = inbox.get("relevance", "")
    hypothesis = inbox.get("hypothesis", "")
    author = inbox.get("author", "")
    source = inbox.get("source", "Discord")
    connection = item.get("connection") or hypothesis or "none"

    return f"""You are Humboldt, an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

A collaborator has surfaced an idea in a research discussion. Engage with it as a research claim: evaluate its relationship to the current law/hypothesis inventory, identify what it opens or challenges, and decide whether it warrants a candidate law or hypothesis note.

ESCALATION: always store-only for ideas (ideas escalate by becoming candidate laws/hypotheses, not by triggering M-003 deep reads).

CURRENT RESEARCH CONTEXT:
{context}

IDEA (from {author or 'unknown'} via {source}):
{idea_text}

Relevance annotation: {relevance}
Connected hypothesis: {hypothesis or 'none annotated'}
Triage note: {item.get('connection', connection)} — {item.get('rationale', '')}

Write a shallow read note in EXACTLY this format:

# Idea: {idea_text[:80]}

**Source:** {source}{f' (by {author})' if author else ''}
**Date read:** {date.today().isoformat()}
**Connected to:** {connection}
**Escalation:** store-only
**Escalation rationale:**

## What this is

[1 sentence: what claim or pattern this idea proposes.]

## What I took from it

[1–2 paragraphs: how this idea connects to or challenges the current inventory. Is it a genuine addition, a restatement of something already captured, or a useful refinement? What does it open?]

## Research connections

[bullet per relevant law or hypothesis: "- **ID:** one sentence on the connection"]

## Candidate laws or signals

[If this idea contains a pattern worth promoting to a candidate law or hypothesis, state it. Format: "CL-Source-N: statement". Write "none" if it is already covered or not yet ripe.]"""


def _make_link_prompt(item: dict, inbox: dict, context: str) -> str:
    title = inbox.get("title") or item["title"]
    # Strip leading "Link: " prefix if present
    link_desc = re.sub(r"^Link:\s*", "", title, flags=re.IGNORECASE)
    url = inbox.get("url") or item["url"]
    relevance = inbox.get("relevance", "")
    hypothesis = inbox.get("hypothesis", "")
    author = inbox.get("author", "")
    source = inbox.get("source", "Discord")
    connection = item.get("connection") or hypothesis or "none"

    return f"""You are Humboldt, an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

A collaborator has shared an external link. You have only the title description and relevance annotation — the full document has not been fetched. Write a synthesis note based on what can be inferred, and decide whether this warrants a full M-003 deep read.

ESCALATION CRITERIA for links — apply strictly:
- The linked work is a sustained primary argument (book, long essay, foundational paper) not just a case study or news article
- The relevance annotation indicates it directly challenges or grounds a current law or hypothesis in a non-obvious way
- The link is to a primary source, not a secondary commentary or reference to Humboldt's own work

CURRENT RESEARCH CONTEXT:
{context}

LINK (shared by {author or 'unknown'} via {source}):
Description: {link_desc}
URL: {url}
Relevance annotation: {relevance}
Triage note: {item.get('connection', connection)} — {item.get('rationale', '')}

Note: the full document was not fetched. Base the note on the description and relevance annotation.

Write a shallow read note in EXACTLY this format:

# Link: {link_desc[:80]}

**Source:** {source}{f' (shared by {author})' if author else ''}
**URL:** {url}
**Date read:** {date.today().isoformat()}
**Connected to:** {connection}
**Escalation:** [store-only OR escalate-to-deep]
**Escalation rationale:** [one sentence if escalating; leave blank if store-only]

## What this is

[1–2 sentences: type of resource (essay/paper/book/post), apparent main argument, primary domain. Acknowledge the inference from description only.]

## What I took from it

[1–2 paragraphs: based on description and relevance annotation, what does this likely contribute to the new nature agenda? What does it open or confirm? Flag any uncertainty from not having read it.]

## Research connections

[bullet per relevant law or hypothesis: "- **ID:** one sentence on the connection"]

## Candidate laws or signals

[If the description suggests a pattern worth tracking, note it. Write "none" if nothing stands out from the description alone.]"""


def _parse_escalation(note: str) -> tuple[bool, str]:
    esc_m = re.search(r"\*\*Escalation:\*\*\s*(.+)$", note, re.MULTILINE | re.IGNORECASE)
    if not esc_m:
        return False, ""
    escalating = "escalate" in esc_m.group(1).lower()
    rationale = ""
    if escalating:
        rat_m = re.search(r"\*\*Escalation rationale:\*\*\s*(.+)$", note, re.MULTILINE)
        if rat_m:
            rationale = rat_m.group(1).strip()
    return escalating, rationale


def shallow_read(triage_path: str, dry_run: bool = False) -> None:
    from dotenv import load_dotenv
    import anthropic
    from daemon import costs

    load_dotenv(_ROOT / ".env")
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    report = Path(triage_path)
    if not report.exists():
        print(f"Triage report not found: {triage_path}")
        return

    items = _parse_triage_report(report)
    if not items:
        print("No non-discard items found in triage report.")
        return

    print(f"Shallow-reading {len(items)} items from {report.name}…")
    if dry_run:
        print("(dry-run — no files will be written)\n")

    laws = _load_laws()
    hyps = _load_hypotheses()
    context = _research_context(laws, hyps)
    out_dir = _ROOT / "bibliography" / "shallow-reads"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0
    escalations: list[dict] = []

    for i, item in enumerate(items, 1):
        inbox = _read_inbox_item(item["file"])
        title = inbox.get("title") or item["title"]
        outfile = out_dir / _output_filename(title)

        if outfile.exists():
            print(f"  [{i}/{len(items)}] skip (exists): {outfile.name}")
            skipped += 1
            continue

        print(f"  [{i}/{len(items)}] {title[:65]}…")

        if dry_run:
            print(f"    → would write: {outfile.name}")
            continue

        costs.check_budget()
        resp = client.messages.create(
            model=_MODEL,
            max_tokens=900,
            messages=[{"role": "user", "content": _make_prompt(item, inbox, context)}],
        )
        costs.log_call("shallow_read", _MODEL, resp.usage.input_tokens, resp.usage.output_tokens)

        note = resp.content[0].text.strip()
        outfile.write_text(note + "\n")
        written += 1

        escalating, rationale = _parse_escalation(note)
        if escalating:
            escalations.append({
                "title": title,
                "file": item["file"],
                "shallow_read": outfile.name,
                "rationale": rationale,
            })
            print(f"    → ESCALATE: {rationale or '(no rationale given)'}")

    print(f"\nDone: {written} written, {skipped} skipped → bibliography/shallow-reads/")

    if escalations:
        print(f"\nDeep read escalations ({len(escalations)}):")
        for e in escalations:
            print(f"  - {e['title'][:70]}")
            if e["rationale"]:
                print(f"    {e['rationale']}")
    else:
        print("\nNo escalations — all stored as shallow reads.")
