# Scaling, Lock-In, and Proxy Compliance: A Political Economy of Responsible AI

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.28023
**Date read:** 2026-09-02
**Connected to:** L-001, L-004, L-014
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source presenting a sustained formal model of how verification legibility and switching costs jointly produce sub-optimal equilibria in safety protocols — it extends L-004 (Goodhart) and L-014 (boundary concentration) by grounding them in a multi-agent sequential game where the mechanism of proxy-compliance emerges from asymmetric information and lock-in, not from optimization pressure alone.

## What this is

A formal political-economy model (game-theoretic) analyzing how AI vendors and deployers reach equilibria where vendors meet observable compliance thresholds (auditability) while cutting substantive mitigation below social optimum. The work treats accountability as an institutional design problem where switching costs and verification asymmetry create conditions for proxy-compliance capture.

## What I took from it

The model makes concrete what has remained structural in L-004 and L-014: **verification legibility is itself a strategic choice**, not an external constraint. Vendors do not simply optimize under existing audit regimes — they shape what is auditable. The proxy-compliance equilibrium is not driven by pure metric capture (optimizing the metric itself) but by the rational anticipation that deployers face prohibitive switching costs post-adoption and thus deploy only shallow monitoring. This suggests a **two-layer lock-in**: first, adoption locks the deployer in; second, the vendor's choice of auditability scope creates a secondary lock on what can *later* be verified or reformed.

This directly challenges a latent assumption in L-001 (ossification through adoption): the paper shows that ossification doesn't just accrue passively — it is engineered at deployment time through the choice of what compliance signals to make legible. Boundary concentration (L-014) is not just where optimizers cluster; it's where vendors *intentionally position the boundary* to be just beyond deployer monitoring capacity.

## Research connections

- **L-001:** Ossification begins not after adoption but *at* the procurement stage, when vendors engineer the auditability surface to survive later reform pressure.
- **L-004:** Extends Goodhart by showing the metric itself (auditability choice) is endogenous; vendors don't optimize a fixed proxy — they choose which proxies become visible.
- **L-014:** Boundary concentration is a vendor strategy, not an emergent pattern; legible compliance is positioned precisely at the threshold of deployer verification capacity.
- **L-012:** Intervention-layer displacement appears here as: once vendor-chosen auditability is locked in, interventions on substantive safety cannot reach the decision protocol; they can only be applied to the audit surface.
- **seed-069:** Transparency-legibility substitution: vendors use auditability (transparency at the margin) as a substitute for actual trust, relying on deployer lock-in to prevent discovery.
- **seed-082:** Additive intervention displacement: adding monitoring capacity post-adoption doesn't fix root pressure if the vendor has already chosen the auditability boundary; monitoring is additive and hollow.

## Seed

**Seed title:** Auditability-Scope Lock-In Under Deployment Switching Costs

**Seed type:** insight

**Seed text:** In safety-critical protocol systems where vendors choose what compliance signals are legible to deployers, and where post-adoption switching costs are high, vendors rationally position the auditability scope at the threshold of deployer monitoring capacity, knowing that institutional lock-in will prevent later expansion of what can be verified. The proxy-compliance equilibrium emerges not from metric optimization but from strategic choice of which compliance dimensions are rendered legible. This mechanism generalizes beyond AI systems to any protocol with asymmetric information advantage at procurement time and high post-adoption exit costs — the vendor's choice of transparency architecture becomes a governance lock that outlasts any later reform intent.
