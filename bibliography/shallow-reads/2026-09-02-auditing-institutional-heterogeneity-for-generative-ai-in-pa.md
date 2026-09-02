# Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.22606
**Date read:** 2026-09-02
**Connected to:** L-004, L-015
**Kind:** empirical audit
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A large-scale content audit of 102 US transplant center patient-education handbooks, measuring disagreement patterns across 5.7M pairwise comparisons using LLM-based structured judgment. The work tests the premise that grounding generative AI in "local" institutional documents produces consistent guidance—and finds substantial heterogeneity in medical guidance across nominally equivalent institutional contexts.

## What I took from it

This is a direct empirical measurement of **L-015 (Interpretive Continuity Decay)** in its institutional form: formal documents survive intact, but their semantic content diverges under distributed authorship. The paper shows that when a protocol (patient education) is formalized into legible, machine-readable documents across independent instantiations of the same institutional type, the documents *agree in form* but *diverge in substance*—yet downstream systems (generative AI assistants) treat them as equivalent and grounded.

The work does *not* argue this is a bug in AI; it reveals the bug was already in the institution. The heterogeneity predates the AI layer. This complicates **L-004 (Goodhart Generalization)**: the metric here (local grounding) fails not because optimization pressure distorts it, but because the underlying coordination infrastructure was never uniform to begin with. Formalization masks rather than resolves institutional fragmentation. The study is a careful measurement of institutional fiction—the shared assumption that "transplant center best practices" exist uniformly—collapsing under legibility.

## Research connections

- **L-004:** Goodhart failure occurs at document level before AI optimization begins; grounding-as-proxy masks rather than solves heterogeneity
- **L-015:** Formal audit traces (handbooks) survive intact; institutional meaning and coordination practice diverge silently across distributed sites
- **seed-062 (Formalization Opacity Collapse):** Formalizing patient education for machine consumption exposes pre-existing semantic fragmentation that informal practice concealed
- **seed-069 (Transparency-Legibility as Trust Proxy Substitution):** "Grounding in local documents" operates as a trust proxy that substitutes for actual institutional alignment; the audit breaks this proxy
- **seed-073 (Correlated Failure Under Proxy Consensus):** Multiple AI systems deployed across sites will fail in correlated ways when they inherit the same underlying document heterogeneity

## Seed

**Seed title:** Formalization-Exposed Institutional Heterogeneity in Safety-Critical Domains

**Seed type:** observation

**Seed text:** When safety-critical coordination norms are formalized into legible, machine-readable documents for integration into automated systems, the formalization process exposes pre-existing heterogeneity in institutional practice that informal coordination had successfully masked. This heterogeneity is not created by formalization or by downstream optimization pressure; it is *revealed* by it. The regulatory and operational assumption that "grounding in local institutional knowledge" eliminates ambiguity fails when that local knowledge was never actually coordinated across institutional peers. In safety-critical domains (medicine, finance, critical infrastructure), this pattern suggests that formalization for automation may force resolution of coordination deficits that were previously stable under informality, creating acute governance crises at the moment of legibility. This generalizes beyond patient education to any distributed institution-of-institutions attempting to deploy unified automated systems.
