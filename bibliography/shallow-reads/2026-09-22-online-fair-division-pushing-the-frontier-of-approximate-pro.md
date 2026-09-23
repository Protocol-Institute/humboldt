# Online Fair Division: Pushing the Frontier of Approximate Proportionality

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.13650
**Date read:** 2026-09-22
**Connected to:** L-006
**Kind:** content
**Escalation:** store-only

## What this is

A theoretical computer science paper on online fair division algorithms under irreversible allocation constraints. The work studies what fairness guarantees (proportionality up to one good) remain achievable when indivisible resources arrive sequentially and allocation decisions cannot be revised, with an adversary choosing resource arrival order.

## What I took from it

This is a competent hardness result in a classical domain (fair division) but does not engage with the protocolized systems questions that drive the research agenda. The paper treats irreversibility as a computational constraint on optimization, not as a structural feature of protocol design under coordination pressure.

L-006 (Coordination Cost Conservation) predicts that when a protocol layer is tightened—here, by forcing immediate irrevocable allocation—the coordination burden shifts rather than disappears. This paper measures what fairness *cannot* be achieved, but does not investigate where agents or mechanisms *relocate* coordination labor (e.g., to pre-commitment strategies, side contracting, or signal design upstream). The focus is on algorithmic approximation bounds, not on the conservation of coordination cost across the system.

The adversarial model (adaptive resource ordering) is a weak proxy for real protocol-level strategic behavior and does not illuminate how actual agents would game or workaround the irreversibility constraint.

## Research connections

- **L-006:** Tests a prediction under a specific constraint (temporal irreversibility), but measures fairness degradation rather than coordination cost displacement.
- **L-009:** Tangentially relevant if competitive agents race to claim resources; not explored in the paper.

## Seed

**Seed title:** none
