# How optimistic inflow forecasts distort dispatch, prices, and contracts in hydro-dominated power systems: evidence from Brazil

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.00504
**Date read:** 2026-09-01
**Connected to:** L-004, L-013
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study of how systematic bias in a measurable input (inflow forecasts) propagates through an operational dispatch protocol and market pricing mechanism in Brazil's hydrothermal system. The work documents the mechanism and downstream consequences but does not present a primary theoretical argument or challenge existing law inventory.

## What I took from it

This is a clean application domain for L-004 (Goodhart Generalization: Metric Capture), showing how a proxy metric—the inflow forecast—becomes optimized under the constraints of a centralized planning model, with the optimization pressure distorting both the forecast itself and the dispatch decisions that depend on it. The case also touches L-013 (Paradigm-Locked Anomaly Tolerance), suggesting that the Brazilian system continued to treat optimistically biased forecasts as valid inputs despite persistent, observable evidence of systematic error.

The paper is valuable for *confirming* the mechanics of metric capture in a real infrastructure protocol, but it does not generalize the mechanism beyond the hydro domain or reveal a new structural principle. It is a domain-specific instance of a law already under accumulation.

## Research connections

- **L-004:** Direct exemplification—inflow forecasts as measurable proxy for unmeasurable future water availability; optimization pressure on the proxy degrades dispatch and pricing fidelity.
- **L-013:** Evidence that the protocol system tolerated accumulating forecast error signals without triggering structural review or re-parameterization.

## Seed

**Seed title:** none
