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
- `humboldt`: ~99 vectors (2026-05-28; ~170 after pending ingest) — Humboldt's own notebook, reading notes, shallow reads, laws, hypotheses, inbox ideas

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
python3 -m agent.humboldt assess L-001

# Generate candidate laws for a topic (no file output)
python3 -m agent.humboldt hypothesize "coordination cost"

# List documents in the deep-read library
python3 -m agent.humboldt library

# Deep-read a document from bibliography/deep-reads/ (reads actual PDF)
python3 -m agent.humboldt deepread "simon"

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
```

### Deep-read library

Source PDFs live in `bibliography/deep-reads/`. Drop new documents there; the `library` command lists them. Reading notes go in `bibliography/notes/`.

**Important:** M-003 deep reads must always read the actual PDF — never from training knowledge. In sessions (Claude Code), use the Read tool on the PDF in `bibliography/deep-reads/` with specific page ranges. In CLI mode, use `humboldt deepread`. Relying on training memory of a book defeats the purpose of deep reading.

---

## Research Inventory

`research/` is the core output — always commit it. Files:

```
research/
├── projects/     Markdown — living arc documents (one per inquiry, phase-gated)
│                 Templates: _template-discovered.md, _template-imported.md
│                 P-001 Ossification (retro), P-002 Hardness Asymmetry (retro)
│                 P-003 Formalization Ratchet (valley), P-004 Goodhart import (valley)
│                 P-005 Gall import (valley), P-006 Coordination Cost (valley)
│                 P-007 Trust Ratchet (valley)
├── laws/         YAML — publication artifacts for completed heavy lifts
│                 Schema: id, name, statement, type, confidence, domains,
│                 related_laws, mechanism, falsification_conditions,
│                 counterexamples, evidence, notes, project_file, registered
├── hypotheses/   YAML — lightweight index pointing to project files (being phased out)
│                 Hypothesis tracking has moved to project files (sensemaking section)
└── theories/     Markdown — unified theory development

bibliography/
├── deep-reads/   PDF source documents — drop new deep-read texts here
│                 READING-HINTS.md — reading hints index (required before any deep read)
├── notes/        Markdown reading notes — one per source, produced by M-003
└── shallow-reads/ One-paragraph synthesis notes for triage-feed shallow decisions
                  _SHALLOW-READ-FORMAT.md — template (skipped by ingest, prefix _)
```

**Project file conventions:**
- New inquiry arc → use `_template-discovered.md` if originated here; `_template-imported.md` if importing a named law
- Phase field tracks current arc position (M-017 vocabulary): `exploration | sensemaking | valley | heavy_lift | retrospective`
- Law YAMLs are created at the separation event (end of heavy lift) — not before
- Hypothesis YAMLs (H-00x) are legacy; new hypotheses live in project file sensemaking sections
- "Imported regularities" (L-004 Goodhart, L-005 Gall) enter at valley phase — sensemaking done elsewhere

When a new law is added or updated, also update the `related_laws` field in any affected files.

---

## Session Rituals

Sessions touch one or more tracks. Track 2 startup always runs. Tracks 1 and 3 startup/wrapup run only when that track is active in the session. **Track 2 is the enforcer at wrapup: it must explicitly report on the wrapup checklist for every active track before the session closes.**

Items marked **[REQUIRED]** are non-skippable. Skipping them must be flagged explicitly and justified.

---

### Track 2 Startup — always runs first

*Infrastructure and orientation. Runs at the start of every session.*

1. Read `status.md` — last entry: what was open, where things ended. Note the daemon PID.
2. Read `TODO.md` — current Track 2 and Track 3 priorities.
3. Check `research/laws/` — current count by confidence level.
4. Note any hypotheses `status: active` that are ready for investigation.
5. Confirm which tracks are active in this session and declare them at the start.

---

### Track 1 Startup — runs when Track 1 work is planned

*Orients the researcher before investigation. Read before generating or testing anything.*

1. Read the two most recent lab notebook entries (`notebook/`) — pick up the live thread of inquiry.
2. Read `research/agenda.md` — Humboldt's own research queue. This is the Track 1 to-do list; it lives in `research/` because it belongs to Humboldt, not to the operator.
3. Scan `research/hypotheses/` for active hypotheses — identify which are ready for adversarial testing vs. still generative.

---

### Track 3 Startup — none

Track 3 has no startup ritual. It responds to Track 1 and 2 output at wrapup.

---

### Track 1 Wrapup — runs after any Track 1 work

1. **[REQUIRED]** Write lab notebook entry in `notebook/YYYY-MM-DD.md` — first person, covers what was investigated, what emerged, what questions opened. Update `notebook/README.md` index. Entry must be written even if the session felt inconclusive; inconclusive sessions often contain the most important observations.
2. **[REQUIRED]** Update `research/agenda.md` — revise priorities based on what this session produced. Mark completed items done, add new items that emerged, reorder based on current state of inquiry. This is Humboldt's own list; it should reflect Humboldt's current sense of what matters next, not a frozen prior plan.
3. Update any `research/laws/` or `research/hypotheses/` YAML files modified during the session.
4. Update reading log in `bibliography/notes/[source].md` if a deep read session occurred.

---

### Track 2 Wrapup — always runs last, enforces all other tracks

*The enforcer. Track 2 closes the session and verifies all active tracks completed their wrapup.*

1. Update `status.md` — dated entry, one-line summary, open items. **Always include current daemon PID** (or "daemon not running") so status.md is the single source of truth for daemon state.
2. Update `CLAUDE.md` if: namespace vector counts changed, new CLI commands added, new keys added, or ritual definitions changed.
3. Commit all changed files — `research/`, `notebook/`, `bibliography/`, `methods/`, `_template/`, any modified docs.
4. Push to `origin main`.
5. **[REQUIRED]** Write `dev-log.md` entry — covers Track 2 and Track 3 activity: infrastructure changes, persona decisions, open issues updated. Even a short entry is required; silence is not.
6. Update Claude memory at `/Users/Venkat/.claude/projects/-Users-Venkat-Dropbox-Code-protocol-institute/memory/` — anything non-obvious about research findings, design decisions, or pipeline changes.
7. **[REQUIRED]** Report the wrapup checklist explicitly:

```
SESSION WRAPUP REPORT
─────────────────────
Active tracks this session: [T1 / T2 / T3]

Track 1: [✓ lab notebook written | SKIPPED — reason: ___]
Track 2: [✓ dev-log written | SKIPPED — reason: ___]
         [✓ status.md updated]
         [✓ committed and pushed]
Track 3: [✓ template scan completed | no material changes | SKIPPED — reason: ___]
```

---

### Track 3 Wrapup — runs after Track 1 and 2 wrapup, when either was active

*Scans session output for patterns that should generalize into the template.*

1. Review Track 1 wrapup output (new techniques, new method applications, notebook observations about research process) — does any of it represent a generalizable pattern not yet in `_template/`?
2. Review Track 2 wrapup output (persona decisions, SOUL/METHOD changes, ritual refinements) — does any of it update the template's recommended patterns?
3. If material changes found: update the relevant file(s) in `_template/`. If no material changes: note "no template updates" in the Track 3 line of the wrapup report.

---

### Keys/env (any track, if changed)

New env vars: update `.env.template`; add to `../.env.keys`; add row to `../admin/keys.md`.
