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

## At Session Start

1. Read `status.md` — review the last entry for open questions and where the previous session ended.
2. Check `research/laws/` — count current laws by confidence level.
3. Note any hypotheses marked `status: active` that are ready for investigation.

---

## After Each Session

**Documentation (always):**
1. `status.md` — add a dated log entry with PT start–end times and a one-line summary.
2. `CLAUDE.md` — update namespace vector counts if the c3po index has grown since last session.

**Research artifacts:**
3. `git add research/` — commit updated laws, hypotheses, theories.
4. `data/sessions/` is gitignored — session logs stay local.

**Keys/env (if changed):**
5. New env vars: update `.env.template`; add to `../.env.keys`; add a row to `../admin/keys.md`.

**Repo:**
6. `git commit` and `git push`.

**Memory:**
7. Update Claude memory (`/Users/Venkat/.claude/projects/.../memory/`) — save anything non-obvious about research findings or pipeline decisions.
