# RANDAO Manipulation in the Presence of MEV

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.02143
**Date read:** 2026-11-23
**Connected to:** L-008, L-014, seed-461
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of strategic manipulation in Ethereum's RANDAO randomness protocol, extending prior work by decoupling block-proposal capacity from actual reward capture. The paper develops a generalized reward model and computes ε-optimal manipulation strategies for multiple reward schemes (consensus rollover, MEV, oracle attacks, etc.).

## What I took from it

This is a competent domain-specific analysis that confirms L-008 (proxy optimization under computable enforcement) in the specific case of randomness-beacon manipulation: when randomness becomes a legible computational input to a protocol with heterogeneous reward structures, optimizing agents decouple the proxy (block proposal fraction) from the actual payoff surface. The generalized reward model is the technical contribution.

However, the paper does *not* investigate the systemic consequences of this decoupling — it does not ask whether the ε-optimal strategies induce cascade failures, whether reward-model misspecification becomes protocol-level risk, or whether the toolkit generalizes to other protocol domains. It is a technical solution paper to a known problem class, not a primary source making a sustained theoretical argument about how computable enforcement and proxy decoupling interact at scale.

The connection to L-014 (strategic boundary concentration) is weaker: the paper does not examine whether agents concentrate optimization pressure at the formal boundary between randomness protocol and reward protocol, though the structure invites that reading.

## Research connections

- **L-008:** Confirms the core mechanism — when randomness enforcement becomes computable and legible, optimizing agents treat block-proposal capacity as a proxy distinct from true reward surface, and can compute strategies that exploit the gap.
- **L-014:** Tangential — the paper does not examine whether optimization pressure concentrates at formal protocol boundaries, only that it escapes the naive proxy.
- **seed-461:** Directly relevant — demonstrates that reward-model proxy capture is a live optimization target when enforcement is computable; the generalized model is a methodological advance but does not resolve the deeper instability.

## Seed

**Seed title:** Reward-Model Legibility as Orthogonal Optimization Axis

**Seed type:** observation

**Seed text:** When a protocol makes an enforcement signal computable (randomness, block proposals, oracle inputs), it does not eliminate proxy optimization — it merely displaces it to the layer above: the reward model itself. Strategic agents decouple capacity from payoff by learning which reward schemes are exposed to which attack surfaces. The key variable is not whether the proxy is manipulable, but whether the relationship between proxy and true reward is itself formally specified and therefore subject to endogenous refinement. Protocols that leave reward models informal or agent-heterogeneous may resist this layer of optimization longer than those that legalize them. This suggests a secondary ossification vector: formalized reward models become coordination targets in their own right.
