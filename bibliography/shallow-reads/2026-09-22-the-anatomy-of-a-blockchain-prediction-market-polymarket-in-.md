# The Anatomy of a Blockchain Prediction Market: Polymarket in the 2024 U.S. Presidential Election

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2603.03136
**Date read:** 2026-09-22
**Connected to:** L-001, L-009, L-010, seed-147
**Kind:** content
**Escalation:** store-only

## What this is

An empirical decomposition of Polymarket's Trump presidential election market using complete on-chain settlement data, separating genuine turnover from naive volume metrics by tracking outcome share minting/burning cycles within trades. The work develops transaction-level instrumentation to measure true price impact and market depth in blockchain prediction markets.

## What I took from it

This is competent infrastructure work—it solves a real measurement problem (naive volume overcounting in AMM-style prediction markets)—but does not present a sustained theoretical or empirical argument about protocol behavior under stress, adoption pressure, or coordination dynamics. The paper is methodological rather than mechanistic. It does not challenge or extend any of the current law inventory; it does not surface a new mechanism absent from the research inventory. The triage notes suggest connections to L-009 (catastrophic risk cancellation in symmetric racing) and L-010 (coordination adoption nonmonotonicity), but the paper does not engage with these dynamics. There is no analysis of how the protocol itself changed behavior, or how winner concentration in the market created cost asymmetries, or how batched settlement commitment behavior emerged under pressure. The paper treats Polymarket as a legible artifact whose true turnover can be measured; it does not examine how the protocol's formalization of outcome shares as computable, tradeable objects reshaped agent behavior or created new coordination surfaces.

## Research connections

- **L-001:** Polymarket's protocol remained unchanged during the 2024 cycle; this paper does not examine ossification pressure or adoption constraints.
- **L-009:** The paper does not examine whether concentrated winner stakes in the market created risk cancellation or cost-asymmetry dynamics.
- **L-010:** The paper does not track adoption cascades or nonmonotonic coordination signaling.
- **seed-147:** No data on batched settlement commitment or behavioral clustering under settlement cycles.

## Seed

**Seed title:** none
