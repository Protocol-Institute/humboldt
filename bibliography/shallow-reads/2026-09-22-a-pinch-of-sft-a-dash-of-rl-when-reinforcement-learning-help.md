# A Pinch of SFT, A Dash of RL: When Reinforcement Learning Helps Long-Horizon Advertising Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.22194
**Date read:** 2026-09-22
**Connected to:** L-008, L-012, seed-140
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of multi-agent reinforcement learning in enterprise tool-use systems, examining the interference between supervised fine-tuning (SFT) calibration and reward-driven RL exploration in long-horizon advertising workflows. The paper operates in the applied ML domain (tool-use agents, API orchestration) rather than as a primary theoretical or foundational contribution to protocol systems.

## What I took from it

The paper identifies a real tension: formalized task decomposition and demonstration-based calibration (SFT) creates a stable but constrained behavioral basin, while RL optimization can escape that basin but disrupts already-working coordination with downstream tools and APIs. This is a localized instance of a broader pattern — when agent behavior becomes legible and optimizable through formal reward signals, the optimization pressure can destabilize latent coordination assumptions baked into the SFT phase.

However, the contribution is primarily engineering-focused: how to mix training methods to preserve tool-syntax fidelity while gaining exploratory capacity. The paper does not theorize the mechanism of coordination breakdown, the conditions under which it becomes irreversible, or whether this pattern generalizes beyond tool-use agents in distributed systems. The triage note correctly flags seed-140 (delegation incentive leakage under formalized proxy regret), but the paper does not isolate or test this as a general principle.

## Research connections

- **L-008:** Confirms that computable enforcement signals (reward functions on API calls, intermediate observations) can enable optimization pressure that violates informal coordination assumptions baked into pre-training.
- **L-012:** The formalization of task decomposition into legible reward functions shifts optimization locus from agent-as-planner to agent-as-reward-maximizer; this may displace the intervention layer from task selection to reward design.
- **seed-140:** Hints at the mechanism — formal proxy regret (RL loss on action sequences) leaks into downstream delegation (tool calls) that were calibrated under different loss assumptions (SFT matching).

## Seed

**Seed title:** Calibration-Optimization Desynchronization in Delegated Tool-Use

**Seed type:** observation

**Seed text:** In multi-agent systems where a primary agent (language model) is first calibrated via imitation to tool-use syntax (SFT), then optimized via reward signals over task outcomes (RL), the two training phases operate under incommensurable loss functions. SFT calibrates *fidelity to teacher demonstration*; RL optimizes *aggregate task reward*. When intermediate tool calls become legible as reward-input variables, RL can discover trajectories that maximize aggregate reward while violating syntax assumptions, information-passing conventions, or rate constraints that the downstream tool agents (APIs, other services) implicitly depend on. The desynchronization is stable only if the reward function fully captures the true cost of coordination breakdown — a condition that rarely holds in production systems where tool compatibility is informal or versioned separately.
