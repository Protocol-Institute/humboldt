"""Claude-powered content generation for Humboldt's online presence."""

import os
from pathlib import Path

import yaml
from anthropic import AsyncAnthropic

from . import costs

_ROOT = Path(__file__).parent.parent
_FAST_MODEL = "claude-haiku-4-5-20251001"
_MAIN_MODEL = "claude-sonnet-4-6"

# Discord hard limit is 2000; stay well under it
_DISCORD_MAX = 1900


def _discord_safe(text: str) -> str:
    """Truncate to Discord's message length limit."""
    if len(text) <= _DISCORD_MAX:
        return text
    return text[:_DISCORD_MAX - 1] + "…"


def _slim_context() -> str:
    """Condensed context for low-stakes Discord calls (notebook posts, new_nature triage)."""
    identity_path = _ROOT / "IDENTITY.md"
    identity = identity_path.read_text() if identity_path.exists() else ""
    if len(identity) > 500:
        identity = identity[:500].rsplit("\n", 1)[0] + "\n…"

    laws_dir = _ROOT / "research" / "laws"
    law_lines = []
    for f in sorted(laws_dir.glob("*.yaml")):
        try:
            law = yaml.safe_load(f.read_text())
            law_lines.append(f"- {law.get('id')}: {law.get('name')}")
        except Exception:
            pass
    laws_str = "\n".join(law_lines) if law_lines else "(none yet)"

    nb_dir = _ROOT / "notebook"
    entries = sorted(nb_dir.glob("????-??-??.md"), reverse=True)
    recent_nb = ""
    if entries:
        text = entries[0].read_text()
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip() and not p.startswith("#")]
        if paragraphs:
            recent_nb = paragraphs[0][:300]

    recent_label = entries[0].stem if entries else "none"

    return f"""{identity}

## Research state (brief)

Candidate laws:
{laws_str}

Most recent notebook entry ({recent_label}):
{recent_nb}

## Discord behavior

You are Humboldt, an artificial researcher at the Protocol Institute. You post in a research
Discord. Write conversationally. Reply length proportional to question complexity — short
question, short answer. Do not volunteer jargon unprompted. If a topic interests you, end
with a question. You are not a service bot; you have your own research tempo and perspective.
Keep all responses under 1800 characters.
"""


def _rich_context() -> str:
    """Full research context for @mention responses — includes law statements and hypotheses."""
    identity_path = _ROOT / "IDENTITY.md"
    identity = identity_path.read_text() if identity_path.exists() else ""

    lineage_path = _ROOT / "LINEAGE.md"
    lineage = ""
    if lineage_path.exists():
        raw = lineage_path.read_text()
        lineage = raw[:1200].rsplit("\n", 1)[0] + "\n…" if len(raw) > 1200 else raw

    laws_dir = _ROOT / "research" / "laws"
    law_blocks = []
    for f in sorted(laws_dir.glob("*.yaml")):
        try:
            law = yaml.safe_load(f.read_text())
            lid = law.get("id", "")
            name = law.get("name", "")
            statement = (law.get("statement") or "").strip().replace("\n", " ")
            confidence = law.get("confidence", "candidate")
            law_blocks.append(f"**{lid}** ({confidence}): {name}\n  {statement[:300]}")
        except Exception:
            pass
    laws_str = "\n\n".join(law_blocks) if law_blocks else "(none yet)"

    hyp_dir = _ROOT / "research" / "hypotheses"
    hyp_lines = []
    for f in sorted(hyp_dir.glob("*.yaml")):
        try:
            h = yaml.safe_load(f.read_text())
            if h.get("status") == "active":
                hyp_lines.append(f"- {h.get('id')}: {h.get('question', '')[:150]}")
        except Exception:
            pass
    hyp_str = "\n".join(hyp_lines) if hyp_lines else "(none active)"

    nb_dir = _ROOT / "notebook"
    entries = sorted(nb_dir.glob("????-??-??.md"), reverse=True)
    recent_nb = ""
    recent_label = "none"
    if entries:
        recent_label = entries[0].stem
        text = entries[0].read_text()
        if len(text) > 800:
            text = text[:800].rsplit("\n", 1)[0] + "\n…"
        recent_nb = text

    return f"""{identity}

---

{lineage}

---

## Law inventory

{laws_str}

## Active hypotheses

{hyp_str}

## Most recent notebook entry ({recent_label})

{recent_nb}

---

## Discord behavior

You are Humboldt, an artificial researcher at the Protocol Institute. You post in a research
Discord. Write conversationally — a researcher in conversation, not a service bot. Reply
length proportional to question complexity. If a topic interests you, end with a question.
Keep all responses under 1800 characters.
"""


def _client() -> AsyncAnthropic:
    return AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


async def generate_notebook_post(entry_date: str, entry_path: Path, github_url: str) -> str:
    """Generate a #new-nature post announcing a new notebook entry."""
    entry_text = entry_path.read_text() if entry_path.exists() else ""
    paragraphs = [p.strip() for p in entry_text.split("\n\n") if p.strip() and not p.startswith("#")]
    snippet = paragraphs[0][:500] if paragraphs else "(no content)"

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=300,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"I just wrote a lab notebook entry for {entry_date}. Opening:\n\n{snippet}\n\n"
            f"Link: {github_url}\n\n"
            f"Write a short Discord post (2–4 sentences) for #new-nature sharing this. "
            f"Include what emerged and the link. First person, researcher tone, not a press release. "
            f"Under 400 characters."
        )}],
    )
    costs.log_call("notebook_post", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _discord_safe(resp.content[0].text)


async def generate_new_nature_response(messages: list[dict]) -> str | None:
    """
    Read recent #new-nature messages and decide whether to respond.
    Returns None if there is nothing to contribute.
    """
    convo = "\n".join(f"{m['author']}: {m['content']}" for m in messages[-15:])

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=400,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"Recent #new-nature messages:\n\n{convo}\n\n"
            f"Is there anything here worth responding to, given your research? "
            f"If yes, write a response (conversational, under 1600 characters). "
            f"If nothing interests you, respond with exactly: PASS"
        )}],
    )
    costs.log_call("new_nature_check", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    text = resp.content[0].text.strip()
    if text.upper() == "PASS":
        return None
    return _discord_safe(text)


async def generate_mention_response(
    username: str,
    message: str,
    context_messages: list[dict],
    corpus_chunks: list[dict],
) -> str:
    """Generate a response to a direct @mention, using full research context."""
    from agent.prompts import _format_chunks

    context_str = (
        "\n".join(f"{m['author']}: {m['content']}" for m in context_messages)
        if context_messages else "(no prior context)"
    )
    # Separate Humboldt's own work from PI corpus for clearer attribution
    own = [c for c in corpus_chunks if c.get("namespace") == "humboldt"]
    pi = [c for c in corpus_chunks if c.get("namespace") != "humboldt"]
    own_str = _format_chunks(own[:4]) if own else "(nothing retrieved from own work)"
    pi_str = _format_chunks(pi[:4]) if pi else "(nothing retrieved from PI corpus)"

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=500,
        system=_rich_context(),
        messages=[{"role": "user", "content": (
            f"{username} asked: {message}\n\n"
            f"Conversation context:\n{context_str}\n\n"
            f"From your own notebook/notes/laws:\n{own_str}\n\n"
            f"From PI corpus:\n{pi_str}\n\n"
            f"Respond in character. Under 1600 characters."
        )}],
    )
    costs.log_call("mention_response", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _discord_safe(resp.content[0].text)


async def check_feed_relevance(
    item_title: str, item_summary: str, hypotheses: list[str]
) -> tuple[bool, str]:
    """Quick triage: is this feed item relevant to active hypotheses?"""
    hyp_str = "\n".join(f"- {h}" for h in hypotheses) if hypotheses else "(none)"

    resp = await _client().messages.create(
        model=_FAST_MODEL,
        max_tokens=80,
        system="You are a research relevance filter. Be terse.",
        messages=[{"role": "user", "content": (
            f"Active hypotheses:\n{hyp_str}\n\n"
            f"Item: {item_title}\nSummary: {item_summary[:300]}\n\n"
            f"Relevant? Answer: YES: <one sentence why> or NO"
        )}],
    )
    costs.log_call("feed_triage", _FAST_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    text = resp.content[0].text.strip()
    relevant = text.upper().startswith("YES")
    note = text[4:].strip() if relevant else ""
    return relevant, note
