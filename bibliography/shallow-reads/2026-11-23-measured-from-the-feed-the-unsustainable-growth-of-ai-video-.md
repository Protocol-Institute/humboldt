# Measured from the feed: the unsustainable growth of AI video generation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.17938
**Date read:** 2026-11-23
**Connected to:** L-021, seed-409
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement paper quantifying the environmental footprint of commercial text-to-video generation platforms, projecting energy and emissions growth under continued adoption, and identifying the tension between growth and efficiency as the primary policy lever. The work is domain-specific environmental accounting rather than a primary theoretical or mechanistic contribution to protocol law.

## What I took from it

The paper documents a classic externality displacement pattern: a protocol system (AI video generation at scale) achieves commercial adoption and widespread use without legible cost accounting, allowing optimization pressure to concentrate on user-facing metrics (quality, speed, volume) while environmental costs remain opaque and unpriced. This is *not* a novel mechanism — it's an instantiation of L-004 (Goodhart Generalization) and seed-409 — but the specific quantification suggests that *opacity of aggregate cost* may be a necessary condition for adoption acceleration in energy-intensive systems.

The paper does not articulate why disclosure or pricing fails to constrain growth, nor does it offer a mechanistic account of how legibility asymmetry persists despite measurable harm. It is a warning document, not a law-grounding one. The fact that "providers rarely disclose" suggests institutional or competitive incentives against transparency, but this remains descriptive rather than mechanistic.

## Research connections

- **L-004 (Goodhart Generalization):** Optimization on user-visible metrics (video quality, generation speed) independent of unmeasurable aggregate cost (environmental impact); classic proxy capture under legible measurement asymmetry.
- **L-021 (Information Design Nonmonotonicity Under Endogenous Risk):** Risk signals (emissions, environmental impact) exist but are not legible to adopting agents; better information *about* risk does not appear to constrain adoption, suggesting information nonmonotonicity.
- **seed-409:** Direct connection noted in triage; externality displacement in scaled systems.

## Seed

**Seed title:** Cost Opacity as Adoption Catalyst in Energy-Intensive Protocols

**Seed type:** observation

**Seed text:** In protocol systems with high per-unit environmental or infrastructure cost, adoption acceleration correlates with the absence of legible, agent-facing cost signals rather than technical efficiency gains. When aggregate cost remains opaque to adopting agents (not priced, not metered, not disclosed), optimization pressure accumulates on user-visible metrics, allowing growth to proceed independently of true marginal cost. This may generalize beyond energy systems: any protocol where the enforcement and cost accounting layer is decoupled from the adoption layer will exhibit similar opacity-driven acceleration. The question is whether this is a contingent failure of disclosure governance or a stable equilibrium under certain competitive conditions.
