# Recidivism Prediction, Peer Effect Estimation, and Prediction-Powered Inference with LLM Text Measures

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2509.20634
**Date read:** 2026-09-22
**Connected to:** L-004, L-012, seed-146
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study deploying LLM embeddings and zero-shot classification on ~200k text exchanges from correctional facilities to estimate peer effects on recidivism and improve prediction accuracy by ~30% over baseline covariates. The work is methodologically sound but domain-specific: it demonstrates technical feasibility of LLM-derived behavioral measures in a high-stakes prediction context rather than presenting a generalizable mechanism or challenging an existing law.

## What I took from it

The paper instantiates the pipeline flagged in the triage note: formalized text interpretation (LLM embeddings as proxy for behavioral state) → prediction task optimization → deployment in a safety-critical decision context (recidivism assessment). The 30% accuracy gain is achieved by substituting unstructured social signals (written exchanges) with machine-readable embeddings — a direct case of L-004 (Goodhart Generalization) in formation: the proxy (LLM behavioral embedding) correlates with the unmeasurable goal (actual recidivism risk) well *ex post* but will be optimized against by agents aware of the measure. The paper does not discuss whether residents might learn to game the text measures, or whether the embedding stability persists under adversarial or anticipatory behavior modification.

The work also partially instantiates L-012 (Intervention-Layer Displacement): the prediction becomes legible input to judicial/parole decision protocols, shifting optimization pressure from "actual rehabilitation signals" to "text patterns that LLM embeddings weight heavily." This is noted in passing (peer effect estimation requires causal claims about behavioral influence) but not foregrounded as a mechanism risk.

## Research connections

- **L-004:** LLM embeddings are a proxy for unmeasurable behavioral construct (rehabilitation trajectory); accuracy gain under optimization pressure is not tested; metric capture risk is unaddressed.
- **L-012:** LLM text measures become legible input to recidivism-conditional decision protocols (parole, security level); optimization locus may displace from rehabilitation to text-generation patterns.
- **seed-146:** Interpretability formalization (LLM embeddings as interpretable behavioral proxy) enacted as proxy substitution — the embedding *replaces* narrative assessment in the decision chain, not supplements it.

## Seed

**Seed title:** Proxy Embedding Stability Under Legible Deployment

**Seed type:** question

**Seed text:** When unstructured behavioral signals (text, interaction logs) are formalized as machine-readable embeddings and deployed in decision protocols affecting agents who produced the signals, does the embedding's predictive validity persist under anticipatory behavior modification? Specifically: if agents learn that LLM embeddings of their written exchanges influence recidivism assessments, will they generate text optimized for embedding space rather than authentic behavioral expression, and if so, does this degrade the embedding's correlation with ground-truth outcome (actual recidivism)? This generalizes beyond corrections to any domain where LLM-derived behavioral proxies are used in agent-affecting decisions (hiring, lending, welfare eligibility).
