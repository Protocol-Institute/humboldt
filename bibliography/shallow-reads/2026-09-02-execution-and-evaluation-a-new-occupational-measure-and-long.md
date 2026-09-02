# Execution and Evaluation: A New Occupational Measure and Long-Run Employment Gradients

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2607.20807
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical labor economics paper that introduces a new occupational coding scheme distinguishing execution tasks (those AI can perform) from evaluation tasks (judging correctness), applied to 19,265 O*NET task statements. The main claim is that this execution–evaluation split predicts employment exposure differently than existing measures (routine-task intensity, AI capability scores), and that it is reproducible across model coders and dataset versions.

## What I took from it

The paper provides a **domain-specific instantiation** of L-012 (Intervention-Layer Displacement): when the prediction of which tasks are automatable becomes a legible input to labor market and hiring decisions, optimization pressure shifts away from what genuinely matters (whether the output is *correct*) toward what is *measurable* (whether the execution is automatable). The execution share becomes a proxy for exposure, but the measure inherently privileges legibility of production over legibility of verification.

This confirms the asymmetry claimed in L-012 but does not explain the *mechanism* by which labor markets internalize and act on this proxy, nor does it track what happens downstream when agents optimize for high execution share (e.g., task redesign, role bundling, or hollowing of evaluation). The paper treats the measure as descriptive; it does not examine whether the distinction between execution and evaluation itself becomes institutionalized or whether the measure *creates* the labor-market behavior it claims to predict.

## Research connections

- **L-004 (Goodhart Generalization):** The execution share is a proxy for exposure to automation (the unmeasurable goal being "economic vulnerability to displacement"). Under sufficient optimization pressure from policy, education, and hiring, the measure risks capturing what is legible rather than what is consequential.

- **L-012 (Intervention-Layer Displacement):** The formalization of "execution vs. evaluation" as a computable occupational attribute relocates optimization pressure from outcomes (correctness, value) to legible inputs (automatable task performance). Labor markets and policymakers may then optimize for the proxy.

- **seed-073 (Correlated Failure Under Proxy Consensus):** If the execution–evaluation distinction becomes consensus among labor economists and HR systems, multiple institutions will optimize on the same proxy, creating correlation in failure modes (e.g., mass bundling of evaluation tasks into roles that become unmatchable to workers).

- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** The measure assumes executability and evaluability are independent; if AI advances in evaluation asymmetrically (e.g., model-grading systems), the upstream distinction collapses and the occupational measure loses discriminative power.

## Seed

**Seed title:** Execution–Evaluation Legibility Inversion in Labor Markets

**Seed type:** observation

**Seed text:** When task automata are classified by execution legibility (whether AI can perform the task) rather than evaluation legibility (whether AI can verify correctness), institutional actors optimize hiring, education, and job design around the legible dimension. This creates a ratchet: as execution share becomes a standard occupational measure, labor markets treat it as a ground truth of vulnerability, even though it is a proxy for a mismatch between what is easily predicted and what is consequential. The measure itself may drive task bundling and role hollowing that increases actual evaluation opacity while appearing to increase automata-readiness. This generalizes beyond labor to any domain where a protocol introduces a proxy for human judgment and agents gain access to that proxy before gaining access to mechanisms for verifying the proxy's fidelity.
