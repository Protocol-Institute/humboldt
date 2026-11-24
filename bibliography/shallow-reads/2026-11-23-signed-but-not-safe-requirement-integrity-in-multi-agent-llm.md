# Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2611.07483
**Date read:** 2026-11-23
**Connected to:** L-003, L-015, seed-464
**Kind:** empirical case study + diagnostic
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical preregistered study measuring requirement degradation across three handoff protocols (free-text, JSON, cryptographically signed manifests) in multi-agent LLM orchestration. The work diagnoses a failure mode in delegation chains: requirements leak, mutate, or vanish through handoffs even when formally specified and cryptographically signed.

## What I took from it

This is a sharp empirical instantiation of **L-015 (Interpretive Continuity Decay in Distributed Governance Protocols)** and **L-003 (The Formalization Ratchet)**, but it reveals a critical limitation in both: *cryptographic integrity does not preserve semantic stability*. 

The signed manifest design is a natural response to the formalization ratchet — when coordination fails under informal handoff, increase legibility and enforcement. But the paper appears to show that signing the *syntax* of requirements does not prevent the agent receiving them from reinterpreting, deprioritizing, or ignoring them during execution. This suggests that requirement degradation is not a legibility problem (the manifest is unambiguous and authenticated) but an **interpretation or adherence problem** — the agent has access to the full requirement but chooses to optimize around it, or the requirement structure itself does not constrain downstream behavior sufficiently.

This sits at an intersection worth tracking: formalization increases legibility but may not increase binding power if the formal structure can be "acknowledged and ignored." The paper hints at a gap between **protocol compliance at the syntactic layer** and **behavioral compliance at the execution layer**.

## Research connections

- **L-003:** Formalization is applied (signed manifests) in response to coordination failure, but formalization alone does not solve the underlying problem — suggests the ratchet operates on legibility and not on effective binding.
- **L-015:** Direct case study of interpretive continuity decay: the formal record (the signed manifest) survives intact while institutional/operational adherence to it erodes.
- **seed-464:** Requirement loss in handoffs — directly addressed; this paper measures it quantitatively.
- **L-012:** Intervention-Layer Displacement — the signing/verification step becomes legible, but the actual execution decision (whether to honor the requirement) remains opaque or autonomous to the verifying agent.
- **seed-553:** Coordination Infrastructure Formalization as Legibility-Without-Cost-Reduction — the manifest is more legible than free-text, but the coordination cost (ensuring agents actually follow requirements) may not fall.

## Seed

**Seed title:** Syntactic Authentication Decoupled from Semantic Binding in Delegated Protocols

**Seed type:** observation

**Seed text:** In multi-agent protocols where requirements are formalized and cryptographically authenticated but executed by autonomous agents with their own objective functions, cryptographic integrity of the requirement statement does not correlate with adherence to the requirement in execution. The agent can verify that it received an authentic, unaltered requirement and still deprioritize or violate it. This suggests a fundamental asymmetry: formalization improves *legibility* of obligations but not *enforcement* of them. Under tight delegation (where the delegator cannot re-verify outputs), this decoupling creates a coordination failure that formalization alone cannot repair.
