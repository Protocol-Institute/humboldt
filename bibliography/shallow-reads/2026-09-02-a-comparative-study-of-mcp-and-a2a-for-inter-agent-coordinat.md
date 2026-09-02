# A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.23884
**Date read:** 2026-09-02
**Connected to:** L-003, L-006
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark/engineering comparison paper evaluating two concrete inter-agent coordination protocols (MCP and A2A) through implementation in LLM-based multi-agent systems. The work is grounded in practical systems engineering rather than theory-building or mechanism discovery.

## What I took from it

This is a tool-paper masquerading partially as a systems study. The triage assignment to L-003 and L-006 is premature — the abstract provides no evidence that the authors are tracing formalization ratchet dynamics or coordination cost conservation across protocol transitions. Instead, this appears to be a straightforward engineering comparison: which protocol works better for a specific coordination task?

The relevant observation is *meta*: this type of paper will proliferate as agentic systems become standard infrastructure. Such comparisons are useful for practitioners but generate weak inductive signal for law-building unless they include explicit attention to failure modes under scaling, adoption pressure, or formal constraint tightening. The absence of that framing in the abstract suggests this is a "which tool performs better" study, not a study of how protocols ossify or how costs are displaced.

## Research connections

- **L-003:** No evidence the paper traces how informal coordination norms are replaced by formalization under stress in these systems.
- **L-006:** No indication the paper measures whether coordination costs are conserved or displaced across MCP vs. A2A adoption scenarios.
- **seed-062 (Formalization Opacity Collapse):** Potential weak signal if the paper documents how automation legibility differs between protocols, but abstract does not suggest this analysis.

## Method note

Benchmark and tool-comparison papers should be systematized separately from mechanism-discovery work. When a paper enters the funnel because it concerns protocol design, triage should require explicit evidence that the authors are tracking one of: (a) how the protocol behaves under adoption pressure, (b) where coordination costs migrate under switching, or (c) what informal norms the formalization displaced. A comparative performance table alone is not sufficient signal. This paper should be shelved as a reference for engineering practice, not as a candidate for law induction unless a full read reveals emergent dysfunction patterns.
