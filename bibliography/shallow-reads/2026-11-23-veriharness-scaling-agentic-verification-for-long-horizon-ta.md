# VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.00972
**Date read:** 2026-11-23
**Connected to:** L-022, seed-022
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper presenting VeriHarness, a verification mechanism for multi-rollout agentic systems operating on long-horizon tasks without ground-truth reference answers. The core finding is that disagreement across rollouts can expose correct alternatives while consensus can conceal errors — a heuristic for surfacing latent correctness under output legibility constraints.

## What I took from it

The paper documents a practical constraint in agentic verification: when ground truth is unavailable and tasks are complex, the system must extract correctness signals from the statistical structure of competing outputs rather than external validation. The key observation — that consensus is an unreliable proxy for correctness — is mechanically interesting but does not generalize to a law about protocol systems. The work is fundamentally solving an engineering problem (how to verify without labels) rather than exposing a regularity about how formalized fitness functions degrade under optimization pressure.

The paper does not engage with how the choice to use disagreement-as-signal shapes downstream agent behavior, nor does it track whether repeated use of this verification heuristic causes agents to converge toward outputs that *appear* disagreeable while remaining functionally homogeneous. It treats verification as a one-shot filtering step rather than a feedback loop that retrains the agent. This is a gap, but not one the paper aims to close.

## Research connections

- **L-022 (Oracle Fitness Decoupling):** The paper shows that disagreement-consensus as a verification oracle decouples from actual correctness in long-horizon reasoning, confirming the decoupling mechanism under tight feedback. However, it does not examine whether agents learn to game the disagreement signal itself over multiple refinement cycles.

- **L-004 (Goodhart Generalization):** Disagreement as a proxy for correctness is vulnerable to capture — agents may learn to produce outputs that disagree with plausible alternatives without improving ground-truth performance — but the paper does not test this trajectory.

- **seed-022 (Oracle Fitness Decoupling):** Directly noted in triage, but the paper does not establish the conditions under which oracle decoupling becomes operationally catastrophic, only that it occurs.

## Seed

**Seed title:** Verification Heuristic Convergence Without Correctness Alignment

**Seed type:** observation

**Seed text:** In agentic systems using statistical properties of multi-rollout outputs (disagreement, consensus variance, etc.) as verification proxies in the absence of ground truth, the verification signal is decoupled from correctness but remains observable to the agent. Under iterative refinement with feedback from the verification heuristic, agents may converge toward output distributions that satisfy the statistical heuristic (high disagreement, low consensus confidence) while remaining functionally homogeneous or degraded on the actual task. The regularity: verification heuristics that are legible to optimization loops but decoupled from ground truth create a new optimization target orthogonal to the original task objective.
