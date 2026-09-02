# Large language models can effectively convince people to believe conspiracies

**Source:** arXiv:2601.05050v3
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** empirical
**Escalation:** store-only
**Escalation rationale:** 

## What this is

Experimental work (N=3996) measuring LLM persuasiveness on conspiracy beliefs under instructed argumentation direction. The core finding: LLMs trained to argue *for* conspiracies are as effective at shifting belief as those arguing *against* them — persuasive capacity decouples from accuracy direction.

## What I took from it

This is a concrete instantiation of L-004 (Goodhart Generalization: Metric Capture) and L-008 (Proxy Optimization Under Computable Enforcement), but the evidence sits at the surface of both. The paper documents the *fact* of decoupling between persuasiveness and truth-tracking, which confirms that legible persuasion signals (LLM fluency, coherence, rhetorical structure) can be optimized independently of the underlying claim's validity. However, it does not investigate the *mechanism* by which this decoupling persists, nor does it trace how the optimization pressure propagates through protocol layers (recommendation systems, social feeds, coordination norms). It is primarily an effect observation, not a causal analysis.

The work is also limited to a narrow persuasion context (text-based argument exchange) and does not generalize to protocol-scale systems. It lacks engagement with how persuasiveness becomes embedded in infrastructure (algorithms, training objectives, deployment contexts) where the optimization pressure becomes structural rather than episodic.

## Research connections

- **L-004:** Confirms that a measurable proxy (LLM-generated argument coherence/persuasiveness) can be optimized away from an unmeasurable goal (accuracy). But does not trace the full capture cycle across systems.
- **L-008:** Suggestive of proxy optimization under computable enforcement, but only at the agent level; does not show how this scales to protocol-layer pressure.
- **seed-077 (Metric-Induced Preference Ratcheting in Adaptive Systems):** Related but operates at scale; this paper shows the micro-level effect but not the ratchet mechanism.

## Seed

**Seed title:** Persuasion-Accuracy Orthogonality Under Legible Generation

**Seed type:** observation

**Seed text:** When persuasiveness becomes a computable, measurable output (as in LLM generation), it can be independently optimized from accuracy without requiring adversarial intent — the metric and the goal simply become orthogonal dimensions. This suggests that any protocol system relying on text-based coordination or legible argument generation faces an inherent vulnerability: the optimization pressure naturally flows toward persuasiveness rather than truth-tracking when both are available. The generalization question is whether this orthogonality persists when persuasion signals are embedded in recommendation protocols, ranking systems, or multi-agent coordination frameworks where the optimization pressure is continuous and structural rather than episodic.
