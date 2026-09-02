# Applied and Filtered: An End-to-End Algorithmic Fairness Audit of A Public Employment Agency

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.13022
**Date read:** 2026-09-02
**Connected to:** L-012, L-014
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** —

## What this is

An empirical audit of a semi-automated hiring system (TalentClue) deployed in a public employment agency (Barcelona Activa), analyzing ~497k candidate-vacancy entries across seven pipeline stages (Sep 2017–Sep 2022). The work treats the algorithmic system not as an isolated technical component but as embedded in organizational workflow, attempting to trace fairness outcomes across the full pipeline rather than within a single decision node.

## What I took from it

This appears to be a confirmatory case study rather than a mechanism-discovery paper. It documents the phenomenon that intervention-layer displacement and strategic boundary concentration occur in practice—that is, fairness problems don't stay localized in the algorithm but migrate across organizational layers and decision boundaries—but does not theorize *why* this happens or under what conditions it generalizes.

The implicit finding (inferred from the framing) is likely that narrowing audit scope to the algorithmic component misses where fairness failure actually accumulates. This supports L-012 and L-014 phenomenologically but does not explain the underlying dynamics or provide a generalizable mechanism. The work is important for validation but does not advance the law inventory or settle open mechanism questions.

## Research connections

- **L-012:** Intervention-Layer Displacement — documents that fairness interventions at the algorithm layer do not contain fairness outcomes; pressure migrates to other pipeline stages.
- **L-014:** Strategic Boundary Concentration — suggests that when legality/fairness becomes bounded to computable components (the algorithm), optimization pressure concentrates at organizational or procedural boundaries instead.
- **seed-062 (Formalization Opacity Collapse):** The audit likely exposes gap between what formalizes (algorithm) and what actually shapes outcomes (human discretion, filtering, application of results).

## Method note

This work validates the necessity of **end-to-end system audits** as a methodological posture: single-component fairness evaluation systematically fails to detect where actual harm or bias accumulates. For protocolized systems research, this suggests auditing should trace **causal responsibility across layers**, not assume protocol boundaries correspond to responsibility boundaries. It also demonstrates that meta-research on audit methodology itself—how to instrument complex sociotechnical systems—is necessary infrastructure for law discovery in this space.
