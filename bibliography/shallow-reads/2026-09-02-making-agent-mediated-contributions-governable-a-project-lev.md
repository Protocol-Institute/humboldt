# Making Agent-Mediated Contributions Governable: A Project-Level Governance Manifest for Open-Source AI Collaboration

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.15769
**Date read:** 2026-09-02
**Connected to:** L-001, L-003, seed-021
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A diagnostic and prescriptive paper on governance infrastructure for agent-generated contributions in open-source software. The work audits 50 GitHub repositories to identify gaps in project-level rules and review gates designed to handle the volume and risk profile of AI-assisted code contributions, then proposes an organizational framework for "governability infrastructure."

## What I took from it

The paper confirms the empirical premise of L-001 (protocol ossification under adoption pressure) and L-003 (formalization ratchet under stress) in a concrete domain: OSS projects are experiencing a scaling crisis where agent-mediated contributions arrive faster than maintainers can review them, forcing rapid formalization of previously informal review norms. The diagnostic audit reveals that existing projects lack structured risk and evidence gates; governance is reactive and ad hoc. The proposed solution—explicit project-level rules organizing contribution-specific risk states and accountability markers—is a direct instantiation of the formalization ratchet: informal coordination (ad-hoc review, trust-based gatekeeping) is being replaced by formal, computable legibility (risk classification, evidence requirements, audit trails).

However, the paper does not probe the *cost* of this formalization or track whether the new governance infrastructure itself becomes resistant to change (the ossification problem). It also does not investigate whether the legibility requirements imposed by agent traceability inadvertently shift optimization pressure onto the *form* of contributions rather than their correctness—a candidate instantiation of L-008 (proxy optimization under computable enforcement). The work is primarily a design and audit contribution, not a mechanism investigation.

## Research connections

- **L-001:** Confirms the adoption pressure → formalization dynamic; does not measure ossification lag or resistance.
- **L-003:** Direct evidence of informal norms being replaced by formal rules under scaling stress; formalization is the coping mechanism.
- **seed-021:** Aligns with the governance capacity saturation hypothesis; agent scaling outpaces review bandwidth.

## Seed

**Seed title:** Legibility-Driven Review Gate Displacement
**Seed type:** observation
**Seed text:** When contribution volume scales beyond maintainer review capacity, projects formalize governance by making contribution properties (risk, evidence, accountability state) legible and machine-readable. This shifts the optimization pressure from *correctness assessment* to *compliance with legibility requirements*. Agents and contributors then optimize for the formal markers (audit trails, risk labels, evidence slots) rather than the underlying properties those markers were meant to signal. The governance infrastructure designed to enable assessment becomes a new optimization target, decoupling form from intent—a candidate instance of L-012 and L-008 under domain-specific conditions.
