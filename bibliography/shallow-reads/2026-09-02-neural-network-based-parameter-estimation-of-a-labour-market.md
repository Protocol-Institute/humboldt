# Neural Network-Based Parameter Estimation of a Labour Market Agent-Based Model

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2602.15572
**Date read:** 2026-09-02
**Connected to:** L-005, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical paper on using neural network-based simulation-based inference (SBI) to estimate parameters in large-scale agent-based models, focusing on labour market simulation. The primary contribution is a methodological solution to computational bottlenecks in ABM calibration — replacing exhaustive parameter space exploration with learned surrogate mappings from summary statistics to parameter distributions.

## What I took from it

The paper illustrates a practical instantiation of L-005 (Gall Generalization) and L-006 (Coordination Cost Conservation) at the layer of model-to-reality alignment: ABMs that function acceptably resist reformulation or simplification because their parameter spaces have been calibrated through expensive exploration. The introduction of a NN surrogate doesn't eliminate this resistance — it *displaces* it. The calibration burden moves from direct simulation-space search to training data generation and surrogate validation. Functionally, the system remains locked to its prior parameter discovery pathway; introducing the NN layer adds a new verification cost (surrogate accuracy bounds) without removing the original ossification around the ABM structure itself.

The work confirms that computational constraint drives formalization (feeds L-003 pathway), but does not engage the deeper question: whether NN-mediated parameter estimation introduces new forms of latent-state coupling (seed-063) or proxy collapse (seed-080) when the surrogate's learned mapping diverges silently from true parameter-outcome relationships under out-of-distribution conditions.

## Research connections

- **L-005:** ABM systems that produce acceptable outputs resist restructuring; NN surrogates mask rather than resolve this — they add a layer of indirection without freeing the underlying model.
- **L-006:** Coordination cost between model and reality is conserved; it shifts from parameter-space search cost to surrogate-validation cost.
- **L-003:** Computational pressure drives formalization of informal ABM tuning into computable SBI pipelines.
- **seed-062 (Formalization Opacity Collapse):** Automation of calibration via NN may collapse interpretability of which parameter combinations matter; the model becomes harder to understand, not easier.

## Seed

**Seed title:** Surrogate Lattice Lock — Calibration Debt Displacement in Automated Model Inversion

**Seed type:** observation

**Seed text:** When parameter estimation in complex simulations is automated via learned surrogates (neural networks or other function approximators), the computational debt does not disappear — it is displaced to surrogate validation and accuracy certification. The original model's calibration pathway becomes invisible, frozen within the surrogate's learned weights. Under subsequent model revision, pressure to preserve surrogate accuracy can exceed pressure to improve underlying model fidelity, creating a new form of L-005-style resistance: the system resists not restructuring of the model itself, but decoupling from the surrogate it has been calibrated through. This may generalize to any protocol system where an expensive prior calibration is encoded into an opaque learned layer.
