"""
Humboldt — Protocol Institute research agent.

Usage:
    python3 -m agent.humboldt investigate "<topic>"
    python3 -m agent.humboldt hypothesize "<topic>"
    python3 -m agent.humboldt assess <law-id>
    python3 -m agent.humboldt theorize
    python3 -m agent.humboldt inventory
"""

import sys
import os
import json
import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from . import retrieval as ret
from . import synthesizer as synth
from . import prompts

RESEARCH_DIR = Path(__file__).parent.parent / "research"
LAWS_DIR = RESEARCH_DIR / "laws"
HYPOTHESES_DIR = RESEARCH_DIR / "hypotheses"
THEORIES_DIR = RESEARCH_DIR / "theories"
DATA_DIR = Path(__file__).parent.parent / "data" / "sessions"
LIBRARY_DIR = Path(__file__).parent.parent / "bibliography" / "deep-reads"
NOTES_DIR = Path(__file__).parent.parent / "bibliography" / "notes"


def _load_inventory() -> str:
    """Load all law YAML files as a single string."""
    files = sorted(LAWS_DIR.glob("*.yaml"))
    if not files:
        return "(no laws in inventory yet)"
    parts = []
    for f in files:
        parts.append(f"--- {f.name} ---\n" + f.read_text())
    return "\n\n".join(parts)


def _session_log_path(slug: str) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    date = datetime.date.today().isoformat()
    return DATA_DIR / f"{date}-{slug}.md"


def cmd_investigate(topic: str, namespaces: list[str] = ret.NS_BROAD):
    """Open-ended investigation of a topic."""
    soul = prompts.load_soul()
    print(f"\n=== HUMBOLDT: Investigating '{topic}' ===\n")

    # Generate targeted retrieval queries
    print("Generating retrieval queries...")
    sys_q, usr_q = prompts.hypothesis_prompt(soul, topic)
    queries_raw = synth.synthesize(sys_q, f"Generate 4 targeted search queries for: {topic}. Output only the queries, one per line.")
    queries = [l.strip().lstrip("0123456789. ") for l in queries_raw.splitlines() if l.strip()][:4]
    print(f"Queries: {queries}\n")

    # Retrieve from corpus
    print(f"Retrieving from corpus (namespaces: {namespaces})...")
    chunks = ret.multi_retrieve(queries, namespaces=namespaces, top_k_each=8)
    print(f"Retrieved {len(chunks)} unique chunks.\n")

    if not chunks:
        print("No corpus results found. Corpus may be thin on this topic.")
        return

    # Synthesis
    print("Synthesizing candidate laws...\n")
    system, user = prompts.investigation_prompt(soul, topic, chunks[:20])
    output = synth.synthesize_streaming(system, user)

    # Save session log
    slug = topic.lower().replace(" ", "-")[:40]
    log_path = _session_log_path(slug)
    log_path.write_text(
        f"# Humboldt Session — {topic}\n"
        f"Date: {datetime.date.today().isoformat()}\n\n"
        f"## Retrieval queries\n"
        + "\n".join(f"- {q}" for q in queries)
        + f"\n\n## Retrieved chunks: {len(chunks)}\n\n"
        f"## Synthesis output\n\n{output}\n"
    )
    print(f"\nSession log saved: {log_path}")
    print("Next: review output, create law YAML files in research/laws/")


def cmd_hypothesize(topic: str):
    """Generate candidate law hypotheses without writing files."""
    soul = prompts.load_soul()
    print(f"\n=== HUMBOLDT: Hypothesizing on '{topic}' ===\n")
    system, user = prompts.hypothesis_prompt(soul, topic)
    synth.synthesize_streaming(system, user)


def cmd_assess(law_id: str, namespaces: list[str] = ret.NS_ALL):
    """Gather evidence for a specific law."""
    soul = prompts.load_soul()
    law_files = list(LAWS_DIR.glob(f"{law_id}*.yaml"))
    if not law_files:
        print(f"No law file found matching '{law_id}' in {LAWS_DIR}")
        sys.exit(1)

    import yaml
    law = yaml.safe_load(law_files[0].read_text())
    statement = law.get("statement", "")
    print(f"\n=== HUMBOLDT: Assessing {law.get('id')} — {law.get('name')} ===\n")

    # Build adversarial + supporting queries
    queries = [
        statement[:200],
        f"counterexample {law.get('name', '')}",
        f"mechanism {law.get('name', '')}",
    ]
    if law.get("domains"):
        for d in law["domains"][:2]:
            queries.append(f"{law.get('name', '')} {d}")

    chunks = ret.multi_retrieve(queries, namespaces=namespaces, top_k_each=10)
    print(f"Retrieved {len(chunks)} unique chunks.\n")

    system, user = prompts.evidence_prompt(soul, statement, chunks[:20])
    print("Analyzing evidence...\n")
    synth.synthesize_streaming(system, user)


def cmd_deepread(doc_name: str, page_range: str = None):
    """
    Deep-read a document from bibliography/deep-reads/.

    Reads the actual PDF — never relies on training knowledge.
    Writes or updates reading notes in bibliography/notes/<doc>.md.

    Usage:
        humboldt deepread "simon"           # full document
        humboldt deepread "simon" "60-138"  # page range (1-indexed)
    """
    import pypdf

    # Find the PDF
    matches = sorted(LIBRARY_DIR.glob(f"*{doc_name}*.pdf"))
    if not matches:
        available = [p.name for p in sorted(LIBRARY_DIR.glob("*.pdf"))]
        print(f"No document matching '{doc_name}' in library.")
        if available:
            print(f"Available: {', '.join(available)}")
        return

    pdf_path = matches[0]
    doc_stem = pdf_path.stem
    print(f"\n=== HUMBOLDT: Deep reading '{pdf_path.name}' ===\n")

    # Parse page range (1-indexed, inclusive)
    reader = pypdf.PdfReader(str(pdf_path))
    total = len(reader.pages)
    if page_range:
        parts = page_range.split("-")
        start = max(0, int(parts[0]) - 1)
        end = min(total, int(parts[1]) if len(parts) > 1 else total)
        range_label = f"pp. {start+1}–{end} of {total}"
    else:
        start, end = 0, total
        range_label = f"full document ({total} pages)"

    # Extract text
    print(f"Extracting text ({range_label})...")
    pages_text = []
    for i in range(start, end):
        text = reader.pages[i].extract_text() or ""
        if text.strip():
            pages_text.append(f"[p.{i+1}]\n{text}")
    extracted = "\n\n".join(pages_text)

    if not extracted.strip():
        print("No text extracted — PDF may be image-based or encrypted.")
        return

    print(f"Extracted {len(extracted):,} characters from {len(pages_text)} pages.\n")

    # Synthesize
    soul = prompts.load_soul()
    doc_title = doc_stem.replace("-", " ").title()
    system, user = prompts.deep_read_prompt(soul, doc_title, range_label, extracted)

    print("Synthesizing deep-read notes...\n")
    output = synth.synthesize_streaming(system, user)

    # Write or append notes
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    notes_file = NOTES_DIR / f"{doc_stem}.md"
    if notes_file.exists():
        existing = notes_file.read_text()
        # Append new reading session under a separator
        notes_file.write_text(
            existing.rstrip() + f"\n\n---\n\n## Reading session: {range_label}\n\n{output}\n"
        )
        print(f"\nNotes appended to: {notes_file}")
    else:
        notes_file.write_text(
            f"# Deep Read Notes: {doc_title}\n\n"
            f"*Source: `bibliography/deep-reads/{pdf_path.name}`*\n\n"
            f"---\n\n## Reading session: {range_label}\n\n{output}\n"
        )
        print(f"\nNotes written to: {notes_file}")

    print("Next: review notes, promote candidate laws to research/hypotheses/")


def cmd_library():
    """List documents available in the deep-read library."""
    pdfs = sorted(LIBRARY_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"Library is empty. Add PDFs to {LIBRARY_DIR}")
        return
    print(f"\n=== HUMBOLDT Library — {len(pdfs)} document(s) ===\n")
    for pdf in pdfs:
        notes_file = NOTES_DIR / f"{pdf.stem}.md"
        status = "notes exist" if notes_file.exists() else "no notes yet"
        print(f"  {pdf.name}  [{status}]")
    print()


def cmd_theorize():
    """Scan inventory for unification opportunities."""
    soul = prompts.load_soul()
    inventory = _load_inventory()
    if "no laws" in inventory:
        print("Inventory is empty. Run 'investigate' first.")
        return

    print("\n=== HUMBOLDT: Theorizing across inventory ===\n")
    system, user = prompts.theorize_prompt(soul, inventory)
    output = synth.synthesize_streaming(system, user)

    slug = f"theory-{datetime.date.today().isoformat()}"
    log_path = _session_log_path(slug)
    log_path.write_text(f"# Humboldt Theory Session\nDate: {datetime.date.today().isoformat()}\n\n{output}\n")
    print(f"\nSession log saved: {log_path}")


def cmd_inventory():
    """Display current law inventory."""
    files = sorted(LAWS_DIR.glob("*.yaml"))
    if not files:
        print("Law inventory is empty.")
        return

    import yaml
    print(f"\n=== HUMBOLDT Law Inventory — {len(files)} laws ===\n")
    by_confidence = {}
    for f in files:
        law = yaml.safe_load(f.read_text())
        conf = law.get("confidence", "speculative")
        by_confidence.setdefault(conf, []).append(law)

    for conf in ["established", "candidate", "contested", "speculative"]:
        laws = by_confidence.get(conf, [])
        if laws:
            print(f"[{conf.upper()}]")
            for l in laws:
                print(f"  {l.get('id')} — {l.get('name')}")
                domains = l.get("domains", [])
                if domains:
                    print(f"          domains: {', '.join(str(d) for d in domains[:3])}")
            print()


def cmd_ingest():
    """Ingest Humboldt's own documents into the humboldt Pinecone namespace."""
    from agent.ingest import ingest_all
    ingest_all(verbose=True)


def cmd_triage_feed(output: str | None = None):
    """Triage inbox/feed-*.md items against current laws and hypotheses."""
    from agent.triage import triage_feed
    triage_feed(output_path=output)


def cmd_triage_discord(output: str | None = None):
    """Triage inbox/discord-*.md items (ideas + links) against current laws and hypotheses."""
    from agent.triage import triage_discord
    triage_discord(output_path=output)


def cmd_shallow_read(triage_path: str, dry_run: bool = False):
    """Shallow-read all non-discard items from a triage report."""
    from agent.shallow_read import shallow_read
    shallow_read(triage_path=triage_path, dry_run=dry_run)


def cmd_inbox_status():
    """Show unprocessed inbox composition."""
    from agent.inbox import status
    status()


def cmd_inbox_archive_discards(report_path: str):
    """Archive discard items from a triage report → inbox/processed/; update people model."""
    from agent.inbox import archive_discards
    archive_discards(report_path=report_path)


def cmd_inbox_cleanup():
    """Delete inbox/processed/ items older than 30 days."""
    from agent.inbox import cleanup
    cleanup()


def cmd_people(handle: str | None = None):
    """Show contribution trust model for all collaborators, or detail for one."""
    from daemon.people import contribution_summary, person_contribution_detail
    if handle:
        print(person_contribution_detail(handle))
    else:
        print(contribution_summary())


def cmd_daemon_run():
    """Start the Humboldt daemon (Discord bot + scheduled tasks)."""
    from daemon.runner import run
    run()


def cmd_daemon_restart():
    """Send SIGUSR1 to the running daemon to trigger a graceful hot-reload."""
    import signal as _signal
    daemon_dir = Path(__file__).parent.parent / "daemon"
    pid_file = daemon_dir / "daemon.pid"
    if not pid_file.exists():
        print("No daemon.pid found — daemon does not appear to be running.")
        print("Start it with: python3 -m agent.humboldt daemon run")
        sys.exit(1)
    pid = int(pid_file.read_text().strip())
    try:
        os.kill(pid, _signal.SIGUSR1)
        print(f"SIGUSR1 sent to daemon PID {pid} — reloading with updated code.")
    except ProcessLookupError:
        print(f"PID {pid} not found — daemon may have crashed. Remove daemon.pid and restart.")
        sys.exit(1)


def cmd_daemon_status():
    """Show daemon state and cumulative API costs."""
    import json
    daemon_dir = Path(__file__).parent.parent / "daemon"

    pid_file = daemon_dir / "daemon.pid"
    if pid_file.exists():
        print(f"\nDaemon PID: {pid_file.read_text().strip()} (running)")
    else:
        print("\nDaemon PID: not running (no daemon.pid)")

    state_path = daemon_dir / "state.json"
    if not state_path.exists():
        print("No daemon state found — daemon has not been run yet.")
    else:
        state = json.loads(state_path.read_text())
        print("\n=== Daemon state ===\n")
        print(f"  Last startup         : {state.get('last_startup', 'unknown')}")
        print(f"  Last clean shutdown  : {state.get('last_clean_shutdown', 'never (crash?)')}")
        print(f"  Last notebook commit : {(state.get('last_notebook_commit') or 'none')[:12]}…")
        posted = state.get("notebook_entries_posted", [])
        print(f"  Notebook entries posted : {', '.join(posted) if posted else 'none'}")
        print(f"  Last #new-nature msg    : {state.get('last_new_nature_message_id', 'none')}")
        print(f"  Last feed check         : {state.get('last_feed_check', 'never')}")
        print(f"  Responded mention IDs   : {len(state.get('responded_mention_ids', []))} tracked")

    from daemon import costs
    t = costs.totals()
    print("\n=== API costs (cumulative) ===\n")
    if t["calls"] == 0:
        print("  No calls logged yet.")
    else:
        print(f"  Total calls    : {t['calls']}")
        print(f"  Input tokens   : {t['input_tokens']:,}")
        print(f"  Output tokens  : {t['output_tokens']:,}")
        print(f"  Total cost     : ${t['total_usd']:.4f}")
        print()
        for op, usd in t["by_operation"].items():
            print(f"  {op:<28} ${usd:.4f}")
    print()


async def _discord_sweep_async(since: str | None, limit: int):
    """
    Sweep historical #new-nature messages through the capture system.

    Fetches messages via Discord REST API (no gateway connection needed),
    working backwards from most recent. Stops at --since DATE or --limit.
    """
    import asyncio
    import sys
    import urllib.request
    from datetime import datetime, timezone
    from daemon import capture as cap

    channel_id = os.environ["DISCORD_NEW_NATURE_CHANNEL_ID"]
    token = os.environ["DISCORD_BOT_TOKEN"]

    _UA = (
        f"DiscordBot (https://github.com/Rapptz/discord.py, 2.3.2) "
        f"Python/{sys.version_info.major}.{sys.version_info.minor}"
    )

    def rest_get(path: str):
        req = urllib.request.Request(
            f"https://discord.com/api/v10{path}",
            headers={"Authorization": f"Bot {token}", "User-Agent": _UA},
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())

    # Resolve bot user ID to filter self-messages
    me = rest_get("/users/@me")
    bot_id = me["id"]
    print(f"Bot: {me['username']}#{me.get('discriminator', '0')} (id {bot_id})")

    # Parse --since date (interpret as UTC midnight)
    since_dt: datetime | None = None
    if since:
        since_dt = datetime.fromisoformat(since).replace(tzinfo=timezone.utc)

    total_scanned = 0
    total_captured = 0
    batch_num = 0
    before: str | None = None
    stop = False

    print(f"Sweeping #new-nature{f' since {since}' if since else ' (full history)'}...")
    print(f"Limit: {limit} messages\n")

    while not stop and total_scanned < limit:
        url = f"/channels/{channel_id}/messages?limit=100"
        if before:
            url += f"&before={before}"

        batch_raw = rest_get(url)
        if not batch_raw:
            break

        # Filter and normalise messages; stop at date boundary
        messages = []
        for msg in batch_raw:
            if msg["author"]["id"] == bot_id:
                continue
            ts = datetime.fromisoformat(msg["timestamp"].replace("Z", "+00:00"))
            if since_dt and ts < since_dt:
                stop = True
                break
            messages.append({
                "author": msg["author"]["username"],
                "content": msg["content"][:400],
            })

        total_scanned += len(batch_raw)
        batch_num += 1

        if messages:
            n = await cap.run_capture(messages, "#new-nature")
            total_captured += n
            print(f"  Batch {batch_num:>3} ({len(messages):>3} msgs) → {n} captured  [{total_scanned} scanned, {total_captured} saved]")
        else:
            print(f"  Batch {batch_num:>3} ({len(batch_raw):>3} msgs, all filtered)")

        if len(batch_raw) < 100:
            break

        # Paginate: use the ID of the oldest message in this batch
        before = batch_raw[-1]["id"]
        # Respect Discord rate limits (~50 req/s; 100ms is well within limits)
        await asyncio.sleep(0.2)

    print(f"\nSweep complete: {total_scanned} messages scanned, {total_captured} items saved to inbox/")


def cmd_discord_sweep(since: str | None = None, limit: int = 1000):
    """Run a catch-up capture sweep over historical #new-nature messages."""
    import asyncio
    asyncio.run(_discord_sweep_async(since, limit))


async def _discord_post_async(draft: bool):
    """Generate and optionally post the most recent notebook entry with thread creation."""
    from daemon import presence
    from daemon.notebook_watcher import get_new_notebook_entries
    from agent import notebook_index as nbi

    entries = get_new_notebook_entries(None)
    if not entries:
        print("No notebook entries found.")
        return

    entry = entries[0]
    date = entry["date"]
    entry_url = nbi.entry_url(date)
    print(f"Generating post for notebook entry: {date}")
    print(f"Entry URL: {entry_url}")
    post = await presence.generate_notebook_post(
        date, entry["path"], entry["github_url"], entry_url=entry_url,
    )

    if draft:
        print("\n─── DRAFT ───────────────────────────────")
        print(post)
        print("─────────────────────────────────────────\n")
        return

    import json
    import urllib.request
    channel_id = os.environ["DISCORD_NEW_NATURE_CHANNEL_ID"]
    token = os.environ["DISCORD_BOT_TOKEN"]
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (https://github.com/Protocol-Institute/humboldt, 1.0)",
    }

    # Post the announcement
    data = json.dumps({"content": post}).encode()
    req = urllib.request.Request(
        f"https://discord.com/api/v10/channels/{channel_id}/messages",
        data=data, headers=headers, method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        msg = json.loads(resp.read())
        announcement_id = msg["id"]
        print(f"Posted to #new-nature (message {announcement_id})")

    # Create a discussion thread on the announcement
    thread_id: str | None = None
    try:
        index_entry = nbi.get_entry(date) or {}
        title = index_entry.get("title", date)
        thread_data = json.dumps({
            "name": f"Discussion: {title[:80]}",
            "auto_archive_duration": 10080,  # 7 days
        }).encode()
        req = urllib.request.Request(
            f"https://discord.com/api/v10/channels/{channel_id}/messages/{announcement_id}/threads",
            data=thread_data, headers=headers, method="POST",
        )
        with urllib.request.urlopen(req) as resp:
            thread = json.loads(resp.read())
            thread_id = thread["id"]
            print(f"Created discussion thread: {thread['name']} (id {thread_id})")
    except Exception as e:
        print(f"Warning: thread creation failed: {e}")

    # Save IDs to index.yaml
    nbi.upsert_entry(date, discord_announcement_id=announcement_id, discord_thread_id=thread_id)
    print(f"Saved announcement/thread IDs to notebook/index.yaml")


def cmd_discord_post(draft: bool = False):
    """Manually generate and post a notebook announcement to #new-nature."""
    import asyncio
    asyncio.run(_discord_post_async(draft))


def cmd_publish_site(dry_run: bool = False):
    """Build humboldt-site/ and deploy to Cloudflare Pages."""
    from agent.publish_site import publish_site
    ok = publish_site(dry_run=dry_run, verbose=True)
    if not ok and not dry_run:
        sys.exit(1)


_PUBLISH_DEPRECATED_MSG = (
    "This command targeted the old protocol-institute.org website (now removed).\n"
    "Use `publish-site` instead — it rebuilds and deploys humboldt-site/ to CF Pages."
)


def cmd_publish(dry_run: bool = False):
    print(_PUBLISH_DEPRECATED_MSG)
    sys.exit(1)


def cmd_publish_research(dry_run: bool = False):
    print(_PUBLISH_DEPRECATED_MSG)
    sys.exit(1)


def cmd_publish_reading(dry_run: bool = False):
    print(_PUBLISH_DEPRECATED_MSG)
    sys.exit(1)


def cmd_publish_architecture(dry_run: bool = False):
    print(_PUBLISH_DEPRECATED_MSG)
    sys.exit(1)


def cmd_references_list(unsorted_only: bool = False):
    """Display the reference list grouped by status."""
    from agent.references import cmd_list
    cmd_list(unsorted_only=unsorted_only)


def cmd_references_sort(dry_run: bool = False):
    """Classify unsorted references into read / deep_read / discard."""
    from agent.references import sort_references
    sort_references(dry_run=dry_run, verbose=True)


def cmd_references_promote():
    """Manually promote all inbox link captures to the reference list."""
    from agent.references import promote_inbox_links
    n = promote_inbox_links(verbose=True)
    print(f"\n{n} reference(s) added from inbox.")


USAGE = """
Usage:
  python3 -m agent.humboldt investigate "<topic>"        # open-ended investigation
  python3 -m agent.humboldt hypothesize "<topic>"        # propose candidate laws (no files)
  python3 -m agent.humboldt assess <law-id>              # gather evidence for a law
  python3 -m agent.humboldt theorize                     # find unification opportunities
  python3 -m agent.humboldt inventory                    # show current law inventory
  python3 -m agent.humboldt library                      # list deep-read library
  python3 -m agent.humboldt deepread "<name>"            # deep-read full document
  python3 -m agent.humboldt deepread "<name>" "<p1-p2>"  # deep-read page range
  python3 -m agent.humboldt triage-feed                  # score inbox feed items → discard/shallow report
  python3 -m agent.humboldt triage-feed --output FILE    # write triage report to file
  python3 -m agent.humboldt triage-discord               # score inbox discord items (ideas+links) → report
  python3 -m agent.humboldt triage-discord --output FILE # write discord triage report to file
  python3 -m agent.humboldt shallow-read --from-triage FILE   # shallow-read all non-discard items; deletes source files
  python3 -m agent.humboldt shallow-read --from-triage FILE --dry-run  # preview, no writes
  python3 -m agent.humboldt inbox status                      # show unprocessed inbox composition
  python3 -m agent.humboldt inbox archive-discards --from-triage FILE  # move discards → processed/; update people model
  python3 -m agent.humboldt inbox cleanup                     # delete processed/ items older than 30 days
  python3 -m agent.humboldt people                            # show contribution trust model for all collaborators
  python3 -m agent.humboldt people <handle>                   # detail for one collaborator
  python3 -m agent.humboldt ingest                       # embed notebook/notes/laws/ideas/shallow-reads → Pinecone humboldt ns
  python3 -m agent.humboldt daemon run                   # start daemon (Discord + feeds)
  python3 -m agent.humboldt daemon restart               # hot-reload daemon (SIGUSR1, preserves state)
  python3 -m agent.humboldt daemon status                # show daemon state + PID
  python3 -m agent.humboldt discord post                 # post latest notebook entry to Discord
  python3 -m agent.humboldt discord post --draft         # preview post without sending
  python3 -m agent.humboldt discord sweep                # capture sweep: full #new-nature history
  python3 -m agent.humboldt discord sweep --since DATE   # sweep since YYYY-MM-DD (UTC)
  python3 -m agent.humboldt discord sweep --limit N      # cap at N messages (default 1000)
  python3 -m agent.humboldt publish-site                  # build humboldt-site/ + deploy to CF Pages
  python3 -m agent.humboldt publish-site --dry-run        # build only, no deploy
  python3 -m agent.humboldt references list              # show reference list by status
  python3 -m agent.humboldt references list --unsorted   # show only unsorted
  python3 -m agent.humboldt references sort              # classify unsorted → read/deep_read/discard
  python3 -m agent.humboldt references sort --dry-run    # preview sort decisions, no writes
  python3 -m agent.humboldt references promote           # manually promote inbox links → reference list
"""


def main():
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        sys.exit(0)

    cmd = args[0]
    rest = args[1:]

    if cmd == "investigate":
        if not rest:
            print("Usage: humboldt investigate \"<topic>\"")
            sys.exit(1)
        cmd_investigate(" ".join(rest))
    elif cmd == "hypothesize":
        if not rest:
            print("Usage: humboldt hypothesize \"<topic>\"")
            sys.exit(1)
        cmd_hypothesize(" ".join(rest))
    elif cmd == "assess":
        if not rest:
            print("Usage: humboldt assess <law-id>  (e.g. L-001)")
            sys.exit(1)
        cmd_assess(rest[0])
    elif cmd == "theorize":
        cmd_theorize()
    elif cmd == "inventory":
        cmd_inventory()
    elif cmd == "library":
        cmd_library()
    elif cmd == "deepread":
        if not rest:
            print("Usage: humboldt deepread \"<doc-name>\" [\"<page-range>\"]")
            sys.exit(1)
        doc = rest[0]
        pages = rest[1] if len(rest) > 1 else None
        cmd_deepread(doc, pages)
    elif cmd == "triage-feed":
        output = None
        if "--output" in rest:
            idx = rest.index("--output")
            if idx + 1 < len(rest):
                output = rest[idx + 1]
        cmd_triage_feed(output=output)
    elif cmd == "triage-discord":
        output = None
        if "--output" in rest:
            idx = rest.index("--output")
            if idx + 1 < len(rest):
                output = rest[idx + 1]
        cmd_triage_discord(output=output)
    elif cmd == "shallow-read":
        triage_path = None
        dry_run = "--dry-run" in rest
        if "--from-triage" in rest:
            idx = rest.index("--from-triage")
            if idx + 1 < len(rest):
                triage_path = rest[idx + 1]
        if not triage_path:
            print("Usage: humboldt shallow-read --from-triage <report-path>")
            sys.exit(1)
        cmd_shallow_read(triage_path=triage_path, dry_run=dry_run)
    elif cmd == "inbox":
        subcmd = rest[0] if rest else "status"
        if subcmd == "status":
            cmd_inbox_status()
        elif subcmd == "archive-discards":
            report_path = None
            if "--from-triage" in rest:
                idx = rest.index("--from-triage")
                if idx + 1 < len(rest):
                    report_path = rest[idx + 1]
            if not report_path:
                print("Usage: humboldt inbox archive-discards --from-triage <report-path>")
                sys.exit(1)
            cmd_inbox_archive_discards(report_path=report_path)
        elif subcmd == "cleanup":
            cmd_inbox_cleanup()
        else:
            print(f"Unknown inbox subcommand: {subcmd}")
            sys.exit(1)
    elif cmd == "people":
        handle = rest[0] if rest else None
        cmd_people(handle=handle)
    elif cmd == "ingest":
        cmd_ingest()
    elif cmd == "pre-notebook":
        subcmd = rest[0] if rest else "show"
        if subcmd == "mark-consumed":
            from agent.pre_notebook import mark_consumed
            mark_consumed()
            print("Pre-notebook cursor advanced.")
        else:
            from agent.pre_notebook import show_pending
            show_pending()
    elif cmd == "daemon":
        subcmd = rest[0] if rest else "run"
        if subcmd == "run":
            cmd_daemon_run()
        elif subcmd == "status":
            cmd_daemon_status()
        elif subcmd == "restart":
            cmd_daemon_restart()
        else:
            print(f"Unknown daemon subcommand: {subcmd}")
            sys.exit(1)
    elif cmd == "publish-site":
        dry_run = "--dry-run" in rest
        cmd_publish_site(dry_run=dry_run)
    elif cmd in ("publish", "publish-research", "publish-reading", "publish-architecture"):
        dry_run = "--dry-run" in rest
        if cmd == "publish":
            cmd_publish(dry_run=dry_run)
        elif cmd == "publish-research":
            cmd_publish_research(dry_run=dry_run)
        elif cmd == "publish-reading":
            cmd_publish_reading(dry_run=dry_run)
        elif cmd == "publish-architecture":
            cmd_publish_architecture(dry_run=dry_run)
    elif cmd == "references":
        subcmd = rest[0] if rest else "list"
        if subcmd == "list":
            unsorted_only = "--unsorted" in rest
            cmd_references_list(unsorted_only=unsorted_only)
        elif subcmd == "sort":
            dry_run = "--dry-run" in rest
            cmd_references_sort(dry_run=dry_run)
        elif subcmd == "promote":
            cmd_references_promote()
        else:
            print(f"Unknown references subcommand: {subcmd}")
            sys.exit(1)
    elif cmd == "discord":
        subcmd = rest[0] if rest else ""
        if subcmd == "post":
            draft = "--draft" in rest
            cmd_discord_post(draft=draft)
        elif subcmd == "sweep":
            since = None
            limit = 1000
            i = 1
            while i < len(rest):
                if rest[i] == "--since" and i + 1 < len(rest):
                    since = rest[i + 1]
                    i += 2
                elif rest[i] == "--limit" and i + 1 < len(rest):
                    limit = int(rest[i + 1])
                    i += 2
                else:
                    i += 1
            cmd_discord_sweep(since=since, limit=limit)
        else:
            print(f"Unknown discord subcommand: {subcmd}")
            sys.exit(1)
    else:
        print(f"Unknown command: {cmd}")
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
