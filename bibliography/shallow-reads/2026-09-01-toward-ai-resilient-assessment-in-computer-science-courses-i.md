# Toward AI-Resilient Assessment in Computer Science Courses in an AI-Native World

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.30655
**Date read:** 2026-09-01
**Connected to:** L-001, L-003
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A pedagogical framework paper proposing formal methods for assessment design under AI adoption pressure. The work aims to define "AI-resilient skill" as a measurable outcome and argues for decoupling student evaluation from AI budget/access asymmetry by establishing a Pareto frontier of legitimate AI-native baselines.

## What I took from it

This is a case study in *reactive formalization under adoption pressure* rather than a theory-bearing document. The paper observes that AI availability in assessment contexts creates a coordination problem—institutions need a legible, defensible rule for what constitutes legitimate vs. unfair AI use—and responds by proposing formal specification (task definition, executable evaluator, declared frontier, grading rule).

This is precisely L-003 (Formalization Ratchet) at work: informal norms about "doing your own work" become unenforceable and lose coherence once AI agents become capable collaborators. The proposed solution is further formalization—higher-fidelity specification of the game boundary. The paper does not examine whether this formalization itself creates new optimization pressures or shifts the locus of gaming (e.g., to frontier-gaming, task-gaming, or evaluator-gaming). It is symptom management, not mechanism investigation.

The connection to L-001 (Ossification) is weaker but present: once an assessment protocol codifies a Pareto frontier, that frontier becomes difficult to revise as institutions adopt it, even if the frontier was provisional or empirically discovered rather than principled.

## Research connections

- **L-003:** Directly illustrates the Formalization Ratchet mechanism—pressure from AI adoption forces informal assessment norms into formal, computable rules.
- **L-004:** The "AI-resilient skill" metric is itself a proxy for unmeasurable educational goals; the paper does not examine whether optimizing to that metric will capture or distort the intended outcome.
- **seed-014 (if it existed):** Illustrates how legal/protocol obligation formalization (here, assessment rules) creates new surfaces for optimization and boundary-concentration behavior.

## Method note

This paper is useful as a *symptom detector* rather than a *law source*: it documents a live institutional problem and an attempted solution, but treats the solution as unambiguous improvement rather than a move in a larger strategic game. Future work should track whether AI-resilient assessment frameworks actually reduce gaming or simply relocate it. The meta lesson is that case studies of protocol redesign under stress are most valuable when they include longitudinal post-adoption observation of whether the redesigned protocol exhibits the pathologies it was meant to cure—otherwise they remain prescriptive rather than predictive.
