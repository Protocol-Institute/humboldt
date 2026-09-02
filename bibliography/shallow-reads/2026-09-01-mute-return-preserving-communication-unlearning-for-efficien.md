# MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.03473
**Date read:** 2026-09-01
**Connected to:** L-006, L-010, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A multi-agent reinforcement learning paper proposing a method ("MUTE") that optimizes communication in bandwidth-constrained cooperative games by filtering messages based on task return rather than information-theoretic metrics. The core claim is that high-informativeness and task-relevance are decoupled — a message can be maximally informative yet irrelevant to joint reward.

## What I took from it

The paper confirms a key friction in L-006 (Coordination Cost Conservation): when bandwidth becomes a hard constraint, the system does not eliminate coordination cost, it *displaces* it. Here, information-theoretic surrogates (mutual information, entropy reduction) are abandoned in favor of return-preserving filtering. This is not a solution to coordination cost; it is a *relocation* — computational overhead shifts from communication selection to return prediction and counterfactual evaluation.

The mechanism described aligns with **L-004 (Goodhart Generalization)**: optimizing for "informativeness" as a proxy for "useful coordination" produces messages that are high-signal in the statistical sense but functionally inert. The paper's intervention — switching the proxy to "return-relevant" — is pragmatically correct but does not resolve the underlying tension: in partially observable settings, what constitutes "return relevance" is itself only observable post-hoc, creating a moving target under online adaptation.

The work sits at the edges of **L-010 (Coordination Adoption Nonmonotonicity)** but does not substantively engage it. The sparse communication regime could produce adoption cascades or collapse, depending on whether agents can distinguish signal from filtered noise — the paper does not address this.

## Research connections

- **L-006:** Confirms coordination cost displacement rather than elimination; bandwidth constraint moves burden to return-prediction layer rather than removal.
- **L-004:** Documents Goodhart failure in communication sparsity (informativeness ≠ return relevance); proxy switching is pragmatic but does not resolve the decoupling.
- **L-010:** Touches the boundary (sparse signals + conditional adoption) but does not model nonmonotonic adoption dynamics.
- **seed-048:** Weak connection — paper optimizes *within* communication protocol, does not examine how capability and cooperation invert under bandwidth.

## Seed

**Seed title:** Proxy Decoupling Under Legibility Collapse
**Seed type:** observation
**Seed text:** In resource-constrained coordination systems, proxies that are optimal under full observability (information-theoretic metrics) become misaligned with task objectives as constraints tighten. Switching to a "truer" proxy (return-relevance) does not resolve the decoupling — it relocates the cost and creates a nested optimization problem (predicting what is return-relevant without full state visibility). Under progressive constraint tightening, the cost of maintaining proxy alignment may eventually exceed the cost of the constraint itself, creating a regime transition. This pattern likely generalizes beyond communication to any coordination layer where legibility decays faster than the underlying system dynamics.
