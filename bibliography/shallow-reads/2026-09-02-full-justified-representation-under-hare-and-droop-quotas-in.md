# Full Justified Representation under Hare and Droop Quotas in Polynomial Time

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.05417
**Date read:** 2026-09-02
**Connected to:** L-003, L-001
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational social choice paper introducing a polynomial-time algorithm for computing committees that satisfy Full Justified Representation (FJR) under two distinct quota conventions (Hare and Droop). The work formalizes a fairness axiom in multiwinner voting and provides a descending-budget mechanism that achieves it under different price-setting regimes.

## What I took from it

This is a competent formalization paper, not a primary theoretical or empirical investigation of protocol behavior under adoption or stress. It advances the computational tractability of a fairness criterion rather than investigating how that criterion behaves once institutionalized. The paper does not examine what happens when FJR-compliance becomes a legible, enforced obligation in an actual electoral system—no data on adoption barriers, no analysis of how the quota choice itself becomes contested or sticky, no mechanism for understanding what happens when the fairness axiom conflicts with other institutional pressures (speed, auditability, voter preference intensity).

The implicit assumption throughout is that a cleaner, more formally justified algorithm will be preferred if computable. This is precisely the kind of move that feeds L-003 and L-001, but the paper itself does not theorize those dynamics. It is a tool enabling formalization, not an investigation of what formalization does to a coordination system once deployed.

## Research connections

- **L-003 [Formalization Ratchet]:** The paper demonstrates how an informal fairness intuition (justified representation) becomes formally specified and algorithmically executable, but does not ask whether this formalization locks the criterion in place or makes amendment harder.

- **L-001 [Protocol Ossification Under Adoption Pressure]:** The algorithm's polynomial-time tractability lowers the adoption barrier for FJR compliance, but the paper does not investigate whether widespread adoption of this specific formalization creates lock-in around the Hare/Droop distinction or makes switching costs prohibitive.

- **seed-062 [Formalization Opacity Collapse]:** By rendering fairness as a computable property with explicit price mechanisms, the paper exemplifies how informal judgment becomes legible to optimization, but does not track whether this legibility then becomes a target.

- none

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
