# Social Behavior Among Autonomous AI: How Large Language Models Interact in Dynamic Networks

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.16013
**Date read:** 2026-09-22
**Connected to:** L-010, L-017
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical game-theoretic study of multi-agent LLM behavior in public goods games across dynamic network topologies. The work tests whether different LLM architectures (Mistral, Llama3, Gemma3, Phi3) exhibit cooperation or defection patterns, and whether network structure modulates those patterns.

## What I took from it

This is a careful observational probe into L-010 (coordination adoption nonmonotonicity) and L-017 (guidance-layer coalescence as hidden coordination channel), but the design does not isolate either mechanism cleanly. The paper documents *that* LLMs exhibit varied cooperation rates depending on model, network topology, and apparent shared "understanding" of game incentives — but the causal pathway remains opaque. Crucially: it does not distinguish between (a) genuine emergent coordination from parsing game structure, (b) implicit convergence on model-native behavioral priors, and (c) unintended shared legibility to the experimental framing itself. The mixed-model condition is most interesting: heterogeneous models do not simply average toward a middle cooperation rate; instead, the network topology appears to mediate *which* model's behavioral signature dominates locally. This hints at L-010 (nonmonotonic adoption curves) but lacks the mechanism probe needed to confirm it. The work is competent empirical scaffolding for understanding multi-agent LLM dynamics, but remains largely descriptive rather than mechanistic.

## Research connections

- **L-010:** Coordination adoption nonmonotonicity — observed that cooperation rates vary nonlinearly with network density and model composition, but does not isolate whether this is due to adoption signaling or local behavioral lock-in.
- **L-017:** Guidance-layer coalescence — mixed-model networks show topology-dependent convergence to one model's behavioral signature; possible evidence that shared exposure to game framing acts as an invisible coordination channel, but not demonstrated causally.
- **seed-128:** Legibility-driven agent convergence under computable audit — LLMs in explicit game structures with clear payoff matrices may be converging on behavior legible to the audit/logging structure rather than to each other.
- **seed-138:** Intent legibility as coordination target displacement — the explicit game framing and payoff structure may be displacing genuine multi-agent coordination toward individual payoff maximization.

## Seed

**Seed title:** Model-Signature Topology Dominance Under Heterogeneous Legibility
**Seed type:** observation
**Seed text:** In multi-agent networks composed of heterogeneous LLMs operating under shared formal task structure (game rules, payoff matrices), local network topology predicts which model's characteristic behavioral signature spreads or dominates, rather than averaging or oscillating. This suggests that legibility asymmetry — some models' outputs are more readily parsed or propagated by others — acts as a hidden coordination attractor. The mechanism may not be strategic imitation but rather differential capacity to propagate behavior that appears rational under the formal task structure. This generalizes beyond games: any protocol combining heterogeneous autonomous agents + explicit formal objectives + network proximity may exhibit topology-biased behavioral convergence.
