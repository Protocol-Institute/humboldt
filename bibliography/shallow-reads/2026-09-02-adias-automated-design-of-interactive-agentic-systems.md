# ADIAS: Automated Design of Interactive Agentic Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.06410
**Date read:** 2026-09-02
**Connected to:** L-012, L-016
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper proposing issue-centric rather than candidate-centric optimization for iterative agent design. The work addresses repair efficiency in multi-round agent harness iteration by making explicit the persistent problem state across rounds, rather than organizing feedback around successive agent candidates.

## What I took from it

The paper documents a real operational friction in agentic system tuning: when the optimization loop is organized around *agent candidates* (what gets tried), the *issues themselves* become implicit and fragmented across evaluation rounds. This creates a secondary efficiency problem—repair progress doesn't consolidate, interventions don't target root causes cleanly.

This is relevant to L-012 (Intervention-Layer Displacement) insofar as it shows what happens when the legible input to the optimization loop shifts from "which agent works?" to "which issue persists?"—but the paper does not interrogate *whether this shift changes what gets optimized for*, nor whether making issues explicit creates new targeting surfaces that the system then optimizes around orthogonally. The work is competent engineering; it does not theorize the consequence of making a previously implicit layer legible. L-016 (Normative Intervention Algorithmic Retraining Effect) is weakly connected: the paper acknowledges that repeated interventions can have cumulative effects, but treats this as a problem to solve (via explicit issue tracking) rather than a mechanism to study.

## Research connections

- **L-012:** Shift from candidate-legibility to issue-legibility as optimization target may displace pressure, but paper does not examine what gets optimized *after* issues become the decision input.
- **L-016:** Paper mentions intervention propagation and cumulative effects but does not model or measure adaptive system response to repeated normative corrections.
- **seed-082 (Additive Intervention in Overloaded Protocols):** Making repair progress explicit may add a layer without removing root pressure; unclear whether consolidated issue tracking reduces or merely reorganizes coordination cost.

## Seed

**Seed title:** Legibility-Driven Repair Targeting as Secondary Optimization Surface

**Seed type:** question

**Seed text:** When iterative optimization of agentic systems shifts from agent-candidate organization to explicit persistent issue state, the issue taxonomy itself becomes a legible decision substrate. Systems may then optimize to cluster problems within tractable issue categories, defer rare or cross-cutting issues, or route problems toward interventions that are cheap to execute *relative to issue legibility* rather than relative to actual repair efficacy. Does making coordination work (issue tracking) legible cause the optimization pressure to move orthogonally—from "solve the agent problem" to "solve the issues that fit the issue schema"?
