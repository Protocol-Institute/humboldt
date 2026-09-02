# The Accuracy Trap: Structural Scarcity Amplifies Relative Inequality in Algorithmic Allocation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.11491
**Date read:** 2026-09-02
**Connected to:** L-004, L-008, L-012
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source deriving a scaling law for metric capture under structural scarcity; presents a mechanism (ranking-vs-classification divergence) absent from current inventory; pattern generalizes across rationing domains.

## What this is

A theoretical paper establishing that when algorithmic allocation operates under structural scarcity (demand >> supply), optimizing for accuracy/calibration as a fairness proxy produces a scaling law in relative inequality that is orthogonal to model quality. The work challenges the standard debiasing frame by showing that the statistical properties governing ranking systems diverge fundamentally from classification systems, creating a regime where fairness-as-accuracy becomes actively harmful.

## What I took from it

This is a direct instantiation and mechanistic grounding of **L-004 (Goodhart Generalization: Metric Capture)** under a specific but broad constraint class. The paper shows that accuracy/calibration—the legible, computable proxy for fairness in allocation—becomes *more* optimizable and *more* divorced from the actual fairness goal precisely as scarcity increases. This directly feeds **L-008 (Proxy Optimization Under Computable Enforcement)**: when the ranking protocol is formalized and enforcement becomes legible to optimization (i.e., when you can measure calibration and feed it into system design), the locus of pressure shifts from the underlying allocation problem to the proxy itself.

Critically, this also illuminates **L-012 (Intervention-Layer Displacement)**: interventions designed to improve fairness get redirected into the legible calibration layer, leaving the root rationing problem untouched. The paper suggests that under structural scarcity, *any* fairness metric will exhibit this pathology if it is computable and becomes the target of system optimization. This is not a flaw in a particular algorithm; it is a structural property of the regime.

## Research connections

- **L-004:** Accuracy/calibration as fairness proxy exhibits metric capture under scarcity; optimization pressure concentrates on the proxy rather than the goal (fairness under rationing).
- **L-008:** Computable accuracy signals become optimization targets; agents (system designers, auditors) condition behavior on legible calibration metrics, displacing pressure away from the actual allocation problem.
- **L-012:** Normative fairness interventions targeting accuracy end up locked into the prediction/ranking layer; the intervention locus is displaced upstream, leaving scarcity-induced harm unaddressed.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** When demand/supply is asymmetric and structural, the proxy (accuracy) collapses as a stand-in for fairness; upstream scarcity structure overpowers downstream metric optimization.
- **seed-077 (Metric-Induced Preference Ratcheting):** Optimization for accuracy in ranking systems induces downstream changes in how the metric is understood and defended, creating lock-in.

## Seed

**Seed title:** Scarcity-Induced Proxy Collapse in Rationing Protocols

**Seed type:** observation + mechanism

**Seed text:** In allocation protocols operating under structural scarcity (demand >> supply by a scaling factor), accuracy/calibration in ranking systems scales away from fairness according to a computable scaling law, independent of model quality or debiasing effort. This occurs because ranking under scarcity is fundamentally a rationing problem, not a classification problem; legible optimization targets (accuracy metrics) become decoupled from the unmeasurable fairness goal. Protocols that lock fairness into computable proxies under high-scarcity regimes will exhibit this pattern across domains (welfare, medical triage, resource allocation) where demand is persistent and structural.
