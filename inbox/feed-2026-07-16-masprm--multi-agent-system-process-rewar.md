# MASPRM: Multi-Agent System Process Reward Model

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2510.24803
**Date:** 2026-07-16
**Relevance:** Directly addresses coordination cost efficiency in multi-agent systems by identifying value-generating agent contributions, which tests CL-002's prediction that systems optimize coordination overhead.

## Summary

arXiv:2510.24803v3 Announce Type: replace 
Abstract: Inference-time search over multi-agent systems (MAS) wastes compute when it cannot identify which agent's intermediate message advanced progress. We present the Multi-Agent System Process Reward Model (MASPRM), which scores routed transcripts (ordered sequences of messages between agents) and acts as an inference controller for step-level beam search (SBS) and Monte Carlo Tree Search (MCTS). MASPRM is trained from multi-agent MCTS rollouts labeled only with terminal outcome rewards, without human step-level annotations. We evaluate on GSM8K,
