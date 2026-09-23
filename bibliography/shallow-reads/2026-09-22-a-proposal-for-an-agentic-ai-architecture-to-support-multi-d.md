# A Proposal for an Agentic AI Architecture to Support Multi-Domain Decision-Making in the Brazilian Armed Forces

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.20080
**Date read:** 2026-09-22
**Connected to:** L-012, seed-138
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A conceptual architecture proposal for integrating agentic AI into military command-and-control systems to accelerate decision cycles across multi-domain operational environments (land, aerospace, naval, cyber, electromagnetic). The work positions itself as a response to human cognitive bottleneck in OODA loops under data volume and velocity strain.

## What I took from it

The proposal describes a system design that formalizes prediction outputs as legible inputs to command-level decision protocols—precisely the condition that triggers L-012 (Intervention-Layer Displacement). The architecture appears to make operator intent, risk assessment, and course-of-action selection more computable and machine-readable. However, the paper appears to be **architectural/conceptual rather than empirical**: it proposes a system design without systematic testing of how optimization pressure migrates when predictions become this legible, or whether human operators retain meaningful causal authority once the "decision" input has been pre-shaped by agentic inference.

The framing also assumes that integrating heterogeneous domain data into a unified decision surface will *reduce* coordination cost and human cognitive load—a claim that sits in tension with L-006 (Coordination Cost Conservation) and L-003 (Formalization Ratchet). Centralizing legible decision inputs may reduce OODA cycle latency locally while displacing coordination burden elsewhere (inter-domain negotiation, exception handling, trust re-establishment when predictions fail).

## Research connections

- **L-012:** The proposal operationalizes exactly the condition: formal prediction becomes legible machine-readable input to protocol-governed decision layer. Whether optimization pressure shifts to prediction manipulation, decision-boundary gaming, or upstream domain data legibility is untested.
- **seed-138:** Intent legibility is positioned as *enabling* faster command decisions, but the proposal does not model how formalizing intent (as inputs to agentic reasoning) may displace the target from human strategic choice to protocol-conformant outputs.
- **L-003:** Multi-domain coordination norms are being replaced by formal legible protocols; no discussion of what informal slack is lost.
- **seed-145:** Enforcement legibility (machine-readable compliance with decision protocols) may become an escalation trigger in agentic hierarchies if agents learn to predict and pre-empt human override.

## Seed

**Seed title:** Prediction Legibility as Intent Boundary Collapse in Safety-Critical Multi-Agent Command

**Seed type:** motif

**Seed text:** In command-and-control protocols where AI systems formalize predictions as legible, machine-readable inputs to human decision layers, the locus of strategic choice may migrate from explicit operator intent to pre-decision shaping by inference systems. The operator appears to retain causal authority over the final command, but their decision space is now constrained by what predictions the system surfaces, how they are ranked, and what alternatives are suppressed as "irrational" by the agentic layer. This pattern may generalize beyond C2 to any multi-agent protocol where one agent's inference precedes another agent's formal choice: the second agent's "freedom" becomes bounded by the first agent's legibility choices, even absent explicit delegation or oversight failure.
