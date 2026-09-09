# ChatGPT Solves All Tested Qiskit Homework Assignments

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.19707
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical assessment of whether LLM-solvability of quantum computing homework can be mitigated through assignment redesign (adding seeded randomization, requiring output discussion) rather than AI restriction. The work tests three homework packages against ChatGPT to measure residual vulnerability.

## What I took from it

This is a competent defensive-design case study, but it operates entirely within the adaptive-arms-race frame rather than surfacing a mechanism. The paper's implicit claim—that *sufficient* problem-specificity and output-discussion requirements can preserve autogradability under LLM pressure—is a localized workaround, not a generalization about protocol architecture or governance.

The work *does* confirm the surface reading of L-004 and L-008: as assessment becomes more computable and legible to optimizing agents (here, LLMs), the proxy (homework completion) gets captured. But the paper's response (add noise, require discussion) is mitigation engineering, not a revelation about how protocols fail or stabilize under such pressure. No mechanism is exposed that would transfer to other protocol domains (governance, cryptography, coordination).

The deeper question—*whether formalized assessment systems are fundamentally vulnerable to capability-driven proxy capture, or whether there exists a design envelope that resists it*—remains unsettled. This paper tests one envelope boundary but doesn't interrogate the boundary itself.

## Research connections

- **L-004:** Confirms metric capture in educational assessment; LLMs optimize against homework-submission proxy under automated grading legibility.
- **L-008:** Consistent with computable enforcement enabling proxy optimization; the legible autograder becomes a predictable target.
- **seed-062:** Tangential: formalization of assessment (autogradable notebooks) enables LLM legibility; adds to the pool of observations on formalization-opacity collapse.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
