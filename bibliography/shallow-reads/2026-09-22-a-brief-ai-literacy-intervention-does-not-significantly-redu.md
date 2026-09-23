# A Brief AI Literacy Intervention Does Not Significantly Reduce Over-Reliance and Increases Under-Reliance on ChatGPT: A Randomized Study

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2503.10556
**Date read:** 2026-09-22
**Connected to:** L-016, seed-129
**Kind:** empirical intervention study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A randomized controlled trial measuring whether AI literacy training reduces over-reliance on LLM outputs in high school students solving math problems. Students in the intervention group received explanation of LLM mechanics and limitations; both groups then solved puzzles with deliberately incorrect ChatGPT advice in 50% of trials. The study finds the intervention neither significantly reduces over-reliance nor improves calibration, and reports a swing toward under-reliance (overcorrection).

## What I took from it

The paper documents a *non-monotonic response to legibility intervention* in human-AI coordination: making the protocol mechanism and failure modes more transparent does not produce the expected calibrated reliance. Instead it produces a bimodal outcome—some agents lock into over-trust, others swing to under-trust—suggesting that legibility itself becomes a coordination target rather than a correction mechanism.

This is consistent with seed-129 (Legibility-Induced Conformity Locking) but inverts the prediction: the intervention was designed to *break* lock-in by adding information, yet the heterogeneous response implies that formalized knowledge of LLM limitations does not reduce the salience of the reliance decision boundary. The study does not investigate *why* the intervention fails—it offers no mechanism for the non-effect or the under-reliance swing. This leaves open whether the failure is due to: (a) insufficient legibility depth (students still cannot *operationalize* the knowledge), (b) legibility-induced bifurcation (knowledge creates two stable equilibria rather than one corrected equilibrium), or (c) intervention-layer displacement (the salient cue shifts from "know how LLMs work" to "was I taught to distrust this").

## Research connections

- **L-016 (Normative Intervention Algorithmic Retraining Effect):** The intervention is normative (prescriptive knowledge about good reliance practices) applied to a guidance-receiving system (ChatGPT as advice). The failure to shift behavior toward calibration suggests intervention-induced retraining away from the target norm, though the mechanism is opaque.

- **seed-129 (Legibility-Induced Conformity Locking):** The intervention increases legibility of LLM failure modes, yet reliance behavior *bifurcates* rather than converges. Suggests that legibility can stabilize multiple equilibria rather than break a single lock.

- **seed-144 (Informality as Coordination Cost Refuge Under Substitution Pressure):** The study does not measure whether students *disregard* the formal literacy training and revert to intuitive reliance heuristics when facing time pressure or uncertainty.

## Seed

**Seed title:** Normative Transparency as Bifurcation, Not Calibration

**Seed type:** observation

**Seed text:** In human-AI coordination protocols, explicit training in the agent's limitations and correct usage strategy produces bimodal rather than unimodal response distributions—some agents increase reliance (ignoring the warning), others over-correct to under-reliance (treating the warning as a legible reason to distrust). The intervention does not calibrate reliance; it creates two stable equilibria. This suggests that legibility of mechanism does not map to behavioral correction when the coordination target is *subjective* (appropriate reliance) rather than *legible* (rule-following). The bifurcation may persist because the formal knowledge becomes a boundary signal itself—"I was trained to be skeptical"—rather than actionable constraint on reliance choice.
