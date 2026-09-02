# Beyond Self-Resolution: Settlement Factorization for Robust Natural Language Mechanism

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.04382
**Date read:** 2026-09-01
**Connected to:** L-004, L-008, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design paper proposing settlement factorization: a protocol architecture that separates (1) the advice input layer from (2) the scoring/evaluation layer, preventing advisers from writing the answer key against which they are measured. The work treats natural language advice in paid forecasting and recommendation systems, addressing the circularity problem where an adviser could influence both the decision and the label used to judge them.

## What I took from it

The paper is technically sound and addresses a real structural problem in advice-taking protocols. Settlement factorization is a concrete instantiation of L-004 (Goodhart Generalization) — by physically separating report hardening from label production, it attempts to prevent metric capture through architectural constraint rather than trust or incentive alignment alone.

However, the work is fundamentally a design solution to a known problem class, not an investigation of *how or why* the problem emerges at scale, or what happens when the separation itself becomes a target for optimization. The paper does not examine whether external label production creates new failure modes (e.g., label drift, collusion between decision-maker and external labeler, or systematic misalignment between advice and externally-produced ground truth). It is silent on whether factorization costs scale, whether protocols adopting it face ossification pressure (L-001), or whether the intervention displaces the optimization locus rather than eliminating it (L-012).

## Research connections

- **L-004:** Confirms the existence of metric capture in advice protocols; proposes architectural separation as mitigation but does not explore whether the separation itself becomes gamed.
- **L-008:** Tangentially relevant — as advice signals become more precisely computable and enforceable, capture pressure increases; factorization is a response, but the paper doesn't measure whether enforcement legibility shifts optimization to the labeling layer.
- **L-012:** Relevant but underdeveloped — the paper does not ask whether externalizing label production simply moves the decision pressure from the adviser to the labeler, creating a new intervention layer vulnerable to capture.
- **seed-014 (if extant):** The separation itself becomes a "protocol boundary" where political/institutional choice is frozen; the paper treats label production as neutral but does not examine whose interests the external labeler serves.

## Seed

**Seed title:** Factorization as Capture Displacement, Not Elimination

**Seed type:** question

**Seed text:** When advice-evaluation protocols are factorized to prevent self-scoring, does the optimization pressure migrate from the adviser-scorer loop to the decision-maker–external-labeler loop? Under what conditions does externalized labeling introduce *new* misalignment (e.g., label drift, institutional capture of the labeler, systematic inversion of ground truth) that exceeds the original self-resolution hazard? The generalization: architectural separation of measurement from decision in any protocol system may relocate rather than resolve Goodhart capture—the relevant question is not whether factorization works in isolation, but whether it is stable under pressure to optimize the new boundary.
