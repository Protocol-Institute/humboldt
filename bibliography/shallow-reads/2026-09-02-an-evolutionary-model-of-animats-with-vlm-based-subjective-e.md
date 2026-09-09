# An evolutionary model of animats with VLM-based subjective evaluation

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.07537
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A genetic algorithm framework using Vision-Language Model (VLM) subjective evaluations ("adorably," "weirdly") as fitness criteria for evolving virtual soft robots. The work treats language-based aesthetic and behavioral descriptors as legible optimization targets in an evolutionary selection loop.

## What I took from it

This is a clean instantiation of L-004 (Goodhart Generalization) and L-008 (Proxy Optimization Under Computable Enforcement) operating in tandem, but the domain is narrow enough that it doesn't yet generalize beyond the specific case of aesthetic evolution. The paper demonstrates the mechanism: VLM judgments are *computable* (legible to the optimization loop), *substitutable* for ground-truth fitness (behavioral functionality is not measured directly), and *misaligned* with actual locomotor performance or energy efficiency — precisely the conditions under which proxy capture occurs. 

The work is competent but not theoretically ambitious. It presents a tool (VLM + GA) rather than a law or mechanism discovery. No sustained argument is offered about *why* this pattern generalizes, what breaks under scaling, or how the system would degrade if optimization pressure increased. The paper does not interrogate the brittleness of VLM-as-referee or the risk of adversarial morphologies that exploit language-model artifacts.

## Research connections

- **L-004:** VLM aesthetic descriptors are measurable proxies for unmeasurable behavioral goals (e.g., "fitness"); optimization against them is expected to produce Goodhart capture.
- **L-008:** The legibility of VLM judgments to the evolutionary algorithm creates a computable enforcement signal; the work does not explore whether this legibility itself becomes an optimization target independent of actual behavior.
- **seed-080:** VLM-provided fitness scores collapse under upstream asymmetry — the model's training distribution may not cover the space of evolved morphologies, creating silent failures.

## Seed

**Seed title:** VLM Evaluator Drift in Open-Ended Evolution

**Seed type:** question

**Seed text:** When a generative or language model is used as a legible fitness evaluator in an open-ended search process, the evaluator's judgments may drift away from the training distribution of the model, causing silent failure or adversarial capture. This is distinct from standard proxy capture — it is *evaluator capture*: the evolved system optimizes for output patterns that exploit the model's artifacts rather than the intended behavioral property. Does this pattern appear in any protocol system using adaptive models for evaluation, allocation, or enforcement, independent of whether the underlying objective is aesthetic, functional, or normative?
