# Representational Equality in Cross-country Value Simulation: A Systematic Analysis of Large Language Models

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.08058
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical benchmark study evaluating LLMs as proxies for cross-national opinion simulation, measuring representational accuracy disparity across populations. Primary contribution is identifying and quantifying uneven simulation fidelity as a downstream bias amplification risk.

## What I took from it

The paper documents a known failure mode of proxy metrics under heterogeneous populations: when LLMs are deployed as opinion proxies, average accuracy masks severe representational inequality—some populations are modeled far more accurately than others. This is a direct instance of L-004 (Goodhart Generalization) in the measurement layer, but the paper does not theorize the mechanism by which proxy optimization produces this inequality, nor does it investigate whether the inequality is *caused* by the optimization process itself or merely revealed by it.

The work sits at L-012 (Intervention-Layer Displacement) but in reverse: rather than a prediction being formalized into a decision input, here an unmeasurable social fact (opinion distribution) is collapsed into a computable proxy (LLM simulation accuracy), and the optimization pressure on that proxy creates a measurement artifact that then feeds downstream. However, the paper treats this as a technical calibration problem, not as evidence of a deeper coordination failure or protocol asymmetry. It does not address whether making representational equality itself a measurable objective would simply displace the bias elsewhere (a second-order L-004 instance).

## Research connections

- **L-004:** LLM-as-proxy exhibits classic Goodhart capture—optimizing for average opinion accuracy unmasks catastrophic inequality in subpopulation fidelity; the proxy becomes a legible target and degrades under optimization pressure, but unevenly.
- **L-012:** Opinion proxy formalization creates a legible input to downstream allocation/policy protocols; the locus of optimization shifts from "represent opinion fairly" to "maximize LLM simulation accuracy on measurable benchmarks," displacing the real coordination problem upward.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** The paper documents collapse of proxy fidelity under demographic asymmetry—some populations' opinion structures are harder for LLMs to capture, creating systematic advantage/disadvantage. Asymmetry in training data upstream produces asymmetry in proxy performance downstream.
- **seed-004 (Metric Capture):** Direct instance; representational equality is unmeasurable; average accuracy is computable; optimization targets the computable proxy and degrades the unmeasurable goal.

## Seed

**Seed title:** Proxy Fidelity Asymmetry Under Population Heterogeneity

**Seed type:** observation

**Seed text:** When a heterogeneous population is collapsed into a single computable proxy (accuracy metric), optimization pressure on that proxy produces systematically unequal fidelity across subpopulations, even when average performance improves. The inequality is not random noise but reflects upstream structural asymmetries (data availability, representational capacity, training incentives). This suggests a general pattern: proxy systems optimized on aggregate metrics will concentrate modeling error along dimensions of population heterogeneity that are invisible to the aggregate metric. The mechanism generalizes beyond opinion simulation to any protocol using a single legible proxy to represent a heterogeneous social or computational space.
