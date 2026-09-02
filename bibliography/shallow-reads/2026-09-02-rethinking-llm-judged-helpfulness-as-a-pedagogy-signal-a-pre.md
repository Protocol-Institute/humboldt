# Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.28128
**Date read:** 2026-09-02
**Connected to:** L-004, L-015
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:**

## What this is

A pre-registered empirical audit testing whether LLM-based helpfulness judgments can reliably distinguish pedagogical guidance from direct answer-giving in tutoring contexts. The work uses deterministic detectors and frozen judges (Claude Opus as primary evaluator) to measure whether a general-purpose rubric captures pedagogical intent or collapses to answer leakage detection.

## What I took from it

This is a **measurement-validity study**, not a theoretical contribution. It documents a specific failure mode of proxy judgment in distributed evaluation systems — that LLM judges trained on "helpfulness" may not discriminate the pedagogical signal they are meant to capture. The pre-registration and use of a frozen judge are methodologically sound, but the paper appears to be a bounded audit rather than a mechanism discovery or law-forming argument.

The work confirms the *existence* of L-004 (Goodhart Generalization) in the specific domain of pedagogical evaluation, and touches on L-015 (Interpretive Continuity Decay) insofar as the rubric may survive formally intact while its operational meaning (pedagogical vs. direct) diverges. However, it does not explain *why* the proxy captures poorly, does not generalize the mechanism beyond tutoring systems, and does not propose a countervailing principle or deeper law. It is a case study with methodological rigor, not a sustained theoretical or empirical argument for a new mechanism.

## Research connections

- **L-004:** Confirms that measurable helpfulness proxies in tutoring contexts are subject to capture when the ground truth (pedagogical efficacy) remains unmeasurable and the proxy (LLM judgment) optimizes for surface-level features.
- **L-015:** Raises the question of whether formal audit trails (frozen judge scores) can preserve nominal continuity while interpretive alignment (what "helpful" means across judges) decays — but does not develop this.
- **seed-069:** Tangentially relevant: transparency (showing answer vs. guidance) may substitute for trust in asymmetric-knowledge protocols (student-tutor), but this is not explored.

## Method note

This work demonstrates a valuable pattern: pre-registration + frozen primary judge + deterministic secondary detectors is a sound architecture for auditing proxy validity in distributed systems. However, the audit design assumes the rubric's *existence* is the problem, not its *capture under optimization*. Future work should vary the judge (not freeze it) and the optimization target to isolate whether the failure is measurement error, proxy collapse, or paradigm lock. The methodology is strong for falsification but weak for mechanism discovery — it shows *that* helpfulness judgments fail to capture pedagogy, but not *why* or under what conditions the failure becomes systematic.
