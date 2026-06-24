# Sphere of Influence Centrality via Shapley Values: Empirical Approximation and Network Coverage Analysis

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.24121
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical evaluation paper applying coalitional game theory (Shapley values) to the classical network centrality problem. The work tests whether Shapley-value-based "sphere of influence" metrics outperform classical centrality measures in selecting m nodes to maximize coverage under three reachability criteria (single-hop, k-hop, multi-path) on real-world networks.

## What I took from it

This is a *method paper with empirical validation*, not a primary theoretical contribution. It operationalizes an existing framework (Michalak et al.'s Shapley-based approach) and benchmarks it against baseline centrality metrics. The relevance to the "new nature" agenda is limited: it confirms that coalitional value assignments can model interdependent node influence better than degree/betweenness, but this is already theoretically expected. The paper does not reveal a mechanism absent from our inventory—it applies known machinery to a known problem.

The empirical scope (Euroroad, Facebook TV shows, [third network incomplete in abstract]) is narrow for generalizing claims about protocolized systems. No discussion of adaptive dynamics, strategic behavior, or how these centrality orderings change under manipulation or evolution—all critical for artificial/protocol systems.

## Research connections

- None at present (no established laws or active hypotheses yet defined in context).

## Candidate laws or signals

**none**

---

**STORAGE NOTE:** File under "Network centrality → coalitional methods" for reference. Revisit only if future work investigates how Shapley-centrality rankings degrade under adversarial node removal or protocol-driven rewiring.
