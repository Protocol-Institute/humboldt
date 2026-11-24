# Cogentic: Multi-Agent Orchestration for Automated Proof Discovery

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.40324
**Date read:** 2026-11-23
**Connected to:** L-023, seed-459
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper presenting Cogentic, a multi-agent orchestration framework for automated mathematical proof discovery. The work deploys a population of language models in an iterative prove-verify loop, with a central orchestrator allocating agents to explore competing conjectures, resolve technical obstacles, and maintain long-horizon progress on open problems.

## What I took from it

This is an engineering contribution to multi-agent coordination under legible optimization, not a theoretical claim about protocol dynamics. The framework is designed to *preserve* exploration diversity and intermediate novelty through asynchronous agent allocation — a tactical response to the problem that single-shot generation fails on open-ended problems. However, the paper does not analyze what happens to the system's novelty production, conjecture diversity, or exploration substrate under sustained optimization pressure, nor does it examine whether the prove-verify loop itself becomes a legibility surface that ossifies over deployment time.

The connection to L-023 (Informality as Novelty Sink) is real but inverted: Cogentic *uses* informal agent-to-agent feedback (via the orchestrator's allocation signals) to preserve novelty, rather than studying what happens when informality is formalized. The paper is a proof-of-concept for preserving diversity under coordination, not a study of diversity collapse under formalization. It does not investigate whether the orchestrator's legible allocation protocol eventually becomes the target of optimization itself, or whether agents converge on stereotyped conjecture-generation strategies that satisfy the verify function.

## Research connections

- **L-023:** Cogentic is a system *designed* to prevent novelty sink by keeping agent search spaces decoupled, but the paper does not measure whether the prove-verify loop itself becomes a legible optimization target that reduces functional diversity over time.
- **seed-459:** Related to the tension between formal verification and exploratory freedom, but not directly engaged.
- **L-008 (Proxy Optimization Under Computable Enforcement):** The verify function is a computable proxy for mathematical validity; the paper does not study whether agents optimize for proof-verification-legibility rather than proof correctness under sustained iteration.

## Seed

**Seed title:** Orchestrator Legibility as Implicit Optimization Surface in Multi-Agent Proof Search

**Seed type:** question

**Seed text:** In multi-agent systems where a central orchestrator allocates resources based on legible signals (success/failure of verification, intermediate conjecture quality), does the orchestrator's allocation protocol itself become an implicit optimization target, causing agents to converge on proof-discovery strategies that maximize orchestrator-legibility rather than exploratory diversity? Under what conditions does the prove-verify loop transition from a diversity-preserving mechanism to a novelty bottleneck?
