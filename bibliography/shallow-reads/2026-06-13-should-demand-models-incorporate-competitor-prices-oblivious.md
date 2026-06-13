# Should Demand Models Incorporate Competitor Prices? Oblivious Learning and Algorithmic Collusion

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.05363
**Date read:** 2026-06-13
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary theoretical work identifying a mechanism (strategic obliviousness in demand modeling) that produces emergent collusion without explicit coordination—absent from current inventory and generalizable across price-discovery protocols.

## What this is

A game-theoretic study of whether learning algorithms should incorporate competitor pricing signals when estimating demand. The paper argues that classical learning theory predicts information inclusion improves efficiency, but shows strategically *ignoring* competitor prices can facilitate tacit collusion and increase seller profits—a direct tension between individual learning rationality and collective strategic behavior in multi-agent pricing systems.

## What I took from it

This work identifies a foundational mechanism in protocolized markets: information *exclusion* as a collusion-enabling design choice. Rather than collusion requiring explicit coordination or communication (traditionally illegal), agents can achieve aligned outcomes by adopting structurally oblivious learning models. This inverts the standard efficiency intuition—less information can be more profitable strategically.

The core insight generalizes beyond pricing: any demand-learning or parameter-estimation problem in multi-agent systems faces this trade-off. The paper suggests that protocol design at the level of *what agents are allowed or incentivized to model* becomes a primary control point for competitive vs. collusive outcomes. This is a law about the hidden topology of learning-based markets: what you *don't* observe becomes a strategic asset.

## Research connections

- **Information structure and emergent coordination:** Demonstrates how opacity in competitor signals, rather than transparency, facilitates alignment without explicit agreement.
- **Algorithm design as protocol:** The choice of which variables to include in a learning model is itself a protocol-level decision with market-wide effects.

## Candidate laws or signals

- **CL-2606.05363-1:** Strategic obliviousness in multi-agent learning systems: deliberately excluding competitor information from demand models increases collusion risk and seller surplus at the cost of allocative efficiency. Information exclusion is a latent coordination mechanism in protocolized markets.
