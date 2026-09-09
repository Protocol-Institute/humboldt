# Socioeconomic Inference in LLM Medical Triage: Same Symptoms, Different ZIP Code

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.22605
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Empirical case study demonstrating that LLM medical triage systems alter clinical recommendations (ER referral rates) based on socioeconomic signals (explicit and implicit via ZIP code) while holding symptomatology constant. Tests three deployment-tier models across a fixed neurological symptom profile.

## What I took from it

This is a clean instantiation of **L-004 (Goodhart Generalization)** and **L-012 (Intervention-Layer Displacement)** within a safety-critical protocol, but at the level of demonstration rather than mechanism discovery. The paper shows that when clinical triage becomes a legible LLM prediction task, the optimization surface shifts: the model is being trained/evaluated on accuracy against some training corpus, but that corpus likely contains real-world co-correlations between SES and healthcare outcomes. The model captures the statistical correlation as a proxy for clinical urgency. Critically, this is *not* what the deployment protocol intended — the intervention layer (the triage recommendation) becomes subject to optimization pressures latent in the training data, displacing the actual decision locus away from symptom assessment toward SES inference.

However, the paper appears to be a straightforward empirical audit rather than a theoretical or mechanistic argument about why this pattern should generalize beyond LLM medical systems or what structural conditions produce it. It confirms existing laws without extending them.

## Research connections

- **L-004 (Goodhart Generalization):** The model optimizes a proxy (likelihood of hospitalization in training data) correlated with but distinct from the unmeasurable goal (appropriate triage given symptom severity). SES becomes the captured metric.
- **L-012 (Intervention-Layer Displacement):** Clinical decision authority shifts from symptom-based reasoning to latent SES inference baked into model weights. The legibility of the prediction task enables optimization against unintended targets.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** SES signals in the input asymmetrically predict training outcomes; the model treats SES as a legible proxy for something unmeasurable (true urgency or historical access patterns).

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Rationale for store-only:** The paper documents a known failure mode (metric capture in safety-critical AI systems) in a specific domain. It does not propose a novel mechanism, challenge existing laws, or argue why this pattern should generalize to non-LLM or non-medical protocols. It is evidence *for* L-004 and L-012, not an extension or complication of them. The case is important for safety engineering but does not advance the inventory of law-shaped fragments.
