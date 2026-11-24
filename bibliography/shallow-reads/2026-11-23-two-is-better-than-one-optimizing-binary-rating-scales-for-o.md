# Two is better than one: optimizing binary rating scales for online platforms

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2611.23626
**Date read:** 2026-11-23
**Connected to:** L-004, seed-023
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic optimization paper proposing that platform designers can improve rating informativeness by deploying *heterogeneous* rating scales across different user populations rather than optimizing a single uniform scale. The work treats rating design as a mechanism design problem under binary feedback constraints.

## What I took from it

The paper is narrowly focused on signal extraction efficiency given fixed user behavior—a technical contribution to platform mechanism design. It does not investigate how heterogeneous rating scales affect user behavior, coordination, or the deeper dynamics of metric capture that L-004 tracks.

The proposal to fragment rating scales by user cohort is instrumentally reasonable but represents the *opposite* direction from the dynamics we're tracking. L-004 concerns *metric capture under optimization pressure*—the tendency for measurable proxies to degrade as agents learn the measurement function. This paper assumes measurement function is fixed and designer-controlled; it does not address what happens when users discover they face different scales, or when platforms iteratively retrain scales in response to observed gaming. Seed-023 (informality as novelty sink) is tangentially relevant: heterogeneous scales could suppress convergence to uniform informal norms, but the paper offers no evidence on this, and the mechanism is orthogonal to their contribution.

This is competent technical work. It does not generalize beyond the narrow question of optimal rating scale parameterization.

## Research connections

- **L-004:** Tangential. The paper optimizes *within* metric capture but does not investigate capture dynamics or agent responses to measurement heterogeneity.
- **seed-023:** Tangential. Heterogeneous scales could affect informality, but no mechanism or evidence is offered.

## Seed

**Seed title:** none
