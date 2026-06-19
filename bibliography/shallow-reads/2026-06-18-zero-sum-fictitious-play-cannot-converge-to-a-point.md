# Zero-Sum Fictitious Play Cannot Converge to a Point

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2604.07544
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical result in multi-agent learning dynamics showing that fictitious play—a canonical history-based protocol where agents best-respond to empirical opponent distributions—fails to converge pointwise in zero-sum games with non-singleton equilibrium sets. The paper strengthens classical convergence guarantees by demonstrating that even when the protocol converges to the equilibrium set, it cannot settle on any single strategy when multiple equilibria exist and are fully mixed.

## What I took from it

This is a negative result about a specific learning protocol, not a foundational claim about protocolized systems in general. The finding is internally consistent with game theory: fictitious play achieves set-wise convergence (a weaker guarantee) but not point-wise convergence (a stronger one). The result applies only to zero-sum games with fully mixed equilibrium sets—a constrained domain.

The relevance to the new nature research agenda is limited. This addresses *failure modes of a particular learning algorithm* rather than uncovering structural laws governing how artificial systems behave under constraint. The paper does not propose a mechanism absent from current inventory, nor does it suggest a generalizable pattern beyond game-theoretic convergence behavior. It refines known bounds on an existing protocol rather than challenging or extending an active hypothesis about protocolized systems.

## Research connections

- None currently active in the research context.

## Candidate laws or signals

none
