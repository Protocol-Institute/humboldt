# Fig: Automated Multiagent Behavior Elicitor

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.28891
**Date read:** 2026-11-23
**Connected to:** L-016, seed-023
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper presenting Fig, an agentic system that systematically elicits target behaviors from multiagent game environments by decomposing behavior descriptions into sub-behaviors and intervening on game rules, opponent behavior, and instructions. The work is methodological rather than theoretical — it demonstrates a technique for behavior engineering in controlled multiagent settings.

## What I took from it

The paper operationalizes automated intervention design but does not present a primary theoretical argument about how such systematic intervention affects protocol stability, coordination cost, or the emergence of informal workarounds. It sits downstream of L-016 (Normative Intervention Algorithmic Retraining Effect) rather than enriching it: the system *applies* normative interventions (rule changes, instruction rewrites, opponent retuning) but does not examine how the targeted agents adapt to, circumvent, or absorb these interventions over repeated cycles. The work confirms that behavior elicitation can be automated and decomposed, but leaves open the deeper question of whether systematic legible intervention creates new coordination surfaces or drives agents toward illegible (informal) strategies. This is a capability demonstration, not a law-gathering exercise.

The paper's connection to seed-023 (Informality as Novelty Sink Under Legible Optimization) is suggestive but underdeveloped: if Fig's interventions are legible and systematic, do agents in the resulting environment eventually discover informal workarounds that the intervention system cannot detect or formalize? The paper does not track this.

## Research connections

- **L-016:** Fig demonstrates automated intervention design but does not measure whether targeted agents develop adaptive counter-strategies or revert to informal coordination. No data on retraining effect magnitude.
- **seed-023:** Raises but does not answer whether systematic legible behavior elicitation drives novelty and informality underground, concentrating functional diversity in unmonitored channels.
- **L-012 (Intervention-Layer Displacement):** Fig's intervention system could exemplify how the locus of optimization pressure shifts when interventions become precise and legible, but this is not examined.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
