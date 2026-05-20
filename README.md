# Humboldt

An autonomous research agent investigating the **new nature** — laws of artificial and protocolized systems that are nearly as inviolable as those of the physical world.

Named for Alexander von Humboldt (1769–1859), the naturalist who sought to discover the underlying unity and lawfulness of all natural phenomena. Where Humboldt mapped the laws of climate, altitude, and life across continents, this agent maps the structural regularities that govern protocols, coordination mechanisms, and artificial order at every scale.

---

## The Research Program

Protocols and protocolized systems — from TCP/IP to parliamentary procedure, from financial settlement to social media feed algorithms — are not arbitrary. They exhibit deep structural regularities: tendencies, constraints, and failure modes that recur across domains and levels of formalization. Some of these regularities are strong enough to be called laws.

**New nature** is the study of these laws. It asks:

- What patterns recur across radically different protocolized systems?
- Which of these patterns are structural necessities, and which are contingent design choices?
- Are there unified principles that explain why protocols harden, fail, ossify, adapt, or proliferate?
- What is the protocol-theoretic analog of thermodynamics, or of natural selection?

Humboldt investigates these questions by:

1. **Querying the Protocol Institute's research corpus** (via the c3po index) for evidence, examples, and prior theorization
2. **Generating and stress-testing hypotheses** about candidate laws
3. **Building a structured inventory** of proposed laws with evidence, counterexamples, and confidence levels
4. **Seeking unifying theories** that subsume multiple candidate laws under a common framework

---

## Corpus

Humboldt draws on the Protocol Institute's research library via the c3po Pinecone index — approximately 19,700+ embeddings spanning:

| Namespace | Contents |
|-----------|----------|
| `pdfs` | ~82 academic papers and working papers from the Summer of Protocols |
| `substack` | ~200 issues of Protocolized magazine |
| `videos` | Talks, lectures, and presentations |
| `bibliography` | Curated references |
| `discord` + `discord_links` | Protocol Institute community discourse |
| `sig` | Special Interest Group discussions |

Direct Pinecone access (primary) and c3po Worker API (secondary) are both supported.

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│  RESEARCH AGENT (humboldt.py)                                        │
│                                                                      │
│  topic / hypothesis ──► retrieval.py ──► c3po Pinecone index        │
│                              │         (voyage-3 embeddings)         │
│                              ▼                                       │
│                       ranked corpus excerpts                         │
│                              │                                       │
│                              ▼                                       │
│                     synthesizer.py ──► Claude (Sonnet)               │
│                              │         with SOUL.md persona          │
│                              ▼                                       │
│                      research output:                                │
│                        - structured law candidates (YAML)            │
│                        - evidence summaries                          │
│                        - cross-law connections                       │
│                        - unified theory sketches                     │
└──────────────────────────────────────────────────────────────────────┘
                              │
                  research/ inventory (git-tracked)
                    laws/        — candidate laws with evidence
                    hypotheses/  — active research questions
                    theories/    — unified theory development
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.14 (`/opt/homebrew/bin/python3`) |
| Embeddings | Voyage AI `voyage-3` (shared with c3po) |
| Vector DB | Pinecone `c3po` index (shared with c3po) |
| LLM | Claude Sonnet 4.6 via Anthropic API |
| Output format | YAML (human-readable, git-diffable) |
| Interface | CLI (`python3 -m agent.humboldt`) |

---

## Development Setup

```bash
/opt/homebrew/bin/python3 -m venv .venv
source .venv/bin/activate
pip install voyageai pinecone-client anthropic python-dotenv pyyaml rich

cp .env.template .env
# Fill values from ../protocol-institute/.env.keys
xattr -w com.dropbox.ignored 1 .env
```

---

## Project Status

See `status.md` for the activity log.
