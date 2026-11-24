# STAKE: Preventing a colluding majority from double spending

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.01169
**Date read:** 2026-11-23
**Connected to:** L-002, L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of blockchain safety under partial synchrony, exploring whether relaxed honesty assumptions (majority rather than supermajority) can be achieved by introducing economic incentive structure (stake). The work appears to address the feasibility frontier of reducing honest-node requirements through mechanism design rather than protocol reformulation.

## What I took from it

The paper sits at the intersection of L-002 (Hardness Asymmetry) and L-003 (Formalization Ratchet), but does not substantially advance either. It documents a known constraint — the 2/3 supermajority requirement in classic Byzantine fault tolerance — and proposes that game-theoretic incentives (stake) can lower the threshold to a simple majority. However, this appears to be an engineering trade-off rather than a mechanism discovery: verification of double-spend safety remains harder than execution (attackers can explore many fork strategies; defenders must secure against all simultaneously), and the formalization of stake as a legible cost simply displaces rather than resolves coordination burden.

The work is domain-specific: it does not expose a generalizable pattern about how protocol systems behave under adoption pressure, nor does it reveal a mechanism absent from the current inventory. The synchrony assumptions are indeed formalized, but this is a technical refinement within an existing research lineage (partial synchrony protocols) rather than a fresh theoretical insight about artificial systems.

## Research connections

- **L-002:** Confirms hardness asymmetry (verification of safety harder than attack exploration), but does not deepen the mechanism.
- **L-003:** Formalization Ratchet applies tangentially — stake becomes a legible proxy for trust — but the paper does not examine how this formalization changes the topology of informal norms around validator participation.
- **seed-515 (Computable Belief as Collusion Surface):** Faint connection — stake creates a machine-readable signal of commitment, which could become a coordination surface for colluders; not explored in the paper.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
