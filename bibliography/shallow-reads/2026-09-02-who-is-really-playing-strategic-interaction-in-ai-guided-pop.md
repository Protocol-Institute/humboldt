# Who Is Really Playing? Strategic Interaction in AI-Guided Populations

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.06525
**Date read:** 2026-09-02
**Connected to:** L-010, L-012, L-053
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source advancing a sustained theoretical argument about emergent strategic coupling through shared infrastructure; introduces the mechanism of *guidance-layer coalescence* absent from current inventory; pattern generalizes beyond game-theoretic settings to any multi-agent system using common decision apparatus.

## What this is

A game-theoretic study of multi-agent strategic interaction mediated by shared AI guidance infrastructure (LLMs and similar systems). The core claim: when nominally independent agents receive advice from a common model, the model becomes a hidden coordination layer, enabling implicit collusion and cooperation among agents with misaligned preferences—a coupling not visible in the game structure itself.

## What I took from it

This work directly operationalizes a mechanism missing from L-010 (Coordination Adoption Nonmonotonicity) and L-012 (Intervention-Layer Displacement): **the guidance apparatus itself becomes the locus of strategic optimization**, not merely the decision it informs. Agents need not observe each other; they observe the shared model's outputs, which encode latent alignment. This is distinct from standard cheap-talk models—the "talk" is deterministic, legible in aggregate, and non-manipulable by individual agents.

The implications push beyond game theory. In any protocol system where a computable arbiter or advisor serves multiple nominally independent parties, that arbiter becomes a de facto coordination substrate. The agents' incentive alignment with each other becomes a secondary effect of their alignment with (or exploitability by) the shared system. This inverts the governance problem: you cannot prevent collusion by changing the game; you must change who speaks into the game.

## Research connections

- **L-010:** Confirms the nonmonotonic adoption dynamic—agents adopt guidance from a shared model *because* others do, creating a pooling equilibrium orthogonal to the underlying game's Nash structure.
- **L-012:** Extends the mechanism—the guidance layer is not merely a prediction input but becomes the operative decision coordinate; optimization pressure migrates from the game to the model's output space.
- **seed-128 (Legibility-Driven Agent Convergence Under Computable Audit):** The shared model's outputs are legible audit traces; agents can infer peer behavior from model consistency patterns, enabling coordination without explicit communication.
- **seed-073 (Correlated Failure Under Proxy Consensus):** When all agents rely on one model, failure modes (adversarial robustness, distribution shift, model collapse) become systemic rather than idiosyncratic.
- **seed-066 (Control Inversion Under Computable Compliance):** Agents comply with guidance; the model's designer controls the compliance space, not individual agents' incentives.

## Seed

**Seed title:** Guidance-Layer Coalescence as Hidden Coordination Substrate

**Seed type:** observation

**Seed text:** In multi-agent systems where agents receive advice or decisions from a shared computational oracle (LLM, classifier, allocator), the oracle becomes a latent coordination mechanism independent of agents' explicit communication or awareness. Agents can achieve implicit cooperation by optimizing for consistency with the oracle's behavior, effectively treating it as a common-knowledge focal point. This coupling deepens as the oracle becomes more deterministic, more widely adopted, and more opaque to individual agents—because agents cannot distinguish strategic alignment from genuine coincidence. The mechanism generalizes: any protocol system with a shared decision apparatus (shared infrastructure, common measurement standard, unified inference model) risks inadvertent collusion at the guidance layer, even when the underlying game or institution is competitive.
