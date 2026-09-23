# Intervention problems in the Linear Threshold Model: A general formulation and new results

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2609.17146
**Date read:** 2026-09-22
**Connected to:** L-003, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper studying optimal intervention design in linear threshold (LT) models — network coordination games where agents adopt actions based on neighbor thresholds. The work formalizes the planner's problem: modify agent thresholds at cost to achieve desired equilibrium outcomes. Standard GT optimization problem with new structural results.

## What I took from it

The paper formulates threshold modification as a legible optimization target (L-003: formalization under pressure), and the cost-threshold tradeoff creates a natural proxy optimization surface. However, the work treats agent strategies as passive responders to threshold parameters, not as strategic actors who *know* thresholds are being modified and condition their own threshold-setting on that knowledge. This is a classical game-theory blindness: it does not capture the strategic anticipation loop that would arise in a real protocol context (L-010's nonmonotonicity).

The model is clean precisely because it excludes the feedback: agents don't learn that thresholds are instruments of control, don't strategically misreport their own thresholds, and don't cluster adoption behavior around the planner's known modification boundaries. The paper is solving the *abstract* intervention problem, not the *protocolized* one. It confirms that threshold legibility enables optimization, but does not test whether that optimization breaks down under strategic response — which is where L-010 and L-003 live.

## Research connections

- **L-003 (Formalization Ratchet):** Threshold models are inherently formalizable coordination norms; the paper shows threshold modification becomes an optimization target once thresholds are legible parameters. Confirms formalization enables optimization, but doesn't test the ratchet effect (can thresholds be informalized once formalized?).

- **L-010 (Coordination Adoption Nonmonotonicity):** The paper assumes monotonic response to threshold changes. Real adoption curves would be nonmonotonic if agents condition their threshold on *observing* that thresholds are being modified by a planner — this creates discontinuous strategic shifts. The paper does not model this.

- **seed-129 (Legibility-Induced Conformity Locking):** Once thresholds are rendered legible and modifiable, agents may converge on conformist strategies ("adopt what the modification target is") rather than genuinely coordinate on network state. The paper doesn't track this substitution.

## Seed

**Seed title:** Threshold Legibility as Strategic Anticipation Blindness

**Seed type:** observation

**Seed text:** Linear threshold models become tractable for planner optimization precisely because agents are modeled as stateless responders to threshold parameters—they do not anticipate that thresholds are being strategically modified. In any protocolized system where threshold-like coordination rules are legible and modifiable, agents will condition their own threshold-setting (or misrepresentation of thresholds) on the *fact of modification itself*, creating a second-order strategic loop. This generates discontinuities and nonmonotonicity invisible to single-level game-theoretic optimization. The model's tractability depends on the opacity assumption that agents cannot observe or anticipate the planner's intervention — a condition that fails precisely when intervention becomes a known, legible protocol feature.
