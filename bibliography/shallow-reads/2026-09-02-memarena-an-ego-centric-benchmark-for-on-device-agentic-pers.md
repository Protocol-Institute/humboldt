# MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants at Scale

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.02613
**Date read:** 2026-09-02
**Connected to:** none
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing MemArena, a conversational dataset and evaluation framework for testing personal memory assistants running on-device. The work combines a multi-agent simulator (MASim) with ground-truth memory co-generation to measure how well edge-deployed models handle activity-dense, ego-centric, multi-session conversational contexts at scale (50 agents, 15 days, 10.3M tokens).

## What I took from it

This is primarily a tool contribution — a dataset and evaluation harness — rather than a sustained argument about how protocolized systems behave. However, it does illustrate an emerging evaluation challenge: as personal agents become stateful, multi-session, and distributed (on-device), the benchmark must capture **ego-centric observation asymmetry** — what each agent sees depends on its position in a multi-agent social graph. This mirrors challenges in L-015 (interpretive continuity decay) and seed-069 (transparency-legibility as trust proxy substitution), but only obliquely: MemArena measures recall and consistency, not the institutional decay or normative drift that happens when formal records survive but their context erodes.

The ego-centric framing also hints at a tension relevant to seed-081 (attribution legibility as optimization target): as personal assistants optimize for recall and coherence, they may inadvertently optimize for *legible* memories (those easily attributed to speakers/agents) over *accurate* ones, creating a form of Goodhart-like drift in the memory domain.

## Research connections

- **L-011:** On-device agentic systems using generative memory components may lock into operationally functional but causally detached states (e.g., a model learns to predict plausible rather than true memories).
- **L-004:** If memory benchmarks measure proxy signals (e.g., BLEU-style recall metrics) rather than actual utility to the agent or privacy preservation, optimization may capture the metric rather than the goal.
- **seed-069:** Ego-centric transparency (legible memory traces) may become a proxy for trustworthiness in personal agents, displacing actual verification.
- **seed-081:** Attribution legibility (who said what, to whom) becomes an optimization target; agents may over-optimize for clear speaker attribution at the cost of contextual nuance.

## Method note

This work exemplifies a methodological pattern worth tracking: as agent systems become stateful and multi-session, evaluation must simulate **temporal and relational coherence**, not just single-turn correctness. The use of a co-generated ground truth is pragmatic but risks ossifying a particular notion of "correct" memory (e.g., propositional accuracy) that may not generalize to real privacy or utility concerns. Future benchmarks may need to decompose memory into multiple evaluation substrates — legibility, privacy, utility, drift — rather than treating it as a monolithic signal. This suggests that benchmark design for protocolized agent systems should anticipate measurement capture (L-004) by deliberating *which failures we're willing to miss* in exchange for tractability.
