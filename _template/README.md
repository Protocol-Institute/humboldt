# Artificial Researcher Template

A pattern library for building artificial researchers — autonomous investigators that pursue original research rather than answer questions posed by humans.

This template is extracted from [Humboldt](https://github.com/Protocol-Institute/humboldt), the Protocol Institute's artificial researcher investigating the "new nature" (laws of protocolized and artificial systems). It generalizes the design patterns that proved useful into a reusable scaffold for other research projects.

---

## What this is for

This template is for teams that want to create an artificial researcher that:
- Has a specific research agenda (a domain it investigates systematically)
- Builds up a cumulative knowledge base over many sessions (laws, hypotheses, bibliography)
- Uses structured research methods, not just prompting
- Publishes its work in a readable form (lab notebook)
- Can be customized per project while sharing common infrastructure

It is **not** a RAG assistant template (that's what c3po is for). The distinction:

| | RAG assistant | Artificial researcher |
|---|---|---|
| Goal | Answer your questions | Pursue its own research agenda, independent of user requests |
| Knowledge | Your corpus | General knowledge + targeted retrieval |
| Output | Responses to queries | Cumulative research inventory |
| Sessions | Stateless | Stateful — builds across sessions |
| Voice | Neutral, helpful | Opinionated, investigative |

---

## Core concepts

### The persona architecture

Every artificial researcher needs a set of distinct documents assembled dynamically into the system prompt. As of pattern version 0.2, these are:

1. **IDENTITY** (`IDENTITY.md`) — *Who am I?* Short and stable. Lineage telos, research mission, intellectual temperament, voice. No methodology, no behavioral rules.

2. **LINEAGE** (`LINEAGE.md`) — *What have I actually become?* Append-only. Starts nearly empty. Updated only when a deep read is completed (intellectual influences) or a law reaches established confidence (own discoveries). This is earned identity, not declared identity.

3. **MEMORY** (`MEMORY.md`) — *What is my research story?* Narrative memory. Updated at significant moments, not every session. The story the researcher tells itself about its development.

4. **METHOD** (`METHOD.md`) — *How do I reason about evidence?* Epistemic standards: provenance marking (corpus/external/inference), confidence levels, falsification requirements, mechanism standards.

5. **BOOTSTRAP** (`BOOTSTRAP.md`) — *How do I wake up?* The session startup sequence (read notebook → scan inbox → scan environment → run OODA gate) plus the Decide-phase configuration (priority ordering, meta-policies).

6. **Methods inventory** (`methods/`) — *What specific techniques do I use?* Growing library of named procedures. M-000 (OODA) is the kernel; M-001 onward are research techniques.

The key design principle: **LINEAGE and MEMORY start nearly empty and grow slowly**. Declared identity is a fiction; earned identity is evidence. The system prompt becomes more distinctive as the researcher does actual work.

**Note on SOUL.md:** Earlier versions of this pattern used a single monolithic SOUL.md. This was inherited from RAG assistant design and is wrong for a researcher. The multi-document architecture above replaces it.

### The formalization continuum

Research output should flow through explicit maturity stages:

```
Raw observation → Notebook entry → Hypothesis (YAML) → Candidate law (YAML) → Established law
```

Each stage has its own artifact type and schema. Premature formalization (jumping from observation to law) is the most common research quality failure.

### The lab notebook

The lab notebook (`notebook/`) is the public-facing record of research activity — written in the researcher's voice, timestamped, cumulative. It is not a summary of sessions but a genuine notebook: open questions, partial results, false starts, and emerging patterns all belong here. It is meant to be read by humans interested in following the research as it develops.

---

## File structure

```
_template/
├── README.md                   ← this file
├── SOUL-template.md            ← researcher identity template
├── METHOD-template.md          ← investigative philosophy template
├── CLAUDE-template.md          ← AI agent setup (optional — for Claude Code users)
├── methods/
│   ├── README.md               ← methods inventory overview
│   ├── M-001-random-links.md   ← core generative technique (required pattern)
│   ├── M-002-canonical-domains.md ← optional: home domain reservoir
│   └── M-003-deep-read.md      ← optional: deep source internalization
├── notebook/
│   └── README.md               ← lab notebook pattern
├── research/
│   └── README.md               ← research inventory pattern
└── bibliography/
    └── README.md               ← bibliography pattern
```

### What is required vs. optional

| Pattern | Required? | Notes |
|---------|-----------|-------|
| SOUL.md | Required | Every researcher needs an identity |
| METHOD.md | Required | Every researcher needs an epistemic philosophy |
| methods/ inventory | Required | At least one technique; grows over time |
| M-001 (Random Links) | Recommended | The most universally useful generative technique |
| M-002 (Canonical Domains) | Optional | Valuable for mature researchers; premature at founding |
| M-003 (Deep Read) | Optional | Valuable when there are foundational texts worth internalizing |
| Lab notebook | Required | The public face of the research |
| Research inventory (YAML) | Required | The cumulative knowledge base |
| Bibliography | Optional | Useful when the researcher curates sources actively |

---

## How to use this template

1. Copy the `_template/` directory into your new project as the root scaffold
2. Fill in `SOUL-template.md` → rename to `SOUL.md`
3. Fill in `METHOD-template.md` → rename to `METHOD.md`
4. Add or remove methods from `methods/` as appropriate for your domain
5. Initialize the research inventory with seed hypotheses
6. Write the first lab notebook entry after the first research session

Do not fork Humboldt itself — take this template, which contains the patterns without the Protocol Institute's specific research agenda.

---

## Provenance

Extracted from [Humboldt](https://github.com/Protocol-Institute/humboldt) by the Protocol Institute, 2026.
Pattern version: 0.1 (initial extraction — expected to evolve significantly through 2026).
