# Repeated-Game Security for Restaking-Based Verifiable Inference

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.09055
**Date read:** 2026-09-02
**Connected to:** L-007, L-013
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source identifying a mechanism (repeated-game gap in stake-based verification) absent from current inventory; it directly challenges the foundational security model of a major protocol class and generalizes to any repeated-verification system under collateralization.

## What this is

A game-theoretic analysis of restaking-based verifiable inference protocols. The paper demonstrates that one-shot slashing conditions (penalty > cheating benefit) provide weaker security guarantees under repeated play with the same stake, introducing what the authors call a "repeated-game gap"—a window where rational actors can profitably cheat across multiple rounds despite individual round penalties being theoretically sufficient.

## What I took from it

This work directly instantiates and challenges a blind spot in L-007 (Trust Ratchet in Safety-Critical Protocols). The paper shows that operational age and stability *without structural ratcheting of enforcement cost* can actually enable defection under repeated interaction. The trust accumulation assumed in L-007 turns out to be conditional on proper repeated-game analysis—a protocol system that "functions correctly" in isolated transactions can develop latent exploitability under stationarity.

More broadly, this surfaces a coordination failure specific to legible, computable enforcement: the one-shot rationality condition (penalty > gain) is *locally sufficient but globally insufficient* under repeated play. This suggests a generalization: protocols that reduce verification and punishment to legible, computable functions may create optimization surfaces where agents can arbitrage the difference between single-interaction and multi-interaction payoff structures. The repeated-game gap is a form of Goodhart capture (L-004) applied to time-stratified enforcement—the proxy (one-round slashing) optimizes away the real objective (security across multiple rounds).

## Research connections

- **L-007:** Directly challenges the sufficiency of operational stability as trust signal in safety-critical protocols; shows trust accumulation can mask defection equilibria.
- **L-013:** Exemplifies paradigm-locked anomaly tolerance—the one-shot security model persists in protocol design even when repeated-game analysis shows it is insufficient.
- **L-004 (Goodhart Generalization):** The one-round slashing condition is a measurable proxy for unmeasurable security; optimization under repetition breaks the proxy.
- **L-008 (Proxy Optimization Under Computable Enforcement):** Restaking protocols render penalties legible and computable; the paper shows agents can exploit legibility across time horizons.
- **seed-073 (Correlated Failure Under Proxy Consensus):** Multiple verifiers using the same one-shot rationality assumption can fail in coordinated ways under repeated play.
- **seed-082 (Additive Intervention Preserves Root Pressure):** Slashing penalties are additive interventions; the paper suggests they preserve the underlying incentive pressure across repeated rounds.

## Seed

**Seed title:** Repeated-Game Security Disjunction in Legible Enforcement

**Seed type:** mechanism

**Seed text:** In protocols where enforcement signals (slashing, penalties, proof requirements) are rendered computable and legible, one-shot rationality conditions are necessary but not sufficient for security under repeated play with the same stake. The gap between single-interaction and multi-interaction payoff structures creates an exploitation surface invisible to stateless verification models. This generalizes beyond restaking to any protocol where agents repeatedly interact under a fixed enforcement rule that was validated only for one-shot play; the legibility that enables automated punishment also enables time-stratified arbitrage of the penalty function.
