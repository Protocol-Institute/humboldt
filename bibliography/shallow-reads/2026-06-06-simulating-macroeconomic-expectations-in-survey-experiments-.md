# Simulating Macroeconomic Expectations in Survey Experiments with LLM-based Economic Agents

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2505.17648
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A validation study demonstrating that LLM-based agents can reproduce human macroeconomic expectation distributions across survey designs. The work constructs modular agents with personal characteristics, prior beliefs, and dynamic information access, then tests output fidelity against three representative human survey experiments.

## What I took from it

This is a methodological contribution to agent-based modeling in economics, not a theoretical intervention. The core claim—that LLMs can *approximate* human expectation formation when scaffolded with appropriate context modules—is empirically useful for simulation but does not reveal new mechanisms of how protocolized systems behave under constraint. The paper validates a tool for generating synthetic survey data, which is valuable for computational efficiency and experimental design iteration, but does not investigate what structural properties of LLMs make them capable (or incapable) of this approximation, nor does it interrogate failure modes or boundary conditions where fidelity breaks. The work assumes expectations are largely reconstructible from retrieval + prior state + external signal—a reasonable null, but one that doesn't probe the deeper question of whether artificial agents develop *different* expectation dynamics under different training regimes, scale, or architectural constraints.

## Research connections

- **Absent:** No established laws or active hypotheses currently exist in our inventory for this domain. This work is orthogonal to protocolized system behavior under conflict, emergence, or resource constraint.

## Candidate laws or signals

None. This is a validation of fidelity between one artifact class (LLM agents) and one human behavior class (survey responses), not a claim about how protocolized systems *behave differently* or under what conditions they diverge from human baselines. Useful for reproducibility of experiments, but not diagnostic of new nature structure.
