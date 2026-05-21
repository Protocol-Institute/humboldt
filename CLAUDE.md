# CLAUDE.md — Humboldt

> **Environment rules, keys & safety policies:** see [Code/CLAUDE.md](../../CLAUDE.md) — read before starting work.
> **PI key registry & security policy:** see [`../admin/keys.md`](../admin/keys.md) and [`../admin/security.md`](../admin/security.md). Do not register PI keys in `Code/.env.keys`.

Humboldt is the Protocol Institute's artificial researcher — an independent investigator of the **new nature**, laws of protocolized and artificial systems. See `README.md` for the research agenda; `SOUL.md` for the researcher's identity; `ARCHITECTURE.md` for the system design.

---

## Python

Use `/opt/homebrew/bin/python3` (Python 3.14). Activate venv before running scripts:

```bash
source .venv/bin/activate
```

Install deps:

```bash
pip install voyageai pinecone anthropic python-dotenv pyyaml rich
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

Namespaces (as of 2026-05-20):
- `pdfs`: 766 vectors — Summer of Protocols papers
- `substack`: 1,040 vectors — Protocolized magazine
- `videos`: 2,940 vectors — talks and lectures
- `bibliography`: 278 vectors — curated references
- `discord`: 3,301 vectors — PI community Discord
- `discord_links`: 6,722 vectors — enriched Discord links
- `sig`: 4,689 vectors — SIG channel discussions
- `transcripts`: 4 vectors (grows with use)

Humboldt will add a `humboldt` namespace in Phase 4 for its own ingested sources. Do not write to c3po namespaces.

---

## Running Humboldt

```bash
source .venv/bin/activate

# Investigate a topic
python3 -m agent.humboldt investigate "protocol ossification"

# Display current law inventory
python3 -m agent.humboldt inventory

# Assess evidence for a specific law
python3 -m agent.humboldt assess L-001

# Generate candidate laws for a topic (no file output)
python3 -m agent.humboldt hypothesize "coordination cost"
```

---

## Research Inventory

`research/` is the core output — always commit it. Files:

```
research/
├── laws/         YAML — candidate laws (schema in SOUL.md)
├── hypotheses/   YAML — active research questions
└── theories/     Markdown — unified theory development
```

When a new law is added or updated, also update the `related_laws` field in any affected files.

---

## Session Rituals

Sessions touch one or more tracks. Track 2 startup always runs. Tracks 1 and 3 startup/wrapup run only when that track is active in the session. **Track 2 is the enforcer at wrapup: it must explicitly report on the wrapup checklist for every active track before the session closes.**

Items marked **[REQUIRED]** are non-skippable. Skipping them must be flagged explicitly and justified.

---

### Track 2 Startup — always runs first

*Infrastructure and orientation. Runs at the start of every session.*

1. Read `status.md` — last entry: what was open, where things ended.
2. Read `dev-log.md` — any open infrastructure issues that affect this session.
3. Check `research/laws/` — current count by confidence level.
4. Note any hypotheses `status: active` that are ready for investigation.
5. Confirm which tracks are active in this session and declare them at the start.

---

### Track 1 Startup — runs when Track 1 work is planned

*Orients the researcher before investigation. Read before generating or testing anything.*

1. Read the two most recent lab notebook entries (`notebook/`) — pick up the live thread of inquiry.
2. Scan `research/hypotheses/` for active hypotheses — identify which are ready for adversarial testing vs. still generative.
3. Identify any open questions from the most recent notebook entry that are directly pursuable in this session.

---

### Track 3 Startup — none

Track 3 has no startup ritual. It responds to Track 1 and 2 output at wrapup.

---

### Track 1 Wrapup — runs after any Track 1 work

1. **[REQUIRED]** Write lab notebook entry in `notebook/YYYY-MM-DD.md` — first person, covers what was investigated, what emerged, what questions opened. Update `notebook/README.md` index. Entry must be written even if the session felt inconclusive; inconclusive sessions often contain the most important observations.
2. Update any `research/laws/` or `research/hypotheses/` YAML files modified during the session.
3. Update `bibliography/deep-reads/` reading log if a deep read session occurred.

---

### Track 2 Wrapup — always runs last, enforces all other tracks

*The enforcer. Track 2 closes the session and verifies all active tracks completed their wrapup.*

1. Update `status.md` — dated entry, one-line summary, open items.
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
