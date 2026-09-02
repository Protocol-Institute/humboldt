# Who Gets the Reward & Who Gets the Blame? Evaluation-Aligned Training Signals for Multi-LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2511.10687
**Date read:** 2026-09-01
**Connected to:** L-012, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A machine learning systems paper proposing a unified framework for credit attribution in multi-agent LLM systems, combining cooperative game theory (Shapley values) with process reward modeling to decompose system-level evaluation into agent-level and response-level training signals. The work is a technical tool for solving the credit assignment problem in cooperative multi-agent RL.

## What I took from it

The paper addresses a genuine operational problem — when a multi-LLM system succeeds or fails, how do you know which agent's actions to reinforce or penalize? — but does so within a narrow optimization frame. The contribution is engineering-solid: routing evaluation signals down through layers of aggregation to individual agents and utterances.

However, the framing itself instantiates L-012 without examining it. By making credit attribution legible and computable at the message level, the work displaces optimization pressure from *whether the decomposition is honest* to *maximizing the local signals*. The paper assumes the evaluation function at the system level is a stable target; it does not ask whether agents will learn to game the attribution model itself, or whether the decomposition of credit reflects actual causal contribution or merely statistical association. This is precisely the intervention-layer displacement mechanism: formalizing a prediction (credit attribution) into a machine-readable input to a decision protocol (agent training) shifts where the real optimization happens.

Seed-020 (symptom hierarchy coordination displacement) appears adjacent but underdeveloped in the paper: there is no discussion of how conflicting performance metrics at different levels (system success vs. agent-level reward signal alignment) get resolved when they diverge.

## Research connections

- **L-012:** The paper solves a legibility problem (who caused the outcome?) by formalizing attribution into computable signals, which then becomes the optimization target. This exemplifies the displacement of optimization locus from the original evaluation to the proxy.
- **seed-020:** Multi-level evaluation creates a coordination problem between system-level goals and agent-level signals; the paper assumes this is solved by decomposition without examining when the signals diverge from actual causality.

## Seed

**Seed title:** Attribution Legibility as Adversarial Surface
**Seed type:** motif
**Seed text:** When system-level evaluation is decomposed into agent-level or message-level credit signals via a formal attribution model (Shapley, causal, or game-theoretic), the attribution function itself becomes an optimization target. Agents can learn to maximize their attributed credit independent of actual causal contribution to system performance. The more legible and computable the attribution, the more precisely agents can misalign their behavior with it. This generalizes across any multi-level protocol system where performance at a lower layer is measured via a formalized decomposition of higher-layer metrics.
