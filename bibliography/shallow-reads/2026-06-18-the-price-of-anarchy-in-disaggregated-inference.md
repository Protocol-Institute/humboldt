# The Price of Anarchy in Disaggregated Inference

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.17081
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** First formal game-theoretic treatment of a widely-deployed inference architecture class; introduces mechanism (hierarchical resource competition with positive externalities) absent from current inventory; generalizable beyond GPU serving to any disaggregated compute substrate.

## What this is

This is a primary theoretical paper applying game theory to disaggregated inference systems—architectures that physically separate the prefill (prompt processing) and decode (token generation) phases onto independent GPU pools. The authors model the resulting resource competition as three coupled games and analyze equilibrium inefficiency (price of anarchy) using NVIDIA Dynamo as a concrete instantiation.

## What I took from it

This work identifies a structural property of disaggregated artificial systems that has gone largely unanalyzed: when a fixed hardware budget is partitioned across functionally distinct but interdependent computational phases, the agents optimizing each phase (or requests routed to them) face conflicting incentive structures. The paper's framing as a *coupled game* with positive externalities is significant—it suggests that naive equilibria in such systems are *jointly suboptimal*, and that centralized allocation would outperform decentralized routing. This directly implicates questions about whether protocolized artificial systems inevitably suffer efficiency loss proportional to their degree of disaggregation, and whether this loss is recoverable through architectural constraints or only through coordination overhead.

The hierarchical KV cache game adds a second-order effect: shared state (the cache) becomes a competitive resource, introducing congestion dynamics that cut across the prefill/decode boundary. This is a mechanism that doesn't appear in homogeneous-pool serving systems.

## Research connections

- **Efficiency degradation in decentralized protocols:** This provides a quantitative framework for measuring how much throughput or latency is sacrificed when artificial systems are disaggregated for modularity or fault isolation.

## Candidate laws or signals

- **CL-2606.17081-1:** *Disaggregation overhead law*: Decentralized resource allocation in disaggregated inference architectures produces equilibria with measurable price of anarchy; the cost scales with the number of coupled games and the degree of cache contention.

- **CL-2606.17081-2:** *Positive externalities in compute routing*: Request routing that benefits one phase (e.g., prefill) can impose negative congestion externalities on the other (decode), creating a signature of misaligned optimization that is recoverable only through joint scheduling.
