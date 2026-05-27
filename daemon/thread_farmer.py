"""
thread_farmer.py — harvest comments from Discord notebook entry threads.

Reads notebook/index.yaml for entries that have discord_thread_id set.
For each, fetches messages posted since thread_last_farmed (or all if never
farmed). Saves structured inbox files and updates thread_last_farmed in the
index. Called from task_conversation_review (daily).
"""

import logging
from datetime import datetime, timezone
from pathlib import Path

import discord

from agent import notebook_index as nbi

logger = logging.getLogger("humboldt.thread_farmer")
_ROOT = Path(__file__).parent.parent


def _dt_to_snowflake(dt: datetime) -> int:
    """Convert a datetime to an approximate Discord snowflake for history pagination."""
    discord_epoch_ms = 1420070400000
    ms = int(dt.timestamp() * 1000)
    return (ms - discord_epoch_ms) << 22


def _write_inbox_file(
    path: Path,
    date: str,
    title: str,
    messages: list[dict],
    entry_url: str,
) -> None:
    lines = [
        f"# Thread comments: {title}",
        "",
        f"source: discord-thread",
        f"entry_date: {date}",
        f"entry_url: {entry_url}",
        f"harvested: {datetime.now(timezone.utc).isoformat()}",
        f"message_count: {len(messages)}",
        "",
        "---",
        "",
    ]
    for m in messages:
        ts = m["timestamp"][:10]
        lines.append(f"**@{m['author']}** ({ts}): {m['content']}")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines))


async def harvest_thread_comments(
    client: discord.Client,
    entry: dict,
) -> int:
    """
    Fetch new comments from the Discord thread for one notebook entry.

    Returns the number of new messages saved to inbox/.
    """
    thread_id = entry.get("discord_thread_id")
    if not thread_id:
        return 0

    last_farmed_str = entry.get("thread_last_farmed")
    after_obj: discord.Object | None = None
    if last_farmed_str:
        after_dt = datetime.fromisoformat(last_farmed_str)
        after_obj = discord.Object(id=_dt_to_snowflake(after_dt))

    try:
        thread = client.get_channel(int(thread_id))
        if thread is None:
            thread = await client.fetch_channel(int(thread_id))
    except Exception as e:
        logger.warning(f"Could not access thread {thread_id} for {entry.get('date')}: {e}")
        return 0

    messages: list[dict] = []
    try:
        kwargs: dict = {"limit": 100}
        if after_obj:
            kwargs["after"] = after_obj
        async for msg in thread.history(**kwargs):
            if msg.author.bot:
                continue
            messages.append({
                "author": msg.author.name,
                "content": msg.content[:600],
                "timestamp": msg.created_at.isoformat(),
            })
    except Exception as e:
        logger.warning(f"Thread history fetch failed for {thread_id}: {e}")
        return 0

    if not messages:
        nbi.upsert_entry(entry["date"], thread_last_farmed=datetime.now(timezone.utc).isoformat())
        return 0

    messages.reverse()  # chronological order for the prompt

    date = entry.get("date", "unknown")
    title = entry.get("title", date)
    now_str = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    inbox_path = _ROOT / "inbox" / f"thread-{date}-{now_str}.md"
    _write_inbox_file(inbox_path, date, title, messages, entry.get("url", ""))

    nbi.upsert_entry(entry["date"], thread_last_farmed=datetime.now(timezone.utc).isoformat())
    logger.info(f"Harvested {len(messages)} thread comment(s) for entry {date} → {inbox_path.name}")
    return len(messages)


async def run_harvest(client: discord.Client) -> int:
    """
    Harvest thread comments for all indexed entries that have a discord_thread_id.

    Returns total number of messages saved across all threads.
    """
    entries = nbi.load()
    total = 0
    for entry in entries:
        if not entry.get("discord_thread_id"):
            continue
        try:
            n = await harvest_thread_comments(client, entry)
            total += n
        except Exception as e:
            logger.error(f"Harvest failed for entry {entry.get('date')}: {e}")
    return total
