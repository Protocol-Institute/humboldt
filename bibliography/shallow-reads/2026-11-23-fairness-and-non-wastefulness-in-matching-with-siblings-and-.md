# Fairness and Non-wastefulness in Matching with Siblings and Initial Enrollments: Compatibility and Complexity

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.01041
**Date read:** 2026-11-23
**Connected to:** L-019, seed-157
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic matching paper extending the school-choice literature to handle two complicating features: families with multiple children exhibiting joint preferences, and initial enrollments that constrain the feasible matching space. The authors study existence and computational complexity of matchings satisfying simultaneous fairness (stability/strategy-proofness) and efficiency (non-wastefulness) conditions.

## What I took from it

This is a constraint-satisfaction paper nested within a well-explored domain. The main result is that combining joint family preferences with initial enrollment constraints creates fundamental incompatibilities between classical fairness and efficiency desiderata — but this is a *problem impossibility* result, not a *law of protocol systems under optimization pressure*.

The paper does not investigate how agents behave when no mechanism can simultaneously guarantee fairness and efficiency, nor does it study what real systems do when these conditions collide. It does not examine how the introduction of computable fairness criteria (stability, strategy-proofness) alters agent behavior, strategic boundary concentration, or the emergence of workarounds. The technical contribution — showing that certain combinations of axioms are incompatible under these constraints — is a negative result in axiomatic mechanism design, not a regularity about how protocolized systems actually degrade, ossify, or redistribute optimization pressure when idealized goals become conflicting.

The work is competent but not generalizing beyond matching theory. It does not offer insight into the dynamics of protocol compromise, metric cascade, or how systems shift burden when formal requirements become mutually unsatisfiable.

## Research connections

- **L-019:** Tangentially: the paper identifies a *representation-rationalizability tradeoff*, but only as a static incompatibility theorem, not as a mechanism of protocol drift under optimization. No lens on how agents respond to impossibility.
- **seed-157:** Listed as connected in triage, but no mechanism visible in the abstract for how interpretability functions as coordination proxy under joint-preference constraints.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
