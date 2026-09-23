# Envy-Free Chore Allocation with Unit Subsidies under Negative Dichotomous Valuations

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.14465
**Date read:** 2026-09-22
**Connected to:** L-019, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** [blank]

## What this is

A fair division paper extending the dichotomous goods allocation model to the chore case. The work proves that under negative dichotomous valuations (each chore has marginal disutility 0 or 1 per agent), envy-free allocations exist with at most one unit of subsidy per agent, matching the bound for the dual goods problem.

## What I took from it

This is a completion of a symmetry result in fair division: the goods and chores models now have matching subsidy guarantees under dichotomous preference structure. However, the work operates entirely within the classical preference-aggregation setting and does not examine what happens when the binary valuation constraint itself becomes a *proxy* for unmeasurable fairness or satisfaction, nor does it investigate how agents optimize *against* the dichotomous structure once it is formalized as a legible protocol.

The paper is technically sound but does not extend the mechanism inventory or reveal new failure modes in preference aggregation under formalization. The dichotomous constraint simplifies the problem rather than creating the kind of metric capture or boundary displacement dynamics that characterize L-004 or L-019 in their protocolized contexts.

## Research connections

- **L-019:** The dichotomous valuation is itself a severe representation constraint, but the paper does not examine whether agents would optimize around or falsify this constraint if the protocol were operationalized. The tradeoff between representability and rationalizability is assumed solved by the problem definition, not explored.
- **L-004:** The subsidy becomes a measurable proxy for "fairness," but the paper studies only the static existence problem, not whether subsidies would induce strategic misreporting or metric gaming if deployed in a real system.
- **seed-129:** Implied but not addressed: whether formalizing dichotomous valuations as a protocol input creates legibility-driven convergence to stated preferences or whether agents learn to express only binary signals strategically.

## Seed

**Seed title:** none

**Seed type:** [null]

**Seed text:** [This is competent work within fair division theory, but it does not generalize beyond the allocation setting or produce a mechanism absent from the current inventory. The binary valuation constraint is a simplification device, not a natural emergence under stress or scaling.]
