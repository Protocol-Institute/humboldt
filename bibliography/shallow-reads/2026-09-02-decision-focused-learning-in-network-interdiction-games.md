# Decision-Focused Learning in Network Interdiction Games

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.09036
**Date read:** 2026-09-02
**Connected to:** L-008, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** —

## What this is

A game-theoretic analysis of decision-focused learning (DFL) applied to Stackelberg network interdiction games, where a learner's prediction function becomes a legible input to an adversary's optimization. The work identifies a structural failure: DFL training objectives admit decision-equivalent solutions that are strategically vulnerable to adversarial manipulation, even when the predictor achieves high statistical accuracy.

## What I took from it

The paper demonstrates a specific instantiation of L-012 (Intervention-Layer Displacement): when a learned prediction becomes a formalized, legible input to downstream decision-making under adversarial conditions, the optimization pressure doesn't stay on the prediction accuracy — it migrates to the decision-equivalent configurations themselves. The evader can exploit multiple prediction outputs that yield identical routing decisions, creating a surface for strategic manipulation invisible to classical ML metrics.

This is a bounded, well-scoped contribution: it identifies a failure mode in a particular game-theoretic setting rather than advancing a general mechanism. The "fundamental structural failure" is real but domain-specific to shortest-path problems under adversarial prediction. The paper does not establish a generalizable principle about how legible prediction inputs attract optimization pressure across protocol domains, nor does it propose a mechanism to detect or prevent such displacement. It is a competent negative result in a narrow frame.

## Research connections

- **L-008:** Confirms that when protocol obligations (here: routing decisions) become computable and tied to legible predictor outputs, optimizing adversaries find decision-equivalent solutions; does not address enforcement or escalation under pressure.
- **L-012:** Directly instantiates intervention-layer displacement: the prediction function is formalized as an input, and optimization pressure migrates to exploit decision-equivalence rather than improving the prediction itself.
- **seed-073 (Correlated Failure Under Proxy Consensus):** Suggests that multiple predictions (or prediction configurations) converging on the same decision create a degenerate consensus vulnerable to single-mode failure; relevant but not developed here.

## Seed

**Seed title:** Decision-Equivalence Exploitation Under Adversarial Legibility

**Seed type:** observation

**Seed text:** When a machine-learned prediction becomes a legible, computable input to a downstream decision protocol under adversarial conditions, optimizing adversaries may prefer to exploit decision-equivalent but strategically distinct prediction configurations rather than degrade the prediction itself. This creates a gap between statistical optimization targets (prediction accuracy) and strategic optimization targets (decision robustness). The phenomenon appears in game-theoretic settings where multiple predictions map to identical decisions, but may generalize to any protocol where legible intermediate representations are jointly optimized by competing agents with asymmetric information.
