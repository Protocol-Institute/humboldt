# Perpetual Fully-Online Approximate Fairness

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.19844
**Date read:** 2026-09-01
**Connected to:** L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper on fair allocation algorithms operating under strict online constraints: decisions are irrevocable, arrival patterns are unknown, duration is unbounded, and fairness must be maintained in aggregate across rounds. The work develops approximation algorithms for perpetual fairness in resource allocation (food banks, scheduling, priority systems) where traditional fairness guarantees cannot be computed in advance.

## What I took from it

The paper instantiates L-006 (Coordination Cost Conservation) in a specific technical domain but does not generalize beyond it or reveal a new mechanism. The core finding—that fairness constraints in perpetual online settings require trading off individual-round optimality for long-run aggregate fairness—is a localized consequence of information asymmetry and commitment architecture, not a discovery of how coordination costs transfer or hide when protocols shift layers.

The work is technically sound but treats fairness as a static constraint to be approximately satisfied, not as an emergent property of protocol design under stress. It does not investigate what happens when the fairness definition itself becomes contested, when agents optimize the metric rather than the underlying allocation, or how the "approximate" character of fairness accumulates into legitimacy failures over time—all of which would ground the work in the new nature agenda.

## Research connections

- **L-006:** The paper shows one instantiation of coordination cost conservation: the cost of maintaining fairness in perpetual online allocation is transferred from up-front planning into per-round approximation and verification overhead. However, this is domain-specific confirmation, not a challenge to or extension of the law.
- **L-004 (Goodhart Generalization):** Implicit risk: as fairness metrics become operationalized in the algorithm, optimization pressure may shift from fair allocation to metric satisfaction. The paper does not explore this.
- **seed-016 (stopping-rule-substitution):** Weak connection: the "perpetual" framing may mask latent stopping rules (funding exhaustion, user churn, policy change) that violate the unknown-duration assumption.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
