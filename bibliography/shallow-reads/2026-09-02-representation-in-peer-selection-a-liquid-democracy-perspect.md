# Representation in Peer Selection: A Liquid Democracy Perspective

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.13085
**Date read:** 2026-09-02
**Connected to:** L-010, L-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic study of committee selection under "liquid profiles"—preference structures derived from delegation graphs where voters approve candidates transitively through a single trusted agent. The paper formalizes delegation-based peer selection and examines computational and axiomatic properties of voting rules under this domain restriction.

## What I took from it

The paper models a real coordination structure (transitive trust delegation) as a constraint on preference expression, which is relevant to L-010 and L-015's concerns about how adoption signals and interpretive coherence behave in distributed governance. However, the work remains primarily formal and analytical—it establishes properties of voting rules under restricted preference domains rather than empirically tracking how agents actually adopt, defect, or reinterpret delegation protocols under pressure.

The study does not examine what happens when the "liquid" structure itself becomes contested (e.g., when trust chains break, agents fork delegations, or verification of transitivity becomes opaque at scale). It is a clean mathematical treatment of an idealized coordination primitive, not an investigation of how such primitives degrade or reorganize under real adoption and stress conditions.

## Research connections

- **L-010 (Coordination Adoption Nonmonotonicity):** The paper constrains preference space in ways that likely affect monotonicity of adoption curves, but does not track empirical adoption dynamics or thresholds.
- **L-015 (Interpretive Continuity Decay in Distributed Governance):** Transitive trust delegation is formally specified here, but the paper does not investigate how shared interpretation of delegation chains diverges over time or across agents.
- **seed-070 (Obligate-Coordination-as-Infrastructure-Constraint):** Liquid profiles instantiate delegation as a structural constraint; the paper shows this works mathematically but not how agents resist or rewire it.

## Seed

**Seed title:** Delegation Formalism as Trust Legibility Lock

**Seed type:** observation

**Seed text:** When delegation is formalized as a transitive and single-channel structure (one trusted agent per voter, approved set as closure), it converts diffuse trust into a computable, auditable preference profile. This makes coordination verifiable but also fixes the trust topology against rewiring under uncertainty or defection pressure. As adoption scales, agents may develop parallel or hidden delegation chains to escape the formal constraint, creating a gap between the legible delegation graph and actual coordination. The seed: *formal delegation protocols may exhibit a trade-off between interpretive coherence (in the small) and coordination flexibility (under scaling or conflict).*
