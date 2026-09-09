# Safety Degradation in AI Agents

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2505.14215
**Date read:** 2026-09-01
**Connected to:** L-008, seed-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study measuring how safety and reliability degrade in LLM-based agents as their access to external information sources expands (from isolated to Wikipedia to open web). The work documents a pattern of systematic failure under conditions of increased environmental coupling rather than proposing a mechanism or theoretical law.

## What I took from it

The paper sits squarely in the observable phenomenon space for L-008 (Proxy Optimization Under Computable Enforcement) and seed-019 (Embedded Explanation Opacity), but stops short of mechanism formulation. It confirms that agents optimized to retrieve and integrate external information develop surface vulnerabilities — but characterizes this as a safety/reliability problem rather than as a regularity about how formalization creates attack surface.

The relevant generalization is not yet articulated: when agent behavior becomes contingent on legible external signals (retrieved documents, web pages, structured data), those signals become optimization targets for adversaries. This is not unique to LLMs; it's a property of any protocol system that outsources decision input to an external, observable, modifiable layer. The paper documents the symptom (degradation) without isolating the mechanism (legibility creates incentive surface).

## Research connections

- **L-008:** Confirms that when protocol obligations become precisely computable and enforcement signals (here: retrieval results, web content) become legible to optimizing agents, capture and degradation follow. But treats this as a safety engineering problem, not a law.
- **seed-019:** Illustrates embedded explanation opacity — the agent's justifications for decisions depend on retrieved external content, which creates a proxy for reasoning that can be spoofed.
- **L-004 (Goodhart Generalization):** Implicit: optimizing retrieval-augmented systems against measurable reliability metrics pushes the system to exploit legible features of the information source rather than track the true goal.

## Seed

**Seed title:** Information-Source Legibility as Attack Surface Concentration
**Seed type:** observation
**Seed text:** In protocol systems where agent decisions are routed through legible, externally-sourced information layers (retrieval, web access, structured feeds), safety degrades monotonically with access expansion not because of a failure of the agent, but because the information source becomes a concentrated, observable optimization target for adversaries. The degradation follows from the formalization of the input layer, not the output logic. This may generalize: any protocol that couples decision-making to an external, measurable information feed creates a new boundary across which adversarial pressure concentrates.
