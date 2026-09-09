# BoilerSketch: A TA-Supervised, Diagram-First GenAI Practice for Structured Diagrams in CS1/Early CS2

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.00844
**Date read:** 2026-09-02
**Connected to:** L-003, seed-029
**Kind:** meta
**Escalation:** store-only

## What this is

A practice paper describing a GenAI interface design for educational support (CS1/CS2) that privileges diagram-first generation over text, mediated through TA supervision. The work addresses a pedagogical bottleneck—student questions that demand visual explanation—by constraining the protocol layer (GenAI output format) to a structured, verifiable modality.

## What I took from it

The paper instantiates a real-world case of **L-003 (Formalization Ratchet)** in microcosm: stress on support capacity (scaling pressure) drives adoption of a *formalized* substitution (GenAI interface with structural constraints) over informal coordination (ad-hoc TA diagrams). The TA-supervised layer is not accidental; it is the enforcement boundary that preserves pedagogical validity under automation.

This also illuminates **seed-029** (the triage note is correct): the interface *shape* (diagram-first, not text-first) functionally selects which coordination norms are legible and reproducible. The protocol does not merely assist existing practice—it reshapes what "correct explanation" looks like by making certain forms computable and verifiable. This is a low-stakes but clear instance of how formalization pressure selects protocol architectures that survive at scale.

The meta-layer observation: TA supervision is not optional oversight; it is load-bearing governance infrastructure. Removing it would cause the system to collapse into text-forward unreliability. The protocol *requires* the human layer.

## Research connections

- **L-003:** Formalization under scaling pressure (support bottleneck) drives adoption of structured, verifiable protocol (diagram-first GenAI) over informal exemplar coordination (ad-hoc TA drawings).
- **seed-029:** Protocol interface design (diagram-first vs. text-first) functionally determines which coordination norms become legible, verifiable, and reproducible.
- **seed-070:** TA supervision functions as obligate coordination infrastructure—the protocol cannot operate without it; it is an irreducible governance residual.

## Method note

This paper demonstrates the value of studying protocol design *in the wild* at educational/organizational scales where intervention is feasible and observability is high. The TA-supervised layer is particularly instructive: it reveals that automation does not eliminate human coordination; it displaces and formalizes it. Research on protocolized systems should attend closely to cases where human roles *stabilize* under formal system adoption, as these often mark the discovery of genuine irreducible coordination costs. Such cases are evidence factories for L-006 (Coordination Cost Conservation).
