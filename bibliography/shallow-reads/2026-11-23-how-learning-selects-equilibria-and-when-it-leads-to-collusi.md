# How Learning Selects Equilibria and When It Leads to Collusion

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.36306
**Date read:** 2026-11-23
**Connected to:** L-009, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of how learning algorithm design (specifically, belief-testing and exploration rate functions) selects among multiple Nash equilibria in multi-agent Markov games. The paper shows that stochastically stable states correspond to equilibria maximizing the minimum transformed discounted value across players — a formal characterization of equilibrium selection under learning dynamics, with implications for when collusive or welfare-reducing outcomes emerge.

## What I took from it

The paper provides formal machinery for understanding *how* learning protocols induce equilibrium selection, but operates at a remove from the new nature's core concerns. It is a pure game-theoretic result: the equilibrium selected by a learning algorithm depends on the shape of the exploration/belief-testing function, and high-exploration regimes favor collusive outcomes (high minimum payoff). This is relevant to L-009 (Catastrophic Risk Cancellation) and L-010 (Coordination Adoption Nonmonotonicity) as a *mechanism*, but only in the narrow case where agents have symmetric payoff structures and learning is synchronized. 

The work does not examine what happens when the protocol itself becomes an object of optimization pressure, when agents condition adoption on *other agents' adoption decisions*, or when enforcement becomes legible and strategic. It treats equilibrium selection as a solved problem once you specify the learning rule; it does not engage with how protocol design interacts with agent incentives to deviate from, game, or reinterpret the protocol itself. This is competent technical work but stays inside the game-theoretic sandbox.

## Research connections

- **L-009:** Provides a formal sketch of how symmetric games with concentrated payoffs for first movers can produce collusive equilibria under certain learning dynamics — but does not examine the asymmetric, strategic deployment contexts where catastrophic risk cancellation is the concern.
- **L-010:** Shows equilibrium selection as a function of learning algorithm design, relevant to the nonmonotonicity question, but only for synchronized, belief-based learning; does not address endogenous coordination signals or herding effects.
- **seed-515 (Computable Belief as Collusion Surface):** The paper's formalism of belief-testing and belief-rejection as protocol steps resonates with the idea that legible belief states become surfaces for implicit coordination, but the paper does not examine this.
- none

## Seed

**Seed title:** Learning-Rate Regimes as Collusion Gatekeepers

**Seed type:** observation

**Seed text:** In multi-agent learning protocols where exploration rates are endogenous functions of agent payoffs, high-payoff equilibria (including collusive ones) become stochastically stable attractors. This suggests a threshold phenomenon: exploration rates set by agent preference (rather than exogenous schedule) tend to collapse toward equilibria that maximize minimum payoffs across the coalition, even when those equilibria are Pareto-dominated or socially harmful. The generalization: in any protocol where agents can modulate the legibility or testability of their own behavior, equilibrium selection will bias toward outcomes that concentrate payoff improvement among the learning coalition.
