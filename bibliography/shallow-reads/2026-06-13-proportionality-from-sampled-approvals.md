# Proportionality from Sampled Approvals

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.10446
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical computer science paper analyzing sample complexity bounds for proportional representation in multiwinner elections. The work derives polynomial sampling requirements (Õ(k⁵ log m/δ)) needed to guarantee justified representation axioms hold when voter ballots are drawn from a population rather than collected exhaustively.

## What I took from it

This is primarily a complexity result within established algorithmic social choice theory—it characterizes the *cost* of achieving a known desideratum (proportionality via JR) under a specific constraint (sampling). The contribution is technical: mapping the sample-to-accuracy tradeoff for a family of voting rules.

For the new nature agenda, this does *not* present a mechanism absent from inventory, nor does it challenge or extend a law. It operates within the axiom-driven design paradigm of multiwinner voting, where proportionality is pre-defined and the problem is implementation. The pattern (sample complexity scaling) is narrow to this domain and doesn't generalize to protocolized systems beyond electoral contexts without substantial translation work.

The paper answers an engineering question—how many ballots do we need?—rather than discovering an emergent law or failure mode of these systems under natural conditions.

## Research connections

- none

## Candidate laws or signals

none
