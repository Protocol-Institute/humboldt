# Does the grand coalition form? Persistence, arrival, and the role of the sharing rule in a dynamic process of nested binding agreements

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.17766
**Date read:** 2026-09-02
**Connected to:** L-003, L-010, seed-021
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic model of dynamic coalition formation where players iteratively form and dissolve binding nested agreements under self-confirming beliefs. The work extends Konishi and Ray (2003) and Heitzig and Kornek (2018) by studying conditions under which a "grand coalition" (all players bound in a single agreement) forms, persists, or fails to arrive, focusing on how surplus-sharing rules shape equilibrium outcomes.

## What I took from it

The paper models formalization under coordination pressure (players moving from informal to binding nested agreements) and examines what determines whether escalating formalization leads to full coordination or equilibrium fragmentation. The self-confirming beliefs framework is relevant to L-010 (adoption nonmonotonicity), since players condition on expectations about others' future coalitional behavior—creating potential for multiple equilibria and non-monotonic adoption paths depending on initial conditions and belief anchoring.

However, the work operates in a purely strategic game-theoretic register. It does not investigate whether the formalization process itself changes the agents' optimization targets, introduce unexpected rigidities, or generate the kinds of causal detachment (L-011) or metric capture (L-004) effects that characterize artificial protocol systems. It treats binding agreements as costless formalization; it does not model ossification (L-001), coordination cost conservation (L-006), or the institutional decay dynamics that actual protocolized systems exhibit. The paper answers "when do coalitions form?" not "what happens to the system as formalization deepens?"

## Research connections

- **L-003 [Formalization Ratchet]:** Coalition formation is indeed a formalization event, but the paper does not study whether stress causes irreversible norm entrenchment or whether informal coordination becomes unrecoverable once agreements are binding.
- **L-010 [Coordination Adoption Nonmonotonicity]:** Self-confirming beliefs over coalitional membership do create path-dependent adoption surfaces, but the paper does not investigate whether intermediate adoption levels create unstable or inverted incentive structures.
- **seed-021:** Referenced in triage but not visible in current seed pool; likely concerns binding agreement dynamics and belief ratcheting.

## Seed

**Seed title:** Surplus-Rule Rigidity Under Nested Formalization

**Seed type:** observation

**Seed text:** In systems where players bind via hierarchical nested agreements and must agree on internal surplus allocation before the agreement becomes active, the sharing rule becomes a load-bearing constraint on both formation and stability. Once a sharing rule is formalized and a coalition operates under it, changing the rule requires unbinding the agreement—triggering cascade dissolution of all child agreements. This creates a form of ossification specific to formalization depth: the deeper the nesting, the more costly rule renegotiation becomes, even when all members would benefit from a different allocation. The mechanism generalizes to any protocol system where formal terms become prerequisites for activation and unwinding those terms triggers cascading structural collapse.
