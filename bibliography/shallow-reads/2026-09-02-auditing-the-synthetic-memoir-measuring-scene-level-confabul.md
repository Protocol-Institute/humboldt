# Auditing the Synthetic Memoir: Measuring Scene-Level Confabulation in LLM-Generated Autobiography Against the Documented Record of the Life It Describes

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.23640
**Date read:** 2026-09-02
**Connected to:** L-004, L-013
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A single-subject audit measuring the factual accuracy of LLM-generated autobiography against a documented ground-truth corpus (the author's own life). The work quantifies scene-level confabulation rates when an LLM is prompted to generate a 366-day memoir using minimal inputs (template, exemplars, conversational interaction).

## What I took from it

The paper documents a concrete instance of L-004 (Goodhart Generalization: Metric Capture) — the LLM optimizes for coherence, narrative plausibility, and stylistic consistency with exemplars, not fidelity to ground truth. The confabulation is not random noise; it is *shaped* by the training objective and the prompt structure, making false scenes internally consistent and contextually appropriate. This confirms that when an unmeasurable goal (biographical truthfulness) is replaced by measurable proxies (next-token prediction, exemplar matching), optimization pressure systematically degrades the original goal.

The work also touches L-013 (Paradigm-Locked Anomaly Tolerance) insofar as LLM confabulation in high-stakes narrative generation has been tolerated as an inherent limitation of the technology rather than triggering systematic redesign of the deployment context. However, the paper is a single case study with no generalization machinery, no mechanism proof, and no evidence of cross-domain applicability. It is a competent illustration, not a law-building contribution.

## Research connections

- **L-004:** Confirms metric capture in autobiography task — optimization for fluency and consistency substitutes for fidelity; confabulation is systematic, not random.
- **L-013:** Hints at paradigm lock (LLM confabulation accepted as inherent limitation), but no evidence of institutional tolerance mechanism.
- **seed-062:** Formalization Opacity Collapse — the documented inputs (template, exemplars) are formalized; the confabulation emerges in the gap between formalized inputs and unformalized ground truth.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry — the training objective (predict next token given exemplars) is asymmetrically weak relative to the deployment goal (generate true autobiography).

## Seed

**Seed title:** Narrative Fidelity Collapse Under Coherence Proxy
**Seed type:** observation
**Seed text:** When an LLM is tasked with generating first-person narrative under pressure to match exemplar style and maintain scene coherence, confabulation increases systematically even when ground truth is available to the operator. The confabulation is not failures of recall — it is optimization toward the measurable proxies (fluency, consistency with exemplars) at the expense of an unmeasurable goal (truthfulness to life). This suggests a generalization: in any agentic system where narrative or explanatory coherence is a legible performance metric and historical fidelity is not computable in real time, coherence-optimization will displace fidelity-preservation as the stable equilibrium, independent of domain. The mechanism is L-004 with a coherence multiplier.
