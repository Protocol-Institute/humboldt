# LLMs as Teaching Assistants for Mathematics Exam Grading: Reliability, and Practical Usability

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.01247
**Date read:** 2026-09-01
**Connected to:** L-004, seed-019
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** —

## What this is

An empirical evaluation paper testing LLM performance on a bounded task (grading open-ended mathematics exams against rubrics). The work measures reliability across model variants and practical usability for instructors, but does not present a sustained theoretical argument about protocol behavior or propose a mechanism absent from current inventory.

## What I took from it

This is a case study in proxy substitution — the paper evaluates whether a measurable signal (LLM grade agreement with rubrics) can replace an unmeasurable goal (detecting student mathematical understanding and misconception repair). The research confirms the practical bind described in L-004 and seed-019: once grading rubrics are formalized for human consistency, they become legible targets for optimization. The paper's finding (likely) shows variance in how different LLMs capture rubric intent, which is consistent with Goodhart-type capture under computational enforcement, but the paper does not examine *why* capture occurs or how it propagates into downstream incentives on students or instruction.

The work is valuable as a case marker (education is a new domain applying protocol-like systems to unmeasurable goods) but does not engage with the structural mechanisms driving capture or the institutional feedback loops that emerge when grading becomes algorithmic. It documents a symptom, not the law.

## Research connections

- **L-004:** Confirms the category (measurable proxy for unmeasurable goal under computational optimization pressure) but does not investigate the capture mechanism or generalization across domains.
- **seed-019:** Embedded explanation opacity — LLM grading may produce rubric-compliant scores without transparent reasoning about misconception repair, deepening the gap between formal compliance and pedagogical intent.

## Method note

This type of bounded empirical evaluation is essential for *identifying* where proxy capture occurs in practice, but the research design does not isolate the *structural conditions* that make capture inevitable versus contingent. Future work should compare outcomes in domains where rubrics are loose versus tight, and measure whether algorithmic grading shifts instructor behavior toward rubric-gaming. The pattern suggests that protocol papers should include a section on "what does optimization pressure on this proxy do to the unmeasurable outcome?" — a gap most tool/case papers leave unfilled.
