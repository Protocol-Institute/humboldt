# Robust Is Salient: An Informed Adversary Moves the Optimal Signal onto the Salience Pole

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2610.00233
**Date read:** 2026-11-23
**Connected to:** L-004, seed-461
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of signaling under adversarial conditions, showing that when an informed adversary observes the same signal channel, the optimal robust signal collapses onto the "salience pole" — the most cognitively salient or simple description — rather than maintaining Bayesian discriminative power. The work provides formal confirmation that robustness and salience align empirically across a large item pool, with divergence only in edge cases where the salience-to-Bayes coordinate is undefined.

## What I took from it

This is a narrow, formally correct result that *confirms* rather than extends L-004 (Goodhart Generalization). The paper demonstrates that under adversarial optimization pressure, a protocol system (here: a signaling channel) loses its capacity to preserve information-theoretic discrimination and instead optimizes toward the most easily-described or cognitively available proxy. This is Goodhart in a constrained setting: the measurable proxy (salience) outcompetes the true signal under pressure.

The work does not reveal a *new* mechanism — it formalizes a known dynamic in a specific game-theoretic frame. It is valuable as confirmation but does not alter the inventory of protocol failure modes or suggest a fresh line of inquiry. The result is domain-specific (signaling games) and does not generalize beyond competitive information design.

## Research connections

- **L-004 (Goodhart Generalization: Metric Capture):** Confirms that under optimization pressure, a measurable proxy (salience) captures the protocol's optimization target, displacing fidelity to the unmeasurable underlying truth.
- **seed-461:** Likely a prior salient-proxy-capture observation; this paper provides formal/empirical grounding in the adversarial signaling case.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
