# Research Agenda

*Humboldt's own queue of next research tasks. Updated at wrapup after Track 1 sessions.*

*Arc position is read from phase tempo, not elapsed time or session count. The right
question at session start is not "what's been waiting longest?" but "what's nearest to
a natural phase transition?" Each bucket below reflects a phase-position diagnosis,
updated at session wrapup. See `bibliography/notes/rao-tempo.md` §M-017 for the
phase vocabulary and tempo signatures.*

---

## Current state — 2026-08-17 (session 30)

> **Note:** the buckets below still use the pre-redesign vocabulary (T-/DS-/CL- ids).
> The live artifacts are now `laws/L-NNN-*.yaml`. Reconciling this file to the law
> records is an open task — see `TODO.md`. The block here is the accurate near-term queue.

**Blocked until 2026-09-01 — corpus reads offline.** Pinecone's monthly egress quota is
exhausted; `assess` refuses to run rather than verdict on an empty evidence slot (see
`plans/read-outage-2026-08.md`). Anything requiring retrieval waits. Induction is
unaffected and continues.

**Awaiting supervisor review — 5 new laws from the 2026-08-17 induction sweep:**
- **L-012** Intervention-Layer Displacement in Automated Decision Protocols
- **L-013** Paradigm-Locked Anomaly Tolerance in Protocol Systems
- **L-014** Strategic Boundary Concentration Under Computable Legality
- **L-015** Interpretive Continuity Decay in Distributed Governance Protocols
- **L-016** Normative Intervention Algorithmic Retraining Effect

All five are exploration/speculative with model-drafted triggers. Same review shape as
L-008–011 got in session 28: check the statement doesn't overclaim its seed, hand-set the
advance/challenge triggers, and give each an executable gap in `open_questions`.

**Open counterexample to chase:** the sweep attached a counterexample to **L-001**
(whether ossification is a necessary consequence of formalization). L-001 is at
heavy-lift/supported — a live counterexample there matters more than five new
exploration-stage laws. Assess it first when reads return.

**Also queued:** L-008 gained two further examples, L-002/L-003/L-004/L-011 one each,
L-006 and L-007 a reference each.

---

## Heavy Lift Ready
*Valley exhausted — synthesis committed; writing the publishable artifact toward the
separation event. A separation event requires a published artifact available for
external review, critique, and falsification attempts.*

- **T-001** (Ossification) — formulation complete, domains documented. Needs a publishable artifact.
- **T-002** (Hardness Asymmetry) — formulation complete. Needs a publishable artifact.
- **T-003** (Goodhart, imported) — protocol-theoretic formulation ready; DS-004 valley work continues in parallel.
- **T-004** (Gall, imported) — protocol-theoretic formulation ready; DS-005 valley work continues in parallel.

---

## Valley — stagnant / behavior-blocked
*No movement even with attention. Diagnose before proceeding: (a) needs a targeted
investigation session, or (b) a behavior stub is blocking the next phase move?
Note diagnosis in the project file and here.*

- **DS-007 / CL-003 (Trust Ratchet)** — `research/ds/DS-007-trust-ratchet.md`
  Diagnosis: not behavior-blocked — needs deliberate investigation session. The
  near-miss category and the F-001 ↔ CL-003 interaction are the two unresolved threads.
  Transition trigger: near-miss data tested; compounding-resistance mechanism examined.

---

## Valley — productive
*Grinding with diminishing but nonzero returns. This is the correct tempo for this
phase. Do not accelerate; do not confuse slow progress with stagnation. The valley
cannot be shortened without compromising the separation event.*

- **DS-006 / CL-002 (Coordination Cost Conservation)** — `research/ds/DS-006-coordination-cost-conservation.md`
  Crux: automation question — does machine coordination cost count as "coordination
  cost" for the purposes of the conservation claim? Simon's near-decomposability
  framework may reframe before it resolves.
  Transition trigger: automation question resolved in either direction — either a
  principled argument that machine coordination cost counts (conservation holds) or a
  documented case of genuine elimination via automation (conservation fails or needs
  scoping). Either closes the valley and opens the heavy lift.

- **DS-003 / CL-001 (Formalization Ratchet)** — `research/ds/DS-003-formalization-ratchet.md`
  Status: candidate confidence; falsification conditions not fully tested. The
  internally-developed vs. externally-imposed distinction surfaced in counterexamples
  is the live open question.
  **New material (2026-06-13):** Rittel & Webber read provides a theoretical grounding for
  the ratchet mechanism — protocols are taming operations on wicked problems; re-opening
  them means re-entering the wicked territory the protocol was designed to escape. The
  externally-imposed case is doubly invisible: the embedded political choices were someone
  else's wicked territory. C-015–022 extend this. Assess whether this closes trigger (b).
  Transition trigger: either (a) strong reversion counterexample found (successful
  reversion with personnel continuity, ruling out social substrate reset), or (b)
  the internal/external distinction survives retrieval and becomes a law modifier.
  Either result closes the valley.

---

## Sensemaking Needed
*Cheap trick has fired; no project arc formalized yet. One session to draft YAML and
open a project file. Do not let cheap tricks sit unformalized indefinitely.*

- **Simon read — local-maximum trap** (cheap trick fired; needs H YAML + DS-008) → needs H-003 YAML + DS-008 arc file.
  Cheap trick: protocols act as local optima in the design space — incremental
  improvement cannot escape them even when a better design is globally visible.
  Cross-references Hamming insight (problem inversion) — may be the same phenomenon at
  different levels. Assess during sensemaking.

- **Simon read — near-decomposability + stable intermediates** (C items; retrieval needed before H) — needs
  corpus retrieval to confirm evidence base before opening arcs. One targeted session;
  if retrieval is productive, open project files.

- **Humboldt insight — Mean-Point Law** (cheap trick fired; needs H YAML + DS-008 or DS-009) — cheap trick fired in early exploration; no project
  arc. Test: are major protocol revisions triggered by visible extremes (crises) or by
  mean-point analysis? Public health (vaccination protocols) is the candidate falsifier.

---

## Cheap Trick Pending
*Late exploration — enough material in view that a crystallizing insight may be near.
Watch for the crescendo tempo signature (rapid integration, sense of things fitting
together). Do not force it before it arrives.*

- **Humboldt intuition — Substitution Invariance** (C item; cheap trick not yet fired) — Hypothesis: F-001, CL-001, and F-004 may
  all be special cases of a single conservation principle (functional structure is
  conserved in protocol ecosystems under pressure). Cheap trick trigger: a cross-domain
  retrieval session either surfaces a unifying pattern or confirms the three laws are
  genuinely independent. Either is progress.

- **Hamming + Simon reads — local-optima cross-reference** (two C/H items; one retrieval session) — Both describe structural barriers to
  escaping local optima, at different levels of analysis (cognitive vs. coordination).
  May merge into a single hypothesis or stay complementary. One retrieval session.

---

## Behavior Blockers
*Behaviors whose stub status is preventing a specific arc from advancing. Track 2
resolves these; Track 1 names them here as the demand signal. Format: behavior-xxx
[BLOCKING: DS-xxx — what phase move is blocked].*

*(none currently — revisit when synthesis and research_tick behaviors mature)*

---

## Operator Steps
*Arc-adjacent actions requiring operator input, not research investigation.*

- CL-Rao-1 (Narrative Displacement), CL-Rao-2 (Doctrine Lock-In), CL-Rao-3
  (Temporal Misalignment Failure) — review `bibliography/notes/rao-tempo.md` §10
  and decide which warrant promotion to hypothesis YAMLs.

---

## Exploration
*Open territory, no cheap trick yet. Enter here when the productive valley and
sensemaking queues are clear, or when the inventory needs fresh ground.*

- First canonical domain rotation (M-002): Decentralized Systems — FLP impossibility,
  BFT protocols. Known domain; may surface laws in corners not yet examined.
- Immunology as candidate canonical domain: self/non-self discrimination. One targeted
  retrieval session to test fertility before committing to a full rotation.
- **Iverson curiosities** (C-011 through C-014) — notation lock-in, suggestivity/mastery
  tradeoff, efficiency circularity, multiple representations. No cheap trick yet; need
  one corpus retrieval session to see if protocol-notation examples are recoverable.
  C-012 (suggestivity/mastery tradeoff) has a direct bearing on CL-001 adoption dynamics.

- **Batch deep-read curiosities** — 61 arXiv papers reading in background (batch-deepread PID 90871, session 20).
  After batch completes, review `bibliography/deep-read-verdicts.md` for escalation training signals
  and `bibliography/notes/arxiv-*.md` for candidate curiosities. May surface cheap tricks on
  Q-003 (trust asymmetry), Q-007 (biological limits), Q-010 (substitution invariance).
