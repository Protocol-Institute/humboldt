# Bounded Sovereignty and the Control Tax: Pricing AI Oversight When the Deployer Does Not Own the Model

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.19216
**Date read:** 2026-09-02
**Connected to:** L-001, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A policy and mechanism design paper analyzing the cost structure of AI safety oversight when deployment control is split between an API deployer (who controls business logic and user interaction) and a model provider (who controls weights, infrastructure, and serving). It introduces "bounded sovereignty" as a formal frame for this partial-control regime and estimates the contractual and technical overhead ("control tax") required to achieve equivalent safety guarantees to full-stack control.

## What I took from it

The paper is primarily a **cost accounting exercise** within an already-defined problem space (how to verify safe behavior under split custody). It does not present a sustained theoretical argument about protocol dynamics or the mechanisms by which such split-control regimes form, persist, or degrade. 

The work confirms L-006 (Coordination Cost Conservation) in a narrow sense: safety assurance requirements do not disappear when sovereignty is bounded; they migrate from technical instrumentation into contractual verification, logging, attestation, and audit infrastructure. The "control tax" is the residual friction cost of enforcing equivalent safety across a boundary.

However, the paper does not examine how this boundary itself ossifies (L-001), how the delegation of control creates novel optimization pressures, or what happens to trust and interpretability when the deployer cannot access internal model state. It is descriptive of the problem, not generative of mechanism.

## Research connections

- **L-001:** Bounded sovereignty may represent a structural pressure that accelerates ossification — once API-based deployment becomes standard, the model provider's interface and contractual terms become de facto frozen, even if not by formal consensus.
- **L-006:** Confirms the core observation: coordination cost (audit, attestation, contractual verification) is the new carrier of the safety burden, not eliminated by it.
- **seed-064:** Infrastructure-Trust Decoupling — the split between deployer and provider creates a new form of trust asymmetry where the deployer must rely on provider attestations rather than direct observation.
- **seed-070:** Obligate-Coordination-as-Infrastructure-Constraint — bounded sovereignty makes coordination between deployer and provider not optional but baked into the safety protocol.

## Seed

**Seed title:** Control Tax as Proxy for Coordination Boundary Opacity

**Seed type:** motif

**Seed text:** When technical control over a system is partitioned between two agents with misaligned observability (deployer sees outputs; provider sees internals), the safety assurance cost increases monotonically with the size of the observability gap. This cost cannot be eliminated, only redistributed across layers: instrumentation → logging → attestation → audit. In systems where the boundary is contractually fixed, the control tax becomes a floor on the minimum coordination overhead, and agents optimize within this constraint rather than seeking to breach it. This generalizes beyond AI deployment to any multi-agent protocol where one party's safety depends on another's internal state but lacks direct access.
