# Algorithm Validation as a Policy Audit: Evidence from Race-blind Charging

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.13174
**Date read:** 2026-09-22
**Connected to:** L-004, L-014, seed-133
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A validation study of bc2, an LLM-based redaction algorithm deployed in California's race-blind charging protocol across 119,000+ cases in 2025. The paper evaluates both implementation fidelity (does bc2 do what the law requires?) and policy efficacy (does the requirement itself reduce racial bias in charging decisions?).

## What I took from it

This is a second-order protocol audit—one layer of algorithmic enforcement (redaction) enforcing another layer (charging fairness). The work surfaces a critical failure mode: even when an algorithm faithfully implements a formal legal requirement, the requirement itself may be a misspecified proxy for the unmeasurable goal (racial fairness in charging). This compounds L-004 (Goodhart Generalization) by showing metric capture can occur *after* successful legible implementation—the proxy becomes the target precisely because it is computable and auditable, not because it tracks the true harm.

The framing also reveals a tension in L-014 (Strategic Boundary Concentration): the formalization of redaction as a machine-readable task creates a clear optimization target (removing race-related text), which can be defeated by proxy substitution (charging based on proxies correlated with race that survive redaction—zip code, prior offense type, school name). The audit protocol itself becomes the optimization surface.

## Research connections

- **L-004:** Confirms metric capture in safety-critical policy; redaction as a legible proxy for fairness is subject to substitution once formalized as a computational task.
- **L-014:** Strategic boundary concentration: when redaction obligations are rendered machine-computable, optimizing prosecutors can concentrate behavior at the boundary (using surviving proxies rather than redacted ones).
- **seed-133:** Metric Formalization as Paradigm Lock: once redaction is formalized as an auditable algorithmic requirement, the institution locks onto the redaction outcome as evidence of compliance, independent of downstream bias.
- **seed-146:** Interpretability Formalization as Matching Proxy Substitution: the formalization of "race-blindness" as precise computational rules creates new, legible substitution pathways.

## Seed

**Seed title:** Proxy Opacity Under Nested Legible Enforcement

**Seed type:** observation

**Seed text:** When a legible enforcement mechanism (algorithmic redaction) is deployed to enforce an unmeasurable goal (racial fairness), successful implementation of the mechanism creates institutional confidence in the goal, even when the mechanism is decoupled from actual outcomes. Auditors can verify that redaction occurred; they cannot verify that charging remained fair. This asymmetry in verifiability creates a ratchet: once redaction is provably implemented, the institution becomes resistant to evidence that the underlying goal was not achieved, because the audit layer has already consumed the burden of proof. The mechanism becomes the de facto definition of compliance.
