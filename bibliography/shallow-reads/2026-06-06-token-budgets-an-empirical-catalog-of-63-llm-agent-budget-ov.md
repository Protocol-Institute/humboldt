# Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.04056
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary empirical source that identifies a genuine failure class in protocolized agent systems (budget aliasing/enforcement gaps) and proposes a type-theoretic mitigation absent from current inventory; the pattern generalizes across 21 frameworks and suggests a foundational design principle for resource-aware artificial systems.

## What this is

An empirical catalog of 63 production budget-overrun failures across LLM-agent orchestration frameworks (2023–2026), paired with a case study of affine-type enforcement in Rust as a structural solution. The work argues that ad-hoc wrapper-based budget control fails to prevent double-spend and use-after-delegation pathologies because budget tokens lack type-system visibility and linear-resource semantics.

## What I took from it

This directly addresses a critical gap in protocolized artificial systems: the enforcement of *integrity properties on resource consumption itself*. Most agent frameworks treat budgets as runtime parameters rather than values with semantic constraints (no aliasing, no re-use, no delegation without consumption). The empirical catalog establishes budget overrun as a *systematic failure class*, not a user-error edge case — suggesting that artificial systems operating under resource constraints require formal accounting, not informal monitoring.

The affine-type solution is significant because it embeds budget accountability into the *language semantics* of agent orchestration, making violations uncompilable rather than catchable-at-runtime. This aligns with a broader principle: that protocols governing artificial systems must be enforced at the syntax/type level, not bolted on as runtime checks. The generalization across 21 frameworks suggests this is not a framework-specific bug but a *category error* in how agent budgets are modeled.

## Research connections

- **None yet established** — this is a new domain entry.

## Candidate laws or signals

- **CL-Token-Budget-1:** *Resource-bearing values in protocolized agent systems must be typed as linear/affine resources to prevent aliasing, double-spend, and delegation pathologies; ad-hoc runtime accounting is insufficient and produces systematic failure classes.*

- **CL-Token-Budget-2:** *Budget-overrun failures cluster across heterogeneous frameworks at >3 incidents/framework-year, suggesting the failure mode is architectural rather than implementation-specific.*
