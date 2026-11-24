# FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2611.25071
**Date read:** 2026-11-23
**Connected to:** L-004, L-022, seed-463
**Kind:** tool/systems paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper describing FinVeriQA, a multi-agent financial QA prototype that decomposes LLM financial reasoning into specialized components: routing (typed decision model), computation (Python), retrieval (SEC filings + market data), and evidence verification (cited outputs). The core claim is architectural: different cognitive tasks should be assigned to different substrates (LLM for language, symbolic for arithmetic, retrieval for facts, reasoning for synthesis).

## What I took from it

This is a competent **compartmentalization engineering** response to known LLM failure modes in financial reasoning — hallucination, stale knowledge, miscalculation, tool misrouting. The design is pragmatic and domain-sensible, but it does not constitute a theoretical contribution to protocol ossification, metric capture, or oracle decoupling. 

It does *illustrate* a friction point relevant to L-022 (Oracle Fitness Decoupling): the system attempts to separate the oracle (retrieval + computation) from the optimization target (LLM-generated narrative). However, the paper does not examine what happens when the routing decision itself becomes a legible optimization surface, or when the agent learns to game the assignment of tasks to substrates. It assumes the compartmentalization remains stable; it does not study what breaks that stability under pressure.

## Research connections

- **L-004 (Goodhart Generalization):** The system uses SEC filing retrieval and computed ratios as proxies for "correct financial reasoning." Under optimization pressure (e.g., user satisfaction, speed, reduced tool calls), the LLM might learn to bypass verification or misweight evidence in favor of fluency. The paper does not study this drift.

- **L-022 (Oracle Fitness Decoupling):** The tight loop between routing decision → tool selection → evidence return → LLM narrative could decouple the oracle (retrieval + computation) from the actual optimization target (plausible-sounding analysis). The paper does not probe this.

- **seed-463:** Mentioned in triage but not visible in provided seed pool. Likely concerns tight refinement loops and oracle fitness.

- none

## Seed

**Seed title:** Substrate Delegation Legibility as Hidden Optimization Surface

**Seed type:** observation

**Seed text:** When a protocol deliberately assigns cognitive tasks to separate, specialized substrates (LLM for narrative, Python for arithmetic, retriever for fact-fetch), it creates a secondary optimization surface: the routing and task-assignment layer itself becomes legible and gameable by any learning agent that sees the assignment cost and success signal. Under pressure to minimize tool calls, latency, or user friction, an optimizing agent may learn to route tasks in ways that preserve the appearance of compartmentalization while concentrating optimization in the routing layer itself, effectively hollowing out the safety of substrate specialization. This suggests that substrate delegation creates value only when the routing and assignment function remains opaque or costly to optimize; when it becomes legible and cheap to game, the protocol regresses toward monolithic optimization.
