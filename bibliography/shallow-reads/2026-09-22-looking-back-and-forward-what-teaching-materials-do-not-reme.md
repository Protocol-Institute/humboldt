# Looking Back and Forward: What Teaching Materials Do Not Remember About Instructional Reasoning

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.19488
**Date read:** 2026-09-22
**Connected to:** L-003, seed-131
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A design-oriented paper proposing "Teaching Memory" as a framework to preserve instructional reasoning (intentions, context, reflective insights) alongside instructional artifacts in educational systems. The work diagnoses a gap in Learning Management Systems: they store what is taught, not why or how it was reasoned about, and this reasoning evaporates when materials pass to new instructors.

## What I took from it

This is a precise case study in **seed-131** (Context Legibility as Failure Attribution Boundary): when instructional artifacts become formally stored and transferable (legible), the contextual reasoning that made them coherent becomes invisible, making it impossible for downstream users to distinguish between *intended design choices* and *historical accident*. New instructors inherit rules without rationales, creating a failure mode where protocol drift appears as incomprehensible variation rather than adaptive response.

The paper also touches on **L-003** (Formalization Ratchet): as teaching moves from informal apprenticeship to codified materials, there is pressure to formalize—but formalization strips context. The framework proposed here attempts to resist that ratchet by treating reasoning as a first-class artifact. However, the paper does not investigate whether Teaching Memory itself becomes subject to the same ossification: does preserved reasoning eventually calcify into dogma?

## Research connections

- **L-003:** Formalization of teaching materials creates a ratchet where informal reasoning (adaptive, contextual, reflective) is replaced by formal artifacts; Teaching Memory attempts to preserve reasoning but does not investigate whether this creates a new ossification layer.
- **seed-131:** Legibility of artifacts without legibility of context creates a boundary where failures cannot be correctly attributed—new instructors cannot distinguish between robust design and contingent circumstance.

## Method note

This paper exemplifies a critical methodological gap in protocol research: we study what systems *do* and what *rules* they follow, but rarely preserve the *reasoning about constraints and tradeoffs* that made those rules sensible in a specific context. As protocolized systems become more distributed and automated, the loss of instructional reasoning (why this signal? why this threshold? what was the failure case we were protecting against?) becomes a systematic vulnerability. Future research on governance, safety-critical protocols, and coordination systems should include institutional memory methods as a primary design concern, not a documentation afterthought.
