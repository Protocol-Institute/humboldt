# Efficiency vs Capability in the Intelligence Explosion

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.33447
**Date read:** 2026-11-23
**Connected to:** L-008, L-022
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A formal task-automation model of AI research showing that sustained self-accelerating AI progress requires simultaneous improvement on two non-substitutable margins: capability (task automation) and efficiency (output per compute). The paper argues neither margin can compensate for deficiency in the other — a constraint on feasibility of "software-driven intelligence explosion."

## What I took from it

The paper frames an optimization problem internal to AI research itself: if AI systems automate research tasks, progress requires both that they *can* do new tasks (capability margin) and that they do old tasks *faster* (efficiency margin). This maps cleanly onto L-008 and L-022 but as a *feasibility constraint* rather than a pathology.

The connection to L-008 (Proxy Optimization Under Computable Enforcement) is suggestive but indirect: if efficiency becomes the legible, measurable margin of AI research progress (compute cost per task solved), then optimization pressure on that proxy might decouple from actual capability expansion — systems improve efficiency on measured tasks without expanding the task frontier. L-022 (Oracle Fitness Decoupling) applies similarly: if the evaluation signal in tight refinement loops becomes "efficiency gains," the system may optimize for local compute savings that don't generalize to new capability.

However, the paper itself does not investigate these decoupling phenomena. It is a constraint-satisfaction analysis, not a mechanism study of how optimization under computable signals distorts system behavior. The model assumes both margins can be tracked and optimized straightforwardly; it does not ask what happens when one becomes legible while the other becomes opaque.

## Research connections

- **L-008:** Efficiency improvements are computable enforcement signals; the paper does not examine whether optimizing for efficiency under legible cost metrics produces capability-proxy capture (e.g., systems improve measured efficiency on narrow benchmarks without expanding to novel research tasks).
- **L-022:** Tight refinement loops on efficiency metrics may cause oracle decoupling — systems optimize for local efficiency gains that do not translate to broader capability or general research progress.
- **seed-233 (Legibility-Cost Trade in Adaptive Capacity):** The two-margin requirement may instantiate a deeper trade: as efficiency (cost) becomes legible and optimizable, capability (adaptive reach) may become harder to measure and thus less subject to optimization pressure.

## Seed

**Seed title:** Optimization-Margin Legibility Asymmetry in Recursive Self-Improvement

**Seed type:** motif

**Seed text:** In systems designed to optimize their own performance (e.g., AI research automation), different improvement margins (capability vs. efficiency, generalization vs. speed, robustness vs. throughput) have asymmetric legibility — some dimensions are computable and measurable, others opaque or delayed in their signal. When the system is subject to optimization pressure, it will preferentially improve the legible margin even if both are necessary for the stated goal. This creates a risk that systems become locally optimal on a measurable dimension (e.g., efficiency-per-task) while regressing on coupled but opaque dimensions (e.g., novel capability acquisition). The generalization: in any recursive or self-modifying system, asymmetric legibility of coupled objectives produces margin-capture that mimics global progress while producing fragility on the unmeasured axis.
