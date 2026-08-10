# Bridging Predictions and Interventions: An Integrated Framework for Automated Decision-Systems

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.25668
**Date read:** 2026-08-10
**Connected to:** L-004, L-008, seed-016
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A CS+policy paper arguing that predictive accuracy alone does not determine downstream outcomes in automated decision systems (ADS), and proposing an integrated framework that bridges prediction quality to intervention effectiveness across criminal justice, clinical, and educational settings. The core claim is empirical observation across domains rather than a sustained theoretical or mechanistic argument.

## What I took from it

The paper documents a widespread decoupling: that improving the prediction component of an ADS does not reliably improve organizational outcomes, and may worsen them under certain decision-rule configurations. This is directly relevant to L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement), but the paper itself does not isolate the *mechanism* driving this decoupling.

The work treats the prediction-to-intervention gap as a design problem solvable by framework integration, rather than as evidence of a deeper regularization: that when predictions become the legible optimization target within a computable decision protocol, the decision-maker's behavior shifts away from the original objective and toward prediction improvement itself—a stopping-rule substitution (seed-016). The paper documents the symptom but does not name the cause as protocol-level capture.

This reads as a competent empirical failure-mode catalog rather than a primary theoretical or mechanistic investigation. It confirms that L-004 and L-008 operate in this domain, but does not advance the mechanism inventory.

## Research connections

- **L-004:** Confirms metric capture in prediction-based ADS: improved accuracy does not yield improved outcomes; suggests the goal and the measurable proxy have decoupled under optimization pressure.
- **L-008:** Relevant to the conditions under which computable enforcement signals (prediction scores, decision thresholds) become independent optimizable targets, displacing the original objective.
- **seed-016:** The paper's core observation—that decision-makers optimize for prediction improvement rather than outcome improvement—is stopping-rule substitution in a protocol context.

## Seed

**Seed title:** Prediction Proxy Decoupling in Consequential Protocols
**Seed type:** observation
**Seed text:** When predictions are formalized into legible decision inputs within a safety-critical protocol (criminal justice, clinical triage, resource allocation), the optimization pressure on the decision-maker shifts from the original outcome (recidivism, patient recovery, student success) to the intermediate prediction target itself. This decoupling occurs independent of prediction accuracy improvements, suggesting that computable enforcement and legibility of the proxy metric—not the quality of the proxy—drives the capture. The mechanism may generalize to any multi-stage protocol where an intermediate component becomes independently measurable and organizationally accountable.
