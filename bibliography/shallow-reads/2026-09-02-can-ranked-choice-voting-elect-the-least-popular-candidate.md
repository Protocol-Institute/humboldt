# Can ranked-choice voting elect the least popular candidate?

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2602.21504
**Date read:** 2026-09-02
**Connected to:** L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

A formal voting-theory paper analyzing the failure modes of instant runoff voting (IRV) under three-candidate elections. The work computes probabilities that IRV selects a "weakest" candidate across four competing definitions of weakness (Borda loser, Bucklin loser, plurality-last, utility-minimum) under standard voter behavior models. It is a bounded technical analysis within electoral systems, not a primary theoretical contribution to protocol dynamics.

## What I took from it

The paper is competent but domain-specific. It demonstrates a known pathology of IRV — the algorithm can violate multiple reasonable metrics of candidate strength simultaneously — but does not theorize *why* formalization of voting rules creates these failure modes, nor does it explore how such pathologies reshape the governance protocols that adopt them.

The work confirms that **metric choice under formalization produces outcome variance**, which is already captured by L-004 (Goodhart Generalization) and L-003 (Formalization Ratchet). However, the paper treats this as a technical problem in voting theory rather than as evidence of a deeper regularity: that formalizing coordination rules (especially under adoption pressure) locks in *arbitrary metric hierarchies* that then shape political incentives. The paper does not ask: "Once IRV is formalized and adopted, how do political actors learn to exploit its pathologies?" or "Does adoption of a flawed formal rule trigger defensive formalization of *candidate recruitment* norms?"

## Research connections

- **L-003:** The Formalization Ratchet is at work here—IRV formalizes a coordination problem, introduces metric ambiguity, and the paper shows the consequences. But the paper does not investigate whether adoption creates path-dependency or pressure to further formalize derivative rules.
- **L-004:** Goodhart Generalization is illustrated: multiple proxies for "strength" yield different winners under optimization. The paper documents the collision but does not theorize how agents adapt.
- **seed-073:** Correlated Failure Under Proxy Consensus — IRV's failures emerge precisely when four candidate-strength metrics diverge. This is not a bug; it is an artifact of computable legibility.

## Seed

**Seed title:** Metric Collapse Under Formalized Plurality Rules

**Seed type:** observation

**Seed text:** When a coordination rule (electoral, resource-allocation, or priority-setting) is formalized to be computationally deterministic, the rule must select a single metric or hierarchy of metrics to resolve ties and edge cases. Under adoption, political actors or protocol participants learn the metric's pathologies and optimize around them. Crucially: the rule cannot be adjusted in real time without returning to informality. The formalized rule thus locks in a specific metric bias, and once locked, generates recurring anomalies that are difficult to repair without reopening the entire protocol. This is distinct from Goodhart's law—it is the *ossification of an arbitrary metric choice* under the pressure of adoption.
