# Censorship Resistance and Throughput with Multiple Concurrent Proposers

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.16995
**Date read:** 2026-09-02
**Connected to:** L-009, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of economic censorship incentives in blockchain proposer systems, modeling the cost-benefit tradeoff for adversaries bribing proposers to exclude transactions. The work introduces the metric of economic censorship resistance (eCR) and examines how proposer multiplicity affects the feasibility of censorship attacks.

## What I took from it

The paper is a well-scoped attack-cost model applied to a specific protocol layer (transaction inclusion), but it does not present a primary sustained argument about general protocol behavior, nor does it offer a mechanism absent from the current inventory. The core finding — that eCR degrades under single proposers and improves with concurrent proposers — is a domain-specific economic result rather than a law-shaped regularity about protocolized systems.

The work does sit at the boundary of L-014 (Strategic Boundary Concentration Under Computable Legality): transactions are highly legible inputs to proposers, and the censorship cost surface is indeed computable and optimizable. However, the paper treats this as a static game rather than exploring how the incentive structure itself evolves under repeated interaction, protocol evolution, or institutional drift. It confirms that legible boundaries attract optimization pressure, but does not advance our understanding of how that pressure propagates, self-reinforces, or destabilizes the protocol over time.

## Research connections

- **L-014:** Confirms that transaction-level inclusion decisions are legible optimization targets for rational actors; does not investigate downstream effects or institutional response.
- **L-009:** Relevant as a case where symmetric racing (multiple proposers competing) can reduce vulnerability to concentrated attack; worth tracking as a counterexample or boundary condition.
- **seed-075 (Multi-Layer Censorship as Coordination Cost Displacement):** Suggests censorship pressure might migrate to other layers if proposer-level resistance hardens; this paper only models one layer.

## Seed

**Seed title:** Censorship Legibility Collapse Under Single-Layer Optimization

**Seed type:** observation

**Seed text:** Economic censorship resistance in transaction protocols exhibits a sharp phase transition as proposer cardinality increases: single proposers present a single, legible optimization target with concentrated value, while distributed proposers diffuse the target surface and raise bribe coordination costs. However, this does not eliminate censorship incentives—it displaces them. When a protocol hardens one layer of transaction inclusion, optimizing pressure should migrate to higher layers (mempool filtering, network-level routing) or adjacent protocols (private pools, dark pools). The generalization: legibility-driven censorship cannot be permanently eliminated by local protocol hardening; it can only be displaced to the boundary where legibility is highest and coordination cost is lowest.
