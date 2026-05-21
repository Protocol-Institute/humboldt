# Humboldt

An autonomous research agent investigating the **new nature** — laws of artificial and protocolized systems that are nearly as inviolable as those of the physical world.

Named for Alexander von Humboldt (1769–1859), the naturalist who sought the underlying unity and lawfulness of all natural phenomena. Where Humboldt mapped the laws of climate, altitude, and life across continents, this agent maps the structural regularities that govern protocols, coordination mechanisms, and artificial order at every scale.

---

## Follow the research

**[Lab Notebook →](notebook/)** — Humboldt's field notes, updated after each research session. Written in first person. A record of what was investigated, what emerged, and what questions remain open.

The most recent entry: **[2026-05-20](notebook/2026-05-20.md)** — First investigations; Trust Ratchet hypothesis emerged; Simon deep read begun.

---

## The Research Program

Protocols and protocolized systems — from TCP/IP to parliamentary procedure, from financial settlement to social media algorithms — are not arbitrary. They exhibit deep structural regularities: tendencies, constraints, and failure modes that recur across domains and levels of formalization. Some of these regularities are strong enough to be called laws.

**New nature** is the study of these laws. It asks:

- What patterns recur across radically different protocolized systems?
- Which of these patterns are structural necessities, and which are contingent design choices?
- Are there unified principles that explain why protocols harden, fail, ossify, adapt, or proliferate?
- What is the protocol-theoretic analog of thermodynamics, or of natural selection?

---

## Current Research Inventory

| Type | Count | Examples |
|------|-------|---------|
| Candidate laws | 5 | L-001 (Ossification), L-002 (Hardness Asymmetry), L-004 (Metric Capture) |
| Active hypotheses | 2 | H-001 (Coordination Cost Conservation), H-002 (Trust Ratchet) |
| Techniques | 3 | M-001 (Random Links), M-002 (Canonical Domains), M-003 (Deep Read) |
| Deep reads | 1 in progress | Simon, *The Sciences of the Artificial* (1996) |

Full inventory: [`research/laws/`](research/laws/), [`research/hypotheses/`](research/hypotheses/)

---

## Project Structure

This project has three parallel tracks:

**Track 1 — Research:** Humboldt's original research work. Primary artifacts: lab notebook, research inventory (laws + hypotheses), bibliography, methods.

**Track 2 — Persona development:** Evolving the research agent's identity, methodology, and infrastructure. Primary artifacts: `SOUL.md`, `METHOD.md`, `dev-log.md`, `CLAUDE.md`, `ARCHITECTURE.md`.

**Track 3 — Artificial Researcher Template:** A generalized pattern library for building autonomous research agents, extracted from this project. Primary artifact: [`_template/`](_template/) — designed for eventual forking by other research projects.

```
humboldt/
├── notebook/          Track 1: Lab notebook (published, first-person)
├── research/          Track 1: Laws, hypotheses, theories (YAML + markdown)
│   ├── laws/
│   ├── hypotheses/
│   └── theories/
├── bibliography/      Track 1: Curated references and deep-read entries
│   └── deep-reads/
├── methods/           Track 1+2: Technique inventory
├── agent/             Track 2: Python agent code
├── SOUL.md            Track 2: Researcher identity and agenda
├── ARCHITECTURE.md    Track 2: System design
├── ROADMAP.md         Track 2: Phase plan
├── dev-log.md         Track 2: Development and persona evolution log
└── _template/         Track 3: Artificial researcher pattern library
```

---

## Corpus

Humboldt draws on the Protocol Institute's research library via the c3po Pinecone index — approximately 19,700+ embeddings spanning:

| Namespace | Contents |
|-----------|----------|
| `pdfs` | ~82 academic papers from the Summer of Protocols |
| `substack` | ~200 issues of Protocolized magazine |
| `videos` | Talks, lectures, and presentations |
| `bibliography` | Curated references |
| `discord` + `discord_links` | Protocol Institute community discourse |
| `sig` | Special Interest Group discussions |

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.14 |
| Embeddings | Voyage AI `voyage-3` (shared with c3po) |
| Vector DB | Pinecone `c3po` index (shared with c3po) |
| LLM | Claude Sonnet 4.6 via Anthropic API |
| Interface | CLI (`python3 -m agent.humboldt`) |

---

## Development Setup

```bash
/opt/homebrew/bin/python3 -m venv .venv
source .venv/bin/activate
pip install voyageai pinecone anthropic python-dotenv pyyaml rich

cp .env.template .env
# Fill values from ../protocol-institute/.env.keys
xattr -w com.dropbox.ignored 1 .env
```

---

## Relationship to c3po

[C3PO](https://github.com/Protocol-Institute/c3po) is a RAG research *assistant* — it answers your questions using the Protocol Institute corpus. Humboldt is a research *agent* — it pursues its own research agenda using that same corpus as one of several resources. C3PO is stateless; Humboldt is cumulative. They share a Pinecone index but have different purposes.

---

## The Artificial Researcher Template

The patterns developed here — the three-layer SOUL/METHOD/methods architecture, the formalization continuum, the lab notebook, the methods inventory — are being extracted into a reusable template in [`_template/`](_template/). The goal is to make it possible for other projects to fork this pattern and build their own autonomous research agents without starting from scratch.

The template is in early development (v0.1). It will stabilize after a few more research sessions.

---

*Project status: [`status.md`](status.md) — [`dev-log.md`](dev-log.md)*
