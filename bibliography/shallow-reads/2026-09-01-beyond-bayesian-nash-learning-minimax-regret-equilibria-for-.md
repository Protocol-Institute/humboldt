# Beyond Bayesian Nash: Learning Minimax-Regret Equilibria for Adversarial Team Games under Asymmetric Information

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.09993
**Date read:** 2026-09-01
**Connected to:** L-009, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper extending equilibrium solution concepts for adversarial team games with hidden information, proposing minimax-regret equilibria as an alternative to Bayesian Nash equilibrium under distributional uncertainty. The work is technical and domain-specific to competitive graph-based games with asymmetric information structures.

## What I took from it

The paper addresses robustness to type distributions in competitive settings where one player has hidden information and can condition deceptive play on observed opponent moves. This touches seed-048 (capability-cooperation inversion) in that the adversary's ability to condition play on type observations creates an asymmetric advantage that standard equilibrium concepts fail to capture. However, the paper frames this as a *solution concept* problem (how to find equilibria robust to distributional uncertainty) rather than as a protocol *mechanism* problem. It does not examine how such asymmetries cascade through multi-round coordination, how they deform incentive structures under scaling, or how deception-robust protocols ossify when adopted widely. The minimax-regret framework is mathematically sound but remains internal to game theory rather than engaging with how such games embed in systems with path dependence, institutional memory, or enforcement costs.

## Research connections

- **L-009:** The paper models racing protocols (reachability games, goal search) with hidden types, but does not examine whether symmetric racing creates catastrophic risk cancellation or how concentrated prizes interact with distributed costs.
- **seed-048:** Capability-cooperation inversion is implicit (the adversary's hidden type gives it unilateral conditioning power), but the paper does not track how this inversion evolves under repeated play, feedback, or protocol amendment.

## Seed

**Seed title:** none
