# Remote ID Spoofing-Aware Trajectory Planning for Small Unmanned Aerial Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.19650
**Date read:** 2026-09-02
**Connected to:** L-008, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A control systems paper presenting a decentralized trajectory planner for small UAS that explicitly models Remote Identification (RID) broadcasts as spoofable and incorporates signal-strength verification to reduce collision risk. The work treats a legible but unverified identity signal as an attack surface and proposes physical-layer redundancy (RSSI) as a credibility filter.

## What I took from it

This is a competent domain-specific application of adversarial signal reasoning to a safety-critical protocol, but it does not generalize the underlying mechanism. The paper confirms the tactical insight that legible identity broadcasts become optimization targets when enforcement is distributed and verification is costly — this is squarely within L-008 and L-014's scope. However, the solution (RSSI-based verification) is hardware-specific and does not illuminate a generalizable law about how computable legality creates strategic boundary concentration or how optimization pressure migrates under formalization.

The work demonstrates the symptom clearly: agents optimizing against spoofable identity signals in a safety-critical coordination space. But it does not investigate *why* identity became the computable legible target, nor does it explore whether the same pattern recurs in non-aerial domains where identity or location proxies are formalized and machine-readable. It treats the spoofing problem as a local control engineering challenge rather than as an instance of a broader protocol vulnerability class.

## Research connections

- **L-008 [Proxy Optimization Under Computable Enforcement]:** Confirms the tactical pattern — when RID identity becomes a legible, computable input to collision avoidance logic, it becomes an optimization target for spoofing attacks. But does not theorize the generalization.
- **L-014 [Strategic Boundary Concentration Under Computable Legibility]:** The paper shows agents concentrating attack pressure on the legible (RID broadcast) rather than the hard-to-forge (physical position). Validates the pattern but within a narrow domain.
- **seed-080 [Proxy Collapse Under Upstream Asymmetry in Automated Systems]:** RID as a proxy for verified identity collapses when the upstream source (the UAS's own broadcast) is spoofable and the downstream consumer (collision-avoidance planner) cannot independently verify. Relevant but not explored.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**RATIONALE FOR STORE-ONLY:** This paper applies existing mechanistic understanding to a specific safety domain without introducing a mechanism not already in the inventory, without cross-domain theoretical contribution, and without challenging or extending the current laws. The insight is tactical confirmation, not foundational.
