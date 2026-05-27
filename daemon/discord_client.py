"""Humboldt Discord bot — event handlers and scheduled presence tasks."""

import asyncio
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# Max age for a message to be eligible as a thread anchor (seconds)
_THREAD_ANCHOR_MAX_AGE = 15 * 60  # 15 minutes


def _parse_thread_response(text: str) -> tuple[str | None, str]:
    """
    Parse optional THREAD: prefix from model output.

    Returns (thread_title, response_body).
    thread_title is None for a normal channel post.
    """
    if text.startswith("THREAD:"):
        first_line, _, rest = text.partition("\n")
        title = first_line[7:].strip()[:90]
        body = rest.strip()
        if title and body:
            return title, body
    return None, text


def _resolve_mentions(text: str, name_to_id: dict[str, str]) -> str:
    """
    Replace @username with <@user_id> for real Discord pings.

    Only replaces names that appear in name_to_id; unknown @-words are left as-is.
    """
    import re

    def replace(m: re.Match) -> str:
        uid = name_to_id.get(m.group(1))
        return f"<@{uid}>" if uid else m.group(0)

    return re.sub(r"@([\w._-]+)", replace, text)

import discord
import signal
import yaml
from discord.ext import tasks

from . import state as st
from . import notebook_watcher as nw
from . import feed_monitor as fm
from . import presence
from . import capture as cap
from . import people as ppl
from . import conversation_review as cr

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
        self.reload_requested = False  # set before close() to trigger os.execv in runner

    async def setup_hook(self):
        self.task_notebook.start()
        self.task_feeds.start()
        self.task_conversation_review.start()
        # SIGUSR1 triggers a graceful hot-reload: saves state, then re-execs
        self.loop.add_signal_handler(signal.SIGUSR1, self._schedule_reload)
        # new-nature uses a manual loop for adaptive check intervals
        self.loop.create_task(self._new_nature_loop())

    def _schedule_reload(self) -> None:
        asyncio.create_task(self._graceful_reload(notify_operator=False))

    async def _graceful_reload(self, notify_operator: bool = True) -> None:
        logger.info("Graceful reload initiated")
        if notify_operator:
            try:
                operator = await self.fetch_user(self.operator_id)
                await operator.send("Reloading with updated code — back in a moment.")
            except Exception:
                pass
        self.reload_requested = True
        await self.close()  # triggers our close() override which saves clean-shutdown marker

    async def close(self) -> None:
        state = st.load()
        state["last_clean_shutdown"] = datetime.now(timezone.utc).isoformat()
        st.save(state)
        pid_file = Path(__file__).parent / "daemon.pid"
        pid_file.unlink(missing_ok=True)
        logger.info("Clean shutdown recorded")
        await super().close()

    async def on_ready(self):
        logger.info(f"Humboldt online: {self.user} (id {self.user.id})")
        state = st.load()
        state["last_startup"] = datetime.now(timezone.utc).isoformat()
        # Write PID file so `daemon restart` can find us
        pid_file = Path(__file__).parent / "daemon.pid"
        pid_file.write_text(str(os.getpid()))
        st.save(state)
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

        # Determine whether this is a brief code-update restart (< 5 min offline).
        # If so, skip the "catching up" prefix — we weren't really away.
        brief_restart = False
        last_shutdown_str = state.get("last_clean_shutdown")
        last_startup_str = state.get("last_startup")
        if last_shutdown_str and last_startup_str:
            shutdown_dt = datetime.fromisoformat(last_shutdown_str)
            startup_dt = datetime.fromisoformat(last_startup_str)
            offline_seconds = (startup_dt - shutdown_dt).total_seconds()
            brief_restart = 0 < offline_seconds < 300  # < 5 minutes = code-update restart

        responded_ids: set[str] = set(state.get("responded_mention_ids", []))

        missed = []
        latest_id: str | None = None
        async for msg in channel.history(limit=100, after=discord.Object(id=int(last_msg_id))):
            latest_id = str(msg.id)
            if msg.author != self.user and self.user in msg.mentions:
                if str(msg.id) not in responded_ids:
                    missed.append(msg)

        # Advance the cursor past everything we just scanned, including bot messages
        if latest_id:
            state["last_new_nature_message_id"] = latest_id
            st.save(state)

        if not missed:
            return

        logger.info(f"Responding to {len(missed)} missed @mention(s) (brief_restart={brief_restart})")
        for msg in reversed(missed):
            content = msg.content.replace(f"<@{self.user.id}>", "").strip()
            if not content:
                continue
            history = []
            name_to_id: dict[str, str] = {msg.author.name: str(msg.author.id)}
            async for ctx in channel.history(limit=9, before=msg):
                history.insert(0, {"author": ctx.author.name, "content": ctx.content[:300]})
                name_to_id[ctx.author.name] = str(ctx.author.id)
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
                prefix = "" if brief_restart else "*(catching up from while I was offline)*\n"
                await msg.reply(f"{prefix}{response}")
                # Mark as responded so a subsequent restart doesn't re-process it
                state = st.load()
                st.record_responded_mention(state, str(msg.id))
                st.save(state)
            except Exception as e:
                logger.error(f"Missed mention response failed: {e}")

    async def _handle_operator_dm(self, message: discord.Message) -> None:
        """Handle control commands sent as DMs from the operator."""
        cmd = message.content.strip().lower()
        if cmd == "!reload":
            await message.channel.send("Reloading with updated code — back in a moment.")
            await self._graceful_reload(notify_operator=False)
        elif cmd == "!status":
            state = st.load()
            last_startup = state.get("last_startup", "unknown")
            last_shutdown = state.get("last_clean_shutdown", "never")
            await message.channel.send(
                f"Online since: {last_startup}\n"
                f"Last clean shutdown: {last_shutdown}\n"
                f"Last #new-nature msg ID: {state.get('last_new_nature_message_id', 'none')}\n"
                f"Responded mention IDs tracked: {len(state.get('responded_mention_ids', []))}"
            )
        else:
            await message.channel.send(f"Unknown command `{cmd}`. Available: `!reload`, `!status`.")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        # DMs from the operator: control commands
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id == self.operator_id:
                await self._handle_operator_dm(message)
            return

        if self.user not in message.mentions:
            return

        content = message.content.replace(f"<@{self.user.id}>", "").strip()
        if not content:
            return

        logger.info(f"@mention from {message.author.name}: {content[:80]}")

        history = []
        name_to_id: dict[str, str] = {message.author.name: str(message.author.id)}
        async for msg in message.channel.history(limit=9, before=message):
            history.insert(0, {"author": msg.author.name, "content": msg.content[:300]})
            name_to_id[msg.author.name] = str(msg.author.id)

        chunks = []
        try:
            from agent import retrieval as ret
            loop = asyncio.get_event_loop()
            chunks = await loop.run_in_executor(
                None, lambda: ret.multi_retrieve([content], namespaces=ret.NS_BROAD_PLUS, top_k_each=5)
            )
        except Exception as e:
            logger.warning(f"Retrieval skipped: {e}")

        # Fetch person context (None for first-time interactions)
        person_context = ppl.get_person_context(message.author.name)

        async with message.channel.typing():
            response = await presence.generate_mention_response(
                username=message.author.name,
                message=content,
                context_messages=history,
                corpus_chunks=chunks,
                person_context=person_context,
            )

        thread_title, body = _parse_thread_response(response)
        body = _resolve_mentions(body, name_to_id)
        if thread_title:
            try:
                thread = await message.create_thread(
                    name=thread_title,
                    auto_archive_duration=1440,
                )
                await thread.send(body)
                logger.info(f"Opened thread from @mention: '{thread_title}'")
            except discord.Forbidden:
                logger.warning("No thread permission, falling back to reply")
                await message.reply(body)
            except Exception as e:
                logger.error(f"Thread creation failed: {e}")
                await message.reply(body)
        else:
            await message.reply(body)

        # Advance the message cursor and mark this mention as responded to.
        # This prevents _scan_missed_mentions from re-processing it on restart.
        cursor_state = st.load()
        if str(message.id) > (cursor_state.get("last_new_nature_message_id") or "0"):
            cursor_state["last_new_nature_message_id"] = str(message.id)
        st.record_responded_mention(cursor_state, str(message.id))
        st.save(cursor_state)

        # Record this interaction and check notebook threshold (non-blocking)
        asyncio.create_task(
            self._record_interaction_and_check(
                username=message.author.name,
                user_id=str(message.author.id),
                message_snippet=content,
                channel=f"#{message.channel.name}",
            )
        )

        # Capture ideas/links from the conversation after replying (non-blocking)
        capture_messages = history + [{"author": message.author.name, "content": content}]
        asyncio.create_task(cap.run_capture(capture_messages, f"#{message.channel.name}"))

    # ── People memory ────────────────────────────────────────────────────────

    async def _record_interaction_and_check(
        self,
        username: str,
        user_id: str,
        message_snippet: str,
        channel: str,
    ) -> None:
        """
        Record a direct @mention interaction, then write a notebook entry if the
        person has crossed the recurring-interlocutor threshold.
        """
        person = await self.loop.run_in_executor(
            None,
            lambda: ppl.record_interaction(username, user_id, message_snippet, channel),
        )
        if ppl.needs_notebook_entry(username):
            logger.info(f"Writing person notebook entry for @{username}")
            try:
                entry_text = await presence.generate_person_notebook_entry(username, person)
                await self._append_person_to_notebook(username, entry_text)
                await self.loop.run_in_executor(
                    None, lambda: ppl.mark_notebook_entry_written(username)
                )
            except Exception as e:
                logger.error(f"Person notebook entry failed for @{username}: {e}")

    async def _append_person_to_notebook(self, username: str, entry_text: str) -> None:
        """Append a person-as-research-conversation entry to today's notebook file."""
        import datetime
        today = datetime.date.today().isoformat()
        nb_path = _ROOT / "notebook" / f"{today}.md"

        section = (
            f"\n\n---\n\n"
            f"## Research conversation: @{username}\n\n"
            f"{entry_text}\n"
        )

        if nb_path.exists():
            existing = nb_path.read_text()
            nb_path.write_text(existing.rstrip() + section)
        else:
            nb_path.write_text(
                f"# Lab Notebook — {today}\n\n"
                f"*Ongoing research conversations.*\n"
                + section
            )

        logger.info(f"Person notebook entry appended: {nb_path.name} (@{username})")

        # Commit the updated notebook entry
        import subprocess
        try:
            subprocess.run(
                ["git", "add", str(nb_path)],
                cwd=_ROOT, check=True, capture_output=True,
            )
            subprocess.run(
                ["git", "commit", "-m",
                 f"Notebook: research conversation entry for @{username}\n\n"
                 f"Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"],
                cwd=_ROOT, check=True, capture_output=True,
            )
            subprocess.run(
                ["git", "push", "origin", "main"],
                cwd=_ROOT, check=True, capture_output=True,
            )
        except subprocess.CalledProcessError as e:
            logger.warning(f"Person notebook commit failed: {e.stderr.decode()}")

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
                from agent import notebook_index as nbi
                entry_url = nbi.entry_url(entry["date"])
                post = await presence.generate_notebook_post(
                    entry["date"], entry["path"], entry["github_url"],
                    entry_url=entry_url,
                )
                announcement_id: str | None = None
                thread_id: str | None = None
                if channel:
                    msg = await channel.send(post)
                    announcement_id = str(msg.id)
                    # Create a discussion thread on the announcement
                    try:
                        thread = await msg.create_thread(
                            name=f"Discussion: {entry['date']}",
                            auto_archive_duration=10080,  # 7 days
                        )
                        thread_id = str(thread.id)
                        logger.info(f"Created discussion thread for {entry['date']}: {thread_id}")
                    except Exception as te:
                        logger.warning(f"Thread creation failed for {entry['date']}: {te}")
                # Persist announcement and thread IDs in index.yaml
                nbi.upsert_entry(
                    entry["date"],
                    discord_announcement_id=announcement_id,
                    discord_thread_id=thread_id,
                )
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

            # Publish new notebook entries to the PI website
            try:
                from agent.publish import publish
                published_entries = await self.loop.run_in_executor(None, publish)
                if published_entries:
                    logger.info(f"Published {len(published_entries)} notebook entry(ies) to website")
            except Exception as e:
                logger.warning(f"Post-notebook publish failed: {e}")

    @task_notebook.before_loop
    async def before_task_notebook(self):
        await self.wait_until_ready()

    async def _bot_post_context(self, n: int = 5) -> tuple[list[str], float]:
        """
        Single history scan returning:
          - recent_posts: last n bot messages, oldest first (for repetition avoidance)
          - last_post_age: seconds since most recent bot post (inf if none)
        """
        channel = self.get_channel(self.new_nature_id)
        if not channel:
            return [], float("inf")
        posts: list[str] = []
        last_age = float("inf")
        async for msg in channel.history(limit=80):
            if msg.author == self.user:
                if not posts:  # first seen = most recent
                    last_age = (datetime.now(timezone.utc) - msg.created_at).total_seconds()
                posts.append(msg.content[:400])
                if len(posts) >= n:
                    break
        return list(reversed(posts)), last_age

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

    # ── #new-nature presence (adaptive-interval manual loop) ─────────────────

    def _next_check_interval(self) -> int:
        """
        Return seconds until next #new-nature tick.

        Exponential back-off from last human message activity:
          < 4 min  → check in 90 s
          < 12 min → check in 3 min
          < 30 min → check in 8 min
          < 90 min → check in 20 min
          ≥ 90 min → check in 30 min  (steady state / no activity)
        """
        state = st.load()
        last_ts = state.get("last_new_nature_activity")
        if not last_ts:
            return 30 * 60

        last = datetime.fromisoformat(last_ts)
        age = (datetime.now(timezone.utc) - last).total_seconds()

        if age < 4 * 60:
            return 90
        if age < 12 * 60:
            return 3 * 60
        if age < 30 * 60:
            return 8 * 60
        if age < 90 * 60:
            return 20 * 60
        return 30 * 60

    async def _new_nature_loop(self):
        """Manual loop — calls _new_nature_tick() then sleeps for the adaptive interval."""
        await self.wait_until_ready()
        while not self.is_closed():
            try:
                await self._new_nature_tick()
            except Exception as e:
                logger.error(f"new-nature tick error: {e}")
            interval = self._next_check_interval()
            logger.debug(f"Next #new-nature check in {interval}s")
            await asyncio.sleep(interval)

    async def _new_nature_tick(self):
        """Single #new-nature check: read new messages, maybe respond, maybe capture."""
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

        messages: list[dict] = []
        latest_id: str | None = None
        latest_human_msg: discord.Message | None = None  # most recent non-bot msg (for threading)
        name_to_id: dict[str, str] = {}

        async for msg in channel.history(**kwargs):
            latest_id = str(msg.id)
            if msg.author != self.user:
                # @mentions are handled exclusively by on_message; skipping them here
                # prevents a duplicate post when on_message creates a thread and the tick
                # fires before the cursor has advanced past that message.
                if self.user in msg.mentions:
                    continue
                if latest_human_msg is None:
                    latest_human_msg = msg  # first seen = newest (history is reverse-chron)
                name_to_id[msg.author.name] = str(msg.author.id)
                messages.append({"author": msg.author.name, "content": msg.content[:400]})

        # Update state: advance message cursor; record activity time if humans posted
        if latest_id:
            state["last_new_nature_message_id"] = latest_id
            if messages:
                state["last_new_nature_activity"] = datetime.now(timezone.utc).isoformat()
            st.save(state)

        if not messages:
            return

        messages.reverse()  # chronological order for the prompt
        logger.info(f"Checking {len(messages)} new #new-nature messages")

        recent_bot_posts, last_bot_age = await self._bot_post_context(n=5)

        # Run presence check and capture in parallel
        try:
            response_text, n_captured = await asyncio.gather(
                presence.generate_new_nature_response(messages, recent_bot_posts=recent_bot_posts),
                cap.run_capture(messages, "#new-nature"),
                return_exceptions=True,
            )
        except Exception as e:
            logger.error(f"new-nature gather error: {e}")
            return

        if isinstance(response_text, Exception):
            logger.error(f"new-nature response error: {response_text}")
            response_text = None
        if isinstance(n_captured, Exception):
            logger.warning(f"new-nature capture error: {n_captured}")
            n_captured = 0

        if response_text and channel:
            thread_title, body = _parse_thread_response(response_text)
            body = _resolve_mentions(body, name_to_id)
            long_gap = last_bot_age > 30 * 60

            # Only thread if the anchor message is recent enough to be meaningful
            anchor_age = (
                (datetime.now(timezone.utc) - latest_human_msg.created_at).total_seconds()
                if latest_human_msg else float("inf")
            )
            if thread_title and latest_human_msg and anchor_age < _THREAD_ANCHOR_MAX_AGE:
                try:
                    thread = await latest_human_msg.create_thread(
                        name=thread_title,
                        auto_archive_duration=1440,
                    )
                    await thread.send(body)
                    logger.info(f"Opened thread: '{thread_title}'")
                except discord.Forbidden:
                    # No thread permission: fall back to a plain channel post
                    logger.warning("No thread permission — posting to channel instead")
                    await channel.send(body)
                except discord.HTTPException as e:
                    # 160004 = thread already exists on this message; drop silently
                    if e.code == 160004:
                        logger.info(f"Thread already exists on anchor message — skipping")
                    else:
                        logger.error(f"Thread creation failed (HTTP {e.status} code={e.code}): {e.text}")
                        await channel.send(body)
                except Exception as e:
                    logger.error(f"Thread creation failed unexpectedly: {e}")
                    await channel.send(body)
            else:
                if thread_title:
                    logger.debug(f"Thread '{thread_title}' skipped — anchor too old ({anchor_age:.0f}s)")
                await channel.send(body)

        if n_captured:
            logger.info(f"Captured {n_captured} item(s) from #new-nature")

    # ── Conversation review ───────────────────────────────────────────────────

    @tasks.loop(hours=24)
    async def task_conversation_review(self):
        """
        Daily pass: synthesize ideas from recent Discord into notebook +
        promote inbox link captures to bibliography/references.yaml.
        """
        state = st.load()
        last_review = state.get("last_conversation_review")

        # On first run, record the date and skip (no history to review yet)
        if last_review is None:
            from datetime import date
            state["last_conversation_review"] = date.today().isoformat()
            st.save(state)
            logger.info("Conversation review initialized")
            return

        channel = self.get_channel(self.new_nature_id)
        messages: list[dict] = []

        if channel:
            # Fetch all messages since last review (up to 200)
            async for msg in channel.history(limit=200):
                if msg.author != self.user:
                    messages.append({
                        "author": msg.author.name,
                        "content": msg.content[:400],
                    })
            messages.reverse()  # chronological order

        try:
            result = await cr.run_review(messages, last_review_date=last_review)
            logger.info(
                f"Conversation review done: "
                f"notebook={'yes' if result['notebook_written'] else 'no'}, "
                f"refs_added={result['references_added']}"
            )
        except Exception as e:
            logger.error(f"Conversation review failed: {e}")
            return

        # Harvest new thread comments → inbox/ for reorientation context
        try:
            from . import thread_farmer as tf
            n_harvested = await tf.run_harvest(self)
            if n_harvested:
                logger.info(f"Thread farmer: harvested {n_harvested} comment(s) from notebook threads")
        except Exception as e:
            logger.warning(f"Thread harvest failed: {e}")

        from datetime import date
        state["last_conversation_review"] = date.today().isoformat()
        st.save(state)

    @task_conversation_review.before_loop
    async def before_task_conversation_review(self):
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
            # Suppress DMs if we just restarted quickly (code-update restart < 5 min offline).
            # Items are still saved to inbox; the DM is just noise during active development.
            suppress_dm = False
            current_state = st.load()
            last_shutdown_str = current_state.get("last_clean_shutdown")
            last_startup_str = current_state.get("last_startup")
            if last_shutdown_str and last_startup_str:
                shutdown_dt = datetime.fromisoformat(last_shutdown_str)
                startup_dt = datetime.fromisoformat(last_startup_str)
                offline_seconds = (startup_dt - shutdown_dt).total_seconds()
                suppress_dm = 0 < offline_seconds < 300
            if suppress_dm:
                logger.info(f"Feed DM suppressed (brief restart): {len(saved_titles)} item(s) in inbox")
            else:
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
