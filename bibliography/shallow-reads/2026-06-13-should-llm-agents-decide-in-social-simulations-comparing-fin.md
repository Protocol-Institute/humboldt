# Should LLM Agents Decide in Social Simulations? Comparing Finite-State and LLM-Based Decision Policies

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2606.12369
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper comparing LLM-based and finite-state decision policies in online social network simulations. The work investigates whether LLMs preserve interpretable, researcher-specified behavioral policies or systematically deviate from them, framing this as a risk to simulation validity.

## What I took from it

This is a *transparency and fidelity audit*, not a theoretical or mechanistic investigation. The paper asks: does substituting a finite-state machine with an LLM decision layer break the experimental contract? This is important for simulation practice but does not engage with why or how LLMs deviate, nor does it establish a generalizable principle about artificial agent behavior under specification constraints.

The work implicitly surfaces a real tension in protocolized systems — the gap between intended and emergent policy — but treats it as a *methodological problem to solve* rather than a *phenomenon to understand*. There is no sustained argument about the conditions under which opaque agents preserve or violate constraints, no mechanistic account of deviation modes, and no evidence the findings generalize beyond OSN simulation contexts.

## Research connections

- None currently applicable; no established laws or active hypotheses in the inventory yet.

## Candidate laws or signals

none
