# A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2611.24039
**Date read:** 2026-11-23
**Connected to:** L-001, L-013
**Kind:** meta
**Escalation:** store-only

## What this is

An industrial case study documenting a "bakeoff" evaluation conducted by a global bank's innovation lab to assess agentic AI platforms for enterprise deployment. The paper reports a mismatch between benchmark-driven procurement (which measures isolated model capability) and actual platform performance (which is dominated by orchestration, memory, governance, and tooling layers), and argues that enterprises are adopting these systems faster than measurement frameworks can validate them.

## What I took from it

This is a canonical observation of **L-013 (Paradigm-Locked Anomaly Tolerance)**: the banking sector has a mature procurement apparatus optimized for traditional software and model evaluation, but that apparatus cannot measure the salient failure modes and integration risks of agentic platforms. The paper documents the lag between capability attestation (vendor demos, benchmark scores) and operational validation (platform-level stability, governance layer robustness). This confirms the broader pattern that established institutions tolerate accumulating evidence of measurement inadequacy—here, the evidence is explicit ("procured faster than they can be measured")—without triggering paradigm revision. The framework itself is an attempt at remediation, but the meta-pattern remains: the innovation cycle (procurement velocity) is outpacing the assurance cycle (measurement maturity). This also touches **L-001 (Protocol Ossification Under Adoption Pressure)**: once a platform is embedded in enterprise systems, switching costs and trust accumulation lock in architectural choices (orchestration, memory, governance patterns) that become difficult to revise even if measurement later reveals them to be suboptimal.

## Research connections

- **L-001:** Procurement under incomplete measurement creates locked-in platform choices that resist later modification; adoption velocity exceeds the ability to establish reversibility criteria.
- **L-013:** Banks continue to deploy agentic systems using legacy procurement and audit frameworks despite explicit awareness that those frameworks do not measure the actual failure modes of multi-layer agent orchestration.
- **seed-554:** Formal risk category lag under operational capability adoption — the bank's risk taxonomy and audit procedures lag behind the operational surface area introduced by agentic platforms.
- **seed-452:** Legitimacy collapse under macro formalization — vendor demos provide legitimacy signal, but formalized measurement frameworks cannot yet codify the same signal, creating delegitimacy pressure on institutional buyers.

## Method note

This paper suggests that measurement inadequacy should not be treated as a technical problem awaiting solution, but as a stable institutional equilibrium worth modeling. The case demonstrates that awareness of measurement gaps does not automatically trigger framework revision; instead, procurement and deployment continue under old paradigms, generating a parallel shadow evaluation culture (vendor bakeoffs, internal proofs-of-concept). Research on protocolized systems in this space should map not just the technical gaps but the institutional incentive structures that sustain paradigm-locked evaluation regimes. This suggests that regulatory and procurement meta-research is as strategically important as domain-specific capability measurement.
