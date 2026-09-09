# Small edits, large models: How Wikipedia advocacy shapes LLM values

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.24890
**Date read:** 2026-09-01
**Connected to:** L-001, L-003, seed-036
**Kind:** empirical case study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement study demonstrating that a small organized group (Pro-Animal Wikipedians) can shape LLM outputs on a specific domain (animal welfare) through targeted edits to Wikipedia articles that appear in training data with elevated weight. Uses gradient-based attribution to trace causal influence from 125 edits across 115 pages to downstream model behavior.

## What I took from it

The paper provides concrete evidence that protocol substrate capture — specifically, control over high-weighted training signal — can be achieved through upstream formalization work (converting advocacy positions into sourced Wikipedia text). This confirms the vulnerability mechanism in L-001 and L-003: once a protocol (LLM training pipelines) depends on a narrowly-curated, heavily-weighted substrate (Wikipedia), small coordinated edits to that substrate function as leverage points.

However, the mechanism is *not* about protocol ossification or formalization ratchet in the way those laws predict. Rather, it's a straightforward case of **upstream source concentration**: Wikipedia is already formalized, already weighted, already integrated into pipelines. The advocates didn't ossify anything — they exploited existing ossification. The causal story is simpler and narrower than the laws suggest: edits → weighted training signal → model outputs. This is more akin to supply-chain insertion than protocol evolution or norm capture.

The work does not present a sustained theoretical argument about what happens to coordination systems under this kind of capture, nor does it generalize the mechanism beyond this specific case (advocacy → training data → model behavior).

## Research connections

- **L-001:** Confirms that adoption-dependent systems become leverage points, but via upstream substrate rather than protocol modification itself.
- **L-003:** Shows formalization as *existing condition* enabling capture, not as the causal driver of capture.
- **seed-036:** Tangentially related — advocates are performing a kind of "translation" (advocacy norms into sourced Wikipedia text) rather than conversion, but the seed is about protocol reform, not training data injection.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**JUSTIFICATION FOR STORE-ONLY:**

This is a competent empirical measurement paper demonstrating a real vulnerability (concentrated training data can be shaped by small groups), but it is **not** a primary theoretical or empirical source for a law about artificial protocol systems. It is a case study of data attribution and advocacy effectiveness. It does not:

1. Challenge or extend an existing law (L-001, L-003 remain unchanged; the mechanism is simpler than predicted).
2. Introduce a novel mechanism absent from inventory (upstream substrate concentration in training pipelines is already well-known; the novelty is the measurement, not the insight).
3. Generalize beyond the specific domain (animal welfare advocacy in LLMs).

It belongs in the evidence bin for L-001 and L-003, but does not warrant deep reading for law induction.
