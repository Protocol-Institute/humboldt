# UnitBoost: Managing Compound LLM Systems with a Merge Operator, Not a Model

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2609.09815
**Date:** 2026-09-10
**Relevance:** Proposes a novel merge operator approach for coordinating multiple LLMs in compound systems, addressing a fundamental architectural problem in multi-agent LLM orchestration.

## Summary

arXiv:2609.09815v1 Announce Type: cross 
Abstract: Compound LLM systems often solve a coordination problem by adding a higher-level LLM. The resulting meta-agent reads workers' outputs, writes the final answer, allocates later calls, and decides when to stop. It is expressive, but it also concentrates three control decisions in an opaque, order-sensitive model call. We ask whether the manager needs to be generative at all. UnitBoost replaces that model with a defined meta-level operator: a task-given unit map turns worker outputs into slot-value proposals, a constrained argmax assembles the ou
