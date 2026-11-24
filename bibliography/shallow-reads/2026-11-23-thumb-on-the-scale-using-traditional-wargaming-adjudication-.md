# Thumb on the scale: Using traditional wargaming adjudication practices to improve AI-judged evaluations and grading

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.32066
**Date read:** 2026-11-23
**Connected to:** L-004, seed-528
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper that maps procedural design patterns from two centuries of wargaming adjudication onto problems in AI evaluation rubrics. The core claim is that AI evaluation failures are not primarily about *which judge* (which AI model) or *what criteria* (rubric wording), but about *how judgment is administered* — the procedural freedom, constraint, and failure modes of the adjudication process itself. Tests one wargaming method (adjudication procedure variation) on 378 player actions.

## What I took from it

This is a **procedural literacy paper** — it argues that evaluation systems have been optimizing the wrong layer. Rather than iterating on rubric clarity or judge selection (the legible, measurable surfaces), the work suggests the hidden load sits in *procedural structure*: how much discretion the adjudicator has, when they apply it, what feedback loops exist, and how those interact with the system's stress points.

This connects obliquely to L-004 (Goodhart Generalization) but in a protective direction: the paper is not arguing that metrics *will* get captured, but that *how you administer the measurement* determines capture vulnerability. It suggests that formalization of judgment (which the triage note flags as an ossification vector) can be *defended against* by borrowing procedural constraints from domains that have operated under similar uncertainty for longer. The implication is that protocol design should inherit not just decision rules but *decision-flow topology* from mature informal systems.

The work also bears on L-023 (Informality as Novelty Sink): wargaming procedure intentionally preserves referee discretion *within bounded channels*, a pattern that might resist the total legibility collapse that drives novelty capture in rigid formal systems. It suggests that some formalization can be *protective* if it formalizes procedure rather than outcome.

## Research connections

- **L-004:** Metric capture risk might be modulated not by better rubrics but by procedural constraints on when and how the rubric is applied — a layer current research undersamples.
- **seed-528:** Directly engaged — adjudication procedure as audit criteria and ossification vector. The paper tests whether procedural variation *prevents* ossification.
- **L-023:** Wargaming procedure design as a model for maintaining functional discretion within formalization, possibly resisting novelty capture.
- **seed-544 (Metalinguistic Displacement Under Formalization Pressure):** Wargaming adjudicators develop metalanguages to describe judgment *prior to* formalization; this may be a preventive pattern worth studying.

## Method note

This paper models a valuable methodological move for the new nature research agenda: *importing procedural design from mature informal domains into formal systems analysis*. Rather than studying failures only by reading forward (what does formalization break?), it reads backward (what did we do before formalization to handle the same uncertainty?). For protocol research, this suggests systematic comparison with pre-computational analogues — not as historical curiosity but as a source of tested procedural topologies that might transfer. The wargaming case also demonstrates that procedure testing is feasible and yields actionable refinement, suggesting that evaluation and audit systems themselves should be treated as experimental domains, not fixed reference frames.
