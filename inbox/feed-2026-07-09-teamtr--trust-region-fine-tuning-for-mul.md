# TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2605.15207
**Date:** 2026-07-09
**Relevance:** Directly addresses coordination failure modes in multi-agent LLM systems, relevant to CL-002 (coordination costs increase with formalization) and CL-003 (trust degradation in safety protocols).

## Summary

arXiv:2605.15207v2 Announce Type: replace-cross 
Abstract: Multi-agent LLM systems have shown promise for complex reasoning, yet recent evaluations reveal they often underperform single-model baselines. We identify a structural failure mode in sequential fine-tuning of shared-context teams: updating one agent shifts the team's context distribution, and when subsequent updates are evaluated on cached rollouts, this mismatch compounds. We formalize this as the compounding occupancy shift and prove that stale-occupancy evaluation incurs a penalty that scales quadratically with the number of agent
