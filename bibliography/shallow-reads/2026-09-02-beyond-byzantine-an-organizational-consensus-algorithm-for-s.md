# Beyond Byzantine: An Organizational Consensus Algorithm for Self-Interested Agents Under Information Asymmetry

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.28957
**Date read:** 2026-09-02
**Connected to:** L-003, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design paper proposing OCA, a consensus protocol for multi-agent organizational settings where agents are boundedly rational and self-interested rather than Byzantine-classified. The work models departmental decision-coordination as an incomplete-information game and aims to construct incentive-compatible equilibria under asymmetric beliefs.

## What I took from it

The paper identifies a real gap: Byzantine consensus assumes binary honesty/malice, but organizational agents inhabit a messier middle ground. OCA attempts to formalize bounded rationality and preference heterogeneity as *legible constraint classes* rather than adversarial models. This is a direct operationalization of L-003 (Formalization Ratchet) — informal departmental norms (trust, contextual forbearance, tacit hierarchy) are being replaced by computable preference functions and incentive structures. 

The mechanism design framing also engages L-006 (Coordination Cost Conservation): by making preferences explicit and verifiable, the protocol may reduce *hidden* coordination friction but likely displaces it into information revelation costs, mechanism design complexity, and the overhead of maintaining bounded-rationality models. The paper does not appear to track this trade-off empirically or theoretically.

## Research connections

- **L-003:** Direct instance — informal norms replaced by formalized preference models under scaling/coordination pressure.
- **L-006:** Potential mechanism — coordination cost may be conserved across the shift from trust-based to incentive-based coordination; no evidence presented either way.
- **seed-070:** The protocol formalizes inter-departmental coordination as a legible constraint infrastructure; this may become an obligate dependency.
- **seed-077:** If OCA uses measurable proxies for departmental preference (e.g., revealed preference, stated utility), those proxies may undergo preference ratcheting under repeated interaction.
- **L-008:** Boundary case — if OCA enforcement signals become precisely computable, optimization pressure may migrate to preference model specification itself.

## Seed

**Seed title:** Preference Formalism as Coordination Substrate Lock

**Seed type:** motif

**Seed text:** When organizational consensus protocols replace informal norms with explicit preference models and incentive compatibility constraints, the system becomes dependent on the stability of *preference legibility itself* — the ability to specify, communicate, and enforce what agents want. Over time, agents optimize for *being well-modeled* rather than for the original informal goals. The protocol locks into the preference ontology used at formalization time, making subsequent norm drift invisible to the mechanism. This may generalize beyond mechanism design: any system that formalizes motivation as a legible input to coordination machinery becomes hostage to the accuracy and completeness of that model.
