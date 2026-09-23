# Core Up-To-One for Participatory Budgeting with Additive Utilities

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.15928
**Date read:** 2026-09-22
**Connected to:** L-006, L-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper on fair division protocols for participatory budgeting. It proposes a selection rule (utility-weighted harmonic entropy plus cost penalty) that satisfies the "core-up-to-one" fairness condition — a weakening of the core concept that permits coalitions to block only if they can improve all members by more than the cost of a single project.

## What I took from it

This is competent work on preference aggregation fairness, but it operates *within* the standard rational-agent framework and does not interrogate the structural conditions under which that framework breaks down under protocol formalization.

The paper assumes additive utilities and cost-feasibility as given constraints. It does not examine: (1) how the choice to render preferences as additive utilities itself shapes which coalitions form or which preferences are expressible; (2) whether the fairness guarantee (core-up-to-one) remains meaningful once budgeting allocation becomes legible to optimization; (3) whether formalization of the allocation rule itself produces incentive leakage or gaming at the preference-elicitation stage.

The work confirms that preference aggregation in fair division can be *technically solved* under rationality assumptions, but does not engage with L-019's claim that representation and rationalizability trade off — i.e., that rendering heterogeneous preferences into a computable aggregation function itself constrains what preferences can be *rationally held* within the protocol.

## Research connections

- **L-006 (Coordination Cost Conservation):** The paper assumes coordination costs are already localized to the preference-elicitation phase; it does not track whether the fairness guarantee moves coordination burden to enforcement or coalition-formation layers.
- **L-019 (Representation-Rationalizability Tradeoff):** The additive utility model is a representational choice that may exclude non-additive preference structures; the paper does not examine whether this choice makes certain agent archetypes *rational* within the protocol while rendering others formally irrational.
- **seed-144 (Informality as Coordination Cost Refuge):** No engagement with whether agents would seek informal preference-sharing outside the protocol to avoid being locked into additive decomposition.

## Seed

**Seed title:** none

---

**Reasoning:** This paper solves a well-posed technical problem in mechanism design but does not disturb the foundational assumptions of that problem class. It advances the state of fair division under rationality but does not expose a new mechanism by which formalization itself produces protocol instability, agent evasion, or invariant fragility. The work is orthogonal to the "new nature" research agenda rather than feeding it.
