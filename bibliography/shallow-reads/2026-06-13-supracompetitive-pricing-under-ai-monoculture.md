# Supracompetitive Pricing Under AI Monoculture

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2601.01279
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary theoretical source demonstrating a mechanism (emergent collusion via shared model architecture and feedback aggregation) absent from current inventory, with generalization potential beyond pricing to any multi-agent system using shared learned models.

## What this is

A game-theoretic model of duopoly pricing where competing sellers delegate to a shared AI system. The paper argues that standard deployment practices—correlated recommendations from a single model plus performance-driven updates aggregating seller feedback—can produce supracompetitive (collusive) pricing outcomes without explicit coordination.

## What I took from it

This addresses a genuine gap in how we model artificial systems: the emergence of coordination effects not through agent design but through the *shared substrate* itself. The mechanism appears to be twofold: (1) a shared model naturally produces correlated outputs, reducing price variance across competitors, and (2) feedback aggregation (learning from collective performance signals) reinforces high-price equilibria because both sellers benefit when prices rise together.

This is foundational to understanding "new nature" because it reveals that **monoculture in artificial systems—using a single model across competing entities—acts as a latent coordination device**. It's not collusion by design; it's collusion by architecture. The pattern likely generalizes beyond pricing to any resource-allocation, bidding, or strategic setting where multiple agents share a learned model and aggregate feedback.

## Research connections

None yet (fresh domain entry).

## Candidate laws or signals

- **CL-2601.01279-1:** *Shared learned models in multi-agent systems tend toward correlated equilibria; feedback aggregation across agents reinforces extremal outcomes (high prices, low diversity) without explicit coordination protocols.*
