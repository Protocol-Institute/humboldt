# Measuring Agents in Production

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2512.04123
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study documenting deployment practices and evaluation methods for LLM-based agents in production across 26 domains (20 case studies + 86 surveyed practitioners). The work is primarily descriptive and inventory-building rather than theoretical or mechanistic—it characterizes *what works in practice* without advancing a testable claim about the underlying laws governing agent behavior or system dynamics.

## What I took from it

This is valuable operational ethnography of the "new nature" under construction, but it operates at the documentation layer rather than the mechanism layer. The paper establishes baseline empirical facts about how humans currently *measure and validate* autonomous agent behavior in constrained domains—essentially a field guide to current protocolization attempts. It will be useful for understanding adoption friction and evaluation bottlenecks, but does not establish or challenge a law of protocolized systems; rather, it catalogs the ad-hoc measurement regimes that exist *before* such laws would be formalized.

The gap between what practitioners measure (success metrics, failure modes, user satisfaction) and what the "new nature" research agenda tracks (scaling laws, emergence patterns, protocol stability under load) suggests this is parallel work: important context, not theoretical contribution.

## Research connections

- none yet established

## Candidate laws or signals

- **CL-MAP-1:** Measurement practice in production agent systems remains domain-specific and heterogeneous across industries; no convergence yet on universal evaluation primitives for autonomous system behavior.
