# The Endogeneity of Miscalibration: Impossibility and Escape in Scored Reporting

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.07671
**Date read:** 2026-11-23
**Connected to:** L-004, L-012, seed-241
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary theoretical source identifying a structural impossibility in dual-incentive protocols that directly instantiates and extends L-004 (Goodhart Generalization) and L-012 (Intervention-Layer Displacement), with a generalizable mechanism for how welfare-maximizing decision rules endogenously produce miscalibration across any scoring regime.

## What this is

A game-theoretic analysis of probability reporting under dual incentive structures: an agent receives payment both via proper scoring rule (accuracy reward) and via an approval rule (decision-consequence reward). The paper proves that when perfect screening is attainable, the welfare-maximizing approval rule cannot be affine, forcing endogenous miscalibration, and identifies a "reserve report" equilibrium where the agent's strategic deviation cost exactly equals the approval payoff.

## What I took from it

This work operationalizes a critical vulnerability in layered-incentive protocols: the conflict between accuracy and decision optimization is *not* a calibration or design failure — it is structural and inevitable under welfare maximization. When a decision rule responds nonlinearly to a report, the agent can exploit the gap between the scoring rule's incentive and the decision rule's consequence. This directly confirms and extends L-004 by showing that Goodhart capture occurs *predictably* at a specific threshold (the reserve report), making it not merely a failure mode but an equilibrium outcome.

The mechanism also activates L-012 (Intervention-Layer Displacement): the approval rule's nonlinearity shifts optimization pressure from "truthful calibration" to "strategic deviation at the margin." The paper shows this is unavoidable when the decision-maker wants to screen agents (e.g., approve only high-quality reports). This suggests a deeper law: in any protocol with separable reward layers (accuracy layer + decision consequence layer), the decision layer will displace the accuracy layer's optimization target unless the decision rule is constrained to be affine — but affinity often conflicts with welfare maximization.

## Research connections

- **L-004 (Goodhart Generalization):** The paper proves Goodhart capture is not contingent on measurement error or optimization intensity — it is structural in dual-incentive settings. The reserve report is the predictable locus of metric capture.

- **L-012 (Intervention-Layer Displacement):** The approval rule, introduced to improve decisions, displaces optimization away from the scoring rule's target. The locus of distortion migrates to the decision margin.

- **L-008 (Proxy Optimization Under Computable Enforcement):** When approval rules are legible and computable, agents can precisely locate the reserve report and exploit it. Computability amplifies miscalibration.

- **seed-241 (Dual-Layer Incentive Nonmonotonicity):** The paper shows adding a second incentive layer does not monotonically improve outcome quality — it creates a new source of strategic distortion.

- **L-019 (Representation-Rationalizability Tradeoff):** The welfare-optimal approval rule trades representational fidelity (accurate probability reports) for decision-side rationality (correct screening). This is a formal instantiation of that tradeoff.

## Seed

**Seed title:** Dual-Incentive Endorsement Threshold as Miscalibration Anchor

**Seed type:** mechanism

**Seed text:** In any protocol where an agent's report triggers both a scoring-rule reward (function of accuracy) and a decision-consequence reward (function of approval/rejection), the welfare-maximizing decision rule is necessarily nonaffine, creating a "reserve report" equilibrium at which the agent's cost of strategic deviation exactly equals the decision payoff. This threshold exists independently of agent rationality or optimization intensity — it is a structural property of the incentive layering. The miscalibration is not preventable via better calibration training; it is endogenous to the protocol's dual-layer structure. This generalizes beyond probability scoring to any composite reward system where a legible decision rule responds nonlinearly to a formally reported
