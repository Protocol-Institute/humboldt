# Moral Entropy: Auditing Bias and Uncertainty in Moral Judgment

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.21992
**Date read:** 2026-09-22
**Connected to:** L-004, L-019, seed-150
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A Bayesian framework paper proposing that annotator disagreement on moral judgments should be preserved as uncertainty rather than collapsed into majority votes. The work decomposes disagreement entropy into aleatoric (irreducible moral pluralism) and epistemic (noise/insufficiency) components, treating moral labeling as a posterior estimation problem rather than a consensus problem.

## What I took from it

The paper documents a real empirical phenomenon — that treating moral judgment as a scalar classification task requires collapsing genuine moral pluralism into a single proxy target — but does not theorize the downstream consequences of this collapse. It correctly identifies that majority-vote protocols discard information about heterogeneity, but the proposed solution (keeping the full posterior) is a representation problem, not a mechanism diagnosis.

The work is orthogonal to L-004 (Goodhart Generalization) because it does not ask what happens when systems are *optimized against* the scalar moral proxy once deployed; it only documents that the proxy is lossy. It intersects L-019 (Representation-Rationalizability Tradeoff) only descriptively — showing that moral aggregation has this tradeoff — without exploring whether attempts to preserve heterogeneity (e.g., multi-dimensional moral representations) create new optimization pressures, gaming surfaces, or coordination failures. The paper is a tool/method contribution, not a primary theoretical argument about protocol behavior under stress.

## Research connections

- **L-004:** Documents that moral judgment aggregation requires proxy collapse, but does not examine what happens when systems optimize against collapsed proxies in deployment.
- **L-019:** Confirms representation-rationalizability tension exists in moral preference aggregation, but does not trace mechanism or downstream protocol effects.
- **seed-150:** Connected by triage note; aligns with legibility-driven conformity concerns, but paper treats legibility as a *representation problem* rather than an *incentive problem*.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
