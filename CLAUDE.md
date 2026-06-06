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
pip install voyageai pinecone anthropic python-dotenv pyyaml rich pypdf markdown
```

---

## Keys

PI keys are stored in `../.env.keys` and inventoried in `../admin/keys.md`. Copy to `.env` (gitignored) before running scripts. After creating `.env`:

```bash
xattr -w com.dropbox.ignored 1 .env
```

Humboldt reuses the c3po keys — no new key provisioning required for Phase 1. Keys needed:

| Variable | Source |
|----------|--------|
| `VOYAGE_API_KEY` | `../.env.keys` — same as c3po |
| `PINECONE_API_KEY` | `../.env.keys` — same as c3po |
| `PINECONE_C3PO_HOST` | `../.env.keys` — same as c3po |
| `ANTHROPIC_API_KEY` | `../.env.keys` — same as c3po |
| `C3PO_WORKER_URL` | Phase 2 — URL of deployed c3po worker |
| `C3PO_MCP_KEY` | Phase 2 — `MCP_API_KEY` from c3po config |

---

## Pinecone Index

Humboldt uses the existing c3po index (read-only in Phase 1):

- Index name: `c3po`
- Host: `PINECONE_C3PO_HOST` from env
- Dimensions: 1024 (voyage-3)
- Metric: cosine

Namespaces (as of 2026-05-20 for PI corpus; 2026-05-26 for humboldt):
- `pdfs`: 766 vectors — Summer of Protocols papers
- `substack`: 1,040 vectors — Protocolized magazine
- `videos`: 2,940 vectors — talks and lectures
- `bibliography`: 278 vectors — curated references
- `discord`: 3,301 vectors — PI community Discord
- `discord_links`: 6,722 vectors — enriched Discord links
- `sig`: 4,689 vectors — SIG channel discussions
- `transcripts`: 4 vectors (grows with use)
- `humboldt`: 1,260 vectors (2026-06-06) — Humboldt's own notebook, reading notes, shallow reads, curiosities (C items), DS files, CL/T/H artifacts, inbox ideas

Do not write to c3po namespaces. Humboldt's own work goes to the `humboldt` namespace via `humboldt ingest`.

---

## Running Humboldt

```bash
source .venv/bin/activate

# Investigate a topic (corpus + synthesis)
python3 -m agent.humboldt investigate "protocol ossification"

# Display current law inventory
python3 -m agent.humboldt inventory

# Assess evidence for a specific law
python3 -m agent.humboldt assess F-001

# Generate candidate laws for a topic (no file output)
python3 -m agent.humboldt hypothesize "coordination cost"

# List documents in the deep-read library
python3 -m agent.humboldt library

# Deep-read a document from bibliography/deep-reads/ (reads actual PDF)
python3 -m agent.humboldt deepread "simon"

# Pre-notebook activity queue — automated process log since last notebook entry
python3 -m agent.humboldt pre-notebook              # show pending entries
python3 -m agent.humboldt pre-notebook mark-consumed # advance cursor after writing notebook

# Ingest Humboldt's own documents → humboldt Pinecone namespace
# Covers: notebook, reading notes, shallow reads, laws, hypotheses, inbox discord-ideas
# Run after each session that adds any of the above
python3 -m agent.humboldt ingest

# Triage inbox/feed-*.md items against current laws and hypotheses
# Produces a discard / shallow report (uses Haiku); depth decisions deferred to shallow-read
python3 -m agent.humboldt triage-feed
python3 -m agent.humboldt triage-feed --output inbox/triage-YYYY-MM-DD.md

# Shallow-read all non-discard items from a triage report (uses Haiku)
# Humboldt writes a synthesis note and decides: store-only or escalate-to-deep
# Output: bibliography/shallow-reads/YYYY-MM-DD-{title-slug}.md (idempotent)
python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md
python3 -m agent.humboldt shallow-read --from-triage inbox/triage-YYYY-MM-DD.md --dry-run

# Triage inbox/discord-*.md items (ideas + links from Discord)
# Produces a discard / shallow report (uses Haiku, higher discard bar than feed triage)
python3 -m agent.humboldt triage-discord
python3 -m agent.humboldt triage-discord --output inbox/triage-discord-YYYY-MM-DD.md

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

# Discord manual post
python3 -m agent.humboldt discord post           # post latest notebook entry to #new-nature
python3 -m agent.humboldt discord post --draft   # preview without posting
python3 -m agent.humboldt deepread "simon" "111-138"   # specific page range

# Discord catch-up sweep (captures ideas/links from historical #new-nature messages)
python3 -m agent.humboldt discord sweep
python3 -m agent.humboldt discord sweep --since 2026-05-01  # since a date (UTC)
python3 -m agent.humboldt discord sweep --limit 500          # cap at N messages

# Publish notebook entries to the PI website (humboldt-notebook.html → git push)
# The daemon runs this automatically after each new notebook entry is detected.
python3 -m agent.humboldt publish               # render + push to website repo
python3 -m agent.humboldt publish --dry-run     # preview rendering, no git ops

# Publish research status page (reads research/c,h,cl,theories,f → humboldt-research/index.html)
# Run after any session that changes the research inventory.
python3 -m agent.humboldt publish-research              # generate + push
python3 -m agent.humboldt publish-research --dry-run    # preview, no git ops
```

### Deep-read library

Source PDFs live in `bibliography/deep-reads/`. Drop new documents there; the `library` command lists them. Reading notes go in `bibliography/notes/`.

**Important:** M-003 deep reads must always read the actual PDF — never from training knowledge. In sessions (Claude Code), use the Read tool on the PDF in `bibliography/deep-reads/` with specific page ranges. In CLI mode, use `humboldt deepread`. Relying on training memory of a book defeats the purpose of deep reading.

---

## Research Inventory

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
