# Dynamic Pooling and Regional Participation in Deceased-Donor Organ Allocation

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.18147
**Date read:** 2026-11-23
**Connected to:** L-006, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of transitions from regional to pooled organ allocation systems, using multiclass queueing models to characterize Pareto gains and participation incentives. The work is a domain-specific application paper: it models a real coordination problem (organ allocation) but does not establish a mechanism absent from the current inventory or generalize beyond transplantation policy.

## What I took from it

The paper operationalizes a concrete instance of L-006 (Coordination Cost Conservation) and L-010 (Coordination Adoption Nonmonotonicity): pooling reduces total matching waste but redistributes regional advantage, creating asymmetric incentive profiles that can suppress adoption even when aggregate welfare rises. The dynamic queueing framing captures *when* agents condition participation on coordination signals from other regions—specifically, regional fairness outcomes rather than global efficiency.

However, the analysis remains within transplantation mechanics. It does not challenge or extend the laws themselves; it confirms their application to a new domain. The regional participation resistance is treated as a known incentive problem, not a novel mechanism. The paper acknowledges the tension between pooling efficiency and regional defection but does not expose a deeper pattern about how coordination cost conservation produces adoption barriers in protocol transitions generally.

## Research connections

- **L-006:** Pooling reallocates coordination cost from match-finding to regional fairness negotiation; total cost does not decrease.
- **L-010:** Regional agents adopt pooling conditionally on fairness signals from other regions, producing the nonmonotonic adoption curve the paper observes.
- **seed-467 (Coordination Structure Elasticity Under Difficulty Variance):** Regional participation variance in pooling scales with difficulty of local match-finding; softer regions defect first.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
