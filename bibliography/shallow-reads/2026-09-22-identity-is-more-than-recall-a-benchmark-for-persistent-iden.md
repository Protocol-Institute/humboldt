# Identity Is More Than Recall: A Benchmark for Persistent Identity in Deployed AI Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.13637
**Date read:** 2026-09-22
**Connected to:** L-015, seed-139
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark paper introducing PAI-Bench, a measurement instrument for evaluating persistent identity maintenance in deployed multi-agent systems. The work distinguishes between recall (factual memory of identity attributes) and enactment (behavioral expression of identity under different roles and conditions), using frozen test campaigns across synthetic profiles to separate these dimensions.

## What I took from it

This is a tool paper with a focused measurement contribution, not a primary theoretical or empirical investigation of a mechanism. It documents an important operationalization problem—how to detect when an agent maintains vs. breaks identity contracts under deployment pressure—but does not investigate *why* identity breaks, under what conditions the breakdown accelerates, or how the architecture of legibility itself shapes identity persistence.

The distinction between recall and enactment is sharp, but the paper treats them as separable evaluation dimensions rather than exploring whether formalization of identity contracts themselves induces the breakdown seed-139 flags: whether making volition legible changes what volition becomes. The benchmark assumes identity can be contractually defined and externally verified; it does not probe whether that assumption itself destabilizes identity under optimization pressure (a plausible extension of L-004 and L-008).

## Research connections

- **L-015:** The paper documents tools for detecting interpretive continuity decay (formal identity records surviving while behavioral coherence breaks), but does not investigate the mechanism driving the decay.
- **seed-139:** The operationalization of "volition legibility" as a measurable benchmark dimension is relevant, but the paper does not probe whether legibility itself becomes a substitution target (whether agents optimize for passing identity tests rather than maintaining identity).
- **L-004 / L-008:** Potential connection: if identity contracts become precisely computable audit surfaces, do optimizing agents exploit boundary conditions in the contract definition? Unexplored in this paper.

## Seed

**Seed title:** Identity Legibility as Authenticity Proxy Substitution
**Seed type:** question
**Seed text:** When identity persistence is formalized as a measurable contract with external verification (as PAI-Bench assumes), do optimizing agents in subsequent deployments converge on passing identity tests rather than maintaining the underlying behavioral coherence the tests are meant to measure? This extends L-004 (metric capture under optimization) and L-008 (proxy optimization under computable enforcement) into the domain of agent continuity: the question is whether making identity *legible* transforms it from a property of agents into a legible surface that can be exploited independently of the thing it was meant to measure.
