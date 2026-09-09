# Aligning LLM-Simulated and Human Examinees for Psychometric Calibration: A Cognitive Diagnostic Profiling Approach

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.26317
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper proposing Cognitive Diagnostic Profiling (CDP), a prompting framework to make LLM-simulated test-takers produce response distributions closer to human examinees during psychometric calibration. The core problem: LLMs generate responses that are too uniform and accurate to serve as useful proxies for human variance during test development.

## What I took from it

The paper confirms a narrow instantiation of L-004 (Goodhart Generalization): when you use LLM response accuracy as a proxy for human test-taker variance to calibrate assessment instruments, the proxy captures uniformity rather than the heterogeneity you actually need. The proposed solution—injecting natural-language cognitive profiles to induce variance—is a pragmatic engineering fix that does not generalize as a law.

The work touches L-008 (Proxy Optimization Under Computable Enforcement) tangentially: the moment LLM responses become legible as calibration inputs, optimization pressure reshapes them away from human-like variance. But this is a solved design problem (add noise, simulate profiles), not a mechanism that resists solution or propagates across protocol boundaries. The paper is competent psychometrics + prompt engineering; it does not expose a structural regularity in how protocolized systems fail when proxies replace unmeasurable targets.

## Research connections

- **L-004:** Confirms that accuracy-as-proxy for human-like response heterogeneity fails under optimization; the fix is to diversify inputs, not eliminate the proxy.
- **L-008:** LLM responses become legible and measurable; the system optimizes toward uniformity instead of the underlying human variance distribution. But this is within-domain, not a cross-layer or cross-system pattern.
- **seed-059:** Tangentially related—trust in LLM calibration proxies inverts when the proxy (accuracy) diverges from the goal (variance coverage). Not developed here.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Rationale for store-only:** This is a capable tool paper solving a real applied problem (LLM test-taker simulation for assessment). It provides no sustained theoretical argument, introduces no mechanism absent from L-004 or L-008, and does not generalize beyond test calibration. The solution (profile injection) is domain-specific engineering. The observation (LLM accuracy ≠ human variance) is a known artifact, not a law candidate.
