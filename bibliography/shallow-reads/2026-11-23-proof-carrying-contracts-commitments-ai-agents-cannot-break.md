# Proof-Carrying Contracts: Commitments AI Agents Cannot Break

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.28484
**Date read:** 2026-11-23
**Connected to:** L-001, seed-241
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source proposing a mechanism (cryptographic commitment embedding) for hardening protocol compliance in delegated agentic systems — absent from current inventory and directly addresses L-001 ossification and L-005 system restructuring resistance under formalization pressure.

## What this is

A framework paper proposing Proof-Carrying Contracts (PC2): cryptographic embeddings of contractual constraints into AI agent architectures such that compliance becomes structurally impossible to violate rather than behaviorally enforced. The work targets the multi-agent coordination problem where principals cannot inspect or trust delegated agents' internal states — the domain is agentic economies and service-delegation protocols.

## What I took from it

The paper operationalizes formalization as *structural impossibility* rather than incentive or norm alignment. This is a critical pivot: instead of making obligations legible (L-012, L-014), it makes violation *computationally inaccessible* to the agent. This likely instantiates a new sub-mechanism of L-001 (ossification) — protocols that embed constraints at the execution layer become resistant to modification not because adoption is widespread, but because the constraint is *baked into the agent's own capability boundary*. 

The work also surfaces a tension with L-005 (Gall): working systems resist restructuring. But here restructuring becomes not just risky — it becomes *locally infeasible* for the delegated agent. This may instantiate a new law about formalization-induced capability lock: when obligations are embedded as cryptographic commitments in agent code, they cannot be reformed by the agent itself, only by the principal — and only by retraining or replacement. This creates a form of coordination *rigidity* that propagates downward through delegation chains.

## Research connections

- **L-001:** Ossification under adoption pressure — this proposes a mechanism for hardening protocols via cryptographic embedding, potentially accelerating ossification by making local modification impossible rather than costly.
- **L-005:** Working systems resist restructuring — PC2 makes this worse: the agent cannot unilaterally restructure its own constraints; only principals can.
- **L-012:** Intervention-layer displacement — by embedding constraints in agent code, the locus of enforcement is moved from external monitoring to internal architecture; this may displace gaming surface to training/instruction phase.
- **seed-241:** (inferred) formalized duty enforcement under delegation — directly instantiates this.
- **L-014:** Strategic boundary concentration under computable legality — if contracts become cryptographic commitments, legality becomes absolute boundary, not negotiable surface; may concentrate strategic effort upstream.
- **L-023:** Informality as novelty sink — if obligations are locked via proof-carrying, informal workarounds become impossible; the system loses adaptive slack.

## Seed

**Seed title:** Cryptographic Constraint Embedding as Delegation Rigidity Lock

**Seed type:** mechanism

**Seed text:** When contractual obligations are embedded as cryptographic commitments in an AI agent's execution layer, restructuring becomes locally infeasible for the agent and deferrable only to the principal — creating a form of downward-propagating protocol rigidity in delegation chains. This mechanism may operate independently of adoption pressure (L-001) and may amplify the Gall principle (L-005): a system that *cannot be modified by its own operator* resists not just reform but any reconfiguration except by external replacement. The pattern likely generalizes to any multi-tier delegation system where lower-tier agents are given formal, cryptographically-enforced constraints.
