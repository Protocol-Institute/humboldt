# Who Should Be Generated? Justifying Demographic Targets in Open-Ended Generation

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.02551
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A normative paper on the *justification problem* in demographic fairness auditing of generative systems — specifically, the upstream question of what target demographic distributions ought to be used when evaluating model outputs. The work examines the gap between group fairness definitions (which assume input-side sensitive attributes) and generative audits (which must specify output-side demographic targets post-hoc). It is domain-specific to generative AI fairness evaluation.

## What I took from it

The paper surfaces a real protocol-layer problem: when fairness metrics require a target distribution that is itself unjustified or underspecified, the audit becomes a *Goodhart capture in disguise*. The model optimizes toward an arbitrary demographic proxy, and the justification for that proxy is pushed outside the system. This confirms L-004 (Goodhart Generalization) in a new instantiation — but the instantiation is narrow and the mechanism already mapped.

The work does not explain *why* systems gravitate toward unjustified targets, nor does it provide a mechanism for when this displacement occurs systematically. It identifies a normative gap rather than a causal law. The paper stays at the level of "we should justify our targets better" without exploring the structural forces that prevent justification or the conditions under which target opacity becomes stable equilibrium.

There is a weak signal toward L-012 (Intervention-Layer Displacement): when demographic fairness is operationalized as a legible input to the audit protocol, optimization pressure shifts from the underlying alignment intent (what *should* be generated) to the measurable proxy (matching a target histogram). But the paper does not trace this displacement or show it generalizing beyond fairness metrics.

## Research connections

- **L-004:** Confirms Goodhart in the specific case of demographic target selection in generative audits; target distribution as proxy for unmeasurable normative goal.
- **L-012:** Weak signal — operationalizing fairness as a legible demographic metric may shift optimization pressure away from the underlying intent, but the paper does not develop this mechanism.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry in Automated Systems):** The demographic target is itself a proxy chosen under asymmetric information; its collapse or inadequacy is predictable but the paper does not predict it.

## Seed

**Seed title:** Target Justification Externalization in Metric Protocols

**Seed type:** observation

**Seed text:** When a protocol requires specification of a target distribution for audit or optimization (demographic, output, or otherwise), and that target is not derived from the system's own specifications or user-side input, the justification burden is pushed to a layer outside the protocol. This creates a stable asymmetry: the protocol can optimize to the target (solving an internal problem), but cannot solve or flag the upstream problem of *why that target is correct*. In generative fairness audits, this means the model can be audited against any demographic distribution without the audit system having a mechanism to reject unjustified targets. The pattern likely generalizes to any protocol where optimization objectives are supplied externally rather than derived from system intent.
