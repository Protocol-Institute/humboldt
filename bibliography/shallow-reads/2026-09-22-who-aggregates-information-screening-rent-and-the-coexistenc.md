# Who Aggregates Information? Screening, Rent, and the Coexistence of CLOB and AMM Prediction Markets

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2609.20017
**Date read:** 2026-09-22
**Connected to:** L-006, seed-136
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical and theoretical paper on prediction market microstructure, specifically why CLOB (Central Limit Order Book) and AMM (Automated Market Maker) protocols coexist rather than one dominating. The authors argue that classical market-making theory fails for prediction markets because noise flow cannot support delta-neutral making; instead, makers profit from behavioral tail demand (one-sided imbalances), and this structural difference explains protocol divergence and information aggregation location.

## What I took from it

The paper documents a real coordination cost redistribution across market protocol layers (CLOB vs. AMM), but the mechanism is domain-specific: it hinges on the absence of exogenous liquidity demand and the resulting vulnerability of classical spread-capture strategies. This confirms L-006 (coordination cost is conserved, not eliminated) but does so through a narrow, well-understood financial microstructure argument rather than through a general protocol principle. The coexistence is explained by rational agent sorting — different information structures and risk tolerances map to different protocol interfaces — rather than by opacity, legacy lock-in, or the kinds of systematic misalignment that characterize new-nature protocols.

The observation that behavioral demand (concentrated imbalance) becomes the arbitrage frontier when randomized noise disappears is sharp but domain-bound. It does not challenge the legibility paradigm or reveal a hidden coordination surface; it simply shows that market design must fit information structure.

## Research connections

- **L-006:** Coordination cost conservation across protocol layers holds here, but as a textbook microstructure sorting result, not as a general constraint on protocol transformation.
- **seed-136:** Text-Protocol Expressibility Floor — prediction markets embed a sharp expressibility boundary (binary or scalar outcome), but the paper treats this as a design choice, not as a generative constraint on coordination norms.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
