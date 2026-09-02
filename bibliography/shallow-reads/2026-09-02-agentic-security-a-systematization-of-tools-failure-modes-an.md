# Agentic Security: A Systematization of Tools, Failure Modes, and Design Laws for LLM-Driven Penetration Testing

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.21423
**Date read:** 2026-09-02
**Connected to:** L-001, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systematization paper cataloging failure modes in LLM-driven security automation pipelines, grounded in hands-on evaluation of ten deployed tools. Introduces an Integration Friction Index to separate one-time engineering cost from recurring organizational, legal, and maintenance friction—mapping the gap between lab demonstrations and production deployment.

## What I took from it

The paper documents a recurring pattern: systems that work in controlled settings accumulate operational failures under real deployment pressure that are *orthogonal to* the underlying LLM capability or tool quality. This maps cleanly onto L-013 (Paradigm-Locked Anomaly Tolerance)—teams continue deploying systems that show mounting evidence of malfunction because the system is *architecturally committed* and the failure modes don't trigger paradigm revision; they're absorbed as "integration friction" or "organizational constraints."

The Integration Friction Index itself is a measurement artifact worth tracking. By separating one-time cost from recurring friction, the paper makes visible a hidden coordination cost (L-006 candidate) that doesn't disappear under protocol layer transitions—it just gets redistributed. When you move from manual pentesting to agentic pentesting, you don't eliminate friction; you move it from human operator judgment to tool orchestration, compliance, and escalation overhead. The paper suggests this is *conserved*, not eliminated.

However, the work remains primarily a tool-focused systematization. It catalogs failure modes but does not sustain a claim about a mechanism that generalizes beyond LLM-driven security tooling, nor does it challenge or extend an existing law. It confirms existing suspicions about ossification and anomaly tolerance but does not provide a novel theoretical or empirical spine.

## Research connections

- **L-001:** Confirms the pattern—deployed security tool suites become harder to modify even when failure modes are documented; adoption inertia blocks revision.
- **L-013:** Direct evidence of anomaly tolerance: teams continue operating systems with known, documented failure modes because the system is embedded and paradigm revision is costly.
- **L-006:** Suggestive—the Integration Friction Index hints at a conserved coordination cost across layers (manual → agentic), but the paper does not formalize or test this.
- **seed-076 (Handler-Lodged Ossification in Opaque Protocols):** The paper documents how tool integration locks become embedded in organizational process layers, making the friction "opaque" to re-architecture.

## Seed

**Seed title:** Integration Friction as Conserved Coordination Overhead

**Seed type:** observation

**Seed text:** In protocol transitions from manual to automated execution (e.g., manual pentesting to agentic pentesting), coordination cost does not decrease; it shifts from operator cognition to organizational orchestration, compliance, and escalation overhead. The total friction—measured as engineering, legal, maintenance, and organizational cost—appears to be *conserved* across the transition, suggesting a deeper law about where coordination burden can be moved but not eliminated. This would generalize beyond security tooling to any system undergoing formalization under adoption pressure.
