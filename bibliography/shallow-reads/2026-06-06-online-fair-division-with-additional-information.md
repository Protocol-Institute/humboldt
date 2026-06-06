# Online Fair Division with Additional Information

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2505.24503
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Introduces information asymmetry as a mechanism for relaxing fundamental impossibility constraints in sequential allocation — a generalizable pattern for protocolized systems under irreversibility.

## What this is

A theoretical game-theoretic study of fair division under sequential (online) constraints, investigating how access to distributional information (future values, normalization bounds) affects achievability of fairness guarantees. The work establishes impossibility results for zero-information settings and provides constructive algorithms when agents' total valuations are known.

## What I took from it

This paper addresses a core tension in the new nature: **irreversibility + incomplete information = impossibility**. The finding that normalization information alone enables approximate fairness guarantees suggests that protocolized systems can escape hard impossibility boundaries not by relaxing fairness definitions, but by modifying information structure. This is a mechanism, not a domain-specific artifact.

The deeper signal: in sequential allocation protocols (goods, compute, bandwidth, tokens), the *availability of aggregate metadata* functions as a hidden degree of freedom. Systems that commit to transparent total-value disclosure may achieve fairness properties that appear impossible under strict online-only constraints. This generalizes beyond fair division to any protocolized allocation under irreversibility.

The impossibility results themselves are also significant — they formalize what breaks when you combine three constraints (online arrival, irrevocable commitment, strict fairness) without information leverage. Understanding which impossibilities can be *relaxed by information* vs. *require redefinition of fairness* is central to designing implementable protocols.

## Research connections

- **Information structure as a protocol design variable:** Information access functions as a control parameter on achievable guarantees in irreversible systems — worth tracking across domains.

## Candidate laws or signals

- **CL-2505.24503-1:** In sequential allocation under irrevocability, approximate fairness becomes achievable when agents' aggregate valuations are publicly committed, suggesting that transparency of *aggregate* (not individual) information can unlock fairness properties that appear impossible under strict privacy.
