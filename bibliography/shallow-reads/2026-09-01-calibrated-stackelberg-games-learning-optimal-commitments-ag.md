# Calibrated Stackelberg Games: Learning Optimal Commitments Against Calibrated Agents

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2306.02704
**Date read:** 2026-09-01
**Connected to:** L-010, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic model extending Stackelberg competition to settings where agents respond not to direct observation of a principal's action but to calibrated probabilistic forecasts of it. The paper develops learning algorithms for principals to compute optimal commitment strategies in this setting, treating forecast calibration as a constraint on strategic interaction rather than assuming ad hoc agent algorithms.

## What I took from it

The framework is technically sound and addresses a realistic constraint — agents often condition on predictions *about* actions rather than actions themselves — but the relevance to protocol-layer laws is indirect. The work operates within classical game theory's assumption of rational best-response, which is orthogonal to questions about how coordination signals propagate, fail to propagate, or trigger nonmonotonic adoption dynamics (L-010). The calibration constraint is a legibility constraint, but the paper does not examine what happens when calibration itself becomes a contested or manipulated signal, nor does it model how repeated cycles of commitment + forecast + response reshape the agent's forecast model itself. The mechanism of interest here is agent rationality under information asymmetry, not protocol ossification, metric capture, or coordination cost conservation.

## Research connections

- **L-010:** The model holds adoption monotonic at the equilibrium level (agents best-respond rationally to calibrated forecasts). L-010 predicts nonmonotonicity; this work provides no evidence for or against it — it assumes it away via the rationality assumption.
- **seed-048:** The commitment-to-forecast structure is a form of capability-cooperation inversion, but the paper does not examine whether repeated forecasting and response generates emergent decoupling between the forecast signal and the principal's actual behavior.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
