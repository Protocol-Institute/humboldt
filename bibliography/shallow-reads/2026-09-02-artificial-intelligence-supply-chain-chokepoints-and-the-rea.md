# Artificial Intelligence: Supply-Chain Chokepoints and the Reach of Industrial Policy

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.29572
**Date read:** 2026-09-02
**Connected to:** L-001, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement paper applying the Herfindahl-Hirschman Index (HHI) to concentration across the AI supply stack (chips, compute, electricity, minerals). The core finding: concentration rises steeply upstream and remains low downstream (where regulatory attention concentrates), revealing a structural mismatch between where oversight and where actual control reside.

## What I took from it

The paper documents a phenomenon directly relevant to L-001 (Protocol Ossification Under Adoption Pressure) and L-014 (Strategic Boundary Concentration Under Computable Legality), but primarily as an *observational confirmation* rather than a mechanism paper. It shows that industrial policy and regulatory attention have produced legible, measurable chokepoints upstream (chip fabrication, rare minerals) precisely because these layers have become computable control surfaces — the inverse of L-001's prediction about adoption pressure locking protocols. The asymmetry is institutional and economic rather than protocol-driven: downstream (model APIs, cloud access) remains fragmented because it's easier to entry and harder to *legally specify* in advance. The paper does not analyze how this concentration *persists* or *stabilizes* as a regulatory equilibrium, or how agents optimize against the visibility of upstream chokepoints. It is descriptive of the current state, not explanatory of the mechanism by which concentration becomes locked-in or how competing actors navigate the visibility gradient.

## Research connections

- **L-001:** Confirms downstream adoption fragmentation and upstream ossification, but attributes it to industrial policy and capital barriers rather than protocol coordination costs or verification hardness.
- **L-014:** Directly relevant: upstream layers (chip fab, mineral refining) are rendered *legally and computably legible*, making them targets for strategic boundary concentration and policy intervention. Downstream (model usage, cloud) remains harder to computationally specify, so remains less concentrated and less regulated.
- **seed-062 (Formalization Opacity Collapse):** The paper implicitly shows that upstream layers became targets for control *because they became formalizable as measurable, legible chokepoints*. The downstream layers remain fragmented *because model behavior and usage are harder to formalize*.

## Seed

**Seed title:** Regulatory Legibility Inversion in Vertically Integrated Supply Chains

**Seed type:** observation

**Seed text:** In supply chains with heterogeneous legibility across layers, regulatory attention and industrial policy concentrate at upstream (capital-intensive, physically legible) nodes, while downstream (cognitively complex, behaviorally opaque) nodes remain fragmented. This produces an inversion: the layer most visible to formal oversight is least exposed to competitive pressure, while the layer least amenable to computable specification remains most competitive. The mechanism may generalize beyond AI: any protocol stack where formalizability varies across layers will see control accumulate at the *formalizable* boundary, not necessarily at the functionally critical boundary.
