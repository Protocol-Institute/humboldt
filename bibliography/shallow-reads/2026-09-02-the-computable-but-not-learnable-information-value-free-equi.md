# The Computable but Not Learnable Information-Value-Free Equilibria and Regulation of Algorithmic Collusion

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.27128
**Date read:** 2026-09-02
**Connected to:** L-008, seed-053
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper establishing a computability–learnability gap: information-value-free correlated equilibria can be computed efficiently offline but are not learnable by broad classes of standard learning algorithms operating on local payoff feedback alone. The domain is algorithmic collusion in repeated games.

## What I took from it

The paper identifies a structural separation between what is *computationally accessible* and what is *behaviorally reachable* under decentralized learning. This is relevant to L-008 (Proxy Optimization Under Computable Enforcement) insofar as it shows that making an equilibrium *computable* does not automatically make it *adoptable* by distributed agents using standard adaptation mechanics. However, the result is narrower than the open line requires: it applies to a specific class of equilibria (information-value-free) and specific learning rules, and does not establish that this gap persists under strategic optimization pressure or multi-layer protocol design.

The work also does not address whether agents with access to the offline computation could deliberately deploy strategies to *enforce* convergence to the computable equilibrium—which is the core mechanism of L-008. The paper is primarily a negative result about standard learning, not an examination of what happens when enforcement legibility is added to the system.

## Research connections

- **L-008:** Shows a gap between computability and learnability, but does not address computable enforcement or strategic boundary optimization under legibility pressure.
- **seed-053:** Confirms that collusive equilibria can be algorithmically specified; does not establish whether they become optimization targets under regulatory or competitive pressure.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
