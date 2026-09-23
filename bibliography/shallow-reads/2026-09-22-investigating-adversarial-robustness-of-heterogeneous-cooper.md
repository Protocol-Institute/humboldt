# Investigating Adversarial Robustness of Heterogeneous Cooperative Perception

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.17856
**Date read:** 2026-09-22
**Connected to:** L-008, seed-132
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of adversarial attack surface in multi-agent cooperative perception systems, examining whether sensor heterogeneity provides robustness against poisoning attacks in learned feature fusion. The work tests the hypothesis that diversity in sensor modalities naturally defends against adversarial feature injection, finding (preliminarily) that this defense is weaker than assumed.

## What I took from it

The paper directly engages L-008 (proxy optimization under computable enforcement) by demonstrating that when perception features become legible and machine-fusible inputs to a downstream decision protocol, a single malicious agent can craft inputs that systematically erase objects from the fused scene. This is a concrete instantiation of the mechanism: when the translation from heterogeneous sensors to a unified feature space becomes formally specified and differentiable, optimization pressure on the attacker becomes precise and legible, making the attack surface computable.

The result undermines a common intuition — that heterogeneity automatically provides defense. Instead, the paper suggests heterogeneity creates a *new attack surface* (translation modules) rather than eliminating the old one. This aligns with seed-132 (synthetic adversary metric faithfulness collapse): the fusion protocol's "robustness" metric (object detection fidelity after fusion) becomes a legible optimization target for an adversary with access to feature transmission, causing the metric to lose correlation with actual safety. The heterogeneity itself becomes part of the attack *design space*.

## Research connections

- **L-008:** Demonstrates computable legibility of attack surface under learned fusion; adversary optimization becomes tractable when feature translation is differentiable.
- **seed-132:** Confirms metric collapse: robustness measured by object detection performance becomes uncorrelated with true scene integrity under adversarial optimization.
- **L-004 (Goodhart):** Fusion fidelity as a proxy for true cooperative perception safety fails when attacked.
- **seed-139:** Heterogeneous sensor setup creates appearance of independent volition (diverse sources) but fusion module is shared decision point — legibility of this module inverts the expected benefit.

## Seed

**Seed title:** Heterogeneity as Attack Surface Proliferation Under Fusion Legibility

**Seed type:** observation

**Seed text:** In multi-agent protocols where heterogeneous agents produce incompatible outputs that are fused via a learned translation layer, the translation layer itself becomes a computable attack surface that can be more efficiently exploited than attack surfaces in homogeneous systems. Heterogeneity does not reduce the attack surface; it relocates it from direct input tampering to learned fusion, where the optimization landscape is continuous and differentiable. This suggests a general pattern: diversity in upstream production can concentrate attack surface at unification boundaries where legibility is highest.
