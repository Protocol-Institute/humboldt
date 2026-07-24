# Shared Selective Persistent Memory for Agentic LLM Systems

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.09493
**Date:** 2026-07-13
**Relevance:** Directly relevant to CL-002 (Coordination Cost Conservation) — persistent memory reduces per-session coordination overhead in multi-agent tool-use workflows, addressing the cost of re-establishing shared context across turns.

## Summary

arXiv:2607.09493v1 Announce Type: cross 
Abstract: Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation histories is token-inefficient and counterproductive: irrelevant context degrades generation quality. We introduce shared selective persistent memory, an architecture that identifies and retains four categories of reusable context (task speci
