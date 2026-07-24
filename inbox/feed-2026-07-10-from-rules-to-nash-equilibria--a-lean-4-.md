# From Rules to Nash Equilibria: A Lean 4 Case Study in Game-Theoretic Analysis of a Competitive Trading Card Game

**Source:** cs.GT updates on arXiv.org
**URL:** https://arxiv.org/abs/2607.08692
**Date:** 2026-07-10
**Relevance:** Directly demonstrates formalization of strategic equilibria in complex rule systems (CL-001), provides empirical case for how coordination constraints emerge from game structure (CL-002), and illustrates trust-building through machine-checked formal verification of competitive protocols (CL-003).

## Summary

arXiv:2607.08692v1 Announce Type: new 
Abstract: We present a metagame analysis of the competitive Pokemon Trading Card Game, machine-checked in Lean 4 over real tournament data. The headline game-theoretic results, including Nash equilibrium, replicator dynamics, and the matrix-level type-bridge computation, rely on native_decide, which trusts Lean's compiler rather than its kernel; the trust boundary is made explicit. The artifact spans approximately 31,900 lines, 87 files, and 2,627 theorems, of which roughly 200 directly verify empirical claims, with no sorry, admit, or custom axioms. Anal
