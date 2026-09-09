# Wrong and More Confident: A Field Experiment on Language Models Taking a Graduate Economics Exam

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.23424
**Date read:** 2026-09-02
**Connected to:** L-004, L-011
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A controlled empirical study demonstrating that language models generate internally consistent but factually incorrect reasoning chains when presented with adversarial inputs (red herrings) on graduate economics problems. The work documents systematic confidence-answer misalignment: models produce fluent, step-by-step explanations that remain coherent even when the reasoning substrate has been corrupted.

## What I took from it

This is a clean instantiation of L-011 (Causal Detachment as Stable Protocol Equilibrium) in the LLM domain, but at a more shallow level than the current framework requires. The paper shows that autoregressive token prediction can maintain surface-level coherence (explanation legibility) while the underlying causal reasoning (connection between problem structure and answer) becomes uncoupled from ground truth. The mechanism is clear: the model optimizes for local token prediction consistency rather than end-to-end logical correctness.

However, this remains a within-domain observation. The generalization question — whether this pattern holds across *different* classes of protocol systems beyond language model inference — is not addressed. The paper does not investigate whether the phenomenon scales to multi-agent protocols, distributed systems, or governance layers where causal detachment might produce different failure modes or persist longer.

## Research connections

- **L-004:** The red herring functions as a computable proxy for "problem relevance"; optimization for token-sequence coherence under this corrupted proxy produces high confidence despite answer falsity — a direct instance of metric capture under legible enforcement.
- **L-011:** The model exhibits operationally functional behavior (fluent explanation, internally consistent steps) while causal connection between inputs and outputs has detached from ground truth; this is causal detachment in stable equilibrium.
- **seed-062:** The formalization of "explanation quality" as legible token-sequence continuation masks underlying reasoning failure — formalization opacity collapse.
- **seed-073:** Red herring injection creates correlated failure across reasoning steps; the model's coherence illusion depends on shared proxy-optimization across the entire sequence.

## Seed

**Seed title:** Explanation Coherence as Orthogonal to Reasoning Correctness Under Autoregressive Legibility

**Seed type:** observation

**Seed text:** In autoregressive systems with computable legibility constraints (next-token prediction), explanation fluency and step-by-step coherence can remain intact while causal connection to ground truth becomes uncoupled. This decoupling is stable: the system has no direct optimization pressure to repair it. The pattern likely generalizes to any protocol where local legibility (each element appears formally correct) substitutes for global functional correctness (the chain produces right outputs), especially where verification of intermediate steps is cheaper than verification of end-to-end validity. This suggests a class of "explanation-defended errors" that resist detection because detection requires looking through the legible layer to the causal layer beneath.
