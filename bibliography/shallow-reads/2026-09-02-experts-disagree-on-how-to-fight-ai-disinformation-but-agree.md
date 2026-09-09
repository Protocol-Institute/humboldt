# Experts Disagree on How to Fight AI Disinformation, but Agree That Health and Politics Need Different Solutions

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.28621
**Date read:** 2026-09-02
**Connected to:** L-004, seed-026
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A Delphi-style expert elicitation study (54 international experts) mapping threat perception and intervention preferences across AI disinformation domains. The work documents domain-specific disagreement on both threat typology (video deepfakes rank highest in politics; AI text in health) and solution efficacy (government regulation receives both highest "most effective" and highest "least effective" votes), concluding that one-size mitigation frameworks are incoherent.

## What I took from it

This is a **threat-modeling paper**, not a law-grounding or mechanism paper. It confirms that metric capture operates *domain-specifically*: the proxy chosen to measure "disinformation threat" is incommensurable between health and politics because the causal chains to harm are structurally different (epistemic capture vs. behavioral manipulation, different decision timescales, different constituencies of harm). The expert disagreement on regulation efficacy is noteworthy but *expected under L-004 conditions* — once you fix a metric (e.g., "deepfake detection rate"), optimization pressure migrates elsewhere, and the same intervention (regulation) becomes simultaneously adaptive in one frame and maladaptive in another.

The paper does not investigate *why* this incommensurability persists, nor does it examine whether attempts to unify mitigation protocols under a single metric-regime would predictably reproduce the disagreement at a lower level. It is a good map of the problem surface, but the mechanism remains external to the study.

## Research connections

- **L-004 [Goodhart Generalization]:** Domain-specific proxy capture — the threat metric that works in politics (deepfake prevalence) does not transfer to health (text-based misinformation), suggesting metric capture is not just about optimization pressure but about structural incommensurability of causal models across domains.
- **seed-026:** Cited in triage note but not available in current inventory; likely tracks domain-specificity of metric failure.
- **L-012 [Intervention-Layer Displacement]:** The regulation disagreement hints at this — interventions designed at the protocol layer (legal enforcement) get reinterpreted as proxy-optimizing signals depending on which threat model is operative.

## Seed

**Seed title:** Domain-Locked Metric Incommensurability in Multi-Regime Protocol Systems

**Seed type:** observation

**Seed text:** When a single intervention (e.g., regulation, detection, labeling) is applied across domains with structurally different causal models of harm, the metric used to assess efficacy becomes domain-specific and non-transferable. Experts disagree not because they lack evidence but because they are optimizing against incommensurable threat models encoded in their choice of metric. This suggests that protocol unification across domains with different causal structures does not resolve via better metrics, but reproduces disagreement at each new consolidation layer — a possible instance of L-006 (Coordination Cost Conservation) where the cost of metric alignment is shifted rather than eliminated.
