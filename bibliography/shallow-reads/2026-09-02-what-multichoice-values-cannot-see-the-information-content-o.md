# What Multichoice Values Cannot See: The Information Content of Anonymous Values for Games with Graded Participation

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.01527
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A theoretical characterization paper in cooperative game theory proving what linear, symmetric value functions *cannot* extract from games where players have graded (multilevel) participation. The work establishes an invariance: any anonymous value function computing individual payoffs is blind to certain structural features of coalition formation under ordered participation levels. The domain is formal — voting with abstention, multichoice games, feature attribution — and the contribution is a negative result: a classification of information loss.

## What I took from it

This is a competent technical paper establishing a structural limit on symmetric value extraction. It shows that when players can participate at $m$ ordered levels, the family of all linear symmetric values can only "see" permutation-invariant properties — they are structurally insensitive to asymmetries in how coalitions form across participation levels. This connects to L-004 (Goodhart Generalization) in a narrow but real way: the proxy (multichoice value) genuinely loses information about the underlying game structure, and this loss is *permanent under the symmetry constraint*. It also touches L-008 (proxy optimization under computable enforcement) because if these values are used as legible attribution mechanisms in automated systems, the system inherits this blindness.

However, the paper does not theorize *why* this matters operationally, does not track what happens when agents optimize against these limited proxies, and does not generalize the mechanism beyond symmetric value functions. It is an existence proof of information loss, not a law about protocol behavior or agent capture.

## Research connections

- **L-004:** The multichoice value is a proxy for true coalition contribution; the paper proves this proxy has structural information gaps independent of optimization pressure. Confirms the premise that proxies lose information, but does not show capture dynamics.
- **L-008:** If these values are formalized into legible enforcement signals (e.g., automated feature attribution, voting fraud detection), agents optimizing against them would exploit the blindness systematically. Paper does not explore this.
- **seed-073 (Correlated Failure Under Proxy Consensus):** When multiple systems rely on the same symmetric value function, they all inherit the same blindness; failure modes become correlated. Paper hints at this but does not develop it.

## Seed

**Seed title:** Symmetry-Locked Blindness in Computable Proxies

**Seed type:** observation

**Seed text:** Anonymous (symmetric) value functions in graded-participation games are structurally incapable of detecting information present in the game structure itself — specifically, asymmetries in coalition formation across participation levels. This blindness is not a function of computational cost or incomplete data; it is built into the symmetry constraint itself. When such proxies are formalized as legible enforcement signals in automated protocols, the system inherits this blindness as a permanent structural property, and agents optimizing against the protocol will discover and exploit it. The mechanism generalizes beyond game theory: any computable proxy that enforces symmetry constraints on asymmetric underlying domains will have systematic gaps in what it can observe or enforce.
