# Measuring Judgment Quality in Natural-Language Explanations: Evidence from Forecasting Tournaments

**Source:** arXiv.org — https://arxiv.org/abs/2606.30987
**Date read:** 2026-09-01
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A measurement paper introducing Explanation Quality Markers (EQMs)—sixty LLM-scored reasoning patterns applied to 55,000+ forecast-rationale pairs from forecasting tournaments. The work treats explanation quality as measurable via pattern extraction rather than holistic evaluation, enabling scale analysis of judgment-explanation pairs against realized outcomes.

## What I took from it

This is a tool paper for *measuring* explanation quality, not a primary source establishing or challenging a law about how explanations function in decision protocols. The contribution is methodological: it makes explanation quality computable and legible to downstream optimization. 

The connection to L-012 (Intervention-Layer Displacement) is real but inverted: the paper *creates* a new legible intervention layer (the EQM scores) that can itself become an optimization target. The question whether forecasters subsequently optimize *for EQM markers* rather than *for judgment accuracy* is unaddressed. Similarly, the framing assumes explanation quality can be proxied by pattern markers—a direct instance of proxy risk (L-004)—but the paper does not investigate whether optimizing forecasters learn to generate high-EQM rationales independent of forecast accuracy.

The forecasting tournament context is relatively clean because outcomes are legible and delayed, reducing immediate Goodhart capture. But it is not clear whether the pattern holds when explanations must satisfy multiple audiences (risk managers, auditors, end-users) with misaligned preferences.

## Research connections

- **L-004 (Goodhart Generalization):** The EQMs are measurable proxies for unmeasurable explanation quality; the paper does not test whether forecasters optimize the markers rather than the underlying judgment.
- **L-012 (Intervention-Layer Displacement):** EQMs create a new computable layer for evaluation; whether this becomes an optimization target independent of forecast accuracy is unexamined.
- **seed-019 (Embedded Explanation Opacity):** LLM scoring of human explanations introduces a new opacity layer—the model's feature extraction is not transparent to the forecaster or end-user.

## Seed

**Seed title:** Explanation-Marker Decoupling Under Scaled Legibility

**Seed type:** question

**Seed text:** When explanation quality is rendered computable via pattern extraction and fed into decision workflows as a legible signal, does forecaster behavior bifurcate—optimizing for marker conformity independent of judgment accuracy? In forecasting tournaments, outcome feedback is delayed and outcome-tied, suppressing this risk. But in advisory or recommendation settings where explanation markers feed directly into trust or selection decisions, markers may become decoupled from the reasoning they ostensibly measure. The generalization: any protocol that makes reasoning *legible* without making it *verifiable* creates a new optimization surface orthogonal to the original goal.
