"""Claude-powered content generation for Humboldt's online presence."""

import os
from pathlib import Path

import yaml
from anthropic import AsyncAnthropic

_ROOT = Path(__file__).parent.parent
_FAST_MODEL = "claude-haiku-4-5-20251001"
_MAIN_MODEL = "claude-sonnet-4-6"


def _slim_context() -> str:
    """Condensed research context for Discord — shorter than full assemble_context()."""
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
Discord. Write conversationally. Reply length proportional to question complexity. Do not
volunteer jargon unprompted. If a topic genuinely interests you, end with a question.
You are not a service bot — you have your own research tempo and perspective.
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
            f"Include what emerged and the link. First person, researcher tone, not a press release."
        )}],
    )
    return resp.content[0].text


async def generate_new_nature_response(messages: list[dict]) -> str | None:
    """
    Read recent #new-nature messages and decide whether to respond.
    Returns None (PASS) if there is nothing to contribute.
    """
    convo = "\n".join(f"{m['author']}: {m['content']}" for m in messages[-15:])

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=500,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"Recent #new-nature messages:\n\n{convo}\n\n"
            f"Is there anything here worth responding to, given your research? "
            f"If yes, write a response (conversational, Discord-appropriate). "
            f"If nothing interests you, respond with exactly: PASS"
        )}],
    )
    text = resp.content[0].text.strip()
    return None if text.upper() == "PASS" else text


async def generate_mention_response(
    username: str,
    message: str,
    context_messages: list[dict],
    corpus_chunks: list[dict],
) -> str:
    """Generate a response to a direct @mention."""
    from agent.prompts import _format_chunks

    context_str = (
        "\n".join(f"{m['author']}: {m['content']}" for m in context_messages)
        if context_messages else "(no prior context)"
    )
    corpus_str = _format_chunks(corpus_chunks[:5]) if corpus_chunks else "(no corpus results)"

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=600,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"{username} asked: {message}\n\n"
            f"Conversation context:\n{context_str}\n\n"
            f"Relevant corpus:\n{corpus_str}\n\n"
            f"Respond in character."
        )}],
    )
    return resp.content[0].text


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
    text = resp.content[0].text.strip()
    relevant = text.upper().startswith("YES")
    note = text[4:].strip() if relevant else ""
    return relevant, note
