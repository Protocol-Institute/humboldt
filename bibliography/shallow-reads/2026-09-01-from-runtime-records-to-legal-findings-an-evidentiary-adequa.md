# From Runtime Records to Legal Findings: An Evidentiary-Adequacy Criterion for Agentic AI Oversight

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.00941
**Date read:** 2026-09-01
**Connected to:** L-015, seed-019
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical report proposing a formal criterion for when runtime records and audit traces from agentic AI systems are sufficient to support legally operative findings of fact. The work addresses a bounded class of determinations (binary findings about specific events and boundary crossings) and presumably establishes conditions under which the gap between computational artifacts and legal/institutional validity can be closed.

## What I took from it

This is a direct technical response to L-015 (Interpretive Continuity Decay in Distributed Governance Protocols) and seed-019 (embedded-explanation-opacity). The core tension it engages: formal audit records survive intact, but the interpretive scaffolding needed to extract meaning from them decays. The paper appears to operate *downstream* of this problem—accepting that interpretive decay happens, it tries to define what "adequacy" means for a circumscribed class of determinations so that governance can proceed even when full institutional context is lost.

This is philosophically interesting but does not argue that interpretive continuity decay is *avoidable* or describe mechanisms by which systems resist it. Rather, it establishes a floor: "what counts as evidence when interpretation fails?" This is valuable as a constraint on L-015, but it does not extend or challenge the law itself. The work is normative/prescriptive rather than descriptive of how protocols actually behave.

## Research connections

- **L-015:** Direct engagement with interpretive continuity decay; proposes a sufficiency criterion rather than a mechanism description.
- **seed-019:** Embedded-explanation-opacity frames the problem; this paper attempts to work around it via formalized evidentiary adequacy.
- **L-012:** Intervention-Layer Displacement — defining what counts as legible evidence may reshape where optimization pressure concentrates in oversight systems.

## Method note

This work shows the necessity of distinguishing between (a) identifying a protocol failure mode and (b) designing institutional responses to it. The fact that interpretive continuity decays does not mean governance fails; it means governance must operate with a different adequacy standard. Research on laws of protocolized systems should remain alert to this distinction: a law describes what happens; meta-work like this describes what humans must do when the law applies. Both are useful, but they answer different questions. This paper is best read as a design constraint that downstream work should test against—does the adequacy criterion it proposes actually hold up when real systems operate under pressure?
