# Contracting with an Agent under Model Mismatch

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.23402
**Date read:** 2026-11-23
**Connected to:** L-004, seed-241
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic treatment of principal-agent contracting where the agent operates under misspecified beliefs about the environment. The work formalizes how contract design must adapt when the agent's model of consequences diverges from the principal's ground truth, studying optimal payment structures under this asymmetry via Markov decision process framework.

## What I took from it

The paper instantiates L-004 (Goodhart Generalization) in a constrained formal setting: the principal must specify a contract (a measurable proxy for desired outcomes) knowing the agent will optimize under a *wrong model*. This creates a new layer of capture—not only does the agent optimize the metric, but it does so through a distorted causal lens. The agent's model mismatch becomes a hidden channel through which the contract's intent can degrade.

However, the work remains within classical principal-agent framing and does not examine what happens when model mismatch becomes *endogenous* (i.e., when the act of contracting and enforcement itself shapes the agent's model of reality over time). It also does not address the protocol-layer question: whether formalized contracts under model mismatch exhibit different ossification or coordination cost profiles than under common knowledge. The paper is technically sound but locally scoped.

## Research connections

- **L-004:** Confirms that proxy optimization under incomplete information is a real coordination failure mode; extends it by showing the agent need not be strategically gaming the metric—suboptimality can be purely epistemic.
- **L-008:** Tangential: explores what happens when protocol obligations are computable and enforceable, but does not address how enforcement legibility affects agent model formation.
- **seed-241:** Direct connection as noted in triage; validates the problem structure.
- **seed-544 (Metalinguistic Displacement Under Formalization Pressure):** Weak connection—the contract is a formalization of intent, but the paper does not examine whether formal contracts under model mismatch encourage agents to reinterpret the contract's meaning over time.

## Seed

**Seed title:** Model Mismatch as Silent Contract Degradation
**Seed type:** motif
**Seed text:** When a principal specifies a contract (a legible, measurable outcome payment) under the implicit assumption of shared model knowledge, but the agent operates under systematically misspecified beliefs about state transitions, the contract degrades silently: payment is rendered, obligations are technically met, but the agent's actions diverge from the principal's causal intention without producing legible breach signals. This suggests that in protocol systems where agent models are heterogeneous or privately held, formalization of contracts may create an *illusion of alignment* while concentrating real coordination failure into opaque belief layers—a potential hidden channel for protocol drift.
