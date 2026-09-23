# Stop Removing Stopwords: How an Inherited Preprocessing Default Distorts Legal Text-as-Data

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.19153
**Date read:** 2026-09-22
**Connected to:** L-003, seed-144
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study documenting how a mid-century information retrieval preprocessing convention (stopword removal) has persisted unchallenged into modern legal text-as-data pipelines, with demonstrated harmful effects on classification accuracy and interpretability. The work performs exhaustive single-word ablation to measure task-specific impact rather than accepting inherited defaults.

## What I took from it

This is a case study in **protocol inheritance without validation** — a pattern directly relevant to L-003 (Formalization Ratchet) and seed-144 (Informality as Coordination Cost Refuge). The paper reveals how a design choice embedded in mid-century IR systems became formalized into modern legal NLP pipelines without ever being stress-tested against the actual task (legal text classification). When formalization occurs through adoption rather than deliberate validation, inherited defaults survive even when they degrade performance.

The mechanism is subtle: stopword removal was rational under *computational scarcity* (1950s), became a *best practice norm*, and then persisted as *unexamined infrastructure* in domains (legal text analysis) where the assumptions no longer held. This mirrors how informal coordination norms become hardened into protocol under scaling pressure (L-003), but inverted — here, an artifact of *past* formalization becomes an invisible constraint on *present* practice. The paper's intervention (measuring task-specific impact via ablation) is methodologically sound but reveals a gap: the field had no systematic mechanism to surface and validate inherited assumptions in preprocessing pipelines.

## Research connections

- **L-003:** Demonstrates a variant of formalization ratcheting: formal preprocessing conventions, once adopted at scale, resist re-examination even when no longer fit for purpose.
- **seed-144:** Stopword removal as a case where informal judgment (which words matter in legal context) was replaced by a formalized rule inherited from a different domain, then treated as settled.
- **seed-133:** Related pattern — preprocessing defaults function as a "paradigm lock" that prevents certain classes of evidence (the linguistic signal in function words) from being visible to downstream analysis.

## Method note

This work models a valuable research posture: systematic ablation of inherited assumptions in protocolized systems, rather than accepting "standard practice" as justified. For the new nature research agenda, this suggests that **infrastructure archaeology** — tracing where design choices originate and whether their original constraints still apply — should be a standing practice. The paper's contribution is not a novel algorithm but a discipline: exhaustive validation of inherited defaults before they calcify into canon. This is particularly relevant for systems that blend human-legible interpretability with formal optimization, where bad defaults can persist indefinitely if they don't obviously break quantitative metrics.
