# Width, Memory, and Delay: A Resource Accounting for the Limits of Flat Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.00028
**Date read:** 2026-09-02
**Connected to:** L-006, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

This is a control-theoretic analysis of flat (non-hierarchical) multi-agent systems, arguing that such systems face an irreducible, population-independent error floor in disturbance rejection. The authors use a testbed to show that adding agents alone cannot overcome performance limits — hierarchical organization is necessary to break through the causal ceiling imposed by latency, communication bandwidth, and memory constraints.

## What I took from it

The paper formalizes a constraint on coordination in homogeneous systems: coordination cost does not vanish with scale, but rather becomes *locked into the protocol structure itself* through latency and causal delay. This is consistent with L-006 (Coordination Cost Conservation) but does not substantially extend it — the mechanism is already predicted by existing heavy-lifts around protocol friction under scaling.

The work is primarily a **negative result** in control theory: it shows what *cannot* be done with flat architectures. It does not examine what happens when agents begin to optimize against the latency constraints themselves (the space where L-008 operates), nor does it model the adaptive, strategic behavior that emerges in artificial protocol systems. It is domain-specific (swarms, multi-agent RL) and does not generalize to governance, economic coordination, or other protocol classes where strategic adaptation is the key phenomenon.

## Research connections

- **L-006:** Confirms that coordination cost is *conserved* across scaling — adding width does not reduce latency or communication overhead, it redistributes them. But this is already inventoried; the paper does not open a new line.
- **L-008:** Latency and communication constraints become legible optimization targets for adaptive agents. The paper shows the constraint exists but does not model strategic response to it.
- **seed-070 (Obligate-Coordination-as-Infrastructure-Constraint):** Suggests causal delay as an irreducible infrastructure floor, not merely a tuning parameter. Modest resonance but no new mechanism.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**DECISION: Store as shallow only.** This is competent work in control theory, but it operates within the already-mapped territory of coordination cost conservation under scaling. It does not examine adaptation, protocol capture, or strategic behavior — the zones where new regularities emerge in artificial systems. No new mechanism is introduced that would change the law inventory or open lines of inquiry.
