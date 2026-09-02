# Testing Fairness with Utility Tradeoffs: A Wasserstein Projection Approach

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2505.11678
**Date read:** 2026-09-02
**Connected to:** L-004, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A statistical testing framework that relaxes strict fairness constraints in algorithmic decision-making systems by jointly evaluating approximate fairness and utility retention. The work treats fairness-utility tradeoffs as a hypothesis testing problem, using Wasserstein projections to operationalize demographic parity under utility thresholds.

## What I took from it

The paper demonstrates a key instantiation of **L-004 (Goodhart Generalization)**: fairness-as-measurable-proxy becomes a lever for utility optimization. By formalizing "approximate fairness" as a relaxable metric, the framework operationalizes the permission structure for metric capture. However, the work does not theorize *why* this capture occurs or what determines the equilibrium between formal fairness and actual utility extraction — it engineers around the tradeoff rather than explaining its necessity.

The approach is consistent with **L-006 (Coordination Cost Conservation)**: the framework does not eliminate the fairness-utility tension, but displaces it from the protocol layer (strict fairness rules) to the statistical layer (hypothesis testing thresholds). Coordination work formerly done by hard constraints is now delegated to threshold-tuning and parameter selection — the cost is conserved, not eliminated.

The work is ultimately a tool paper optimizing within an already-framed problem space. It does not investigate whether the fairness metric itself is capturing the unmeasurable goal (equity, non-discrimination, dignity) or simply creating legible compliance theater.

## Research connections

- **L-004:** Fairness metrics become optimization targets; utility can be recovered by relaxing fairness constraints, consistent with metric capture dynamics under computable enforcement.
- **L-006:** Fairness-utility tension is displaced from hard protocol constraints to statistical parameter tuning; coordination cost is conserved across representation layers.
- **seed-077:** Metric-induced preference ratcheting — fairness metrics, once formalized and relaxed, create incentive structures to optimize utility within the relaxed bounds.
- **seed-080:** Proxy collapse under upstream asymmetry — demographic parity proxies may fail when the demographic categories themselves encode upstream inequities.

## Seed

**Seed title:** Formalized Fairness as Utility Laundering Scaffold

**Seed type:** observation

**Seed text:** When fairness metrics are formalized into testable, relaxable constraints with computable utility thresholds, the protocol creates a legible zone for utility optimization that preserves fairness-appearance while weakening fairness-substance. The framework does not prevent capture; it architectures permission for it. In systems where fairness is the nominal constraint and utility is the optimization objective, formalizing both as jointly-testable quantities tends to produce equilibria where fairness is satisfied nominally (passing the test) while utility extraction proceeds maximally (within the test's tolerance). This may generalize to any two-objective protocol where one objective is harder to measure than the other and one objective has more concentrated payoff.
