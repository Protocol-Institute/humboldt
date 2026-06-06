# Architecture — Humboldt

## Overview

Humboldt is an artificial researcher — an autonomous agent that investigates laws of protocolized and artificial systems. It runs in two modes:

- **CLI mode**: operator-driven research sessions (investigate, deep-read, assess, synthesize)
- **Daemon mode**: always-on Discord presence + autonomous background tasks

Research output is structured and versioned (git): YAML law files, project arc documents, lab notebook entries, reading notes. The daemon extends the research into the PI community in real time — posting new findings, responding to conversations, capturing ideas and references from Discord.

---

## Persona Architecture

Humboldt's persona is assembled dynamically from six documents, not a monolithic prompt:

| Document | Role | Loaded by |
|----------|------|-----------|
| `IDENTITY.md` | Who Humboldt is — lineage, mission, temperament, voice | All Claude calls |
| `LINEAGE.md` | Intellectual lineage — grows as deep reads complete and laws establish | Rich context calls |
| `MEMORY.md` | Narrative memory of the research journey | Rich context calls |
| `METHOD.md` | Epistemic standards — evidence provenance, confidence levels, falsification | CLI research calls |
| `BOOTSTRAP.md` | Session startup sequence + Decide-phase configuration | CLI sessions |
| `methods/M-000-ooda.md` | OS kernel — the OODA decision gate and research loop | CLI sessions |

`presence.py` assembles two tiers of context for Discord calls:

- `_slim_context()` — IDENTITY excerpt + law names + latest notebook paragraph. Used for proactive channel posts and notebook announcements.
- `_rich_context()` — Full IDENTITY + LINEAGE excerpt + law statements + active hypotheses + recent notebook. Used for @mention responses.

---

## System Components

### `agent/retrieval.py` — Corpus Interface

**Primary mode: Direct Pinecone** (default)
- Embeds queries with Voyage AI `voyage-3`
- Queries the shared c3po Pinecone index
- Namespaces: `pdfs`, `substack`, `videos`, `bibliography`, `discord`, `discord_links`, `sig`, `transcripts`, `humboldt`
- Retrieval strategy varies by task (see table below)

**Secondary mode: C3PO Worker API** (fallback)
- HTTP calls to the deployed c3po worker
- Used for cross-checking or when direct Pinecone access is unavailable

The `humboldt` namespace holds Humboldt's own output — notebook entries, reading notes, law and hypothesis YAMLs — indexed by `agent/ingest.py`. Self-retrieval enables corpus-grounded responses about Humboldt's own prior work.

### `agent/synthesizer.py` — Claude Interface

Wraps the Anthropic API for research synthesis tasks:

- **Hypothesis generation**: given a topic, propose candidate laws and sub-questions
- **Evidence analysis**: extract relevant evidence from retrieved chunks and rate quality
- **Law formulation**: draft structured law statements with scope conditions and falsification criteria
- **Theory sketching**: scan existing laws for unification opportunities

Uses `claude-sonnet-4-6`. Prompt caching on the system block (persona documents are large and reused across calls in a session).

### `agent/ingest.py` — Self-Indexing Pipeline

Chunks and embeds Humboldt's own research output into the `humboldt` Pinecone namespace:

- `notebook/*.md` — lab notebook entries, chunked by `##` section
- `bibliography/notes/*.md` — deep-read notes, chunked by section
- `bibliography/shallow-reads/*.md` — shallow-read notes, chunked by section
- `research/c/*.yaml` — Curiosity items (exploration phase)
- `research/h/*.yaml` — Hypothesis items (sensemaking phase)
- `research/cl/*.yaml` — Candidate Law items (valley phase)
- `research/f/*.yaml` — Falsification Monitor items (retrospective phase)
- `research/ds/*.md` — Deep Story arc files, chunked by section
- `inbox/discord-idea-*.md` — community-captured ideas

Each vector carries augmented metadata (document title, date, section, type) so retrieved results are self-identifying in prompts. Run after any session that produces new notebook entries or modifies research artifacts. The daemon runs `ingest_all()` automatically after new notebook entries are detected.

### `agent/publish.py` — Website Publishing Pipeline

Renders lab notebook entries to the PI website (`humboldt-notebook.html`):

- Converts notebook markdown to HTML via `python-markdown`
- Inserts new entries into the website file by anchor marker
- Commits and pushes to the website repo

Run manually with `humboldt publish` or `humboldt publish --dry-run`. The daemon triggers this automatically after `ingest_all()` when new notebook entries are detected.

### `agent/references.py` — Reference Management

Manages `bibliography/references.yaml`, a curated list of papers and links:

- `humboldt references list` — show reference list by status
- `humboldt references sort` — classify unsorted items (read / deep_read / discard) via Claude
- `humboldt references promote` — manually promote inbox link captures to the reference list

### `agent/humboldt.py` — CLI Orchestrator

Entry point for all CLI operations. Key commands:

```
python3 -m agent.humboldt investigate "<topic>"        # corpus retrieval + synthesis
python3 -m agent.humboldt hypothesize "<topic>"        # candidate law generation only
python3 -m agent.humboldt assess <law-id>              # evidence gathering for a law
python3 -m agent.humboldt deepread "<doc-name>"        # M-003 deep read from PDF
python3 -m agent.humboldt inventory                    # display law inventory
python3 -m agent.humboldt ingest                       # embed own docs → humboldt namespace
python3 -m agent.humboldt publish [--dry-run]          # render notebook → website
python3 -m agent.humboldt daemon run                   # start daemon
python3 -m agent.humboldt daemon restart               # hot-reload daemon (SIGUSR1)
python3 -m agent.humboldt daemon status                # PID + state summary
python3 -m agent.humboldt discord post [--draft]       # manual notebook post to Discord
python3 -m agent.humboldt discord sweep [--since DATE] # capture sweep over channel history
python3 -m agent.humboldt references list/sort/promote # reference management
```

---

## Daemon Layer

The daemon (`daemon/`) is a long-running Discord bot that runs Humboldt's online presence and background tasks. It is always-on and event-driven, distinct from the operator-driven CLI sessions.

### `daemon/runner.py` — Process Manager

Starts the `HumboldtBot` Discord client. After the bot exits, checks `bot.reload_requested` — if set, calls `os.execv()` to replace the process with updated code, preserving all state.

### `daemon/discord_client.py` — Discord Bot

`HumboldtBot(discord.Client)` with four scheduled tasks and two event handlers:

**Scheduled tasks:**

| Task | Interval | Purpose |
|------|----------|---------|
| `task_notebook` | 30 min | Watch for new notebook commits; post to #new-nature; trigger ingest + publish |
| `task_feeds` | 12 h | Poll RSS/Atom feeds; run relevance check (Haiku); save to `inbox/`; DM operator |
| `task_conversation_review` | 24 h | Synthesize recent Discord into notebook; promote inbox links to references |
| `_new_nature_loop` | Adaptive | Proactive #new-nature presence (see below) |

**Event handlers:**

- `on_message`: handles @mentions in channels (full rich-context response) and DM commands from the operator (`!reload`, `!status`)
- `on_ready`: records startup time, writes `daemon.pid`, triggers `_scan_missed_mentions`

**`_new_nature_loop` — adaptive presence:**

Replaces a fixed-interval task. Checks #new-nature on an exponential backoff schedule based on time since last human message activity: 90s → 3min → 8min → 20min → 30min. Skips @mention messages (those are `on_message`'s responsibility). Thread creation uses the most recent non-mention message as the anchor; falls back to channel post if anchor is older than 15 minutes.

**`_scan_missed_mentions`:**

On startup, scans for @mentions that arrived while offline and responds to any not already in `responded_mention_ids`. Omits "(catching up from while I was offline)" prefix on brief restarts (< 5 min offline).

**Graceful shutdown and hot-reload:**

- `close()` override saves `last_clean_shutdown` to state and deletes `daemon.pid`
- SIGUSR1 handler triggers `_graceful_reload()`, which sets `reload_requested = True` and calls `close()`; `runner.py` then `os.execv()`s the process
- `!reload` DM from operator triggers the same path

### `daemon/presence.py` — Content Generation

All Claude calls for Discord output. Two context tiers (`_slim_context` / `_rich_context`) and six generation functions:

- `generate_notebook_post` — post announcing a new notebook entry (Haiku)
- `generate_new_nature_response` — proactive channel response to new messages (Haiku)
- `generate_mention_response` — @mention reply with full research context (Sonnet)
- `generate_person_notebook_entry` — notebook entry about a recurring interlocutor (Sonnet)
- `check_feed_relevance` — assess whether a feed item bears on active research (Haiku)
- `generate_conversation_review` — daily synthesis of Discord into notebook (Sonnet)

### `daemon/capture.py` — Idea and Reference Capture

After every batch of Discord messages, runs a lightweight Haiku extraction to identify:
1. Ideas or arguments that bear on active hypotheses or challenge current laws
2. External papers, articles, or URLs cited by participants

Captured items are saved to `inbox/` as dated markdown files. Deduplicates URLs within a daemon session.

### `daemon/people.py` — Interlocutor Memory

Tracks recurring Discord participants in `daemon/people.json` (gitignored). After `NOTEBOOK_THRESHOLD` (3) interactions with a person, flags that a notebook entry should be written about them. Used to personalize @mention responses with interaction history.

### `daemon/conversation_review.py` — Daily Synthesis

Runs every 24 hours:
1. Reads recent #new-nature messages and writes a reflective notebook section (Sonnet) — what emerged, what challenged current thinking
2. Promotes unseen inbox link captures to `bibliography/references.yaml` as `unsorted` entries

### `daemon/feed_monitor.py` — Feed Polling

Fetches RSS/Atom feeds configured in `daemon/config.yaml`. Returns items newer than `last_feed_check`. Each item is checked for relevance against active hypotheses; relevant items are saved to `inbox/`.

### `daemon/state.py` — Persistent State

Single JSON file (`daemon/state.json`, gitignored) tracks everything the daemon needs across restarts:

| Field | Purpose |
|-------|---------|
| `last_notebook_commit` | Git commit hash; detects new notebook entries |
| `notebook_entries_posted` | Dates already announced to Discord |
| `last_new_nature_message_id` | Discord cursor for the tick loop |
| `last_new_nature_activity` | Timestamp of last human message (drives adaptive intervals) |
| `last_feed_check` | Timestamp; feeds only return items after this |
| `last_conversation_review` | Date of last daily synthesis pass |
| `responded_mention_ids` | Message IDs already replied to (cap 500); prevents restart duplicates |
| `last_startup` | ISO timestamp of most recent daemon startup |
| `last_clean_shutdown` | ISO timestamp of last graceful shutdown; absence implies crash |

---

## Research Inventory

Research output is organized around the **Double Freytag phase model** (Rao, *Tempo*). Each phase produces a typed artifact. The DS file is the narrative arc container spanning all phases of a single inquiry.

```
research/
├── ds/       DS-NNN — Deep Story arc files (one per inquiry thread)
│             The arc container: tracks phase position, tempo, transition trigger,
│             and blocking behavior for each thread. Opened at the start of any
│             new inquiry; closed after the separation event artifact is published.
├── c/        C-NNN — Curiosity items (exploration phase)
│             Provocations, not proto-laws. Flows in continuously from inbox,
│             Discord, reading, and observation. The only rule: not a candidate law.
├── h/        H-NNN — Hypothesis items (sensemaking phase, post-cheap-trick)
│             Tracks the developing framing from first insight to working claim.
│             Created at the cheap trick transition; closed when promoted to CL.
├── cl/       CL-NNN — Candidate Law items (valley phase)
│             Evidence accumulating under an organizing insight. Has a named
│             transition_trigger: the specific condition that would close the valley
│             and open the heavy lift.
├── theories/ T-NNN — Theory items (heavy lift phase)
│             Synthesis committed; writing the publishable artifact. A T item
│             only exists when Humboldt is actively writing toward publication.
└── f/        F-NNN — Falsification Monitor items (retrospective phase)
              Created only after a separation event — a published artifact available
              for independent review. Currently empty: no separation events have occurred.
```

**Phase-to-artifact mapping:**

| Phase | Artifact | Created when |
|-------|----------|-------------|
| Liminal Passage | — | — |
| Exploration | C (Curiosity) | Any provocation worth keeping |
| Sensemaking | H (Hypothesis) | Cheap trick fires; organizing insight crystallizes |
| Valley | CL (Candidate Law) | Evidence accumulating; arc in sustained investigation |
| Heavy Lift | T (Theory) | Writing toward a publishable separation event |
| Retrospective | F (Falsification Monitor) | After a published artifact enters external scrutiny |

**Transitions:** Cheap Trick (exploration → sensemaking) and Separation Event (heavy lift → retrospective) are named. Other transitions are unnamed and triggered by readiness assessment recorded in `transition_trigger` field of the arc's DS file.

**No confidence field.** There are no "established" laws — only laws that have not yet been falsified or superseded. F items use `status: active | superseded | refuted`.

---

## Behavior Inventory

Humboldt's research techniques are called **behaviors** — named, documented habits rather than recipes. The canonical inventory is `behaviors/registry.yaml`. Each behavior has a stable hash ID; M-0xx legacy IDs are cross-referenced as `legacy_id` fields.

**Two classification axes:**
- **Classification:** `supervised` (operator-triggered), `live` (autonomous during a session), `daemon` (runs outside sessions)
- **State:** `stub` (defined, not implemented), `prototyping` (in active development), `production` (stable)

**Boot behaviors** (deterministically triggered by the bootstrap sequence):

| ID | Name | State |
|----|------|-------|
| boot-000 | Wakeup Sequence | production |
| boot-001 | OODA Decision Gate | stub |

**Supervised behaviors** (operator-triggered):

| ID | Name | State | Legacy |
|----|------|-------|--------|
| behavior-t5m | Deep Read | prototyping | M-003 |
| behavior-m7v | Cross-Training | stub | M-014 |
| behavior-h4v | Field Trip | stub | M-007 |
| behavior-n1s | Visual Thinking | stub | M-009 |

**Live behaviors** (can run autonomously):

| ID | Name | State | Legacy |
|----|------|-------|--------|
| behavior-q2n | Random Links | production | M-001 |
| behavior-c7r | Curiosity Browsing | stub | — |
| behavior-f8p | Canonical Domains | stub | M-002 |
| behavior-j6d | Bullshit Detector | stub | M-008 |
| behavior-z8l | Fermi Estimation | stub | M-010 |
| behavior-y2g | Dyson Design | stub | M-011 |
| behavior-r4k | Thought Experiments | stub | M-012 |
| behavior-c9p | Design Fictions | stub | M-013 |
| behavior-s5j | Open Source Exploration | stub | M-018 |

**Daemon behaviors** (Discord bot + scheduled tasks):

| ID | Name | State |
|----|------|-------|
| behavior-e2h | Feed Intake | prototyping |
| behavior-a8r | Conversation Synthesis | prototyping |
| behavior-o4t | Idea/Link Capture | prototyping |
| behavior-g7u | Notebook Publish | production |
| behavior-v3c | Thread Farming | prototyping |

The full registry with descriptions, source files, and implementation notes is in `behaviors/registry.yaml`. The `methods/` directory contains the detailed specification documents for each behavior; behavior IDs are the canonical reference, M-0xx names are historical.

---

## Deep-Read Library

Source PDFs in `bibliography/deep-reads/`. Reading notes in `bibliography/notes/`. `READING-HINTS.md` is the pre-read index: each entry records the operator's reading hint before the read begins. All reads must use the actual PDF — never from training memory. This is enforced by M-003 procedure.

Candidates not yet in hand are tracked in `bibliography/deep-read-hopper.md`, with source of recommendation (deep read discovery, shallow read escalation, Discord, operator, web) and PDF status.

**Completed reads:** Simon (*Sciences of the Artificial*), Hamming (*You and Your Research*), von Humboldt (*Cosmos Vol. 1*), Rao (*Tempo*), Iverson (*Notation as a Tool of Thought*).

---

## Inbox

`inbox/` receives captured items from three sources:
1. **Discord capture** (`daemon/capture.py`) — ideas and references extracted from #new-nature
2. **Feed monitor** (`daemon/feed_monitor.py`) — relevant RSS/Atom items
3. **Discord sweep** (`humboldt discord sweep`) — historical batch capture

Inbox files are markdown with a structured header. Processed at the start of research sessions; promoted to references via `humboldt references promote` or the daily conversation review.

---

## Data Flow

### CLI research session

```
humboldt investigate "<topic>"
    │
    ├── assemble_context(): IDENTITY + METHOD + BOOTSTRAP + M-000 + inventory
    │
    ├── retrieval.py: embed topic → Pinecone (c3po + humboldt namespaces)
    │
    ├── synthesizer.py: Claude synthesis pass
    │   System: assembled persona (cached) + existing inventory
    │   User: retrieved chunks + research task
    │
    ├── write/update research/c|h|cl|theories|ds/ YAML/MD artifacts
    │
    └── git add research/ notebook/ && git commit && git push
```

### Daemon notebook cycle

```
New notebook commit detected (task_notebook, every 30 min)
    │
    ├── presence.generate_notebook_post() → #new-nature channel post
    │
    ├── ingest.ingest_all() → humboldt Pinecone namespace updated
    │
    └── publish.publish() → humboldt-notebook.html → git push website repo
```

### Daemon Discord presence cycle

```
New #new-nature messages (adaptive: 90s–30min)
    │
    ├── Skip @mention messages (handled by on_message)
    │
    ├── presence.generate_new_nature_response() → maybe post or open thread
    │
    └── capture.run_capture() → ideas/links → inbox/
```

---

## Connection to C3PO

| | C3PO | Humboldt |
|-|------|---------|
| User | Human researchers via web UI | Autonomous agent + PI Discord community |
| Task | Answer questions about protocols | Discover and formalize laws of protocolized systems |
| Output | Conversational response + citations | Law inventory, project arcs, theory drafts, notebook |
| Corpus access | Own query path | Shared Pinecone index (direct) + own humboldt namespace |
| Persona | Reference librarian | Naturalist investigator |
| Deployment | Cloudflare Worker | Local CLI + always-on daemon |

The shared Pinecone index means Humboldt benefits immediately from every new corpus ingestion done by c3po. The `humboldt` namespace is Humboldt-exclusive — c3po does not index it.

---

## Security

Keys follow the Protocol Institute security policy (`../admin/security.md`):
- All secrets in `.env` (gitignored, Dropbox-ignored)
- Values sourced from `../protocol-institute/.env.keys`
- Keys registered in `../admin/keys.md`
- Humboldt reuses c3po keys (VOYAGE, PINECONE, ANTHROPIC) — no new key provisioning required
- Additional key: `DISCORD_BOT_TOKEN`, `DISCORD_GUILD_ID`, `DISCORD_NEW_NATURE_CHANNEL_ID`, `DISCORD_OPERATOR_USER_ID` — registered in `../admin/keys.md`
