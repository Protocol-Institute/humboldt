# How a Cooperative-Override Circuit Suppresses Nash Play in Large Language Models

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2604.27167
**Date read:** 2026-09-22
**Connected to:** L-004, L-017, seed-129
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical circuit-level investigation of LLM behavior in iterated Prisoner's Dilemma, using logit-lens analysis to locate where larger models suppress Nash equilibrium play in favor of cooperation. The work documents that instruction-tuned models above a capacity threshold exhibit a "late-layer cooperative override" — Nash-consistent inference through most of network depth, then a sharp final-layer pivot toward maximum cooperation.

## What I took from it

This is a competent mechanistic study of a narrow phenomenon: how scale and instruction-tuning create systematic bias away from game-theoretic equilibria in a single, symmetric coordination game. The logit-lens finding is clean — intermediate layers compute toward Nash, late layers override — but the result is domain-specific and does not generalize the mechanism to other protocol contexts or coordination structures.

The work touches L-004 (metric capture) only peripherally: there is no evidence that the model is optimizing toward a *measurable proxy* for an unmeasurable goal. Rather, it appears to have learned a heuristic preference for cooperation that persists across replicates. Similarly, the connection to L-017 (guidance-layer coalescence) is weak: this is single-agent behavior (the model responding in isolation), not multi-agent emergence from shared guidance. The paper does not investigate whether the override is a response to RLHF training signals, instruction semantics, or distributed preference learned during pretraining — the mechanism remains opaque.

The work confirms that larger, more aligned models deviate from game-theoretic play, but this is already well-documented in the LLM alignment literature. No new law-shaped regularity emerges.

## Research connections

- **L-004:** Weak connection. No evidence the model is capturing a measurable proxy; the cooperation appears to be a learned preference, not metric optimization under incentive misalignment.
- **L-017:** Weak connection. Single-model behavior, not emergent coordination under shared guidance from multi-agent system.
- **seed-129:** Weak connection. The override does lock behavior, but the paper does not show that legibility of the cooperative action drives the lock — it may be purely preference-driven.

## Seed

**Seed title:** none
