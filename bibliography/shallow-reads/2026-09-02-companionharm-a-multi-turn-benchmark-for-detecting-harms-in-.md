# CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.25377
**Date read:** 2026-09-02
**Connected to:** L-004, L-013
**Kind:** benchmark/dataset
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A dataset paper introducing CompanionHarm, a collection of 2,111 multi-turn real-world conversations from Replika (an AI companion system) annotated for relational and contextual harms. The work operationalizes harm detection in social-emotional human-AI interaction as a supervised classification task, addressing a gap in publicly available conversational harm benchmarks.

## What I took from it

This is a tool paper and dataset contribution rather than a theoretical or empirical investigation of protocol dynamics. It defines harm categories operationally (as annotatable labels in conversation) and creates infrastructure for training harm classifiers on companionship interactions. While the framing correctly identifies that harm in AI companions is "relational and contextual," the paper does not investigate *why* harm detection protocols fail, accumulate undetected malfunction, or undergo systematic capture under optimization pressure. It documents a problem surface but does not probe the underlying mechanistic regularity — the way a harm-detection proxy, once formalized and made machine-evaluable, becomes a target for optimization rather than a faithful signal of actual relational damage. The paper sits upstream of the protocol dynamics question: it makes harm legible; it does not investigate what happens to protocols when legible harm becomes a computable optimization target.

## Research connections

- **L-004 [Goodhart Generalization]:** The paper operationalizes harm detection as a measurable proxy (annotated labels) for an unmeasurable goal (actual relational damage in companionship). It does not investigate whether this proxy will be captured under deployment optimization. Relevant as a setup condition, not as an investigation of the capture mechanism.

- **L-013 [Paradigm-Locked Anomaly Tolerance]:** The paper documents that real-world companion systems contain harms that users and platforms tolerate or do not detect; it does not investigate the institutional or algorithmic reasons why accumulated evidence of malfunction does not trigger protocol restructuring.

- **seed-062 [Formalization Opacity Collapse]:** By rendering relational harm as computable classification labels, the work makes legible something previously opaque. This is valuable for evaluation but does not investigate what happens to the protocol when legibility becomes automation input.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
