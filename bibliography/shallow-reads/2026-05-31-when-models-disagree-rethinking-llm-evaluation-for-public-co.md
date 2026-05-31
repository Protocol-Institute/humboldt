# When Models Disagree: Rethinking LLM Evaluation for Public Comment Analysis

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2605.29025
**Date read:** 2026-05-31
**Connected to:** L-004, L-003
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper proposing an auditing pipeline for LLM-based policy document categorization, focused on detecting and managing disagreement between models rather than optimizing single-model accuracy. The work is applied and diagnostic in scope, addressing a real deployment failure mode rather than presenting a sustained theoretical argument about protocol dynamics.

## What I took from it

The paper illustrates a practical instantiation of L-004 (Goodhart Generalization) in policy automation: when agencies adopt a single-model stance classifier as the proxy for "public opinion structure," optimization pressure on that model's accuracy metric divorces the reported categorization from the actual interpretive complexity of the comment corpus. Multi-model disagreement becomes visible evidence of unmeasurable goal collapse.

The proposed Interpretive Audit Pipeline itself represents a partial formalization response (L-003 signal), converting informal expert judgment about "which disagreements matter" into an explicit protocol. However, the paper does not investigate whether this formalization itself undergoes ossification, metric capture, or produces downstream coordination costs. It treats the auditing protocol as a solution rather than as a new system subject to the same pressures it diagnoses in the LLM layer.

## Research connections

- **L-004:** Demonstrates metric capture in policy automation—accuracy on validated stance samples fails to detect systematic divergence in how models interpret ambiguous public input; optimization narrows what counts as a valid "comment."
- **L-003:** Documents emergence of formalization under stress (scaling pressure in comment volume and diversity); proposes explicit audit pipeline as stabilization response, but does not examine whether this new protocol inherits capture dynamics.
- **H-001 (coordination cost conservation):** Introduces a new protocol layer (interpretive auditing) ostensibly to reduce coordination failure between agency reviewers and model outputs; unclear whether total coordination cost shifts or centralizes.

## Candidate laws or signals

- **CL-Disagreement-as-Opacity:** In systems where multiple candidate implementations of an interpretive function produce materially different outputs, disagreement itself becomes a reliable signal of domain complexity that single-metric evaluation systematically masks. (Does not generalize beyond evaluation design yet; needs confirmation in other protocol contexts.)
