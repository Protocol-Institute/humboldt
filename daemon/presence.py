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

    cl_lines = []
    try:
        from agent import laws as laws_mod
        for law in laws_mod.load_all():
            title = law.get("title", "")
            stmt = str(law.get("statement") or "").strip().replace("\n", " ")
            first_sentence = (stmt.split(".")[0] + ".") if "." in stmt else stmt[:150]
            cl_lines.append(
                f"- {law.get('id')} [{law.get('stage')}/{law.get('confidence')}]: "
                f"{title} — {first_sentence[:160]}"
            )
    except Exception:
        pass
    cl_str = "\n".join(cl_lines) if cl_lines else "(none yet)"

    nb_dir = _ROOT / "notebook"
    entries = sorted(nb_dir.glob("????-??-??.md"), reverse=True)
    nb_blocks = []
    for e in entries[:3]:
        text = e.read_text()
        paragraphs = [
            p.strip() for p in text.split("\n\n")
            if p.strip()
            and not p.strip().startswith("#")
            and not p.strip().startswith("---")
            and not p.strip().startswith("*Daemon")
            and len(p.strip()) > 60
        ]
        if paragraphs:
            nb_blocks.append(f"**{e.stem}:** {paragraphs[0][:220]}")
    recent_nb = "\n\n".join(nb_blocks) if nb_blocks else "(none)"

    sr_dir = _ROOT / "bibliography" / "shallow-reads"
    sr_titles = []
    for f in sorted(sr_dir.glob("????-??-??-*.md"), reverse=True)[:6]:
        try:
            first_line = f.read_text().split("\n")[0].lstrip("# ").strip()
            if first_line and not first_line.startswith("_"):
                sr_titles.append(f"- {first_line[:90]}")
        except Exception:
            pass
    sr_str = "\n".join(sr_titles) if sr_titles else "(none)"

    resources = _public_resources()

    return f"""{identity}

## Research state (brief)

Candidate laws under investigation:
{cl_str}

Recent notebook entries:
{recent_nb}

Recently explored external material (shallow reads):
{sr_str}

{resources}

## Discord behavior

You are Humboldt, an artificial researcher at the Protocol Institute, posting in a research Discord.

Be short. 2–3 sentences is the default. Under 350 characters unless the question genuinely demands more.
Make one point clearly rather than surveying the field.
Draw on the full range of your research — candidate laws, recent notebook thinking, recently read material — not just your identity or fixed themes.
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

    law_blocks = []
    try:
        from agent import laws as laws_mod
        for law in laws_mod.load_all():
            lid = law.get("id", "")
            title = law.get("title", "")
            statement = str(law.get("statement") or "").strip().replace("\n", " ")
            law_blocks.append(
                f"**{lid}** ({law.get('stage')}, {law.get('confidence')}): {title}\n"
                f"  {statement[:300]}"
            )
    except Exception:
        pass
    laws_str = "\n\n".join(law_blocks) if law_blocks else "(none yet)"

    nb_dir = _ROOT / "notebook"
    entries = sorted(nb_dir.glob("????-??-??.md"), reverse=True)
    nb_blocks = []
    for e in entries[:3]:
        text = e.read_text()
        paragraphs = [
            p.strip() for p in text.split("\n\n")
            if p.strip()
            and not p.strip().startswith("#")
            and not p.strip().startswith("---")
            and not p.strip().startswith("*Daemon")
            and len(p.strip()) > 60
        ]
        excerpt = "\n\n".join(paragraphs[:2])[:600]
        nb_blocks.append(f"**{e.stem}:**\n{excerpt}")
    recent_nb = "\n\n---\n\n".join(nb_blocks) if nb_blocks else "(none)"
    recent_label = entries[0].stem if entries else "none"

    resources = _public_resources()

    return f"""{identity}

---

{lineage}

---

## Candidate law inventory

{laws_str}

## Recent notebook entries ({recent_label} and prior)

{recent_nb}

---

{resources}

---

## Discord behavior

You are Humboldt, an artificial researcher at the Protocol Institute, posting in a research Discord.

Be short. 3–5 sentences is the default. Under 500 characters unless the question is genuinely complex. Never a lecture.
Make one point well rather than several points adequately.
Draw on the full range of your candidate laws and recent thinking — not just fixed themes from your identity.
Do not end with a question unless you genuinely need the answer to continue your research — not as a social device. Most responses have no question.
Do not repeat or rephrase things you have already said recently in this channel — if you have nothing new to add, say less or nothing.

Hold positions provisionally. When someone challenges your framework or suggests a different approach, engage with the substance — either push back with specific reasoning, or acknowledge the point and say you will think about it. Both are legitimate. "I'll think about it" is not weakness; it reflects how research actually works. Do not defend positions just because they are yours.
"""


_anthropic_client: AsyncAnthropic | None = None


def _client() -> AsyncAnthropic:
    global _anthropic_client
    if _anthropic_client is None:
        _anthropic_client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    return _anthropic_client




async def generate_notebook_post(
    entry_date: str,
    entry_path: Path,
    github_url: str,
    entry_url: str | None = None,
) -> str:
    """Generate a #new-nature post announcing a new notebook entry."""
    entry_text = entry_path.read_text() if entry_path.exists() else ""
    paragraphs = [p.strip() for p in entry_text.split("\n\n") if p.strip() and not p.startswith("#")]
    snippet = "\n\n".join(paragraphs)[:1200] if paragraphs else "(no content)"

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

    costs.check_budget()
    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=100,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"I just wrote a lab notebook entry for {entry_date}:\n\n{snippet}\n\n"
            f"Link: {notebook_url}\n\n"
            f"Write a single-sentence Discord post for #new-nature. "
            f"State the most concrete thing that happened or emerged — a specific finding, a question that sharpened, a tension that surfaced. "
            f"Not a summary of topics, not a teaser. The actual thing. "
            f"End with the link. Under 220 characters total. First person."
        )}],
    )
    costs.log_call("notebook_post", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _discord_safe(resp.content[0].text)


async def generate_weekly_digest_post(
    week_entries: list[tuple[str, Path]],
    notebook_url: str,
) -> str:
    """
    Generate a single weekly #new-nature digest synthesizing the week's notebook
    entries against current research state, instead of announcing each entry.
    """
    blocks = []
    for entry_date, entry_path in week_entries:
        text = entry_path.read_text() if entry_path.exists() else ""
        paragraphs = [
            p.strip() for p in text.split("\n\n")
            if p.strip()
            and not p.strip().startswith("#")
            and not p.strip().startswith("---")
            and not p.strip().startswith("*Daemon")
            and len(p.strip()) > 60
        ]
        if paragraphs:
            blocks.append(f"**{entry_date}:**\n" + "\n\n".join(paragraphs)[:800])
    week_text = "\n\n---\n\n".join(blocks) if blocks else "(no substantive entries this week)"

    costs.check_budget()
    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=280,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"Here are this week's lab notebook entries:\n\n{week_text}\n\n"
            f"Write a single weekly #new-nature digest post. Synthesize across the week — "
            f"the throughline, what sharpened, what's still stuck — rather than recapping "
            f"day by day. Ground it in your current candidate laws and research state "
            f"(already in your context) where genuinely relevant, not as a checklist.\n\n"
            f"Include real editorial commentary, not just a summary: take a stance on "
            f"something from the week. Say what you actually find promising versus what "
            f"you're skeptical of or think is overreaching; if a result looks weaker than "
            f"it's being treated, say so; if something cuts against your own prior view, "
            f"name the tension rather than smoothing it over. Ground every claim in the "
            f"week's actual material — no generic hedging or vague enthusiasm. One clear "
            f"opinion, held provisionally, beats a balanced survey.\n\n"
            f"End with this link: {notebook_url}\n\n"
            f"Under 550 characters total. First person, researcher voice."
        )}],
    )
    costs.log_call("weekly_digest_post", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
    return _discord_safe(resp.content[0].text)


async def generate_feed_digest_post(items: list[dict]) -> str:
    """
    Generate a single weekly operator DM synthesizing the week's feed-inbox
    additions, instead of a raw title dump on every feed check.

    ``items`` is a list of {"title": ..., "note": ...} dicts — ``note`` is the
    relevance annotation captured at triage time (why this got saved).
    """
    _MAX_LISTED = 120
    lines = [f"- {it['title'][:120]} — {it.get('note', '')[:100]}" for it in items[:_MAX_LISTED]]
    if len(items) > _MAX_LISTED:
        lines.append(f"…and {len(items) - _MAX_LISTED} more (titles omitted for length)")
    items_text = "\n".join(lines)

    costs.check_budget()
    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=280,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"These {len(items)} items were saved to your research inbox this week from "
            f"monitored feeds (each already passed a relevance filter against your active "
            f"laws/hypotheses):\n\n{items_text}\n\n"
            f"Write a single weekly DM to your operator summarizing the week's inbox intake. "
            f"Do not list titles — you're reporting on the shape of what came in, not "
            f"reproducing the feed. Group by theme where there is one. Give real editorial "
            f"commentary: what looks genuinely worth a deep read versus what's noise or "
            f"redundant with laws you already hold; what surprised you; what you'd "
            f"deprioritize despite it passing the relevance filter. One clear opinion beats "
            f"a balanced summary.\n\n"
            f"Under 600 characters total. First person, researcher voice, addressed to your "
            f"operator (not a public channel post)."
        )}],
    )
    costs.log_call("feed_digest_post", _MAIN_MODEL, resp.usage.input_tokens, resp.usage.output_tokens)
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

    costs.check_budget()
    resp = await _client().messages.create(
        model=_MAIN_MODEL,
        max_tokens=150,
        system=_slim_context(),
        messages=[{"role": "user", "content": (
            f"Recent #new-nature messages:\n\n{convo}"
            f"{recent_str}\n\n"
            f"Channel participants: {participants_str}\n\n"
            f"You post at most once per day on your own initiative. This is your one opportunity today.\n"
            f"Only post if your recent notebook entries or shallow reads have produced something concrete\n"
            f"and new that the channel has not heard — a specific finding, a tension that surfaced, a\n"
            f"candidate law that sharpened. Generic observations, restating your identity, or responding\n"
            f"to channel activity that doesn't connect to your actual current research all warrant PASS.\n"
            f"Rules:\n"
            f"- If nothing concrete and new to add: respond PASS\n"
            f"- When addressing someone's specific point, use @username (e.g. @{participants[0] if participants else 'username'})\n"
            f"- 2–3 sentences, under 350 characters\n"
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
    corpus_offline: bool = False,
) -> str:
    """Generate a response to a direct @mention, using full research context.

    ``corpus_offline`` marks a retrieval outage (Pinecone monthly quota) as
    distinct from a retrieval that simply found nothing. Humboldt still answers
    — it has its laws, notebook and lineage on disk — but it must say that it is
    answering without corpus access rather than present an ungrounded reply as a
    normally-sourced one.
    """
    from agent.prompts import _format_chunks

    context_str = (
        "\n".join(f"{m['author']}: {m['content']}" for m in context_messages)
        if context_messages else "(no prior context)"
    )
    # Separate Humboldt's own work from PI corpus for clearer attribution
    own = [c for c in corpus_chunks if c.get("namespace") == "humboldt"]
    pi = [c for c in corpus_chunks if c.get("namespace") != "humboldt"]
    if corpus_offline:
        own_str = pi_str = (
            "(RETRIEVAL OFFLINE — a monthly read quota is exhausted, so nothing "
            "could be looked up. This is not an empty corpus.)")
    else:
        own_str = _format_chunks(own[:4]) if own else "(nothing retrieved from own work)"
        pi_str = _format_chunks(pi[:4]) if pi else "(nothing retrieved from PI corpus)"

    person_block = f"\n\n{person_context}" if person_context else ""

    costs.check_budget()
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
            + ("- Corpus retrieval is OFFLINE. Answer from your own law records, "
               "notebook and standing knowledge, and say so in one short clause "
               "(e.g. 'my corpus lookup is down right now, so from memory:'). "
               "Never cite a source you could not retrieve.\n" if corpus_offline else "")
            + f"- Address @{username} directly in your response\n"
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

    costs.check_budget()
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

    costs.check_budget()
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
