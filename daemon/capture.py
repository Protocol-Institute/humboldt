"""Discord conversation capture — extracts ideas and references into inbox/.

Runs after every batch of Discord messages Humboldt reads, using a cheap
Haiku call to identify:
  1. Ideas / arguments that bear on active hypotheses or challenge current laws
  2. External papers, articles, or URLs cited by participants

Captured items are saved to inbox/ as markdown files, ready for Humboldt
to process at the start of the next research session.
"""

import json
import logging
import os
import re
from datetime import datetime
from pathlib import Path

from anthropic import AsyncAnthropic

from . import costs

logger = logging.getLogger("humboldt.capture")

_ROOT = Path(__file__).parent.parent
_INBOX_DIR = _ROOT / "inbox"
_FAST_MODEL = "claude-haiku-4-5-20251001"

# Track URLs already saved this daemon session to avoid duplicates
_saved_urls: set[str] = set()


def _load_research_context() -> tuple[list[str], list[str]]:
    """Load the current law inventory for the extraction prompt."""
    hypotheses: list[str] = []
    laws: list[str] = []
    try:
        from agent import laws as laws_mod
        for law in laws_mod.load_all():
            title = law.get("title", "")
            stmt = str(law.get("statement") or "").strip().replace("\n", " ")
            first_sentence = (stmt.split(".")[0] + ".") if "." in stmt else stmt[:120]
            entry = f"{law.get('id')}: {title} — {first_sentence[:120]}"
            hypotheses.append(entry)
            laws.append(f"{law.get('id')}: {title}")
    except Exception:
        pass

    return hypotheses, laws


async def extract_captures(
    messages: list[dict],
    source_channel: str = "#new-nature",
) -> list[dict]:
    """
    Scan a batch of Discord messages for capturable research material.

    Uses Haiku to identify:
      - IDEAS: arguments or observations bearing on active hypotheses or laws
      - LINKS: external papers / articles / URLs cited by participants

    Parameters
    ----------
    messages:
        List of {"author": str, "content": str} dicts, in chronological order.
    source_channel:
        Channel name for logging / file metadata.

    Returns
    -------
    List of capture dicts:
        {
            "type": "idea" | "link",
            "summary": str,       # one-sentence description
            "url": str | None,    # for links
            "author": str,        # Discord username
            "hypothesis": str | None,  # e.g. "H-001" if matched
            "relevance": str,     # one sentence
        }
    Returns [] if nothing is worth capturing.
    """
    if not messages:
        return []

    hypotheses, laws = _load_research_context()
    hyp_str = "\n".join(f"- {h}" for h in hypotheses) if hypotheses else "(none active)"
    law_str = "\n".join(f"- {l}" for l in laws) if laws else "(none established)"

    # Cap at 15 messages per call to keep output tokens bounded
    # (caller should chunk larger batches if needed)
    convo = "\n".join(
        f"{m['author']}: {m['content'][:400]}" for m in messages[-15:]
    )

    prompt = f"""You are a research capture filter for Humboldt, an artificial researcher at the Protocol Institute.

Active hypotheses:
{hyp_str}

Current law inventory:
{law_str}

Discord conversation from {source_channel}:
{convo}

Identify two types of capturable items:
1. IDEAS — arguments, observations, framings, or claims that directly bear on the hypotheses or challenge/support the laws above. Skip general chit-chat; only capture if genuinely relevant to the research agenda.
2. LINKS — external papers, articles, books, blog posts, or URLs that participants cite and that could be relevant to the research.

Return a JSON array. Each item:
{{
  "type": "idea" | "link",
  "summary": "<one sentence describing the idea or resource>",
  "url": "<URL string, or null if not a link>",
  "author": "<discord username who raised it>",
  "hypothesis": "<H-ID if this directly relates to a specific hypothesis, or null>",
  "relevance": "<one sentence: why this matters to the research>"
}}

Rules:
- Only include items with clear research relevance. If in doubt, omit.
- For links: include the URL exactly as it appears in the conversation.
- For ideas: summarize the argument in your own words, not a quote.
- If nothing is worth capturing, return: []

Return only valid JSON — no markdown fences, no commentary."""

    costs.check_budget()
    try:
        async with AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"]) as client:
            resp = await client.messages.create(
                model=_FAST_MODEL,
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}],
            )
        costs.log_call(
            "discord_capture",
            _FAST_MODEL,
            resp.usage.input_tokens,
            resp.usage.output_tokens,
        )
        raw = resp.content[0].text.strip()
        # Strip markdown fences in case the model wraps anyway
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```\s*$", "", raw)
        captures = json.loads(raw)
        if not isinstance(captures, list):
            logger.warning(f"Capture extraction returned non-list: {raw[:80]}")
            return []
        logger.info(
            f"Capture extraction: {len(captures)} item(s) from {len(messages)} message(s)"
        )
        return captures
    except json.JSONDecodeError as e:
        logger.warning(f"Capture JSON parse error: {e} — raw: {raw[:120]}")
        return []
    except Exception as e:
        logger.warning(f"Capture extraction failed: {e}")
        return []


def save_capture(item: dict, source_channel: str = "#new-nature") -> Path | None:
    """
    Write a single captured item to inbox/ as a markdown file.

    Returns the path written, or None if the item was skipped (duplicate URL).
    """
    global _saved_urls

    url = item.get("url") or None
    item_type = item.get("type", "idea")
    summary = (item.get("summary") or "untitled").strip()

    # Deduplicate links: check in-session cache first, then scan inbox/ files
    if url:
        if url in _saved_urls:
            logger.debug(f"Capture dedup (session): {url}")
            return None
        for existing in _INBOX_DIR.glob("discord-link-*.md"):
            try:
                if url in existing.read_text():
                    logger.debug(f"Capture dedup (file): {url} in {existing.name}")
                    _saved_urls.add(url)
                    return None
            except Exception:
                pass

    _INBOX_DIR.mkdir(exist_ok=True)
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H%M")

    # Build filename slug from summary
    slug = summary[:50].lower()
    for ch in " /\\:*?\"<>|',.()\n\t":
        slug = slug.replace(ch, "-")
    slug = re.sub(r"-+", "-", slug).strip("-")[:40]

    fname = f"discord-{item_type}-{date_str}-{time_str}-{slug}.md"
    path = _INBOX_DIR / fname

    author = item.get("author") or "unknown"
    hypothesis = item.get("hypothesis") or None
    relevance = item.get("relevance") or ""

    lines = [
        f"# {item_type.capitalize()}: {summary}\n",
        f"**Source:** Discord {source_channel}",
        f"**Author:** {author}",
        f"**Date:** {date_str}",
        f"**Type:** {item_type}",
    ]
    if hypothesis:
        lines.append(f"**Hypothesis:** {hypothesis}")
    if url:
        lines.append(f"**URL:** {url}")
    lines.append(f"**Relevance:** {relevance}")
    lines.append("")  # trailing newline

    path.write_text("\n".join(lines) + "\n")
    logger.info(f"Captured {item_type} from {author}: {summary[:60]}")

    if url:
        _saved_urls.add(url)

    return path


async def run_capture(
    messages: list[dict],
    source_channel: str = "#new-nature",
    chunk_size: int = 15,
) -> int:
    """
    Convenience wrapper: extract + save all captures from a message batch.

    Large batches are split into chunks of chunk_size to keep output tokens
    within bounds. Returns the total count of items saved.
    """
    saved = 0
    # Process in chunks; preserve chronological order
    for i in range(0, max(1, len(messages)), chunk_size):
        chunk = messages[i : i + chunk_size]
        captures = await extract_captures(chunk, source_channel)
        for item in captures:
            result = save_capture(item, source_channel)
            if result is not None:
                saved += 1
    return saved
