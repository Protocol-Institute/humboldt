# Responsibility in Multi-Agent Sequential Decision-Making: Comparing Human Judgments to Formal Models of Causal Attribution

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.04318
**Date read:** 2026-09-02
**Connected to:** L-018, seed-018
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical survey paper comparing formal causal attribution models (grounded in actual causality frameworks) against human responsibility judgments in multi-agent sequential decision scenarios. The work measures alignment/misalignment between computable responsibility protocols and human intuition in high-stakes settings.

## What I took from it

This is a diagnostic paper on a core failure mode: the gap between formalized responsibility assignment and human judgment under distributed agency. It directly probes whether rendering causality and responsibility "legible" through formal causal models produces protocols that preserve the normative content humans expect.

The work is relevant to **L-012** (Intervention-Layer Displacement) and **L-015** (Interpretive Continuity Decay) — it tests whether formalizing causal attribution as a computable input to governance protocols causes optimization pressures or interpretive drift. It also bears on **seed-069** (Transparency-Legibility as Trust Proxy Substitution) and **seed-072** (Explanation-Marker Decoupling Under Scaled Legibility): does making causal chains formally legible substitute for actual normative alignment?

The paper's likely finding — misalignment between formal and human models — is important not as a failure of the formal system, but as evidence that responsibility assignment may be **unmeasurable** in the sense that drives **seed-068** (Unmeasurability as Anomaly Insulation): systems that rely on formal causal attribution may systematically tolerate failures of legitimacy while remaining internally auditable.

## Research connections

- **L-012:** Formalizing causal attribution as computable input to responsibility protocols risks displacing optimization pressure upstream into attribution model design rather than actual accountability.
- **L-015:** Formal audit traces of causal chains can survive intact while the institutional meaning of responsibility decays.
- **seed-068:** Responsibility may be an unmeasurable goal; computable causal proxies may insulate protocol systems from detecting normative failures.
- **seed-069:** Formal causal transparency may substitute for trust without preserving its functional role.
- **seed-072:** Explanations of causality may decouple from markers of responsibility under scaled automated systems.

## Method note

This paper demonstrates the value of systematic human-judgment calibration as a diagnostic tool for protocol design. Rather than assuming formal models of causality are correct and then scaling them, the work creates a measurement baseline for misalignment — a prerequisite for detecting whether formalization introduces systematic drift. The meta-lesson: when designing protocols for high-stakes domains (governance, safety, accountability), run empirical human-judgment surveys early to establish whether the formal model is *capturing the right thing*, not just whether it's internally consistent. This is particularly important for unmeasurable goals where the formal model may be elegant but hollow.
