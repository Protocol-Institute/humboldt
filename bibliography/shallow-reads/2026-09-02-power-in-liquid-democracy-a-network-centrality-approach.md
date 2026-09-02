# Power in Liquid Democracy: A Network Centrality Approach

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.13188
**Date read:** 2026-09-02
**Connected to:** L-010, L-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper proposing Random Walk Decay centrality as a tractable metric for measuring voter influence in liquid democracy systems (where votes can be transitively delegated). The work provides axiomatic grounding for the metric and argues for its advantages over PageRank-style alternatives in capturing influence propagation through delegation networks.

## What I took from it

The paper treats delegation networks as a static structural problem: how to measure power given a fixed graph of delegation relationships. This is technically sound but orthogonal to the core dynamics that L-010 and L-015 flag. The work does not examine *why* adoption patterns are non-monotonic (L-010) or how interpretive continuity decays when formal audit trails survive institutional memory loss (L-015). The delegation graph itself is treated as exogenous; the paper does not model strategic delegation, defection under visibility pressure, or the conditions under which delegators revoke or redirect votes based on metric legibility. There is no mechanism for how a formalized power metric, once published, becomes an optimization target that reshapes delegation behavior itself—a classic L-008 / seed-059 dynamic. The work is competent within its frame but does not probe the feedback loops that make liquid democracy systems unstable or resilient.

## Research connections

- **L-010:** Paper assumes delegation adoption is static; does not address why adoption curves are non-monotonic or how coordination signals alter delegator behavior.
- **L-015:** No examination of institutional knowledge loss when formal delegation records persist but social context for interpreting them decays.
- **seed-059:** Trust Legibility Inversion — The centrality metric, once published, may become a target for strategic delegation rather than a neutral measurement tool.
- **seed-069:** Transparency-Legibility as Trust Proxy Substitution — Formalizing power via centrality may substitute for deeper institutional trust in delegatees.

## Seed

**Seed title:** Formalized Power Metrics as Delegation Attractors

**Seed type:** motif

**Seed text:** In delegation-based governance protocols, the formalization and publication of a power metric (e.g., centrality score) creates a legible optimization target for delegators, displacing strategic behavior away from reputation or competence signals and toward network position. This generates a two-layer distortion: (1) delegators preferentially select high-centrality nodes to maximize their own indirect influence (positive feedback); (2) centrality scores become decoupled from the actual decision quality or trustworthiness they were intended to proxy. The effect is strongest when the metric is simple, machine-readable, and widely circulated. This pattern likely generalizes to any governance protocol where influence is formalized as a computable quantity and agents can condition behavior on it.
