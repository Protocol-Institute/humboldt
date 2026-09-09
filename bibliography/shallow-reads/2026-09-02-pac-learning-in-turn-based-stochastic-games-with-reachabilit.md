# PAC Learning in Turn-Based Stochastic Games with Reachability Objectives: A Decentralized Private Approach via Expected Conditional Distance

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.14877
**Date read:** 2026-09-02
**Connected to:** L-005
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

This is a theoretical machine learning paper on the hardness and feasibility of PAC learning in turn-based stochastic games where players compete to reach target states. The work addresses the foundational difficulty that reachability objectives resist efficient learning even in simplified settings (MDPs), and proposes a decentralized private learning approach using expected conditional distance as a proxy metric.

## What I took from it

The paper establishes a negative result — that certain coordination objectives (reachability in adversarial settings) are provably hard to learn efficiently from first principles — and then proposes a workaround using proxy metrics and decentralized private mechanisms. This touches on L-005's claim about complex systems resisting restructuring, but only tangentially: the paper is concerned with *learning efficiency in the abstract*, not with the empirical observation that working protocols cannot be safely replaced from scratch.

The use of expected conditional distance as a legible proxy for the unmeasurable goal (reaching the target state in an adversarial game) does resonate with L-004 (Goodhart Generalization), but the paper does not examine what happens when this proxy is optimized under pressure over time — it is concerned with convergence guarantees in the learning phase, not with long-run protocol drift.

The work is technically sound but domain-specific: it does not generalize a mechanism beyond game-theoretic learning, nor does it challenge or extend an existing law in the inventory. It confirms that reachability is hard, but this is already known in the community.

## Research connections

- **L-005:** The paper's negative results (PAC-hardness) suggest that complex coordination objectives cannot be learned from scratch efficiently, which aligns with the claim that working systems resist restructuring — but the paper does not study actual working systems or their evolution.
- **L-004:** The use of expected conditional distance as a proxy for unmeasurable reachability is a form of metric substitution, but the paper does not track what happens when agents optimize this proxy over extended operational time.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** The decentralized private approach assumes asymmetric information; the conditional distance metric may collapse if upstream asymmetries shift, but this is not studied.

## Seed

**Seed title:** none

**Seed type:** 

**Seed text:**
