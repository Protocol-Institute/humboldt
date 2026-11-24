# Governed Sovereign RAG for Public Administration: Tripartite Epistemic Routing, Facet-Guided Clarification, and Deterministic Numeric Verification in Citizen Services

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.36561
**Date read:** 2026-11-23
**Connected to:** L-003, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A deployed case study of a retrieval-augmented generation system for public administration (Tlaxcala, Mexico) designed to govern conversational AI output through formal rule enforcement, deterministic verification, and architectural constraints. The system prioritizes regulatory certainty and data sovereignty over generality, using tripartite epistemic routing to prevent hallucinated fees and out-of-jurisdiction advice.

## What I took from it

This is a systems integration paper, not a theoretical or empirical investigation of protocol dynamics. It demonstrates instantiation of L-003 (Formalization Ratchet) and L-014 (Strategic Boundary Concentration Under Computable Legality) *as design strategy* — the paper shows how formalization is *deployed as a remedy* for coordination failure in citizen-facing services, but does not investigate the costs, rigidities, or long-term equilibria that formalization introduces.

The core move is converting underspecified procedural knowledge into computable verification rules: numeric fees are deterministically checked against official tables; jurisdiction is encoded as a faceted query router; response generation is constrained by retrieval over curated procedure documents. This is governance-by-formalization, not governance-of-formalization. The paper does not examine whether this boundary concentration (pushing optimization pressure to the margins of the system) displaces gaming to new surfaces, creates credential stranding, or accumulates interpretive debt as the actual procedures drift from their formal encoding.

## Research connections

- **L-003:** The paper *exemplifies* the Formalization Ratchet as a response to scaling pressure and query underspecification, but does not measure the cost of this transition or test whether informal coordination norms were displaced or simply moved offline.
- **L-014:** Direct instantiation: legal/procedural obligations are rendered precisely computable (fee tables, jurisdiction rules, procedure eligibility), and the system's design assumes this legibility solves the coordination problem. No investigation of where optimization pressure concentrates at system boundaries.
- **seed-554:** The system formalizes risk categories (hallucination, jurisdiction error, fee fabrication) in response to operational capability (LLM deployment), but does not examine whether the formal risk model lags actual failure modes that emerge under citizen-adversary interaction.

## Seed

**Seed title:** Formalization as Coordination Displacement, Not Resolution

**Seed type:** observation

**Seed text:** When a protocol system (here: citizen-government service coordination) faces high rates of uncoordinated or adversarial output under scaling, formalization is deployed as a containment strategy by rendering key decision surfaces computable and rule-bound. The paper shows the technical success of this strategy within its design boundaries (zero hallucinated fees, deterministic routing). However, it does not investigate whether formalization *resolves* the underlying coordination failure or *displaces* it: citizens may shift from query ambiguity to strategic boundary-probing; procedure owners may face pressure to encode procedural knowledge that was previously tacit and negotiable; the system may accumulate interpretive debt as real procedures diverge from their formal model. This suggests formalization in governance protocols may exhibit the same conservation principle as L-006 (coordination cost is conserved, not eliminated, across layer transitions).
