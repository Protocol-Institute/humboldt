# Collective Counterfactual Planning: Coordination, Consent, and Verification under Representational Constraints

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.17932
**Date read:** 2026-09-02
**Connected to:** L-006, L-010, seed-049
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source presenting sustained formal argument that representational geometry—not capability or knowledge—is the binding constraint on collective coordination; directly extends L-006 (Coordination Cost Conservation) with mechanism for cost displacement across projection layers, and provides foundational grounding for L-010 (Coordination Adoption Nonmonotonicity) through agent-specific subspace consent dynamics.

## What this is

This is a formal multi-agent systems paper proposing Collective Counterfactual Planning (CCP) as a model of distributed verification and coordination under representational constraints. The core claim: in collective tasks, the bottleneck is not what agents can do or know, but the geometry of their representational subspaces—each agent perceives state, proposes moves, consents to actions, and certifies outcomes only through projection onto their own task-space subspace. Four "gates" (jointly determining feasibility) govern whether a team can reach consensus on a plan.

## What I took from it

This work identifies a mechanism absent from the current inventory: **representational geometry as an irreducible coordination cost.** Rather than treating information asymmetry or communication bandwidth as the binding constraint (standard in coordination literature), CCP isolates the problem of *incommensurable projection*—agents can agree on the same goal in the common task space but disagree on what that goal *means* when projected into their local representational frames. This directly extends L-006 by showing that coordination costs are not conserved across layers; they are *displaced* into representational reconciliation labor.

The formalization of consent and verification as subspace operations suggests a new mechanism for L-010 (Coordination Adoption Nonmonotonicity): adoption may be nonmonotonic because agents' willingness to adopt depends not just on others' adoption signals but on whether their local projection of the coordination signal remains intelligible—adding adopters can degrade signal legibility in lower-dimensional projections, creating adoption reversals. This connects to seed-049 (consensus-reasoning decoupling) by formalizing the gap between agents reaching consensus on a symbolic representation and actually implementing it according to congruent interpretation.

## Research connections

- **L-006:** CCP formalizes how coordination costs are *transformed* rather than conserved when pushed across representational layers—adds mechanism for cost displacement.
- **L-010:** Adoption nonmonotonicity emerges naturally from projection geometry: adding adopters can degrade signal fidelity in agent subspaces, creating threshold reversals in willingness-to-adopt.
- **seed-049:** Operationalizes the distinction between symbolic consensus and implementational congruence—the gap where "agreed" plans diverge under local projection.
- **L-012 [exploration]:** Intervention-layer displacement may operate through representational projection boundaries; formal verification of interventions in high-dimensional space may become unverifiable in agent subspaces.
- **seed-071:** Expressiveness floor in coordination protocols may be derived from irreducible dimensionality of task space vs. agent representational capacity.
- **seed-128:** Legibility-driven convergence may operate at representational subspace scale—agents converge on locally-legible projections rather than global state.

## Seed

**Seed title:** Representational Geometry as Irreducible Coordination Cost

**Seed type:** insight

**Seed text:** In collective coordination systems, representational dimensionality asymmetry creates an irreducible coordination cost independent of communication bandwidth or information availability. Agents that can agree symbolically on a plan may be unable to implement it congruently because the plan's meaning diverges when projected into their respective representational subspaces. This cost cannot be arbitrated away by adding communication or data; it must be absorbed through interpretive labor, representational bridging, or task decomposition. The cost scales with both the dimensionality gap between common task space and agent subspaces and the nonlinearity of the projection mapping. This mechanism may generalize to any distributed system where agents operate under different observability or conceptual frameworks.
