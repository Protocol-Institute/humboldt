# Positive and Negative Determinant Strategies in Repeated Games with Behavior-Value Inconsistency

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.00625
**Date read:** 2026-09-01
**Connected to:** L-009
**Kind:** content
**Escalation:** store-only

## What this is

A game-theoretic study extending zero-determinant (ZD) strategies to a setting where agents incur internal costs when behavior diverges from internal belief or intent. The work models repeated games under a new cost structure: agents pay a penalty not just for outcome loss but for self-inconsistency, then analyzes how ZD strategies (which allow unilateral payoff control) behave under this constraint.

## What I took from it

The paper treats behavior-value inconsistency as a computable cost, which is tractable but orthogonal to the open inquiry L-009 (Catastrophic Risk Cancellation in Symmetric Racing Protocols). L-009 concerns the risk profile of competitive races where first-mover advantage is concentrated but failure costs are shared; this work addresses consistency penalties in repeated bilateral interaction, a different strategic geometry.

The introduction of internal cost as a legible constraint is mechanically interesting but doesn't yet clarify how symmetric racing protocols exhibit risk cancellation, nor does it model the concentrated-payoff asymmetry central to L-009. The frame is individual rationality under self-consistency; the racing question is about collective risk under asymmetric prize and failure structures. The work may eventually inform how agents in racing scenarios internalize or disguise inconsistency, but the current model does not generalize to competitive deployment pressure or distributed protocol adoption.

## Research connections

- **L-009:** Tangentially relevant—ZD strategies with behavioral costs might apply to racing scenarios, but the paper models bilateral repeated games, not multi-agent competitive races with asymmetric payoffs.
- **L-004 (Goodhart Generalization):** The internal cost for behavior-value inconsistency is itself a new measurable proxy; worth noting whether agents can game consistency metrics.
- **seed-049 (Consensus-Reasoning Decoupling):** The decoupling of behavior from internal value parallels the machinery here; unclear if seed-049 applies or if the consistency cost prevents true decoupling.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
