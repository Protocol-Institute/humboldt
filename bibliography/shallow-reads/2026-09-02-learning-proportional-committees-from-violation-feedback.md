# Learning Proportional Committees from Violation Feedback

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.30111
**Date read:** 2026-09-02
**Connected to:** L-003, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic learning paper on committee selection under adversarial violation feedback. The learner proposes committees iteratively; an oracle either accepts or reveals a proportional representation violation. The work compares informativeness of full-witness feedback (violation level + omitted candidate + affected group) versus candidate-only feedback, establishing sample complexity bounds for learning proportionally representative approval-based committees.

## What I took from it

The paper formalizes a feedback regime for discovering hidden preference distributions through violation signals. This is relevant to L-003 (Formalization Ratchet) in that the move from informal majoritarian judgment to computable proportionality criteria creates a legible target surface for optimization. The oracle adversarially *selects* which violation to surface — a design choice that shapes what the learner can infer. This echoes L-010 (Coordination Adoption Nonmonotonicity): different feedback structures produce different learning trajectories, and fuller information does not monotonically improve adoption of the learned rule. 

However, the domain is narrow: this is a pure learning-under-feedback problem, not an empirical study of how committees actually adopt proportional rules, nor a mechanism operating at scale in a protocol system. The violation feedback itself is idealized — an oracle, not a distributed governance process. The connection to formalization ratchet is suggestive but not demonstrated: we see *that* a proportional rule can be learned from violations, not *how* informal norms break down when formalization pressure mounts, nor how the learned rule then ossifies.

## Research connections

- **L-003:** Formalization creates a legible target surface (proportional representation) that can be optimized against via violation signals; does not show the ratchet dynamic itself (informal → formal → rigid).
- **L-010:** Different feedback informativeness levels alter learning speed and trajectory; no evidence here of nonmonotonicity in *adoption* (agents conditioning on others' adoption).
- **seed-062 (Formalization Opacity Collapse):** Moving from violation signals to computable committee criteria represents a transparency gain, but the paper does not explore what becomes opaque in the process.
- **seed-073 (Correlated Failure Under Proxy Consensus):** Proportional representation is a proxy for voter preference satisfaction; no exploration of how consensus on this proxy might mask divergent underlying goals.

## Seed

**Seed title:** Violation Informativeness as Learning Regime Stratification

**Seed type:** observation

**Seed text:** In protocol systems where compliance is learned via feedback on violations, the granularity and specificity of violation signals stratifies the speed and confidence of learner inference. Richer violation feedback (which candidates, which groups harmed, magnitude of violation) accelerates convergence but may also accelerate convergence to locally legible but globally unstable equilibria. The oracle's adversarial selection of *which* violation to reveal introduces a hidden layer of protocol design: the choice of feedback informativeness itself becomes an optimization pressure point. This may generalize to any adaptive protocol where the entity generating feedback (auditor, enforcement agent, monitor) has agency over *what* signals to make visible.
