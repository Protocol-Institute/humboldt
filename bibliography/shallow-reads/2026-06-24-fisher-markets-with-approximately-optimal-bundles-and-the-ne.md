# Fisher Markets with Approximately Optimal Bundles and the Need for a PCP Theorem for PPAD

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2604.27276
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational complexity paper establishing hardness results for equilibrium computation in Fisher markets under relaxed optimality constraints. The work shows that even when buyers accept approximately optimal bundles (rather than perfectly optimal ones), finding competitive equilibrium remains PPAD-hard under a conjectured complexity assumption (PCP-for-PPAD).

## What I took from it

This paper is a negative result within established economic game theory, not a characterization of protocolized system behavior itself. It demonstrates that the *computational boundary* of market equilibrium doesn't shift meaningfully when relaxing the equilibrium notion—a hardness result persists. This is relevant to understanding the cost structure of protocol design, but does not present a generative mechanism governing artificial systems, nor does it challenge or extend a law about their behavior. The result is domain-specific (Fisher markets with SPLC utilities) and does not appear to generalize to other protocol families or shed light on emergent properties of artificial systems more broadly.

The hardness holds even under symmetry (equal budgets), which slightly constrains where tractability might hide—but this is refinement within existing complexity taxonomy, not discovery of new protocol dynamics.

## Research connections

- none identified

## Candidate laws or signals

none
