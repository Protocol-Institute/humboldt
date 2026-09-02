# The Bidding Games: Reinforcement Learning for MEV Extraction on Polygon Blockchain

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2510.14642
**Date read:** 2026-09-02
**Connected to:** L-008, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic and empirical study of MEV extraction strategies under sealed-bid auction mechanisms (Polygon Atlas). The paper models searcher bidding behavior using reinforcement learning and analyzes equilibrium strategies in a highly constrained, time-pressured auction environment.

## What I took from it

The work demonstrates a concrete instance of **computable obligation capture** (L-014): as MEV auction rules become formally specified and machine-readable, optimizing agents concentrate strategic effort at formally legible boundaries—here, the bid function and timing windows. The RL approach itself is the mechanism by which agents discover and exploit the precise computational surface of the protocol.

This also provides empirical texture for **L-008** (Proxy Optimization Under Computable Enforcement): the gas price / auction bid becomes a legible, optimizable proxy for "right to transaction ordering," and the paper appears to show agents systematically learning to extract surplus by optimizing precisely against the computable signal. However, the paper reads as a technical contribution to game theory and RL rather than a *causal argument* about how formalizing obligations shapes incentive structures generically. It is domain-specific work with strong technical merit but limited generalization claim.

The sealed-bid mechanism itself is framed as reducing congestion relative to spam-based PGA—a coordination cost reduction—but the paper does not examine whether this cost is truly conserved (L-006) or displaced to a different layer (search costs, latency sensitivity, information asymmetry).

## Research connections

- **L-008:** Demonstrates proxy optimization in action—bid functions as legible enforcement surface for MEV extraction under time constraint and computable rules.
- **L-014:** Illustrates strategic boundary concentration: optimizing agents cluster behavior around formally legible auction parameters (bid timing, value thresholds).
- **seed-073 (Correlated Failure Under Proxy Consensus):** RL agents converging on similar bidding strategies may induce correlated failures under market stress or rule changes.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Information asymmetry in sealed-bid setting (private mempool visibility) may create conditions for bid-function proxy collapse.

## Seed

**Seed title:** Sealed-Bid Formalization as Latency-Compressed Optimization Surface

**Seed type:** observation

**Seed text:** When transaction ordering rights are formalized as sealed-bid auctions under extreme time constraints (millisecond windows), the computable bid function becomes the sole legible surface for strategic optimization, and RL-driven agents converge on extraction strategies that exploit temporal and informational asymmetries in the auction mechanism itself rather than in the underlying resource allocation problem. This suggests a broader pattern: formalizing obligations under time pressure may shift optimization from the goal space (fair ordering) to the mechanism space (bid timing), concentrating strategic pressure at computational bottlenecks. Testable in other time-constrained, sealed mechanisms (cloud resource auctions, real-time trading halts).
