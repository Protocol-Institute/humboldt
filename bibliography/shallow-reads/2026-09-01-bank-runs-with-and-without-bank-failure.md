# Bank Runs With and Without Bank Failure

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2601.20285
**Date read:** 2026-09-01
**Connected to:** L-010, seed-020
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Historical empirical study using NLP on newspapers to construct a dataset of 3,984 U.S. bank runs (1863–1934). Establishes that runs occur in both weak and strong banks, but failure is concentrated among weak banks; runs are triggered by macroeconomic news, not just idiosyncratic weakness.

## What I took from it

The paper documents a critical decoupling: *coordination signals (bank-run behavior) are not reliable indicators of the target's true state*. Depositors coordinate on withdrawal (a protocol-level cascade) in response to two distinct triggers: (a) genuine weakness, and (b) negative macro news. The outcome—failure vs. survival—depends on fundamentals independent of the run itself. This is a clean instance of **symptom hierarchy displacement** (seed-020): the observable coordination event (run) is not causally primary; it can occur in strong banks and fail to cause failure. The protocol (fractional-reserve banking + information asymmetry) creates a coordination adoption nonmonotonicity (L-010) where agents condition on *signals from the financial ecosystem*, not on direct bank valuation.

This also illustrates a mechanism that may generalize to modern automated systems: **when verification is asymmetric and costly, agents optimize on legible signals (macro news, contagion) rather than on ground truth (bank solvency)**. The run is a rational response under information constraints, but the signal carries noise. In today's machine-learning pipelines, this becomes acute: cascades can be triggered by upstream model failures or distribution shifts that don't reflect true system state.

## Research connections

- **L-010:** Adoption nonmonotonicity confirmed: runs adopt nonmonotonically as a function of depositor beliefs about *other depositors' behavior* and macro conditions, not monotonically on bank health.
- **seed-020:** Symptom hierarchy displacement: the observable symptom (run) and the underlying disease (insolvency) are decoupled; runs occur in healthy banks; strong banks survive runs.
- **L-008 (exploration):** Early signal: when enforcement is legible (deposit withdrawal is mechanically computable), agents optimize on available macro legibility rather than private fundamentals, creating a proxy for systemic risk that feeds back into systemic risk itself.

## Seed

**Seed title:** Legible-Signal Cascade in Asymmetric-Verification Protocols

**Seed type:** motif

**Seed text:** In protocols where agents must coordinate under asymmetric information and verification is costly, observable cascades (runs, withdrawals, exits) can be triggered by legible upstream signals (macro news, contagion reports) that are only weakly coupled to ground truth about the target system. The cascade is a rational response to information constraint, but it creates a self-reinforcing feedback loop independent of the signal's predictive validity. This pattern should generalize beyond banking to any multi-agent protocol where (a) individual agents lack direct verification, (b) macro or systemic signals are highly legible, and (c) individual decisions are contingent on coordination beliefs. Modern ML recommendation and allocation systems exhibit this structure: cascades of preference or allocation can be triggered by upstream model outputs that carry high noise but high legibility to downstream optimizers.
