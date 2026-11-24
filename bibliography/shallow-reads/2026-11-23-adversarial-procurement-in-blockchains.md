# Adversarial procurement in blockchains

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.05559
**Date read:** 2026-11-23
**Connected to:** L-002, seed-098
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic treatment of mechanism design for sourcing expensive computational tasks (proof generation, settlement labor) in adversarial blockchain contexts where prover-verifier asymmetry is structural. The work formalizes the tension between task difficulty and incentive alignment when participants are pseudonymous and potentially strategic about participation.

## What I took from it

This is a focused application of hardness asymmetry (L-002) to a specific protocol layer rather than a theoretical extension of it. The paper operationalizes the asymmetry *as a feature* of mechanism design — the gap between prover cost and verifier cost becomes the lever for incentive structuring. This confirms L-002's generalizability to blockchain contexts but does not expose new mechanisms of how asymmetry propagates into coordination failure, adoption resistance, or unexpected equilibria.

The work is mechanistically sound but domain-bound. It treats the asymmetry as a design parameter to be exploited for immediate incentive alignment, not as a source of longer-term ossification, strategic drift, or catastrophic miscalibration. It does not investigate how procurement mechanisms themselves become formalized and resistant to modification once adoption pressure sets in (L-001 territory), nor does it address whether the legibility of the prover-verifier boundary creates new surfaces for strategic manipulation at higher layers.

## Research connections

- **L-002 (Hardness Asymmetry):** Direct instantiation in cryptographic proof contexts; confirms asymmetry is mechanistically stable across verification domains.
- **seed-098:** Referenced in triage note; likely concerns sabotage legibility and threshold protocol vulnerability — not examined in abstract.

## Seed

**Seed title:** none

**Seed type:** 

**Seed text:** 

---

**RATIONALE FOR STORE-ONLY:**

This paper meets 1 of 4 escalation criteria:
1. ✓ Primary source presenting sustained theoretical argument (game-theoretic formalization)
2. ✗ Does NOT challenge or substantially extend a law — it instantiates L-002 in a narrow domain
3. ✗ Does NOT introduce absent mechanism — prover-verifier asymmetry is already catalogued
4. ✗ Pattern does NOT generalize beyond blockchain procurement — it's a domain application

The work is technically competent and confirms existing theory in a new domain, but it does not crack open a new line of inquiry or expose a mechanism absent from the inventory. Store for domain reference; no seed emission warranted.
