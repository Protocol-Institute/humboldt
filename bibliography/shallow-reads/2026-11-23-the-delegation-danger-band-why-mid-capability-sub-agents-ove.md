# The Delegation Danger Band: Why Mid-Capability Sub-Agents Over-Trust Inherited Stale State

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.00041
**Date read:** 2026-11-23
**Connected to:** L-012, seed-464
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical measurement paper testing how inherited context state affects decision accuracy in hierarchical agent frameworks across capability tiers. The work compares three inheritance policies (Reset, Selective, Full) on a fixed task ladder using same-family model scales (Qwen 0.6B–8B), measuring how mid-capability agents behave differently than larger or smaller peers when given stale or superseded priors.

## What I took from it

This is a narrow, competent benchmark study on agent delegation patterns. It measures a real phenomenon — that mid-tier agents appear to over-weight inherited conclusions even when given signals that those conclusions are stale — but frames it as a capability-tier artifact rather than a protocol law. The paper is well-scoped within multi-agent systems engineering and provides useful negative results for framework design.

The work touches **L-012** (Intervention-Layer Displacement) in that the locus of error shifts from task-inference to trust-of-inherited-state, but does not interrogate why this shift occurs structurally or whether it generalizes beyond the fork-delegation case. It does not engage with why mid-capability agents specifically show this vulnerability, nor does it connect to coordination or protocol ossification dynamics. The stale-state problem is treated as a capability calibration issue rather than as evidence of a deeper pattern in how agents encode and defer to formalized prior conclusions.

## Research connections

- **L-012:** Touches the displacement mechanism but localizes it to fork-delegation rather than the broader class of formalized handoff protocols.
- **seed-464:** Directly referenced in triage; the paper documents the phenomenon but does not develop the generalized principle.
- **seed-543 (Trust Ratchet Substrate Divergence):** Weak: inherited state acts like a trust signal, but the paper does not measure trust accumulation or substrate divergence.
- **seed-515 (Computable Belief as Collusion Surface):** Tangential; stale conclusions become computable objects that mid-tier agents treat as opaque priors.

## Seed

**Seed title:** Capability-Dependent Prior Entrenchment in Hierarchical Delegation
**Seed type:** observation
**Seed text:** Sub-agents in hierarchical delegation frameworks show non-monotonic trust in inherited state as a function of capability tier: smaller agents ignore stale priors (insufficient confidence to override), larger agents detect staleness and re-infer, but mid-capability agents over-weight inherited conclusions as though they were freshly validated. This suggests agents in a narrow competence band may treat formalized priors (conclusions encoded in context) as more trustworthy than their own inference on novel evidence, implying that formalization itself creates a credibility asymmetry independent of actual information quality. The pattern may generalize to any protocol where intermediate-capability agents must decide between deferring to formalized legacy state and re-computing from base evidence.
