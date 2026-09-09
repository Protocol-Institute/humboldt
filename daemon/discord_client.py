"""Humboldt Discord bot — event handlers and scheduled presence tasks."""

import asyncio
import logging
import os
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# Max age for a message to be eligible as a thread anchor (seconds)
_THREAD_ANCHOR_MAX_AGE = 15 * 60  # 15 minutes

# TODO(proactive-engagement): _new_nature_tick's self-initiated "jump into the
# conversation" posting (generate_new_nature_response) was disabled 2026-07-24
# for being too chatty/redundant even at its 1/day cap. Before re-enabling,
# it needs real tuning — sharper judgment on whether Humboldt actually has
# something worth adding vs. generic engagement, probably corpus-grounded
# content requirements similar to task_weekly_digest, and a longer natural
# gap between posts. Capture (idea/link extraction) is unaffected and keeps
# running silently. See daemon/presence.py:generate_new_nature_response.
_PROACTIVE_ENGAGEMENT_ENABLED = False


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
from . import pause as pz
from . import notebook_watcher as nw
from . import feed_monitor as fm
from . import presence
from . import capture as cap
from . import people as ppl
from . import conversation_review as cr
from .costs import BudgetExceeded

logger = logging.getLogger("humboldt.discord")
_ROOT = Path(__file__).parent.parent


def _load_config() -> dict:
    config_path = Path(__file__).parent / "config.yaml"
    if config_path.exists():
        return yaml.safe_load(config_path.read_text()) or {}
    return {}


def _active_hypotheses() -> list[str]:
    cl_dir = _ROOT / "research" / "cl"
    result = []
    for f in sorted(cl_dir.glob("CL-*.yaml")):
        try:
            cl = yaml.safe_load(f.read_text())
            if cl.get("research_status") != "archived":
                result.append(f"{cl.get('id')} — {cl.get('name')}")
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
        self.task_feed_digest.start()
        self.task_conversation_review.start()
        self.task_weekly_digest.start()
        self.task_read_budget_watch.start()
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

    async def _already_replied_to(self, msg: discord.Message) -> bool:
        """Check Discord history: has Humboldt already sent a reply to this specific message?"""
        async for recent in msg.channel.history(limit=50, after=msg):
            if recent.author == self.user and recent.reference:
                if recent.reference.message_id == msg.id:
                    return True
        return False

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
        # force_full_scan in state overrides brief_restart detection (used for manual catch-up).
        brief_restart = False
        if state.get("force_full_scan"):
            fresh = st.load()
            fresh.pop("force_full_scan", None)
            st.save(fresh)
        else:
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
        scan_limit = 100 if brief_restart else 500
        async for msg in channel.history(limit=scan_limit, after=discord.Object(id=int(last_msg_id))):
            latest_id = str(msg.id)
            if msg.author != self.user and self.user in msg.mentions:
                if str(msg.id) not in responded_ids:
                    missed.append(msg)

        # Advance cursor with a fresh load so we never regress it and never
        # overwrite fields (like responded_mention_ids) written by concurrent coroutines.
        if latest_id:
            fresh = st.load()
            current = fresh.get("last_new_nature_message_id") or "0"
            if latest_id > current:
                fresh["last_new_nature_message_id"] = latest_id
            st.save(fresh)

        if not missed:
            return

        logger.info(f"Checking {len(missed)} missed @mention(s) against Discord history (brief_restart={brief_restart})")
        for msg in reversed(missed):
            content = msg.content.replace(f"<@{self.user.id}>", "").strip()
            if not content:
                continue
            if pz.is_paused():
                try:
                    await msg.reply(pz.offline_message())
                    fresh = st.load()
                    st.record_responded_mention(fresh, str(msg.id))
                    st.save(fresh)
                except Exception as e:
                    logger.warning(f"Paused-offline reply failed for {msg.id}: {e}")
                continue
            # Primary duplicate guard: check Discord's own history for an existing reply.
            # This survives state resets, reconnects, and race conditions.
            try:
                if await self._already_replied_to(msg):
                    logger.info(f"Skipping @mention {msg.id} — reply already exists in channel")
                    fresh = st.load()
                    st.record_responded_mention(fresh, str(msg.id))
                    st.save(fresh)
                    continue
            except Exception as e:
                logger.warning(f"Discord reply-check failed for {msg.id}: {e}")

            history = []
            name_to_id: dict[str, str] = {msg.author.name: str(msg.author.id)}
            async for ctx in channel.history(limit=9, before=msg):
                history.insert(0, {"author": ctx.author.name, "content": ctx.content[:300]})
                name_to_id[ctx.author.name] = str(ctx.author.id)
            chunks = []
            corpus_offline = False
            from agent import retrieval as ret
            try:
                chunks = await self.loop.run_in_executor(
                    None, lambda: ret.multi_retrieve([content], namespaces=ret.NS_BROAD_PLUS, top_k_each=ret.REPLY_TOP_K, op="discord_mention")
                )
            except ret.RetrievalUnavailable as e:
                corpus_offline = True
                logger.warning(f"Corpus offline for catch-up mention: {e}")
            except Exception as e:  # noqa: BLE001
                logger.warning(f"Retrieval failed for catch-up mention: {e}")
            try:
                response = await presence.generate_mention_response(
                    username=msg.author.name,
                    message=content,
                    context_messages=history,
                    corpus_chunks=chunks,
                    corpus_offline=corpus_offline,
                )
                prefix = "" if brief_restart else "*(catching up from while I was offline)*\n"
                await msg.reply(f"{prefix}{response}")
                # Secondary guard: record in state so fast-path skips the Discord check next time.
                fresh = st.load()
                st.record_responded_mention(fresh, str(msg.id))
                st.save(fresh)
            except Exception as e:
                logger.error(f"Missed mention response failed: {e}", exc_info=True)
                try:
                    await msg.reply("*(Something went wrong — couldn't generate a response.)*")
                except Exception:
                    pass

    async def _catchup_all_channels(self, report_channel, since_date: str) -> None:
        """
        Scan every accessible text channel (and active threads) for @mentions since
        since_date that Humboldt hasn't replied to. Responds with the offline-catchup prefix.
        Used by the !catchup operator DM command after extended outages.
        """
        from datetime import datetime, timezone
        since_dt = datetime.fromisoformat(since_date).replace(tzinfo=timezone.utc)
        responded_ids: set[str] = set(st.load().get("responded_mention_ids", []))

        guild = self.get_guild(self.guild_id)
        if not guild:
            await report_channel.send("Guild not found.")
            return

        # Collect all scannable channels: text channels + active thread channels
        channels_to_scan = []
        for ch in guild.text_channels:
            try:
                if ch.permissions_for(guild.me).read_message_history:
                    channels_to_scan.append(ch)
            except Exception:
                pass
        try:
            active_threads = await guild.active_threads()
            for t in active_threads.threads:
                channels_to_scan.append(t)
        except Exception:
            pass

        total_found = 0
        total_replied = 0
        for ch in channels_to_scan:
            try:
                async for msg in ch.history(limit=500, after=discord.Object(id=self._dt_to_snowflake(since_dt))):
                    if msg.author == self.user:
                        continue
                    if self.user not in msg.mentions:
                        continue
                    if str(msg.id) in responded_ids:
                        continue
                    total_found += 1
                    # Check Discord history for an existing reply
                    try:
                        if await self._already_replied_to(msg):
                            fresh = st.load()
                            st.record_responded_mention(fresh, str(msg.id))
                            st.save(fresh)
                            responded_ids.add(str(msg.id))
                            continue
                    except Exception:
                        pass

                    content = msg.content.replace(f"<@{self.user.id}>", "").strip()
                    if not content:
                        continue

                    if pz.is_paused():
                        try:
                            await msg.reply(pz.offline_message())
                            fresh = st.load()
                            st.record_responded_mention(fresh, str(msg.id))
                            st.save(fresh)
                            responded_ids.add(str(msg.id))
                            total_replied += 1
                        except Exception as e:
                            logger.warning(f"Paused-offline reply failed for {msg.id}: {e}")
                        continue

                    history = []
                    name_to_id: dict[str, str] = {msg.author.name: str(msg.author.id)}
                    async for ctx in ch.history(limit=9, before=msg):
                        history.insert(0, {"author": ctx.author.name, "content": ctx.content[:300]})
                        name_to_id[ctx.author.name] = str(ctx.author.id)

                    chunks = []
                    corpus_offline = False
                    from agent import retrieval as ret
                    try:
                        chunks = await self.loop.run_in_executor(
                            None, lambda c=content: ret.multi_retrieve([c], namespaces=ret.NS_BROAD_PLUS, top_k_each=ret.REPLY_TOP_K, op="discord_mention")
                        )
                    except ret.RetrievalUnavailable as e:
                        corpus_offline = True
                        logger.warning(f"Corpus offline for mention: {e}")
                    except Exception as e:  # noqa: BLE001
                        logger.warning(f"Retrieval failed for mention: {e}")

                    try:
                        response = await presence.generate_mention_response(
                            username=msg.author.name,
                            message=content,
                            context_messages=history,
                            corpus_chunks=chunks,
                            corpus_offline=corpus_offline,
                        )
                        thread_title, body = _parse_thread_response(response)
                        body = _resolve_mentions(body, name_to_id)
                        await msg.reply(f"*(catching up from while I was offline)*\n{body}")
                        logger.info(f"Catchup: replied to @mention from {msg.author.name} in #{ch.name}: {content[:60]}")
                        fresh = st.load()
                        st.record_responded_mention(fresh, str(msg.id))
                        st.save(fresh)
                        responded_ids.add(str(msg.id))
                        total_replied += 1
                    except Exception as e:
                        logger.error(f"Catchup reply failed for {msg.id}: {e}", exc_info=True)
                        try:
                            await msg.reply("*(Something went wrong — couldn't generate a response.)*")
                        except Exception:
                            pass
            except Exception as e:
                logger.warning(f"Catchup: could not scan #{getattr(ch, 'name', ch.id)}: {e}")

        await report_channel.send(
            f"Catchup complete. Found {total_found} unresponded @mention(s) since {since_date}; "
            f"replied to {total_replied}."
        )

    @staticmethod
    def _dt_to_snowflake(dt) -> int:
        """Convert a datetime to a Discord snowflake ID for use as history `after=` cursor."""
        DISCORD_EPOCH = 1420070400000
        ts_ms = int(dt.timestamp() * 1000)
        return (ts_ms - DISCORD_EPOCH) << 22

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
        elif cmd.startswith("!catchup"):
            # !catchup-all — scan all guild channels for missed @mentions since blackout
            # Optional: !catchup 2026-06-04  (defaults to Jun 4 blackout start)
            parts = cmd.split()
            since_date = parts[1] if len(parts) > 1 else "2026-06-04"
            await message.channel.send(f"Scanning all channels for missed @mentions since {since_date}…")
            await self._catchup_all_channels(message.channel, since_date)
        else:
            await message.channel.send(f"Unknown command `{cmd}`. Available: `!reload`, `!status`, `!catchup [YYYY-MM-DD]`.")

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

        if pz.is_paused():
            await message.reply(pz.offline_message())
            return

        history = []
        name_to_id: dict[str, str] = {message.author.name: str(message.author.id)}
        async for msg in message.channel.history(limit=9, before=message):
            history.insert(0, {"author": msg.author.name, "content": msg.content[:300]})
            name_to_id[msg.author.name] = str(msg.author.id)

        chunks = []
        corpus_offline = False
        from agent import retrieval as ret
        try:
            loop = asyncio.get_event_loop()
            chunks = await loop.run_in_executor(
                None, lambda: ret.multi_retrieve([content], namespaces=ret.NS_BROAD_PLUS, top_k_each=ret.REPLY_TOP_K, op="discord_mention")
            )
        except ret.RetrievalUnavailable as e:
            corpus_offline = True
            logger.warning(f"Corpus offline: {e}")
        except Exception as e:
            logger.warning(f"Retrieval skipped: {e}")

        # Fetch person context (None for first-time interactions)
        person_context = ppl.get_person_context(message.author.name)

        try:
            async with message.channel.typing():
                response = await presence.generate_mention_response(
                    username=message.author.name,
                    message=content,
                    context_messages=history,
                    corpus_chunks=chunks,
                    person_context=person_context,
                    corpus_offline=corpus_offline,
                )
        except BudgetExceeded as e:
            logger.warning(f"Budget exceeded — skipping @mention response: {e}")
            await message.reply("I've hit my daily API budget and am offline until midnight. Back tomorrow.")
            return
        except Exception as e:
            logger.error(f"Mention response failed: {e}", exc_info=True)
            await message.reply("*(Something went wrong on my end — couldn't generate a response.)*")
            return

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
        Record a direct @mention interaction, then write a person notebook entry
        if either signal threshold is crossed: interaction count OR useful
        contribution count >= NOTEBOOK_THRESHOLD. Engaging with Humboldt at all
        is high-value signal, so interactions alone suffice to trigger the entry.
        """
        await self.loop.run_in_executor(
            None,
            lambda: ppl.record_interaction(username, user_id, message_snippet, channel),
        )
        if ppl.needs_person_notebook_entry(username):
            logger.info(f"Writing person notebook entry for @{username} (threshold crossed)")
            try:
                from agent.person_notebook import generate_person_notebook_entry
                out = await self.loop.run_in_executor(
                    None, lambda: generate_person_notebook_entry(username)
                )
                if out:
                    logger.info(f"Person notebook entry written: {out}")
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
        """
        Watch for new notebook commits and keep infra fresh (re-index, publish
        site, advance pre-notebook cursor). Discord announcement of notebook
        content is handled separately, on a weekly cadence, by task_weekly_digest —
        this task no longer posts per entry.
        """
        state = st.load()
        last_commit = state.get("last_notebook_commit")

        if last_commit is None:
            # First run: initialize without processing historical entries
            head = nw.get_head_commit()
            state["last_notebook_commit"] = head
            st.save(state)
            logger.info(f"Notebook watcher initialized at {head}")
            return

        new_entries = nw.get_new_notebook_entries(last_commit)

        head = nw.get_head_commit()
        fresh = st.load()
        fresh["last_notebook_commit"] = head
        st.save(fresh)

        if new_entries:
            logger.info(
                f"Notebook watcher: {len(new_entries)} new "
                f"entr{'y' if len(new_entries) == 1 else 'ies'} detected"
            )
            # Re-ingest after new notebook entries so humboldt namespace stays current.
            # Skipped while paused (no Pinecone writes) — ingest_all() is content-hash
            # incremental, so nothing is lost: the next unpaused run picks up everything
            # that changed in the meantime.
            if pz.is_paused():
                logger.info("Paused — skipping Pinecone re-index")
            else:
                try:
                    from agent.ingest import ingest_all
                    await self.loop.run_in_executor(None, lambda: ingest_all(verbose=False))
                    logger.info("humboldt namespace re-indexed after notebook update")
                except Exception as e:
                    logger.warning(f"Post-notebook ingest failed: {e}")

            # Rebuild and deploy humboldt-site to CF Pages
            try:
                from agent.publish_site import publish_site
                ok = await self.loop.run_in_executor(None, lambda: publish_site(verbose=False))
                if ok:
                    logger.info("Published notebook update to humboldt-site (CF Pages)")
                else:
                    logger.warning("Post-notebook publish-site returned failure")
            except Exception as e:
                logger.warning(f"Post-notebook publish failed: {e}")

            # Advance pre-notebook cursor — new entries have consumed the queue
            try:
                from agent.pre_notebook import mark_consumed
                await self.loop.run_in_executor(None, mark_consumed)
                logger.info("Pre-notebook cursor advanced after notebook commit")
            except Exception as e:
                logger.warning(f"Pre-notebook cursor advance failed: {e}")

    @task_notebook.before_loop
    async def before_task_notebook(self):
        await self.wait_until_ready()

    @tasks.loop(hours=24)
    async def task_weekly_digest(self):
        """
        Weekly pass: post ONE #new-nature digest synthesizing the past week's
        notebook entries against current research state, instead of announcing
        every entry as it lands (that per-entry cadence moved daily once
        conversation_review started writing a notebook section every day).
        """
        if pz.is_paused():
            return
        state = st.load()
        last_digest = state.get("last_weekly_digest_date")
        today = date.today()

        if last_digest is None:
            # First run: start the clock, don't post historical backlog
            state["last_weekly_digest_date"] = today.isoformat()
            st.save(state)
            logger.info("Weekly digest initialized")
            return

        last_date = date.fromisoformat(last_digest)
        if (today - last_date).days < 7:
            return  # not due yet

        nb_dir = _ROOT / "notebook"
        week_entries: list[tuple[str, Path]] = []
        for f in sorted(nb_dir.glob("????-??-??.md")):
            try:
                entry_date = date.fromisoformat(f.stem)
            except ValueError:
                continue
            if last_date < entry_date <= today:
                week_entries.append((f.stem, f))

        if not week_entries:
            logger.info("Weekly digest: no notebook entries since last digest, skipping post")
            fresh = st.load()
            fresh["last_weekly_digest_date"] = today.isoformat()
            st.save(fresh)
            return

        try:
            from agent import notebook_index as nbi
            notebook_url = nbi.entry_url(week_entries[-1][0])
            post = await presence.generate_weekly_digest_post(week_entries, notebook_url)
            channel = self.get_channel(self.new_nature_id)
            if channel:
                await channel.send(post)
            logger.info(f"Weekly digest posted ({len(week_entries)} entries synthesized)")
        except Exception as e:
            logger.error(f"Weekly digest failed: {e}")
            return

        fresh = st.load()
        fresh["last_weekly_digest_date"] = today.isoformat()
        st.save(fresh)

    @task_weekly_digest.before_loop
    async def before_task_weekly_digest(self):
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
        if pz.is_paused():
            return
        if not self._within_active_hours():
            return

        # One proactive post per calendar day — skip the check entirely if already posted today.
        from datetime import date as _date
        today_str = _date.today().isoformat()
        _quick_state = st.load()
        if _quick_state.get("last_proactive_post_date") == today_str:
            logger.debug("Proactive post already made today — skipping #new-nature check")
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

        # Update state with a fresh load so concurrent coroutine saves aren't overwritten.
        if latest_id:
            fresh = st.load()
            current = fresh.get("last_new_nature_message_id") or "0"
            if latest_id > current:
                fresh["last_new_nature_message_id"] = latest_id
            if messages:
                fresh["last_new_nature_activity"] = datetime.now(timezone.utc).isoformat()
            st.save(fresh)

        if not messages:
            return

        messages.reverse()  # chronological order for the prompt
        logger.info(f"Checking {len(messages)} new #new-nature messages")

        if not _PROACTIVE_ENGAGEMENT_ENABLED:
            # Posting disabled — see TODO(proactive-engagement) at top of file.
            # Capture still runs so ideas/links aren't lost while this is off.
            try:
                n_captured = await cap.run_capture(messages, "#new-nature")
                if n_captured:
                    logger.info(f"Captured {n_captured} item(s) from #new-nature")
            except Exception as e:
                logger.warning(f"new-nature capture error: {e}")
            return

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
            body = _resolve_mentions(response_text, name_to_id)
            await channel.send(body)
            fresh = st.load()
            fresh["last_proactive_post_date"] = today_str
            st.save(fresh)

        if n_captured:
            logger.info(f"Captured {n_captured} item(s) from #new-nature")

    # ── Conversation review ───────────────────────────────────────────────────

    @tasks.loop(hours=24)
    async def task_conversation_review(self):
        """
        Daily pass: synthesize ideas from recent Discord into notebook +
        promote inbox link captures to bibliography/references.yaml.
        """
        if pz.is_paused():
            return
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
        fresh = st.load()
        fresh["last_conversation_review"] = date.today().isoformat()
        st.save(fresh)

    @task_conversation_review.before_loop
    async def before_task_conversation_review(self):
        await self.wait_until_ready()

    # ── Feed monitor ─────────────────────────────────────────────────────────

    @tasks.loop(hours=12)
    async def task_feeds(self):
        """
        Fetch, relevance-filter, and save new feed items to the inbox. Runs
        regardless of pause state — silent data collection, no Discord side
        effect. Saved items accumulate in state['pending_feed_items'] for
        task_feed_digest to report on weekly, instead of DMing the operator
        a raw title dump on every 12h check.
        """
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
        saved_items = []

        for feed_cfg in feeds:
            try:
                items = fm.fetch_new_items(feed_cfg["url"], last_check)
                for item in items[:15]:
                    relevant, note = await presence.check_feed_relevance(
                        item["title"], item["summary"], hypotheses
                    )
                    if relevant:
                        fm.save_to_inbox(item, note)
                        saved_items.append({"title": item["title"], "note": note})
                        logger.info(f"Inbox: {item['title'][:60]}")
            except Exception as e:
                logger.error(f"Feed error ({feed_cfg.get('name')}): {e}")

        fresh = st.load()
        fresh["last_feed_check"] = datetime.now(timezone.utc).isoformat()
        if saved_items:
            fresh.setdefault("pending_feed_items", []).extend(saved_items)
        st.save(fresh)

    @task_feeds.before_loop
    async def before_task_feeds(self):
        await self.wait_until_ready()

    @tasks.loop(hours=24)
    async def task_feed_digest(self):
        """
        Weekly pass: DM the operator ONE editorial synthesis of the week's
        feed-inbox additions, instead of a raw title dump on every 12h check
        (see task_feeds). Gated by pause like other proactive Discord output.
        """
        if pz.is_paused():
            return
        state = st.load()
        last_digest = state.get("last_feed_digest_date")
        today = date.today()

        if last_digest is None:
            # First run: start the clock, don't post historical backlog
            state["last_feed_digest_date"] = today.isoformat()
            st.save(state)
            logger.info("Feed digest initialized")
            return

        if (today - date.fromisoformat(last_digest)).days < 7:
            return  # not due yet

        pending = state.get("pending_feed_items", [])
        if not pending:
            logger.info("Feed digest: no new inbox items since last digest, skipping DM")
            fresh = st.load()
            fresh["last_feed_digest_date"] = today.isoformat()
            st.save(fresh)
            return

        try:
            post = await presence.generate_feed_digest_post(pending)
            operator = await self.fetch_user(self.operator_id)
            await operator.send(post)
            logger.info(f"Feed digest sent ({len(pending)} item(s) synthesized)")
        except Exception as e:
            logger.error(f"Feed digest failed: {e}")
            return

        fresh = st.load()
        fresh["last_feed_digest_date"] = today.isoformat()
        fresh["pending_feed_items"] = []
        st.save(fresh)

    @task_feed_digest.before_loop
    async def before_task_feed_digest(self):
        await self.wait_until_ready()

    # ── Corpus read budget ───────────────────────────────────────────────────

    @tasks.loop(hours=24)
    async def task_read_budget_watch(self):
        """
        Watch the Pinecone monthly read budget and DM the operator on the two
        events that matter: crossing the egress warn threshold, and the breaker
        tripping.

        This exists because the 2026-08 outage was found by accident weeks
        late. Every other signal in this system reports *spend after the fact*;
        this is the only one that fires while there is still budget left to
        protect. Alerts once per month per event — a daily nag would train the
        operator to ignore it.

        Pause-gated for consistency with every other Discord side effect (see
        feedback on pause completeness), but always logged at WARNING so a
        paused daemon still leaves the evidence in daemon.log.
        """
        from agent import read_budget as rb
        from agent import read_egress as re_

        state = st.load()
        month = re_.month_key()
        alerts = []

        until = rb.paused_until()
        if until and state.get("read_outage_alerted_until") != until:
            alerts.append(f"⚠️ **Corpus reads are OFFLINE until {until}.**\n{rb.reason()[:300]}")
            state["read_outage_alerted_until"] = until

        s = re_.summary(month)
        if (s["fraction"] >= re_.WARN_FRACTION
                and state.get("read_egress_warned_month") != month):
            alerts.append(
                f"⚠️ **Pinecone read egress at {s['fraction'] * 100:.0f}% of the "
                f"monthly cap** ({month}, Python paths only — the site chat "
                f"Worker counts separately in KV).\n"
                f"Top paths: " + ", ".join(
                    f"{op} {n / 1_000_000:.0f}MB" for op, n in list(s["by_op"].items())[:3])
            )
            state["read_egress_warned_month"] = month

        if not alerts:
            return

        for a in alerts:
            logger.warning(a.replace("\n", " ")[:300])

        if pz.is_paused():
            st.save(state)  # still record it, so unpausing does not re-alert
            return

        try:
            operator = await self.fetch_user(self.operator_id)
            await operator.send("\n\n".join(alerts))
        except Exception as e:  # noqa: BLE001
            logger.error(f"Read-budget alert DM failed: {e}")
            return
        st.save(state)

    @task_read_budget_watch.before_loop
    async def before_task_read_budget_watch(self):
        await self.wait_until_ready()
