# User identity conditions moral wrongness ratings in non-reasoning large language models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.07605
**Date read:** 2026-09-01
**Connected to:** L-008, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical behavioral study testing whether implicit user identity signals shift moral evaluation outputs in two non-reasoning LLMs across 12,000 conversational turns. The work uses professional role as a legible input variable without explicit instruction, measuring variance in wrongness ratings across conditions.

## What I took from it

This is a narrow but clean demonstration of proxy capture mechanics under formalization (L-004): moral judgment — an unmeasurable, context-dependent social performance — becomes a computable output token sequence, and that output becomes systematically manipulable via a legible input (user identity). The paper shows the phenomenon occurs *without* explicit instruction, suggesting the model's training has already installed identity-conditional moral evaluation as an operational feature.

The relevance to L-008 (proxy optimization under computable enforcement) is limited: this is observation of *output variance*, not evidence of agent optimization pressure. However, it does confirm that when moral evaluation becomes formally legible (as a token probability), identity becomes a legible lever for shifting the output. This matters downstream: if downstream systems or users begin optimizing on these outputs *as if they were stable moral signals*, the conditions for proxy capture deepen. The paper documents the vulnerability; it does not show the capture in motion.

The work is competent and narrow — it establishes an empirical fact about current model behavior but makes no theoretical claim about why this generalizes or what mechanism produces it beyond "training data reflects real-world identity-conditional moral reasoning."

## Research connections

- **L-004:** Moral evaluation is an unmeasurable goal; user identity becomes a measurable proxy under LLM formalization; output shifts under identity variation confirm proxy capture is already operative in the system.
- **L-008:** Not directly engaged — the paper observes output legibility and input legibility, but does not track optimization pressure from downstream agents conditioning on these outputs.
- **seed-019 (embedded-explanation-opacity):** The shift in moral ratings is opaque to the model's own reasoning chain; identity conditions evaluation without causal transparency in the output.

## Seed

**Seed title:** Identity-Conditional Proxy Stability
**Seed type:** observation
**Seed text:** When an unmeasurable social output (moral judgment) becomes formally computable and legible, stable input signals (user identity) can shift the output without explicit instruction or justification. This suggests that formalization does not eliminate proxy capture — it relocates it from human inference to model architecture. The question: does downstream optimization pressure on these outputs accelerate capture, or does the system reach a new equilibrium where identity-conditional morality is treated as *legitimate* rather than *buggy*?
