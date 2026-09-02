# Limitations of Best-of-Both-Worlds Solutions in Approval-Based Multiwinner Elections

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.01830
**Date read:** 2026-09-02
**Connected to:** L-003, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mathematical impossibility result in voting theory proving that ex-ante proportionality guarantees cannot be simultaneously achieved with ex-post representation axioms in approval-based multiwinner elections. The paper formalizes fairness requirements and derives incompatibility theorems showing trade-offs between different fairness framings.

## What I took from it

The paper demonstrates a structural tension between *fractional* (aggregate, ex-ante) and *realized* (concrete, ex-post) fairness in allocation protocols. This is domain-competent theoretical work but does not generalize beyond its specific institutional context. The impossibility result confirms that fairness axioms cannot all be simultaneously satisfied, but this is a local equilibrium problem in voting design, not a window into a broader mechanism governing protocol behavior under formalization or scaling pressure.

The triage note linking this to L-003 (Formalization Ratchet) and L-006 (Coordination Cost Conservation) appears mistaken on inspection. The paper does not show that informal coordination becomes replaced by formal rules under stress, nor does it demonstrate conservation of coordination costs across protocol layers. It is instead an axiomatic exclusion proof internal to a single voting rule family.

## Research connections

- **L-003:** The paper formalizes fairness axioms but does not investigate whether such formalization *replaces* prior informal norms or alters coordination pressure. No stress condition triggers the shift.
- **L-006:** The paper operates within a single protocol layer (approval-based multiwinner rules) and does not trace cost displacement across transitions.
- **seed-077** (Metric-Induced Preference Ratcheting): Weak connection — the paper shows that ex-ante optimization targets are incompatible with ex-post axioms, but does not explore whether optimizing agents adapt preferences in response to metric legibility.

## Seed

**Seed title:** none
