# RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.12216
**Date:** 2026-07-15
**Relevance:** Directly measures how coordination overhead (shared state, role instructions, summaries) displaces task-relevant content in prompts, empirically testing CL-002's prediction that coordination costs are conserved rather than eliminated.

## Summary

arXiv:2607.12216v1 Announce Type: cross 
Abstract: Multi-agent and memory-augmented LLM systems often place coordination content, shared state, prior discussion, tool outputs, summaries, and role instructions, inside the same finite prompt used for the current task. This creates a practical allocation problem: every token spent on coordination is unavailable to task instructions or evidence when a call is assembled under a fixed context budget. We introduce the Roundtable Context Window Test (RCWT), a controlled protocol for measuring this task-budget displacement effect. RCWT varies coordinat
