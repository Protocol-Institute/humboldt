# Causal Inference under Interference with Learned Exposure Mappings

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.19224
**Date read:** 2026-09-02
**Connected to:** none
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper on causal inference in spatial spillover settings where the exposure mapping (how treatment propagates through space) is unknown and must be learned from observational data. The work compares mechanistic transport models with modern operator-learning approaches (PDE, PINO, FNO, GeoPT) to understand how uncertainty in learned exposure mappings propagates into downstream causal estimates under interference.

## What I took from it

This is a competent methodological contribution to the causal inference literature, but it operates entirely within the standard problem frame of statistical identification. The core issue — uncertainty in a latent mechanism that shapes observable spillovers — is treated as an estimation problem solvable by choosing the right learning architecture.

What *doesn't* emerge here is any structural insight about how formalized exposure mappings reshape the agents or institutions operating within them, how legibility of spillover creates new optimization targets, or whether the act of learning and automating the mapping introduces systematic distortions in how actors perceive or respond to treatment. The paper assumes the exposure mapping is a fixed fact to be discovered, not a site of strategic behavior or protocol drift. No tension between mechanistic and learned models points toward a deeper pattern about formalization opacity or legibility-driven convergence.

This reads as domain-specific methodology, not as a window onto how artificial coordination systems behave when causal structure becomes computable.

## Research connections

- none

## Seed

**Seed title:** none
