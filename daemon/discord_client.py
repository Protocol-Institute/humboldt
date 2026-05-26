"""Humboldt Discord bot — event handlers and scheduled presence tasks."""

import asyncio
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import discord
import yaml
from discord.ext import tasks

from . import state as st
from . import notebook_watcher as nw
from . import feed_monitor as fm
from . import presence

logger = logging.getLogger("humboldt.discord")
_ROOT = Path(__file__).parent.parent


def _load_config() -> dict:
    config_path = Path(__file__).parent / "config.yaml"
    if config_path.exists():
        return yaml.safe_load(config_path.read_text()) or {}
    return {}


def _active_hypotheses() -> list[str]:
    hyp_dir = _ROOT / "research" / "hypotheses"
    result = []
    for f in sorted(hyp_dir.glob("*.yaml")):
        try:
            h = yaml.safe_load(f.read_text())
            if h.get("status") == "active":
                result.append(f"{h.get('id')} — {h.get('name')}")
        except Exception:
            pass
    return result


class HumboldtBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        super().__init__(intents=intents)
        self.config = _load_config()
        self.guild_id = int(os.environ["DISCORD_GUILD_ID"])
        self.new_nature_id = int(os.environ["DISCORD_NEW_NATURE_CHANNEL_ID"])
        self.operator_id = int(os.environ["DISCORD_OPERATOR_USER_ID"])

    async def setup_hook(self):
        self.task_notebook.start()
        self.task_new_nature.start()
        self.task_feeds.start()

    async def on_ready(self):
        logger.info(f"Humboldt online: {self.user} (id {self.user.id})")
        self.loop.create_task(self._scan_missed_mentions())

    async def _scan_missed_mentions(self):
        """Respond to @mentions that arrived in #new-nature while the bot was offline."""
        await self.wait_until_ready()
        state = st.load()
        last_msg_id = state.get("last_new_nature_message_id")
        if not last_msg_id:
            return

        channel = self.get_channel(self.new_nature_id)
        if not channel:
            return

        missed = []
        async for msg in channel.history(limit=100, after=discord.Object(id=int(last_msg_id))):
            if msg.author != self.user and self.user in msg.mentions:
                missed.append(msg)

        if not missed:
            return

        logger.info(f"Responding to {len(missed)} missed @mention(s)")
        for msg in reversed(missed):
            content = msg.content.replace(f"<@{self.user.id}>", "").strip()
            if not content:
                continue
            history = []
            async for ctx in channel.history(limit=9, before=msg):
                history.insert(0, {"author": ctx.author.name, "content": ctx.content[:300]})
            chunks = []
            try:
                from agent import retrieval as ret
                chunks = await self.loop.run_in_executor(
                    None, lambda: ret.multi_retrieve([content], namespaces=ret.NS_BROAD_PLUS, top_k_each=5)
                )
            except Exception:
                pass
            try:
                response = await presence.generate_mention_response(
                    username=msg.author.name,
                    message=content,
                    context_messages=history,
                    corpus_chunks=chunks,
                )
                await msg.reply(f"*(catching up from while I was offline)*\n{response}")
            except Exception as e:
                logger.error(f"Missed mention response failed: {e}")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        if self.user not in message.mentions:
            return

        content = message.content.replace(f"<@{self.user.id}>", "").strip()
        if not content:
            return

        logger.info(f"@mention from {message.author.name}: {content[:80]}")

        history = []
        async for msg in message.channel.history(limit=9, before=message):
            history.insert(0, {"author": msg.author.name, "content": msg.content[:300]})

        chunks = []
        try:
            from agent import retrieval as ret
            loop = asyncio.get_event_loop()
            chunks = await loop.run_in_executor(
                None, lambda: ret.multi_retrieve([content], namespaces=ret.NS_BROAD_PLUS, top_k_each=5)
            )
        except Exception as e:
            logger.warning(f"Retrieval skipped: {e}")

        async with message.channel.typing():
            response = await presence.generate_mention_response(
                username=message.author.name,
                message=content,
                context_messages=history,
                corpus_chunks=chunks,
            )

        await message.reply(response)

    # ── Notebook watcher ─────────────────────────────────────────────────────

    @tasks.loop(minutes=30)
    async def task_notebook(self):
        state = st.load()
        last_commit = state.get("last_notebook_commit")

        if last_commit is None:
            # First run: initialize without posting historical entries
            head = nw.get_head_commit()
            state["last_notebook_commit"] = head
            state["notebook_entries_posted"] = []
            st.save(state)
            logger.info(f"Notebook watcher initialized at {head}")
            return

        new_entries = nw.get_new_notebook_entries(last_commit)
        posted = set(state.get("notebook_entries_posted", []))
        channel = self.get_channel(self.new_nature_id)

        for entry in new_entries:
            if entry["date"] in posted or not entry["path"].exists():
                continue
            logger.info(f"Posting notebook entry {entry['date']}")
            try:
                post = await presence.generate_notebook_post(
                    entry["date"], entry["path"], entry["github_url"]
                )
                if channel:
                    await channel.send(post)
                posted.add(entry["date"])
            except Exception as e:
                logger.error(f"Failed to post notebook entry: {e}")

        head = nw.get_head_commit()
        state["last_notebook_commit"] = head
        state["notebook_entries_posted"] = list(posted)
        st.save(state)

        if new_entries:
            # Re-ingest after new notebook entries so humboldt namespace stays current
            try:
                from agent.ingest import ingest_all
                await self.loop.run_in_executor(None, lambda: ingest_all(verbose=False))
                logger.info("humboldt namespace re-indexed after notebook update")
            except Exception as e:
                logger.warning(f"Post-notebook ingest failed: {e}")

    @task_notebook.before_loop
    async def before_task_notebook(self):
        await self.wait_until_ready()

    def _within_active_hours(self) -> bool:
        """Return True if current Pacific time is within configured active hours."""
        ah = self.config.get("discord", {}).get("active_hours", {})
        tz_name = ah.get("timezone", "America/Los_Angeles")
        start = ah.get("start", 8)
        end = ah.get("end", 23)
        now = datetime.now(ZoneInfo(tz_name))
        active = start <= now.hour < end
        if not active:
            logger.info(f"Outside active hours ({now.strftime('%H:%M %Z')}), skipping")
        return active

    # ── #new-nature presence ─────────────────────────────────────────────────

    @tasks.loop(minutes=30)
    async def task_new_nature(self):
        if not self._within_active_hours():
            return

        state = st.load()
        last_msg_id = state.get("last_new_nature_message_id")
        channel = self.get_channel(self.new_nature_id)
        if not channel:
            return

        kwargs: dict = {"limit": 100}
        if last_msg_id:
            kwargs["after"] = discord.Object(id=int(last_msg_id))

        messages = []
        latest_id = None
        async for msg in channel.history(**kwargs):
            if msg.author != self.user:
                messages.append({"author": msg.author.name, "content": msg.content[:400]})
            latest_id = str(msg.id)

        if latest_id:
            state["last_new_nature_message_id"] = latest_id
            st.save(state)

        if not messages:
            return

        messages.reverse()
        logger.info(f"Checking {len(messages)} new #new-nature messages")

        try:
            response = await presence.generate_new_nature_response(messages)
            if response and channel:
                await channel.send(response)
        except Exception as e:
            logger.error(f"new-nature response error: {e}")

    @task_new_nature.before_loop
    async def before_task_new_nature(self):
        await self.wait_until_ready()

    # ── Feed monitor ─────────────────────────────────────────────────────────

    @tasks.loop(hours=12)
    async def task_feeds(self):
        state = st.load()
        last_check_str = state.get("last_feed_check")

        if last_check_str is None:
            # First run: record current time, skip historical items
            state["last_feed_check"] = datetime.now(timezone.utc).isoformat()
            st.save(state)
            logger.info("Feed monitor initialized")
            return

        last_check = datetime.fromisoformat(last_check_str)
        feeds = self.config.get("feeds", {}).get("sources", [])
        hypotheses = _active_hypotheses()
        saved_titles = []

        for feed_cfg in feeds:
            try:
                items = fm.fetch_new_items(feed_cfg["url"], last_check)
                for item in items[:15]:
                    relevant, note = await presence.check_feed_relevance(
                        item["title"], item["summary"], hypotheses
                    )
                    if relevant:
                        fm.save_to_inbox(item, note)
                        saved_titles.append(item["title"])
                        logger.info(f"Inbox: {item['title'][:60]}")
            except Exception as e:
                logger.error(f"Feed error ({feed_cfg.get('name')}): {e}")

        state["last_feed_check"] = datetime.now(timezone.utc).isoformat()
        st.save(state)

        if saved_titles:
            try:
                operator = await self.fetch_user(self.operator_id)
                titles_str = "\n".join(f"- {t[:80]}" for t in saved_titles[:5])
                suffix = f"\n…and {len(saved_titles) - 5} more" if len(saved_titles) > 5 else ""
                await operator.send(
                    f"Humboldt inbox: {len(saved_titles)} new item(s) from feeds:\n{titles_str}{suffix}"
                )
            except Exception as e:
                logger.warning(f"Operator DM failed: {e}")

    @task_feeds.before_loop
    async def before_task_feeds(self):
        await self.wait_until_ready()
