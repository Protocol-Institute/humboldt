"""
Perform shallow reads on inbox items from a triage report (funnel stage 3).

Humboldt reads each non-discard item and writes a synthesis note to
bibliography/shallow-reads/. Each read then does three things downstream
(redesign §5 stage 3 — "summary + embed + seeds/evidence + bibliography update"):

1. **Bibliography** — the item's entry (created at triage as ``listed``) is
   upgraded to ``read_depth: shallow`` with ``summary:`` pointing at the note,
   and linked to any laws the read connects to.
2. **Seed emission** — when the note surfaces something law-shaped, a seed lands
   in ``laws/seeds/`` for the induction sweep to consume. This is the fuel line
   into stage 5; without it induct only ever sees the 47 migrated seeds.
3. **Escalation** — whether to spend an Opus deep read on the source.

``kind: meta`` items (research methodology, epistemics) route down this same
path but emit **no seed**: their terminal output is a graph-change proposal
(§6.4), which is not built yet. They are tagged in the bibliography and
otherwise left alone.

Escalation criteria (applied strictly — should be rare):
- Primary source with a sustained argument, not just a measurement or case study
- Directly challenges, substantially extends, or grounds a law or open line of inquiry
- Introduces a mechanism not captured by current inventory
- Cross-domain generality beyond the specific case studied

Usage:
    python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md
    python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md --dry-run
    python3 -m agent.humboldt shallow-read --from-triage FILE --limit 3
"""

import os
import re
from datetime import date
from pathlib import Path

import yaml

from agent import bibliography as bib
from agent import funnel_context

_ROOT = Path(__file__).parent.parent
_MODEL = "claude-haiku-4-5-20251001"
_SEEDS_DIR = _ROOT / "laws" / "seeds"
_SEED_TYPES = {"insight", "observation", "question", "motif"}


def _parse_triage_report(report_path: Path) -> list[dict]:
    """Extract all non-discard items from a triage report.

    Tolerant of every format the report has had: the 3-category legacy layout
    (DEEP READ sections are treated as shallow), the 2-category layout, and the
    post-redesign layout that carries a trailing ``bib-NNNN · kind`` line.
    """
    text = report_path.read_text()
    items = []
    for section in re.finditer(
        r"^## (SHALLOW READ|DEEP READ)\b.*?\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    ):
        # Split the section into per-item blocks on the "- **Title**" bullet.
        blocks = re.split(r"\n(?=- \*\*)", section.group(2))
        for block in blocks:
            title_m = re.match(r"- \*\*(.+?)\*\*\s*$", block.strip().splitlines()[0]) \
                if block.strip() else None
            if not title_m:
                continue
            file_m = re.search(r"^\s+`([^`]+)`\s*$", block, re.MULTILINE)
            if not file_m:
                continue
            conn_m = re.search(r"^\s{2}(.+?) — (.+?)$", block, re.MULTILINE)
            url_m = re.search(r"^\s+<([^>]+)>\s*$", block, re.MULTILINE)
            tail_m = re.search(r"^\s+(bib-\d+|bib-pending)\s*·\s*(content|meta)\s*$",
                               block, re.MULTILINE)
            items.append({
                "title": title_m.group(1).strip(),
                "connection": conn_m.group(1).strip() if conn_m else "none",
                "rationale": conn_m.group(2).strip() if conn_m else "",
                "file": file_m.group(1).strip(),
                "url": (url_m.group(1).strip() if url_m else ""),
                "bib_id": (tail_m.group(1) if tail_m and tail_m.group(1) != "bib-pending"
                           else ""),
                "kind": tail_m.group(2) if tail_m else "content",
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


def _existing_note(out_dir: Path, title: str) -> Path | None:
    """Find an already-written note for this title under ANY date prefix.

    The skip check used to be ``_output_filename(title).exists()``, which embeds
    ``date.today()`` — so it only ever matched notes written *today*. Any run that
    crossed midnight (a long backlog sweep, or one paused and resumed the next day)
    silently re-read and re-paid for every item it had already done, and left a
    second copy of each note differing only in date prefix. Found 2026-09-02 with 45
    duplicated slugs on disk, most dating back to the June sweeps.

    Matching on the slug under a fixed-width date glob makes the skip date-agnostic.
    """
    return next(iter(sorted(out_dir.glob(f"????-??-??-{_slugify(title)}.md"))), None)


# ── Prompt construction ───────────────────────────────────────────────────────

_SEED_BLOCK = """## Seed

**Seed title:** [a short name for the fragment, or exactly "none"]
**Seed type:** [insight | observation | question | motif]
**Seed text:** [2–4 sentences stating the law-shaped fragment: the regularity, \
the condition under which it holds, and why it might generalize. Self-contained — \
an induction sweep will read this without the source in front of it.]"""

_SEED_GUIDANCE = """SEED EMISSION — the fuel line into the induction sweep:
A seed is a law-shaped fragment: a candidate regularity, a mechanism hint, a
sharp question, or a recurring motif worth tracking. It is NOT yet a law — it
needs no falsification condition, no cross-domain evidence, no mechanism proof.
Emit a seed when the read leaves you with something general worth returning to.
Write "none" when the read is a competent piece of work with nothing that
generalizes beyond its own case, or when the fragment merely restates a law or
seed already in the inventory above. Roughly: most reads produce no seed."""

_META_BLOCK = """## Method note

[2–4 sentences: what this suggests about how research should be conducted, \
evaluated, or organized. This is a meta read — it feeds the behavior graph, not \
the law inventory, so do not propose a candidate law here.]"""


def _make_prompt(item: dict, inbox: dict, context: str) -> str:
    item_type = inbox.get("item_type", "feed")
    if item_type == "idea":
        return _make_idea_prompt(item, inbox, context)
    if item_type == "link":
        return _make_link_prompt(item, inbox, context)
    return _make_feed_prompt(item, inbox, context)


def _tail_sections(item: dict) -> str:
    """Meta reads close with a method note; content reads close with a seed."""
    return _META_BLOCK if item.get("kind") == "meta" else _SEED_BLOCK


def _tail_guidance(item: dict) -> str:
    if item.get("kind") == "meta":
        return ("This item is tagged META — it concerns how research is done, not "
                "protocolized systems themselves. Do not emit a seed or propose a law.")
    return _SEED_GUIDANCE


def _make_feed_prompt(item: dict, inbox: dict, context: str) -> str:
    title = inbox.get("title") or item["title"]
    source = inbox.get("source", "")
    url = inbox.get("url") or item["url"]
    summary = inbox.get("summary", "")
    source_ref = f"{source} — {url}".strip(" —") if source or url else url

    return f"""You are Humboldt, an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

You are doing a shallow read of a paper. Write a focused synthesis note, then decide whether this warrants a full deep read.

ESCALATION CRITERIA — apply strictly, escalation should be rare:
- This is a primary source presenting a sustained theoretical or empirical argument (not a benchmark, tool paper, or case study)
- It directly challenges, substantially extends, or provides foundational grounding for a law or open line of inquiry
- It introduces a mechanism genuinely absent from the current research inventory
- The pattern generalizes beyond the specific domain studied
If fewer than two of these apply, store as shallow only.

{_tail_guidance(item)}

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
**Kind:** {item.get('kind', 'content')}
**Escalation:** [store-only OR escalate-to-deep]
**Escalation rationale:** [one sentence if escalating; leave blank if store-only]

## What this is

[1–2 sentences: type of work, main argument, primary domain.]

## What I took from it

[1–2 paragraphs: what is relevant to the new nature research agenda. Not a general summary — focus on the intersection with the current law inventory and open lines of inquiry. What does this confirm, challenge, or open?]

## Research connections

[bullet per relevant law or seed: "- **ID:** one sentence on the connection". Write "- none" if there is no real connection.]

{_tail_sections(item)}"""


def _make_idea_prompt(item: dict, inbox: dict, context: str) -> str:
    title = inbox.get("title") or item["title"]
    idea_text = re.sub(r"^Idea:\s*", "", title, flags=re.IGNORECASE)
    relevance = inbox.get("relevance", "")
    hypothesis = inbox.get("hypothesis", "")
    author = inbox.get("author", "")
    source = inbox.get("source", "Discord")
    connection = item.get("connection") or hypothesis or "none"

    return f"""You are Humboldt, an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

A collaborator has surfaced an idea in a research discussion. Engage with it as a research claim: evaluate its relationship to the current law inventory and seed pool, identify what it opens or challenges, and decide whether it is law-shaped enough to seed.

ESCALATION: always store-only for ideas (an idea escalates by becoming a seed and then a law, not by triggering a deep read).

{_tail_guidance(item)}

CURRENT RESEARCH CONTEXT:
{context}

IDEA (from {author or 'unknown'} via {source}):
{idea_text}

Relevance annotation: {relevance}
Connected law/seed: {hypothesis or 'none annotated'}
Triage note: {item.get('connection', connection)} — {item.get('rationale', '')}

Write a shallow read note in EXACTLY this format:

# Idea: {idea_text[:80]}

**Source:** {source}{f' (by {author})' if author else ''}
**Date read:** {date.today().isoformat()}
**Connected to:** {connection}
**Kind:** {item.get('kind', 'content')}
**Escalation:** store-only
**Escalation rationale:**

## What this is

[1 sentence: what claim or pattern this idea proposes.]

## What I took from it

[1–2 paragraphs: how this idea connects to or challenges the current inventory. Is it a genuine addition, a restatement of something already captured, or a useful refinement? What does it open?]

## Research connections

[bullet per relevant law or seed: "- **ID:** one sentence on the connection". Write "- none" if there is no real connection.]

{_tail_sections(item)}"""


def _make_link_prompt(item: dict, inbox: dict, context: str) -> str:
    title = inbox.get("title") or item["title"]
    link_desc = re.sub(r"^Link:\s*", "", title, flags=re.IGNORECASE)
    url = inbox.get("url") or item["url"]
    relevance = inbox.get("relevance", "")
    hypothesis = inbox.get("hypothesis", "")
    author = inbox.get("author", "")
    source = inbox.get("source", "Discord")
    connection = item.get("connection") or hypothesis or "none"

    return f"""You are Humboldt, an artificial researcher investigating laws of protocolized and artificial systems — the "new nature."

A collaborator has shared an external link. You have only the title description and relevance annotation — the full document has not been fetched. Write a synthesis note based on what can be inferred, and decide whether this warrants a full deep read.

ESCALATION CRITERIA for links — apply strictly:
- The linked work is a sustained primary argument (book, long essay, foundational paper) not just a case study or news article
- The relevance annotation indicates it directly challenges or grounds a current law or open line of inquiry in a non-obvious way
- The link is to a primary source, not a secondary commentary or reference to Humboldt's own work

{_tail_guidance(item)}

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
**Kind:** {item.get('kind', 'content')}
**Escalation:** [store-only OR escalate-to-deep]
**Escalation rationale:** [one sentence if escalating; leave blank if store-only]

## What this is

[1–2 sentences: type of resource (essay/paper/book/post), apparent main argument, primary domain. Acknowledge the inference from description only.]

## What I took from it

[1–2 paragraphs: based on description and relevance annotation, what does this likely contribute to the new nature agenda? What does it open or confirm? Flag any uncertainty from not having read it.]

## Research connections

[bullet per relevant law or seed: "- **ID:** one sentence on the connection". Write "- none" if there is no real connection.]

{_tail_sections(item)}"""


# ── Note parsing ──────────────────────────────────────────────────────────────

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


def _parse_connections(note: str, fallback: str) -> list[str]:
    """Law/seed tokens the note declares, from its 'Connected to:' header."""
    m = re.search(r"^\*\*Connected to:\*\*\s*(.+)$", note, re.MULTILINE)
    raw = m.group(1).strip() if m else fallback
    return [t for t in re.split(r"[,\s]+", raw or "") if t]


def _parse_seed(note: str) -> dict | None:
    """Extract the seed block from a shallow-read note, if it declared one."""
    title_m = re.search(r"^\*\*Seed title:\*\*\s*(.*)$", note, re.MULTILINE)
    text_m = re.search(r"^\*\*Seed text:\*\*\s*(.+?)(?=\n\*\*|\n##|\Z)",
                       note, re.MULTILINE | re.DOTALL)
    if not title_m or not text_m:
        return None
    title = title_m.group(1).strip().strip("[]").strip()
    text = " ".join(text_m.group(1).split()).strip().strip("[]").strip()
    if not title or title.lower() in {"none", "n/a", "-"} or not text:
        return None
    if text.lower().startswith("2–4 sentences") or text.lower() in {"none", "n/a"}:
        return None
    type_m = re.search(r"^\*\*Seed type:\*\*\s*(.*)$", note, re.MULTILINE)
    stype = (type_m.group(1).strip().strip("[]").lower() if type_m else "insight")
    stype = stype if stype in _SEED_TYPES else "insight"
    return {"title": title, "text": text, "type": stype}


def _write_seed(seed: dict, source_path: str, connections: list[str]) -> str:
    """Write one seed YAML into laws/seeds/. Returns the seed id.

    Seeds are plain PyYAML (unlike law records, they are not ruamel-managed and
    carry no comments). Shape follows laws/seeds/README.md and the migrated
    seed-001..047 files.
    """
    _SEEDS_DIR.mkdir(parents=True, exist_ok=True)
    seed_id = funnel_context.next_seed_id()
    record = {
        "id": seed_id,
        "title": seed["title"],
        "text": seed["text"],
        "source": source_path,
        "origin": "shallow-read",
        "surfaced": date.today().isoformat(),
        "type": seed["type"],
        "connections": connections,
        "status": "open",
    }
    path = _SEEDS_DIR / f"{seed_id}-{_slugify(seed['title'])}.yaml"
    path.write_text(yaml.dump(record, sort_keys=False, allow_unicode=True,
                              default_flow_style=False, width=100))
    return seed_id


def _update_bibliography(item: dict, inbox: dict, note_path: Path,
                         connections: list[str]) -> tuple[str, list[str]]:
    """Upgrade the item's entry to ``read_depth: shallow`` and link its laws.

    Matching goes through ``bibliography.upsert`` — the same url/title dedup the
    triage stage used — so a read never forks a second entry for a source that is
    already listed. Returns ``(bib_id, mapped_law_ids)``.
    """
    entries = bib.load()
    current_ids = funnel_context.current_law_ids()
    mapped, raw = bib.map_law_tokens(connections, current_ids)
    source = inbox.get("source", "")
    url = inbox.get("url") or item.get("url") or None
    entry = bib.upsert(
        entries,
        title=inbox.get("title") or item["title"],
        url=url,
        year=bib.year_from(url, source, item.get("file")),
        encountered="discord" if inbox.get("author") else "feed",
        read_depth="shallow",
        kind=item.get("kind", "content"),
        summary=str(note_path.relative_to(_ROOT)),
        laws=mapped,
        connected_raw=raw,
    )
    bib.save(entries)
    # link_law is the canonical forward-index write; after the upsert above it is
    # a no-op for links already merged, and catches any law id that arrived only
    # in the note's own "Connected to:" header.
    for law_id in mapped:
        bib.link_law(entry["id"], law_id)
    return entry["id"], mapped


# ── Entry point ───────────────────────────────────────────────────────────────

def shallow_read(triage_path: str, dry_run: bool = False,
                 limit: int | None = None) -> None:
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
    if limit:
        items = items[:limit]

    print(f"Shallow-reading {len(items)} items from {report.name}…")
    if dry_run:
        print("(dry-run — no files will be written)\n")

    context = funnel_context.research_context()
    out_dir = _ROOT / "bibliography" / "shallow-reads"
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0
    escalations: list[dict] = []
    seeds_emitted: list[str] = []
    bib_updated: list[str] = []

    for i, item in enumerate(items, 1):
        inbox = _read_inbox_item(item["file"])
        title = inbox.get("title") or item["title"]
        outfile = out_dir / _output_filename(title)

        prior = _existing_note(out_dir, title)
        if prior is not None:
            print(f"  [{i}/{len(items)}] skip (exists): {prior.name}")
            skipped += 1
            continue

        kind_tag = " [meta]" if item.get("kind") == "meta" else ""
        print(f"  [{i}/{len(items)}]{kind_tag} {title[:65]}…")

        if dry_run:
            print(f"    → would write: {outfile.name}")
            continue

        costs.check_budget()
        resp = client.messages.create(
            model=_MODEL,
            max_tokens=1000,
            messages=[{"role": "user", "content": _make_prompt(item, inbox, context)}],
        )
        costs.log_call("shallow_read", _MODEL, resp.usage.input_tokens, resp.usage.output_tokens)

        note = resp.content[0].text.strip()
        outfile.write_text(note + "\n")
        written += 1

        # Bibliography: listed → shallow, summary path, law links.
        connections = _parse_connections(note, item.get("connection", ""))
        try:
            bib_id, mapped = _update_bibliography(item, inbox, outfile, connections)
            bib_updated.append(bib_id)
            print(f"    → bibliography: {bib_id} read_depth=shallow"
                  + (f" · laws {', '.join(mapped)}" if mapped else ""))
        except Exception as e:  # noqa: BLE001 — a bib failure must not lose the note
            bib_id, mapped = item.get("bib_id", ""), []
            print(f"    ! bibliography update failed: {e}")

        # Seeds: content items only (meta reads terminate in graph-change
        # proposals, which are not built yet — §6.4).
        if item.get("kind") != "meta":
            seed = _parse_seed(note)
            if seed:
                seed_id = _write_seed(
                    seed,
                    source_path=str(outfile.relative_to(_ROOT)),
                    connections=mapped or [c for c in connections
                                           if not c.lower().startswith("none")],
                )
                seeds_emitted.append(seed_id)
                print(f"    → seed {seed_id}: {seed['title'][:60]}")

        # Update people model for discord items (feed items have no author)
        author = inbox.get("author", "")
        if author:
            from daemon import people as ppl
            from agent.person_notebook import generate_person_notebook_entry
            crossed = ppl.record_contributions_for_authors(
                author_string=author,
                decision="shallow",
                item_type=inbox.get("item_type", "unknown"),
                title=title,
                connection=item.get("connection", ""),
            )
            for handle in crossed:
                print(f"    → person threshold crossed: @{handle} — generating notebook entry…")
                out = generate_person_notebook_entry(handle)
                if out:
                    print(f"    → written: {out}")

        # Delete source inbox file — content is safely in the shallow-read note
        src = _ROOT / "inbox" / item["file"]
        if src.exists():
            src.unlink()

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
    print(f"  bibliography entries upgraded to shallow: {len(bib_updated)}")
    print(f"  seeds emitted → laws/seeds/: {len(seeds_emitted)}"
          + (f" ({', '.join(seeds_emitted)})" if seeds_emitted else ""))

    if escalations:
        print(f"\nDeep read escalations ({len(escalations)}):")
        for e in escalations:
            print(f"  - {e['title'][:70]}")
            if e["rationale"]:
                print(f"    {e['rationale']}")
    else:
        print("\nNo escalations — all stored as shallow reads.")

    if dry_run or written == 0:
        return

    # Append to pre-notebook log
    from agent.pre_notebook import append as pn_append
    escalation_titles = [e["title"] for e in escalations]
    summary = (
        f"Shallow-read {written} items from {Path(triage_path).name}: "
        f"{len(escalations)} escalation(s), {len(seeds_emitted)} seed(s) emitted, "
        f"{len(bib_updated)} bibliography entries deepened."
        + (f" Escalated: {'; '.join(escalation_titles[:3])}." if escalation_titles else "")
    )
    pn_append(
        process="shallow_read",
        summary=summary,
        detail={
            "written": written,
            "skipped": skipped,
            "escalations": escalation_titles,
            "seeds": seeds_emitted,
            "bibliography": len(bib_updated),
            "triage_source": Path(triage_path).name,
        },
    )

    # Re-ingest so shallow-read notes are immediately searchable. Pinecone writes
    # are a paused side-effect like any other (session 23) — skip while paused and
    # let the operator run `humboldt ingest` after unpausing.
    from daemon import pause as pz
    if pz.is_paused():
        print(f"\nPaused until {pz.paused_until()} — skipping Pinecone ingest. "
              "Run `humboldt ingest` after unpausing.")
        return
    print("\nRe-ingesting humboldt namespace…")
    from agent.ingest import ingest_all
    ingest_all(verbose=True)
