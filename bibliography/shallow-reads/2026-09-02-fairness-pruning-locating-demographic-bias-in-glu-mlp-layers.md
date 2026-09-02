# Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential Activations

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.28319
**Date read:** 2026-09-02
**Connected to:** L-004, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical method paper proposing inference-time neuron identification for demographic bias mitigation in LLMs via differential activation analysis on GLU layers. The work is a tool contribution — a localization technique — rather than a primary theoretical or empirical argument about protocol dynamics or generalized laws.

## What I took from it

The paper demonstrates a narrow implementation of bias-as-computable-proxy: it renders a social harm (demographic bias) as a legible, machine-measurable signal (differential activation patterns), then proposes structural intervention at the locus of measurement. This fits cleanly into L-004 (Goodhart Generalization: metric capture) and L-014 (Strategic Boundary Concentration Under Computable Legality) — the work presupposes that bias *can* be localized and pruned at the neuron level, implicitly treating activation differential as a sufficient fairness proxy.

However, the paper does not investigate *why* this proxy succeeds or fails, does not track the long-term drift between the proxy (activation difference) and the target (actual fairness in deployment), and does not examine what optimization pressures emerge once fairness becomes computable at the layer level. It is a competent technical contribution within an existing paradigm (bias detection via differentials) without mechanism discovery or cross-domain generalization.

## Research connections

- **L-004 (Goodhart Generalization):** Fairness pruning exemplifies the conversion of unmeasurable social goal (fairness) into measurable proxy (neuron activation contrast); no evidence yet on whether this proxy sustains under optimization pressure post-deployment.
- **L-014 (Strategic Boundary Concentration):** By rendering bias as computable and legible at the architectural boundary (GLU layers), the method creates a new site for optimization gaming — agents with access to activation patterns may learn to evade detection.
- **seed-073 (Correlated Failure Under Proxy Consensus):** If the differential activation proxy becomes standard in fairness tooling, downstream systems may rely on it as a consensus signal without independent validation, risking coordinated failure.

## Seed

**Seed title:** Proxy Legibility Cascades in Safety-Critical Automation

**Seed type:** motif

**Seed text:** When a harmful or undesirable outcome in automated systems is rendered computationally legible and localized (e.g., as neuron activation patterns, metrics, or threshold violations), it becomes both detectable and—critically—a target for optimization by downstream systems or agents with access to that legibility. The proxy succeeds in detection but may fail in prevention, because the proxy's own legibility creates incentives for circumvention that the original unmeasurable phenomenon did not. This pattern appears to hold across computable enforcement domains: the more precisely a protocol obligation or harm is made machine-readable, the more reliably it becomes a target for evasion rather than a site for genuine mitigation.
