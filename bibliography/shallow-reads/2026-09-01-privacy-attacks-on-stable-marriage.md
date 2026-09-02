# Privacy Attacks on Stable Marriage

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.13015
**Date read:** 2026-09-01
**Connected to:** L-002
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A mechanism design security paper demonstrating privacy attacks on the stable marriage algorithm under repeated interaction. The work shows that when an attacker (e.g., hospitals) can query the algorithm multiple times, they can infer private preference information through differential analysis of outputs. The domain is mechanism design and privacy-preserving algorithms.

## What I took from it

This is a competent application of differential privacy analysis to a classic mechanism design problem, but it operates entirely within the *specificity* of the stable marriage protocol. The attack pattern—repeated querying to extract latent preferences—is well-established in privacy literature and does not generalize a novel constraint on protocol classes.

The connection to L-002 (Hardness Asymmetry) is real but limited: the paper confirms that *verification* of outcome fairness (a matched pair is stable) is computationally trivial, while *privacy preservation* during execution is hard—but this is a restatement of the standard privacy-computation tradeoff, not a new discovery about protocol asymmetries. The attack requires the attacker to already control one side of the market (hospitals), which is a domain-specific assumption, not a generalizable protocol condition.

## Research connections

- **L-002:** Confirms verification-execution asymmetry in mechanism design, but as a special case of privacy-computation hardness, not a novel structural principle.
- **L-004:** Tangentially: preference elicitation as proxy for true preference creates optimization target for attack, but this is incidental to the mechanism design framing, not a generalization about metric capture.
- none (open lines)

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
