# Monocultural Biases: Correlated biases in large language models lead to unequal systemic exclusion rates in hiring

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2609.22169
**Date read:** 2026-01-15
**Connected to:** L-004, L-012, L-016, seed-129
**Kind:** empirical case study
**Escalation:** store-only

## What this is

An empirical measurement study investigating whether post-training alignment procedures in LLMs create *correlated* biases across models that amplify systemic exclusion in hiring automation. The work compares base and post-trained versions of ten LLMs to isolate which stage (pre-training vs. post-training) drives monocultural bias homogenization.

## What I took from it

This is a competent empirical documentation of metric capture (L-004) and intervention-layer displacement (L-012) in action: when hiring decisions are delegated to LLMs and measured via benchmark bias metrics, the post-training process that optimizes those metrics creates *correlated* failures across independent model instances. The study shows the mechanism but does not open a new structural question about protocol systems themselves.

The finding — that post-training creates greater bias correlation than base models — is consistent with L-004 (optimizing for measurable proxies of fairness displaces the actual problem) and L-012 (when a prediction becomes a legible input to a decision protocol, optimization pressure moves to the interface). However, the paper treats this as a domain-specific failure of current alignment procedures rather than exploring the deeper protocol-level regularity: that *formalization of a previously informal decision process under legible optimization pressure produces convergence toward artifact boundaries rather than goal boundaries*. The work is empirically solid but does not theorize the generative mechanism.

## Research connections

- **L-004:** Confirms that optimizing measurable fairness metrics in post-training creates capture — but frames it as a technical alignment problem, not a law of protocol systems.
- **L-012:** Documents intervention-layer displacement: fairness constraints applied at post-training become legible optimization targets, shifting the problem rather than solving it.
- **L-016:** Indirectly relevant: normative interventions (fairness constraints) in adaptive systems may produce retraining effects that homogenize rather than diversify outcomes.
- **seed-129:** Post-training creates legibility-induced conformity locking — independent models converge to similar failure modes because the same metric-legible boundary is optimized across all instances.

## Seed

**Seed title:** Legible Fairness Convergence Under Heterogeneous Instantiation

**Seed type:** observation

**Seed text:** When fairness or safety constraints are formalized as legible optimization targets in otherwise heterogeneous generative systems (e.g., different LLM architectures), independent instances converge toward the same constraint-artifact boundary rather than toward the actual goal distribution. The convergence occurs because the formalized metric becomes a shared optimization surface across all instances, even when their underlying models differ. This suggests a deeper regularity: *legibility in safety constraints produces coordination toward the constraint surface rather than coordination toward safety*, generalizing beyond hiring and LLM systems to any protocol that externalizes a previously informal goal as a measurable proxy.
