# The Art of Calling the Winner by Asking Just Enough Questions: Competitive Preference Elicitation with Next-Best Queries

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.29087
**Date read:** 2026-09-02
**Connected to:** L-003, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational game theory paper studying active preference elicitation under voting rules, where an algorithm queries agents for their next-favorite alternative and measures competitive ratio (worst-case queries needed vs. hindsight minimum). The work develops query strategies for sublinear competitive ratios across multiple voting rules.

## What I took from it

This is a bounded algorithmic contribution to a specific technical problem (query efficiency in preference aggregation), not a sustained theoretical or empirical investigation of protocol dynamics. The paper does not examine how formalization of preference-revelation affects agent behavior, nor does it model adoption feedback loops or institutional consequences of moving from informal to computable preference aggregation.

The connection to L-003 (Formalization Ratchet) is weak: the paper takes formalized preference elicitation as a design goal, not as a phenomenon to interrogate. It does not show *why* informal preference coordination would be replaced by structured queries under stress, or what happens to coordination norms in the transition. Similarly, L-010 (Coordination Adoption Nonmonotonicity) would require the paper to model *agent choice* to participate in the protocol as a function of others' participation—this paper assumes participation and optimizes query efficiency.

The work is clean engineering within an assumed frame, not investigation of the frame's emergence or pathology.

## Research connections

- **L-003:** Formalization Ratchet — Paper assumes preference formalization as design goal, does not interrogate when or why informal coordination norms are replaced by computable elicitation protocols.
- **L-010:** Coordination Adoption Nonmonotonicity — Paper does not model agent participation decisions as a function of others' adoption; assumes fixed participation.
- none (seed pool)

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
