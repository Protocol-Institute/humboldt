# Measuring AI harms with multidimensional Lorenz Zonoids

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.16004
**Date read:** 2026-09-22
**Connected to:** L-004, seed-132
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper proposing Lorenz Zonoids as a tool for measuring multidimensional AI harms in governance contexts. The work argues that existing risk management frameworks collapse ordinal, multidimensional harm data into univariate metrics, rendering governance protocols "compliance-driven and provider-centric" rather than harm-centered. Lorenz Zonoids are presented as a mathematical framework capable of preserving dimensional structure while enabling severity-weighted aggregation.

## What I took from it

The paper diagnoses a real compression problem: governance protocols that require legible, actionable risk signals systematically discard the dimensional structure of harm data to produce scalar compliance metrics. This creates the conditions for metric capture (L-004) — optimizing agents can satisfy formal governance signals while harm remains unequally distributed across dimensions.

However, the paper's solution — introducing a more dimensionally-faithful measurement apparatus — risks a category error. It treats metric capture as *solvable by better metrics* rather than as a *structural consequence of protocol formalization*. The paper does not engage with whether Lorenz Zonoids, once formalized into governance protocols, would themselves become optimization targets, undergo gradient-following deflection, or enable new forms of dimensional gaming. It assumes measurement fidelity is the bottleneck; the research context suggests *legibility itself* is the problem. A governance protocol using Lorenz Zonoids would still need to render them actionable to agents and enforcers — at which point the capture cycle restarts at a higher dimensional complexity.

## Research connections

- **L-004 (Goodhart Generalization):** Correctly identifies metric collapse as capture risk, but proposes dimensional fidelity rather than engaging with the formalization ratchet (L-003) that governs whether richer metrics remain interpretable under adoption pressure.
- **seed-132 (Synthetic Adversary Metric Faithfulness Collapse):** The Lorenz Zonoid framing assumes faithfulness can be preserved under strategic optimization; seed-132 suggests this is not mechanically true — dimensionality increase may accelerate collapse under computable enforcement (L-008).
- **L-003 (The Formalization Ratchet):** The paper does not address whether multidimensional Lorenz Zonoids, under stress or scaling pressure, would themselves formalize into simpler proxies — and whether the dimensional fidelity gained at design time would degrade under operational pressure.

## Seed

**Seed title:** Dimensional Fidelity Decay Under Formalized Governance

**Seed type:** question

**Seed text:** When a measurement apparatus designed to preserve dimensional structure (e.g., Lorenz Zonoids) is formalized into a protocol for governance or allocation, does dimensional fidelity degrade monotonically as a function of (a) adoption scale, (b) need for real-time legibility, or (c) strategic optimization pressure? Or do richer dimensional frameworks create new gaming surfaces rather than reducing capture risk? This suggests a distinction between *measurement fidelity at design time* and *protocol interpretability under adoption* — and implies that metric capture may be unsolvable by dimensional multiplication alone.
