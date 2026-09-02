# PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.05318
**Date read:** 2026-09-01
**Connected to:** L-006, L-012, seed-020
**Kind:** benchmark/tool paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing PiSAs, a test suite for privacy violations in multi-agent LLM systems. The work identifies that contextual integrity failures occur not just at system outputs but internally across shared agent memory, inter-agent messaging, and coordination layers—gaps in existing single-user privacy frameworks.

## What I took from it

The paper makes a solid empirical observation: privacy architectures designed around user-system boundaries break when agents become organizational infrastructure with shared state. The locus of privacy risk shifts from *output leakage* to *coordination layer leakage*—information intended for agent A gets exposed to agent B through shared memory or message routing, not through external breach.

This maps cleanly to L-012 (Intervention-Layer Displacement): as decision protocols become formally specified and agent communication becomes machine-readable, the optimization pressure on privacy boundaries shifts from external (user-facing) to internal (agent-facing) layers. However, the paper treats this as a testing problem, not as a regularity about protocol systems. It does not investigate whether this displacement is *inevitable under scaling* or contingent on specific architecture choices. The work is empirically sound but architecturally local—it doesn't ask whether multi-agent systems *necessarily* concentrate privacy risk at coordination layers, or whether this is a design artifact.

## Research connections

- **L-006 (Coordination Cost Conservation):** Privacy enforcement cost may be conserved across layers—preventing output leakage may force investment in internal message auditing, but the total coordination cost of maintaining information boundaries doesn't decrease.
- **L-012 (Intervention-Layer Displacement):** The benchmark documents the phenomenon but not the mechanism: whether internal agent privacy violations are *inevitable consequences* of formalized shared infrastructure or artifacts of current design.
- **seed-020 (Symptom Hierarchy Coordination Displacement):** Privacy symptoms may surface at the coordination layer (inter-agent leakage) while root causes remain at the infrastructure layer (shared memory design).

## Seed

**Seed title:** Privacy Boundary Relocation Under Agent Coordination Formalization
**Seed type:** observation
**Seed text:** In multi-agent systems where agent coordination becomes machine-readable and enforced through shared state (memory, message queues, logging), privacy violations migrate from external outputs (user-facing) to internal coordination channels (agent-to-agent). The total privacy surface area may not shrink—it shifts. This suggests a deeper regularity: formalizing coordination boundaries in protocol systems does not eliminate privacy/security risk; it *displaces* the locus of risk to whatever layer becomes legible to optimization. Investigate whether this generalizes: does any protocol system that makes internal coordination machine-readable automatically concentrate risk at that layer?
