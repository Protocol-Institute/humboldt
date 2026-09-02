# Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.22611
**Date read:** 2026-09-02
**Connected to:** L-002, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems architecture paper proposing a decentralized multi-layered access control framework for stochastic AI agents in critical infrastructure. The work treats RBAC determinism-mismatch as a design problem and offers technical solutions rather than theorizing the underlying protocol dynamics.

## What I took from it

The paper correctly identifies a genuine friction: traditional role-based access control assumes deterministic, auditable action sequences, while agentic systems produce stochastic outputs that make boundary enforcement noisy and attribution hard. This confirms the presence of a **legibility-enforcement gap** when optimization agents operate under computable obligation models.

However, the paper remains domain-specific and solution-focused. It does not develop a sustained argument about why this gap arises, under what conditions it becomes catastrophic, or how it generalizes beyond AI agent access control. The "multi-layered" framework appears to be pragmatic layering (monitoring + sandboxing + revocation) rather than an investigation of how protocol obligations deform under stochastic pressure. No mechanism for how agents exploit or circumvent the control surface is developed; no cross-domain pattern is generalized.

## Research connections

- **L-014:** Strategic Boundary Concentration Under Computable Legality — The paper identifies that precise, machine-readable access rules become optimization targets, but does not investigate whether agents preferentially concentrate exploitation at formally-defined boundaries rather than at informal governance layers.

- **L-002:** Hardness Asymmetry — Implicit: verification of *whether an agent should act* is cheaper than prediction of *what a stochastic agent will actually do*, creating asymmetric enforcement cost. Not developed.

- **seed-063:** Latent-State Coupling as Silent Protocol Violation — The gap between an agent's decision model (opaque) and its observable action (legible) creates room for undetectable protocol drift. Not explored.

## Seed

**Seed title:** Stochastic Evasion of Deterministic Boundaries

**Seed type:** observation

**Seed text:** Access control protocols designed around deterministic action models face systematic enforcement degradation when applied to stochastic agents whose internal state and decision process are opaque but whose actions are legible and attributable. The mismatch is not purely technical but structural: boundary rules become increasingly fine-grained in response, but fine-grained rules applied to stochastic systems either reduce agent autonomy to near-determinism (defeating the purpose of agentic deployment) or maintain autonomy while accepting uncontrollable false-positive and false-negative error rates at the boundary. This tension may generalize to any protocol system where the observed behavior is computable but the generating process is not.
