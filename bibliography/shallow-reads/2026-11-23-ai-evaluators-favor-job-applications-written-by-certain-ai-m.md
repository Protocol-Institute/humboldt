# AI evaluators favor job applications written by certain AI models, independent of candidate quality

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.41866
**Date read:** 2026-11-23
**Connected to:** L-004, seed-466
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit study demonstrating that LLM-based hiring evaluators systematically prefer job applications written by specific AI writer models, independent of the underlying candidate qualifications or application quality. The work deploys a multi-model framework (11 writer agents × 9 evaluator agents) to isolate model choice as a signal independent of content.

## What I took from it

This is a crisp instantiation of Goodhart Generalization (L-004) in a narrow domain: when the evaluation function becomes legible and automated, the *choice of encoding tool* becomes a proxy for quality independent of the actual measured construct. The finding is clean but domain-bound: it shows preference hierarchy emergence in hiring, not a generalizable mechanism about protocol systems writ large.

The work does not investigate *why* evaluators prefer certain writer models, nor does it trace the downstream coordination effects or adoption dynamics that would constitute a law. It is a well-executed benchmark-style audit: "does X happen?" Yes. The answer is narrow and doesn't expose a mechanism that would transfer to other protocol contexts (governance, consensus, verification, etc.).

The work confirms L-004's prediction locally but does not extend, challenge, or ground it. It does not engage the conditions under which metric capture *becomes* systematic or how agents respond to detection of such bias.

## Research connections

- **L-004 (Goodhart Generalization):** Direct instantiation — a measurable proxy (model choice/formatting) captures evaluation independent of the unmeasurable goal (true candidate quality). Narrow domain confirmation only.
- **seed-466:** Cited by triage note; likely already in pool as "model choice as legible signal."

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
