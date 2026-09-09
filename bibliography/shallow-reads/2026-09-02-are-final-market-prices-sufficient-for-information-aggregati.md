# Are Final Market Prices Sufficient for Information Aggregation? Evidence from Last-Minute Dynamics in Parimutuel Betting

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2509.14645
**Date read:** 2026-09-02
**Connected to:** L-004, L-006
**Kind:** content
**Escalation:** store-only

## What this is

An empirical study of parimutuel betting markets (horse racing) showing that final odds alone are insufficient to infer beliefs or returns; realized returns depend on the *path* through which odds were reached, not just their terminal value. The mechanism: agents betting under non-contingency constraints (cannot condition bets on final odds) face binding coordination problems as information arrives, creating last-minute dynamics that final-price methods erase.

## What I took from it

This is a sharp empirical case of **L-004** (Goodhart Generalization) in action: the standard proxy used in market research — final odds as a sufficient statistic for aggregated belief — breaks down when the protocol enforces a non-contingency constraint. Agents cannot wager on the *actual* signal they care about (the final odds); they must commit earlier, creating a two-period game where interim odds become a coordination device, not just noise.

More interesting: this is also a **L-006** (Coordination Cost Conservation) instance. The protocol's non-contingency structure doesn't eliminate coordination cost; it *displaces* it into path-dependent betting sequences and interim signal-reading. The "missing information" in final prices is not lost — it's lodged in temporal structure and behavioral adaptation. This suggests coordination cost is not reducible; protocols that suppress one coordination mechanism force it to resurface elsewhere (here: as timing strategy and interim-odds sensitivity).

The finding does *not* generalize beyond betting markets cleanly — final prices work better in contingent markets — but it flags a general vulnerability: any protocol that forbids agents from conditioning on the actual terminal signal they care about will generate path-dependent artifacts in aggregate outcomes.

## Research connections

- **L-004**: Final odds as proxy for aggregated belief fails under non-contingency constraint; the proxy breaks precisely when optimization pressure (wanting to know final odds) meets a formalized incomputability (cannot condition on them).
- **L-006**: Coordination cost is displaced, not eliminated; the protocol moves it from bet-contingency to temporal-sequencing and interim-signal-reading.
- **seed-073 (Correlated Failure Under Proxy Consensus)**: The sufficiency of final prices as an aggregate proxy fails precisely when it is most relied upon; this is a consensus failure mode worth tracking.

## Seed

**Seed title:** Non-Contingency Constraint as Coordination-Cost Displacement Mechanism

**Seed type:** observation

**Seed text:** In protocols where agents cannot condition actions on the terminal outcome they care about (here: final odds), coordination cost does not vanish; it migrates into path-dependent behavior, interim signal-reading, and timing strategy. The proxy used to summarize the protocol outcome (final prices) becomes systematically insufficient not because information is lost, but because it is lodged in the sequencing and temporal structure of the protocol itself. This suggests a generalization: any protocol that forbids contingency on a legible outcome will embed coordination cost in the temporal or causal path, making end-state summaries unreliable aggregates. Worth tracking across governance, automation, and allocation protocols.
