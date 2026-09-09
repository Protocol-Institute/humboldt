# Engineering Trustworthy Agentic AI for Critical Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.18548
**Date read:** 2026-09-02
**Connected to:** L-002, L-007, seed-019
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A survey paper treating trustworthiness (verifiability, auditability, operability under engineering constraints) as a first-class engineering property in agentic AI systems deployed in critical domains. The work repositions the evaluation frame from task capability to trust-under-constraint, bridging AI capability literature with safety and verification practices.

## What I took from it

This is methodologically important for framing but does not present a sustained theoretical argument or novel mechanism. It confirms the *framing problem*: that trustworthiness is often treated as downstream to capability rather than as a design constraint. This aligns with L-007 (Trust Ratchet) and the broader ossification family — it suggests that trust accumulation in safety-critical protocols depends on operational stability and auditability, not on theoretical guarantees. However, the paper appears to be a survey organizing existing work rather than introducing mechanisms absent from the current inventory.

The connection to L-002 (Hardness Asymmetry) may be implicit: verification of agentic behavior in critical systems is likely to be costlier than execution, but the paper would need to substantiate this asymmetry empirically in agentic domains for it to strengthen that law. The emphasis on "constraints that engineering practice actually requires" suggests awareness of the gap between formal guarantees and operational reality—a recurring theme in protocol ossification.

## Research connections

- **L-002:** Verification cost may exceed execution cost in agentic systems; this would need case evidence.
- **L-007:** Trust in safety-critical agentic systems likely accumulates through operational age and auditability rather than theoretical certification.
- **seed-064:** Infrastructure-Trust Decoupling — agentic autonomy may decouple from the trust substrate that enables deployment.
- **seed-072:** Explanation-Marker Decoupling — the paper's emphasis on "explanation opacity management" suggests explainability claims may diverge from actual causal legibility.

## Method note

This work highlights a methodological norm worth examining: capability benchmarks dominate AI systems research, while trustworthiness (verification, auditability, failure modes under operational stress) remains a second-order concern. For protocol systems research, this suggests the need to invert evaluation order: ask *first* what makes a system auditable and trustworthy under real constraints, *then* what capabilities can be safely deployed within that envelope. Meta-research should track whether trustworthiness frameworks in critical agentic systems follow the ossification and formalization patterns already observed in non-AI protocols, or whether agentic properties (opacity, learned coupling, causal detachment) introduce novel resistance patterns to auditability.
