"""Claude-powered synthesis for research tasks."""

import os
import anthropic

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 4096


def _client() -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def synthesize(
    system: str,
    user: str,
    max_tokens: int = MAX_TOKENS,
    cache_system: bool = True,
) -> str:
    """
    Call Claude with a system prompt and user message.

    cache_system=True adds prompt caching to the system block (SOUL.md is large
    and reused across calls in a session).
    """
    client = _client()

    system_block = {"type": "text", "text": system}
    if cache_system:
        system_block["cache_control"] = {"type": "ephemeral"}

    resp = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=[system_block],
        messages=[{"role": "user", "content": user}],
    )
    return resp.content[0].text


def synthesize_streaming(
    system: str,
    user: str,
    max_tokens: int = MAX_TOKENS,
    cache_system: bool = True,
) -> str:
    """
    Streaming variant — prints output as it arrives, returns full text.
    """
    client = _client()

    system_block = {"type": "text", "text": system}
    if cache_system:
        system_block["cache_control"] = {"type": "ephemeral"}

    full_text = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=max_tokens,
        system=[system_block],
        messages=[{"role": "user", "content": user}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_text.append(text)

    print()  # final newline
    return "".join(full_text)
