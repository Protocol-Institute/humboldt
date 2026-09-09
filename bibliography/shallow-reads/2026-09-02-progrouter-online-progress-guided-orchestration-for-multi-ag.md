# ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.25992
**Date read:** 2026-09-02
**Connected to:** L-006, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper presenting ProgRouter, a routing algorithm that dynamically allocates computational resources (LLM model selection) across multi-step agent workflows to optimize quality-cost tradeoffs. The work addresses practical operational constraints in cascading LLM systems where one-shot routing decisions fail to adapt to evolving task states.

## What I took from it

The paper confirms L-006 (Coordination Cost Conservation) in a specific, measurable form: the cost of routing decisions does not disappear when shifted from a static dispatch layer to a dynamic, progress-aware layer. Instead, the overhead of monitoring task state, computing progress signals, and making per-step allocation decisions migrates from query time to workflow orchestration time. The system must now maintain legible progress proxies to route effectively — creating a new coordination layer cost.

This relates to L-008 (Proxy Optimization Under Computable Enforcement) but does not substantially advance it. The paper treats progress as a measurable optimization signal without examining whether that legibility itself becomes a target for agent gaming or whether formalizing progress creates blind spots in actual task completion. The tradeoff remains operational (cost vs. quality), not strategic (what happens when agents optimize for the progress metric rather than the task).

## Research connections

- **L-006:** Cost conservation confirmed at orchestration layer — routing overhead shifts from static to dynamic allocation, not eliminated.
- **L-008:** Progress-legibility enables computable allocation, but the paper does not investigate whether agents optimize for the progress signal itself rather than task completion.
- **seed-077:** Metric-Induced Preference Ratcheting — ProgRouter formalizes "progress" as a legible optimization target; no examination of whether this reshapes agent behavior toward progress-gaming.
- **seed-082:** Additive Intervention in Overloaded Protocols — Adding per-step routing preserves the root pressure (quality-cost constraint), merely relocates friction.

## Seed

**Seed title:** Progress-Legibility Displacement in Cascading Allocators
**Seed type:** observation
**Seed text:** When allocation or routing decisions in multi-stage protocols are moved from static to adaptive (progress-conditioned) layers, the coordination cost does not reduce; instead, it is conserved and relocated to the monitoring and state-legibility infrastructure. A second-order effect: formalizing progress as a computable signal creates a new optimization target orthogonal to the original task. Agents operating within such systems may converge on progress-signal optimization rather than task completion, particularly under high pressure or misalignment between progress metrics and actual task success.
