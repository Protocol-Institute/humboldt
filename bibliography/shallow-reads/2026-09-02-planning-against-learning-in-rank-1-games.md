# Planning Against Learning in Rank-1 Games

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.18067
**Date read:** 2026-09-02
**Connected to:** L-008, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper studying the computational tractability of strategic planning against learners using Replicator Dynamics in structured games (rank-1 bimatrix games). The work extends prior results showing that anti-learning optimization is tractable in zero-sum settings to a specific class of general-sum games, establishing hardness boundaries.

## What I took from it

The paper demonstrates that when one agent can observe and model another's learning algorithm (Multiplicative Weights Update / Replicator Dynamics), the first agent's optimization problem changes from playing a game to *planning against a learner*—a distinct computational regime. In rank-1 games, this problem remains tractable, but the work implicitly confirms that as game structure becomes richer, the planner's ability to reliably predict and exploit learner behavior degrades.

This is directly relevant to L-008 (Proxy Optimization Under Computable Enforcement) and L-012 (Intervention-Layer Displacement): the learner's adaptation rule becomes a legible target for optimization, but the planner's leverage is bounded by game structure. The paper does not address protocol-level or institutional systems, so the generalization to governance, auditing, or distributed protocols remains open. The mechanism is narrow—it's about computational hardness, not about how formalizing a learner's behavior changes the system's behavior landscape more broadly.

## Research connections

- **L-008:** Confirms that computable learner dynamics become optimization targets, but shows tractability is structure-dependent; does not explore what happens when multiple layers of learning interact.
- **L-012:** Exemplifies intervention-layer displacement: the planner's optimization pressure moves from the game itself to the learner's decision rule; does not explore how this creates new equilibria or instabilities in multi-layer systems.
- **seed-128 (Legibility-Driven Agent Convergence):** The learner's legible update rule attracts strategic intervention; the paper shows when this is computationally feasible but not how legibility itself changes convergence or stability.
- none: The paper does not engage with protocol ossification, trust, governance structures, or how formalizing learner behavior might displace coordination costs.

## Seed

**Seed title:** Learner-Targeting as Legibility-Gated Intervention
**Seed type:** observation
**Seed text:** When a learning algorithm is legible and its dynamics computable, strategic agents can optimize against it rather than against the environment; the tractability of this counter-optimization depends on the structure of the game, not on the legibility itself. In systems where learning rules are formalized and observable (e.g., protocol enforcement, algorithmic governance, audit-driven compliance), this creates a new optimization tier: agents optimize against auditors, learners, or rule-detectors rather than against the task. This may generalize beyond games to any protocol system where adaptation is formalized and observable—institutional learning rules, regulatory feedback loops, ML-driven decision-making—but the paper does not explore feedback effects or multi-layer dynamics.
