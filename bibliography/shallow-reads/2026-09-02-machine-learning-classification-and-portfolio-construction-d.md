# Machine Learning Classification and Portfolio Construction: Does the Loss Function Matter?

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2108.02283
**Date read:** 2026-09-02
**Connected to:** L-004, seed-045
**Kind:** empirical application
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical finance paper comparing classification vs. regression loss functions in machine learning portfolio construction. The work shows that classification-based models substantially outperform regression-based models (Sharpe ratio 1.83 vs. 1.11) on the same underlying data and architectures, and that this outperformance persists across model families, subsamples, and after transaction costs.

## What I took from it

This is a narrow domain application of L-004 (Goodhart Generalization: Metric Capture), but it does not advance the law itself. The paper demonstrates that *choice of loss function* — the proxy used to train the model — significantly alters real-world outcomes, consistent with L-004's prediction that optimization under a measurable proxy distorts behavior. However, the mechanism here is standard: classification loss (binary/multiclass formulation) happens to be better-calibrated to the actual goal (portfolio excess return) than regression loss is, so the model trained on the "better" proxy performs better. This is optimization working *correctly*, not capture working insidiously.

The work confirms that metric choice matters, but offers no insight into the *pathological* capture dynamics L-004 targets — where optimization pressure gradually erodes the fidelity of the proxy to the unmeasurable goal, producing systematic deception or value collapse. This is a case where the proxy was simply chosen poorly ex ante, then correctly optimized. No feedback loop, no institutional lock-in, no causal chain between optimization and metric-goal decoupling over time.

## Research connections

- **L-004:** Demonstrates metric choice sensitivity in optimization, but does not address the erosion of proxy-goal fidelity under sustained optimization pressure that L-004 targets.
- **seed-045:** Related to proxy effectiveness in financial modeling, but does not explore how proxies degrade or diverge from true objectives as agents adapt to them.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
