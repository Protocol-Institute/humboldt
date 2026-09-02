# Stable and Budget-Feasible Coalition Formation for Clustered Federated Learning: A Hedonic Potential-Game Approach

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.26788
**Date read:** 2026-09-02
**Connected to:** L-006, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper on coalition stability in federated learning, using hedonic potential games to solve the coalition formation problem under budget constraints. The core contribution is an allocation rule that converts coalition surplus into participant preferences while guaranteeing nonnegative coordinator budget retention.

## What I took from it

The paper operationalizes a version of L-006 (Coordination Cost Conservation) within a specific protocol domain: distributed machine learning. It demonstrates that when you formally separate learning benefit, system cost, participant cost, and monetary transfers, stability becomes achievable only if the allocation mechanism preserves budget feasibility—i.e., the coordinator cannot run a deficit.

However, the paper does not investigate what happens *after* stability is achieved. It does not examine whether the formal separation of these cost layers creates new hidden coordination pressures (e.g., gaming of cost attribution, information asymmetry in benefit calculation), whether participants develop preferences for opacity in benefit measurement, or whether the stability conditions become brittle when the unmeasurable components (trust, effort quality, data quality) begin to diverge from their formalized proxies. The work is competent mechanism design but treats coalition preference as already-settled rather than as something shaped by the legibility of cost structure itself.

## Research connections

- **L-006:** Demonstrates cost conservation principle in federated learning context but does not examine cost displacement or re-emergence at different protocol layers.
- **seed-048:** Confirms preference alignment as cooperation constraint, but assumes preferences are exogenous rather than protocol-induced.
- **L-004 (Goodhart):** The formalization of benefit and cost introduces measurement proxies; no examination of optimization pressure on those proxies once deployed.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
