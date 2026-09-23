# Consistency-Robustness Tradeoffs for Strategyproof Scheduling with Predictions

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.14088
**Date read:** 2026-09-22
**Connected to:** L-001, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic mechanism design paper studying strategyproof scheduling when the mechanism receives advance predictions of machine processing times. The work introduces EdgeSkip, a deterministic mechanism that trades off consistency (approximation quality when predictions are correct) against robustness (worst-case performance when predictions are wrong), and characterizes the fundamental tradeoff between these two objectives under strategyproofness constraints.

## What I took from it

This is a canonical metric-capture scenario: the mechanism is optimized against a *legible proxy* (the prediction) while remaining constrained by strategyproofness. The core finding—that consistency and robustness are in tension—confirms L-004 (Goodhart Generalization) in a new domain, but does not supply a mechanism. The paper documents the tradeoff without explaining *why* it exists or *when* it should be expected to generalize.

The strategyproofness constraint itself acts as a *conserved cost*: agents cannot be forced to internalize prediction error, so the mechanism must absorb it through either prediction fidelity or worst-case slack. This mirrors L-006 (Coordination Cost Conservation) but the paper does not frame it that way. The work is technically sound but does not investigate whether this tradeoff is a local artifact of the scheduling domain or a symptom of a deeper regularity in prediction-driven protocol design.

## Research connections

- **L-004:** Confirms metric capture risk when a protocol optimizes against a public prediction; consistency-robustness tradeoff is a symptom of Goodhart pressure, but mechanism of capture not explored.
- **L-001:** Strategyproofness constraint may function as an ossification force—the requirement to remain incentive-compatible limits design flexibility, forcing tradeoff rather than permitting unified improvement.
- **seed-132:** Synthetic Adversary Metric Faithfulness Collapse — The prediction acts as a synthetic ground truth; the paper implicitly assumes prediction accuracy is exogenous, but does not study whether agent behavior under consistent optimization against predictions causes the prediction signal itself to degrade.
- **L-008 (exploration):** Proxy Optimization Under Computable Enforcement — The prediction is a computable input; the mechanism is legibly optimized against it; whether this drives agent adaptation away from the prediction is not studied.

## Seed

**Seed title:** Prediction-Legibility Binding Under Incentive Preservation

**Seed type:** observation

**Seed text:** In mechanism design problems where a protocol receives a computable prediction and must remain strategyproof (or otherwise incentive-compatible), the protocol cannot simultaneously optimize tightly against the prediction and maintain worst-case robustness. The mechanism must choose: sacrifice consistency (tighten prediction fidelity) or sacrifice robustness (tolerate prediction error). This constraint appears to be independent of the specific mechanism design problem. The deeper question: does this tradeoff exist because incentive-compatibility itself imposes a cost-conservation structure (agents cannot be forced to bear prediction error), or because the legibility of the prediction creates a secondary optimization surface that agents can exploit? If the latter, the tradeoff might generalize to any protocol where agents observe the mechanism's internal predictive input.
