# Mapping U.S. Federal AI Governance Against Sector Vulnerability

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.16260
**Date read:** 2026-09-22
**Connected to:** L-001, L-007
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A governance-risk alignment audit mapping 684 federal AI documents against 14 sectors and 24 AI risks, measuring both breadth and depth of coverage and comparing patterns to Delphi-derived sector vulnerability assessments. The work is empirical and sectoral, not a mechanism paper.

## What I took from it

This is a useful empirical calibration of L-001 (Protocol Ossification Under Adoption Pressure) and L-007 (Trust Ratchet in Safety-Critical Protocols) but primarily as a *symptom detector* rather than a mechanism investigator. The paper documents that governance coverage is misaligned with sector risk — which is exactly what ossification and trust ratcheting predict: once a governance protocol begins to stabilize (broad adoption across sectors), it becomes resistant to reallocation toward emerging or heterogeneous risks. The depth-breadth distinction is particularly useful: breadth (frequency) may remain high while depth (substantiveness) may remain shallow for high-vulnerability sectors, which is consistent with L-007's claim that trust accumulates on operational age rather than technical grounding.

However, this is a *mapping study*, not a mechanism study. It shows the outcome (misalignment), not the process by which governance protocols resist sectoral reweighting, nor the conditions under which they would. It tells us where to look for ossification, not how it works.

## Research connections

- **L-001:** Governance frameworks, once adopted across multiple sectors, show resistance to sectoral reweighting — consistent with ossification hypothesis but requires process-level investigation to confirm mechanism.
- **L-007:** Trust in safety-critical governance protocols may accumulate on the basis of longevity and stability of the governance document corpus itself, independent of whether coverage depth matches sector vulnerability — suggests trust ratchet operates on governance process visibility rather than technical validity.
- **seed-131 (Context Legibility as Failure Attribution Boundary):** The misalignment between coverage and vulnerability may reflect a governance legibility floor — sectors with less salient or formalizable risks may be systematically undercovered not due to ossification but due to inability to render risk legible within the governance document protocol.

## Method note

This work demonstrates the value of *protocol-corpus analysis* as an early-warning sensor for mechanism activation. By treating governance documents as a protocol artifact and measuring their structure (breadth/depth, sector allocation, risk taxonomy), the researchers created a legible signal of potential misalignment. However, the paper stops at symptom mapping. Future work should use this as a sampling frame for *protocol resistance testing* — identifying which sectors experience the largest coverage-vulnerability gaps, then investigating whether governance bodies have attempted reallocation and, if so, what mechanisms blocked it. This bridges from audit to mechanism.
