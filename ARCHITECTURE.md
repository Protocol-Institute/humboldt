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

`SOUL.md` is archived (2026-05-21). It was a monolithic persona file; the above modular documents supersede it.

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

- `notebook/*.md` — chunked by `##` section
- `bibliography/notes/*.md` — reading notes, chunked by section
- `research/laws/*.yaml` — full YAML per law
- `research/hypotheses/*.yaml` — full YAML per hypothesis

Each vector carries augmented metadata (document title, date, section) so retrieved results are self-identifying in prompts. Run after any session that produces new notebook entries or modifies laws. The daemon runs `ingest_all()` automatically after new notebook entries are detected.

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

```
research/
├── projects/       Arc documents — one per inquiry thread, phase-gated
│                   Phases: exploration | sensemaking | valley | heavy_lift | retrospective
│                   Templates: _template-discovered.md, _template-imported.md
├── laws/           YAML — formal law statements (produced at heavy_lift separation event)
├── hypotheses/     YAML — active hypotheses (legacy; new ones live in project sensemaking)
└── theories/       Markdown — unified theory development
```

**Project files** are the primary tracking unit for research arcs. Hypothesis YAMLs (H-00x) are a legacy format; new research threads open as project files under `research/projects/`.

**Law YAML schema:**
```yaml
id, name, statement, type, confidence, domains,
related_laws, mechanism, falsification_conditions,
counterexamples, evidence, notes, project_file, registered
```

**Current inventory** (as of 2026-05-27): L-001 through L-005 (formal laws), H-001 and H-002 (active hypotheses), P-001 through P-007 (project arcs).

---

## Methods Inventory

`methods/` contains Humboldt's research technique library — M-000 through M-017:

| Method | Name | Role |
|--------|------|------|
| M-000 | OODA Loop | OS kernel — the core decision gate for every session |
| M-001 | Random Links | Serendipitous cross-domain connection |
| M-002 | Canonical Domains | Rotation through vetted empirical domains |
| M-003 | Deep Read | Structured reading protocol for source texts |
| M-004 | Reading Prioritization | Sequencing the reading queue |
| M-005 | Explore-Exploit | Balancing new territory vs. deepening existing threads |
| M-006 | Research Conversations | Treating discussions as research inputs |
| M-007 | Field Trip | Empirical domain immersion |
| M-008 | Bullshit Detector | Adversarial testing of candidate laws |
| M-009 | Visual Thinking | Diagram-based reasoning |
| M-010 | Fermi Estimation | Order-of-magnitude sanity checks |
| M-011 | Dyson Design | Speculative design as a research tool |
| M-012 | Thought Experiments | Controlled counterfactual reasoning |
| M-013 | Design Fictions | Narrative-form speculation |
| M-014 | Cross-Training | Deliberate domain rotation |
| M-015 | Stress-Relax | Alternating intensity and incubation |
| M-016 | Researcher Calibration | Self-assessment of research craft maturity |
| M-017 | Research Time Management | Phase-position diagnosis and session pacing |

---

## Deep-Read Library

Source PDFs in `bibliography/deep-reads/`. Reading notes in `bibliography/notes/`. `READING-HINTS.md` is the pre-read index: each entry records the operator's reading hint, which shapes the M-003 Phase 1 structural hypothesis. All reads must use the actual PDF — never from training memory.

Current library: Simon (*Sciences of the Artificial*), Hamming (*You and Your Research*), Humboldt (*Cosmos Vol. 1*), Rao (*Tempo*).

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
    ├── write/update research/laws/ or research/projects/ YAML/MD
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
