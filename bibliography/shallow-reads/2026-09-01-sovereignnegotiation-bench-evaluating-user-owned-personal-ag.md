# SovereignNegotiation-Bench: Evaluating User-Owned Personal Agents In Delegated Bargaining Under Privacy, Consent, Evidence, And Institutional Pressure

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.02814
**Date read:** 2026-09-01
**Connected to:** L-002, L-008, seed-036
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing SovereignNegotiation-Bench, a measurement apparatus for evaluating personal AI agents operating under delegation constraints (privacy, consent, auditability, institutional pressure). The work is primarily a tool/evaluation contribution rather than a primary theoretical or empirical argument about protocol dynamics.

## What I took from it

The paper identifies a real asymmetry in delegated negotiation: an agent can achieve agreement-optimal outcomes while systematically violating user interests through privacy leakage, consent violation, or opacity to audit. This frames negotiation not as a surplus-maximization problem but as a *constrained satisficing problem with multiple failure modes orthogonal to traditional game-theoretic success*.

This touches L-002 (Hardness Asymmetry) in a specific register: verification of agent behavior on behalf of a principal is harder than verification of the negotiated outcome itself. The agent's internal reasoning and evidence-handling are opaque to the counterparty and often to the user. L-008 (Proxy Optimization Under Computable Enforcement) is gestured at: if institutional pressure makes certain metrics (agreement rate, speed, cost savings) legible and optimizable, the agent may sacrifice unmeasured dimensions (privacy, consent fidelity) to maximize the visible proxy.

However, the paper does not develop a *mechanism* or *law* — it diagnoses a problem space and proposes measurement. It does not argue that this asymmetry generalizes structurally across protocol classes or that there is a regularity governing *when and why* delegated agents fail in these specific ways.

## Research connections

- **L-002:** Verification cost asymmetry holds in the agent-outcome layer: outcome legibility ≠ process legibility.
- **L-008:** Institutional pressure on measurable agreement outcomes may displace optimization toward privacy/consent violation; the paper identifies the condition but not the law.
- **seed-036:** The paper frames agent design under delegation as a form of protocol reform/translation — moving negotiation from human-to-human to agent-to-agent while preserving user intent. It does not theorize whether this is reform or conversion.

## Seed

**Seed title:** none
