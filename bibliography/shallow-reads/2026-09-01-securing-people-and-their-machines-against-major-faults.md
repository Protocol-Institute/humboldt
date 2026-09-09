# Securing People and their Machines Against Major Faults

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.02304
**Date read:** 2026-09-01
**Connected to:** L-001, L-007
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper proposing a peer-recovery architecture for grassroots platforms (decentralized identity systems anchored to self-chosen public keys). The core solution delegates key recovery to a social graph of designated identity custodians rather than centralized infrastructure, addressing Byzantine fault tolerance under loss of private keys or devices.

## What I took from it

The paper is a competent engineering response to a real problem in decentralized systems: how to recover identity when the cryptographic material is gone and no trusted third party exists. It implements recovery through social trust rather than institutional trust. However, the treatment remains operational and local. It does not engage with the generative tension this creates: social recovery protocols necessarily formalize and make legible the social graph itself (who trusts whom, recovery conditions, custodian selection rules), which both stabilizes the system against certain faults and ossifies the social coordination underneath it. The paper demonstrates L-001 (protocol ossification under adoption pressure) and L-007 (trust ratchet) *in miniature* but does not theorize them. It also does not address whether formalizing custodianship roles displaces coordination pressure elsewhere (L-006 conservation hypothesis, L-012 intervention-layer displacement).

## Research connections

- **L-001:** Protocol ossification: as grassroots platforms scale, recovery rules (who can be a custodian, how many are needed, revocation conditions) will become harder to change without breaking trust in existing custodian chains.
- **L-007:** Trust ratchet: recovery protocols accumulate operational legitimacy through stability; initial social-graph-based schemes become trusted precisely because they persist, even if better mechanisms later emerge.
- **L-006:** Coordination cost conservation: formalizing custodianship may reduce direct social coordination burden but increase protocol governance burden (how to update custodian roles, dispute resolution).
- **seed-026 (incommensurability-as-deformalization-cost):** Converting informal social trust into machine-legible custodian roles creates incommensurability costs when the social meaning of "I trust you with my identity" must be encoded into protocol rules.

## Seed

**Seed title:** Social-to-Legible Conversion in Recovery Protocols
**Seed type:** observation
**Seed text:** When distributed systems lack centralized recovery infrastructure, they delegate recovery to formalized social structures (designated custodians, threshold signatures across trust network). This formalization makes the social graph machine-readable and operationally stable but simultaneously freezes it: changing who can be a custodian or under what conditions recovery is permitted requires protocol migration that breaks incumbent trust chains. Recovery protocols thus exhibit a dual ossification: the protocol itself hardens (L-001), and the social structure it formalizes becomes resistant to renegotiation, even when social relationships themselves remain fluid. This pattern may generalize to any protocol system that externalizes fault tolerance to a formally-specified social layer.
