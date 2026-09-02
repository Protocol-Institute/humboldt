# FOI-O: A global ontology and verification framework for Freedom of Information process modelling

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.02947
**Date read:** 2026-09-02
**Connected to:** L-015, seed-030
**Kind:** tool/infrastructure
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper describing a formalizable ontology and verification infrastructure for modeling Freedom of Information request administration across multiple jurisdictions (New Zealand, Australia). The work treats FOI process records as mixed observational/inferred/legal signals and attempts to standardize how these are captured, verified, and audited.

## What I took from it

This is competent infrastructure work aimed at standardizing a messy governance domain, but the framing confirms rather than extends L-015 without introducing new mechanism. The paper demonstrates the problem L-015 names — formal records (request logs, decision traces, timelines) can be preserved perfectly while institutional understanding of *why those records were generated that way* and *what they should constrain* decays — but it treats this as a *solvability problem* (better ontology = better recovery) rather than as a *structural inevitability*. 

The global iteration (NZ → Commonwealth AU → NSW) is revealing for L-015 but as a confirmation: each jurisdiction must re-instantiate the ontology locally because interpretive continuity cannot be formally encoded. The paper does not examine why standardization across sites fails, or whether formal verification of FOI process traces actually improves downstream governance outcomes. No mechanism for how legibility restoration reverses institutional drift.

## Research connections

- **L-015:** Formal FOI records (timestamps, decision classifications, request metadata) persist perfectly; institutional memory of *regulatory intention and constraint interpretation* does not. The paper attempts to solve this via ontological standardization — a classic formalization ratchet response — but offers no evidence that formal traces recover lost interpretive consensus.

- **seed-030:** Not present in provided seed pool; triage note may refer to archived material. If seed-030 addresses formalization as anomaly-deferral, this paper illustrates it: by formalizing FOI process models, governance institutions create the illusion of transparency while the actual locus of decision-making (interpretive judgment) becomes less legible.

## Seed

**Seed title:** Formalization as Interpretive Opacity Displacement
**Seed type:** observation
**Seed text:** In governance systems where institutional decisions rest on interpretive judgment under ambiguous mandates, formalizing process traces (timestamps, classifications, audit logs) creates a legible record that survives institutional memory loss while displacing opacity rather than reducing it. The formal record becomes a proxy for understanding, masking the fact that the meaning-making layer — how rules are interpreted under pressure — has drifted or been lost. Attempts to recover governance coherence through ontological standardization across jurisdictions consistently fail because interpretive continuity cannot be reified as schema.
