# Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.03010
**Date read:** 2026-11-23
**Connected to:** L-001, L-012
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical benchmarking study comparing non-agentic and multi-agent LLM configurations across five software engineering tasks, with focus on computational cost and environmental sustainability. This is a performance evaluation paper, not a theoretical or mechanistic contribution to protocol dynamics.

## What I took from it

The paper appears to be a standard comparative systems study: varying agent architecture (single-query vs. multi-agent workflow) and measuring task performance, cost, and resource consumption. The triage suggestion connects it to L-001 (Protocol Ossification) and L-012 (Intervention-Layer Displacement), but the abstract does not indicate the work engages with either mechanism theoretically or traces their operation empirically.

If the full paper contains longitudinal data showing how developer teams adopt specific agent configurations and then resist migration away from them *despite superior alternatives becoming available*, that would be L-001-relevant. If it documents how formalized task decomposition creates observable shifts in where optimization pressure accumulates (from task outcome to intermediate prediction signals), that touches L-012. Neither appears evident from the abstract structure — this reads as a tools paper with sustainability framing, not a mechanism study.

## Research connections

- none

## Method note

This triage note flags a common pattern: papers on agentic systems are frequently sorted into the protocol research corpus when they are actually engineering reports or benchmarking exercises. The presence of "comparison," "workflow," and "LLMs" creates false positive signals. Future triage should distinguish between (a) papers that measure performance across configurations and (b) papers that trace how formal legibility of agent behavior creates unintended dynamics in systems that adopt them. This paper appears to be (a).
