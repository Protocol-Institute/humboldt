# Who Are You Explaining To? A Multi-Agent System for Audience-Aware XAI Narratives

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.11033
**Date read:** 2026-09-02
**Connected to:** L-012, seed-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper proposing multi-agent orchestration to generate audience-stratified explanations from learned feature-attribution outputs. The core technical claim is that a single numerical explanation (SHAP-style) must be reified into distinct communication acts for different stakeholder types (patients, clinicians, data scientists), and that naive LLM verbalization fails to preserve fidelity constraints.

## What I took from it

The paper documents a real coordination problem: the same decision-support artifact must satisfy incompatible legibility requirements across heterogeneous audiences. This is an instance of L-012 (Intervention-Layer Displacement), but applied orthogonally — rather than showing how prediction legibility shifts optimization pressure to the decision layer, it shows how **explanation legibility itself becomes a new optimization target that displaces the locus from model quality to narrative construction**.

The work is competent and practically motivated, but treats the audience-segmentation problem as a technical design challenge rather than as a symptom of a deeper regularity: when a protocol output (explanation) must simultaneously satisfy multiple, partially conflicting legibility requirements for different agents, the system will tend to ossify around whichever audience's constraint is most binding or most auditable. This is a special case of formalization under heterogeneous stakeholder pressure, not a new mechanism.

## Research connections

- **L-012:** Confirms the observation that when predictions are formalized as inputs to decision protocols (here: audience-specific communication acts), optimization pressure migrates from the model to the explanation layer.
- **seed-072:** Relevant to explanation-marker decoupling — the work shows that a single attribution can support multiple, contradictory explanatory narratives depending on audience framing.
- **seed-069:** Shows transparency-as-legibility substitution — what appears as "better explanation" is actually explanation tailored to maximize legibility for a specific stakeholder class.

## Seed

**Seed title:** Audience-Legibility Hierarchy as Ossification Driver

**Seed type:** observation

**Seed text:** In multi-stakeholder explanation protocols, when narrative legibility becomes a computable and auditable property, the system will tend to freeze explanation structure around the most legally or institutionally exposed audience rather than the most technically accurate one. The safest explanation under audit (e.g., for clinicians or regulators) becomes the binding constraint, and it propagates upward to shape explanations for all other audiences. Over time, explanation design becomes locked to the most conservative stakeholder's legibility requirements, not the most demanding one epistemically.
