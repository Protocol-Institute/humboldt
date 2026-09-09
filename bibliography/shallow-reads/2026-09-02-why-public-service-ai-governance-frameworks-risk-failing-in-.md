# Why Public Service AI Governance Frameworks Risk Failing in the Age of General-Purpose AI: Lessons from Policing

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.25648
**Date read:** 2026-09-02
**Connected to:** L-001, L-003, L-013
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source arguing that generality in protocol design (GPAI) systematically undermines the governance conditions under which safety has historically been achievable — a direct challenge to L-001 (ossification under adoption) and L-013 (paradigm-locked anomaly tolerance), with a mechanism absent from current inventory.

## What this is

A CS.CY position paper arguing that general-purpose AI systems deployed in public services (specifically policing) create a fundamental mismatch between the historical conditions under which AI safety governance evolved and the structural properties of GPAI itself. The paper claims that generality, accessibility, and low deployment cost — GPAI's core attractions — directly erode the ossification, domain-specificity, and legibility that prior AI safety frameworks relied upon.

## What I took from it

This work identifies a **generality-governance inversion**: safety frameworks were built assuming domain-specificity, high switching costs, and concentrated deployment (conditions favoring ossification and paradigm lock). GPAI inverts all three. The paper argues that when a protocol system becomes general-purpose and low-cost to deploy, it cannot accumulate the operational trust (L-007) or formalization ratchet (L-003) that normally stabilizes governance — instead, it spreads too fast, across too many contexts, for any single governance frame to bind. This is not a failure of *particular* governance designs; it's a structural incompatibility between generality and the conditions under which protocol ossification and trust accumulation occur.

The policing case is instructive: once GPAI is accessible, deployment happens *before* governance can crystallize. The paper suggests this is not anomalous (L-013 paradigm-locked tolerance) but structural. Governance paradigms built for narrow-domain AI cannot "see" the failure mode until GPAI has already migrated across institutional boundaries.

## Research connections

- **L-001:** Directly challenges — suggests adoption pressure + generality may *prevent* ossification rather than force it, leaving protocols fluid and ungovernable rather than rigid and stable.
- **L-003:** The formalization ratchet assumes stress triggers formal replacement of norms; GPAI's low deployment cost may allow norm-evasion at scale before formalization pressure builds.
- **L-013:** Paradigm-locked anomaly tolerance may be structurally irreversible once GPAI enables cross-domain redeployment faster than institutional sense-making.
- **seed-062 (Formalization Opacity Collapse):** GPAI's prompt-driven interface may create a transparency illusion (easy to use = easy to govern) while hiding actual decision-making surface beneath generative opacity.
- **L-012 (Intervention-Layer Displacement):** GPAI's generality means the legible input layer (the prompt) is not the actual decision boundary; interventions at governance layer may not reach decision optimization pressure.

## Seed

**Seed title:** Generality-Governance Asymmetry in Protocol Deployment

**Seed type:** motif

**Seed text:** In protocol systems where the unit of deployment (the model, the system) is general-purpose and low-cost to instantiate, the speed of cross-domain redeployment can outpace the formation of domain-specific governance frames. This creates a stable equilibrium in which protocols spread before trust accumulates (inverting L-007) and governance ossification cannot occur (inverting L-001) because the system is already fluid across contexts. The mechanism: generality decouples deployment from institutional embedding. This pattern should generalize beyond AI to any protocol where versatility and accessibility are inversely correlated with legibility and domain-specificity.
