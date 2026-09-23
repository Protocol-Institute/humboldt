# Online Allocation using Few Samples

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.17343
**Date read:** 2026-09-22
**Connected to:** L-006, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic algorithmic paper studying online allocation under adversarial arrival sequences with bounded sampling budget. The work develops competitive algorithms for resource allocation and load balancing that achieve $(1\pm\epsilon)$-competitive ratios using only polylogarithmic samples, operating in the large-budget or large-makespan regime.

## What I took from it

The paper is a competent algorithmic contribution addressing sample complexity in a classical online problem, but it does not engage with the mechanistic or systemic properties of protocol ossification, coordination cost distribution, or proxy optimization under computable enforcement. The work treats sampling and resource budgets as technical constraints to be optimized away, not as sites where coordination cost is conserved or displaced.

The connection to L-006 (coordination cost conservation) is tenuous: the paper shows how to reduce sample queries through better algorithm design, but does not examine whether this reduction in one layer (information queries) creates hidden costs elsewhere in the protocol stack (e.g., latency acceptance, fairness variance, verification complexity). Similarly, L-008 (proxy optimization under computable enforcement) is not addressed — the paper does not study what happens when allocation decisions become legible targets for strategic manipulation or when the optimization metric itself becomes visible and weaponizable by agents.

This is sound technical work within its frame, but the frame itself is orthogonal to the laws we are accumulating.

## Research connections

- **L-006:** Claimed connection assumes sample reduction is cost elimination; does not track where coordination burden migrates.
- **L-008:** No treatment of what happens when allocation outcomes become formalized, legible decision inputs to downstream agent optimization.
- none

## Seed

**Seed title:** none
