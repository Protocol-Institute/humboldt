# Developer TODO — Tracks 2 and 3

Infrastructure, persona, and template work. This is the *operator* layer — managing Humboldt as a project. Humboldt's own research agenda is in `research/agenda.md`.

Priority: **[H]** urgent, **[M]** soon, **[L]** when convenient.

---

## Track 2 — Persona and Infrastructure

### Immediate

- **[H]** Build Discord presence mechanism for the #new-nature channel. Humboldt should be able to read and post to that channel as part of its research activity. Design questions to resolve: (1) auth/bot setup; (2) participation policy — when does Humboldt post proactively vs. respond? (3) how do Discord inputs flow into the research inventory? (4) what does "Humboldt's lab" look like in practice?
- **[H]** Fix SOUL.md corpus-boundary problem: Humboldt's epistemic boundary is *evidence quality*, not corpus membership. It must reason from general knowledge when the corpus is silent, marking provenance explicitly. Writing "NOT IN CORPUS" as a research result is a design flaw inherited from c3po.
- **[H]** Create `METHOD.md` — extract investigative methodology from SOUL.md. SOUL = who Humboldt is; METHOD = how it approaches research; `methods/` = specific named procedures.

### Near-term

- **[M]** Update SOUL.md "Current Research State" section to be kept fresh at session start — this section should reflect the live inventory, not the founding state.
- **[L]** Implement periodic literature survey mechanism — a scheduled investigative move triggered by the current inventory state, not by external input. Design this as a new technique (M-004?) or as a variant of M-002 Domain Rotation.

---

## Track 3 — Artificial Researcher Template

### Immediate

- **[M]** Copy M-001, M-002, M-003 from `methods/` to `_template/methods/` in generic form — strip Protocol Institute specifics, add parameterization notes.
- **[M]** Write `_template/CLAUDE-template.md` — generic Claude Code setup for artificial researcher projects.

### Near-term

- **[L]** Review `_template/` after 2–3 more full research sessions — see what else generalizes from practice vs. what is Protocol Institute-specific.
- **[L]** Assess readiness to extract as a separate repo. Threshold: mandatory patterns all covered, used implicitly for 5+ sessions, reviewed by at least one other person.
