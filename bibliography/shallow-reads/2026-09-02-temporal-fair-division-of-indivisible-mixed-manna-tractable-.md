# Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.20033
**Date read:** 2026-09-02
**Connected to:** L-004, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational fair division paper studying online allocation of indivisible items (goods, chores, neutrals) arriving sequentially, where each allocation is irrevocable and must satisfy envy-freeness constraints after every round. The work identifies NP-hardness of the decision problem but provides tractable algorithms under bounded item-type cardinality.

## What I took from it

This is competent algorithmic work on a classical coordination problem (fair allocation), but it does not engage with the generative mechanisms we track. The paper studies *how to allocate fairly under temporal constraint* — a normative design problem — not *what happens when fairness metrics become the legible target of optimization* (L-004), nor *how coordination cost redistributes across protocol layers* (L-006). 

The irrevocability constraint is operationally real and does interact with coordination pressure, but the paper treats it as a hard boundary of the problem, not as a protocol design choice with downstream effects. No evidence surfaces that the cyclic rule or tractability conditions reveal systematic pathologies in how agents behave when fairness is rendered computable and enforceable — which is where L-004 and L-008 would activate.

## Research connections

- **L-004:** The paper uses envy-freeness as a measurable proxy for fairness, but does not examine what happens when agents optimize against this metric under enforcement legibility.
- **L-006:** Temporal constraints displace coordination cost, but the paper does not model where that cost migrates or whether it is conserved.
- none (no connection to L-001, L-002, L-003, L-005, L-007, L-008–L-016, or active seed pool)

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
