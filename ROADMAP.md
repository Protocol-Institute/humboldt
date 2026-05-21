# Roadmap — Humboldt

## Phase 1 — Core Research Loop (current)

**Goal:** Working CLI tool that enables Humboldt to investigate a topic, retrieve corpus evidence, and produce structured law candidates.

- [ ] `agent/retrieval.py` — Voyage embed + Pinecone query, Mode A (direct)
- [ ] `agent/synthesizer.py` — Claude Sonnet integration with prompt caching
- [ ] `agent/prompts.py` — SOUL.md loading, research task templates
- [ ] `agent/humboldt.py` — CLI orchestrator: `investigate`, `inventory` subcommands
- [ ] Seed inventory: manually draft 3–5 law candidates to populate `research/laws/` and validate schema
- [ ] Validate retrieval quality: do the corpus chunks Humboldt retrieves actually bear on the proposed laws?
- [ ] `status.md` entries after each research session

**Success criterion:** Run `python3 -m agent.humboldt investigate "protocol ossification"` and get at least one well-formed law YAML with substantive corpus evidence.

---

## Phase 2 — Full Investigative Toolkit

**Goal:** Complete subcommand suite; richer research outputs.

- [ ] `assess` subcommand — focus a session on gathering evidence for/against a specific law
- [ ] `hypothesize` subcommand — generate candidate laws without committing to files
- [ ] `theorize` subcommand — load full inventory, ask Claude to find unification opportunities
- [ ] Counter-evidence retrieval — explicit adversarial queries to stress-test laws
- [ ] Cross-law relation tracking — update `related_laws` across files automatically
- [ ] Confidence scoring — Claude rates evidence quality; updates `confidence` field
- [ ] Mode B retrieval — c3po Worker API as fallback (add `C3PO_WORKER_URL` support)

---

## Phase 3 — Research Journal and Theory Development

**Goal:** Humboldt produces longer-form research outputs and tracks its investigation history.

- [ ] `data/sessions/` summaries as human-readable session journals
- [ ] `theorize` produces structured theory drafts in `research/theories/`
- [ ] Theory files link to supporting laws and flag missing evidence
- [ ] "Open questions" section: laws with thin corpus coverage, flagged for human follow-up
- [ ] Monthly digest: auto-generate a summary of new laws, confidence changes, active theories

---

## Phase 4 — External Corpus Extension

**Goal:** Humboldt can ingest targeted external sources beyond the c3po corpus.

- [ ] `ingest/` pipeline — given a URL or PDF, embed and add to a `humboldt` namespace in Pinecone
- [ ] External laws literature: existing named laws (Goodhart, Gall, Conway, etc.) formally ingested
- [ ] Cross-domain databases: Wikipedia "list of eponymous laws", academic encyclopedias of coordination theory
- [ ] On-demand web fetch: when corpus is thin, Humboldt can fetch a specific URL for synthesis context (not indexed — ephemeral)

---

## Phase 5 — Publication and Sharing

**Goal:** Humboldt's inventory is legible and shareable.

- [ ] `render/` — convert YAML inventory to human-readable formats (Markdown, HTML)
- [ ] Law inventory as a public-facing artifact on protocolized.io (if PI approves)
- [ ] API endpoint — expose law inventory as a structured data feed for other PI tools
- [ ] Possible: Humboldt as a context provider for c3po (c3po can cite Humboldt's laws when answering user questions)
