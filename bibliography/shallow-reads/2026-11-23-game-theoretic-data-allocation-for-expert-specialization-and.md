# Game-Theoretic Data Allocation for Expert Specialization and Routing

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2611.25167
**Date read:** 2026-11-23
**Connected to:** L-004, seed-456, seed-462
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mixture-of-experts architecture (InflEns) where training data allocation and inference routing are both derived from the same game-theoretic equilibrium over a prompt-trait space. Experts compete to claim regions of the data distribution without access to task losses; the resulting allocation is claimed to be both interpretable and predictive of inference performance.

## What I took from it

The paper proposes decoupling expert selection from gradient-based optimization by using a location game to simultaneously determine (1) which data each expert trains on and (2) which expert handles which prompt at inference. The core claim is that this makes the division of labor "inspectable" and allows allocation itself to guide routing.

This touches L-004 (metric capture) in a sideways manner: the game uses position in prompt-trait space as a proxy for expert competence, and the paper's framing assumes this proxy is stable across training and inference. However, the work does not investigate whether optimization pressure on the allocation itself causes the proxy to degrade, nor does it test robustness under distribution shift or adversarial prompt clustering. The connection to metric capture is present but not examined. The paper is also primarily a tool/architecture contribution rather than a theoretical argument about protocol dynamics, so it does not develop the law or challenge existing inventory in a sustained way.

## Research connections

- **L-004:** The game equilibrium selects a legible proxy (position in prompt-trait space) for expert suitability, but the paper does not test whether this proxy remains stable under optimization pressure or multi-round adoption.
- **seed-456:** Allocation-inference coupling under legibility — implicit in the design, not analyzed as a failure mode.
- **seed-462:** Expertise formalization as coordination surface — the game formalizes expertise-distribution matching, but does not examine whether this locks agents into rigid specialization roles.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
