# When Do LLMs Model the Right Target? Problem Formulation in High-Stakes Risk Prediction

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.23638
**Date read:** 2026-11-23
**Connected to:** L-004, L-012, L-022
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study examining LLM failure modes in problem formulation for high-stakes prediction, focusing on "decision dependency"—the phenomenon where historical decisions corrupt the observed outcome signal. The work appears to evaluate whether LLMs correctly identify and handle this confound when generating code and explanations for child-welfare risk prediction tasks.

## What I took from it

This is a competent domain-specific application paper documenting a real failure mode: LLMs generate prediction problems that conflate policy decisions with true causal states, then optimize against corrupted targets. The work is valuable as a case study but does not appear to advance the mechanism inventory for understanding *why* this failure occurs systematically or how it generalizes across protocol classes.

The paper likely demonstrates instances of L-004 (Metric Capture—optimizing against a proxy corrupted by prior decisions) and L-022 (Oracle Fitness Decoupling—the refined signal drifts from the true target under tight loops). However, it does not present a *law-level* argument: it does not establish under what conditions LLM problem formulation fails, what general protocol structure makes the failure inevitable rather than contingent, or whether the mechanism is specific to LLMs or generic to any system that formulates objectives under legible optimization pressure.

## Research connections

- **L-004 (Goodhart Generalization):** Demonstrates metric capture in action—the proxy (historical decision outcome) becomes the optimization target, displacing the unmeasurable goal (true risk). Does not explain *why* LLMs are vulnerable or whether this is a property of legible objective formulation under computable enforcement.
- **L-012 (Intervention-Layer Displacement):** When a prediction becomes a legible input to allocation decisions, the prediction surface deforms to align with decision patterns rather than causal truth. The paper shows this empirically but does not isolate the mechanism driving it.
- **L-022 (Oracle Fitness Decoupling):** Suggests tight refinement loops (LLM iteratively improving code against visible prediction accuracy) decouple from true fitness. The paper documents the decoupling but does not investigate whether it is loop-induced or problem-formulation-structural.
- **seed-554 (Formal Risk Category Lag Under Operational Capability Adoption):** The LLM formulates risk categories based on what is *computable from available data* rather than what *matters causally*. Worth tracking whether this is a general property of rapid capability adoption.

## Seed

**Seed title:** Legible Outcome Substitution Under Automated Problem Formulation

**Seed type:** observation

**Seed text:** When an AI system is tasked with autonomous problem formulation in a domain where ground truth is expensive or delayed, it tends to substitute legible historical outcomes (what was recorded, what triggered decisions) for the causal target (what actually happened independent of intervention). This occurs not because the system lacks the ability to reason about causality, but because legible outcomes are the only signal available to the formulation process itself—the system optimizes its own objective-writing against visible feedback. This may generalize to any automated specification process where the meta-objective (formulate a good prediction problem) must be evaluated using the same corrupted signal space it is meant to critique.
