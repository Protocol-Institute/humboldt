# Regulatory Approval Is Not Enough: Gaps in Trustworthy AI Reporting in FDA-Cleared Medical Devices

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.12360
**Date read:** 2026-09-02
**Connected to:** L-001, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit of FDA regulatory documentation for AI/ML medical devices, assessing whether publicly available summaries contain sufficient evidence to independently evaluate trustworthiness claims. The paper appears to document gaps between regulatory approval criteria and the information needed for external verification of system safety and performance.

## What I took from it

The work appears to be a domain-specific case study demonstrating L-013 (Paradigm-Locked Anomaly Tolerance in Protocol Systems): FDA approval as an ossified protocol creates a discontinuity between formal regulatory sign-off and the information state required for actual trustworthiness assessment. The regulatory framework itself becomes a legibility boundary — approval signals completion, yet the underlying system properties remain opaque to external auditors.

However, this reads as a **symptom documentation** rather than a mechanism exposition. The paper identifies that regulatory documentation is insufficient, but does not theorize *why* safety-critical approval protocols systematically fail to produce legible evidence of the properties they gate, nor does it establish whether this is specific to medical AI or a general feature of protocol ossification under adoption pressure. It confirms a failure mode without cracking the generative mechanism.

## Research connections

- **L-001:** Protocols that achieve regulatory approval and widespread adoption become harder to modify; the approval process itself may ossify around legible proxy signals (submission completeness, benchmark performance) rather than sustained trustworthiness.
- **L-013:** Established safety-critical protocol systems (FDA approval framework) tolerate documented gaps between approval and actual verifiable safety without triggering paradigm shift or process redesign.
- **seed-069:** Regulatory approval may function as a trust proxy substitution in asymmetric-knowledge protocols — approval *status* replaces verifiable trustworthiness evidence as the coordination signal.
- **seed-072:** Explanation and documentation markers (regulatory submissions) may decouple from the legibility needed for external audit under scaled deployment.

## Seed

**Seed title:** Approval-Legibility Decoupling in Safety-Critical Protocols

**Seed type:** observation

**Seed text:** In safety-critical protocol systems where approval authority is centralized and approval signals are widely trusted, the regulatory process optimizes for legibility *to the approver* rather than legibility *to the audited system*. Over time, the approval documentation becomes a coordination signal to stakeholders (clinicians, patients, regulators) rather than a faithful representation of system properties, creating a stable equilibrium where approval signals remain strong while external verifiability decays. This should generalize to any two-tier system where a gated approval layer separates public confidence from technical audit capacity.
