# Governance-as-Code: Translating EU AI Act Technical Requirements into Executable Compliance Pipelines for Generative AI Systems

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.20016
**Date read:** 2026-09-22
**Connected to:** L-001, L-014, seed-133
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical operationalization paper that translates seven identified gaps between the EU AI Act's regulatory language and generative AI system realities into 43 machine-checkable acceptance criteria organized across a CI/CD compliance pipeline. The work is domain-specific (EU AI Act + generative AI) and primarily constructive/engineering-focused rather than advancing a sustained theoretical or empirical argument about protocol behavior.

## What I took from it

The paper documents a real problem in the formalization-to-execution gap: regulatory text written for older AI paradigms creates ambiguities when applied to non-deterministic, emergent systems. The GaC framework represents an *instance* of the Formalization Ratchet (L-003) — stress (regulatory adoption pressure) driving informal coordination norms toward computable proxies. However, the paper does not examine what happens *after* operationalization: whether the machine-checkable criteria themselves become the de facto compliance target, displacing the original regulatory intent; whether non-determinism in generative systems creates systematically unauditable gaps in the pipeline; or whether the legibility of the acceptance criteria triggers the optimization dynamics predicted under L-008 and L-014.

The work is descriptive of a symptom rather than investigative of the underlying mechanism. It does not track whether the boundary between "auditable" and "non-auditable" generative behavior concentrates at the margins of the pipeline (L-014), nor does it measure whether formalization of compliance metrics produces the metric capture predicted under L-004.

## Research connections

- **L-001 (Protocol Ossification):** The paper shows pressure to formalize vague regulatory language into executable rules under adoption deadline, consistent with the law's prediction, but does not measure post-formalization rigidity or resistance to modification.

- **L-014 (Strategic Boundary Concentration Under Computable Legality):** The 43 acceptance criteria convert regulatory obligations into computable targets. The paper does not examine whether optimization pressure concentrates at the boundaries of what the pipeline can formally verify versus what remains opaque in generative behavior.

- **seed-133 (Metric Formalization as Paradigm Lock in Safety Protocols):** The translation from Articles 8–15 into machine-checkable criteria is an instance of safety-relevant compliance becoming legible as a metric. The paper does not investigate whether this formalization locks downstream interpretation of "compliance" to pipeline pass/fail signals, independent of actual system safety.

- **seed-142 (Auditability-Legibility Trap in Trust Governance):** The framework produces detailed audit traces of compliance pipeline results but does not address whether the legibility of the pipeline output creates false confidence in regulatory control over non-deterministic, emergent behavior.

## Seed

**Seed title:** Computable-Incomputable Boundary Displacement in Legalized AI Systems

**Seed type:** observation

**Seed text:** When regulatory obligations written in natural language are operationalized as machine-checkable acceptance criteria in automated compliance pipelines, the locus of strategic optimization and agent effort shifts from satisfying the original regulatory intent to passing the pipeline's formal checks. In systems with irreducibly non-deterministic or emergent behavior (generative AI), this displacement creates a systematic gap: behaviors that pass the pipeline may violate the original regulatory principle, and behaviors that fail the pipeline may be harmless. This suggests that formalizing safety-critical or compliance-critical obligations under adoption pressure does not eliminate the informal-to-formal gap; it relocates it to the boundary between what the pipeline can formally verify and what remains opaque — a relocation that may increase systemic risk by creating the appearance of legibility without corresponding control.
