# An Empirical Study of Coordination Mode as the First-Class Citizen in From-Scratch Multi-Agent Coding

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.27877
**Date read:** 2026-09-02
**Connected to:** L-003, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper (MSEval) for evaluating multi-agent LLM coding systems on real-world tasks, introducing hierarchical rubrics and deterministic evaluation. The framing emphasizes coordination mode as a design variable, but the work is primarily an empirical measurement tool rather than a theoretical or mechanistic argument about protocol behavior.

## What I took from it

The paper's premise—that coordination mode should be a first-class citizen in multi-agent system design—aligns with L-003 (formalization under stress) and L-006 (coordination cost conservation), but the execution treats coordination as an engineering knob rather than investigating the *laws governing how coordination formalizes under pressure*. The work documents that real-world multi-agent coding requires explicit coordination protocols and that informal communication often fails under time/monetary cost constraints—a practical confirmation of the formalization ratchet. However, the paper does not examine *what happens* when informal coordination is replaced with formal protocol, whether coordination costs are merely displaced rather than reduced, or whether the choice of coordination mode itself undergoes ossification once adopted at scale. It measures performance against deterministic rubrics, which is relevant to L-004 (metric capture), but does not investigate whether the rubrics themselves become optimization targets that distort the underlying coordination structure.

## Research connections

- **L-003:** Confirms that multi-agent systems under time/cost pressure shift from informal to formalized coordination; does not mechanistically explain the shift or its consequences.
- **L-006:** Suggests coordination costs are real and measurable in code synthesis; does not test whether formalizing coordination merely relocates rather than reduces cost.
- **L-004 (Goodhart):** Uses deterministic rubrics as success proxies; does not examine whether optimizing toward rubrics decouples from actual multi-agent coordination quality.
- **seed-071 (Expressiveness Floor):** The hierarchical rubric design may instantiate an expressiveness boundary in what coordination modes can be evaluated; worth noting if the framework systematically excludes certain coordination patterns.

## Seed

**Seed title:** none

---

**Justification for store-only:** This is a tool/benchmark paper in the measurement space, not a primary theoretical or empirical argument about coordination law. It documents phenomena consistent with L-003 and L-006 but does not advance mechanism or generalize beyond the domain of LLM-based multi-agent code synthesis. No novel regularity, mechanism, or sharp question emerges that warrants tracking as a law fragment.
