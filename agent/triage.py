"""
Triage inbox items against the live law inventory and seed pool (funnel stage 2).

triage_feed: scores inbox/feed-*.md (arXiv papers)
triage_discord: scores inbox/discord-*.md (ideas and links captured from Discord)

Decisions: discard | shallow
- discard: not meaningfully relevant, or duplicate of existing documented knowledge
- shallow: relevant — route to shallow-read pipeline

Every non-discard item is also tagged ``content`` or ``meta`` (redesign §5):
object-level material about protocolized systems vs. material about how research
itself is done. Both route down the same read paths; meta items terminate in
graph-change proposals rather than seeds, so the tag has to be set here, at the
point of entry, and carried on the bibliography entry.

Triage-in is where a source enters the canonical bibliography: each non-discard
item gets (or upgrades to) a ``bib-NNNN`` entry at ``read_depth: listed``. Later
reads deepen the same entry rather than creating a second one.

Discord items are pre-filtered by the capture pipeline, so the discard bar is higher.

Produces a ranked report for operator review. Does not modify inbox items.

Usage:
    python3 -m agent.humboldt triage-feed [--output FILE] [--limit N] [--dry-run]
    python3 -m agent.humboldt triage-discord [--output FILE] [--limit N] [--dry-run]
"""

import os
import re
from datetime import date
from pathlib import Path

from agent import bibliography as bib
from agent import funnel_context

_ROOT = Path(__file__).parent.parent
_TRIAGE_MODEL = "claude-haiku-4-5-20251001"
_BATCH_SIZE = 15


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


_DECISION_LINE = re.compile(
    r"\[(\d+)\]\s+(discard|shallow|deep)\s*\|\s*(content|meta)\s*\|\s*([^|]*?)\s*\|\s*(.+)",
    re.IGNORECASE,
)
# Pre-redesign reports/responses had no KIND column; accept them and default to content.
_DECISION_LINE_LEGACY = re.compile(
    r"\[(\d+)\]\s+(discard|shallow|deep)\s*\|\s*([^|]*?)\s*\|\s*(.+)",
    re.IGNORECASE,
)


def _parse_decisions(text: str, items: list[dict]) -> list[dict]:
    results = []
    for line in text.strip().splitlines():
        m = _DECISION_LINE.match(line.strip())
        if m:
            idx, decision, kind, connection, rationale = (
                int(m.group(1)) - 1, m.group(2).lower(), m.group(3).lower(),
                m.group(4).strip(), m.group(5).strip(),
            )
        else:
            m = _DECISION_LINE_LEGACY.match(line.strip())
            if not m:
                continue
            idx, decision, kind, connection, rationale = (
                int(m.group(1)) - 1, m.group(2).lower(), "content",
                m.group(3).strip(), m.group(4).strip(),
            )
        if not (0 <= idx < len(items)):
            continue
        results.append({
            "file": items[idx]["file"],
            "title": items[idx]["title"],
            "url": items[idx]["url"],
            "decision": decision,
            "kind": kind if kind in bib.KINDS else "content",
            "connection": connection,
            "rationale": rationale,
        })
    return results


_OUTPUT_SPEC = """For each item below, output EXACTLY one line:
[N] DECISION | KIND | CONNECTION | RATIONALE

- DECISION: discard | shallow
- KIND: content | meta
  content = about protocolized or artificial systems themselves — the object level
  meta    = about how research is done: methodology, epistemics, evaluation
            practice, how good researchers work. Meta items are NOT discards; they
            route down the same read path and feed the behavior graph instead of
            the law inventory.
- CONNECTION: law or seed ids most relevant, e.g. "L-003, seed-041" (or "none")
- RATIONALE: one sentence, max 15 words"""


def _triage_batch(items: list[dict], context: str, client) -> list[dict]:
    item_block = ""
    for i, item in enumerate(items):
        item_block += (
            f"\n[{i + 1}] {item['title']}\n"
            f"Abstract: {item['summary'][:300]}\n"
        )

    prompt = f"""You are triaging research papers for an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

{context}

{_OUTPUT_SPEC}

DECISION guidance:
  discard = not meaningfully relevant to any law, open line of inquiry, or seed
  shallow = relevant — worth a synthesis note (all relevant papers go here; depth
            decisions happen during reading)

{item_block}
Output only the numbered lines."""

    from daemon import costs
    costs.check_budget()

    resp = client.messages.create(
        model=_TRIAGE_MODEL,
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    costs.log_call("triage_feed", _TRIAGE_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _parse_decisions(resp.content[0].text, items)


def _build_report(all_results: list[dict], n_items: int, label: str = "Feed") -> str:
    today = date.today().isoformat()
    by = {"shallow": [], "discard": []}
    for r in all_results:
        bucket = r["decision"] if r["decision"] in by else "shallow"
        by[bucket].append(r)

    n_meta = sum(1 for r in by["shallow"] if r.get("kind") == "meta")
    counts = (f"{len(by['shallow'])} shallow ({n_meta} meta), "
              f"{len(by['discard'])} discard")
    lines = [
        f"# {label} Triage Report — {today}",
        f"\n{n_items} items triaged: {counts}\n",
    ]
    for decision, heading in [("shallow", "SHALLOW READ"), ("discard", "DISCARD")]:
        group = by.get(decision, [])
        if not group:
            continue
        lines.append(f"\n## {heading} ({len(group)})\n")
        for r in group:
            lines.append(f"- **{r['title']}**")
            lines.append(f"  {r['connection']} — {r['rationale']}")
            lines.append(f"  `{r['file']}`")
            if r["url"]:
                lines.append(f"  <{r['url']}>")
            # Machine-readable tail: bibliography id + content/meta tag, which
            # the shallow-read stage reads back rather than re-deriving. Discards
            # never enter the bibliography (§4.1) and so carry no tail.
            if decision != "discard":
                lines.append(f"  {r.get('bib_id', 'bib-pending')} · "
                             f"{r.get('kind', 'content')}")
            lines.append("")
    return "\n".join(lines)


def _record_bibliography(results: list[dict], encountered: str, dry_run: bool) -> int:
    """Create/upgrade a ``listed`` bibliography entry for every non-discard item.

    Mutates ``results`` in place, stamping each with its ``bib_id`` so the report
    carries it downstream. Discards never enter the bibliography (§4.1: one entry
    per source engaged *past* triage-discard).
    """
    keep = [r for r in results if r["decision"] != "discard"]
    if not keep:
        return 0
    entries = bib.load()
    current_ids = funnel_context.current_law_ids()
    for r in keep:
        raw_tokens = re.split(r"[,\s]+", r.get("connection", ""))
        mapped, raw = bib.map_law_tokens(raw_tokens, current_ids)
        entry = bib.upsert(
            entries,
            title=r["title"],
            url=r.get("url") or None,
            year=bib.year_from(r.get("url"), r.get("file")),
            encountered=encountered,
            read_depth="listed",
            kind=r.get("kind", "content"),
            laws=mapped,
            connected_raw=raw,
        )
        r["bib_id"] = entry["id"]
    if not dry_run:
        bib.save(entries)
    return len(keep)


def _load_discord_items() -> list[dict]:
    inbox_dir = _ROOT / "inbox"
    items = []
    for f in sorted(inbox_dir.glob("discord-*.md")):
        text = f.read_text()
        title_m = re.match(r"^#\s+(.+)$", text, re.MULTILINE)
        type_m = re.search(r"\*\*Type:\*\*\s*(.+)$", text, re.MULTILINE)
        relevance_m = re.search(r"\*\*Relevance:\*\*\s*(.+)$", text, re.MULTILINE)
        hypothesis_m = re.search(r"\*\*Hypothesis:\*\*\s*(.+)$", text, re.MULTILINE)
        url_m = re.search(r"\*\*URL:\*\*\s*(.+)$", text, re.MULTILINE)
        author_m = re.search(r"\*\*Author:\*\*\s*(.+)$", text, re.MULTILINE)
        items.append({
            "file": f.name,
            "title": title_m.group(1).strip() if title_m else f.stem,
            "item_type": (type_m.group(1).strip() if type_m else "unknown"),
            "relevance": relevance_m.group(1).strip() if relevance_m else "",
            "hypothesis": hypothesis_m.group(1).strip() if hypothesis_m else "",
            "url": url_m.group(1).strip() if url_m else "",
            "author": author_m.group(1).strip() if author_m else "",
        })
    return items


def _triage_discord_batch(items: list[dict], context: str, client) -> list[dict]:
    item_block = ""
    for i, item in enumerate(items):
        parts = []
        if item["hypothesis"]:
            parts.append(f"Tagged: {item['hypothesis']}")
        if item["relevance"]:
            parts.append(item["relevance"][:150])
        annotation = " — ".join(parts) if parts else "(no annotation)"
        item_block += (
            f"\n[{i + 1}] [{item['item_type']}] {item['title']}\n"
            f"Annotation: {annotation}\n"
        )

    prompt = f"""You are triaging Discord-captured ideas and links for an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

{context}

These items were pre-filtered by a capture pipeline, so most are genuinely relevant. Discard only if:
- The item is clearly tangential despite its annotation
- It is a duplicate of knowledge already well-represented in the law inventory or seed pool

Do NOT discard an item merely because it concerns research method or epistemics — tag it `meta` and keep it.

{_OUTPUT_SPEC}

{item_block}
Output only the numbered lines."""

    from daemon import costs
    costs.check_budget()

    resp = client.messages.create(
        model=_TRIAGE_MODEL,
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    costs.log_call("triage_discord", _TRIAGE_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _parse_decisions(resp.content[0].text, items)


def _run(
    kind_label: str,
    items: list[dict],
    batch_fn,
    encountered: str,
    process: str,
    output_path: str | None,
    limit: int | None,
    dry_run: bool,
) -> None:
    from dotenv import load_dotenv
    import anthropic

    load_dotenv(_ROOT / ".env")

    if not items:
        print(f"No {kind_label.lower()} items in inbox/.")
        return
    if limit:
        items = items[:limit]

    print(f"Triaging {len(items)} {kind_label.lower()} items against the law "
          f"inventory and seed pool…")
    if dry_run:
        print("(dry-run — model is called, no bibliography or report writes)")

    context = funnel_context.research_context()
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    all_results: list[dict] = []
    for i in range(0, len(items), _BATCH_SIZE):
        batch = items[i: i + _BATCH_SIZE]
        print(f"  Scoring {i + 1}–{min(i + _BATCH_SIZE, len(items))} of {len(items)}…")
        all_results.extend(batch_fn(batch, context, client))

    n_bib = _record_bibliography(all_results, encountered, dry_run)
    report = _build_report(all_results, len(items), label=kind_label)

    if output_path and not dry_run:
        Path(output_path).write_text(report)
        print(f"\nReport written to: {output_path}")
    else:
        print("\n" + report)

    n_shallow = sum(1 for r in all_results if r["decision"] == "shallow")
    n_discard = sum(1 for r in all_results if r["decision"] == "discard")
    n_meta = sum(1 for r in all_results
                 if r["decision"] != "discard" and r.get("kind") == "meta")
    print(f"{n_bib} bibliography entr{'y' if n_bib == 1 else 'ies'} "
          f"{'would be ' if dry_run else ''}created/updated at read_depth: listed.")

    if dry_run:
        return

    try:
        from agent.pre_notebook import append as pn_append
        pn_append(
            process=process,
            summary=(f"Triaged {len(items)} {kind_label.lower()} items: {n_shallow} shallow "
                     f"({n_meta} meta), {n_discard} discard; {n_bib} bibliography entries."),
            detail={"shallow": n_shallow, "discard": n_discard, "meta": n_meta,
                    "bibliography": n_bib, "total": len(items)},
        )
    except Exception:
        pass


def triage_discord(output_path: str | None = None, limit: int | None = None,
                   dry_run: bool = False) -> None:
    _run("Discord", _load_discord_items(), _triage_discord_batch,
         encountered="discord", process="triage_discord",
         output_path=output_path, limit=limit, dry_run=dry_run)


def triage_feed(output_path: str | None = None, limit: int | None = None,
                dry_run: bool = False) -> None:
    _run("Feed", _load_feed_items(), _triage_batch,
         encountered="feed", process="triage_feed",
         output_path=output_path, limit=limit, dry_run=dry_run)
