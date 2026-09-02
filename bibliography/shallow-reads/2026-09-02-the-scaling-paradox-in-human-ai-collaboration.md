# The Scaling Paradox in Human-AI Collaboration

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.00818
**Date read:** 2026-09-02
**Connected to:** L-012, L-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An analytical modeling paper examining whether empirical scaling laws in AI systems (improved capability with scale) transfer to human-AI joint performance. The work appears to identify a decoupling between isolated AI capability gains and collaborative system utility, with implications for deployment assumptions.

## What I took from it

The paper targets a genuine empirical puzzle in protocolized human-AI systems: scaling benefits that are robust at the single-agent level vanish or invert when humans must integrate, interpret, or act on AI outputs. This sits squarely on L-012 (Intervention-Layer Displacement) — as AI predictions become more legible and formally integrated into human decision protocols, the optimization pressure may shift away from prediction accuracy toward factors that make the human-AI boundary itself manageable (interpretability, latency, coordination overhead, deferral patterns).

The abstract hints that the model demonstrates *when* gains persist and when they don't, which suggests the paper identifies boundary conditions rather than a universal inversion. This is valuable for the exploration line: it suggests scaling decoupling is not axiomaticbut conditional on protocol structure, agent composition, or information asymmetry in the human-AI loop. However, the shallow read cannot yet confirm whether the mechanism identified is novel (absent from L-012 elaboration) or whether it generalizes beyond human-AI contexts to other human-automation or multi-agent protocol boundaries.

## Research connections

- **L-012:** Core candidate mechanism — optimization pressure shifts from prediction quality to coordination-layer properties (interpretability, latency, control authority) when predictions become formalized inputs to joint decision protocols.
- **seed-069:** Transparency and legibility may substitute for trust in asymmetric-knowledge protocols; scaling AI capability may improve legibility but degrade the trust-substitution equilibrium.
- **seed-072:** Possible candidate for explanation-marker decoupling — as AI systems scale, their outputs become more legible to metrics but explanations decouple from human actionability.

## Seed

**Seed title:** Capability-Coordination Inversion in Scaled Collaborative Protocols

**Seed type:** motif

**Seed text:** In human-AI collaborative protocols, isolated capability scaling (measured on held-out test sets or single-agent benchmarks) may decouple from or invert joint system performance when human agents must interpret, integrate, or defer to AI outputs. The decoupling is sharper when: (a) the human decision boundary is formalized as a protocol with legible AI inputs; (b) human interpretability costs scale sublinearly with AI capability; or (c) coordination overhead (latency, disagreement, authority negotiation) is not metrically captured in capability measures. This suggests that scaling laws are protocol-relative, not capability-absolute — a system may be simultaneously "more capable" and "worse at coordination" under the same capability scale.
