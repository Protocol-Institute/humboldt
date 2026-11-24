# When do token systems stabilize? Compatibility constraints and community structure

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.36744
**Date read:** 2026-11-23
**Connected to:** L-006, seed-456
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of token-exchange protocols with random availability constraints. The paper establishes necessary and sufficient conditions for balance stability and proposes the minimum-token rule as an optimal selection mechanism. Domain: abstract protocol design for peer-to-peer service exchange without monetary intermediaries.

## What I took from it

The work formalizes a narrow but concrete instantiation of L-006 (Coordination Cost Conservation): when compatibility constraints limit who can serve whom, the system must solve a selection problem. The minimum-token rule redistributes across the constraint topology rather than eliminating the underlying tension between balance maintenance and service availability.

The paper does not engage with how agents game the selection rule, how the rule ossifies under adoption, or whether stability properties hold under strategic behavior or information asymmetry. It treats the protocol as a mechanism design problem in a cooperative setting, not as a live system subject to optimization pressure, norm drift, or formal-informal layering. The connection to L-006 is confirmatory rather than generative: it shows that coordination cost persists *within* the protocol layer, but does not expose what happens when the protocol itself becomes subject to modification pressure or when informal norms around service exchange predate and resist formalization.

## Research connections

- **L-006:** Token balance stability under availability constraints is a form of coordination cost redistribution, not elimination. The rule choice shifts which agents bear the cost, not whether the cost exists.
- **seed-456:** Mentioned in triage but not visible in current pool; likely concerns equilibrium multiplicity or rule-dependent stability regions.
- **L-004 (potential weak connection):** Minimum-token rule is a legible proxy for "fairness" or "balance"; under adoption pressure, agents may optimize against the proxy rather than the underlying service-exchange goal.

## Seed

**Seed title:** Selection Rule Legibility as Optimization Target Under Competitive Provision

**Seed type:** observation

**Seed text:** In token systems where service provision is constrained by agent availability and selection is formalized (e.g., minimum-token rule), the selection rule itself becomes a target for strategic behavior. Agents may manipulate token balance not to serve others fairly, but to control their probability of being selected or to signal trustworthiness to the system. The stability condition derived under cooperative assumptions may not hold when selection legibility inverts from a coordination device into an optimization surface. This suggests a tension between formalizing allocation rules and maintaining the informal heuristics that made the original system resilient.
