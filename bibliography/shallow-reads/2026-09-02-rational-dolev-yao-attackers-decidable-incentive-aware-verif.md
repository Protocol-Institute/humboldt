# Rational Dolev--Yao Attackers: Decidable Incentive-Aware Verification of Security Protocols in Strategic Logic

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.22954
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** —

## What this is

A formal methods paper introducing rational agents into symbolic protocol verification. The work extends the classical Dolev--Yao threat model by assigning costs to attacker actions and rewards to security violations, then asks: when is a protocol secure against an intruder maximizing utility rather than executing all actions its knowledge permits? The contribution is a decidable verification framework in strategic logic.

## What I took from it

This is a boundary-case formalization rather than a discovery of a new mechanism. The paper correctly identifies that classical symbolic verification assumes attackers are *omniscient maximizers of destructive capability* (do everything possible), whereas real adversaries operate under resource and incentive constraints. However, the solution—embedding utilities into the verification problem—is a straightforward application of rational choice theory to an existing verification framework. It does not expose a novel regularity about how protocols behave under optimization pressure, nor does it examine what happens when the cost/reward structure becomes legible to protocol designers or when attackers reverse-engineer the utility model itself.

The work addresses L-004 and L-008 superficially: it adds optimization to the attacker model but does not investigate *metric capture* (whether the chosen utility proxy becomes a target for manipulation) or *proxy optimization under computable enforcement* (what happens when attackers can shape the conditions under which they are rewarded). It remains within the symbolic verification domain—a tool paper, not a law-shaped claim about protocol behavior in the wild.

## Research connections

- **L-004 (Goodhart Generalization):** The paper assumes a fixed utility function, but does not explore whether that function becomes distorted when made legible to attackers or when protocol designers learn which attack vectors carry which rewards.
- **L-008 (Proxy Optimization Under Computable Enforcement):** The formalization makes attacker incentives *precisely computable*, but the paper does not investigate whether this legibility creates new optimization channels (e.g., attackers coordinating to change the reward structure itself).
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Implicit: if the utility model is asymmetrically known or subject to designer manipulation, the proxy security guarantee may collapse.
- none

## Seed

**Seed title:** Utility Model Legibility as Protocol Redesign Target

**Seed type:** question

**Seed text:** When a protocol's security is verified against attackers with *legible, computable utility functions*, does the protocol designer's ability to tune reward/cost parameters create an incentive for attackers to influence the parameter-setting process itself, or to demonstrate violations whose utility is calculated under adversarially-chosen metrics? In other words: does rational security verification, by formalizing the attacker's objective, convert the utility model into a new surface of strategic contestation? This may generalize to any protocol system where compliance or security is verified via an explicitly computable proxy for an unmeasurable good (trust, fairness, safety).
