# Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2606.17397
**Date read:** 2026-09-01
**Connected to:** L-012, L-016, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A field experiment on a Japanese gig-work platform (Timee) studying how recommendation algorithms allocate worker attention to job templates. The authors identify a failure mode: optimizing for prediction accuracy (worker favoriting) creates concentration on popular but low-supply templates, misaligning recommendations with actual labor demand.

## What I took from it

This is a tight empirical case of L-012 (Intervention-Layer Displacement in Automated Decision Protocols): the prediction layer (what workers will favorite) becomes decoupled from the coordination problem it was meant to serve (matching workers to available shifts). The algorithm optimizes the *legible* signal—favoriting—rather than the *underlying goal*—efficient labor allocation. This is mechanically similar to L-004 (Goodhart Generalization), but the paper's contribution is showing that the misalignment emerges *specifically* when predictions become formalized as the decision input, shifting optimization pressure away from ground truth.

The intervention result (they test exposure interventions to correct the misdirection) is competent but incremental: showing that you can patch the symptom by reweighting recommendations doesn't establish a law about why the problem arises or how it generalizes. The paper treats this as a design problem, not a protocol problem.

## Research connections

- **L-012:** Clean example of prediction-as-decision-layer creating optimization displacement; the legible signal (favorite likelihood) diverges from the actual coordination need (shift availability). 
- **L-016:** If Timee implements algorithmic retraining to correct the concentration, it may inadvertently create new optimization targets that workers or firms learn to game; the seed here is observation, not mechanism proof.
- **seed-020:** The symptom hierarchy shows: workers see symptoms (few shifts in favorites), Timee sees symptoms (concentration on low-supply templates), but the root sits at the prediction-decision boundary. Interventions at the recommendation layer treat coordination failure as a tuning problem.

## Seed

**Seed title:** Prediction-legibility asymmetry in demand-constrained allocation

**Seed type:** observation

**Seed text:** In allocation protocols where supply is genuinely scarce and intermittent (short-lived job slots), optimizing the prediction accuracy of user preference (what users will engage with) can systematically drift away from optimizing supply-demand matching. The prediction target becomes legible and computable; the ground truth (whether a job slot will actually exist when the user acts) is not. This creates a stable decoupling: platforms can improve recommendation metrics without improving allocation efficiency. The pattern may generalize to any protocol where prediction is used as a decision input in a system with endogenous, time-varying scarcity.
