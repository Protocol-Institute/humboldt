# Regret Minimization for Piecewise Linear Rewards: Contracts, Auctions, and Beyond

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2503.01701
**Date read:** 2026-09-02
**Connected to:** L-004, L-002
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic online learning paper developing regret-minimization algorithms for unknown piecewise-linear reward functions across microeconomic domains (contract design, auctions, bidding). The work is domain-specific algorithmic contribution: it extends existing online learning techniques to handle the discontinuities and non-convexities endemic to principal-agent and auction settings.

## What I took from it

The paper confirms that **metric capture (L-004) operates at the structural level of microeconomic mechanism design itself**: when principal-agent contracts, auction formats, or bidding strategies are formalized as piecewise-linear optimization problems, the agent optimizing under uncertainty will exploit the exact boundary conditions of the formalization. The "reward function" is the legible proxy; the contract or auction rule is the protocol; the learner is the optimizing agent. This is clean instantiation of L-004's mechanism, not a novel challenge to it.

However, the paper does *not* engage with **when or why** piecewise linearity becomes the operative formalization in the first place. It takes as given that contracts, auctions, and bids are naturally piecewise-linear objects. This obscures a prior question: **under what coordination or institutional pressures do microeconomic designers choose to render their agreements as piecewise-linear rather than continuous, smooth, or multi-dimensional?** The ossification pathway (L-001) and the formalization ratchet (L-003) might explain this upstream choice. The paper sits downstream of that process.

## Research connections

- **L-004 (Goodhart Generalization):** Piecewise-linear contract and auction design *instantiates* metric capture; the boundary discontinuities are the exploit surface for optimization.
- **L-002 (Hardness Asymmetry):** Verification cost (checking which piece of the contract applies, who won the auction) is lower than the cost of modifying the contract structure once agents have learned to optimize it.
- **L-001 (Protocol Ossification):** No engagement, but the prevalence of piecewise-linear formalization in mature microeconomic practice might reflect prior ossification of design choice.
- **L-003 (Formalization Ratchet):** The move from informal principal-agent relationships to formal piecewise-linear contracts under stress (hidden action, uncertainty) is an instance, not a test, of this law.

## Seed

**Seed title:** Piecewise Linearity as Coordination Codification Lock

**Seed type:** observation

**Seed text:** Microeconomic protocols (contracts, auctions, bid structures) tend to be formalized as piecewise-linear functions under conditions of scaling, opacity (hidden information), and enforcement legibility. Once a protocol is legible as piecewise-linear, optimization pressure concentrates on boundary exploitation rather than renegotiation of the pieces themselves. This suggests that **piecewise linearity is not a natural representation of economic relationships, but a coordination lock imposed by the joint requirements of formality, computability, and enforceability**. The law-shaped question: do all protocols that achieve sufficient scale and enforcement pressure converge toward piecewise-linear formalization, independent of the underlying phenomenon they govern?
