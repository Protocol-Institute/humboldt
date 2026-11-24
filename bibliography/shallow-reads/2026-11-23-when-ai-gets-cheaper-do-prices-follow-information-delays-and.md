# When AI Gets Cheaper, Do Prices Follow? Information Delays and Algorithmic Pricing

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.31693
**Date read:** 2026-11-23
**Connected to:** L-008, L-004
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A simulation study of algorithmic pricing in a duopoly market, testing whether cost reductions are passed to consumers when sellers use Q-learning policies and face information delays and frequency constraints on price adjustment. The work varies information staleness, repricing frequency, cost structure, and product differentiation across factorial conditions.

## What I took from it

This is a narrow empirical probe into one instantiation of L-008 (proxy optimization under computable enforcement) and L-004 (Goodhart generalization). The core finding — that information delays and repricing constraints dampen or block cost-to-price transmission — is consistent with both laws but does not advance the mechanism or reveal the boundary conditions that would elevate the work to theoretical contribution.

The paper demonstrates that when sellers optimize price via RL against *stale* competitive information, they remain insensitive to cost reductions in the competitor's production function until that cost reduction becomes legible in observed prices. This is a competent domain-specific instantiation of proxy misalignment (observing price, not cost; optimizing on signal lag), but the mechanism is already well-understood through L-008 and L-004. The factorial structure is clean, but the generalization remains within algorithmic pricing — it does not establish whether this delay-induced opacity is a property of *all* protocol systems where optimization pressure decouples from true state, or whether it has features specific to price signals, market structure, or RL architectures.

## Research connections

- **L-008:** The paper illustrates proxy optimization under computable enforcement (price-based rather than cost-based optimization), but does not resolve mechanism or identify when this effect saturates or inverts.
- **L-004:** Metric capture is implicit — sellers optimize on observable competitor price, not on underlying cost driver — but the paper does not test whether this capture generalizes beyond pricing contexts or persists under different information structures.
- **seed-233:** The work touches legibility-cost trade in adaptive capacity, but only operationally; no insight into the deeper trade-off between fidelity and reaction speed in multi-agent learning.
- none

## Seed

**Seed title:** Information-Lag Induced Price Stickiness as Orthogonal to Cost Dynamics

**Seed type:** observation

**Seed text:** When optimizing agents condition action on a delayed proxy of system state (rival price observed with lag N), cost reductions in the true state function do not propagate into action policy until the proxy signal updates to reflect them. The delay introduces a decoupling between the efficiency frontier (new cost structure) and the agent's decision surface (lagged price observation), which persists even when agents have correct forward models of competitor behavior. This suggests that information lag acts as a hidden coordination cost that cannot be reduced by improving agent rationality or model fidelity — only by reducing delay or switching the optimization anchor from proxy to state. Worth tracking whether this holds in non-pricing domains (resource allocation, protocol voting, safety-critical systems) or whether it is specific to continuous-valued, high-frequency optimization targets.
