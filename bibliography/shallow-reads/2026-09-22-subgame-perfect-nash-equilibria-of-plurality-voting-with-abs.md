# Subgame-Perfect Nash Equilibria of Plurality Voting with Abstention: a PSPACE-Completeness Result for Restricted Ballots

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.24292
**Date read:** 2026-09-22
**Connected to:** L-003, seed-150
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic hardness result proving PSPACE-completeness for computing subgame-perfect Nash equilibria in sequential plurality voting with abstention and restricted ballot sets. The work formalizes voting as a sequential game where voters have incomplete control (restricted to a prefix of their preference ranking) and must decide whether to vote or abstain under positive voting cost.

## What I took from it

This is a pure complexity result in voting theory, not a primary source on protocol behavior under adoption or scaling stress. It formalizes a particular coordination problem (plurality voting equilibrium) but does not examine how that formalization changes agent behavior, coordination patterns, or system resilience. The paper treats the formalization (restricted ballots, cost function, sequential moves) as given constraints rather than investigating how the act of making these constraints computable affects equilibrium selection, voter strategy, or protocol stability.

The restriction to a ballot prefix is interesting as a *legibility constraint*—it operationalizes what voters *are allowed to express*—but the paper does not examine whether this constraint, once formalized, becomes an optimization target or whether agents find ways to signal beyond it. There is no treatment of how the computational hardness of equilibrium discovery affects real coordination or whether approximations collapse into pathological equilibria.

## Research connections

- **L-003 (Formalization Ratchet):** The restricted ballot constraint is a formalization intervention, but this paper does not investigate whether formalization *causes* the shift from informal to formal coordination—it assumes the formalization as a given and computes within it.
- **seed-150:** The paper does formalize value/preference aggregation (restricted ranking), but treats this as an input to the game rather than examining how formalization itself becomes a coordination pressure or failure mode.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
