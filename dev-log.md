# Humboldt Dev Log — Track 2

Development log for Humboldt's persona, methodology, and infrastructure. Covers Track 2 (persona evolution) and Track 3 (artificial researcher template) work. Research activity is tracked separately in `notebook/`.

Most recent entry first.

---

## 2026-05-21 — Architecture redesign: from RAG persona to researcher OS

### The core problem resolved

The inherited SOUL.md architecture was built for c3po — a corpus assistant whose identity is defined by the corpus it inhabits and reports from. Humboldt is fundamentally different: defined by interests and skills, not by what it knows; self-directed rather than query-driven; building its own original research inventory rather than synthesizing the corpus for users. The SOUL.md pattern could not accommodate a behavioral loop where Humboldt reviews its own state and decides what to do next.

The fix required a full architecture replacement, not a patch.

### New persona architecture

**Retired:** `SOUL.md` (archived, preserved for reference)

**Replaced by:**

| Document | Purpose |
|----------|---------|
| `IDENTITY.md` | Short stable kernel: lineage telos, mission, intellectual temperament, voice |
| `LINEAGE.md` | Append-only earned lineage: grows from deep reads and established laws only |
| `MEMORY.md` | Narrative memory: how Humboldt tells itself the story of its development |
| `METHOD.md` | Epistemic standards: provenance marking, confidence levels, falsification |
| `BOOTSTRAP.md` | Wakeup sequence and Decide-phase configuration |
| `methods/M-000-ooda.md` | The OS kernel: OODA decision gate |

The key architectural insight: LINEAGE.md and MEMORY.md start nearly empty and grow slowly through research activity. Declared identity is replaced by earned identity. LINEAGE gets one entry per completed deep read and one per law promoted to `established`. MEMORY gets an entry when something significantly shifts. Both are permanent and append-only.

### Dynamic context assembly

`agent/prompts.py` now assembles the system prompt from multiple sources rather than loading a single static SOUL.md. The assembled context includes: IDENTITY + LINEAGE + MEMORY + METHOD + BOOTSTRAP + research state (loaded from research/ at runtime) + methods index (one line per M-NNN) + inbox contents + recent notebook thread. `load_soul()` is a backward-compatible wrapper around `assemble_context()`.

### Behavior stub inventory

Twelve new method stubs written (M-000 through M-015, excluding gaps):

- **M-000** — OODA meta-loop (the kernel)
- **M-004** — Reading prioritization
- **M-005** — Explore-exploit
- **M-006** — Research conversations
- **M-007** — Field trip
- **M-008** — Bullshit detector
- **M-009** — Visual thinking
- **M-010** — Fermi estimation
- **M-011** — Dyson design
- **M-012** — Thought experiments
- **M-013** — Design fictions
- **M-014** — Cross-training
- **M-015** — Stress-relax

The stubs range from immediately usable (M-010 Fermi, M-012 Thought Experiments) to requiring significant adaptation for a digital researcher (M-015 Stress-Relax, M-014 Cross-Training). The OODA stub reflects the operator's specific understanding: Orient is expensive and should only be triggered when the environment has genuinely shifted; routine sessions run as O_DA.

### Library restructure and deep-read wiring

`bibliography/` restructured:
- `bibliography/deep-reads/` — PDF source documents only
- `bibliography/notes/` — reading notes (was `bibliography/deep-reads/*.md`)

`simon_sciences.pdf` moved to `bibliography/deep-reads/simon-sciences-of-artificial.pdf`.
`simon-sciences-of-artificial.md` moved to `bibliography/notes/`.

New CLI commands: `humboldt library` (list documents) and `humboldt deepread "<name>" ["<pages>"]` (read actual PDF via pypdf, write notes to bibliography/notes/).

Critical rule enforced in M-003 and CLAUDE.md: deep reads must always use the actual PDF. Never from training knowledge. A background agent was dispatched to continue the Simon read this session and produced plausible-sounding output from training memory — it was discarded. The rule now has a concrete failure case to point to.

### Inbox

`inbox/` created. The operator drops files here; Humboldt reads them as part of the BOOTSTRAP wakeup sequence. Text and markdown files are inlined into the assembled context; PDFs and large files are listed with a pointer. `inbox/processed/` is where Humboldt moves items after acting on them.

Telegram bot integration (pointing to the existing vgr-library-code infrastructure) is the planned next step for async inbox delivery.

### Hamming PDF acquired

`hamming_you_and_your_research.pdf` downloaded to library. Reading prioritization (M-004) should evaluate it against active hypotheses before Humboldt decides when to engage it. Short document — likely a shallow-mode read alongside a primary investigation session.

### Track 3: template status

The new architecture (IDENTITY/METHOD/BOOTSTRAP/LINEAGE/MEMORY) is itself the core generalization that `_template/` should capture. The existing `SOUL-template.md` and `METHOD-template.md` are now outdated. Updating `_template/` to reflect the new architecture is the next Track 3 priority.

### Open issues

| Priority | Issue |
|----------|-------|
| High | Simon deep read: continue from p.61 using actual PDF |
| High | H-001 (Coordination Cost Conservation): over-aged, needs first retrieval run |
| High | `_template/` update: SOUL-template.md superseded; new architecture templates needed |
| Medium | Discord presence mechanism: still undesigned at implementation level |
| Medium | Telegram inbox integration: wire vgr-library-code bot to write to `inbox/` |

---

## 2026-05-20 (session 2) — Public launch + ritual definition

**Session goals:** complete project housekeeping; publish the project; define operational structure.

### Publication
- Repo made public (`Protocol-Institute/humboldt`)
- Org README (`.github/profile/README.md`) updated — Humboldt listed with description and notebook link
- PI website: `humboldt.html` (project page), `humboldt-notebook.html` (lab notebook, first entry), `projects.html` (Initiatives listing entry with both links)
- Terminology sweep across all files: "artificial researcher" replaces "research agent" / "autonomous agent" everywhere. Key distinction: Humboldt is driven by its own research interests, not by user requests.

### Three-track structure
- Track 1 (Humboldt's research), Track 2 (operator/persona), Track 3 (template) formally defined
- `notebook/` created with first entry (2026-05-20.md) — first person, Track 1 wrapup artifact
- `dev-log.md` created (this file) — Track 2 wrapup artifact
- `_template/` created — Track 3 primary artifact, v0.1

### Session rituals
- Full ritual spec written into CLAUDE.md — startup and wrapup for all three tracks
- Track 2 is enforcer: must produce wrapup checklist report before session closes
- `[REQUIRED]` designation for non-skippable items: lab notebook entry (T1) and dev-log entry (T2)

### To-do structure
- `research/agenda.md` — Humboldt's own queue, first person, lives in `research/` as a research artifact, updated at T1 wrapup [REQUIRED]
- `TODO.md` — operator queue, T2 and T3 only; Humboldt's layer cleanly separated

### Open issues updated
- Discord presence mechanism elevated to highest T2 priority
- SOUL.md corpus-boundary fix and METHOD.md creation remain high priority

---

## Open Issues (Track 2)

| Priority | Issue | Notes |
|----------|-------|-------|
| High | Discord presence mechanism for #new-nature channel | Auth, participation policy, input→inventory flow — see TODO.md |
| High | Fix SOUL.md corpus-boundary problem | Humboldt must reason from general knowledge freely; "NOT IN CORPUS" is never a research result |
| High | Create METHOD.md | SOUL = who; METHOD = how; methods/ = specific procedures |
| Medium | Update SOUL.md "Current Research State" section | Keep live at session start/end |
| Low | Periodic literature survey mechanism | Scheduled investigative move from current inventory state |

## Open Issues (Track 3)

| Priority | Issue | Notes |
|----------|-------|-------|
| Medium | Copy M-001, M-002, M-003 to `_template/methods/` in generic form | Strip PI specifics; add parameterization notes |
| Medium | Write `_template/CLAUDE-template.md` | Generic Claude Code setup for AR projects |
| Low | Extract as separate repo when stable | After 5+ sessions and external review |

---

## 2026-05-20 — Project initialized + methodology scaffolding

**Session goals:** seed the project; design the research persona; define core techniques; begin first deep read.

### Infrastructure
- Created GitHub repo `Protocol-Institute/humboldt` (private, will go public)
- Scaffolded full directory structure, core documentation files, agent code skeleton
- Registered in `../admin/keys.md` (reuses c3po keys — no new provisioning)
- Full pipeline validated: Voyage embed → Pinecone retrieval → Claude synthesis

### Persona design
- Defined SOUL.md — first version based on c3po's style template, adapted for researcher role
- Identified key design tensions (see `persona_design_notes.md`):
  - **Corpus boundary problem:** agent writes "NOT IN CORPUS" instead of reasoning from general knowledge. SOUL.md inherited this from c3po. Must be fixed — Humboldt's epistemic boundary should be evidence quality, not corpus membership.
  - **Identity vs. method separation:** SOUL.md conflates who Humboldt is with how it does research. These should be separated: SOUL = identity/voice/goals; METHOD = investigative approach; `methods/` = specific procedures.
  - **Input mechanism design:** defined four input types for how Humboldt finds new material (lit surveys, researcher discourse, own past records, proactive tips from collaborators)

### Technique inventory (methods/)
- **M-001 (Random Links):** generative; force structural connection between two disparate inputs → candidate law. Worked example: coal mines + blockchain → H-002.
- **M-002 (Canonical Domains):** dual-use; maintain five home domains as analogy reservoirs and stress-test beds. Canonical domain set in `canonical-domains.yaml`.
- **M-003 (Deep Read):** analytical; fully internalize a foundational text over multiple sessions. First text: Simon's *Sciences of the Artificial*.

### Three-track structure defined
- Track 1 (Research): notebook + research inventory
- Track 2 (Persona): dev-log + SOUL + CLAUDE + methodology artifacts
- Track 3 (Template): `_template/` folder for artificial researcher pattern

---

## Open Issues (Track 2)

| Priority | Issue | Notes |
|----------|-------|-------|
| High | Fix SOUL.md corpus-boundary problem | Humboldt must use general knowledge freely, marking provenance; never write "NOT IN CORPUS" |
| High | Create METHOD.md | Separate investigative methodology from persona identity |
| Medium | Update SOUL.md to reference methods/ inventory | SOUL = who; METHOD = how; methods/ = specific procedures |
| Medium | Design Discord integration | "new-nature" channel as Humboldt's lab; participation policy; bot component |
| Low | Implement periodic survey mechanism | Theory-driven retrieval from current inventory state |

## Open Issues (Track 3)

| Priority | Issue | Notes |
|----------|-------|-------|
| Medium | Review `_template/` and extract generalized patterns | Initial scaffold done; needs review after a few more Track 1 sessions to see what generalizes |
| Low | Consider extracting template as a separate repo | Premature until the pattern is stable after 3+ research sessions |
