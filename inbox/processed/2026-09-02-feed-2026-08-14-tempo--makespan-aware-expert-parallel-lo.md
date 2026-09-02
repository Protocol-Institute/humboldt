# TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes

**Source:** cs.GT updates on arXiv.org
**URL:** https://arxiv.org/abs/2608.13057
**Date:** 2026-08-14
**Relevance:** Addresses load balancing optimization in mixture-of-experts systems, relevant to distributed inference and GPU scheduling efficiency.

## Summary

arXiv:2608.13057v1 Announce Type: cross 
Abstract: In expert-parallel (EP) MoE serving, every layer synchronizes at the slowest GPU. Dispatchers balance token counts (EPLB, LPLB, UltraEP) or activated-expert counts (METRO), assuming expert time is linear in one. Measurements on two datacenter GPU generations show it is neither: below $\nstar\!\approx\!156$--$168$ tokens, HBM weight streaming dominates---cost attaches to \emph{activated replicas}, not tokens; above it, grouped GEMM rounds tokens to 128-tile $M$-tiles, so \emph{splitting} an expert adds padded compute. A max-affine profile $t=\m
