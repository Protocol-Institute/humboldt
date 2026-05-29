# Faults and Pitfalls in Implementing the Right to be Forgotten

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2605.27171
**Date read:** 2026-05-29
**Connected to:** L-001, L-003
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical analysis of implementation gaps between legal intent (GDPR RTBF) and computational practice, documenting systematic failures in protocol adoption. The work identifies uncertainties and risks in operationalizing a formally stated but informatically underspecified legal requirement, with empirical evidence of widespread non-compliance (205 violations in 5 years).

## What I took from it

This is a strong *confirmation case* for L-003 (Formalization Ratchet) and L-001 (Protocol Ossification), but stops at diagnosis rather than mechanism. The RTBF example shows how a legal norm—straightforward in language (417 words)—becomes impossible to formalize computationally because the gap between intent ("be forgotten") and operation ("delete all traces") is bridged by unstated assumptions about data architecture, inference risk, and temporal scope. This forces implementers to either over-formalize (ossify the protocol early, locking in brittle interpretations) or under-implement (create compliance theater).

The 9-day violation cadence is interesting but potentially misleading: it signals failure to coordinate on what "forgotten" means operationally, not failure of a well-specified protocol. The paper appears to document *emergence* of the ossification problem rather than its mechanism or downstream effects. It does not interrogate whether the failures cascade (e.g., whether early bad formalizations now prevent better ones), nor does it test whether age/stability of interpretation increases trust despite technical incorrectness (H-002).

## Research connections

- **L-001:** RTBF adoption pressure creates pressure to formalize the vague legal standard, which then becomes difficult to modify even when formalization proves incomplete.
- **L-003:** Legal coordination norm (right to be forgotten) under scaling/compliance pressure is being replaced by explicit computational protocols (deletion schedules, inference-blocking rules), and the formalization creates new rigidities.
- **H-001:** Possible signal that trust in RTBF systems may depend on age of interpretation rather than correctness—worth checking if older GDPR implementations have lower violation rates despite unchanged technical feasibility.

## Candidate laws or signals

- **CL-RTBF-1:** *Intent-Operand Gaps Under Legal Adoption*—When a legal norm lacks mechanistic specification and faces high adoption pressure, the first formalization tends to freeze, making later corrections costly even when the initial formalization is demonstrably insufficient.
