# Predictors and Orchestrators: Parsimonious Machine Learning within an Agentic AI Harness for Multi-Horizon Karst Aquifer Forecasting

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.22251
**Date read:** 2026-09-22
**Connected to:** L-012, seed-138
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A domain-specific hydrology forecasting system that deploys multiple ML model families (XGBoost, ExtraTrees, LSTM, CNN) in an agentic orchestration harness for multi-horizon aquifer prediction. The paper evaluates model parsimony, interpretability, and deployment constraints against 79 years of Edwards Aquifer observational data.

## What I took from it

The system presents a clean case of **prediction-layer formalization feeding into orchestration decisions** (the "agentic harness"), but the paper appears to be a straightforward ML application study rather than an investigation of what happens when this formalization becomes a legible optimization target for downstream agents. The triage note correctly identified L-012 adjacency — the prediction signal is becoming an input to an automated decision layer — but the paper itself does not interrogate how agents respond to or strategically engage with the predictive interface. The work is technically competent and deployment-aware, but it does not sustain an argument about *mechanism* (how prediction legibility reshapes behavior or protocol structure). It documents a system, not a regularity.

The "agentic AI harness" framing in the title is somewhat aspirational: the paper describes model selection and ensemble weighting, not multi-agent interaction dynamics or the emergence of unintended coordination patterns that would drive L-012 or seed-138.

## Research connections

- **L-012:** Prediction formalization as input to decision protocol is present, but the paper does not examine whether optimization pressure migrates from aquifer dynamics to the prediction surface itself.
- **seed-138:** Intent legibility (what the forecasting system is optimizing for) is stated but not treated as a coordination target or locus of strategic behavior.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
