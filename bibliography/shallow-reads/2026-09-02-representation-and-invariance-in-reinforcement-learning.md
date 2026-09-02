# Representation and Invariance in Reinforcement Learning

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2112.07752
**Date read:** 2026-09-02
**Connected to:** L-005, L-011
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical paper formalizing the conditions under which RL agents can be mapped between different formal frameworks while preserving relative intelligence. The core contribution is a sufficiency criterion for framework-agnostic agent portability, with a proof that this criterion cannot be universally met across all framework pairs.

## What I took from it

The paper directly engages the mechanical problem underlying L-011 (Causal Detachment as Stable Protocol Equilibrium) and L-005 (Gall Generalization): when you formalize an agent's behavior in one representational system, can that formalization survive intact when ported to a different representational substrate? 

The negative result — that the sufficiency criterion "cannot be met" — is the key finding here. It suggests that framework conversion necessarily introduces a representation gap that cannot be closed by any single mapping rule. This aligns with L-005's claim that complex functional systems resist restructuring: an RL agent optimized within one framework's reward/state abstraction cannot be naively transplanted without degradation. The paper does not develop the *why* behind this irreducibility, but the finding itself is mechanically sound for the protocol ossification inventory.

However, this remains a domain-specific mathematical result. It does not establish whether the barrier is fundamental to all protocol migration, whether it generalizes to non-RL adaptive systems, or whether it has predictive or exploratory power beyond framework theory.

## Research connections

- **L-005:** The unmappability result confirms Gall's intuition that complex functional systems resist clean restructuring — here instantiated in the formalism of agent representation across framework boundaries.
- **L-011:** Touches the causal detachment question: operational functionality in one framework may not survive formalization in another, suggesting that "stable functional configurations" are substrate-dependent rather than portable.
- **seed-062 (Formalization Opacity Collapse):** The paper hints at a deeper motif — that formalization itself introduces irreversible abstraction loss, a candidate mechanism for why transparency does not guarantee portability.

## Seed

**Seed title:** Representation Gap as Irreducible Protocol Boundary
**Seed type:** observation
**Seed text:** When a protocol agent or decision rule is formalized in one representational system (reward structure, state abstraction, action space), a sufficient mapping into an alternative formal framework cannot be guaranteed to preserve relative performance or functional integrity. The gap is not a gap in clarity or completeness — it is a structural feature of framework incommensurability. This may generalize beyond RL: any protocol migration that requires re-encoding an agent's optimization target into a new legible substrate risks introducing a floor below which performance cannot be recovered without redesign at the agent level, not the framework level.
