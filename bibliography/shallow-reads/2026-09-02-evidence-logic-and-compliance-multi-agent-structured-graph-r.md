# Evidence, Logic, and Compliance: Multi-Agent Structured Graph Reasoning with Expert Arbitration for Medical Referral

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.30938
**Date read:** 2026-09-02
**Connected to:** L-012, seed-049
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A multi-agent system paper addressing medical referral decisions by decomposing the task into structured graph reasoning with expert arbitration. The work attempts to solve information overload and unstructured collaboration in LLM-based medical triage by formalizing evidence into legible decision substrates and distributing reasoning across specialized agents.

## What I took from it

The paper is a competent engineering response to a real problem — LLMs fail at medical referral when evidence is multimodal and subtle signals matter. The solution architecture is precisely what L-012 predicts: by formalizing the decision space into "structured graph reasoning" with legible evidence layers, the optimization pressure shifts away from holistic clinical judgment and into the formalization layer itself. The evidence that matters becomes the evidence that is *structurable* into the graph; urgency indicators that resist graphification become systematically invisible. This is not a bug the system solves — it is the mechanism by which the system trades complexity for legibility.

However, the paper does not examine this trade-off or its consequences. It treats formalization as neutral infrastructure. The work does not investigate whether graph-legible evidence is the *same* as clinically adequate evidence, nor does it track what gets lost in structuration. It is therefore a case study in L-012 instantiation rather than a theoretical or empirical investigation of the mechanism itself.

## Research connections

- **L-012 [Intervention-Layer Displacement]:** The formalization of referral evidence into structured graphs displaces optimization pressure from the clinical judgment layer to the evidence-encoding layer; what becomes optimizable is graph-legibility, not patient outcome.
- **seed-049 [referenced in triage]:** Externalization of decision locus to formalized representation; clinical judgment becomes a function of what can be rendered legible to the reasoning system.
- **seed-062 [Formalization Opacity Collapse]:** Structured graph encoding flattens multimodal clinical evidence into machine-legible nodes; subtle non-graph-encodable urgency signals collapse into noise.
- **L-004 [Metric Capture]:** Graph-structured evidence becomes the proxy for "adequate clinical information"; optimization on this proxy under deployment pressure will systematize the erasure of non-graphifiable signals.

## Seed

**Seed title:** Evidence Legibility Ratchet in Formalized Medical Protocols

**Seed type:** observation

**Seed text:** When clinical or safety-critical decision protocols are externalized into formally structured representations (graphs, databases, decision trees), the set of clinically relevant information compresses to the set that is structurable into that representation. Under deployment pressure, optimization of the formalized layer (accuracy of graph encoding, completeness of evidence nodes) becomes decoupled from optimization of the actual outcome (correct referral, patient safety). Protocols that solve the formalization problem may worsen the clinical outcome problem if the formalization is lossy with respect to the decision-critical features that resist legibility. This suggests a general law: formalization in safety-critical domains creates a permanent asymmetry between legible and non-legible evidence, and systems optimized on legibility will systematically degrade handling of non-legible but outcome-critical signals.
