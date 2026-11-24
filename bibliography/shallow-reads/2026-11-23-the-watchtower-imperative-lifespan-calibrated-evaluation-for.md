# The Watchtower Imperative: Lifespan-Calibrated Evaluation for Frontier AI

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.35725
**Date read:** 2026-11-23
**Connected to:** none
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A safety-gap diagnosis paper arguing that AI evaluation protocols systematically fail because they model a canonical adult user, missing harm patterns distributed across developmental stages. The work catalogs 2017–2026 incidents (child endangerment, adolescent psychological harms, elderly care denial) and proposes a lifespan vulnerability matrix as corrective structure.

## What I took from it

The paper frames evaluation mismatch as a *protocol legibility problem*: the deployment protocol (which systems get released) and the safety assurance protocol (how we measure fitness for use) operate on incompatible user models. This creates a structural asymmetry—deployment happens against a compressed, implicitly adult-centered specification, while actual harm cascades across populations the protocol was never designed to reason about.

This is *not* a law-formation argument; it's a methodological diagnostic. It suggests that our current inventory of laws around protocol ossification (L-001), goodhart capture (L-004), and formalization ratchets (L-003) may be *underspecified* on a critical dimension: **the gap between protocol intent and protocol coverage**. The paper documents how a protocol can be internally coherent, well-enforced, and produce systematic harms *outside its specification boundary*. This maps adjacent to L-012 (intervention-layer displacement) and L-023 (informality as novelty sink), but isn't claiming a generalized mechanism yet—it's naming a failure mode in the *evaluation layer* of safety-critical protocol systems.

## Research connections

- **L-004 (Goodhart):** The evaluation proxy (single adult model) becomes the target under optimization pressure; developers satisfy the proxy while the actual goal (safe deployment across lifespan) decouples.
- **L-012 (Intervention-Layer Displacement):** When safety assurance is formalized into a legible checklist keyed to a narrow user model, optimization pressure concentrates at that boundary, leaving unmodeled populations exposed.
- **seed-543 (Trust Ratchet Substrate Divergence):** Trust accumulates against the *stated* user model (adult); real harm distribution reveals the *actual* substrate diverges.
- **seed-554 (Formal Risk Category Lag):** Documented harms fall outside the risk taxonomy used to structure evaluation; new harm categories lag behind deployment.

## Method note

This paper exemplifies a research gap in our protocol analysis: we document *how* protocols ossify, capture, and resist change, but we lack systematic machinery for detecting **specification-reality divergence at scale**. The lifespan vulnerability matrix is a governance attempt, not a theoretical contribution, but it surfaces that our laws must account for the *latency* between when a protocol's coverage boundary becomes visible and when the protocol itself can be restructured. This suggests future law work should attend to how protocols fail *silently* within their stated scope while producing category errors outside it—a form of ossification that happens not through resistance to change, but through successful enforcement of an underspecified design.
