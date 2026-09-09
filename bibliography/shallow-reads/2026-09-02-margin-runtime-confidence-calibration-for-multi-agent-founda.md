# MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.22949
**Date read:** 2026-09-02
**Connected to:** L-008, L-012, seed-053
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper addressing calibration of self-reported confidence signals from heterogeneous foundation models in a coordinated multi-agent deployment. The work proposes runtime correction of per-model confidence via online learning from deployment outcomes, enabling a coordinator to adaptively weight responses without model retraining or privileged access.

## What I took from it

This is a **competent engineering contribution** that sits at the edge of L-008 and L-012 territory but does not sustain a theoretical argument about the mechanism itself. The paper solves a real problem: foundation models produce incomparable confidence signals, and these become unreliable under distribution shift. By making confidence calibration legible and optimizable at deployment time, the work *instantiates* the condition space for proxy optimization under computable enforcement (L-008) — but it does not interrogate what happens when agents or downstream processes begin optimizing *against* the calibration signal, nor does it explore the feedback loops that arise when the coordinator's weighting becomes itself a legible optimization target.

The work treats confidence calibration as a technical fix, not as a new coordination surface. It does not examine whether runtime legibility of model reliability creates new failure modes, strategic incentives, or drift in model behavior (e.g., whether models learn to game the calibration signal if deployed long enough). The paper is silent on whether calibration collapse or signal divergence emerges under adversarial or self-interested agent setups.

## Research connections

- **L-008:** Instantiates the condition (computable, legible enforcement signal + online optimization) but does not study the downstream effects of optimization pressure or signal capture.
- **L-012:** Shows prediction legibility (model confidence) made formal and legible to a decision protocol (coordinator weighting), but does not track whether the locus of optimization pressure shifts or whether the confidence signal itself becomes a target.
- **seed-053:** Related to trust legibility inversion — confidence becomes a computable proxy for trustworthiness, but the paper does not examine whether this proxy decouples from actual reliability under pressure.

## Seed

**Seed title:** none

---

**Reason:** The paper presents a working solution to a real problem but does not surface a generalizable regularity about how legible confidence signals behave under optimization pressure, how they drift, or what equilibria emerge when multiple agents can condition on them. It does not challenge or extend any current law, introduce a mechanism absent from the inventory, or sustain a theoretical argument. It is a tool paper with valuable operational insights but no candidate law-shaped fragment that warrants tracking across domains.
