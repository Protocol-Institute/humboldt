# Can Large Language Models Represent Urban Publics? Behavioral Replication and Population Mismatch in an Affordable-Housing Experiment

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.27100
**Date read:** 2026-09-02
**Connected to:** L-004, L-012, seed-019
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Direct empirical evidence that aggregate proxy fidelity masks systematic structural misrepresentation across population subgroups; demonstrates mechanism by which L-012 (intervention-layer displacement) operates: policy-relevant heterogeneity becomes invisible to optimization because averaging masks it.

## What this is

Empirical study testing whether eight open-weight LLMs can substitute for survey respondents in urban planning decisions (affordable housing). The paper shows LLMs track average survey responses but systematically fail to preserve spatial proximity effects, tenure-based opinion divides, and partisan structure — the heterogeneity that actually drives policy contestation.

## What I took from it

This is a sharp falsification of proxy adequacy under real-world deployment conditions. L-004 (Goodhart) predicts that optimizing a measurable proxy diverges from the unmeasurable goal; this paper shows the mechanism: LLMs achieve aggregate fidelity while *systematically erasing the dimensions of variation that matter for governance*. The city planner who replaces resident input with LLM surveys gets an accurate population mean but loses the spatial and demographic structure that determines whether the policy is actually acceptable to the affected subgroups.

This confirms L-012 (intervention-layer displacement): once resident opinion becomes legible as a computable input to a planning protocol, optimization pressure moves upstream — not toward better representation of actual preferences, but toward a model that is cheap to query and produces legible answers. The displacement is invisible because the aggregate metric passes validation. The heterogeneity erasure is stable because no one is directly measuring what was lost.

## Research connections

- **L-004:** Proxy (LLM average opinion) achieves measurement validation while the unmeasurable goal (legitimate public input that preserves actual conflict structure) degrades silently.
- **L-012:** Once resident preferences become computable inputs to planning protocols, optimization shifts from "what do residents actually want" to "what can we compute cheaply" — the proxy becomes the goal.
- **L-013:** Planning institutions may tolerate accumulating evidence that LLM surrogates erase demographic structure without triggering protocol redesign, because aggregate validation passes.
- **seed-019:** Population mismatch under proxy compression — aggregate fidelity masks subpopulation misrepresentation.
- **seed-073:** Correlated failure under proxy consensus — all LLMs fail on the same dimensions (spatial, partisan), creating consensus that the proxy works.
- **seed-068:** Unmeasurability as anomaly insulation — the erased heterogeneity (what residents actually contest) is hard to operationalize, so its loss remains invisible to auditing.

## Seed

**Seed title:** Structural Heterogeneity Erasure Under Legible Proxy Validation

**Seed type:** observation

**Seed text:** When a complex, multidimensional population preference is compressed into a legible, measurable proxy for protocol input, aggregate validation (e.g., mean opinion accuracy) can succeed while systematic misrepresentation of subgroup structure (spatial, demographic, partisan) remains undetected and stable. The heterogeneity that actual governance must address — the differences that generate contestation — is precisely what aggregation erases. This creates a stable failure mode: the proxy passes validation tests because the tests measure what was averaged away. Governance systems adopting such proxies remain unaware that they have replaced contested public input with a simulacrum that exhibits consent while being unable to register legitimate structural disagreement.
