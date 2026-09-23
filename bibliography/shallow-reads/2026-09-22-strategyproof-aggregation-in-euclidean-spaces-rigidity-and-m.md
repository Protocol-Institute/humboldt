# Strategyproof Aggregation in Euclidean Spaces: Rigidity and Median Optimality

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.19394
**Date read:** 2026-09-22
**Connected to:** L-019, seed-134
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** [none]

## What this is

A mathematical game theory paper proving that coordinate-wise median aggregation is optimal (minimizes worst-case approximation error) among all continuous, anonymous, deterministic strategyproof mechanisms in finite-dimensional Euclidean spaces. The work establishes a rigidity theorem: under strategyproofness constraints, the solution space collapses to a narrow family of mechanisms.

## What I took from it

The paper demonstrates a deep structural constraint: when you require a preference aggregation mechanism to be strategyproof (incentive-compatible), the set of rational solutions becomes geometrically rigid. The median is not just *good*—it is *forced* by the combination of truthfulness, anonymity, and continuity. This confirms the core intuition of L-019 (representation-rationalizability tradeoff): demanding both high expressiveness (aggregating heterogeneous preferences in continuous space) AND incentive alignment (strategyproofness) creates a binding constraint that eliminates most of the design space.

The paper does not address what happens when agents know this rigidity exists, or how computational legibility of the median mechanism affects strategic behavior at the boundary. It is a proof of optimality within a constrained frame, not a study of how that frame itself becomes a coordination object or point of capture.

## Research connections

- **L-019:** Confirms the existence of hard tradeoffs in preference aggregation under incentive constraints—rigidity is the mechanism forcing the rationalizability boundary.
- **seed-134:** Relevant as a candidate case of how neutrality proxies (median as "neutral" aggregator) become optimization targets once their structure is formalized.

## Seed

**Seed title:** Legibility-Driven Mechanism Rigidity Under Incentive Formalization

**Seed type:** observation

**Seed text:** When preference aggregation mechanisms are required to satisfy both formal incentive properties (strategyproofness) and operate in continuous representational spaces, the solution space undergoes rigidity collapse—multiple mechanisms collapse into a single canonical form (e.g., median). Once this canonical form becomes computationally legible and enforceable, it becomes a stable target for strategic boundary-seeking behavior. The question is whether agents optimize *toward* the median or *around* its known rigidity structure when they recognize it as a locked-in aggregation rule.
