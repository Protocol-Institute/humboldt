# Asymptotic Max-Min Fair Allocation with Random Utilities

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.19319
**Date read:** 2026-09-22
**Connected to:** L-019, seed-130
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical game theory paper deriving asymptotic characterizations of max-min fair allocation protocols for indivisible goods when agent utilities are drawn i.i.d. from a common distribution. The work analyzes the efficiency loss (welfare gap between max-min fairness and utilitarian optimality) under conditions of scaling and distribution tail-lightness.

## What I took from it

This is a clean mathematical treatment of a classical fairness-efficiency tradeoff, but it operates entirely within the space of *design choice* rather than *protocol dynamics*. The paper assumes utilities are exogenous and fixed; agents do not adapt, strategize, or modify their preferences in response to the allocation protocol. It therefore does not engage with the core mechanisms of the new nature: the interaction between formalization pressure and agent behavior under computable enforcement.

The result confirms a known intuition (max-min fairness degrades aggregate welfare) but does not generate evidence about how protocols *change* when exposed to adversarial optimization, how fairness metrics become targets for capture (L-004), or how heterogeneous preference structures resist compression into scalar allocation functions (L-019). The asymptotic regime studied is mathematically elegant but orthogonal to questions of stability, norm erosion, or strategic boundary concentration.

## Research connections

- **L-019:** The paper addresses preference aggregation (max-min fairness as an aggregation rule), but treats preferences as static and non-strategic. It provides no evidence on rationalizability collapse or metric capture under endogenous agent response.
- **seed-130:** The work does not examine how heterogeneous sufficiency (agents with different utility scales or distributions) displaces protocol boundaries or forces representational restructuring.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
