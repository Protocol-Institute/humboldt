# KumbhDoot: A Scale-Ready, LLM-Bounded Architecture for Mass-Gathering Public-Service Assistants

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.07520
**Date read:** 2026-09-02
**Connected to:** L-003, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper describing an agentic architecture for managing information provision at mass gatherings (Kumbh Mela) by bounding LLM use through tiered routing, local knowledge bases, and fallback protocols. The work is primarily engineering-focused: designing a tool that trades broad capability for reliability, cost efficiency, and graceful degradation under constraint.

## What I took from it

The paper documents a concrete case of L-003 (Formalization Ratchet): informal coordination norms around information-seeking at mass gatherings are being replaced by a formal, computationally legible protocol with explicit routing rules, factuality gates, and offline-capable knowledge substrates. This formalization occurs precisely under the stress conditions the law predicts—scale, heterogeneity, and safety criticality.

It also illustrates L-006 (Coordination Cost Conservation) in miniature: the paper explicitly *moves* coordination cost (fact-checking, routing, fallback logic) from runtime LLM inference to offline knowledge architecture. The total coordination problem does not shrink; its location shifts. However, the paper does not investigate whether this displacement creates new costs elsewhere in the system (e.g., knowledge maintenance, version drift, missed edge cases), which would be the deeper test of the conservation hypothesis.

The work is competent systems design but does not develop a novel mechanism or challenge existing theory. It is a domain application of established principles (tiered degradation, local caching, bounded inference).

## Research connections

- **L-003:** Formalization ratchet exemplified: informal "ask someone" norms → formal routing protocol under mass-gathering stress.
- **L-006:** Coordination cost conservation in action: inference cost → knowledge maintenance cost; the total burden shifts layer but may not reduce.
- **seed-062 (Formalization Opacity Collapse):** The paper does not investigate whether formalization of the routing logic itself becomes opaque as the knowledge base scales—a live question.

## Seed

**Seed title:** none
