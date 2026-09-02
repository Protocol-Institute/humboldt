# Ex-ante versus Ex-post: Egalitarian Facility Location Mechanism Design

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.14499
**Date read:** 2026-09-02
**Connected to:** L-004, L-011
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design paper studying strategyproof facility location under egalitarian (minimax) objectives, comparing deterministic versus randomized mechanisms and ex-ante versus ex-post evaluation conditions. The work proves that randomized mechanisms evaluated ex-ante can achieve better approximation ratios than deterministic mechanisms, even under strategyproofness constraints.

## What I took from it

This is a tight technical result with limited generalization. The core finding—that ex-ante randomization permits better welfare approximation than deterministic mechanisms under strategyproofness—is domain-specific and does not reveal a mechanism absent from the inventory or challenge an existing law.

The paper does not engage with the deeper question of *why* agents might accept ex-ante evaluation over ex-post, nor does it examine what happens when ex-ante and ex-post guarantees diverge operationally in a deployed protocol. The strategyproofness constraint is satisfied in both regimes; there is no evidence of metric capture (L-004) because the objective (egalitarian cost) is directly measurable and the mechanism directly optimizes it. There is no causal detachment (L-011) because the mechanism's output is deterministically derived from its inputs under the stated evaluation frame.

The work is sound within its domain but does not generalize to the protocolized systems we track.

## Research connections

- **L-004:** No metric capture present; objective is direct and unproxied.
- **L-011:** No causal detachment; mechanism output causally transparent under evaluation frame.
- **seed-073:** Tangential: uses consensus cost (minimax) rather than pooled metrics, so not a proxy-collapse case.

## Seed

**Seed title:** none

**Seed type:** 

**Seed text:**
