# Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.05402
**Date read:** 2026-09-01
**Connected to:** L-004, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A case study applying EU AI Act compliance frameworks to two medical risk prediction systems (work disability, Alzheimer's disease). The paper observes that both systems are classified as high-risk under the Act and identifies tensions between research-stage development and regulatory deployment requirements.

## What I took from it

The paper documents a compliance-legibility mismatch: medical prediction systems become subject to precise, machine-readable legal obligations (explainability, bias auditing, documentation) once classified as high-risk, but the legalization does not resolve the upstream scientific problem of what the prediction proxy actually measures or whether it should be actionable at all.

This is a live instance of L-014 (computable legality driving boundary concentration), but the paper does not theorize the generative mechanism: it does not ask whether making the legal obligation machine-readable shifts optimization pressure away from medical validity toward regulatory checkbox completion. The work also touches L-004 (metric capture) but treats it as a compliance problem rather than exploring whether proxy optimization accelerates once enforcement becomes computable. The paper remains within case study framing and does not abstract to a pattern claim.

## Research connections

- **L-004:** Proxy optimization in medical risk prediction; unclear whether the paper examines how optimization pressure changes once the prediction task becomes subject to computable regulatory enforcement.
- **L-014:** Strategic boundary concentration; EU AI Act creates legible, machine-checkable boundaries (high-risk classification triggers specific obligations), and the paper observes systems clustering at or near those boundaries, but does not examine whether this reshapes what gets built.
- **seed-019 (embedded-explanation-opacity):** The paper notes explainability requirements but does not explore whether formalizing "explanation" as a computable deliverable decouples it from actual interpretability of the medical model.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Rationale for store-only:** The paper is a competent applied ethics case study documenting high-risk AI compliance challenges in medical prediction. It does not present a sustained theoretical or empirical argument for a generalizable law, introduce a novel mechanism absent from the inventory, or directly challenge or extend existing protocol laws. It illustrates L-004 and L-014 in a narrow domain but does not advance either inquiry. No escalation warranted.
