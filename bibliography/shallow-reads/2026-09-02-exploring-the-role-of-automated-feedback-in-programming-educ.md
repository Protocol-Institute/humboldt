# Exploring the Role of Automated Feedback in Programming Education: A Systematic Literature Review

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2602.00089
**Date read:** 2026-09-02
**Connected to:** L-003, seed-016
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systematic literature review (61 empirical studies through Sept 2024) synthesizing research on automated feedback systems in programming education. The work maps technological and instructional dimensions of feedback automation but does not present sustained theoretical argument about protocol dynamics or mechanisms absent from current inventory.

## What I took from it

This is a survey artifact documenting a domain where formalization pressure is active and visible—pedagogical feedback norms being encoded into computable systems. The triage note correctly identifies L-003 (Formalization Ratchet) as operative: as feedback becomes automated, informal instructor judgment gets replaced by legible, scalable proxies (test-case pass/fail, style checkers, constraint validators). 

However, the paper itself appears to be descriptive synthesis rather than mechanistic investigation. It catalogs *what systems do* and *how they're deployed* but does not isolate why formalization happens under stress, what gets lost in the transition, or how the ratchet locks. This is a natural domain for observing L-003 in action (educational scaling = stress condition), but the paper does not theorize the mechanism or trace its consequences for protocol drift.

## Research connections

- **L-003:** Automated feedback systems exemplify formalization under adoption/scaling pressure in educational coordination, but this review does not isolate the ratchet mechanism or irreversibility conditions.
- **seed-016:** (Not visible in context; triage flagged it—likely concerns metric capture or legibility in learning assessment.)
- **seed-062:** Formalization of pedagogical judgment into computable feedback may exhibit "automation legibility"—what becomes visible/measurable in the system vs. what was legible to informal judgment.
- **L-004:** Risk that automated feedback proxies (code style, test coverage, submission speed) become optimization targets decoupled from actual learning outcomes.

## Method note

This review reveals a common pattern: domain surveys of *applied protocolized systems* accumulate rich descriptive data but rarely isolate causal mechanisms or generative principles. To serve law induction, future syntheses in this space should explicitly map: (1) what coordination norm existed before formalization, (2) what legibility was gained/lost in encoding it, (3) whether the formal system resists re-informalization. A shallow read of 61 studies cannot do this work—but a deeper analysis of a smaller subset, tracking formalization trajectories longitudinally within institutions, could seed L-003 validation or challenge.
