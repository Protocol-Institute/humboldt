# Cross-Task Dissociation in Frontier Vision-Language Model Theory of Mind

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.00261
**Date read:** 2026-09-02
**Connected to:** L-011, seed-019
**Kind:** empirical observation / benchmark
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark study evaluating nine frontier vision-language models on two psychology-derived theory-of-mind tasks (Keysar Director Task, Frith-Happé animated triangles). The work documents task-specific performance fragmentation: VLMs show coherent capability profiles within single task paradigms but diverge substantially across paradigms, suggesting no unified ToM capacity.

## What I took from it

The paper provides clean empirical documentation of a phenomenon L-011 (Causal Detachment as Stable Protocol Equilibrium) predicted: operationally functional configurations that lack causal coherence across task domains remain stable. VLMs achieve high performance within each task's localized inference space without integrating toward a unified representational model. This is *not* a failure to generalize — it's successful task-specific optimization that leaves cross-task coherence unsolved.

However, the study is fundamentally a benchmark paper, not a theoretical or mechanistic exploration. It documents the fragmentation but does not investigate *why* it persists, what architectural or training conditions sustain it, or whether the pattern generalizes beyond vision-language models to other multimodal or multi-task agentic systems. The triage note linking it to L-011 is apt, but the paper itself does not advance the causal or mechanistic understanding of when causal detachment becomes a stable equilibrium versus a temporary training artifact.

## Research connections

- **L-011:** Empirical confirmation that operationally functional configurations in multimodal systems can sustain cross-task incoherence without degradation. Does not explain the mechanism.
- **seed-019:** The fragmentation across task paradigms is consistent with latent-state coupling decoupling, but the paper provides no access to internal representations or training dynamics.
- **seed-063 (Latent-State Coupling as Silent Protocol Violation):** VLM task dissociation may be a case of silent latent misalignment—systems maintain local validity while upstream causal structure diverges.

## Seed

**Seed title:** Task-Domain Causal Opacity as Optimization Attractor

**Seed type:** observation → question

**Seed text:** In multimodal or multi-task systems optimized for legible task-specific performance, cross-domain causal coherence decays without penalizing within-domain accuracy. Systems that achieve high task performance while maintaining structural incoherence across domains suggest that causal integration may not be a natural convergence target under local task loss functions. This raises the question: is cross-task coherence actively suppressed by task-specific optimization, or merely unselected? And does this pattern hold in other protocol-driven multiagent or multimodal systems where performance is measured within task-local scopes?
