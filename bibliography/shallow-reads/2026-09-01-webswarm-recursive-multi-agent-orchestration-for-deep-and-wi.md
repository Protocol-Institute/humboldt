# WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.08662
**Date read:** 2026-09-01
**Connected to:** L-010, seed-048
**Kind:** tool/methods paper
**Escalation:** store-only
**Escalation rationale:**

## What this is

A systems paper presenting WebSwarm, a multi-agent orchestration framework for LLM-based web search. The work addresses the architectural problem of balancing search depth and breadth by decomposing queries into recursive sub-tasks executed across parallel agents with adaptive routing and evidence aggregation.

## What I took from it

This is a competent engineering contribution to distributed LLM coordination, but does not present a sustained theoretical or empirical argument about protocol behavior under adoption pressure, coordination failure modes, or the mechanics of how distributed capability systems develop emergent equilibria. The paper focuses on *design choices* (recursive decomposition, adaptive routing, aggregation strategy) rather than on the *laws* governing when and why such designs succeed or fail across different capability regimes or adoption contexts.

The triage note flagged L-010 (Coordination Adoption Nonmonotonicity) and seed-048 (Capability-Cooperation Inversion), but the paper does not engage with the question of whether multi-agent coordination signals themselves become Goodhart-vulnerable under optimization pressure, nor does it test whether capability asymmetry between agents produces stable or unstable equilibria in recursive delegation. It is a case study of one architectural solution, not an investigation of the underlying regularities that determine which multi-agent protocols can remain functionally transparent as they scale.

## Research connections

- **L-010:** The paper demonstrates one design pattern for multi-agent adoption (recursive sub-tasking), but does not test whether coordination signals from parallel agents create nonmonotonic adoption curves or threshold effects when capability distributions become asymmetric.

- **seed-048:** Implied by the framing (capability-cooperation inversion as agents delegate to each other), but not examined empirically; the paper assumes cooperation is tractable through routing and aggregation rather than investigating whether capability differences destabilize cooperation itself.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
