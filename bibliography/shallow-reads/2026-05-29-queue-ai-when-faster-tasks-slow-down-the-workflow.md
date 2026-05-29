# Queue & AI: When Faster Tasks Slow Down the Workflow

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2605.27202
**Date read:** 2026-05-29
**Connected to:** L-004
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of AI productivity measurement in real workflows, arguing that per-task speed metrics (tasks/hour, mean handle time) fail to capture system-level effects when tasks queue and compete for human attention. Primary domain: customer service, writing, software development operations.

## What I took from it

This is a clean instantiation of L-004 (Goodhart Generalization) applied to the deployment layer rather than the protocol layer itself. The paper documents how optimizing a measurable proxy (task completion speed) under adoption pressure causes protocol drift at the workflow level—faster AI-assisted tasks create queue congestion that slows downstream human review, coordination, and decision gates, negating the per-task gain. 

The work confirms that Goodhart capture is *not* specific to algorithmic metrics or formal protocols, but a general feature of any system where optimization pressure meets partial observability. It also hints at a secondary dynamic worth tracking: the introduction of a faster execution layer (AI) into a human-constrained queueing system creates *protocol stress* that forces either formalization of review/routing (L-003) or systematic underutilization of the faster layer. This suggests coordination costs may not be conserved across layer transitions (H-001)—they may *increase* when speed asymmetry is introduced.

## Research connections

- **L-004:** Direct confirmation; AI speed metrics are perfect Goodhart proxies in workflow contexts—they measure what's easy to measure (per-task time) not what matters (throughput under constraint).
- **L-003:** Implicit signal; organizations may respond to AI-induced queue chaos by formalizing task routing, prioritization, and handoff protocols rather than redesigning workflows.
- **H-001:** Suggestive tension; introduction of faster execution layer appears to *increase* coordination cost at the human bottleneck, not conserve it.
- **H-002:** No direct connection; trust dynamics not in scope.

## Candidate laws or signals

- **CL-2605.27202-1:** Speed Asymmetry Induces Queueing Stress — When a faster execution layer is introduced into a human-constrained system, the per-unit speedup is offset by congestion and coordination overhead at the bottleneck, unless the bottleneck capacity is explicitly expanded or the workflow is restructured to match the new speed regime.
