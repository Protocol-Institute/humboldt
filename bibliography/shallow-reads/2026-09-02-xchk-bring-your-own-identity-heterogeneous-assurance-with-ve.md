# xChk: Bring Your Own Identity -- Heterogeneous Assurance with Verifier-Determined Sufficiency

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.13369
**Date read:** 2026-09-02
**Connected to:** L-014, L-002
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A reference implementation of a federated identity protocol that decouples identity verification from access control by allowing users to enroll via heterogeneous proof sources and relying parties to set their own sufficiency policies. The work is primarily a systems/engineering contribution demonstrating BYOI feasibility via OAuth 2.0/OIDC extensions, not a sustained theoretical or empirical investigation of protocol properties.

## What I took from it

The architecture is *designed* to distribute boundary-setting pressure: the IdP becomes a claim transport layer, and each RP applies its own evidence policy. This is an explicit attempt to prevent centralized metric capture (L-004) by making the sufficiency threshold legible and RP-controlled rather than IdP-determined.

However, the paper does not investigate what actually happens under optimization pressure. It does not study: whether RPs converge on sufficiency standards (pooling), whether the heterogeneity of proof sources creates new vulnerabilities or gaming surfaces, or whether decentralizing the boundary merely displaces the strategic optimization to a new layer (seed-080). The work assumes the policy-choice mechanism solves the problem; it does not treat adoption, gaming, or equilibrium as empirical or theoretical questions.

This is competent protocol design that anticipates some risks, but does not generate sustained evidence about how heterogeneous verification systems behave under adversarial conditions, scale, or long-term institutional drift.

## Research connections

- **L-014:** The work directly instantiates verifier-determined sufficiency, moving the boundary from IdP policy to RP policy. Whether this prevents strategic concentration or displaces it remains unstudied.
- **L-002:** Heterogeneous proofs create asymmetry: verification cost is distributed but forgery cost may concentrate on weaker proof sources. Not addressed.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry — by accepting heterogeneous proofs, the system creates upstream asymmetry in proof quality/cost; optimization pressure may concentrate on the weakest proof source, not the sufficiency policy itself.

## Seed

**Seed title:** Heterogeneous Sufficiency as Boundary Displacement, Not Elimination

**Seed type:** motif

**Seed text:** In protocols that decentralize access control policy to downstream verifiers (RPs) and render proof sufficiency legible and machine-readable, strategic optimization pressure does not disappear — it relocates from the identity provider to the RP population. Under adoption and competition, RPs face incentives to either converge on a common sufficiency standard (reducing heterogeneity to pooled consensus) or to claim lower sufficiency thresholds to capture marginal users, driving down effective assurance across the system. Heterogeneous sufficiency may thus preserve L-014 boundary concentration while creating a secondary form of pressure: competitive lowering of the legible bar.
