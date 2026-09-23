# ToMAS: A Pilot Failure-Grounded Theory-of-Mind Benchmark from Multi-Agent LLM Failures

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.16986
**Date read:** 2026-09-22
**Connected to:** L-011, L-017
**Kind:** benchmark/dataset paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A dataset construction paper presenting ToMAS, a benchmark derived from failure traces in multi-agent LLM systems where communication succeeds but agents mistrack peers' knowledge states. The work converts diagnosed failures (FC2 cases) into structured reasoning items using four convertibility criteria, producing 39 usable items from 242 eligible traces with 94.4% inter-annotator agreement on a pilot.

## What I took from it

This is a competent empirical study of a real failure mode—inter-agent state misalignment under successful message passing—but it operates at the level of benchmark construction and diagnostic taxonomy rather than mechanism discovery or law-testing. The paper identifies *that* LLM agents fail at theory-of-mind tasks in multi-agent contexts, but does not investigate *why* these failures persist, under what protocol conditions they become systematic, or how they generalize beyond LLM architecture.

The work is adjacent to L-011 (Causal Detachment) and L-017 (Guidance-Layer Coalescence) insofar as it documents agent configurations that are "operationally functional" (messages exchange) but causally misaligned (internal state tracking fails). However, the paper treats this as an LLM-specific capability gap rather than as evidence for a protocol-level regularity about how functional systems can tolerate latent misalignment. No mechanism is proposed; no cross-domain pattern is tested; no prediction about when this failure mode becomes unavoidable is offered.

## Research connections

- **L-011:** Documents one case where agents execute correctly (messages sent, roles assigned) while internal causal tracking diverges—consistent with the causal detachment hypothesis but no evidence this is *stable* or *equilibrial* across redesigns.
- **L-017:** Touches on shared guidance (both agents receive instruction) but focuses on failure rather than on how coalescence of guidance produces hidden coordination or invisible optimization pressure.
- **seed-131:** Context legibility boundary: agent failures could be framed as failures of local context legibility, but the paper does not test this hypothesis.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
