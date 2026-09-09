# Legal aid eligibility and court outcomes: a design-based double-machine-learning approach

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2608.05211
**Date read:** 2026-09-02
**Connected to:** L-004, seed-018
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An econometric causal inference study using double machine learning to estimate the effect of legal aid eligibility (via means-testing) on court outcomes in New South Wales. The paper treats means-test assignment as a natural experiment to isolate treatment effects of private vs. public legal representation on acquittal/conviction rates.

## What I took from it

This is a *case study application* of causal inference method to a specific policy domain, not a sustained theoretical or empirical argument about how protocols behave under formalization. The means test itself is a *proxy measure* (ability to pay as surrogate for "legal indigence"), but the paper does not examine what happens *when that proxy becomes the optimization target* — i.e., whether defendants or courts learn to game the eligibility threshold, whether the formalization of "indigence" shifts behavior upstream, or whether the metric capture dynamics predicted by L-004 appear in this domain.

The paper measures an *outcome* (acquittal rates by eligibility status) but does not investigate the *mechanism of metric capture* — whether the legibility of the means test as a decision rule creates incentive distortions, strategic claiming behavior, or institutional gaming. It is descriptive causal inference, not a study of how formalization itself alters protocol behavior.

## Research connections

- **L-004:** The means test is a proxy for legal need, but this paper does not examine whether the proxy becomes an optimization target or whether its use as a computable eligibility rule triggers capture.
- **seed-018:** Mentioned in triage; likely concerns responsibility implication (who bears cost/blame when means test denies aid?), not mechanism of formalization effects.

## Method note

This represents sound econometric practice within its frame: causal inference on policy effects via administrative data linkage. However, it exemplifies a common pattern in policy evaluation research — measuring *outcome differences by policy regime* rather than *studying how the policy rule itself alters agent behavior and institutional structure*. For the new nature agenda, we need work that traces the *causal pathway through formalization*, not just the final outcome gap. This suggests meta-need: policy evaluation papers should be screened for whether they study policy *effects* (outcome differences) or policy *mechanisms* (how formalization restructures incentives and eligibility gaming).
