# Modeling Shipping Emissions: Machine Learning, Engineering, and Policy Counterfactuals

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.01008
**Date read:** 2026-11-23
**Connected to:** L-004, seed-022
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical comparison of prediction methods (ML, regression, hybrid, engineering theory) for maritime CO2 emissions under EU policy enforcement, using out-of-sample counterfactual accuracy as the discriminator. The work documents a prediction-counterfactual gap: high in-sample fit does not transfer to reliable policy response estimation.

## What I took from it

This is a narrow but sharp illustration of **oracle fitness decoupling** (seed-022/L-008): ML models optimized for predictive accuracy on historical fuel consumption data perform well on interpolation but fail catastrophically on out-of-sample counterfactual scenarios (e.g., speed reduction mandates). The gap persists even in a relatively constrained domain where ground-truth physics is available. The finding does not challenge L-004 (Goodhart Generalization) but narrows it: the problem is not that the proxy (prediction accuracy) becomes a goal in itself, but that the proxy is *locally* valid (high R² on holdout fuel data) while remaining orthogonal to the decision-relevant quantity (how emissions respond to policy intervention).

However, this is fundamentally a domain-specific failure mode in applied ML, not a law or mechanism for protocolized systems. The paper does not investigate why this gap arises in protocol or coordination contexts, nor does it generalize the decoupling to systems where multiple agents optimize jointly under computable legibility. It is a case study in the dangers of proxy optimization, not a new mechanism or challenge to existing laws.

## Research connections

- **L-004:** Confirms the prediction-proxy-divergence risk, but under interpolation rather than under optimization pressure from multiple agents.
- **seed-022:** Direct illustration; the oracle fitness (ML model) decouples from policy fitness because the refinement loop (historical data) does not contain the counterfactual scenario.
- **L-008:** Tangential; shows what happens when computable enforcement signals (fuel data) drive model optimization, but does not explore multi-agent racing or catastrophic risk dynamics.

## Seed

**Seed title:** Oracle Fitness Localism Under Bounded Training Support

**Seed type:** observation

**Seed text:** Predictive oracles optimized on historical data achieve high fitness on the training domain (interpolation, within-sample prediction) while remaining orthogonal to fitness on out-of-sample counterfactual queries, even when the underlying mechanism is physically grounded and in-principle deterministic. This gap widens when the counterfactual scenario lies outside the support of the training distribution. In protocol systems where policy makers or agents rely on ML forecasts to guide decisions under novel constraints, this oracle-counterfactual decoupling becomes a hidden failure mode: the protocol appears well-calibrated (high R²) while producing systematically unreliable guidance under intervention. The regularity may generalize to any adaptive protocol component where the optimization pressure (historical data, logged interactions) is misaligned with the deployment distribution (policy shock, strategic deviation).
