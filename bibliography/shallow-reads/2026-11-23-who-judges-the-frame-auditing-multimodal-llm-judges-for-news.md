# Who Judges the Frame? Auditing Multimodal LLM Judges for News Framing Across Event-Level Perspectives

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.00071
**Date read:** 2026-11-23
**Connected to:** L-004, L-012, seed-461
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical audit of multimodal LLMs used as measurement instruments for detecting news framing bias. The work documents systematic drift between the content property being measured (framing) and what the LLM actually outputs—a case study in proxy degradation under deployment as a scalable evaluator.

## What I took from it

The paper exemplifies L-004 (Goodhart Generalization) and L-012 (Intervention-Layer Displacement) in a measurement context, but does not advance either law mechanically. The core observation is that when an LLM is positioned as a "judge" of frame selection, its outputs reflect not only the frame present in the source material but also systematic model biases in how it perceives multimodal content. This is a *restatement* of Goodhart rather than new evidence for a mechanism: the proxy (LLM judgment) diverges from the goal (actual framing present) under optimization/scaling pressure (using the LLM as a scalable evaluator across many articles).

The work is methodologically sound audit work but does not offer a novel mechanism explaining *why* this divergence occurs or under what conditions it generalizes beyond LLM-as-judge systems. It documents the phenomenon without theorizing the law. It remains within the domain of AI evaluation methods rather than offering a law-shaped claim about protocol systems more broadly.

## Research connections

- **L-004:** Confirms proxy capture in measurement contexts, but as restatement rather than new mechanism.
- **L-012:** Intervention-layer displacement occurs: the measurement signal (LLM judgment) becomes the optimization target, displacing the original causal target (actual framing).
- **seed-461:** Related but not directly engaged; would need access to seed-461 details to assess.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
