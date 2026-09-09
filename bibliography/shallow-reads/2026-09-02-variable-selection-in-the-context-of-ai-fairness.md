# Variable Selection in the Context of AI Fairness

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.11251
**Date read:** 2026-09-02
**Connected to:** L-003, L-004
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** —

## What this is

A position paper advocating for interdisciplinary (mathematical + ethical + regulatory) approaches to fairness in AI variable selection. The work frames variable selection as a site where informal ethical norms must be embedded into formal systems under regulatory pressure (EU AI Act), and claims traditional mathematical approaches miss philosophical and social awareness.

## What I took from it

The paper identifies variable selection as a formalization site, which is directly relevant to L-003 (Formalization Ratchet) and L-004 (Goodhart Generalization). However, the argument appears *descriptive and prescriptive* rather than *predictive or mechanistic*. It diagnoses that informal norms (philosophical ethics, social awareness) are lost when formalizing fairness into mathematical variable selection procedures — and recommends interdisciplinary collaboration as remedy. This is a statement of the problem, not an account of why the formalization ratchet occurs or what happens when informal norms collide with computable enforcement.

The paper does not provide sustained empirical evidence or a causal mechanism for how regulatory pressure specifically drives ossification of variable selection choices, nor does it characterize what happens when multiple stakeholders formally codify *conflicting* ethical intuitions into competing fairness metrics. It reads as advocacy rather than investigation of a law.

## Research connections

- **L-003:** Identifies a formalization site (variable selection under regulatory pressure), but does not characterize the mechanism of norm replacement or predict post-formalization behavior.
- **L-004:** Touches on metric capture implicitly (fairness metrics as proxies for unmeasurable ethical goods), but does not study optimization pressure or drift.
- **seed-069:** Tangentially relevant: framing transparency/formalization as substitution for trust, though not developed.
- **seed-071:** Relevant to governance residuals — ethical intuitions that resist formalization into mathematical procedures.

## Method note

This paper exemplifies a common research failure mode in this domain: identification of a design problem without characterization of the system law governing it. The recommendation for "interdisciplinary collaboration" is a solution proposal, not a research output. For the new nature research agenda, we should be alert to papers that diagnose formalization failures but do not predict what systems *will do* when informal norms are forced into computable form under pressure — that is where mechanistic work begins. This read suggests we need empirical studies tracking what happens to variable selection procedures *after* regulatory formalization, not prescriptions for how to design the process better.
