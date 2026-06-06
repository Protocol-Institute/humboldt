# Model Monotonicity in Autobidding Auctions: When Do Better Predictions Lead to Better Outcomes?

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.31036
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic study of feedback between ML model quality and auction mechanism performance in programmatic advertising. The work formalizes conditions under which improvements in pCTR/pCVR prediction accuracy translate to improvements in platform metrics (revenue, welfare) when autobidders respond strategically to those predictions.

## What I took from it

This paper investigates a genuine non-monotonicity in protocolized systems: better input information (refined models) does not guarantee better output outcomes when strategic agents adapt to that information. The insight is mechanistically interesting—it isolates the failure mode as a mismatch between prediction refinement and bidder response rationality—but remains narrowly scoped to the advertising auction domain.

The work engages with formal refinement relations (filtration-inspired), which suggests theoretical rigor, but the paper appears primarily oriented toward characterizing *when* monotonicity holds rather than deriving a novel structural principle. The contribution is domain-specific problem-solving rather than a foundational claim about feedback loops in adaptive systems more broadly. No indication that the mechanism generalizes beyond autobidding or that it challenges existing theory in computational mechanism design.

## Research connections

- **Feedback & adaptation in protocolized systems:** Paper touches on the feedback loop between model quality and agent strategy, but does not develop a general theory of non-monotonicity across system types.

## Candidate laws or signals

none
