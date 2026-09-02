# Nine Raters, One Index: Carrying LLM Disagreement into Labour-Market Estimates

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2507.22748
**Date read:** 2026-09-02
**Connected to:** L-004, seed-019
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of LLM annotation disagreement in labor-market classification tasks, using nine models across three vendors to annotate 1,100 occupation-task cells. The paper demonstrates that while rank orderings remain stable (0.74–0.92 correlation), absolute threshold crossing shows extreme volatility (0.1%–38% of jobs above 0.5), illustrating how model choice becomes an analytic degree of freedom in metric construction.

## What I took from it

This is a direct observational instantiation of L-004 (Goodhart Generalization: Metric Capture) at the *protocol design stage*—before optimization begins. The paper does not study what happens when agents optimize against the metric; instead, it reveals that the metric itself is unstable under the choice of computational substrate. This is crucial: it shows that metric capture can begin not from agent gaming but from the **legibility architecture of the measurement apparatus itself**. The disagreement is not noise to be averaged away; it is structural evidence that the choice of which LLM acts as the annotation layer *is itself a hidden optimization variable* that determines downstream labor-market estimates.

The stability of ranks alongside instability of levels suggests a deeper pattern: **relational structure in protocolized systems may be robust to substrate choice, but absolute legibility thresholds are not.** This has implications for L-015 (Interpretive Continuity Decay) and seed-073 (Correlated Failure Under Proxy Consensus)—when multiple systems converge on ranking agreement but diverge on threshold crossing, institutional actors may preserve formal coherence while losing semantic grounding.

## Research connections

- **L-004:** Metric choice embedded in annotation protocol substrate; disagreement reveals that the "measure" is multiply realizable and that model selection is an undeclared analytic freedom that determines what gets measured as real.
- **seed-019:** (not visible in current context; triage note references it; likely concern with explanation opacity in LLM annotation)
- **seed-073:** Correlated failure under proxy consensus: rank agreement masks threshold divergence, creating false confidence in shared measurement.
- **L-015:** The formal audit trace (occupation rankings) survives; the institutional meaning (which jobs matter) decays across model choices.
- **seed-062:** Formalization Opacity Collapse—the act of rendering occupational skill legible to nine different LLMs exposes rather than resolves the unmeasurable substrate.

## Method note

This paper demonstrates that empirical work on protocolized systems should treat computational substrate choice as a *dependent variable*, not a background parameter. When multiple implementations of the "same" protocol produce substantially divergent legible outputs, the disagreement is not measurement error—it is evidence of where the protocol's semantics have not been sufficiently formalized. The method suggests: always run protocol annotations or decisions across multiple independent implementations (models, vendors, decision rules) before treating the output as ground truth for downstream analysis. Disagreement patterns reveal the hidden degrees of freedom in the system and should be indexed as metadata rather than averaged away.
