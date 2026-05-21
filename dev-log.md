# Humboldt Dev Log — Track 2

Development log for Humboldt's persona, methodology, and infrastructure. Covers Track 2 (persona evolution) and Track 3 (artificial researcher template) work. Research activity is tracked separately in `notebook/`.

Most recent entry first.

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
