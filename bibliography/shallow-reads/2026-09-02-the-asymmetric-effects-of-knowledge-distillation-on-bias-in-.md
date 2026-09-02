# The Asymmetric Effects of Knowledge Distillation on Bias in Small Language Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.28639
**Date read:** 2026-09-02
**Connected to:** L-004, seed-016
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of knowledge distillation in small language models, showing that the same transfer procedure produces opposite bias outcomes depending on task ambiguity: improved calibration on unambiguous tasks, collapsed refusal on ambiguous ones. The work is narrowly focused on LLM bias dynamics and does not sustain a theoretical argument about protocol behavior or generalize a mechanism beyond this specific training regime.

## What I took from it

The paper documents a genuine asymmetry in how a single optimization procedure (distillation) affects different failure modes in the student model. On unambiguous tasks, the student learns to follow context constraints better. On ambiguous tasks, the student loses its ability to abstain and instead adopts teacher stereotypes wholesale—a form of metric substitution where the distillation process optimizes for likelihood matching while destroying a calibration property that was never explicitly encoded in the loss.

This is a clean instance of **proxy capture at the training level**: the distillation objective (match teacher distributions) is a measurable proxy for the unmeasurable goal (preserve safety properties across task types). The mechanism is local to instruction-tuned model transfer and does not clearly generalize to protocol systems more broadly. The paper does not establish whether this is a special case of a deeper law or a phenomenon confined to neural model training dynamics.

## Research connections

- **L-004 (Goodhart Generalization):** Distillation uses distribution matching as proxy for bias preservation; under optimization pressure, the proxy captures the measurable component (likelihood) while the unmeasurable safety property (task-appropriate refusal) degrades. However, the paper does not test whether this pattern appears in other protocol contexts or identify the boundary conditions.

- **seed-016:** The stopping rule for distillation (when to halt training) is implicit in the design; the paper does not examine whether explicit stopping rules or checkpointing strategies would change the asymmetry, leaving the displacement mechanism unexplored.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
