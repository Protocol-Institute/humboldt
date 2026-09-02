# CAP-DO: Learned Contextual Action Proposals for Certified Double-Oracle Solving Across Related Zero-Sum Games

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.24610
**Date read:** 2026-09-02
**Connected to:** L-002, seed-052
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic solver paper applying learned neural proposals to accelerate Double Oracle computation across parametric families of zero-sum games. The contribution is primarily algorithmic: speeding up equilibrium discovery in defender-attacker inspection planning by learning to propose candidate action expansions rather than computing them from scratch each time the payoff context changes.

## What I took from it

The work confirms L-002 (Hardness Asymmetry) in a specific instantiation: the defender must solve a full game to find a certified Nash equilibrium, while the attacker's optimization problem (finding a profitable deviation) is asymmetrically cheaper to verify once a candidate strategy is proposed. The paper mitigates this by using learned proposals to reduce the defender's repeated computation burden across related contexts.

However, the paper does not interrogate the deeper pattern: it treats the asymmetry as a computational engineering problem to be solved via acceleration, not as a structural property of the verification/execution split under legible strategy spaces. The attacker's side of the equation (cost to discover profitable deviations) remains implicit and underexamined. The work is competent but local—it optimizes within the framework without surfacing the generalizable mechanism.

## Research connections

- **L-002:** Confirms verification asymmetry in zero-sum games (defender must solve full equilibrium; attacker searches for profitable deviation). Does not investigate whether this asymmetry persists or inverts under different legibility conditions.
- **seed-052:** Related to strategy space legibility as optimization target, but treats it as a solver efficiency problem rather than a protocol vulnerability vector.

## Seed

**Seed title:** none

---

**Rationale for store-only:** This is a working paper in algorithmic game theory with a clear narrow contribution (neural proposal acceleration for DO). It does not present a primary theoretical argument about protocol systems, does not challenge or extend a law under accumulation, and does not introduce a mechanism absent from the inventory. It instantiates L-002 without deepening it. No seed warrants induction.
