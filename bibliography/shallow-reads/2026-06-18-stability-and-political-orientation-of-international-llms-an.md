# Stability and Political Orientation of International LLMs: An Exploratory Multi-Run Study Conducted in French

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.13760
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study measuring political response consistency across 11 LLMs via repeated runs (n=20 each) using a standardized French-language questionnaire adapted from Political Compass methodology. The work maps intra-model variability and ideological positioning but does not advance a sustained theoretical argument about the mechanisms underlying instability or propose a generalized law of artificial system behavior.

## What I took from it

This is a measurement study in the emerging domain of LLM behavioral stability, but it operates at the descriptive level. It documents *that* variance exists across runs and *where* models cluster ideologically, but the abstract does not indicate mechanistic explanation or abstraction to a principle that would generalize beyond language models or political elicitation.

The French-language choice and multi-model comparison are methodologically sound but localize findings to a specific cultural-linguistic domain, limiting immediate generalizability. The multi-run protocol is good practice for detecting stochasticity, but without analysis of why variance occurs (temperature effects, sampling artifacts, training data properties, architectural features) or how to predict or control it, the contribution remains observational rather than theoretical.

## Research connections

- **Stability in protocolized systems:** The work documents variability in deterministic-appearing outputs but does not engage with whether this is a fundamental property or an artifact of deployment parameters.

## Candidate laws or signals

- **CL-2606.13760-A:** LLMs exhibit run-to-run variability in political response patterns even under identical prompting, but variability magnitude and direction differ by model and language, suggesting that instability is neither universal nor arbitrary—a precondition for identifying causal mechanisms.
