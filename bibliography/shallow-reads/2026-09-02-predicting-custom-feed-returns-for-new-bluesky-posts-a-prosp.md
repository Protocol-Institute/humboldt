# Predicting Custom-Feed Returns for New Bluesky Posts: A Prospective Study

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.13874
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** empirical application
**Escalation:** store-only

## What this is

A systems paper proposing a cold-start ranking task for Bluesky's decentralized feed ecosystem: given a newly published post, predict which independently operated custom feeds will subsequently return (amplify) it. The work frames feed selection as a routing problem rather than a user-centric recommendation problem, building predictive models on post features and feed metadata.

## What I took from it

The paper instantiates L-012 (Intervention-Layer Displacement) in a governance-adjacent domain, but does so in a way that *confirms* the existing law rather than extending it. The optimization pressure displaces from "which posts serve user satisfaction?" (the unmeasurable intent) to "which feeds will algorithmically surface this post?" (the legible proxy). Feed operators become the computable target; user interest becomes latent and unobserved in the routing decision itself.

This is a clean case of proxy substitution, but the paper treats it as a technical problem to be solved, not as a structural reordering. It shows the mechanism operating at scale in a decentralized setting, but offers no evidence of downstream consequences—no measurement of whether this routing optimization eventually distorts feed curator behavior, post production, or user experience. It's a competent cold-start paper with good empirical grounding in one platform's specific architecture.

## Research connections

- **L-004 (Goodhart Generalization):** Feed return prediction is an exact proxy for post virality/fitness; optimization on this metric is already shaping what posts get written and what feeds curate. The paper measures the proxy, not the intent.
- **L-012 (Intervention-Layer Displacement):** Routing optimization is logically upstream of user satisfaction; by making feed-return legible, the intervention layer shifts from user interest to algorithmic amplification likelihood.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Feed return rates are upstream of user satisfaction; this asymmetry may cause the proxy to collapse under optimization pressure, but the paper does not track this.

## Seed

**Seed title:** none

---

**Rationale for store-only:** This is a competent systems paper applying existing law (L-004, L-012) in a new platform context. It does not challenge, extend, or ground those laws with new mechanism evidence. It introduces no novel regularity or generative principle. The work is valuable as a data point confirming that proxy optimization operates in federated recommendation systems, but the fragment is already in inventory.
