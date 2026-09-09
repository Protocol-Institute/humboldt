# An Explainable Agentic System for Detection of Conversational Scams with Summary-Based Memory

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.11707
**Date read:** 2026-09-01
**Connected to:** L-008, seed-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** [blank]

## What this is

A tool paper introducing an agentic detection system that uses memory-conditioned reasoning (summary-based) to identify multi-turn conversational scams rather than single-message phishing. The work treats scam detection as a sequential inference problem where agents maintain legible state (summaries) and apply reasoning over conversation history. Introduces a benchmark (ConScamBen) for evaluation.

## What I took from it

The paper is a competent application of multi-agent reasoning to a real detection task, but operates entirely within the problem-solving domain it defines. It does not theorize about what happens when detection systems become more legible (more computable, more explicitly reasoned-over) to the adversaries they target, nor does it examine the feedback loop between improved detection transparency and adaptation of scam strategies.

The connection to L-008 (Proxy Optimization Under Computable Enforcement) is weak: the paper treats scam detection as a static classification task, not as a dynamic optimization landscape where legible enforcement signals drive adversary adaptation. The system's explainability (which is its stated contribution) renders the detection signal more interpretable to scammers, but the paper does not investigate whether this creates a new failure mode or adaptation pressure.

The triage note suggests seed-019 (embedded explanation opacity), but the system *reduces* opacity by design. This is orthogonal to the seed's concern.

## Research connections

- **L-008:** Weak. The system makes enforcement signals legible (summaries, reasoning chains) but does not study whether this legibility creates optimization pressure on scammers to evade the newly interpretable detection heuristics.
- **seed-019:** Inverted. The work aims at explanation clarity; the seed concerns the opacity that arises from explanation systems themselves.
- none: no connection to ossification, hardness asymmetry, formalization ratchet, or coordination dynamics.

## Seed

**Seed title:** none

---

**Recommendation:** This is a solid engineering contribution to a narrow problem. Store it as a benchmark reference for conversational-scam detection, but it does not advance the research agenda on protocol laws or the new nature. No deep read warranted.
