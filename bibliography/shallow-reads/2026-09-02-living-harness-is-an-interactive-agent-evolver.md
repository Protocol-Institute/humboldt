# Living-Harness Is an Interactive-Agent Evolver

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.26598
**Date read:** 2026-09-02
**Connected to:** L-002, L-005, seed-018
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper proposing Living-Harness, a self-evolving wrapper for LLM agent behavior that updates the persistent execution scaffold (tools, context, memory, workflow) based on post-episode feedback signals rather than keeping it static. The work addresses a gap: agents recover within episodes but fail to propagate learning to the harness that will guide future tasks.

## What I took from it

The paper identifies a real asymmetry in agent protocol architecture: the harness (the structure within which execution occurs) exhibits different revision dynamics than the model weights themselves. Static harnesses create a persistent execution boundary that absorbs failures without updating the scaffold — a form of structural ossification. Living-Harness proposes to flip this by making the harness a learnable component, converting episode trajectories into posterior evidence.

This is technically orthogonal to the core mechanism of L-002 (Hardness Asymmetry between verification and execution) but touches a secondary geometry: the cost of revising execution infrastructure vs. revising the agent's internal state. The paper does not theorize this asymmetry; it merely engineers around it. The deeper question — why harnesses naturally resist revision even when failures accumulate — is left unexplored. This is a tool paper with a valid empirical observation but no mechanistic claim about protocol evolution under adoption pressure or coordination constraints.

## Research connections

- **L-002:** The harness revision cost is distinct from the model revision cost; the paper observes but does not formalize the asymmetry between what is revoked and what persists.
- **L-005:** The harness functions correctly (agents do recover within episodes); the paper's intervention respects the principle that working systems should be evolved, not rebuilt, by making the scaffold gradual.
- **seed-018:** The living-harness architecture treats the execution boundary as a learnable parameter; this touches on how responsibility for failure is distributed between model and scaffold.

## Seed

**Seed title:** Execution Scaffold Revision Resistance
**Seed type:** observation
**Seed text:** In agentic systems, the persistent execution scaffold (harness, tools, context structure, workflow) accumulates failures across episodes at a lower revision rate than internal model weights, even when both receive identical feedback signals. The harness exhibits higher structural inertia because it serves as a coordination interface across multiple agents or serves safety-critical legibility functions. Revision of the scaffold carries higher coordination cost than revision of the model; the asymmetry may depend on whether the harness is observable to or contractually binding on other agents or systems.
