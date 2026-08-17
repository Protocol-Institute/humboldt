# CLAUDE.md — Humboldt

> **Environment rules, keys & safety policies:** see [Code/CLAUDE.md](../../CLAUDE.md) — read before starting work.
> **PI key registry & security policy:** see [`../admin/keys.md`](../admin/keys.md) and [`../admin/security.md`](../admin/security.md). Do not register PI keys in `Code/.env.keys`.

Humboldt is the Protocol Institute's artificial researcher — an independent investigator of the **new nature**, laws of protocolized and artificial systems. See `README.md` for the research agenda; `ARCHITECTURE.md` for the system design.

**Key persona documents** (loaded dynamically into every system prompt via `assemble_context()`):

| Document | Role |
|----------|------|
| `IDENTITY.md` | Who Humboldt is — lineage, mission, temperament, voice |
| `LINEAGE.md` | Earned intellectual lineage — grows via deep reads and established laws |
| `MEMORY.md` | Narrative memory of the research journey — updated at significant moments |
| `METHOD.md` | Epistemic standards — evidence provenance, confidence levels, falsification |
| `BOOTSTRAP.md` | Wakeup sequence + Decide-phase configuration |
| `methods/M-000-ooda.md` | OS kernel — the OODA decision gate and research loop |
| `SOUL.md` | **Archived** 2026-05-21 — superseded by the above |

---

## Python

Use `/opt/homebrew/bin/python3` (Python 3.14). Activate venv before running scripts:

```bash
source .venv/bin/activate
```

Install deps:

```bash
pip install voyageai pinecone anthropic python-dotenv pyyaml ruamel.yaml rich pypdf markdown
```

---

## Keys

PI keys are stored in `../.env.keys` and inventoried in `../admin/keys.md`. Copy to `.env` (gitignored) before running scripts. After creating `.env`:

```bash
xattr -w com.dropbox.ignored 1 .env
```

All PI org keys. No personal keys used.

| Variable | Source |
|----------|--------|
| `VOYAGE_API_KEY` | `../.env.keys` — PI org Voyage AI key |
| `PINECONE_API_KEY` | `../.env.keys` — PI org Pinecone key |
| `PINECONE_C3PO_HOST` | `../.env.keys` — c3po corpus index (read) |
| `PINECONE_HUMBOLDT_HOST` | `../.env.keys` — humboldt research index (read/write) |
| `ANTHROPIC_API_KEY` | `../.env.keys` — personal key (PI org key deferred) |
| `C3PO_WORKER_URL` | Phase 2 — URL of deployed c3po worker |
| `C3PO_MCP_KEY` | Phase 2 — `MCP_API_KEY` from c3po config |

---

## Pinecone Indexes

Humboldt uses two separate indexes on the PI org Pinecone account:

### c3po index (corpus, read-only)
- Index name: `c3po`
- Host: `PINECONE_C3PO_HOST` from env
- Dimensions: 1024 (voyage-3) · Metric: cosine · Cloud: aws us-east-1

PI corpus namespaces (as of 2026-06-07):
- `pdfs`: 750 vectors — Summer of Protocols papers
- `substack`: 1,080 vectors — Protocolized magazine
- `videos`: 2,940 vectors — talks and lectures
- `bibliography`: 278 vectors — curated references
- `discord`: 5,578 vectors — PI community Discord
- `discord_links`: 9,650 vectors — enriched Discord links
- `sig`: 5,315 vectors — SIG channel discussions
- `transcripts`: 22 vectors (grows with use)
- `meta`: 32 vectors
- `definitions`: 560 vectors

### humboldt index (research artifacts, read/write)
- Index name: `humboldt`
- Host: `PINECONE_HUMBOLDT_HOST` from env
- Dimensions: 1024 (voyage-3) · Metric: cosine · Cloud: aws us-east-1
- Default namespace (no namespace name)
- 5,105 vectors (2026-06-24) — notebook, notes, shallow reads, C/H/CL research YAMLs, DS arc files, inbox ideas

Humboldt's own work goes here via `humboldt ingest`. Do not write to c3po namespaces.

---

## Running Humboldt

```bash
source .venv/bin/activate

# Investigate a topic (corpus + synthesis)
python3 -m agent.humboldt investigate "protocol ossification"

# Display current law inventory
python3 -m agent.humboldt inventory

# ── Redesign 2026-08 (branch redesign-2026-08) — law encyclopedia + bibliography ──
# The unified law record (laws/L-NNN-*.yaml) replaces the C/H/CL/T/F artifacts.
# agent/laws.py = CRUD/validation/stage-machine/history (ruamel round-trip).
python3 -m agent.humboldt laws list [--stage S] [--status S]   # inventory table
python3 -m agent.humboldt laws show L-003                       # full record
python3 -m agent.humboldt laws validate [L-003 | all]           # schema + stage-machine

# Canonical bibliography (bibliography/bibliography.yaml). agent/bibliography.py.
python3 -m agent.humboldt bib list [--depth D] [--kind K] [--year Y]
python3 -m agent.humboldt bib show bib-0042
python3 -m agent.humboldt bib stats
python3 -m agent.humboldt bib migrate [--dry-run]   # one-shot legacy-source migration
python3 -m agent.humboldt bib backfill-references [--dry-run]
        # one-shot: law free-text `references:` and examples[].source → bib-NNNN ids
        # where a confident match exists (arXiv id / read-file path / url / title).
        # Ran 2026-08-10: 11 evidence sources resolved across 7 laws; the 21
        # free-text `references:` entries name literatures, not works, so they stay.

# ── Funnel engines (Phase 2) — agent/induct.py + agent/assess.py ──
# induct  = stage 5: seeds + reads-since-cursor + inventory → new laws / evidence (Sonnet).
# assess  = stage 6/8: one law vs its advance trigger → PROMOTE/HOLD/DEMOTE, applied via
#           the laws.py stage machine (Sonnet routine; Opus for heavy-lift/retrospective).
# Both consume the Fable prompts in prompts/{induct,assess}.md. Events → analytics/events.jsonl
# + behaviors/log.jsonl (via agent/funnel_log.py). NOT yet daemon-wired (Phase 5).
python3 -m agent.humboldt induct                     # run the induction sweep
python3 -m agent.humboldt induct --dry-run           # call model, apply nothing
python3 -m agent.humboldt induct --since YYYY-MM-DD    # override the read cursor
python3 -m agent.humboldt assess L-003               # assess one law (promote/hold/demote)
python3 -m agent.humboldt assess L-003 --dry-run     # call model, apply nothing
python3 -m agent.humboldt assess --all               # assess every active law
python3 -m agent.humboldt assess L-003 --no-corpus   # assess on the record alone (see below)

# ── Corpus-read circuit breaker (session 30, agent/read_budget.py) ──
# Pinecone enforces TWO independent monthly caps on reads — read units and egress bytes.
# Either one 429s every query account-wide while upserts and describe_index_stats keep
# working, so a quota check MUST exercise `query`, not `describe`.
# State: data/read-pause.json (gitignored). Auto-trips on a quota 429; self-clears.
# Distinct from `daemon pause`: that means "don't speak", this means "you may speak but
# you have no corpus". Retrieval raises RetrievalUnavailable — it never returns [], since
# an empty list is indistinguishable from "the corpus has nothing" (the 2026-08 bug).
# While tripped: `assess` refuses (--no-corpus overrides), investigate/hypothesize exit 1,
# Discord replies and the site chat disclose the outage. `induct` is UNAFFECTED (no reads).
python3 -m agent.humboldt read-status                  # are corpus reads available?
python3 -m agent.humboldt read-pause <YYYY-MM-DD> [why] # force reads offline
python3 -m agent.humboldt read-unpause                 # clear the pause

# Generate candidate laws for a topic (no file output)
python3 -m agent.humboldt hypothesize "coordination cost"

# List documents in the deep-read library
python3 -m agent.humboldt library

# Deep-read a document from bibliography/deep-reads/ (reads actual PDF)
python3 -m agent.humboldt deepread "simon"

# Batch deep-read all unread arxiv papers + write post-hoc verdicts to bibliography/deep-read-verdicts.md
python3 -m agent.humboldt batch-deepread
python3 -m agent.humboldt batch-deepread "arxiv-2606*"  # subset by glob

# Pre-notebook activity queue — automated process log since last notebook entry
python3 -m agent.humboldt pre-notebook              # show pending entries
python3 -m agent.humboldt pre-notebook mark-consumed # advance cursor after writing notebook

# Ingest Humboldt's own documents → humboldt Pinecone namespace
# Covers: notebook, reading notes, shallow reads, C/H/CL/F/DS artifacts, inbox discord-ideas
# Run after each session that adds any of the above
python3 -m agent.humboldt ingest

# ── Funnel stages 2–3 (reworked 2026-08-10 for the redesign) ──
# Context comes from laws/*.yaml + laws/seeds/ via agent/funnel_context.py — the
# old research/laws/ + research/hypotheses/ readers are gone. Every non-discard
# item is tagged content|meta and gets a bib-NNNN entry at read_depth: listed.

# Triage inbox/feed-*.md items against the law inventory and seed pool (Haiku)
python3 -m agent.humboldt triage-feed
python3 -m agent.humboldt triage-feed --output inbox/triage-YYYY-MM-DD.md
python3 -m agent.humboldt triage-feed --limit N     # first N items only (cheap test)
python3 -m agent.humboldt triage-feed --dry-run     # call the model, write nothing

# Shallow-read all non-discard items from a triage report (uses Haiku)
# Writes a synthesis note; upgrades the bib entry to read_depth: shallow with
# summary: pointing at the note; emits a seed into laws/seeds/ when the note
# surfaces something law-shaped (never for kind: meta items); decides
# store-only vs escalate-to-deep. Skips the Pinecone ingest while paused.
# Output: bibliography/shallow-reads/YYYY-MM-DD-{title-slug}.md (idempotent)
python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md
python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md --limit N
python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md --dry-run

# Triage inbox/discord-*.md items (ideas + links from Discord)
# Produces a discard / shallow report (uses Haiku, higher discard bar than feed triage).
# Meta items are tagged, not discarded — the old "discard research meta-process" rule is gone.
python3 -m agent.humboldt triage-discord
python3 -m agent.humboldt triage-discord --output inbox/triage-discord-YYYY-MM-DD.md
python3 -m agent.humboldt triage-discord --limit N / --dry-run

# Inbox lifecycle management
python3 -m agent.humboldt inbox status                    # show inbox composition + processed count
python3 -m agent.humboldt inbox archive-discards --from-triage inbox/triage-YYYY-MM-DD.md
                                                          # move DISCARD items → inbox/processed/
python3 -m agent.humboldt inbox cleanup                   # delete processed items older than 30 days

# People / trust model
python3 -m agent.humboldt people                         # contribution summary, sorted by trust
python3 -m agent.humboldt people @handle                 # detail for one contributor

# Daemon (Discord bot + scheduled tasks)
python3 -m agent.humboldt daemon run       # start daemon (blocking)
python3 -m agent.humboldt daemon restart   # hot-reload after code changes (SIGUSR1, preserves state)
python3 -m agent.humboldt daemon status    # show PID + last checked timestamps
python3 -m agent.humboldt daemon pause <YYYY-MM-DD>   # offline for posting/querying + Pinecone writes through date (inclusive)
python3 -m agent.humboldt daemon unpause              # resume normal operation immediately

# Discord manual post
python3 -m agent.humboldt discord post           # post latest notebook entry to #new-nature
python3 -m agent.humboldt discord post --draft   # preview without posting
python3 -m agent.humboldt deepread "simon" "111-138"   # specific page range

# Discord catch-up sweep (captures ideas/links from historical #new-nature messages)
python3 -m agent.humboldt discord sweep
python3 -m agent.humboldt discord sweep --since 2026-05-01  # since a date (UTC)
python3 -m agent.humboldt discord sweep --limit 500          # cap at N messages

# Behavior graph — MDP visualization and supervisory loop
# Graph definition: behaviors/mdp.yaml  Log: behaviors/log.jsonl
python3 -m agent.humboldt behaviors graph                          # text summary: phases, nodes, edge counts
python3 -m agent.humboldt behaviors admin                          # start local admin web UI (localhost:7878)
python3 -m agent.humboldt behaviors log <id> [--arc ARC] [--note] # record a behavior visit to log.jsonl
python3 -m agent.humboldt behaviors supervisory                    # analyze log; suggest weight updates

# ⚠ Deploy target: `wrangler pages deploy` infers the branch from git and makes a
# PREVIEW deployment off anything other than `main`, returning success either way.
# publish-site succeeding does NOT mean humboldt.protocol-institute.org changed — the
# whole redesign-2026-08 branch has only ever deployed to preview URLs. Check with
# agent.publish_site.is_production_deploy(); law_notify refuses to announce off-branch.

# Publish the humboldt-site to Cloudflare Pages (humboldt.protocol-institute.org)
# Rebuilds all pages (notebook, research, reading, architecture, about, chat) and deploys.
# The daemon runs this automatically after each new notebook entry is detected.
# Run after any session that changes notebook, research, bibliography, or ARCHITECTURE.md.
python3 -m agent.humboldt publish-site              # build + deploy to CF Pages
python3 -m agent.humboldt publish-site --dry-run    # build only, no deploy
```

### Deep-read library

Source PDFs live in `bibliography/deep-reads/`. Drop new documents there; the `library` command lists them. Reading notes go in `bibliography/notes/`.

**Important:** M-003 deep reads must always read the actual PDF — never from training knowledge. In sessions (Claude Code), use the Read tool on the PDF in `bibliography/deep-reads/` with specific page ranges. In CLI mode, use `humboldt deepread`. Relying on training memory of a book defeats the purpose of deep reading.

---

## Research Inventory

> **⚠ Superseded by the 2026-08 redesign (branch `redesign-2026-08`, Phase 1 done).**
> The C/H/CL/T/F typed-artifact system below is retired. The unified **law record**
> (`laws/L-NNN-*.yaml`, schema `laws/_schema.yaml`) is now the single research artifact;
> `laws/seeds/` is the holding pen (migrated from `research/c/`); `bibliography/bibliography.yaml`
> is the canonical bibliography. The old `research/` subtree (`cl/ ds/ theories/ f/ h/
> questions.md`) is archived at `research/_archive/`; only `research/agenda.md` stays live.
> The section below is kept for reference until the Phase 6 doc rewrite. See
> `plans/redesign-2026-08.md`.

`research/` is the core output — always commit it. The schema follows the Double Freytag
phase model (Rao, *Tempo*). Each phase produces a typed artifact; the DS file is the
narrative arc container spanning all phases.

```
research/
├── ds/       DS-NNN — Deep Story arc files (one per inquiry)
│             Templates: _template-discovered.md, _template-imported.md
│             DS-001 Ossification (F-001, retrospective)
│             DS-002 Hardness Asymmetry (F-002, retrospective)
│             DS-003 Formalization Ratchet (CL-001, valley)
│             DS-004 Goodhart import (F-003 source law, valley for protocol-theoretic CL)
│             DS-005 Gall import (F-004 source law, valley for protocol-theoretic CL)
│             DS-006 Coordination Cost (CL-002, valley)
│             DS-007 Trust Ratchet (CL-003, valley)
├── c/        C-NNN — Curiosity items (exploration phase)
│             Schema in _schema.yaml
├── h/        H-NNN — Hypothesis items (sensemaking phase, post-cheap-trick)
│             Schema in _schema.yaml
├── cl/       CL-NNN — Candidate Law items (valley phase)
│             Schema in _schema.yaml
│             CL-001 Formalization Ratchet, CL-002 Coordination Cost, CL-003 Trust Ratchet
├── theories/ T-NNN — Theory items (heavy lift phase)
│             Schema in _schema.yaml
└── f/        F-NNN — Falsification Monitor items (retrospective phase)
              Schema in _schema.yaml. No "established" — only unfalsified.
              F-001 Ossification, F-002 Hardness Asymmetry
              F-003 Goodhart (imported source law), F-004 Gall (imported source law)

bibliography/
├── deep-reads/   PDF source documents — drop new deep-read texts here
│                 READING-HINTS.md — reading hints index (required before any deep read)
├── notes/        Markdown reading notes — one per source, produced by M-003
└── shallow-reads/ One-paragraph synthesis notes for triage-feed shallow decisions
                  _SHALLOW-READ-FORMAT.md — template (skipped by ingest, prefix _)
```

**Phase-to-artifact mapping (Double Freytag):**

| Phase | Artifact | Schema |
|-------|----------|--------|
| Liminal Passage | — | null |
| Exploration | C (Curiosity) | `research/c/_schema.yaml` |
| Sensemaking | H (Hypothesis) | `research/h/_schema.yaml` |
| Valley | CL (Candidate Law) | `research/cl/_schema.yaml` |
| Heavy Lift | T (Theory) | `research/theories/_schema.yaml` |
| Retrospective | F (Falsification Monitor) | `research/f/_schema.yaml` |

**Transitions:** Cheap Trick (exploration → sensemaking) and Separation Event
(heavy lift → retrospective) are named. The other 4 transitions are unnamed and
triggered by readiness assessment.

**DS file conventions:**
- New arc → use `_template-discovered.md` or `_template-imported.md`
- Header field `**Phase artifact:**` names the current typed artifact (e.g., `CL-002`)
- No "established" confidence — F items are monitored, not certified
- When a CL item is updated, also update `related:` in any affected F/CL files

---

## Session Rituals

Sessions touch one or more tracks. **Startup:** Track 2 always runs first; Track 1 runs when research work is planned; Track 3 has no startup. **Wrapup:** a single unified ritual (see below) always runs regardless of which tracks were active. Steps marked [T1] are skipped only when no Track 1 work occurred this session.

Items marked **[REQUIRED]** are non-skippable. The session checklist must be posted before the session closes.

---

### Track 2 Startup — always runs first

*Infrastructure and orientation. Runs at the start of every session.*

1. Read `status.md` — last entry: what was open, where things ended. Note the daemon PID.
2. Read `TODO.md` — current Track 2 and Track 3 priorities.
3. Check `research/cl/` (candidate laws) and `research/f/` (falsification monitors) — current counts and any new monitoring notes.
4. Note any CL items with `transition_trigger` conditions that may be within reach this session.
5. Confirm which tracks are active in this session and declare them at the start.

---

### Track 1 Startup — runs when Track 1 work is planned

*Orients the researcher before investigation. Read before generating or testing anything.*

1. Run `python3 -m agent.humboldt pre-notebook` — shows all automated activity (shallow reads, ingests, triages, daemon reviews) since the last notebook entry. This is the "what happened while I was away" queue; it feeds into the notebook entry at wrapup.
2. Read the two most recent lab notebook entries (`notebook/`) — pick up the live thread of inquiry.
3. Read `research/agenda.md` — Humboldt's own research queue.
4. Scan `research/cl/` for active candidate laws — read each `transition_trigger` and assess readiness. Note which are productive valley vs. stagnant.

---

### Track 3 Startup — none

Track 3 has no startup ritual. It responds to Track 1 and 2 output at wrapup.

---

### Session Wrapup — unified ritual, always runs, never abbreviated

**Before starting:** Ask "Ready to wrap up, or is there more to do?" Never initiate the wrapup unilaterally.

**The session is not closed until the wrapup checklist has been posted.**

Run all steps in order. Steps marked **[T1]** are skipped only when no Track 1 work occurred; all other steps always run.

1. **[T1]** **[REQUIRED]** Write lab notebook entry `notebook/YYYY-MM-DD.md`. Structure: (a) open with a synthesized paragraph covering all pending pre-notebook entries — "Since the last session, I triaged X items, shallow-read Y, the daemon did Z" — then (b) the live session narrative. Run `python3 -m agent.humboldt pre-notebook` at startup (step 1) to get the queue; synthesize it here. After writing, run `python3 -m agent.humboldt pre-notebook mark-consumed` to advance the cursor. Update `notebook/README.md` index.
2. **[T1]** **[REQUIRED]** Update `research/agenda.md` — mark completed items, add new items that emerged, reorder to reflect current state of inquiry.
3. **[T1]** Update `research/cl/`, `research/h/`, `research/f/`, or `research/theories/` YAMLs for anything touched this session.
4. **[T1]** Update `bibliography/notes/[source].md` if a deep read occurred.
5. **[REQUIRED]** Write `dev-log.md` entry using the schema below. Required for every session — including short, bug-fix, and inconclusive sessions. No devlog entry = session not closed.
6. Update `status.md` — dated entry, one-line summary, open items. Always include daemon PID (or "not running").
7. Update `CLAUDE.md` if: namespace vector counts changed, new CLI commands added, new keys added, or ritual definitions changed.
8. Scan session output for patterns to generalize into `_template/` — update relevant files or note "no changes" in the checklist below.
9. Commit all changed files — `research/`, `notebook/`, `bibliography/`, `methods/`, `dev-log.md`, `status.md`, `CLAUDE.md`, `TODO.md`, `_template/`, any other modified docs. **Do not commit before step 5** — the devlog entry must be in the same commit as the work it covers.
10. Push to `origin main`.
11. Update Claude memory at `/Users/Venkat/.claude/projects/-Users-Venkat-Dropbox-Code-protocol-institute-humboldt/memory/` — anything non-obvious not already in CLAUDE.md.
12. **[REQUIRED]** Post the wrapup checklist.

---

### Dev-log entry schema

Required fields — every entry, every session:

```
## YYYY-MM-DD (session N) — Short descriptive title

**Tracks active:** T1 / T2 / T3
**Daemon PID:** [PID] (or "not running")

[Body: what changed and why. Explain reasoning behind decisions, not just what files changed.
Name the current state of affected subsystems after the session ends. Note anything that
closes off alternatives or locks in a direction. A three-sentence entry is fine for a short
session. Zero sentences is never acceptable.]

**Open (next session):**
- [item]
```

---

### Wrapup checklist (post at end of every session)

```
SESSION WRAPUP — [YYYY-MM-DD] — session [N]
══════════════════════════════════════════════════
Tracks active: [T1 / T2 / T3]
Daemon PID: [PID or "not running"]

 1. [T1] Notebook entry written ........... [✓ | — no T1]
 2. [T1] research/agenda.md updated ........ [✓ | — no T1]
 3. [T1] Laws/hypotheses YAMLs updated ..... [✓ | n/a | — no T1]
 4. [T1] Reading notes updated ............. [✓ | n/a | — no T1]
 5.      dev-log.md entry written ........... [✓ | ✗ EXPLAIN]
 6.      status.md updated .................. [✓ | ✗ EXPLAIN]
 7.      CLAUDE.md updated .................. [✓ | n/a]
 8.      Template scan ...................... [✓ no changes | ✓ updated: ___ | n/a]
 9.      Committed .......................... [✓ | ✗ EXPLAIN]
10.      Pushed ............................. [✓ | ✗ EXPLAIN]
11.      Claude memory updated .............. [✓ | n/a]
══════════════════════════════════════════════════
```

---

### Keys/env (any track, if changed)

New env vars: update `.env.template`; add to `../.env.keys`; add row to `../admin/keys.md`.
