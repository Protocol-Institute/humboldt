"""Claude-powered synthesis for research tasks."""

import os
import anthropic
import httpx

MODEL = "claude-sonnet-4-6"
HAIKU_MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 4096

_MODEL_MAP = {
    "sonnet": MODEL,
    "haiku": HAIKU_MODEL,
}

# 10-minute read timeout for long streaming API calls
_TIMEOUT = httpx.Timeout(connect=10.0, read=600.0, write=10.0, pool=10.0)


def _client() -> anthropic.Anthropic:
    return anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        http_client=httpx.Client(timeout=_TIMEOUT),
    )


def _resolve_model(model: str) -> str:
    return _MODEL_MAP.get(model, model)


def synthesize(
    system: str,
    user: str,
    max_tokens: int = MAX_TOKENS,
    cache_system: bool = True,
    model: str = MODEL,
) -> str:
    """
    Call Claude with a system prompt and user message.

    cache_system=True adds prompt caching to the system block (SOUL.md is large
    and reused across calls in a session).
    model: model ID or shorthand ("sonnet", "haiku")
    """
    client = _client()

    system_block = {"type": "text", "text": system}
    if cache_system:
        system_block["cache_control"] = {"type": "ephemeral"}

    resp = client.messages.create(
        model=_resolve_model(model),
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
    model: str = MODEL,
) -> str:
    """
    Streaming variant — prints output as it arrives, returns full text.
    model: model ID or shorthand ("sonnet", "haiku")
    """
    client = _client()

    system_block = {"type": "text", "text": system}
    if cache_system:
        system_block["cache_control"] = {"type": "ephemeral"}

    full_text = []
    with client.messages.stream(
        model=_resolve_model(model),
        max_tokens=max_tokens,
        system=[system_block],
        messages=[{"role": "user", "content": user}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_text.append(text)

    print()  # final newline
    return "".join(full_text)
