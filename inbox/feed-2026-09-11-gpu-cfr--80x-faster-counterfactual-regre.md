# GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game to Static Dataflow and CUDA Graph Replay

**Source:** cs.GT updates on arXiv.org
**URL:** https://arxiv.org/abs/2609.11923
**Date:** 2026-09-11
**Relevance:** Demonstrates significant GPU acceleration of a historically CPU-bound algorithm through compiler-level optimization and dataflow techniques, relevant to algorithmic efficiency and hardware acceleration research.

## Summary

arXiv:2609.11923v1 Announce Type: cross 
Abstract: Counterfactual regret minimization (CFR) is one of the few large numerical workloads that still runs faster on CPUs than on GPUs. Each iteration sweeps a game tree with up to billions of states in millions of small, interdependent gather and scatter steps issued through a generic tree interface. On a GPU every kernel finishes in microseconds, so kernel launches and framework dispatch dominate the run time, and prior GPU implementations have lost to optimized CPU code. We observe that for a fixed game, everything about a CFR iteration except th
