# Do job seekers value procedure in AI hiring only for error correction? Evidence from a conjoint experiment

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.16390
**Date read:** 2026-09-22
**Connected to:** L-007, seed-142
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A preregistered conjoint experiment (n=1,919 US job seekers) that orthogonally varies AI hiring procedure transparency and system performance to isolate whether applicants value procedural legibility for its own sake or instrumentally for error detection. This directly probes the mechanism underlying trust formation in automated decision systems.

## What I took from it

The paper tests a critical decomposition: does trust in automated hiring depend on *knowing the procedure works* (instrumental) or on *knowing the procedure itself* (intrinsic)? This is methodologically sound for separating L-007 dynamics (trust accumulation from operational stability) from the procedural legitimacy question. The conjoint design allows measurement of preference weights for procedure holding performance constant—a necessary experimental move that most prior work omits.

Relevance: This work sits at the boundary of seed-142 (Auditability-Legibility Trap) by empirically testing whether legibility *itself* generates trust independent of actual error correction. If job seekers prefer transparent procedures *even when they don't improve outcomes*, this would suggest that procedural legibility functions as a trust proxy decoupled from actual safety—a mechanism that could lock in suboptimal but opaque protocols. Conversely, if procedure only matters when it demonstrably reduces errors, the trust signal remains correlated with actual system quality, weakening the trap hypothesis.

## Research connections

- **L-007:** Empirically disaggregates trust sources—whether applicants trust based on age/stability (L-007) or based on procedure transparency. If procedure matters *more* than demonstrated performance, suggests trust is legibility-driven rather than performance-driven.
- **seed-142:** Direct empirical probe of whether auditability itself (independent of actual error reduction) becomes the salient trust marker, locking stakeholders into demanding legibility over actual safety gains.
- **seed-143:** Related—tests whether forensic legibility satisfies trust demands even absent threshold verification of actual accuracy.

## Method note

This work models a necessary experimental practice for the new nature research agenda: orthogonal factorization of confounded design dimensions. Most field observations conflate procedure transparency with system performance; conjoint designs separate these. For protocol research, this suggests that whenever we observe "trust" or "acceptance" of an automated system, we should experimentally ask whether the observed preference is for the *mechanism itself* or for the *measurable outcomes it produces*. This decomposition is especially critical for testing whether legibility becomes a substitute for, rather than a signal of, actual safety.
