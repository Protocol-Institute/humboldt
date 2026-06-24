# Idea: Protocols differ from procedures by typing the space of valid next moves

**Source:** Discord #I imagine the gap is outline in that ZIP (by humboldt)
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** Refines existing distinction inventory without introducing novel operational principle; useful precision on protocol semantics but not yet differentiated enough from active hypothesis work on type-driven behavior to warrant independent candidate status.

## What this is

Protocols actively constrain future states through type signatures on receiver expectations, whereas procedures passively enumerate permitted actions—a distinction between prescriptive typing and permissive rule sets.

## What I took from it

This reiterates and tightens the core protocol/procedure boundary already present in the working hypothesis set (referenced in triage as items 4 and 5). The framing here emphasizes the *active waiting* posture of protocol participants—the attendant process doesn't just check rules after each move, but is structured by the type system to expect only certain shapes of input. 

That said, this is a useful semantic refinement rather than a novel discovery. It clarifies that protocols are not merely restrictive procedures but *type-directed* ones, where the constraint lives in the signature itself, not in post-hoc validation. This opens a small but real question: whether the formalization work (π-calculus, session types) already captures this distinction adequately, or whether something about the *anticipatory* or *stance-taking* aspect of typed waiting deserves separate treatment as a phenomenon of artificial systems specifically.

## Research connections

- **Hypothesis 4 (inferred):** Protocol semantics turn on constraint-before-action rather than constraint-after-action
- **Hypothesis 5 (inferred):** Type structures in protocols encode permissible state transitions, not just rule sets
- **Method alignment:** π-calculus formalism already models this via channel typing and session discipline

## Candidate laws or signals

**none** — The distinction is sound but already absorbed into the active hypothesis work on type-driven protocol structure. Promote to candidate law only if empirical work on real protocol systems (smart contracts, API specs, control planes) shows this typing/permission boundary exhibits consistent *failure modes* or *brittleness patterns* that current hypotheses don't predict.
