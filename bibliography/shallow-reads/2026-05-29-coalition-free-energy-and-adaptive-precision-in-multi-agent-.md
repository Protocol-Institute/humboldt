# Coalition Free Energy and Adaptive Precision in Multi-Agent Cooperation

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.26278
**Date read:** 2026-05-29
**Connected to:** H-001, L-003
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper introducing the Game-Theoretic Free Energy Principle (GT-FEP) to model coalition formation in multi-agent systems. It derives precision-dependent credit assignment rules showing that agents' Shapley values exhibit non-monotonic relationships with sensory precision, revealing trade-offs between inference noise and overconfidence.

## What I took from it

This work is primarily a *formal extension* of existing game theory (Shapley values + precision-weighting), not a primary theoretical claim about how protocolized systems behave under real constraints. While the framing invokes uncertainty and precision in coordination, the paper operates within classical GT assumptions (rationality, full information about payoff structures) and does not engage with the empirical or quasi-empirical study of actual protocol adoption, ossification, or formalization pressures that characterize the "new nature" research agenda.

The precision-dependent Shapley formulation is mathematically interesting but does not test H-001 (coordination cost conservation across layers) in any operational sense—it models an abstract trade-off in a single decision-theoretic layer. There is no evidence that this framework predicts or explains the costs observed when protocols scale, fork, or compete in real adoption contexts. Similarly, while the paper touches on adaptive mechanisms, it does not engage with L-003 (formalization ratchet) as a falsifiable claim about how informal coordination degrades under stress in specific domains.

## Research connections

- **H-001:** The paper's precision-dependent credit model does not address whether coordination costs are conserved when shifting between protocol layers (e.g., governance → execution → verification); it remains within a single mathematical layer.
- **L-003:** No direct test of whether informal coordination norms are replaced by explicit protocols under pressure; the work assumes formal game-theoretic structure throughout.

## Candidate laws or signals

None. This is a sound but incremental contribution to game-theoretic foundations. It does not reveal a pattern in how actual protocolized systems degrade, ossify, or formalize under real-world adoption or scaling pressure.
