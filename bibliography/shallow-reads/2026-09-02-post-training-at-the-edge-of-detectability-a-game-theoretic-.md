# Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.26358
**Date read:** 2026-09-02
**Connected to:** L-004, L-008, seed-016
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic treatment of KL-regularized RL fine-tuning in language models, proposing principled methods for setting the regularization coefficient to balance task performance against policy drift. The work frames the reward-retention trade-off as a detection problem rather than a direct optimization constraint.

## What I took from it

The paper sits at the intersection of L-004 (metric capture under optimization pressure) and L-008 (proxy optimization under computable enforcement), but does not generate new theoretical machinery for either. The framing of KL-regularization as a "detectability edge" is intuitive—the idea that agents optimize up to the boundary of what can be distinguished from baseline behavior—but the paper treats this as a tuning problem rather than a law-like phenomenon with cross-domain generalizations.

The work confirms that when proxy constraints become precisely computable (KL divergence is legible, measurable, enforceable), optimization pressure migrates to exploit the slack within that constraint. However, this is already captured by existing seeds around computable legality and proxy drift. The game-theoretic framing adds rigor to *how* the trade-off is calibrated, but does not reveal a mechanism absent from the current inventory.

## Research connections

- **L-004:** Confirms metric capture: KL-regularization itself becomes the target under optimization; the coefficient must be chosen to stay ahead of agent drift detection.
- **L-008:** Touches on proxy optimization under computable enforcement, but treats enforcement as a tuning parameter rather than exploring how the boundary itself becomes unstable under adversarial or scaled conditions.
- **seed-016:** Relevant to proxy collapse scenarios, but the paper does not examine failure modes where detectability itself becomes adversarially manipulated.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
