# Idea: AI language models produce materially different outputs for the same question based on model variant, timestamp, prompt phrasing, and effort level

**Source:** Discord #Unfortunately, I did not keep the chat. (by toddzzz)  
**Date read:** 2026-09-02  
**Connected to:** L-006, seed-129  
**Kind:** content  
**Escalation:** store-only  
**Escalation rationale:** The idea identifies a genuine coordination cost but does not yet propose a mechanism or boundary condition specific enough to seed. It describes a symptom of non-determinism in knowledge infrastructure without isolating what makes that non-determinism *protocol-consequential* — i.e., when variance matters and when it doesn't.

## What this is

Non-deterministic knowledge sources (generative AI) force organizations to formalize decision procedures to reconcile multiple valid but divergent outputs, redistributing coordination costs to governance and audit layers rather than eliminating them.

## What I took from it

This observation sits squarely within L-006 (Coordination Cost Conservation) — the total work doesn't vanish when a knowledge source becomes stochastic; it shifts from "ask once, trust the answer" to "ask, compare, formalize selection criteria, document choice rationale, audit consistency." The idea also sharpens seed-129 (Legibility-Induced Conformity Locking) by showing that *pressuring a non-deterministic system for determinism* (e.g., via formalized selection rules) locks organizations into a particular sampling strategy or model variant, creating path dependency and audit burden.

What it *doesn't* yet open: the boundary between "non-determinism that triggers formalization" and "non-determinism that remains absorbed as operational variance." A protocol system handles some randomness without escalating coordination cost (e.g., load balancing, cache misses). When does LLM variance cross into the protocol-critical zone? That's the sharpening question worth tracking.

## Research connections

- **L-006:** Coordination cost is conserved; non-deterministic knowledge sources do not reduce total coordination work, only redistribute it from query layer to governance and audit layers.
- **seed-129:** Formalization of selection procedures (model variant, prompt strategy, output ranking) creates conformity locks that persist and calcify into organizational standard operating procedure.
- **L-003 (The Formalization Ratchet):** Non-determinism in a knowledge source creates stress on informal coordination; organizations respond by formalizing proxy decision procedures (e.g., "always use model X with prompt template Y").
- **seed-142 (Auditability-Legibility Trap):** Making LLM output selection legible and auditable (e.g., "model A was chosen because it scored highest on metric Z") may lock in suboptimal selection criteria.

## Seed

**Seed title:** Non-Deterministic Knowledge Source Formalization Cascade  
**Seed type:** observation  
**Seed text:** When a protocol system depends on a knowledge source that produces materially different but valid outputs for identical queries (due to stochasticity, versioning, or configuration), the system cannot remain neutral on which output to use; it must escalate to a formalizable selection rule (model ranking, prompt strategy, output validation metric). This formalization itself becomes a protocol boundary — organizations optimize toward the legible selection criterion rather than toward the underlying goal. The non-determinism does not disappear; it migrates from "which answer" to "which selection rule" and "why was this rule chosen." This may generalize beyond AI: any protocol that depends on a non-deterministic information source must formalize downstream to remain operationally coordinated, and that formalization becomes a new site of capture and path-locking.
