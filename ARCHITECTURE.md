# Architecture — Humboldt

## Overview

Humboldt is a CLI research agent that runs locally. It is not a web service. It produces structured research artifacts (YAML law files, hypothesis notes, theory drafts) committed to git alongside the code.

Unlike c3po (which is a query-response system for human users), Humboldt is an investigator that runs multi-step research sessions, accumulates findings across sessions, and maintains a versioned inventory of its conclusions.

---

## System Components

### 1. `agent/retrieval.py` — Corpus Interface

Two retrieval modes, selectable by env var or CLI flag:

**Mode A: Direct Pinecone** (primary, default)
- Embeds queries with Voyage AI `voyage-3` (same model as c3po)
- Queries the `c3po` Pinecone index directly
- Full access to all namespaces: `pdfs`, `substack`, `videos`, `bibliography`, `discord`, `discord_links`, `sig`
- Namespace selection per query (e.g., prefer `pdfs` + `bibliography` for formal evidence)
- Returns ranked chunks with metadata (title, authors, type, source, url)

**Mode B: C3PO Worker API** (secondary)
- HTTP calls to `GET /search?q=<query>` on the deployed c3po worker
- Authenticated via `C3PO_MCP_KEY` header
- Returns pre-ranked results; no control over namespace weighting
- Useful as a fallback or for cross-checking retrieval quality

### 2. `agent/synthesizer.py` — Claude Interface

Wraps the Anthropic API for research synthesis tasks:

- **Hypothesis generation**: given a topic, propose candidate laws and sub-questions to investigate
- **Evidence analysis**: given retrieved chunks, extract relevant evidence and rate its quality
- **Law formulation**: draft a structured law statement with scope conditions and falsification criteria
- **Theory sketching**: given a set of laws, identify unification opportunities

Prompt caching enabled for SOUL.md (system prompt) and the static portions of research context. Streaming output for interactive sessions.

### 3. `agent/humboldt.py` — Research Session Orchestrator

CLI entry point:

```
python3 -m agent.humboldt investigate "<topic>"   # open-ended investigation
python3 -m agent.humboldt hypothesize "<topic>"   # generate candidate laws only
python3 -m agent.humboldt assess "L-001"          # gather evidence for a specific law
python3 -m agent.humboldt theorize                # scan inventory for unification opportunities
python3 -m agent.humboldt inventory               # display current law inventory
```

Session flow for `investigate`:
1. Load SOUL.md and existing inventory (for context)
2. Embed the topic → retrieve top-K corpus chunks across relevant namespaces
3. Claude synthesis pass: extract evidence, propose candidate laws
4. For each candidate: check against existing inventory (is this already captured?)
5. Generate YAML drafts for new candidates; update existing ones if new evidence found
6. Write session output to `data/sessions/YYYY-MM-DD-<slug>.md`
7. Print summary: new laws proposed, existing laws updated, key quotes

### 4. `research/` — Versioned Research Inventory

Git-tracked. Contains the accumulating output of all research sessions:

```
research/
├── laws/
│   ├── L-001-ossification.yaml
│   ├── L-002-hardness-asymmetry.yaml
│   └── ...
├── hypotheses/
│   ├── H-001-coordination-cost-conservation.yaml
│   └── ...
└── theories/
    ├── T-001-protocol-thermodynamics.md
    └── ...
```

Law files use the schema defined in SOUL.md. Hypothesis files are lighter:

```yaml
id: "H-001"
question: "Is coordination cost conserved across protocol transformations?"
motivation: >
  If true, this would explain why simplifying a protocol at one layer
  reliably increases complexity at an adjacent layer.
related_laws: [L-001, L-003]
retrieval_queries:
  - "coordination cost shifting protocol layers"
  - "complexity tradeoffs distributed systems"
  - "invisible burden protocol simplification"
status: active   # active | resolved | abandoned
notes: ""
opened: "2026-05-20"
```

---

## Data Flow

```
CLI invocation
    │
    ▼
humboldt.py: load SOUL + inventory
    │
    ▼
retrieval.py: embed topic → Pinecone query
    │         (voyage-3, top-15 per namespace, merge + rerank)
    ▼
ranked corpus chunks (with metadata)
    │
    ▼
synthesizer.py: Claude analysis
    │   System: SOUL.md (cached) + inventory snapshot
    │   User: retrieved chunks + research task
    ▼
structured output: law candidates, evidence excerpts, connections
    │
    ▼
humboldt.py: write/update YAML files
    │         write session log
    ▼
git add research/ && git commit
```

---

## Retrieval Strategy

Humboldt uses a layered retrieval strategy that differs from c3po's user-query approach:

| Query type | Namespaces | Top-K | Notes |
|------------|-----------|-------|-------|
| Evidence for a law | `pdfs`, `bibliography` | 12 each | Formal academic sources only |
| Domain examples | all namespaces | 8 each | Cast wide; filter in synthesis |
| Counter-evidence | all namespaces | 10 each | Explicit adversarial framing |
| Related laws | `pdfs`, `substack`, `sig` | 8 each | Community discussion often names patterns |

The synthesis pass uses Claude to evaluate retrieval quality and flag when the corpus is thin. Thin coverage triggers a note in the law file: "corpus coverage limited — extrapolation required."

---

## Connection to C3PO

Humboldt is a sibling project to c3po, not a fork:

| | C3PO | Humboldt |
|-|------|---------|
| User | Human researchers via web UI | Autonomous agent (no human in the loop per session) |
| Task | Answer questions about protocols | Discover laws of protocolized systems |
| Output | Conversational response + citations | Structured YAML law inventory + theory drafts |
| Corpus access | Own query path | Shared Pinecone index (direct) or c3po API |
| Persona | Reference librarian | Naturalist investigator |
| Deployment | Cloudflare Worker | Local CLI |

The shared Pinecone index means Humboldt benefits immediately from every new corpus ingestion done by c3po (Discord sync, new PDFs, Substack updates).

---

## Security

Keys follow the Protocol Institute security policy (`../admin/security.md`):
- All secrets in `.env` (gitignored, Dropbox-ignored)
- Values sourced from `../protocol-institute/.env.keys`
- Keys registered in `../admin/keys.md`
- No secrets in code, config files, or logs

Humboldt reuses the existing c3po keys (VOYAGE, PINECONE, ANTHROPIC) — no new key provisioning required for Phase 1.
