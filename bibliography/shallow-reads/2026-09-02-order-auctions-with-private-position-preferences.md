# Order Auctions with Private Position Preferences

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.00786
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

A mechanism design paper studying auctions for two positions where bidders have heterogeneous *private preferences* about which position they value (some care only about first position; others are indifferent). The authors show that standard first-price auctions cannot achieve efficient allocation ex-post, and characterize equilibria under distribution-free conditions.

## What I took from it

This is a narrow equilibrium characterization paper within classical auction theory. It demonstrates a failure mode of position-based allocation when heterogeneous *preference structures* (not just valuations) are private information. The inefficiency arises because the protocol (first-price rule) cannot distinguish between a high bidder who desperately needs position 1 and one who is indifferent — the observable signal (bid) conflates value magnitude with preference shape.

This touches L-004 (the proxy — bid amount — captures heterogeneous unmeasurable preference structure; optimization on the proxy destroys efficiency) and L-008 (the computable enforcement signal is the bid and position allocation; agents optimize against the formalized rule). However, the paper does not generalize the mechanism beyond this specific auction. It does not develop a law about how *formalization of preference-heterogeneous protocols* fails across domains, nor does it investigate how repeated play or scaling changes the equilibrium structure. It is a competent but domain-contained result.

## Research connections

- **L-004:** The bid functions as a proxy for an unmeasurable internal state (preference structure). Optimization on this proxy (bidding to win position 1 when indifferent) causes misallocation — a special case of metric capture, but not explored as such.
- **L-008:** The legible signal (bid amount + position assignment rule) creates an optimization target; agents' strategies deform around the formal protocol structure.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry in Automated Systems):** The auction reveals that a single bid cannot proxy for a two-dimensional preference state; the proxy collapses when upstream heterogeneity (preference shape) is asymmetric across agents.

## Seed

**Seed title:** Preference-Shape Hiding in Position Allocation Protocols

**Seed type:** observation

**Seed text:** When a protocol allocates scarce positions or resources based on a legible signal (bid, score, priority) that was designed to capture *value magnitude* but agents have heterogeneous *preference structures* (e.g., some value only position A; others value A and B equally), the single signal cannot simultaneously reveal both dimensions. Agents then have incentive to misrepresent preference shape via the available signal channel, collapsing the protocol's information capacity. This may generalize to any computable allocation rule where the preference heterogeneity is structurally orthogonal to the dimensionality of the legible input space.
