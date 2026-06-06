# The Dynamic and Endogenous Behavior of Re-Offense Risk: An Agent-Based Simulation Study of Treatment Allocation in Incarceration Diversion Programs

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2601.12441
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source introducing a mechanistic model of feedback between algorithmic allocation decisions and endogenous risk evolution; generalizable framework for understanding how protocolized systems reshape their own input distributions.

## What this is

An agent-based simulation study that models recidivism risk not as a static individual trait but as a *dynamic property emergent from human-system interaction*. The paper constructs a computational framework linking treatment allocation algorithms to social interaction effects, showing how prioritization decisions reshape risk landscapes over time.

## What I took from it

This work directly instantiates a critical absence in standard algorithmic fairness and risk assessment research: the recognition that *systems do not merely measure and allocate based on fixed states; they alter the state distribution they subsequently measure*. The paper's core move—modeling reoffending risk as endogenous to treatment assignment and social reintegration dynamics—exposes a feedback loop invisible in static risk models. This is a protocolized system exhibiting what we might call *self-modifying input distributions*: the algorithm's allocation decisions change the very population characteristics it was designed to assess, creating potential cycles of under-treatment, escalation, or conversely, unexploited intervention opportunities.

The agent-based approach is methodologically significant because it allows the researchers to isolate mechanisms of feedback that regression-based approaches typically smooth over. If the simulation results hold, this suggests a broader principle: **any algorithmic allocation system operating on a population where the allocation itself shapes future measured attributes will exhibit endogenous instability or hidden optimization surfaces unavailable to static models.**

## Research connections

- **Feedback systems in protocolized environments:** Systems that allocate based on measured state but alter future state through allocation create recursive dependency structures fundamentally different from exogenous-shock models.

## Candidate laws or signals

- **CL-2601.12441-A:** Algorithmic prioritization systems operating on human populations exhibit self-modifying input distributions; risk/outcome measures become endogenous to allocation history, invalidating static predictive assumptions and creating latent optimization surfaces.

- **CL-2601.12441-B:** Treatment allocation algorithms in systems with social interaction dynamics (networks, reintegration cohorts, peer effects) necessarily generate non-linear feedback; marginal allocation decisions can have multiplicative effects on population-level risk evolution.
