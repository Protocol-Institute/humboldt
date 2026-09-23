# Position: It is Time to Virtualize Foundation Models with a Self-evolving Operating System Layer

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.19203
**Date read:** 2026-09-22
**Connected to:** L-001, L-017
**Kind:** position paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper arguing for the creation of a Foundation Model Operating System (FMOS)—a virtualization layer that would standardize runtime, state, memory, budgeting, and guardrail management across compound agentic systems. The analogy is to pre-OS computing: today's agent stacks are fragmented, each reimplementing basic services; a shared OS layer would improve portability and governance. The paper suggests this layer should itself be "self-evolving."

## What I took from it

The paper is primarily an engineering/architecture argument, not a theoretical one. It observes real fragmentation costs and proposes a structural fix by analogy to historical computing. However, the framing inadvertently surfaces two problems for the new nature inventory:

**On L-001 (Protocol Ossification):** The proposal to standardize via a shared OS layer is *exactly* the kind of adoption-pressure vector that drives ossification. A FMOS that achieves wide adoption would become harder to modify precisely because all downstream agentic systems condition on its guarantees. The paper does not acknowledge this tension—it treats standardization as a straightforward good, not as a mechanism that locks in early design choices under adoption load.

**On L-017 (Guidance-Layer Coalescence):** The proposed self-evolving OS layer is a *de facto* shared decision and intervention substrate for all agents using it. If this layer makes recommendations about state management, memory allocation, safety thresholds, or resource budgeting, it becomes a hidden coordination channel—agents are no longer independently choosing behavior, but receiving guidance from a shared system component. The "self-evolving" aspect is particularly concerning: if the OS layer retrains or updates based on system-wide telemetry, it risks the normative retraining effects described in L-016.

The paper does not engage with either dynamic.

## Research connections

- **L-001:** A FMOS achieving widespread adoption would exemplify protocol ossification under adoption pressure—early design choices would become constraints on the entire ecosystem.
- **L-017:** A centralized OS layer providing guidance on state, memory, budgeting, or safety thresholds would constitute a hidden coordination channel, collapsing nominally independent agent decision-making into shared substrate recommendations.
- **seed-144:** A self-evolving OS layer might function as an informality refuge—pushing coordination costs into the OS layer itself, where they become hard to audit or dispute, rather than making them explicit in agent protocols.

## Seed

**Seed title:** Centralized Substrate as Coordination Lockbox Under Virtualization

**Seed type:** question

**Seed text:** When multiple autonomous or semi-autonomous agents share a common virtualization layer (OS, runtime, substrate), what prevents that layer from becoming a hidden coordination and control surface—even if nominally "neutral"? In particular, when the shared layer is adaptive (self-evolving, learning-updated, or metric-driven), does it inevitably become an optimization target for upstream agents, and does that optimization then encode system-wide coordination pressure that appears local to each agent? The risk is highest when the layer claims neutrality while actually implementing resource allocation, safety thresholds, or memory management policies that constrain agent behavior. This might generalize beyond FMOS to any multi-agent system with a shared, updatable substrate.
