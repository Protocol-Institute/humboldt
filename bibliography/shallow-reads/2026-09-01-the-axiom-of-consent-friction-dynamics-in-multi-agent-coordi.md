# The Axiom of Consent: Friction Dynamics in Multi-Agent Coordination

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2601.06692
**Date read:** 2026-09-01
**Connected to:** L-006, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A formal game-theoretic framework deriving coordination friction from a single normative axiom (actions affecting agents require authorization proportional to stakes). The work applies to multi-agent systems with heterogeneous preferences and asymmetric information, modeling friction as measurable resistance (deadlock, overhead, conflict).

## What I took from it

The paper formalizes friction as a structural byproduct of consent constraints, which is a coordination cost mechanism rather than a challenge to L-006 (Coordination Cost Conservation) — it appears to operationalize *how* costs are distributed across layers rather than to test whether they are conserved overall. The axiom itself is normative, not descriptive, which limits applicability to protocol systems where consent is actually enforced. The work does not establish whether friction under consent is monotonic with adoption scale (L-010) or whether it exhibits phase transitions. It treats heterogeneity and stakes asymmetry as exogenous parameters rather than emergent properties of protocol evolution.

The connection to L-006 is present but shallow: the paper shows *that* coordination costs manifest as friction, not *where* those costs migrate when protocols formalize. No evidence is offered that total coordination cost is conserved across transitions or that friction reduction in one layer produces hidden costs elsewhere.

## Research connections

- **L-006:** Friction is operationalized as a coordination cost manifestation, but the paper does not test whether consent-based friction is displaced to other protocol layers or governance structures when formal mechanisms are introduced.
- **L-010:** The paper assumes monotonic preference heterogeneity; it does not model adoption dynamics or feedback loops where coordination signals affect willingness to join the system.
- **seed-021:** The axiom's choice (stakes-proportional authorization) is itself a frozen political choice; the paper does not examine how that level is locked in or what alternative axioms foreclose.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Disposition:** Store as shallow. The paper is technically competent and models a real mechanism (friction under consent constraints), but it is axiomatic rather than empirical, normative rather than descriptive, and does not engage with the mechanisms by which coordination costs migrate, concentrate, or are conserved across protocol transitions. It confirms that friction exists; it does not test whether friction is a stable equilibrium property or a symptom of deeper institutional misalignment. No generalizable regularity emerges that extends beyond multi-agent game theory into the broader laws of protocol systems.
