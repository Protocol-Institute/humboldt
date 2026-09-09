# Agentic AI Enhances Physician Trust in Clinical Decision Making

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.30658
**Date read:** 2026-09-01
**Connected to:** L-007, L-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A small empirical study (n=3 physicians, 315 cases) comparing physician trust in agentic versus non-agentic AI systems in clinical decision support. The paper measures both cognitive trust (process-oriented) and behavioral reliance (outcome-oriented), finding that agentic AI—which exposes intermediate reasoning and tool invocations—increases physician trust relative to black-box baselines.

## What I took from it

This is a narrow confirmatory finding: transparency of reasoning correlates with increased trust in a specific, high-stakes domain. However, the paper does not investigate whether this increased trust is *calibrated* to actual decision quality, nor does it probe whether the transparency effect persists when decisions are wrong. The framing assumes transparency → trust → good outcomes, but the mechanism linking transparency to *correct reliance* remains unexamined.

The work sits at the boundary of L-007 (Trust Ratchet in Safety-Critical Protocols) but inverts the causal story: instead of trust accumulating from operational age and stability, trust here accumulates from *legible intermediate steps*. This raises a sharper question: does transparency act as a trust substitute when operational history is unavailable? The study cannot answer this because all systems are new to the physicians. This is a single-point sample of a protocol system in its adoption phase, not evidence about long-term trust calibration under stress or error.

## Research connections

- **L-007:** Suggests trust in safety-critical protocols may accumulate from legibility/transparency rather than (only) operational age—a potential boundary condition or refinement.
- **seed-019 (embedded-explanation-opacity):** The study assumes explanations are transparent, but does not examine whether the *quality* or *accuracy* of the intermediate steps affects reliance differentially.
- **L-004 (Goodhart Generalization):** Physicians may optimize for "*seeing* reasoning steps" rather than "correct clinical outcomes," especially if step visibility becomes the primary trust signal.

## Seed

**Seed title:** Transparency-Legibility as Trust Proxy Substitution in Asymmetric-Knowledge Protocols

**Seed type:** observation

**Seed text:** In high-stakes protocols where end-users cannot independently verify decision correctness (asymmetric knowledge), intermediate step visibility can substitute for outcome confidence, increasing trust independent of actual decision validity. This effect may be strongest in adoption phase (low operational history) and may invert or degrade as agents gain experience with system failures. The mechanism suggests legibility of *process* becomes a measurable proxy for unmeasurable *safety*, creating a new point of vulnerability under L-004 (Goodhart): physicians may come to trust systems that are *transparent* rather than *correct*, especially under time pressure or when errors are costly but delayed in manifestation.
