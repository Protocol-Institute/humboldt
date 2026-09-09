# Is Per-Agent Policy Composition Safe? Rethinking Successor-Feature Transfer in Cooperative Multi-Agent Reinforcement Learning

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.11658
**Date read:** 2026-09-02
**Connected to:** L-005, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper on safe policy composition in multi-agent reinforcement learning systems with dynamic objectives. The work extends successor-feature methods from single-agent to multi-agent settings, studying whether per-agent policy libraries can be safely recombined under new reward functions without full retraining.

## What I took from it

The paper identifies a genuine failure mode: single-agent policy composition guarantees (monotonic improvement over library policies) do not transfer to cooperative multi-agent systems. When agents compose policies independently using shared feature representations, coordination can degrade — the composed multi-agent policy may perform worse than any policy in the original library on the new objective.

This is mechanically interesting for L-012 (intervention-layer displacement): the optimization pressure shifts from "find a policy" to "find a safe composition," but the safety criterion itself becomes legible and optimizable in ways that break prior guarantees. The paper shows the problem is fundamentally about *information asymmetry in the composition layer* — agents cannot observe each other's policy choices during recombination, leading to miscoordination.

However, the work remains domain-specific (RL policy libraries) and does not develop a generalizable account of when or why composition safety breaks in other protocol contexts. It offers a concrete failure case, not a mechanism or regularity.

## Research connections

- **L-005:** The system "works correctly" (library policies are safe) but restructuring (composing them under new objectives) can fail — a bounded confirmation of Gall resistance in the composition layer.
- **L-012:** The legibility of the composition problem creates new optimization pressure: agents try to solve composition safety, but the legibility itself becomes a target for deviation.
- **seed-071:** Suggests that expressiveness constraints in coordination (agents cannot communicate during policy selection) create irreducible residual governance problems that no mechanistic composition rule can solve.

## Seed

**Seed title:** Composition Legibility Decay in Multi-Agent Feature Spaces

**Seed type:** observation

**Seed text:** In systems where agents compose behaviors from a shared library using individual optimization (each agent independently selecting which library policies to blend), coordination safety cannot be guaranteed by composition rules alone — the composition decision itself becomes decoupled from the joint behavioral consequence. This suggests a broader pattern: legibility of *individual* decisions in multi-agent contexts does not preserve legibility of *collective* outcomes. The gap widens under dynamic objectives, where recomposition frequency increases and agents have no mechanism to validate that others' independent compositions preserve the prior coordination equilibrium.
