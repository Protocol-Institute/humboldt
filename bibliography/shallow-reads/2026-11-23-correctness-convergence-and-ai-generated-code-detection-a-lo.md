# Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.00863
**Date read:** 2026-11-23
**Connected to:** L-013, seed-528
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study comparing student-generated and LLM-generated code across three cohorts (2021, 2023, 2025) to test whether code matching against a reference bank of LLM solutions can reliably detect AI use. The core finding is that many "matches" arise not from copying but from constraint-driven convergence: when a problem admits only a few natural implementations, students and LLMs independently produce identical or near-identical code, rendering match-based detection unreliable as a detection signal.

## What I took from it

This is a narrow competence study in academic integrity detection, not a primary theoretical contribution to protocol dynamics. However, it documents a concrete instance of **audit-trail brittleness**: the paper shows that a formally legible detection criterion (code-to-reference matching) loses discriminative power precisely when optimization pressure increases (more LLM use, tighter assignment constraints). This is an observation, not a mechanism analysis.

The work confirms that formalized detection proxies degrade under adoption pressure, but it does not develop a theory of *why* this happens at the protocol level, nor does it generalize beyond plagiarism detection. The finding—that convergence under constraint mimics copying—is domain-specific and does not establish a law-shaped regularity about protocol systems broadly.

## Research connections

- **L-013 (Paradigm-Locked Anomaly Tolerance):** The paper shows that institutions may continue to rely on code-matching detection even after evidence accumulates that it conflates convergence with copying; however, the paper does not study institutional tolerance or explain why the paradigm persists.
- **seed-528 (referenced in triage note, not in pool):** Detection via audit criteria ossification — the matching criterion becomes rigid and legible but loses fidelity as the problem space saturates.

## Seed

**Seed title:** Constraint-Driven Convergence Mimics Copying Under Audit Legibility

**Seed type:** observation

**Seed text:** When a protocol's audit criterion (e.g., code matching) is formalized as a legible detection signal, the criterion loses discriminative power in environments where the solution space is naturally constrained. Under adoption pressure, the conflation of convergence with copying becomes harder to detect retrospectively, and audit systems may tolerate this ambiguity rather than reformulate the detection rule. The generalization: any formalized audit proxy becomes unreliable when the underlying task permits only a few natural solutions, independent of domain — this pattern should hold in procurement fraud detection, financial compliance matching, and policy conformance auditing.
