# Optimal Fees for Liquidity Provision in Automated Market Makers

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2508.08152
**Date read:** 2026-11-23
**Connected to:** L-004, seed-463
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of optimal fee structures in AMMs using simulation across market conditions. The work treats fee-setting as a static or quasi-dynamic optimization problem, measuring LP profitability against adverse selection losses (LVR) under varying volatility and trader routing behavior.

## What I took from it

The paper confirms the core mechanism of L-004 (Goodhart Generalization: Metric Capture) in a specific domain: static fees are proxies for LP compensation, but under optimization pressure (arbitrageur competition, CEX price discovery), the proxy decouples from the actual loss function. Where the work becomes relevant to protocol law is not in its solution (dynamic pricing) but in what it reveals about the *structure of the problem*: once fee-setting becomes legible and computable, the optimization target (LP profitability) becomes a surface that arbitrageurs and sophisticated traders can directly probe and exploit. This is not unique to AMMs — it's a restatement of L-004 in the domain of market microstructure.

The paper does not engage with whether dynamic fee mechanisms themselves become new surfaces for exploitation, nor does it examine the coordination cost of implementing and governing dynamic pricing. It treats fee design as an isolated optimization problem rather than as a protocol layer embedded in a larger system (seed-553: formalization without cost reduction).

## Research connections

- **L-004:** Confirms metric capture in fee proxies; static fees fail under optimization because they are legible targets for adversarial trading.
- **seed-463:** Dynamic pricing binds prediction to incentive structure — the paper explores this empirically but does not theorize the meta-problem of oscillating fee equilibria.
- **seed-553:** Formalizing fee structure as a computable function may reduce measurement ambiguity but does not reduce the coordination cost of governance or the surface area for gaming.

## Seed

**Seed title:** Fee Legibility as Arbitrage Surface Under Market Stratification
**Seed type:** observation
**Seed text:** When compensation mechanisms in multi-venue trading systems are rendered computable and observable (e.g., AMM fee schedules), the gap between intended compensation (offsetting LVR) and actual LP return becomes a legible optimization target for strategic agents (arbitrageurs, informed traders). The more precise the fee rule, the sharper the arbitrage. This suggests a deeper pattern: formalization of transfer mechanisms in asymmetric-information systems does not reduce gaming — it concentrates it at the boundary between the protocol's loss model and its actual loss distribution. The pattern should generalize to any multi-agent system where compensation is meant to offset an unmeasurable harm but is implemented as a computable fee or allocation rule.
