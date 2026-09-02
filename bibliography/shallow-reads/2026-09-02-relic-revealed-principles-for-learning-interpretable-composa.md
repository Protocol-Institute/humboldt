# RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.16745
**Date read:** 2026-09-02
**Connected to:** L-001, L-005, seed-029
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A multi-agent reinforcement learning framework addressing skill composition when agents maintain private implementations and expose only opaque interfaces. The work introduces RELIC to enable agents to learn interpretable, composable decision-making skills under privacy constraints — a regime where centralized policy optimization is unavailable and agents must infer coordination norms from revealed behavior alone.

## What I took from it

The paper situates itself in a genuine practical constraint space — agents cannot share executable policies, internal state representations, or algorithmic details — and proposes to recover composability through interpretable skill exposure rather than full transparency. This is orthogonal to protocol ossification and Gall-style system resistance in an important way: RELIC does not address what happens *after* adoption locks in an interface; it addresses how to coordinate *despite* heterogeneous, opaque interfaces from the start.

The work thus confirms the difficulty of coordination under formalism gaps (resonant with L-005 and seed-029), but does not engage with the temporal or irreversibility dynamics that make ossification a law rather than a solvable design problem. It is a competent engineering response to a real constraint, not a claim about what happens to protocol systems under stress or adoption pressure. The interpretability angle is pragmatic (agents learn to read each other's revealed actions) rather than foundational (what makes *some* interfaces inherently resist modification while others do not).

## Research connections

- **L-001:** Indirect: RELIC assumes opaque, heterogeneous interfaces as a *boundary condition*, not as an emergent result of adoption pressure. The paper does not test whether interface opacity increases under scale or adoption.
- **L-005:** Relevant but not challenging: RELIC is additive composition of existing opaque agents, which aligns with the claim that complex systems resist restructuring. It does not test whether attempts to re-integrate or homogenize such systems fail predictably.
- **seed-029:** Mirrors the stated triage connection — skill learning across heterogeneous boundaries does produce coordination friction analogous to protocol interface locks. But the paper treats this as a constraint to engineer around, not as a law to characterize.
- **L-012:** Weak signal — skill exposure (the "revealed principles") becomes a legible input to other agents' planning; whether this displaces optimization pressure upstream (into skill selection itself) is not examined.

## Seed

**Seed title:** Interpretability as Coordination Proxy Under Interface Opacity

**Seed type:** motif

**Seed text:** When agents must coordinate across opaque interfaces without policy sharing, they shift optimization pressure from *implementation transparency* toward *behavior predictability* — rendering internal decision structure legible through revealed action patterns rather than code exposure. This suggests that under sufficient interface heterogeneity and opacity constraints, interpretability functions as a *substitute* for formalization, not a precursor to it. The generalization: systems under coordination pressure but blocked from deep integration will accumulate *interpretive scaffolding* (diagnostics, signal protocols, action-outcome mapping) as a conservation effect — the coordination cost is not eliminated, but displaced into the inference and prediction layer.
