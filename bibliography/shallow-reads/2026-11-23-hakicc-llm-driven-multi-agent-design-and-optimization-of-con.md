# HakiCC: LLM-Driven Multi-Agent Design and Optimization of Concurrency Control Protocols

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.00889
**Date read:** 2026-11-23
**Connected to:** L-001, L-005, seed-023
**Kind:** tool/application paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An application paper describing an LLM-driven system for automated design and selection of concurrency control protocols in distributed systems. The work treats protocol design as a search/optimization problem, using multi-agent LLM interaction to explore the design space and select protocols matched to application constraints—addressing the practical problem that most applications default to 2PL or OCC due to lack of expert knowledge.

## What I took from it

This is a competent engineering contribution that sits *outside* the theoretical aperture we're tracking. The paper frames protocol selection as a legibility and automation problem: humans lack the expert knowledge to match protocols to workloads, so LLMs are deployed to do that matching. This is instrumentally interesting but does not engage with *why* protocol landscapes ossify, *how* formalization changes coordination pressure, or *what happens* when optimization pressure is applied to protocol design under conditions of distributed governance or trust accumulation.

The work does not investigate whether automating protocol design via LLM-guided search introduces new failure modes (e.g., convergence on locally-optimal but fragile configurations), whether the solutions discovered are legible to downstream operators, or whether automation displaces rather than resolves the expertise bottleneck. It assumes the protocol design space is traversable via LLM reasoning without systematic error—a strong assumption that would require validation against L-005 (Gall's principle applied to protocol synthesis) and L-001 (whether automation-discovered protocols have different ossification trajectories than human-designed ones).

## Research connections

- **L-001:** No engagement. Does not ask whether LLM-discovered protocols ossify differently or faster than human designs; assumes discovery + deployment, not deployment dynamics.
- **L-005:** Potential tension unexamined. Gall's law suggests complex working systems cannot be replaced from scratch. LLM protocol design may discover novel configurations that violate this principle operationally.
- **seed-023:** Weak connection. Informality (expert judgment in protocol selection) is being automated away, but the paper does not track whether this produces novelty or homogenization in discovered protocol space.

## Seed

**Seed title:** none

---

**Rationale:** This is a tool application, not a primary theoretical or empirical source. It does not sustain a theoretical argument about protocol dynamics, does not introduce a novel mechanism absent from the inventory, and does not generalize beyond the specific domain (concurrency control design automation). The connections to L-001 and L-005 are suggestive but unexplored in the paper itself. Store as reference for future cross-domain comparison if evidence accumulates that automated protocol synthesis produces distinct failure signatures.
