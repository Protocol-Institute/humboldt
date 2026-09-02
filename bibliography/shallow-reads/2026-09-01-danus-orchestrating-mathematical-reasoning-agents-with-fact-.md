# Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.06447
**Date read:** 2026-09-01
**Connected to:** L-011, seed-046
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper describing Danus, an orchestration framework for coordinating multiple LLM-based mathematical reasoning agents using a shared fact-graph memory structure. The work addresses scaling challenges in parallel proof search by centralizing intermediate claim storage and validation.

## What I took from it

This is a competent engineering contribution to multi-agent LLM coordination, but it operates entirely within the solution space of a pre-existing problem class — how to keep distributed reasoning consistent without recomputation. It does not interrogate the protocols themselves or their failure modes under scale.

The fact-graph memory mechanism is a *coordination layer addition*, not a protocol restructuring. It does not challenge L-011 (Causal Detachment as Stable Protocol Equilibrium) because the system remains functionally decoupled from the question of *why* autoregressive outputs diverge from causal grounding in the first place. The shared memory is a patch that makes divergence *legible and recoverable*, but does not address whether the underlying reasoning is causally sound or merely coherent-looking.

There is no engagement with the possibility that orchestration success (measured by proof completion) could mask internal deformalization — agents converging on shared fact-graph entries that are operationally useful but semantically drifted from the original mathematical domain. This is precisely the condition seed-046 (memory-gate-entropy-subject) is designed to track.

## Research connections

- **L-011:** The fact-graph does not resolve causal detachment; it redistributes it across the memory layer. Reasoning remains autoregressive; coordination becomes the artifact.
- **seed-046:** Shared memory structures under optimization pressure (proof completion) may exhibit selective retention of high-utility facts while low-salience grounding erosion goes unmonitored.
- **L-006:** Coordination cost is conserved — Danus moves it from proof-search serialization to fact-graph consistency maintenance and query resolution.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
