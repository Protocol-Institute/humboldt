# Decision-Centered Evaluation of Machine Learning Poverty Maps Using Mobile Phone and Satellite Data

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.23805
**Date read:** 2026-09-22
**Connected to:** L-004, L-012, seed-131
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical evaluation paper applying decision-centered ML assessment to poverty mapping in Sri Lanka using CDRs and satellite imagery. The work demonstrates that average prediction accuracy metrics do not reliably predict downstream targeting performance when budgets are constrained, introducing a gap between classifier optimality and policy utility.

## What I took from it

This is a clean instantiation of L-004 (Goodhart Generalization) and L-012 (Intervention-Layer Displacement) in a governance-resource-allocation context. The paper shows that optimizing for mean prediction error in poverty classification does not optimize for the decision protocol that actually matters: selecting the N poorest regions under a fixed budget. The accuracy metric is unmeasurable-goal proxy (true causal poverty status is unobserved), and under optimization pressure (training ML models), the classifier drifts away from the decision objective.

The decision-centered evaluation framework itself maps cleanly onto L-012's mechanism: the prediction layer (CDR+RS embeddings) becomes legible and optimizable, which displaces the locus of optimization away from the actual policy outcome (correct targeting under budget constraint). The paper does not investigate *why* this displacement occurs or whether it generalizes across decision protocols, but it documents the phenomenon crisply. The work is pragmatic and domain-specific; it does not advance the theory of the displacement or explore conditions under which it becomes pathological.

## Research connections

- **L-004:** Metric capture instantiated in poverty classification—models optimize for accuracy, not for decision-stage utility under budget constraint.
- **L-012:** Intervention-layer displacement confirmed; prediction legibility drives optimization away from decision protocol objectives.
- **seed-131:** Context legibility (accuracy metrics) becomes failure attribution boundary; good metrics do not guarantee correct causal inference for targeting.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**DECISION:** Store only. This is competent empirical work validating existing theoretical expectations in a new domain (poverty targeting). It does not introduce a mechanism absent from the inventory, does not challenge any of L-001 through L-021, and does not generalize its finding into a law candidate. The decision-centered evaluation framework itself is methodological, not a law. No new seed warranted.
