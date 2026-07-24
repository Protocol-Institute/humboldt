# Semantic Early-Stopping for Iterative LLM Agent Loops

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2606.27009
**Date:** 2026-06-26
**Relevance:** Directly relevant to CL-001 (Formalization Ratchet)—semantic stopping criteria represent a shift from syntactic to formally-verifiable termination conditions, creating path-dependent constraints on agent loop design.

## Summary

arXiv:2606.27009v1 Announce Type: cross 
Abstract: Multi-agent large language model (LLM) loops, for example a Writer that drafts and a Critic that revises, are almost always terminated by a fixed iteration cap (max_iterations). This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. We study semantic early-stopping: the loop halts when consecutive draft embeddings stop changing in meaning (cosine distance with a patience window) and the answer's measured quality stops improving. Our work makes thre
