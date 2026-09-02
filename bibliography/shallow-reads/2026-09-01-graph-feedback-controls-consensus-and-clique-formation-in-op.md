# Graph Feedback Controls Consensus and Clique Formation in Open-Weight Language-Model Populations

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.12077
**Date read:** 2026-09-01
**Connected to:** L-010, seed-053
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

An empirical study of convention formation in multi-agent LM systems using a naming-game protocol, measuring how graph topology of inter-model interactions shapes consensus dynamics across parameter-size populations (1.1B–32B). The work separates surface agreement (label choice) from latent state-space alignment and tests how intervention on interaction structure affects clique formation.

## What I took from it

The paper is a solid mechanistic study of how topology controls coordination in LM populations — exactly the kind of legible, computable setting where coordination dynamics become tractable. The key empirical result (that graph structure directly gates consensus formation) is unsurprising and well-executed, but the work is primarily demonstrative rather than law-bearing.

The paper does confirm that in systems where agents are information-integrating black boxes constrained only by protocol-level interaction, the *structure* of that protocol layer becomes the binding constraint on coordination outcomes — no surprises relative to L-010 (Coordination Adoption Nonmonotonicity) or seed-053 (shared infrastructure emergent collusion). It shows that clique formation happens, that graph topology matters, and that state-space alignment can decouple from output agreement. But it does not isolate a novel *mechanism* of alignment or collision that doesn't already follow from multi-agent learning theory. The naming game is a toy coordination problem; the generalization to real protocol racing (where stakes are asymmetric, deployment timing is concentrated, and the prize structure changes behavior) is not addressed.

## Research connections

- **L-010:** Confirms that coordination adoption is topology-dependent; adds no new condition or mechanism to the exploration of nonmonotonicity.
- **seed-053:** Directly studies shared-infrastructure-driven alignment in LM populations; does not isolate a novel collusion mechanism or measure real economic/competitive incentives.
- **L-009:** Catastrophic Risk Cancellation — the paper's LM populations are symmetric and non-competitive; does not address asymmetric racing or first-mover concentration.

## Seed

**Seed title:** none
