# Escaping Python Dependency Hell: A Hybrid Replay-and-Repair Pipeline for Python Dependency Resolution

**Source:** cs.MA updates on arXiv.org
**URL:** https://arxiv.org/abs/2609.26952
**Date:** 2026-09-24
**Relevance:** Directly addresses Python dependency resolution challenges and proposes a hybrid approach (PLLM+) to resolve version conflicts and compatibility issues in Python ecosystems.

## Summary

arXiv:2609.26952v1 Announce Type: cross 
Abstract: Dependency conflicts in Python ecosystems arise from incompatible version constraints, missing packages, and undocumented compatibility relationships, causing many real-world code snippets to fail at execution. This paper presents PLLM+, a hybrid dependency-repair pipeline evaluated on the HG2.9K benchmark of 2,891 dependency-failing snippets. PLLM+ prioritizes inexpensive deterministic steps before invoking LLM-based repair: static AST-based interpreter inference, replay of historically successful dependency configurations from the competitio
