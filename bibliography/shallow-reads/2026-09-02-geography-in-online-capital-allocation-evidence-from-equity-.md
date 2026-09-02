# Geography in Online Capital Allocation: Evidence from Equity-Based Crowdfunding

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.29162
**Date read:** 2026-09-02
**Connected to:** L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of geographic clustering in equity crowdfunding using Japanese platform data (Fundinno). The paper decomposes whether observed local investment concentration reflects search salience, information asymmetry, social ties, or non-pecuniary preference for home-region firms — using detailed user-campaign exposure logs to isolate causal drivers.

## What I took from it

The paper provides concrete evidence *consistent with* L-010 (Coordination Adoption Nonmonotonicity) but does not engage the mechanism. It shows that even when search costs are radically reduced by digital platforms, adoption remains clustered and non-uniform — investors do not spread uniformly across issuers even when all campaigns are equally visible. However, the paper is fundamentally a decomposition exercise: it asks *why* clustering persists (salience, information, ties, preferences), not whether or how adoption decisions are *conditional on observing other adopters' behavior* — the causal core of L-010. The work confirms that reduced friction does not produce coordination equilibration, but treats clustering as a mix of independent preference and information effects rather than as a protocol-level feedback phenomenon. It has no formal model of adoption dynamics or threshold effects.

## Research connections

- **L-010:** Consistent with the empirical claim (adoption remains nonmonotonic despite friction reduction), but does not test the conditional-adoption mechanism. Treats clustering as preference + information, not as feedback-driven protocol behavior.
- **seed-060:** Related to prediction legibility in demand-constrained settings — visibility of campaigns does not equalize demand, suggesting something orthogonal to information availability shapes allocation.

## Seed

**Seed title:** Visibility-Decoupled Adoption Clustering in Frictionless Protocols
**Seed type:** observation
**Seed text:** In protocol systems where search friction is eliminated and all options are equally legible (campaigns visible to all users, no algorithmic hiding), adoption can remain geographically or demographically clustered without invoking information asymmetry or search cost. This suggests clustering is driven by a coordination or preference mechanism *orthogonal to legibility*. In contexts where adoption spreads via social networks or ties rather than centralized matching, visibility reduction may be necessary but not sufficient for equilibration — the protocol system may inherit clustering from its substrate (geography, social structure) independently of its own design. This pattern may generalize to any protocol attempting to aggregate dispersed preference without addressing the structural conditions (network topology, information flows) that shape local vs. global adoption decisions.
