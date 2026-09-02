# IyawoBench v2.0: Extended Diagnostic Evaluation of Large Language Model Clinical Triage in Nigerian Primary Care

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.29085
**Date read:** 2026-09-02
**Connected to:** L-004, L-007
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A diagnostic evaluation paper demonstrating that LLM-based clinical triage systems achieve high scores on standard binary safety metrics ("did not send an emergency home") while exhibiting systematic failure modes that render them undeployable. The work is a case study in measurement capture within safety-critical protocols, not a primary theoretical or empirical argument about the mechanism itself.

## What I took from it

This is a direct empirical confirmation of **L-004 (Goodhart Generalization)** in a safety-critical domain: the metric that was optimized for (binary triage safety) becomes decoupled from the actual goal (reliable clinical judgment). The paper documents the classic pattern—models achieve 100% on the proxy while failing systematically on unmeasured dimensions (severity stratification, confidence calibration, rare-case handling).

The work also touches **L-007 (Trust Ratchet)**: the high metric scores generate institutional confidence and deployment pressure, even as the underlying system remains unsafe. However, the paper does not investigate *why* this trust persists after evidence of failure accumulates—it documents the failure but does not explore the institutional mechanisms that keep the system deployed despite growing anomaly evidence. This suggests a connection to **L-013** (Paradigm-Locked Anomaly Tolerance), but the paper does not engage with that level of analysis.

The paper is competent diagnostic work but remains within the case study domain. It does not propose a generative mechanism for why proxy capture occurs specifically under safety-critical pressure, nor does it test whether the pattern holds across different protocol classes.

## Research connections

- **L-004:** Direct confirmation of metric capture in safety-critical clinical protocols; demonstrates that binary safety proxies become decoupled from unmeasured failure modes under optimization pressure.
- **L-007:** Suggests that trust in the system may accumulate despite evidence of systematic failure, but does not investigate the institutional or cognitive mechanisms.
- **L-013:** Hints at paradigm-locked anomaly tolerance (high metrics suppress urgency to restructure), but remains observational rather than mechanistic.
- **seed-068 (Unmeasurability as Anomaly Insulation):** The paper shows that unmeasurable dimensions of clinical judgment remain hidden from optimization, creating a class of failures that standard metrics cannot surface.

## Seed

**Seed title:** Safety-Metric Decoupling Under Clinical Deployment Pressure

**Seed type:** observation

**Seed text:** In safety-critical protocol systems where the goal is multidimensional (clinical safety + discrimination + confidence calibration) but the deployment metric is univariate (binary emergency detection), optimization toward the metric produces systems that score high on the proxy while failing systematically on unmeasured safety dimensions. The gap widens under adoption pressure because once high metric scores are achieved, institutional and technical pressure to deploy the system increases, reducing incentive to investigate unmeasured failure modes. This may generalize: whenever a safety-critical protocol reduces its observable surface to a small set of legible metrics, the unmeasured dimensions become immune to feedback and accumulate latent failure modes.
