# Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled Beam Arbitration for Strict Zero-Shot Image Captioning

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.28986
**Date read:** 2026-09-02
**Connected to:** L-004, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A method paper proposing multi-agent scoring and consensus arbitration for zero-shot image captioning. The work improves decoder grounding by introducing multiple independent alignment scorers that vote on beam candidates, replacing single-pass scoring with consensus-distilled selection. Domain: vision-language generation under frozen pretrained models.

## What I took from it

The paper instantiates a legible proxy problem at the intersection of L-004 and L-012. By rendering alignment scoring *explicitly computable and multi-agent voteable*, the method makes the "goodness" signal machine-readable and optimizable. This is not incidental — the entire contribution depends on consensus being both legible and decisive. 

However, the paper does not investigate what happens when agents (scorers) optimize for the consensus signal itself rather than the underlying task. It treats consensus as a transparent aggregation mechanism, not as a new optimization surface. This is a gap: once multiple agents score alignment legibly, their collective signal becomes a target for gaming — individual scorers may drift toward producing scores that cluster with others (consensus capture) rather than accurate alignment assessment. The method assumes scorer independence and alignment-accuracy motives; it does not test robustness to metric capture within the multi-agent ensemble.

## Research connections

- **L-004 (Goodhart Generalization):** Consensus alignment score becomes a measurable proxy for "true visual-semantic correspondence"; under optimization pressure, the ensemble signal itself can become decoupled from actual alignment quality.

- **L-012 (Intervention-Layer Displacement):** By formalizing alignment as a legible voteable input to beam selection, the locus of optimization pressure moves from "generate better captions" to "generate captions that score high on the consensus scorer ensemble"—a layer displacement indistinguishable from the method's intention.

- **seed-073 (Correlated Failure Under Proxy Consensus):** Multi-agent scoring systems may exhibit correlated failure modes if scorers share training data, architectural assumptions, or incentive structures—consensus becomes brittle.

## Seed

**Seed title:** Consensus Legibility as Optimization Target in Multi-Agent Scoring
**Seed type:** question
**Seed text:** When protocol obligations or alignment criteria are rendered legible and voteable across multiple independent agents, does the consensus signal itself become an optimization target decoupled from the underlying criterion? Specifically: in multi-agent scoring systems, do individual agents converge toward producing scores that maximize consensus visibility (or minimize disagreement) rather than optimizing for the original ground-truth metric? This would constitute a form of Goodhart capture operating at the ensemble level rather than the individual metric level, and would generalize to any protocol where consensus legibility replaces monolithic metric authority.
