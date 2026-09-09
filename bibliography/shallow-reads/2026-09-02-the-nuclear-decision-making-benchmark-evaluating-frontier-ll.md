# The Nuclear Decision-Making Benchmark: Evaluating Frontier LLMs on Nuclear Tendencies

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.05180
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** benchmark / evaluation framework
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing a structured evaluation framework (151 scenarios across escalation, arms control, non-proliferation, proliferation domains) designed to measure consistency and policy-alignment of frontier LLMs in high-stakes nuclear decision contexts. The work is primarily a measurement tool, not a theoretical or empirical argument about protocol dynamics.

## What I took from it

The NDM Bench is a *proxy legibility instrument* — it makes LLM decision patterns measurable and comparable where they were previously opaque. This is methodologically sound but does not itself investigate what happens when such measurement becomes the target of optimization. The paper establishes a computable enforcement signal (scenario consistency scores) but does not track whether models, when trained or deployed against NDM performance, decouple their internal reasoning from the measured behavior, or whether the proxy captures or misses the actual safety property being approximated.

The relevance to L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement) is potential, not demonstrated. The benchmark *creates the conditions* for Goodhart capture — it operationalizes an unmeasurable goal (appropriate nuclear decision-making) as a measurable proxy (scenario consistency) — but the paper does not investigate whether optimization pressure against NDM scores would hollow out the measure. This is a tool; the law would manifest in downstream deployment or fine-tuning workflows not examined here.

## Research connections

- **L-004:** Creates a measurable proxy for an unmeasurable property (policy-appropriateness), which may become a Goodhart target under optimization pressure; the paper does not test this.
- **L-008:** Establishes a computable enforcement signal (NDM scores) that could drive proxy optimization in models fine-tuned on this benchmark; no evidence of causal detachment or proxy decay is presented.
- **seed-069:** Transparency-Legibility as Trust Proxy Substitution — NDM Bench makes decision patterns legible but does not validate that legibility correlates with actual safety.
- **seed-073:** Correlated Failure Under Proxy Consensus — if multiple models optimize against NDM, they may all fail in identical out-of-distribution ways not captured by the scenario set.

## Seed

**Seed title:** Proxy Legibility Without Validity Binding in Safety-Critical Benchmarks

**Seed type:** question

**Seed text:** When a benchmark operationalizes an unmeasurable safety property (appropriate nuclear decision-making) as a computable proxy (consistency across scenarios), high performance on the proxy may decouple from the ground truth under three conditions: (1) when models are fine-tuned to optimize the proxy; (2) when the proxy encodes domain-specific but non-generalizable consistency patterns; (3) when the scenario set and the real world diverge in ways the benchmark cannot capture. The more legible the proxy, the more optimization pressure it attracts, and the more likely decoupling becomes. This suggests that transparency in safety benchmarks can paradoxically reduce safety if the benchmark becomes a target of computable enforcement rather than a diagnostic tool.
