# AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.28617
**Date read:** 2026-09-02
**Connected to:** L-004, seed-021
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A policy/governance paper proposing an audit framework (AISPA) for surfacing and evaluating system prompts in deployed LLM applications. The work frames system prompts as opaque governance artifacts and proposes user-centric auditing as a remedy for the "trust and accountability gap" created by their non-disclosure.

## What I took from it

This is a governance intervention proposal, not a source documenting dynamics of protocolized systems under stress. It documents a *symptom* — that system prompts function as frozen, non-auditable policy — but does not investigate the mechanisms that make them sticky, or why disclosure itself may not resolve the underlying coordination problem.

The framing does reinforce the empirical reality that critical control parameters in AI systems are deliberately legible only to developers and opaque to users and regulators. This aligns with seed-021 (audit opacity as metric capture governance gap) and L-004 (Goodhart Generalization), but the paper itself proposes a transparency solution rather than investigating what prevents transparency from working as a control mechanism. It does not examine whether auditable prompts would be *modifiable* under adoption pressure, or whether disclosure creates new gaming surfaces (L-001, L-005 adjacent).

The work is upstream of the mechanisms we track: it identifies a structural gap but operates at the policy design level, not at the level of how protocolized systems actually respond to audit, formalization, or disclosure pressure.

## Research connections

- **L-004:** System prompts as measurable proxies for unmeasurable developer intent; audit framework assumes transparency solves capture, but does not test whether legibility redirects rather than resolves optimization pressure.
- **seed-021:** Directly addresses audit opacity, but proposes a solution rather than mapping the mechanism of why opacity persists despite deployment-scale pressure.
- **L-012 (adjacent):** Formalization of prompt governance as legible input could displace optimization locus to prompt design itself rather than actual system behavior.

## Method note

This paper exemplifies a common meta-pattern: governance research identifies a legibility gap and proposes procedural fixes without modeling whether the gap persists *because* disclosure is costlier or riskier than opacity. Research on protocolized systems should systematically distinguish between "gap caused by neglect" and "gap maintained as equilibrium." Audit frameworks are valuable but should be paired with game-theoretic or operational analysis of what happens when governance surfaces are made legible under competitive or adversarial conditions. The framework would be stronger paired with empirical work on whether audited prompts remain stable under subsequent user pressure, or whether disclosure itself becomes a new optimization surface.
