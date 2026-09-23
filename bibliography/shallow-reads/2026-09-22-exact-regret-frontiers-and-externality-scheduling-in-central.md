# Exact Regret Frontiers and Externality Scheduling in Centralized Serial-Dictatorship Bandits

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.19963
**Date read:** 2025-01-17
**Connected to:** L-010, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical game-theoretic paper on multi-agent bandit learning in serial-dictatorship matching protocols. The authors characterize exact regret frontiers when exploration by one agent (learning a player–arm pairing) imposes externalities (regret) on downstream agents in a fixed priority order, under Gaussian reward assumptions.

## What I took from it

The paper formalizes a narrow but precise setting: when a centralized matching protocol uses a fixed serial order, exploration costs are *asymmetrically distributed* across agents—early agents bear discovery cost, later agents bear the cost of suboptimal matched decisions based on incomplete information. The authors show this externality structure reduces to a set of pairwise "exploration quotas" solvable via linear programming at certain instance types.

This is relevant to L-006 (Coordination Cost Conservation) and L-010 (Coordination Adoption Nonmonotonicity) because it demonstrates that in a formally structured protocol with legible decision order, the total coordination cost does not disappear—it concentrates. Early movers face exploration cost; downstream agents face forced passive acceptance. The protocol's formalization *displaces* rather than eliminates the cost structure. However, the paper does not investigate whether agents would rationally exit the protocol, adopt signaling strategies to influence priority order, or whether adoption nonmonotonicity emerges at the boundary. It is a within-protocol optimization study, not a protocol-boundary phenomenon study.

## Research connections

- **L-006:** Confirms the mechanism (cost displacement across layers/agents in a protocol), but does not test whether total cost is truly conserved or whether agents escape the protocol boundary.
- **L-010:** No evidence here on adoption signals or equilibrium multiplicity; the paper assumes fixed priority and full participation.
- **seed-144:** The formalization of exploration quotas creates a legible externality surface that could become a coordination refuge for informal deviation or implicit side-agreements.

## Seed

**Seed title:** Externality Legibility as Protocol Boundary Vulnerability

**Seed type:** observation

**Seed text:** When a protocol formalizes the cost-distribution structure across agents (e.g., via serial order, exploration quotas, or regret allocation rules), it creates a legible target for coalition formation and boundary-crossing renegotiation. Agents can now compute the cost they bear relative to their position and rationally condition participation on compensation or priority reordering. The precision that enables protocol optimization at the interior simultaneously enables agents to see the asymmetry and defect. This may generalize beyond matching: any protocol that makes externality distribution explicit via formal structure risks triggering coordination to circumvent or renegotiate that structure.
