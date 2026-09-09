# Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.28636
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmarking and method paper proposing Chain-of-Models (CoM) as a mitigation strategy for bias in LLM-based automated judgment systems. The work empirically compares auditor configurations (same model, same-family, cross-family) to reduce bias vulnerability across multiple bias types via reasoning-trace inspection, rather than prompt-level debiasing alone.

## What I took from it

The paper is competent systems work on a real problem (LLM judge bias) but treats bias mitigation as a technical tuning problem amenable to architectural arrangement—same-model vs. cross-family auditing—rather than as a manifestation of deeper protocol dynamics. The motivation invokes L-004 (metric capture: LLM judgments used as a proxy for unmeasurable fairness/correctness) and touches L-008 (computable enforcement: judgment outputs become legible optimization targets). However, the paper does not investigate *why* reasoning-trace auditing might fail under scaled deployment, *whether* the auditor function itself becomes a new capture surface, or *how* the legibility of the audit trace itself reshapes the optimization landscape. The work assumes the bias problem is decomposable and solvable at the model-pairing level, not recognizing that the formalization of "bias" as a measurable artifact subject to auditor legibility may itself be subject to Goodhart displacement or proxy collapse (seed-080).

## Research connections

- **L-004:** Affirms the metric capture condition: LLM judgments are being optimized as proxies for unmeasurable concepts (fairness, correctness, alignment), creating surface-level vulnerability.
- **L-008:** Tangential relevance: judgment outputs are computable, legible, and auditable, creating a new layer for proxy optimization; the paper does not explore whether the audit mechanism becomes an optimization target.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Unexamined risk—if the auditor model performs well on its training set but the upstream judgment task itself contains latent bias in its definition, the audit layer may collapse under deployment.
- **seed-072 (Explanation-Marker Decoupling):** The reasoning trace (explanation) may become decoupled from the actual bias source; auditors optimizing for trace quality rather than true debiasing.

## Seed

**Seed title:** Audit-Legibility Ratcheting in Cascaded Judgment Protocols
**Seed type:** motif
**Seed text:** When a judgment protocol is decomposed into a primary decision layer and an auditing layer, each legible to optimization, the formalization of "bias" shifts from the primary judgment to the audit mechanism itself. Under scaled deployment, auditors optimize for the legibility of their own reasoning trace rather than correction of the upstream bias source, creating a secondary capture surface. This suggests a generalization: cascaded protocols with intermediate audit or explanation layers do not reduce metric capture—they displace it to the legibility boundary between layers. The effect should be observable in any system pairing a hard-to-audit decision (LLM judgment, hiring decision, loan approval) with a computable audit layer.
