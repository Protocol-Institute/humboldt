# Deployment-Time Memorization in Foundation-Model Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.10062
**Date read:** 2026-09-01
**Connected to:** L-001, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical characterization paper studying memory design choices in long-lived foundation-model agents as a privacy-utility tradeoff frontier. The work treats memorization not as an artifact of training but as an explicit operational protocol choice deployed at runtime, and audits how different memory configurations affect personalization benefit, data extraction vulnerability, and deletion compliance.

## What I took from it

The paper makes deployment-time memory design legible as a computable obligation — a measurable, tunable protocol surface that agents must actively configure rather than passively inherit from weights. This directly implicates L-008 (Proxy Optimization Under Computable Enforcement): as memory retention becomes precisely specifiable and auditable, optimizing agents will face pressure to exploit the boundary between what the memory protocol formally requires and what it permits. 

The work also touches L-001 (Protocol Ossification), but tangentially — it shows that memory configurations, once deployed for personalization benefit, become operationally sticky (users and downstream systems condition on them), but the paper does not examine whether this stickiness increases with deployment duration or adoption breadth. The contribution is competent empirical scope-setting rather than mechanism discovery. It identifies a tuning surface, not a law governing how that surface evolves under stress.

## Research connections

- **L-008:** Memory design choices become computable proxies for privacy/utility goals; agents optimizing against legible enforcement signals will concentrate risk at protocol boundaries (e.g., extraction during the "deletion window").
- **L-001:** Deployment-time memory configurations may ossify under operational persistence, but the paper does not track this decay or adoption-pressure effects over time.
- **seed-014 (if extant):** Deletion fidelity as a formal obligation introduces a new verification-execution asymmetry: auditing what was *not* retained is harder than auditing what was.

## Seed

**Seed title:** Memory Protocol Boundary Concentration
**Seed type:** motif
**Seed text:** When memory retention becomes a computable, auditable, and tunable deployment-time protocol, optimizing agents will concentrate extraction and evasion risk at the formal boundaries of the memory specification (e.g., pre-deployment history, deletion grace periods, cross-session inference windows) rather than distribute it across the system. The phenomenon generalizes to any protocol where the enforcement boundary is sharp and the interior is legible: risk flows to the margin between what is formally governed and what is not.
