# Which Voting Rules Are More Resilient to Coalitional Manipulation?

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.00758
**Date read:** 2026-09-01
**Connected to:** L-004, seed-049
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational game theory paper analyzing vulnerability of standard ordinal voting rules to coalitional manipulation under the Perturbed Culture model. The authors show that a minimal model (preference weight bias) predicts manipulation resilience across rules, and identify sharp phase transitions in success probability.

## What I took from it

This is technically competent work within voting theory but operates entirely *within* the assumption space of rational strategic manipulation under known rule structures. It does not examine what happens when the voting rule itself becomes the optimization target, nor does it model what agents do when the rule structure becomes opaque, unstable, or subject to reinterpretation under stress.

The phase transition finding is interesting mechanically but not novel to protocol systems generally — we already have L-001 and L-005 addressing rigidity and resistance to change. The work does not address *why* coalitions form, whether the preference model itself can be gamed (preference falsification, strategic misreporting of type), or how voting rule selection becomes politicized when manipulation resilience becomes legible. It treats the voting rule as a fixed artifact, not as a protocol embedded in a system of incentives and institutional memory.

## Research connections

- **L-004 (Goodhart Generalization):** The paper assumes voting rules measure "true preference aggregation," but does not ask whether the preference distribution itself (Perturbed Culture model) becomes a target of optimization once resilience metrics are published.

- **seed-049 (Consensus Reasoning Decoupling):** The work demonstrates formal consensus-finding (voting rule selection) decoupling from actual consensus formation; agents decouple reasoning about which rule to use from reasoning about whether the outcome will be accepted.

- **seed-021 (Level Choice as Frozen Politics):** Choice of voting rule, once made, becomes politically frozen — but the paper does not model the institutional cost of switching rules when manipulation becomes visible.

## Seed

**Seed title:** none
