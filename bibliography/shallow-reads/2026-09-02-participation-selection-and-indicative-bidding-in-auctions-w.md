# Participation, selection and indicative bidding in auctions with costly entry

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.24457
**Date read:** 2026-09-02
**Connected to:** L-008, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Laboratory study of mechanism design in auctions where entry carries sunk costs and agents have incomplete information about their own valuations pre-entry. Tests whether a "indicative bidding" protocol (non-binding preliminary bids before costly commitment) increases participation and revenue compared to unrestricted or capped entry baselines.

## What I took from it

The paper is a localized empirical test of a specific mechanism intervention—indicative bidding as a signal-refinement tool—rather than a sustained theoretical argument about protocol behavior under scaling or conflict. The result (that indicative bidding increases participation under high entry costs by reducing information uncertainty) is domain-specific to auction design and does not generalize to the broader laws of protocol ossification, metric capture, or coordination cost conservation under investigation here.

The triage suggestion that this connects to L-008 (computable enforcement under optimization pressure) and L-010 (adoption nonmonotonicity) is overstated. Indicative bidding does introduce a legible signal mechanism that agents can optimize around, but the paper does not explore whether that legibility itself becomes a target for strategic manipulation, nor does it investigate threshold effects or adoption dynamics that would support L-010. The mechanism is tested in a controlled lab setting with fixed populations, not in scaling or heterogeneous adoption contexts.

## Research connections

- **L-008:** Indicative bidding creates a computable, legible signal (preliminary bid) that agents condition entry decisions on, but the paper does not examine whether agents subsequently optimize the signal itself independent of underlying valuation, which is the core mechanism of L-008.
- **L-010:** The paper does not study adoption curves, threshold effects, or coordination among multiple agents over time; it tests terminal participation rates against baselines in single-round experiments.
- **seed-128 (Legibility-Driven Agent Convergence Under Computable Audit):** Tangential. Indicative bidding increases legibility of intent pre-entry, but no evidence of convergence or drift in agent behavior over repeated rounds.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**DECISION: STORE AS SHALLOW.** This is competent empirical work in mechanism design, but it does not present a sustained theoretical argument about protocol behavior generalizable beyond auction entry design, does not challenge or extend existing laws, and does not introduce a mechanism absent from the research inventory. The legibility-signal-optimization cycle it touches on is already captured by L-008 and seeds in the pool. File and move on.
