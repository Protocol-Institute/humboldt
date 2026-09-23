# Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.17306
**Date read:** 2026-09-22
**Connected to:** L-010, seed-129
**Kind:** meta
**Escalation:** store-only

## What this is

A benchmark and methodology paper evaluating 8 model selection strategies for multi-agent systems that combine multiple LLM outputs. The work systematically compares routing-based, majority-voting, and LLM-judge architectures across scientific reasoning tasks, with focus on optimizing which models to pool together.

## What I took from it

This is a tool-design paper with methodological utility but limited theoretical contribution to protocol behavior. The triage connection to L-010 (Coordination Adoption Nonmonotonicity) and seed-129 (Legibility-Induced Conformity Locking) is plausible but underdeveloped in the abstract: the paper likely *demonstrates* that different selection criteria produce different convergence behaviors in multi-agent ensembles, but does not sustain an argument about why adoption of particular pooling strategies would be nonmonotonic or how legible selection rules induce conformity locking.

The empirical gap between best single-model and best pool selection strategy could be relevant to understanding how ensemble protocols create new coordination surfaces—but only if the paper traces *why* certain selections lock in conformity, rather than simply reporting which pools perform best. Without evidence that the mechanism generalizes beyond LLM ensemble design or that it challenges an existing law, this remains domain-specific optimization.

## Research connections

- **L-010:** Potential relevance if paper shows adoption of model pool strategies exhibits nonmonotonicity with respect to pool diversity or size—i.e., that adding "better" models sometimes decreases ensemble performance. Not clear from abstract whether this is studied.
- **seed-129:** Legibility-induced conformity could apply if legible selection criteria (e.g., "choose highest-accuracy models") create hidden pressure toward homogeneity despite diversity metrics. Unlikely to be the focus.
- **seed-128:** If routing-based selection produces agent convergence on shared model assignments, this touches legibility-driven convergence, but as an engineering trade-off rather than a protocol law.

## Method note

This work exemplifies the benchmark-paper pattern: comprehensive evaluation across axes but no deep mechanistic inquiry into *why* certain strategies succeed or fail, nor evidence that findings generalize beyond the ensemble domain. For protocol research, the question is not "which selection rule optimizes performance" but "what coordination dynamics does legibility of selection rules induce, and do those dynamics persist across protocol contexts?" The paper as described does not appear to ask that question. Useful reference for LLM ensemble practice; not a vector for law induction.
