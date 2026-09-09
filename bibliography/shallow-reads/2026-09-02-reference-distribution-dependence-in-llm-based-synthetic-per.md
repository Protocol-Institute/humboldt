# Reference-Distribution Dependence in LLM-Based Synthetic Persona Data: Diagnosis and Post Hoc Adjustment of Demographic Distributions

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.28668
**Date read:** 2026-09-02
**Connected to:** L-004, L-008, seed-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical diagnosis paper measuring how synthetic persona distributions drift from reference demographic data in LLM-based generation. The work decomposes error into generator bias vs. reference-choice bias using total variation distance on Korean administrative microdata, proposing post hoc adjustment methods.

## What I took from it

The paper documents a specific instantiation of L-004 (Goodhart Generalization): when demographic parity becomes a legible, measurable optimization target in synthetic data generation, the system optimizes toward whichever reference distribution is supplied at generation time, not toward ground truth. The finding that "most observed error is attributable to choice of reference rather than generator" is precisely the proxy capture mechanism — the reference distribution *becomes* the goal once it is formalized as a metric.

This extends L-008 (Proxy Optimization Under Computable Enforcement) into the generative domain: when demographic legibility is computationally enforced as a training signal, the generator locks onto whatever reference is available, creating a new vector of gaming (reference selection) orthogonal to the original demographic fairness objective. The paper treats this as a technical problem amenable to post hoc adjustment; it does not theorize the deeper issue: that making demographic distributions computable and measurable may displace the optimization locus from actual fairness toward reference-matching, creating new forms of specification gaming at the input level.

## Research connections

- **L-004:** Direct instantiation; demographic parity as proxy for unmeasurable fairness goal; under optimization pressure (LLM generation), the system targets the legible reference distribution rather than the underlying fairness intent.
- **L-008:** Computable demographic legibility (reference distribution matching) becomes enforced signal; optimization pressure moves to selection and specification of that reference.
- **seed-019:** Reference distribution as proxy consensus mechanism; decoupling of generator behavior from ground truth under metric enforcement.

## Seed

**Seed title:** Reference-Legibility Lock in Generative Systems

**Seed type:** observation

**Seed text:** When a generative system is optimized against a measurable reference distribution (demographic, statistical, or structural), the system learns to match that reference with high fidelity, but this fidelity becomes independent of whether the reference is accurate or representative of the actual target population. The proxy (reference matching) becomes the stable attractor, and the original objective (real-world fairness or representativeness) detaches from the optimization surface. This creates a new failure mode: you can have high metric compliance and systematic bias simultaneously, with the bias locked in at the reference-selection stage, upstream of the generator. Generalizes beyond demography to any generative protocol where the training signal is conditioned on a formalized external distribution.
