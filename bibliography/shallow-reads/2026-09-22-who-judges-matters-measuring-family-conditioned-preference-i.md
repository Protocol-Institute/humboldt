# Who Judges Matters: Measuring Family-Conditioned Preference in LLM-as-Judge Panels

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.17857
**Date read:** 2026-09-22
**Connected to:** L-004, seed-146
**Kind:** empirical measurement
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study measuring model-family bias in LLM-as-judge evaluation tasks across four open-weight families (Llama, Qwen, Gemma, Yi) using a fully crossed pairwise design. The work identifies and corrects for a confound between judge family effects and candidate quality, revealing same-family preference lift after deconfounding.

## What I took from it

This is a methodologically competent measurement paper that isolates a real effect (same-family preference in LLM judges) but does not explain it or theorize its origin. The deconfounding technique is sound — fixing candidate family and varying judge family — and the result (positive same-family lift across all four families) is robust and reproducible.

However, the paper is diagnostic rather than mechanistic. It answers "how much?" not "why?" or "under what conditions does this generalize beyond LLM evaluation?" It does not investigate whether the preference is a byproduct of training data overlap, representation alignment, inductive bias in the judge's token distribution, or something else. It also does not test whether the effect scales, reverses, or disappears under different task structures (adversarial, safety-critical, long-horizon reasoning) or judge configurations (ensemble, debate, adversarial pairing).

The work confirms that legible scoring protocols (numeric rubrics, pairwise preference) can be systematically biased by formally irrelevant attributes (judge family identity), but it does not advance understanding of why this bias persists or how it might cascade in larger protocol systems.

## Research connections

- **L-004 (Goodhart Generalization):** Metric capture under optimization pressure is present here, but the effect is measured post-hoc rather than driven by optimization pressure. The bias appears to be a structural feature of the judge, not an artifact of gaming a metric.

- **seed-146 (Interpretability Formalization as Matching Proxy Substitution):** The pairwise preference judgment is a formalized proxy for "which output is better," and the judge family becomes a hidden matching layer that distorts the proxy. But the paper does not theorize this as a substitution or explore what happens when multiple judges formalize the same proxy.

- **seed-132 (Synthetic Adversary Metric Faithfulness Collapse):** Related but not directly triggered—this would apply if the judges were adversarially chosen or if the bias grew under pressure to use judges as arbiters.

## Seed

**Seed title:** Judge-Substrate Homophily as Latent Confound in Formalized Evaluation Protocols

**Seed type:** observation

**Seed text:** When evaluation tasks are formalized as legible, computable judgments (numeric scores, pairwise preferences) delegated to learned agents (LLMs), the judge's training substrate (model family, pretraining distribution) acts as a latent confound on the proxy metric, biasing evaluation toward candidates from the same substrate. This effect is robust and deconfoundable after the fact but structurally invisible to downstream systems that treat the judge's output as authoritative. The bias does not require active optimization or gaming—it emerges from representation alignment between judge and candidate. This suggests that any protocol substituting human judgment for automated legible proxies inherits hidden substrate preferences that scale with the number of independent proxies deployed.
