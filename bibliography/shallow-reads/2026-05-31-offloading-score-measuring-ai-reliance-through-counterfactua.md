# Offloading Score: Measuring AI Reliance Through Counterfactual Workflows

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2605.29392
**Date read:** 2026-05-31
**Connected to:** L-004, H-001
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper introducing a measurement framework for quantifying human-AI task distribution through counterfactual workflow simulation, rather than output adoption or self-report. The core contribution is a metric (offloading score) that estimates the fraction of cognitive effort displaced to the AI tool by constructing what-would-have-been baselines.

## What I took from it

This is primarily a measurement/instrumentation contribution rather than a law-bearing theoretical argument. It advances the *operationalization* of reliance but does not itself theorize why reliance patterns emerge or how they scale. The counterfactual methodology is sound for L-004 adjacency—it could be used to detect metric capture in workflows where effort distribution diverges from actual goal achievement—but the paper does not sustain that argument. 

On H-001 (coordination cost conservation across layers), the work is tangential. It measures *within-layer* effort distribution (human vs. AI cognitive load) but does not compare cost when coordination protocol changes—e.g., does effort saved at the execution layer reappear as verification overhead, or as new coordination friction? The paper documents the offloading itself without tracking whether total protocol cost is invariant.

The work is useful as a measurement substrate for future hypothesis testing, but it does not itself present a sustained empirical or theoretical claim about the laws governing artificial systems.

## Research connections

- **L-004:** Offloading score could detect when AI adoption metrics (e.g., tool usage frequency) diverge from actual effort displacement, a signature of metric capture. Not explored in this work.
- **H-001:** Measures single-layer effort distribution but does not track cost conservation across protocol transitions (e.g., does reduced user effort create new coordination or verification costs?).

## Candidate laws or signals

none
