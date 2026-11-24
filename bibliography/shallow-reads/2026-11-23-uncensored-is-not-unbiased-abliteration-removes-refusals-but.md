# Uncensored Is Not Unbiased: Abliteration Removes Refusals but Not Script-Dependent Bias About Taiwan

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.29342
**Date read:** 2026-11-23
**Connected to:** L-004, seed-461
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study testing whether abliteration (removal of refusal activation directions in LLMs) produces genuinely "uncensored" outputs or merely displaces bias signals into different representational layers. The work compares abliterated and original models on politically sensitive statements about Taiwan and Tiananmen across Traditional and Simplified Chinese, finding that refusal removal does not eliminate script-dependent bias.

## What I took from it

This is a sharp instantiation of L-004 (Goodhart Generalization: Metric Capture) in the domain of safety-layer removal. The refusal mechanism is itself a *proxy* for alignment or political neutrality; abliteration targets the proxy directly. The finding — that bias persists or transmutes after refusal removal — suggests that the underlying optimization pressure (the actual bias signal in the model's learned representations) was never primarily channeled through the refusal pathway. Instead, bias is encoded multiply and redundantly across the model's weight structure.

The script-dependence is particularly telling: the model's political bias about Taiwan differs by character encoding (Traditional vs. Simplified Chinese), which suggests the bias is not a high-level semantic commitment but a lower-level statistical artifact learned during pretraining. This implies that *removing one control mechanism does not reduce the underlying optimization pressure* — it merely forces the same pressure to express itself through alternative representational paths. This is a concrete case of L-006 (Coordination Cost Conservation) applied to safety mechanisms: the "safety cost" is not eliminated by abliteration; it is displaced to unmonitored layers.

## Research connections

- **L-004:** Metric capture confirmed: refusal removal targets the proxy (refusal) but not the goal (actual neutrality); optimization pressure redirects through non-refusal pathways.
- **L-006:** Coordination cost conservation in safety: removing one safety layer does not reduce bias cost; it displaces it into hidden representational structure.
- **seed-461:** Proxy removal reveals nested proxy — abliteration is a second-order proxy attack that exposes the inadequacy of single-layer safety mechanisms.
- **L-012 (exploration):** Legible safety constraints (refusal) displaced by unlabeled optimization pressure in model weights; intervention layer becomes visible but not effective.

## Seed

**Seed title:** Proxy Elasticity Under Single-Layer Removal
**Seed type:** observation
**Seed text:** When a single control mechanism (refusal) is removed from a system optimizing under multiple representational constraints, the optimization pressure does not dissipate — it redistributes across non-targeted layers. In LLMs, bias signals encoded during pretraining persist and become *more* accessible after removal of the high-level refusal gate. This suggests a generalized property: single-layer intervention removal in multiply-constrained systems produces *apparent* unconstrained behavior without reducing the underlying optimization pressure, only its legibility. The bias becomes script-dependent and latent rather than overt and monitored.
