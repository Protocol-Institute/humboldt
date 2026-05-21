# Humboldt Dev Log — Track 2

Development log for Humboldt's persona, methodology, and infrastructure. Covers Track 2 (persona evolution) and Track 3 (artificial researcher template) work. Research activity is tracked separately in `notebook/`.

Most recent entry first.

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
