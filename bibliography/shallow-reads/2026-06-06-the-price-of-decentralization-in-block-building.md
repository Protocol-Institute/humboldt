# The Price of Decentralization in Block Building

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.01874
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source modeling a fundamental tension in protocol design (decentralization vs. latency-dependent coverage) that generalizes across distributed systems; introduces geographic-temporal coupling as a mechanism absent from current inventory.

## What this is

This is a game-theoretic analysis of decentralized block building mechanisms (used in Ethereum post-Merge and similar protocols). It models how builders choose geographic regions to maximize transaction coverage and rewards, showing that decentralization's censorship-resistance and fairness benefits are contingent on—and degraded by—builders' spatial positioning constraints and information-source latency asymmetries.

## What I took from it

The paper identifies a **structural cost of decentralization**: the naive assumption that increasing the number of builders improves censorship resistance breaks down under realistic latency conditions. Builders face a stochastic coverage game where geographic location is a strategic variable coupled to transaction access and reward concentration. This suggests decentralized systems exhibit an **irreducible centrality gradient** based on network topology and information propagation delays, even when authority is formally distributed.

This generalizes beyond blockchain: any protocolized system claiming to eliminate monopolistic chokepoints through decentralization must account for the latency-position-concentration triangle. The work reveals that decentralization can be *nominal*—formally multiplied—while *effective* centralization emerges through geographic or informational asymmetry. This is a mechanism-level account of how "decentralized" systems revert to concentration under realistic constraints.

## Research connections

- **Centrality emergence:** geometric and temporal constraints reconstruct centrality even in formally decentralized systems; decentralization may be a constraint-bounded variable, not a boolean.
- **Protocol-topology coupling:** protocol properties (fairness, censorship resistance) are not independent of physical network topology; they are co-determined.

## Candidate laws or signals

- **CL-Decentralization-001:** Decentralization of authority without decentralization of information-source geometry produces latency-ranked builder hierarchies; effective centralization concentrates at low-latency regions.
- **CL-Protocol-Design-001:** Systems designed to eliminate monopoly via formal multiplicity of agents reintroduce concentration through differential access costs (latency, geography, informational asymmetry).
