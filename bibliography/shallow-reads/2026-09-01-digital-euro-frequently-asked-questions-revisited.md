# Digital Euro: Frequently Asked Questions Revisited

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2601.18644
**Date read:** 2026-09-01
**Connected to:** L-001, L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A critical review of ECB design documentation for a retail central bank digital currency (CBDC), interrogating the gap between FAQ claims and technical/operational feasibility across privacy, costs, risks, and utility. Domain-specific critique rather than a generalized law-bearing argument.

## What I took from it

The paper is primarily a *stress-test of published justifications* rather than a primary argument about protocol dynamics. It documents design claims encountering empirical pressure (privacy guarantees vs. surveillance capacity, claimed costlessness vs. real deployment friction, stated utility vs. adoption incentives), but these tensions are presented as case-specific design failures rather than instantiations of deeper regularities.

The work does touch on L-001 (adoption pressure and protocol rigidity) at the margins — the ECB's formalization of CBDC rules through FAQ documents and technical specs creates early commitment that may resist modification once deployed — but this is not the paper's sustained focus. Similarly, L-003 (Formalization Ratchet) is present as a context (central banking pressure toward formal, computable rules) but not examined as a mechanism or empirical phenomenon. The paper reads as forensic documentation of a specific protocol design's shortcomings, not as an investigation of generalizable protocol dynamics.

## Research connections

- **L-001:** CBDC adoption pressure likely to ossify early design choices around privacy/surveillance trade-offs and offline capability, but paper does not investigate this trajectory.
- **L-003:** Formalization pressure is visible (ECB moving from informal coordination norms to machine-readable CBDC specs under scaling/political pressure), but not analyzed as a law-bearing phenomenon.
- **seed-054 (verification-cost-collapse-value-collapse):** Paper hints at a potential inversion: as verification and surveillance capacity increase (through CBDC ledger formalization), claimed utility decreases because privacy guarantees erode — worth tracking, but not the paper's argument.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Disposition:** Store as reference material on CBDC design critique. Flag for retrieval if future work examines how central bank protocol formalization under political/scaling pressure creates irreversible surveillance commitment. Not a primary source for law induction at this stage.
