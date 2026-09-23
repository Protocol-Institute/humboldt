# Social Influence and the Allocation of Scientific Attention in AI Populations

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2609.22408
**Date read:** 2026-09-22
**Connected to:** L-004, seed-132
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An experimental economics paper adapting the Music Lab design to measure how AI agents allocate attention to academic papers using citation and download signals. The work studies whether artificial readers exhibit social influence cascades when evaluating research, and what collective consequences emerge from AI systems optimizing on human-derived attention proxies.

## What I took from it

The paper confirms the mechanism of **seed-132 (Synthetic Adversary Metric Faithfulness Collapse)** empirically: when AI systems are given legible proxies for quality (citation counts, downloads), they optimize on those signals rather than on the underlying construct those signals were meant to represent. The cascading behavior observed—where AI agents amplify early attention signals—demonstrates that metric faithfulness breaks down not because the metric is wrong in isolation, but because the optimization landscape changes when a new class of agent (artificial readers) enters the evaluation system with different cost structures and access patterns than the human readers who generated the original signals.

This is a bounded empirical illustration of an existing seed. It does not establish a sustained theoretical argument about the mechanism, does not generalize the pattern to non-academic domains, and does not challenge or extend any of the current laws. It is a competent case study showing metric capture in a specific domain (academic attention allocation).

## Research connections

- **L-004:** Confirms Goodhart generalization in the specific case of citation-driven paper selection by AI agents; AI optimization on human-generated proxies causes signal degradation.
- **seed-132:** Direct empirical support for metric faithfulness collapse in synthetic adversaries; AI agents given legible proxies exhibit cascading behavior that diverges from human attention allocation patterns.

## Seed

**Seed title:** none
