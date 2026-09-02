# Trusting AI in Competitive Markets

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.26539
**Date read:** 2026-09-02
**Connected to:** L-007, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A laboratory experiment studying divergence in user trust toward AI pricing advice in oligopoly settings (273 sellers, 91 markets, 30 rounds), where advice cannot be independently verified—its success depends on rivals' unobserved responses. The work introduces gender composition as a moderating variable and examines how trust trajectories split under advice exposure and market structure.

## What I took from it

The paper directly engages L-007 (Trust Ratchet in Safety-Critical Protocols) and L-010 (Coordination Adoption Nonmonotonicity), but in a direction that complicates rather than settles either. The core finding—that trust *diverges* rather than monotonically accumulates—suggests that L-007's stability-based trust accumulation may be conditional on whether users can construct a causal narrative linking advice to outcome. In oligopoly pricing, the causal chain is broken by competitor opacity: advice can be sound and still fail, or fail and still be sound. The gender-composition effect hints that social or demographic factors shape how users *resolve* this causal indeterminacy—a mechanism not yet in the inventory.

The work is empirically sound but remains a domain-specific case study. The oligopoly pricing frame is too narrow to generalize the trust-divergence pattern without cross-domain replication. The paper does not articulate a mechanistic explanation for *why* gender composition moderates trust trajectories, treating it more as an observed pattern than a law-like regularity.

## Research connections

- **L-007:** Challenges the universality of trust ratchet accumulation; suggests trust trajectories depend on causal legibility and outcome attribution, not stability alone.
- **L-010:** Adopters' behavior conditioning on others' adoption may depend on their ability to infer whether adoption "works"—which oligopoly advice cannot provide unambiguously.
- **L-004 (Goodhart):** The advice becomes a proxy for unobservable market response; users optimize trust in the proxy rather than in actual pricing outcomes.
- **seed-069 (Transparency-Legibility as Trust Proxy Substitution):** When actual trust targets are opaque, demographic or signal-based proxies may substitute for mechanistic trust.

## Seed

**Seed title:** Causal Opacity as Trust-Divergence Driver in Advice Protocols

**Seed type:** observation

**Seed text:** In protocol systems where advice cannot be independently verified against ground truth—where outcome depends on unobserved actions by distributed agents—user trust diverges rather than accumulating uniformly. Trust trajectories split when users cannot construct a causal narrative linking advice to outcome. In such settings, demographic and social factors become substitutes for mechanistic confidence, and the polarity of divergence (deepening vs. erosion) may be determined by which proxy agents adopt. This suggests that L-007's trust ratchet is conditional on causal legibility; when that is absent, trust becomes a social/demographic equilibrium rather than a functional accumulation.
