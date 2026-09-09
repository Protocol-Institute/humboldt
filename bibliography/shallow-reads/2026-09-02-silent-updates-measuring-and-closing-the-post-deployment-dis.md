# Silent Updates: Measuring and Closing the Post-Deployment Disclosure Gap

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.11803
**Date read:** 2026-09-02
**Connected to:** L-001, L-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement paper documenting the prevalence and mechanisms of undisclosed post-deployment modifications to deployed foundation models. The work catalogs silent update pathways (fine-tuning, prompt revision, retrieval/routing changes) and frames this as a governance failure in audit and chain-of-custody protocols for AI systems.

## What I took from it

This is a tight empirical observation within a well-understood problem space: versioning and transparency in deployed systems. The paper anchors L-015 (interpretive continuity decay) with a concrete mechanism — silent updates create documentary discontinuity even when operational continuity remains — but the causal story is already mapped by existing inventory. The governance failure it documents is a *symptom* of ossification (L-001): once a model achieves adoption, the friction of re-evaluation and public versioning creates incentive pressure toward silent modification. The paper does not theorize this pressure or measure the conditions under which it intensifies; it documents that it occurs.

The work is competent within its frame but does not generalize beyond deployed AI systems or produce mechanism-level insight into why protocol systems systematically decouple documentation from operation. It confirms rather than extends.

## Research connections

- **L-001:** Silent updates are a behavioral consequence of ossification — the friction of formal re-evaluation incentivizes undisclosed modification. Supports but does not extend the law.
- **L-015:** Direct instantiation — formal records (system cards, evaluation reports) survive intact while operational configuration drifts. Illustrative but not mechanistic.
- **seed-062:** Formalization Opacity Collapse — System cards formalize governance intent, but silent updates create an opacity layer *within* the formalized system. Weak connection; the seed concerns loss of clarity under automation, not deliberate non-disclosure.

## Seed

**Seed title:** none

The paper documents behavior (silent updates as rational under governance friction) but does not identify a generalizable regularity about *when* or *why* documentation-operation decoupling becomes stable equilibrium across protocol types, nor does it propose a mechanism that would travel beyond versioned software systems. Store as confirmatory data point for L-001 and L-015 rather than source for new induction.
