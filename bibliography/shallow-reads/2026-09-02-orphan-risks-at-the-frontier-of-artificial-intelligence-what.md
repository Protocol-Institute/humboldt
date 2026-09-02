# Orphan risks at the frontier of artificial intelligence: What diverging safety and compliance frameworks reveal about how AI companies choose the risks they prioritize

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.16895
**Date read:** 2026-09-02
**Connected to:** L-004, L-014
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source documenting sustained divergence between competing risk accounting systems within a single protocol domain (AI safety governance); reveals mechanism of strategic boundary concentration under computable compliance pressure that extends beyond the specific case and challenges assumptions about unified protocol design.

## What this is

An empirical investigation of how frontier AI companies maintain multiple, diverging accounts of risk — distinct safety frameworks vs. compliance frameworks — and strategically choose which risks to prioritize. The work documents the gap between what companies identify as possible failure modes and what they operationalize as actionable risk categories.

## What I took from it

The paper establishes that risk prioritization in AI governance is not a unified inference problem but a **strategic selection problem**. Companies are not simply discovering which risks matter; they are choosing which risks to render legible and actionable within computable compliance structures. This is a direct instantiation of L-014 (Strategic Boundary Concentration Under Computable Legality): when obligations become machine-readable and enforceable, optimizing agents concentrate resources at the boundaries between what is computable/auditable and what is not.

The "orphan risks" — those identified in safety discourse but absent from compliance frameworks — represent a systematic pattern: risks that are real but hard to formalize, measure, or attribute become invisible to protocol enforcement. This suggests a deeper mechanism: **formalization creates not just clarity but systematic blindness**. The divergence is not accidental; it reflects rational response to the asymmetry between the cost of addressing unmeasurable risks and the cost of addressing measurable ones.

This connects to L-004 (Goodhart Generalization) but inverts its emphasis: the paper shows not just metric capture but **metric avoidance** — the strategic exclusion of unmeasurable dimensions from the protocol itself. This is likely to generalize to any safety or governance protocol where compliance is rendered computable.

## Research connections

- **L-004:** The divergence between safety and compliance frameworks is a Goodhart effect operating at the framework-selection level—companies adopt the metric system that most favors their operational profile, not the one most predictive of actual harm.
- **L-014:** Direct evidence of Strategic Boundary Concentration: legible risks cluster at the boundary of what is computable; unmeasurable risks are systematically displaced from governance protocols.
- **L-013:** The paper may document Paradigm-Locked Anomaly Tolerance: how established compliance frameworks tolerate accumulating evidence of divergence from ground-truth risk landscapes without triggering protocol redesign.
- **seed-068:** Unmeasurability as Anomaly Insulation — the paper shows that risks rendered unmeasurable are insulated from governance pressure.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry — compliance frameworks become proxies for safety; when upstream risk identification diverges from downstream compliance, the proxy collapses silently.
- **seed-082:** Additive Intervention in Overloaded Protocols Preserves Root Pressure — adding safety frameworks without restructuring compliance protocols may preserve the underlying pressure toward strategic boundary concentration.

## Seed

**Seed title:** Risk Legibility Stratification in Governance Protocols

**Seed type:** observation + mechanism

**Seed text:** When protocol governance systems render some risk dimensions computable and leave others informal, the system stabilizes into a two-tier risk landscape: formalized risks (subject to enforcement, resource allocation, and accountability) and orphaned risks (identified but unactionable, systematically deprioritized). This stratification is not resolved by adding additional risk frameworks; parallel frameworks create competing legibility signals, intensifying the pressure to concentrate resources on the computable tier. The mechanism generalizes: any safety or governance protocol that treats formalization and enforcement as coupled operations will systematically displace unmeasurable risks into an invisible residual category, and this displacement is stable under optimization pressure.
