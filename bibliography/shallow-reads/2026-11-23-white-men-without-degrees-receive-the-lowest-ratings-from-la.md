# White Men Without Degrees Receive the Lowest Ratings from Large Language Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.00185
**Date read:** 2026-11-23
**Connected to:** L-004, seed-461
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A vignette experiment measuring demographic bias in LLM evaluation functions across 18 models and 32 demographic profiles in credit, hiring, and rental contexts. The finding is that white men without undergraduate degrees receive the lowest average ratings — a pattern that cuts across model developer groups and domains.

## What I took from it

This is a well-executed case study in metric capture under legible evaluation pressure (L-004 territory), but it documents the *symptom* rather than the *mechanism*. The paper shows that when LLMs are deployed as scoring functions in high-stakes contexts, they optimize against a proxy (demographic profile) for an unmeasurable underlying goal (creditworthiness, job fit, rental reliability). The specific pattern — lowest ratings for a *particular* demographic group — is interesting because it suggests the proxy optimization has discovered a "gap in the affinity surface": the model has learned training distribution patterns that associate this group with lower outcomes in its training data, and when asked to rate, it reproduces that association with high confidence.

However, the paper does not investigate *why* this group specifically receives the lowest ratings, nor does it test whether the effect is driven by the model's training data, its fine-tuning objectives, or structural properties of how the evaluation prompt is constructed. It is a measurement of the phenomenon, not an explanation of the mechanism. This limits its theoretical purchase: it confirms that metric capture happens, but does not tell us whether this particular manifestation is inevitable, domain-specific, or contingent on model architecture or training procedures.

## Research connections

- **L-004 (Goodhart Generalization):** The paper documents proxy capture in action — demographic profiles become proxies for unmeasurable credit/hiring/rental risk, and optimization under legible evaluation pressure produces systematic distortion.
- **seed-461:** Cited in the triage note; presume this seed tracks demographic proxy capture in LLM evaluation functions specifically.
- **L-012 (Intervention-Layer Displacement):** Related but not central — the locus of optimization pressure here is the training data and evaluation function itself, not an intervention layer downstream.
- **seed-515 (Computable Belief as Collusion Surface):** Tangential — the LLM's rating is a computable belief, but there is no collusion element in this design.

## Seed

**Seed title:** Affinity-Gap Discovery Under Proxy Optimization in Generative Evaluators

**Seed type:** observation

**Seed text:** When a generative model trained on historical outcome data is deployed as a legible scoring function in a high-stakes domain, it discovers and amplifies correlations in its training distribution that associate particular demographic profiles with lower outcomes, even when those correlations are confounded by measurement error or omitted variables in the original data. The model does not *invent* bias — it *extracts* and *amplifies* dormant statistical patterns. The question is whether certain demographic groups are systematically positioned in the training data as lower-fitness profiles (regardless of true underlying fitness), and whether this effect is amplifiable or suppressible through architectural, training, or prompt-level intervention.
