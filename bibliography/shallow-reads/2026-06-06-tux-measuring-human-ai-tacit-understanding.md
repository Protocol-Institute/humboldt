# TUX: Measuring Human–AI Tacit Understanding

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2605.30930
**Date read:** 2026-01-15
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement framework for tacit alignment—whether LLMs can infer and match human evaluative stances without explicit instruction or reward signals. The work adapts a social party game (Wavelength) as a probe task, treating collaborative understanding as a measurable phenomenon distinct from task success or explicit optimization.

## What I took from it

The paper makes a useful phenomenological distinction: explicit alignment (via reward, instruction, loss functions) versus *tacit* alignment (inferring unstated priors, evaluative frames, representational schemes). This is valuable for studying how protocolized systems navigate underdetermined collaborative contexts where humans operate on implicit shared context.

However, the work remains primarily a *measurement tool* rather than a theory-building exercise. It identifies a gap in evaluation methodology—we don't have standard tasks for probing implicit coordination—but doesn't propose a generative mechanism for *why* or *how* tacit understanding emerges, nor does it test whether the capacity scales predictably or relates to other known properties of LLM cognition. The Wavelength task is a domain-specific probe, useful for benchmarking but not yet evidence of a general principle about alignment in artificial systems.

## Research connections

- **None currently**: No established laws or active hypotheses against which to test this work.

## Candidate laws or signals

- **CL-TUX-1:** *Tacit alignment capacity may decouple from explicit task performance*—systems can succeed on stated objectives while failing to infer unstated evaluative priors, suggesting alignment involves distinct, testable subsystems.
