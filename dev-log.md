# Humboldt Dev Log — Track 2

Development log for Humboldt's persona, methodology, and infrastructure. Covers Track 2 (persona evolution) and Track 3 (artificial researcher template) work. Research activity is tracked separately in `notebook/`.

Most recent entry first.

---

## 2026-05-27 (session 7 addendum) — Circuit breaker + discord post fixes

**Track 2 (infrastructure):**

**Circuit breaker (`daemon/costs.py` + all call sites):**
Added `today_usd()`, `BudgetExceeded` exception, `check_budget()`, and `configured_limit()` to `costs.py`. Every Claude API call site (5 in `presence.py`, 1 in `conversation_review.py`, 1 in `capture.py`) now calls `costs.check_budget()` before invoking the model. If today's local-date spend ≥ the configured limit ($5), `BudgetExceeded` is raised. The date boundary is local midnight — `datetime.now().strftime("%Y-%m-%d")` — so the reset is automatic with no explicit mechanism needed. UTC timestamps in costs.jsonl are converted to local time for the comparison.

For `@mention` responses (`on_message`), `BudgetExceeded` is caught specifically and sends a hardcoded canned reply ("I've hit my daily API budget and am offline until midnight. Back tomorrow.") — no model call needed, so the reply is free. All other task paths (feeds, new-nature ticking, conversation review, capture) silently skip via existing `try/except` blocks.

Limit configurable in `daemon/config.yaml` under `budget.daily_limit_usd`.

**`discord post` CLI (`agent/humboldt.py`):**
Updated `_discord_post_async` to: pass `entry_url` (anchor-linked URL) to `generate_notebook_post`; create a discussion thread on the announcement message via Discord REST API; save announcement/thread IDs to `notebook/index.yaml`. Fixed missing `User-Agent` header — Discord's Cloudflare layer was returning 403 without it.

---

## 2026-05-27 (session 7) — Notebook publish loop complete

**Track 2 (infrastructure):**

Completed the notebook → Discord → thread → harvest pipeline that was half-built at end of session 6. All four components now wired end-to-end.

**`notebook/index.yaml` + `agent/notebook_index.py`:**
New canonical metadata module. `index.yaml` is the single source of truth for entry titles, taglines, git-sourced timestamps, Discord announcement/thread IDs, and `thread_last_farmed` timestamps. `build_from_git()` bootstrapped the three existing entries from git history. All downstream consumers (publish, discord_client, thread_farmer) read/write through this module.

**`agent/publish.py` rewrite:**
The key design decisions: entries get `id="entry-YYYY-MM-DD"` (not slugified section text — dates are stable; section headers change); `§` permalink on the date line (muted grey, turns teal on hover) rather than a floating section nav (simpler, no JS); TOC is newest-first (reading order matches reverse-chronological discovery). The `_add_missing_ids()` migration runs idempotently on every publish, so the existing three entries picked up IDs and permalinks on first run. `publish()` returns `list[dict]` (not `int`) — richer return allows callers to drive downstream actions without re-reading state.

**`daemon/thread_farmer.py`:**
Harvests Discord thread comments → `inbox/` for reorientation context at next session start. Key design: uses Discord snowflake arithmetic to paginate from `thread_last_farmed` rather than fetching all history; filters bot messages; writes structured markdown with source metadata; updates `thread_last_farmed` even if zero messages (marks the baseline). Wired into `task_conversation_review` (daily). 

**`daemon/discord_client.py` `task_notebook`:**
Now uses `nbi.entry_url()` for direct anchor links in announcements; creates a 7-day auto-archive discussion thread on each announcement message; saves `discord_announcement_id` + `discord_thread_id` to index.yaml for the thread farmer to use later.

**Website:**
`humboldt-notebook.html` now has TOC (three entries, newest-first), entry IDs, and `§` permalinks. Pushed to GitHub Pages. Netlify references removed throughout (site migrated to GitHub Pages).

**Design decisions not taken:**
- Slugified section anchors within entries (e.g., `#entry-2026-05-20-first-investigation`): section headers change too easily; date-level linking is stable and sufficient for Discord sharing
- Floating section nav: requires JS, adds complexity; `§` permalink per entry is lighter and handles the primary use case (linking to a specific session from Discord)

**Open track 3:**
Thread farmer pattern (harvest external conversation → structured inbox → session reorientation) is a generalizable design worth adding to `_template/`. Not done this session.

---

## 2026-05-26 (session 6) — M-003 researcher-development section

**Track 2 (persona/methodology):**

Session began with user question: "Deep reads should also pick up on knowledge about going better researcher. Is there any of that in the notes?" The answer: yes, but it wasn't structured anywhere.

**Analysis of existing notes:**
- Hamming (gestalt re-read, complete): the *entire talk* is researcher-development material. Problem selection bias; drive as directed walk; 10-20 problem portfolio; Friday afternoons as Orient practice; ambiguity tolerance as the un-teachable prerequisite; problem inversion as local-optima escape; style as the portable core. All of this was in the gestalt re-read but had no named section.
- Simon (law-hunting only): researcher-development content exists structurally — satisficing as attention allocation model, bounded rationality as a description of the researcher's own situation, the ant's path as a caution against over-attributing to the researcher's mind — but was missed in the law-hunting pass. Will surface in gestalt re-read.
- Cosmos (law-hunting, partial): Humboldt's epistemological method is inherently researcher-development — graduated confidence, critique of observation without synthesis, the warning that accumulating disconnected facts without synthesis reinforces the conviction that there's no law. Also missed.

**What changed:**
- **M-003 output format:** section 8 "What it says about becoming a better researcher" added between "nature of things" and "research connections"; total sections now 12. Section 8 explicitly connects to M-016 dimensions. For texts primarily about research practice, this is now the most important section.
- **M-003 Phase 2:** "researcher-development lessons" added as an annotation category in close reading, alongside general lessons and research connections.
- **prompts.py DEEP_READ_SYSTEM:** section 6 added (same content as M-003 section 8); sections renumbered 6-9 → 7-10. The section is explicit about M-016 connection and notes that technical texts may have thin content here.
- **Hamming notes:** section 6 backfilled from existing gestalt re-read material. Covers all six M-016 maturity dimensions via Hamming's specific vocabulary. Key diagnostic: Humboldt's overconfident position-defense is the "too much belief" end of Hamming's ambiguity tolerance spectrum — not a behavioral tic but a structural failure of the middle state that productive revision requires.
- **Daemon restarted:** PID 18737. Picks up all changes from sessions 5-6: people memory, publish pipeline, conversation review, self-knowledge URLs, open-mindedness, M-003 gestalt-first prompts.

**Track 3 (template):** The addition of section 8 to M-003 is a potential template change — any future artificial researcher should have this section in their deep read format from the start. No template update yet; defer until pattern is exercised and stabilized across multiple reads.

---

## 2026-05-26 (session 5) — Discord quality + notebook publish pipeline

### Infrastructure changes

**New: `daemon/capture.py`** — Discord idea/link capture system:
- `extract_captures()` — Haiku call to extract ideas and external links from conversation messages relevant to active hypotheses/laws
- `save_capture()` — deduplicates (in-session URL set + file scan) and writes `inbox/discord-{type}-{date}-{time}-{slug}.md`
- `run_capture()` — chunks messages in groups of 15 before calling extract_captures; returns count saved
- max_tokens=1500 (raised from 800 to fix JSON truncation on large batches)

**New: `agent/publish.py`** — lab notebook → website publishing pipeline:
- `render_entry()` — converts `notebook/YYYY-MM-DD.md` to HTML using python-markdown; extracts tagline, title (first `##` heading or `<!-- title: ... -->` override); wraps in `<!-- ENTRY: date -->` markers
- `publish()` — diffs existing HTML by entry markers, inserts new entries chronologically, git add/commit/push to `../website` repo
- `_convert_body()` — demotes h2→h3, adds indentation, strips `<hr>` rules
- Used `markdown` library (version 3.10.2); add to `pip install` list

**Updated: `agent/humboldt.py`**:
- Added `cmd_publish(dry_run)` and `publish [--dry-run]` CLI command
- Added `discord sweep [--since DATE] [--limit N]` CLI command (catch-up capture sweep)
- Updated USAGE string

**Updated: `daemon/discord_client.py`**:
- `task_notebook` now runs `publish()` in executor after re-ingest — new notebook entries automatically appear on website
- `_new_nature_loop()` replaces `@tasks.loop` for adaptive interval checking (exponential backoff from last activity)
- `_next_check_interval()` — <4min→90s, <12min→3min, <30min→8min, <90min→20min, else 30min
- `_bot_post_context()` — single history scan returning (recent_bot_posts, last_post_age_seconds)
- `_parse_thread_response()` / `_resolve_mentions()` — THREAD: prefix protocol for thread creation; @username→<@user_id> on long gap or new thread
- Capture runs in parallel with presence check via `asyncio.gather()`

**Updated: `daemon/presence.py`**:
- Style tightened: 2-3 sentences, ≤350 chars; "do not end with a question unless you need the answer for research"
- `generate_new_nature_response()` — added `recent_bot_posts` ("do not repeat these"), participants list, THREAD: prefix instruction; max_tokens=150
- `generate_mention_response()` — added `@username` direct address, THREAD: prefix; max_tokens=200

**Updated: `daemon/state.py`** — added `last_new_nature_activity` field (ISO timestamp of last human message seen)

**Updated: `daemon/feed_monitor.py`** — fixed timezone bug: `datetime.fromtimestamp(mktime(...))` → `datetime.fromtimestamp(mktime(...), tz=timezone.utc)`

**Updated: `CLAUDE.md`** — added `markdown` to pip install; documented `publish` and `discord sweep` CLI commands

### Website

- 2026-05-21 and 2026-05-26 notebook entries manually published to `Protocol-Institute/website` (commit `09d357e`)
- Netlify auto-deployed; entries now live at humboldt-notebook.html
- Future entries will be published automatically by the daemon's `task_notebook`

### Errors resolved this session

- `ANTHROPIC_API_KEY` KeyError in smoke test → env not loaded; fixed with `set -a && source .env && set +a`
- JSON truncation in capture (`max_tokens=800` too small for 26 msgs) → raised to 1500, added chunk_size=15
- Cloudflare 403 on Discord REST calls → added `User-Agent: DiscordBot (...)` header
- Feed timezone crash (`naive vs aware` comparison) → added `tz=timezone.utc` in feed_monitor.py

---

## 2026-05-26 (session 4) — Humboldt namespace: augmented self-retrieval

### Infrastructure changes

**New: `agent/ingest.py`** — ingestion module for Humboldt's own documents:
- `_notebook_chunks()` — splits `notebook/*.md` by `##` headers; augments embed text with `"Lab Notebook YYYY-MM-DD — Section Title"` prefix
- `_notes_chunks()` — splits `bibliography/notes/*.md` by `##` headers; augments with book title
- `_law_chunks()` — embeds each `research/laws/*.yaml` in full (statement + mechanism + domains); no chunking, laws are small
- `_hypothesis_chunks()` — embeds each `research/hypotheses/*.yaml` in full (question + motivation)
- `ingest_all()` — batches and upserts to `humboldt` Pinecone namespace; deterministic IDs so re-runs update in place
- 61 vectors indexed on first run: 30 notebook, 24 notes, 5 law, 2 hypothesis

**Updated: `agent/retrieval.py`** — added `NS_HUMBOLDT = ["humboldt"]` and `NS_BROAD_PLUS` (PI corpus + humboldt namespace)

**Updated: `agent/humboldt.py`** — added `cmd_ingest()` and `ingest` CLI command

**Updated: `daemon/discord_client.py`**:
- `on_message` and `_scan_missed_mentions` now use `NS_BROAD_PLUS` — @mention responses draw from both PI corpus and Humboldt's own notebook/notes/laws
- `task_notebook` calls `ingest_all()` in executor after posting new entries, keeping namespace current

**Updated: `daemon/presence.py`**:
- `_rich_context()` — new full-depth context for @mention responses: IDENTITY + LINEAGE (truncated) + full law statements with mechanism + active hypothesis questions + longer notebook excerpt
- `_slim_context()` — unchanged, still used for notebook posts and new_nature triage
- `generate_mention_response()` now uses `_rich_context()` and separates retrieved chunks into "from own work" vs "from PI corpus" in the prompt, with `max_tokens` raised to 500

### Retrieval quality check

Test queries confirm correct retrieval:
- "coordination cost conservation" → H-001 hypothesis at 0.561, L-001 at 0.434, relevant notebook sections
- "near decomposability Simon stable intermediates" → notebook "What Ch 8 Revealed" at 0.409, Simon notes at 0.404

### Track 3: generalization candidate

The ingest pattern (augmented chunk text with document title + section prefix) is the key design decision that makes retrieval results self-identifying in Claude prompts. This is worth capturing in `_template/` as the recommended approach for any AR project that ingests its own work. Not updating the template this session — one more session to see if the retrieval quality justifies the pattern.

### Open issues updated

| Priority | Issue |
|----------|-------|
| High | H-001 (Coordination Cost Conservation): now four sessions overdue — must open next T1 session with this |
| Medium | Daemon needs manual restart after code changes |
| Low | `_template/` update: ingest pattern worth capturing |
| Low | Always-on machine deployment |

---

## 2026-05-26 (session 3) — Daemon layer built and deployed

### Infrastructure changes

**New: `daemon/` package** — full async daemon layer:
- `discord_client.py` — `HumboldtBot(discord.Client)` with three `ext.tasks` loops: notebook watcher (30 min), #new-nature presence check (30 min, active hours gated), feed monitor (12h)
- `presence.py` — Claude-powered content generation with slim context; `AsyncAnthropic`; `_discord_safe()` truncation at 1900 chars
- `notebook_watcher.py` — `git log` based detection of new notebook entries since last-seen commit
- `feed_monitor.py` — `feedparser` RSS polling + `inbox/` saving
- `state.py` — persistent `state.json` (gitignored, machine-local)
- `costs.py` — per-call cost logging to `costs.jsonl`; `totals()` by operation
- `config.yaml` — intervals, active hours, feed sources (operator-editable)

**CLI additions:** `daemon run`, `daemon status` (shows state + cost totals), `discord post [--draft]`

**Fixes during session:**
- Discord 2000-char limit: `_discord_safe()` + reduced `max_tokens` + explicit prompt instructions
- Cost logging: every Claude call logs to `costs.jsonl`; `daemon status` shows cumulative spend
- Missed @mention catchup: `_scan_missed_mentions()` runs on `on_ready`, responds to any @mentions in #new-nature since last check
- Active hours gate: `_within_active_hours()` checks Pacific time before each new-nature check; configurable in `config.yaml`
- #new-nature history limit: 25 → 100 messages

**Dependencies added:** `discord.py>=2.3`, `feedparser`

**Gitignored:** `daemon/state.json`, `daemon/costs.jsonl`, `daemon/daemon.log`

### Deployment

Bot running live on PI Discord as `humboldt#5503`. First @mention responses verified working. Daemon started with `nohup`, detached from terminal, PID tracked. Bot token and channel/guild IDs registered in `../.env.keys` and `../admin/keys.md`.

### First session costs

Two Claude calls at session start: $0.0086 (new-nature check) + $0.0079 (mention response) = $0.0165 total.

### Track 3: no template changes

The daemon pattern is PI-specific (Discord server, Pinecone index, active hours in Pacific). The general pattern of a daemon layer for an artificial researcher is worth capturing in `_template/` eventually, but too early — needs more sessions to know what generalizes.

### Open issues updated

| Priority | Issue |
|----------|-------|
| High | H-001 (Coordination Cost Conservation): four sessions overdue |
| Medium | Daemon needs manual restart after code changes — `--reload` dev mode deferred |
| Medium | Thread support: `task_new_nature` doesn't scan threads; @mention required |
| Low | Always-on machine deployment: systemd unit file, `git pull` on schedule |

---

## 2026-05-26 (session 2) — Hamming deep read completed

### Infrastructure: no changes

No persona, CLI, or infrastructure changes. Track 2 activity is this entry and the commit.

### What this session produced

Hamming's "You and Your Research" read from actual PDF (13 pages, single session). Notes at `bibliography/notes/hamming-you-and-your-research.md`. Three candidate laws generated (CL-Hamming-1 through CL-Hamming-3). Lab notebook appended.

The Hamming read introduced a distinction the Simon read didn't make explicit: there are two kinds of deep-read sources — framework sources (Simon: analytical tools for understanding what protocols are) and craft sources (Hamming: empirical wisdom about how to do research). M-004 (reading prioritization) should weight these differently. Framework sources contribute to the theory; craft sources contribute to the methodology. Both matter, but for different reasons.

CL-Hamming-2 (problem inversion) and CL-Simon-2 (local-maximum trap) are converging on the same phenomenon at different levels. This will need to be resolved before either is promoted to a hypothesis — either they merge into a single hypothesis with two contributing laws, or they remain complementary laws with explicit cross-references.

### Track 3: one generalization candidate

The framework/craft distinction in reading sources is a generalizable pattern. `_template/` should flag this in its M-004 analog: deep reads serve two functions (analytical framework acquisition, research methodology acquisition), and prioritization should consider both. Not updating the template this session — this is worth sitting with for another session before formalizing it.

---

## 2026-05-26 — Simon deep read completed; notes architecture validated

### Infrastructure: no changes

No persona, CLI, or infrastructure changes this session. The only Track 2 activity is this entry and the commit.

### What this session validated

The deep-read note-taking architecture (introduced 2026-05-20) worked as designed. The file at `bibliography/notes/simon-sciences-of-artificial.md` accumulated cleanly across multiple sessions: vocabulary, analytical moves, protocol-theoretic moments, candidate laws, and open questions are all maintained in a single structured document. The note file is now 400+ lines and covers all priority chapters. This is the intended outcome.

The M-003 deep-read rule — **always read from the actual PDF, never from training memory** — was successfully enforced. The 2026-05-21 session discarded a training-knowledge read; today's session produced the real one. The rule has now been tested under real conditions and confirmed necessary. Background agents are particularly dangerous for well-known texts: they produce plausible-sounding synthesis from training memory without any visible indication that the PDF was not read.

### Open design question: LINEAGE.md update criteria

The Simon read is complete. LINEAGE.md should be updated to acknowledge Simon as an earned lineage entry — not just a reference, but a genuinely influential source that has shaped Humboldt's analytical vocabulary. The criteria from LINEAGE.md: a deep-read source qualifies for LINEAGE entry when (a) it has been fully read, (b) its framework has been internalized and applied (analytical moves A–J, candidate laws), and (c) it has changed how Humboldt sees the research domain.

Simon qualifies on all three. I will update LINEAGE.md in this session.

### Track 3: no template updates

Nothing from this session generalizes to `_template/` in a way not already captured. The deep-read workflow is already in the template. No Track 3 changes needed.

---

## 2026-05-21 — Architecture redesign: from RAG persona to researcher OS

### The core problem resolved

The inherited SOUL.md architecture was built for c3po — a corpus assistant whose identity is defined by the corpus it inhabits and reports from. Humboldt is fundamentally different: defined by interests and skills, not by what it knows; self-directed rather than query-driven; building its own original research inventory rather than synthesizing the corpus for users. The SOUL.md pattern could not accommodate a behavioral loop where Humboldt reviews its own state and decides what to do next.

The fix required a full architecture replacement, not a patch.

### New persona architecture

**Retired:** `SOUL.md` (archived, preserved for reference)

**Replaced by:**

| Document | Purpose |
|----------|---------|
| `IDENTITY.md` | Short stable kernel: lineage telos, mission, intellectual temperament, voice |
| `LINEAGE.md` | Append-only earned lineage: grows from deep reads and established laws only |
| `MEMORY.md` | Narrative memory: how Humboldt tells itself the story of its development |
| `METHOD.md` | Epistemic standards: provenance marking, confidence levels, falsification |
| `BOOTSTRAP.md` | Wakeup sequence and Decide-phase configuration |
| `methods/M-000-ooda.md` | The OS kernel: OODA decision gate |

The key architectural insight: LINEAGE.md and MEMORY.md start nearly empty and grow slowly through research activity. Declared identity is replaced by earned identity. LINEAGE gets one entry per completed deep read and one per law promoted to `established`. MEMORY gets an entry when something significantly shifts. Both are permanent and append-only.

### Dynamic context assembly

`agent/prompts.py` now assembles the system prompt from multiple sources rather than loading a single static SOUL.md. The assembled context includes: IDENTITY + LINEAGE + MEMORY + METHOD + BOOTSTRAP + research state (loaded from research/ at runtime) + methods index (one line per M-NNN) + inbox contents + recent notebook thread. `load_soul()` is a backward-compatible wrapper around `assemble_context()`.

### Behavior stub inventory

Twelve new method stubs written (M-000 through M-015, excluding gaps):

- **M-000** — OODA meta-loop (the kernel)
- **M-004** — Reading prioritization
- **M-005** — Explore-exploit
- **M-006** — Research conversations
- **M-007** — Field trip
- **M-008** — Bullshit detector
- **M-009** — Visual thinking
- **M-010** — Fermi estimation
- **M-011** — Dyson design
- **M-012** — Thought experiments
- **M-013** — Design fictions
- **M-014** — Cross-training
- **M-015** — Stress-relax

The stubs range from immediately usable (M-010 Fermi, M-012 Thought Experiments) to requiring significant adaptation for a digital researcher (M-015 Stress-Relax, M-014 Cross-Training). The OODA stub reflects the operator's specific understanding: Orient is expensive and should only be triggered when the environment has genuinely shifted; routine sessions run as O_DA.

### Library restructure and deep-read wiring

`bibliography/` restructured:
- `bibliography/deep-reads/` — PDF source documents only
- `bibliography/notes/` — reading notes (was `bibliography/deep-reads/*.md`)

`simon_sciences.pdf` moved to `bibliography/deep-reads/simon-sciences-of-artificial.pdf`.
`simon-sciences-of-artificial.md` moved to `bibliography/notes/`.

New CLI commands: `humboldt library` (list documents) and `humboldt deepread "<name>" ["<pages>"]` (read actual PDF via pypdf, write notes to bibliography/notes/).

Critical rule enforced in M-003 and CLAUDE.md: deep reads must always use the actual PDF. Never from training knowledge. A background agent was dispatched to continue the Simon read this session and produced plausible-sounding output from training memory — it was discarded. The rule now has a concrete failure case to point to.

### Inbox

`inbox/` created. The operator drops files here; Humboldt reads them as part of the BOOTSTRAP wakeup sequence. Text and markdown files are inlined into the assembled context; PDFs and large files are listed with a pointer. `inbox/processed/` is where Humboldt moves items after acting on them.

Telegram bot integration (pointing to the existing vgr-library-code infrastructure) is the planned next step for async inbox delivery.

### Hamming PDF acquired

`hamming_you_and_your_research.pdf` downloaded to library. Reading prioritization (M-004) should evaluate it against active hypotheses before Humboldt decides when to engage it. Short document — likely a shallow-mode read alongside a primary investigation session.

### Track 3: template status

The new architecture (IDENTITY/METHOD/BOOTSTRAP/LINEAGE/MEMORY) is itself the core generalization that `_template/` should capture. The existing `SOUL-template.md` and `METHOD-template.md` are now outdated. Updating `_template/` to reflect the new architecture is the next Track 3 priority.

### Open issues

| Priority | Issue |
|----------|-------|
| High | Simon deep read: continue from p.61 using actual PDF |
| High | H-001 (Coordination Cost Conservation): over-aged, needs first retrieval run |
| High | `_template/` update: SOUL-template.md superseded; new architecture templates needed |
| Medium | Discord presence mechanism: still undesigned at implementation level |
| Medium | Telegram inbox integration: wire vgr-library-code bot to write to `inbox/` |

---

## 2026-05-20 (session 2) — Public launch + ritual definition

**Session goals:** complete project housekeeping; publish the project; define operational structure.

### Publication
- Repo made public (`Protocol-Institute/humboldt`)
- Org README (`.github/profile/README.md`) updated — Humboldt listed with description and notebook link
- PI website: `humboldt.html` (project page), `humboldt-notebook.html` (lab notebook, first entry), `projects.html` (Initiatives listing entry with both links)
- Terminology sweep across all files: "artificial researcher" replaces "research agent" / "autonomous agent" everywhere. Key distinction: Humboldt is driven by its own research interests, not by user requests.

### Three-track structure
- Track 1 (Humboldt's research), Track 2 (operator/persona), Track 3 (template) formally defined
- `notebook/` created with first entry (2026-05-20.md) — first person, Track 1 wrapup artifact
- `dev-log.md` created (this file) — Track 2 wrapup artifact
- `_template/` created — Track 3 primary artifact, v0.1

### Session rituals
- Full ritual spec written into CLAUDE.md — startup and wrapup for all three tracks
- Track 2 is enforcer: must produce wrapup checklist report before session closes
- `[REQUIRED]` designation for non-skippable items: lab notebook entry (T1) and dev-log entry (T2)

### To-do structure
- `research/agenda.md` — Humboldt's own queue, first person, lives in `research/` as a research artifact, updated at T1 wrapup [REQUIRED]
- `TODO.md` — operator queue, T2 and T3 only; Humboldt's layer cleanly separated

### Open issues updated
- Discord presence mechanism elevated to highest T2 priority
- SOUL.md corpus-boundary fix and METHOD.md creation remain high priority

---

## Open Issues (Track 2)

| Priority | Issue | Notes |
|----------|-------|-------|
| High | Discord presence mechanism for #new-nature channel | Auth, participation policy, input→inventory flow — see TODO.md |
| High | Fix SOUL.md corpus-boundary problem | Humboldt must reason from general knowledge freely; "NOT IN CORPUS" is never a research result |
| High | Create METHOD.md | SOUL = who; METHOD = how; methods/ = specific procedures |
| Medium | Update SOUL.md "Current Research State" section | Keep live at session start/end |
| Low | Periodic literature survey mechanism | Scheduled investigative move from current inventory state |

## Open Issues (Track 3)

| Priority | Issue | Notes |
|----------|-------|-------|
| Medium | Copy M-001, M-002, M-003 to `_template/methods/` in generic form | Strip PI specifics; add parameterization notes |
| Medium | Write `_template/CLAUDE-template.md` | Generic Claude Code setup for AR projects |
| Low | Extract as separate repo when stable | After 5+ sessions and external review |

---

## 2026-05-20 — Project initialized + methodology scaffolding

**Session goals:** seed the project; design the research persona; define core techniques; begin first deep read.

### Infrastructure
- Created GitHub repo `Protocol-Institute/humboldt` (private, will go public)
- Scaffolded full directory structure, core documentation files, agent code skeleton
- Registered in `../admin/keys.md` (reuses c3po keys — no new provisioning)
- Full pipeline validated: Voyage embed → Pinecone retrieval → Claude synthesis

### Persona design
- Defined SOUL.md — first version based on c3po's style template, adapted for researcher role
- Identified key design tensions (see `persona_design_notes.md`):
  - **Corpus boundary problem:** agent writes "NOT IN CORPUS" instead of reasoning from general knowledge. SOUL.md inherited this from c3po. Must be fixed — Humboldt's epistemic boundary should be evidence quality, not corpus membership.
  - **Identity vs. method separation:** SOUL.md conflates who Humboldt is with how it does research. These should be separated: SOUL = identity/voice/goals; METHOD = investigative approach; `methods/` = specific procedures.
  - **Input mechanism design:** defined four input types for how Humboldt finds new material (lit surveys, researcher discourse, own past records, proactive tips from collaborators)

### Technique inventory (methods/)
- **M-001 (Random Links):** generative; force structural connection between two disparate inputs → candidate law. Worked example: coal mines + blockchain → H-002.
- **M-002 (Canonical Domains):** dual-use; maintain five home domains as analogy reservoirs and stress-test beds. Canonical domain set in `canonical-domains.yaml`.
- **M-003 (Deep Read):** analytical; fully internalize a foundational text over multiple sessions. First text: Simon's *Sciences of the Artificial*.

### Three-track structure defined
- Track 1 (Research): notebook + research inventory
- Track 2 (Persona): dev-log + SOUL + CLAUDE + methodology artifacts
- Track 3 (Template): `_template/` folder for artificial researcher pattern

---

## Open Issues (Track 2)

| Priority | Issue | Notes |
|----------|-------|-------|
| High | Fix SOUL.md corpus-boundary problem | Humboldt must use general knowledge freely, marking provenance; never write "NOT IN CORPUS" |
| High | Create METHOD.md | Separate investigative methodology from persona identity |
| Medium | Update SOUL.md to reference methods/ inventory | SOUL = who; METHOD = how; methods/ = specific procedures |
| Medium | Design Discord integration | "new-nature" channel as Humboldt's lab; participation policy; bot component |
| Low | Implement periodic survey mechanism | Theory-driven retrieval from current inventory state |

## Open Issues (Track 3)

| Priority | Issue | Notes |
|----------|-------|-------|
| Medium | Review `_template/` and extract generalized patterns | Initial scaffold done; needs review after a few more Track 1 sessions to see what generalizes |
| Low | Consider extracting template as a separate repo | Premature until the pattern is stable after 3+ research sessions |
