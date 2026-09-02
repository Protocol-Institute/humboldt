# Extracting ODRL Policies from Business Process Models: A Graph Traversal Approach to Compliance-by-Extraction

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.02607
**Date read:** 2026-09-02
**Connected to:** L-003, seed-036
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper proposing automated extraction of machine-readable policy (ODRL) from informal business process models (BPMN) via graph traversal. The work addresses the scaling bottleneck of translating implicit normative content in procedural representations into formal, computable policy language.

## What I took from it

This is a **competent engineering response to a real coordination problem**, but not a theoretical contribution. The paper documents a legitimate friction: organizations hold vast procedural knowledge in BPMN but cannot feed that into policy infrastructure without expensive human reauthoring. The extraction approach is sound—treating process models as directed graphs and mapping control flow, roles, and constraints to ODRL predicates.

However, the work *exemplifies* rather than interrogates L-003 (Formalization Ratchet). It shows the mechanics of norm-to-formalism conversion under scaling pressure, but does not investigate the deeper claim: whether and how formalization *changes the norm itself*, introduces new vulnerabilities, or locks downstream adaptation. The paper assumes formalization is a lossless compression problem; it does not ask whether the translation introduces systematic bias, closure of interpretation, or new optimization targets (seed-072, seed-080).

The technical approach is also orthogonal to the mechanisms that actually drive protocol ossification, goodhart capture, or coordination cost displacement—it is a tool that *accelerates* formalization, not an analysis of what formalization *does* to a system under stress.

## Research connections

- **L-003:** Confirms the observable pressure to formalize norms under scaling and compliance demand; does not theorize the consequences.
- **seed-036:** Consistent with formalization-as-scaling-response, but no novel mechanism or boundary condition identified.
- **seed-062:** Implicit connection: automated extraction may accelerate "Formalization Opacity Collapse" if the extraction heuristics are not transparent to downstream policy readers.

## Seed

**Seed title:** none
