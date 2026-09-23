# BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.16305
**Date read:** 2026-09-22
**Connected to:** L-001, L-013, seed-149
**Kind:** benchmark / evaluation paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing a trajectory-level evaluation framework for safety behavior in multi-turn LLM agents with tool access. The work identifies that safety failures in long-horizon settings emerge from interaction sequences rather than single turns, and proposes measurement of calibration (act/refuse/defer patterns) across evolving authorization and state contexts.

## What I took from it

This is a competent problem-framing paper that names a real gap — existing benchmarks flatten trajectory-level safety into binary task/attack outcomes, missing the distributed, sequential character of safety failure. The observation that "safety failures may emerge only after multiple turns" aligns with L-013 (paradigm-locked protocols tolerating accumulating evidence of malfunction). However, the paper itself remains within the evaluation/measurement domain: it proposes *how to measure* long-horizon safety calibration, not *why protocols fail under those conditions* or *what mechanism governs the emergence of safety violations across turns*. The benchmark is a tool, not a theory. The implicit mechanism — that safety properties are not compositional across turns — is noted but not explored. No sustained argument about protocol structure, incentive dynamics, or formalization effects; no evidence that the pattern generalizes beyond LLM agents.

## Research connections

- **L-001 (Protocol Ossification):** Not directly engaged. Calibration drift is measured but not explained as resistance to real-time safety adjustments.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** Weak alignment — the multi-turn emergence of failures suggests distributed anomalies that established safety paradigms may not detect, but the paper does not theorize this.
- **seed-149:** Triage reference only; no evidence of substantive connection in abstract.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
