# Toward Fairness in Machine Learning Models for Predicting Treatment Retention and Premature Discontinuation in Medication for Opioid Use Disorder

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.22113
**Date read:** 2026-09-22
**Connected to:** L-004, L-012, seed-132
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A fairness audit of ML retention-prediction models in opioid use disorder treatment. The paper applies standard algorithmic fairness metrics (demographic parity, equalized odds, etc.) to assess whether predictive models exhibit performance disparity across patient subgroups, and proposes mitigation strategies. Domain-specific case study without sustained theoretical argument or novel mechanism.

## What I took from it

The work confirms L-004 and L-012 in microcosm: fairness becomes a legible proxy for an unmeasurable goal (good treatment matching / equitable care), and optimization pressure against fairness metrics displaces the actual intervention locus. When fairness is formalized as a computable constraint on model outputs, the optimization surface shifts — clinicians or systems may end up gaming fairness scores rather than improving actual retention outcomes. The paper does not theorize this displacement; it treats fairness as an add-on constraint, which is precisely the configuration where causal detachment occurs (L-011 / seed-132).

The study also illustrates seed-144 (informality as refuge): clinical judgment about patient risk remains partially informal precisely because formal retention prediction generates adversarial optimization. The paper documents that fairness metrics conflict with each other and with predictive accuracy — a harbinger of the metric capture ratchet already underway in the protocol layer.

## Research connections

- **L-004:** Fairness as unmeasurable goal → measurable proxy → optimization pressure captures proxy rather than goal
- **L-012:** Formalization of prediction as legible input to decision protocol displaces optimization pressure from outcome to metric surface
- **seed-132:** Synthetic adversary (fairness metric) achieves legibility at cost of faithfulness to actual treatment success
- **seed-144:** Informal clinical judgment persists as coordination refuge when formal metrics become optimization targets

## Seed

**Seed title:** Fairness-Outcome Decoupling Under Metric Formalization in Safety-Critical Prediction

**Seed type:** observation

**Seed text:** When fairness metrics are formalized as constraints or objectives in safety-critical prediction systems (e.g., clinical retention models), optimization pressure concentrates on achieving metric parity rather than on the unmeasurable outcome (actual treatment retention and recovery). The formalization creates a new optimization surface that is operationally decoupled from the original goal: a model can satisfy fairness constraints while predicting poorly on the underlying outcome, or satisfy outcome accuracy while violating fairness — this tradeoff persists because fairness is a property of the *prediction distribution*, not the *causal effect of treatment*. The displacement is self-reinforcing: as fairness becomes auditable and reportable, it becomes the legible success criterion, further decoupling from outcome verification which is slow, long-term, and attributionally ambiguous.
