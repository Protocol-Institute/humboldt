# To EFX OR to MMS, That is the Question

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.10397
**Date read:** 2026-09-22
**Connected to:** L-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic impossibility result in fair division. The paper shows that relaxing fairness constraints by allowing agent-wise disjunction (each agent gets *either* EFX *or* MMS) does not restore existence of allocations, contrary to the intuition that flexibility should enable solutions. The core contribution is a counterexample demonstrating that even weakened preference aggregation constraints can be simultaneously unsatisfiable.

## What I took from it

The result illuminates a property of preference aggregation protocols under heterogeneous constraint systems: adding *optionality* across incommensurable fairness metrics does not monotonically increase solvability. This inverts the usual design intuition that flexibility buys tractability.

The finding is relevant to L-019 (Representation-Rationalizability Tradeoff) but in a negative mode: it shows that when aggregation must satisfy multiple *disjunctive* fairness predicates simultaneously across agents, the solution space can collapse even when either predicate alone has (or is believed to have) solutions. This suggests that multi-objective preference aggregation protocols exhibit phase transitions not predicted by single-objective analysis. The mechanism appears to be constraint *interaction* under heterogeneous agent satisfaction requirements — the disjunction structure forces global consistency across local optionality, creating hidden dependencies.

This is relevant to protocol design in automated allocation systems (matching, recommendation, resource division) but the work remains domain-specific: it does not expose a generalizable mechanism of how legibility, formalization, or enforcement pressure distorts the aggregation process itself.

## Research connections

- **L-019:** Adds negative evidence that heterogeneity in preference representation does not monotonically improve rationalizability; disjunctive constraints create coupling across local choices.
- **seed-144:** Suggests that formalization of fairness criteria (rendering them machine-readable predicates) creates constraint interactions absent in informal coordination.

## Seed

**Seed title:** Disjunctive Aggregation Collapse Under Heterogeneous Predicates

**Seed type:** observation

**Seed text:** When a protocol aggregates preferences or constraints via *disjunctive choice* (each agent satisfies at least one of N incommensurable predicates), the global existence of solutions can fail even when each predicate individually admits solutions or appears tractable. The mechanism is hidden coupling: agent-wise optionality creates constraints on other agents' predicates, collapsing the joint solution space. This may generalize to any formalized multi-criterion protocol where agents must be satisfy-or-exit across incomparable metrics.
