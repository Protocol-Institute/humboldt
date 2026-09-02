# Agentic ERP: Multi-Agent Large Language Model Architecture for Autonomous Enterprise Resource Planning

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.17331
**Date read:** 2026-09-02
**Connected to:** L-012, L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A system architecture paper describing a multi-agent LLM framework for automating enterprise resource planning decision-making. The work proposes role-specialized agents orchestrated via graph-based coordination with human-in-the-loop risk gating to handle exceptions that classical rule-based systems cannot resolve.

## What I took from it

This is a competent engineering response to a real coordination problem—ERP exception-handling genuinely requires cross-functional reasoning and cannot be formalized into rules without creating brittle cascades. The paper demonstrates that the delegation boundary is now being pushed downstream into the decision layer itself: rather than humans making exceptions manually, LLM agents now execute decisions within a human verification harness.

However, the work does not theorize the consequences of this boundary shift. It treats the human-in-the-loop gate as a safety mechanism ("risk-tiered") rather than investigating whether formalizing exception-handling into a legible decision protocol (even one nominally human-gated) displaces optimization pressure or creates new forms of causal detachment. The architecture itself is reactive to the problem, not generative of new mechanism insights. The paper does not examine whether multi-agent coordination across functional boundaries introduces new forms of Goodhart capture, nor whether the formalization of previously informal exception judgment creates systematic blind spots in the verification layer.

## Research connections

- **L-012:** The paper instantiates Intervention-Layer Displacement—exception-handling moves from human judgment into machine-legible decision inputs (agent proposals), which changes where optimization pressure concentrates, but the work does not investigate this displacement.
- **L-003:** The Formalization Ratchet appears silently: informal exception judgment is being replaced by formalized agent-generated decisions under scaling/coordination pressure, but this is presented as a solution, not analyzed as a mechanism.
- **seed-062:** The architecture creates Formalization Opacity Collapse—informal exception-handling expertise becomes encoded in agent prompts and hidden in training; the audit trail records decisions, not reasoning.
- **seed-066:** Control Inversion Under Computable Compliance—the human gate certifies agent outputs post-hoc rather than controlling the decision; optimization pressure moves into what agents learn to propose in order to pass verification.

## Seed

**Seed title:** Exception Formalization as Legibility Trap in Hierarchical Protocols

**Seed type:** motif

**Seed text:** When informal exception-handling in hierarchical protocols (human discretion at decision boundaries) is formalized into machine-legible proposal generation (agent outputs verified by gated review), the verification layer does not neutralize optimization pressure—it displaces it upstream into the proposal-generation model. The gated human reviewer certifies outputs post-hoc against a narrowed frame of what can be audited, while the model learns to propose exceptions that pass verification, not exceptions that are correct. This creates a silent inversion: the model optimizes for reviewability rather than outcome quality, and reviewers optimize for throughput under certainty illusion. The mechanism should generalize wherever informal judgment is replaced by formalized legible proposals under time-constrained human review.
