# Reinforcement Learning and Consumption-Savings Behavior

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2510.20748
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An economics paper applying Q-learning with neural network function approximation to household consumption-savings decisions under income uncertainty. The work departs from rational expectations by modeling agents as bounded-rational learners, and uses this framework to explain two empirical regularities in consumption behavior during downturns (elevated MPC for low-liquidity unemployed households, and consumption smoothing failures).

## What I took from it

The paper demonstrates proxy optimization under computable enforcement but does not constitute a primary theoretical or empirical argument about *protocol systems* — it is a behavioral model application. The relevance to L-008 (proxy optimization under computable enforcement) is present but thin: the "protocol" here is the household's learned policy for consumption conditional on observed wealth and income states. The Q-learning agent optimizes against a computable reward signal (consumption utility), but the paper does not investigate how formalization of this signal or its legibility to external enforcement changes behavior. 

The work is technically competent and empirically grounded, but it operates entirely within the domain of neoclassical economics with a single-agent learning lens. It does not engage with protocol *systems*, coordination failure modes, or the specific mechanisms by which making an optimization target legible or computable changes the structure of the problem itself. The MPC patterns it explains are artifacts of bounded rationality and state representation, not legibility-driven distortion.

## Research connections

- **L-004:** Weak connection. The paper shows agents optimizing against a computable proxy (consumption utility), but does not investigate metric capture or the divergence between proxy and ground truth under optimization pressure.
- **L-008:** Weak connection. The setup involves computable enforcement (the agent's own reward signal), but the paper does not study how that computability transforms the protocol structure itself or creates misalignment.
- **seed-077 (Metric-Induced Preference Ratcheting):** Tangential. The learned policy does show path-dependence on the reward signal, but this is standard RL behavior, not a protocol-level phenomenon.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
