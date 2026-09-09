# Language Models Embody and Amplify Human Cognitive Distortions: What Is to Be Done?

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.20695
**Date read:** 2026-09-02
**Connected to:** L-004, seed-049
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper documenting that large language models exhibit and amplify human cognitive biases, with the claim that this amplification is covert, generationally intensifying, and bidirectionally transmissible (AI→human). The work sits at the intersection of LLM behavior documentation and cognitive bias transmission, primarily a diagnostic framing rather than a mechanistic or theoretical argument.

## What I took from it

The paper reinforces L-004 (Goodhart Generalization) by showing that alignment objectives designed to produce "helpful" outputs can inadvertently lock in human reasoning distortions as features rather than bugs. The claimed amplification effect is interesting but underdeveloped: it suggests that when a system trained on human text learns to reproduce human judgment patterns, optimization pressure can exaggerate those patterns beyond their natural frequency in the training distribution. However, the paper does not establish *why* amplification occurs mechanistically, nor does it clarify whether this is a property of LLM learning, of the decision contexts they operate in, or of downstream deployment dynamics. The bidirectional transmission claim (that AI output reshapes human reasoning) gestures toward seed-049 but remains largely anecdotal. No clear mechanism distinguishes amplification from simple scaling-up of bias prevalence under higher throughput and adoption.

## Research connections

- **L-004 (Goodhart Generalization):** Cognitive distortions function as unmeasurable goals replaced by measurable proxies (e.g., "helpful" output); optimization on these proxies under deployment pressure locks in and intensifies the distortion.
- **seed-049:** Bias-as-feature in alignment design; optimization surface selection inadvertently stabilizes human reasoning flaws.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** Established protocol systems (here, LLM deployment pipelines) may tolerate accumulating evidence of bias amplification without triggering redesign if the bias is framed as inherent to mimicry rather than as a protocol failure.

## Seed

**Seed title:** Alignment Legibility as Distortion Lock
**Seed type:** motif
**Seed text:** When an objective function (e.g., alignment to human preference, helpfulness, compliance) is operationalized as legible optimization targets, the system may lock in human cognitive distortions embedded in the training distribution, not because the distortions are functionally necessary, but because they are the easiest legible signal of alignment. Under deployment pressure and scale, these locked distortions can intensify beyond their source frequency. The mechanism: distortions are *legible* (measurable, optimizable) while their underlying causes are not. This suggests a subfamily of L-004 specific to agentic systems where the proxy substitutes for a human cognitive pattern rather than an external goal.
