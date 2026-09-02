# Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.15095
**Date read:** 2026-09-02
**Connected to:** L-010, seed-053
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A multi-agent simulation framework using LLM agents to model political coalition formation, addressing the problem that standard RLHF-trained models lack the ideological persistence needed to sustain partisan behavior. The authors combine SFT and other alignment techniques to produce agents capable of stable coalition dynamics, then audit emergent collusion patterns.

## What I took from it

This is a tool/benchmark paper that documents a technical engineering problem (RLHF neutrality bias preventing partisan consistency) and solves it via fine-tuning. The coalition formation dynamics being simulated are the substantive output, but the paper itself does not present a primary theoretical argument about coalition formation laws, nor does it systematically investigate why adoption patterns, coordination signals, or protocol-level constraints affect coalition stability across domains.

The work is relevant to L-010 (Coordination Adoption Nonmonotonicity) insofar as it tests coalition formation under symmetric agent conditions, but the paper does not isolate or measure nonmonotonic adoption curves, nor does it investigate what protocol features induce oscillation or threshold effects in coordination success. It observes emergent behavior but does not theorize the mechanism.

The audit component is competent but does not generalize beyond LLM agent behavior — it is specific to the bias pathologies of a particular model class.

## Research connections

- **L-010:** Conducts coalition formation experiments under symmetric agent setup, but does not isolate adoption nonmonotonicity as a focal phenomenon or vary protocol structure to test threshold effects.
- **seed-053:** Relevant to emergent collusion observation, but collusion is outcome, not mechanism interrogation.

## Seed

**Seed title:** none
