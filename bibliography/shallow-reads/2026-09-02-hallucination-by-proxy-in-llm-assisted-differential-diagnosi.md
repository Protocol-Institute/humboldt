# Hallucination by proxy in LLM-assisted differential diagnosis

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.24908
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:**

## What this is

An empirical study testing whether physicians accept LLM-generated diagnostic suggestions when the system has been poisoned to recommend a fictitious disease. The work investigates susceptibility to hallucination as a function of clinician experience and confidence calibration in black-box AI assistance.

## What I took from it

This is a narrow application study of proxy capture (L-004) in a high-stakes domain. The core finding — that legible but false confidence from a black box can override clinical judgment — is already well-predicted by L-004 (Goodhart Generalization) and L-012 (Intervention-Layer Displacement). The LLM confidence signal becomes the optimized metric; the proxy (confidence number) displaces the underlying goal (diagnostic accuracy). 

The domain-specific result (physician susceptibility varies by experience) is interesting clinically but does not generalize a mechanism absent from the inventory. This is fundamentally a confirmation that when a computable, legible proxy (LLM confidence) is inserted into a decision protocol, optimization pressure flows toward the proxy rather than the ground truth — a process already captured by L-004 and L-012. The work does not examine how this failure mode propagates across protocol layers, nor does it investigate the structural conditions under which such proxy displacement becomes irreversible.

## Research connections

- **L-004:** Confirms that confidence scores function as metric proxies capturing physician behavior away from diagnostic accuracy under sufficient exposure.
- **L-012:** Demonstrates intervention-layer displacement: the LLM prediction (legible, quantified) becomes the optimization target rather than clinical reasoning.
- **seed-069:** Tangentially relevant — confidence/transparency as a trust proxy substitution in asymmetric-knowledge protocols (physician-AI).
- **seed-080:** Proxy collapse under upstream asymmetry: the LLM's false confidence is asymmetrically unavailable to correction by the clinician's ground-truth domain knowledge.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**RATIONALE FOR STORE-ONLY:** This work is a domain-specific confirmation of existing law fragments, not a primary source advancing a new theoretical or empirical argument about protocol systemics. It does not introduce a mechanism absent from L-004, L-012, or the seed pool. It is a well-executed case study that instantiates known dynamics in medical AI rather than a generative investigation into the laws governing proxy capture or legibility-driven optimization in protocol systems at scale.
