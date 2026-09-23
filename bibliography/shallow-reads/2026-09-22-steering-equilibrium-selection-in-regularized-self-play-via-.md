# Steering Equilibrium Selection in Regularized Self-Play via the Reference Policy

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.19820
**Date read:** 2026-09-22
**Connected to:** L-004, seed-150
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of how the reference policy in regularized self-play (the family behind DeepNash) silently selects among value-equivalent Nash equilibria through entropy regularization. The work demonstrates that reference policy choice can be used to steer equilibrium selection in 2-player zero-sum games, and empirically tests this on five exactly-solvable games and a 2-D polytope.

## What I took from it

This is a technical refinement paper within an established algorithmic family—it does not present a sustained theoretical argument about protocols or their behavior under scaling, adoption, or adversarial pressure. The core finding—that a hyperparameter (the reference policy) encodes implicit tie-breaking among equivalent outcomes—is a mechanism for *predictable selection* rather than a source of instability, ossification, or governance failure.

The work is relevant to L-004 (Goodhart Generalization) only in a limited sense: it shows that when a protocol (self-play with entropy regularization) has multiple solutions with identical formal performance, the choice of regularizer becomes the implicit optimization target. However, this is a feature of the algorithm's design, not an emergent capture phenomenon. There is no evidence here that agents gaming the reference policy, or that the regularizer itself becomes a site of strategic distortion under deployment pressure.

## Research connections

- **L-004:** Regularization parameters can encode implicit optimization targets among formally equivalent solutions; however, this appears to be a design choice rather than metric capture under optimization pressure.
- **seed-150:** The reference policy does encode value formalization, but as a deliberate steering mechanism, not as a spontaneous proxy substitution under pressure.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
