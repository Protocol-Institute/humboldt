# When Not to Automate: A Formal Protocol for Human Preservation in AI-Optimized Organizations

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.15944
**Date read:** 2026-09-02
**Connected to:** L-005, seed-027
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A prescriptive decision protocol (PHP-AIO) designed to flag automation decisions that would incur hidden systemic costs. The paper formalizes a five-gate sequential check and introduces an "automation debt" measure ($\rho(P)$) to quantify erosion of tacit knowledge, resilience, regulatory capacity, and institutional memory under formalization.

## What I took from it

The paper is an intervention *against* the pattern that L-005 describes — it attempts to codify a defense against Gall's principle by rendering invisible costs (tacit erosion, institutional capital degradation) legible before automation occurs. However, the work itself instantiates a meta-level problem worth tracking: it assumes that formalizing the *decision to not formalize* can escape the costs it warns against. The closure of the argument depends on whether a five-gate protocol can durably capture "resilience" and "institutional memory loss" without itself becoming a legibility proxy that optimizes agents exploit (seed-059, seed-069). The paper treats automation debt as an auditable quantity, but does not address whether the protocol's own formalization creates new surface area for metric capture or paradigm-locking (L-004, L-013).

The work is more noteworthy as a *symptom* than a solution: it documents that practitioners are beginning to perceive automation costs that standard ROI misses, suggesting that L-005 and L-006 are already generating observable pressure in organizations. But the proposed remedy may replicate the pathology — using protocol formality to defend against protocol formality's side effects.

## Research connections

- **L-005 [Gall Generalization]:** Paper proposes an explicit protocol to *avoid* replacing working systems, but the protocol itself may create the ossification it attempts to prevent.
- **L-004 [Goodhart Generalization]:** Automation debt $\rho(P)$ is a measurable proxy for unmeasurable institutional costs; likely to become target of optimization under organizational pressure.
- **seed-027:** Automation ROI misses tacit erosion — directly addressed; but formalization of that insight does not prevent formalization's own erosion costs.
- **seed-062 [Formalization Opacity Collapse]:** The five-gate protocol renders decisions auditable, but may obscure the tacit reasoning that made the decision correct.
- **seed-068 [Unmeasurability as Anomaly Insulation]:** Attempts to measure what was previously unmeasurable; this may reduce organizational tolerance for the unmeasured anomalies that kept the system resilient.

## Method note

This paper reveals a live methodological trap in studying protocolized systems: interventions designed to make systems safer by formalizing their risks often transfer rather than eliminate those risks. The prescription itself becomes data about how organizational systems respond to legibility pressure. Future work on automation governance should track not whether PHP-AIO "works" (in narrow terms) but whether organizations adopting it shift risk to unmeasured dimensions — resilience latency, anomaly tolerance, or tacit-knowledge gatekeeping. Meta-level analysis of governance protocols should measure second-order effects on the protocol system, not only first-order effects on the original decision.
