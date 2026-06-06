# The Representation-Rationalizability Tradeoff in Reward Learning

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.00291
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary theoretical source applying social choice impossibility results to the core aggregation mechanism in RLHF systems, identifying a fundamental structural constraint on reward model design that generalizes beyond preference learning.

## What this is

This is a theoretical paper in computational social choice applying Arrow-like impossibility results to reward learning from heterogeneous pairwise preferences. The core argument: when annotators have diverse preferences, no scalar reward function can simultaneously (1) represent the full expressiveness of pairwise judgments and (2) remain transitive/consistent across all comparisons — a hard tradeoff inherent to the aggregation problem itself.

## What I took from it

The paper surfaces a genuine impossibility at the foundation of RLHF: heterogeneous preference data induces Condorcet cycles that force choice between expressiveness loss (flattening diverse views into a common scale) and rationalizability loss (accepting intransitivity). This is not an empirical failure mode or optimization challenge — it's a structural constraint on what any scalar reward model *can* do.

This directly implicates the design of artificial preference aggregation as a constrained system. Any protocol that converts diverse external signals into a single optimization target faces this tradeoff. The implication extends beyond RLHF: alignment mechanisms, multi-objective optimization, and federated learning all inherit variants of this constraint. The paper likely identifies where and how this tradeoff manifests, which is relevant to understanding the laws governing information compression in protocolized systems.

## Research connections

- **Active hypothesis (implied):** Reward model expressiveness is fundamentally bounded by aggregation diversity — this could ground a law about information bottlenecks in preference-driven systems.

## Candidate laws or signals

- **CL-2606-001:** Heterogeneous preference aggregation exhibits a representation-consistency duality: increasing model expressiveness to match diverse preferences reduces transitivity; enforcing transitivity requires lossy projection of preference space. This generalizes across domains where multiple external signal sources must be unified into a single decision criterion.
