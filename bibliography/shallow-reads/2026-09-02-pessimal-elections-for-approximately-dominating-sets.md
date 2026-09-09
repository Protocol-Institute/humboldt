# Pessimal Elections for Approximately Dominating Sets

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.06872
**Date read:** 2026-09-02
**Connected to:** L-004, seed-022
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper on voting protocols and committee selection, addressing Condorcet's paradox by relaxing majority thresholds. The work shows that impossibility results in social choice can be circumvented through metric relaxation—trading off decisiveness (exact majority preference) for tractability (approximate domination).

## What I took from it

This is a direct confirmation case for L-004 (Goodhart Generalization: Metric Capture) at the protocol design level, but it does not advance the mechanism or boundary conditions. The paper demonstrates the classic move: when a proxy measure (majority preference over committees) fails to capture the underlying goal (genuine collective preference), designers respond by relaxing the measurement standard itself rather than regrounding the protocol. 

What's absent here is any investigation of *what happens when agents optimize against the relaxed metric*. The paper treats the approximate domination threshold as a design lever, not as a new surface for strategic capture. In the new nature frame, this is a snapshot of a protocol *before* its metrics become legible to optimizing agents—before the relaxed threshold itself becomes a target for manipulation or gaming. The work is mathematically sound but mechanically hollow: it does not test whether the approximate-domination proxy is more or less vulnerable to capture than the original majority rule.

## Research connections

- **L-004:** Confirms the pattern—when an exact metric fails, relaxation is the default response. Does not test robustness of the relaxed metric to optimization.
- **seed-022:** Restates the observation; no new mechanism or boundary condition offered.
- **L-008:** Proxy Optimization Under Computable Enforcement — This paper shows *design-time* metric relaxation; L-008 tracks what happens when agents *operationally* optimize against the relaxed rule.

## Seed

**Seed title:** none
