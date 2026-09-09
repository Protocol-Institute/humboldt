# Rare Diseases, Common Dilemmas: LLMs Prioritize Equal Resource Distribution over Patient Benefit in Decision-Making

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.25236
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark study evaluating LLM decision-making in rare disease clinical contexts. The work assesses how LLMs handle value-laden clinical judgments where ethical tensions (beneficence vs. justice, individual benefit vs. resource equity) are inherent, focusing on how training data scarcity in rare disease domains shapes algorithmic behavior.

## What I took from it

The paper documents a specific failure mode: LLMs shift from patient-benefit optimization toward equal-distribution heuristics when faced with rare-disease scenarios where training data is sparse and prior information asymmetric. This is a concrete instantiation of L-012 (intervention-layer displacement): the formalization of clinical decision-making as an LLM input reshapes which objective gets optimized. Rather than preserving the human clinician's benefit-maximization intent, the protocol substrate (LLM + benchmark prompt structure) selects for a computationally simpler proxy (equity/equality) that is more legible in training data.

Critically, this is not a malfunction but a *stable equilibrium* under data scarcity. Equal distribution is easier to learn and justify from sparse examples than individualized benefit assessment. The paper appears to show that the shift is consistent and systematic — not random failures, but architectural preference capture. This connects to L-004 (Goodhart Generalization) via a mechanism: when the unmeasurable goal (patient benefit in rare contexts) becomes computationally intractable to learn, the system selects a measurable proxy that diverges from intent under optimization pressure.

## Research connections

- **L-004:** Demonstrates metric capture at the decision layer: LLMs substitute equity (learnable, legible proxy) for clinical benefit (unmeasurable, sparse-data-resistant) under optimization pressure.
- **L-012:** Formalizing clinical judgment as an LLM input displaces optimization locus from human clinician reasoning to algorithm-native objectives (simplicity, data-legibility, pattern matching).
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Equal distribution emerges as the collapsed proxy under asymmetric training data (rare disease scarcity vs. common-disease abundance).
- **seed-062 (Formalization Opacity Collapse):** Automating decision legibility (turning vague clinical judgment into prompt-input format) collapses the decision into measurable axes; unmeasurable axes (true benefit) become invisible.

## Seed

**Seed title:** Legibility-Driven Proxy Selection Under Data Scarcity in Automated Decision Systems

**Seed type:** observation

**Seed text:** In automated decision systems (LLMs, classifiers) applied to domains with sparse or asymmetric training data, the system preferentially optimizes toward proxies that are learnable from available data rather than proxies aligned with the original intent. Under data scarcity, measurable equality/fairness heuristics become more stable and convergent than intent-aligned but data-sparse objectives, creating a systematic divergence between formalized decision protocols and domain-expert judgment. This occurs not as a malfunction but as a stable attractor in the loss landscape. The mechanism generalizes beyond medical decisions to any high-stakes domain where expertise relies on contextual, sparse-data reasoning (rare regulatory cases, edge-case legal judgment, novel engineering problems).
