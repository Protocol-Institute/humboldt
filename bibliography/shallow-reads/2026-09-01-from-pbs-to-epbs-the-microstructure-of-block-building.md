# From PBS to ePBS: the Microstructure of Block Building

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.11240
**Date read:** 2026-09-01
**Connected to:** L-001, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of two sequential auction mechanisms for Ethereum block construction, modeling PBS (relay-based) and ePBS (direct proposer-builder interaction) as restricted versions of a common imperfect-information two-stage game. The work derives equilibrium properties and comparative statics on stopping rules and information disclosure.

## What I took from it

The paper is technically rigorous but narrowly scoped to block-building incentives and does not sustain a broader argument about protocol systems or their governance. While the triage note cites L-001 (ossification) and L-014 (boundary concentration under computable enforcement), the paper itself does not investigate either mechanism. 

The shift from PBS to ePBS is presented as an upgrade motivated by MEV efficiency and latency reduction, not as evidence of ossification resistance or as a case where formalization of builder bids creates new optimization boundaries. The work models the microstructure *after* the design choice is fixed, rather than explaining *why* the design was chosen or what pressures drove it. There is no investigation of how adoption of PBS (now widespread) constrained the design space for ePBS, nor any evidence that computable bid verification created new strategic concentration points. The paper is strong technical game theory applied to a specific protocol layer, but not a primary source on laws governing protocol evolution or institutional change.

## Research connections

- **L-001:** Mentioned in triage but not addressed; no evidence that PBS ossification created pressure for ePBS redesign.
- **L-014:** Mentioned in triage; the paper models bid verification but does not investigate whether formalization of builder bids displaced optimization pressure to hidden layers (e.g., builder collusion, threshold manipulation).
- none

## Seed

**Seed title:** none
