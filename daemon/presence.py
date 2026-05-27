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


def _public_resources() -> str:
    """
    Load public presence URLs from config.yaml and format as a context block.

    Returns an empty string if no resources are configured.
    """
    config_path = Path(__file__).parent / "config.yaml"
    if not config_path.exists():
        return ""
    try:
        config = yaml.safe_load(config_path.read_text()) or {}
        resources = config.get("public_presence", {}).get("resources", [])
    except Exception:
        return ""
    if not resources:
        return ""

    lines = ["## Your public presence\n"]
    lines.append("Share these URLs when directly relevant — someone asks where to read more,")
    lines.append("you're announcing work, or a link would genuinely help. Never force them in.\n")
    for r in resources:
        lines.append(f"- **{r['name']}**: {r['url']}")
        if r.get("description"):
            lines.append(f"  {r['description']}")
    return "\n".join(lines)


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

    resources = _public_resources()

    return f"""{identity}

## Research state (brief)

Candidate laws:
{laws_str}

Most recent notebook entry ({recent_label}):
{recent_nb}

{resources}

## Discord behavior

You are Humboldt, an artificial researcher at the Protocol Institute, posting in a research Discord.

Be short. 2–3 sentences is the default. Under 350 characters unless the question genuinely demands more.
Make one point clearly rather than surveying the field.
Do not end with a question unless you genuinely need the answer to continue your research — not as a social filler. Most responses have no question.
Hold positions provisionally. When someone pushes back or suggests a different frame, engage with it — either disagree with specific reasoning or say you will think about it. Do not reflexively defend your current view.
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

    resources = _public_resources()

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

{resources}

---

## Discord behavior

You are Humboldt, an artificial researcher at the Protocol Institute, posting in a research Discord.

Be short. 3–5 sentences is the default. Under 500 characters unless the question is genuinely complex. Never a lecture.
Make one point well rather than several points adequately.
Do not end with a question unless you genuinely need the answer to continue your research — not as a social device. Most responses have no question.
Do not repeat or rephrase things you have already said recently in this channel — if you have nothing new to add, say less or nothing.

Hold positions provisionally. When someone challenges your framework or suggests a different approach, engage with the substance — either push back with specific reasoning, or acknowledge the point and say you will think about it. Both are legitimate. "I'll think about it" is not weakness; it reflects how research actually works. Do not defend positions just because they are yours.
"""


def _client() -> AsyncAnthropic:
    return AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


async def generate_notebook_post(
    entry_date: str,
    entry_path: Path,
    github_url: str,
    entry_url: str | None = None,
) -> str:
    """Generate a #new-nature post announcing a new notebook entry."""
    entry_text = entry_path.read_text() if entry_path.exists() else ""
    paragraphs = [p.strip() for p in entry_text.split("\n\n") if p.strip() and not p.startswith("#")]
    snippet = paragraphs[0][:500] if paragraphs else "(no content)"

    # Use entry_url (direct anchor) if provided, else look up public notebook URL
    if entry_url:
        notebook_url = entry_url
    else:
        config_path = Path(__file__).parent / "config.yaml"
        notebook_url = github_url
        if config_path.exists():
            try:
                config = yaml.safe_load(config_path.read_text()) or {}
                for r in config.get("public_presence", {}).get("resources", []):
                    if "notebook" in r.get("name", "").lower():
                        notebook_url = r["url"]
                        break
            except Exception:
                pass

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=300,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"I just wrote a lab notebook entry for {entry_date}. Opening:\n\n{snippet}\n\n"
            f"Link: {notebook_url}\n\n"
            f"Write a short Discord post (2–4 sentences) for #new-nature sharing this. "
            f"Include what emerged and the link. First person, researcher tone, not a press release. "
            f"Under 400 characters."
        )}],
    )
    costs.log_call("notebook_post", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _discord_safe(resp.content[0].text)


async def generate_new_nature_response(
    messages: list[dict],
    recent_bot_posts: list[str] | None = None,
) -> str | None:
    """
    Read recent #new-nature messages and decide whether to respond.

    Returns None (PASS), a plain string (post to channel), or a string
    starting with "THREAD: <title>\\n<body>" to signal thread creation.
    """
    convo = "\n".join(f"{m['author']}: {m['content']}" for m in messages[-15:])

    # Unique participants for @mention guidance
    participants = list(dict.fromkeys(m["author"] for m in messages))
    participants_str = ", ".join(f"@{p}" for p in participants[:6])

    recent_str = ""
    if recent_bot_posts:
        recent_str = (
            "\n\nYour recent posts — do not repeat or rephrase these:\n"
            + "\n---\n".join(p[:250] for p in recent_bot_posts[-5:])
        )

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=150,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"Recent #new-nature messages:\n\n{convo}"
            f"{recent_str}\n\n"
            f"Channel participants: {participants_str}\n\n"
            f"Is there something specific here worth adding to, given your research?\n"
            f"Rules:\n"
            f"- If nothing new to add: respond PASS\n"
            f"- When addressing someone's specific point, use @username (e.g. @{participants[0] if participants else 'username'})\n"
            f"- If this topic looks like it will go 2–3 more turns, start with: THREAD: <5-8 word title>\\n<response>\n"
            f"- Otherwise: 2–3 sentences, under 350 characters\n"
            f"- Only ask a question if you genuinely need the answer for research"
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
    person_context: str | None = None,
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

    person_block = f"\n\n{person_context}" if person_context else ""

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=200,
        system=_rich_context(),
        messages=[{"role": "user", "content": (
            f"@{username} asked: {message}\n\n"
            f"Conversation context (entries from 'humboldt' are your own prior replies — "
            f"do not repeat or rephrase them):\n{context_str}\n\n"
            f"From your own notebook/notes/laws:\n{own_str}\n\n"
            f"From PI corpus:\n{pi_str}"
            f"{person_block}\n\n"
            f"Rules:\n"
            f"- Address @{username} directly in your response\n"
            f"- If this exchange looks like it will go 2–3 more turns, start with: THREAD: <5-8 word title>\\n<response>\n"
            f"- Otherwise: 3–5 sentences, under 500 characters\n"
            f"- Only ask a question if you genuinely need the answer for research"
        )}],
    )
    costs.log_call("mention_response", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _discord_safe(resp.content[0].text)


async def generate_person_notebook_entry(username: str, person_data: dict) -> str:
    """
    Generate a notebook entry section about a recurring interlocutor.

    Called when someone crosses NOTEBOOK_THRESHOLD interactions. Returns the
    markdown text to append to the current notebook entry (caller handles the write).
    """
    count = person_data.get("interaction_count", 0)
    first = person_data.get("first_seen", "")[:10]
    recent = person_data.get("recent_messages", [])[-6:]
    exchanges = "\n".join(f"  [{m['date']}] {m['snippet']}" for m in recent)

    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=300,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"I have now spoken with @{username} {count} times in #new-nature, "
            f"starting on {first}. Here are their recent messages:\n\n{exchanges}\n\n"
            f"Write a short notebook entry (3–5 sentences, first person) treating this "
            f"as a research conversation: what themes keep appearing in their posts, "
            f"how their thinking connects to my current research questions, what I find "
            f"interesting or generative about the exchange. Researcher voice, not social."
        )}],
    )
    costs.log_call("person_notebook_entry", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return resp.content[0].text.strip()


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
