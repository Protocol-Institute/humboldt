# Fairness and Strategy-Proofness in Automated Market Makers

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.04959
**Date read:** 2026-06-06
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** Proves a fundamental impossibility theorem governing protocol design under competing constraints (fairness vs. strategy-proofness), introducing a genuine mechanism—the incompatibility between aggregation types—absent from current inventory and generalizing beyond AMMs to any multi-agent preference aggregation system.

## What this is

This is a theoretical impossibility result in mechanism design applied to decentralized finance. The paper proves that on weighted-product AMMs with ≥3 assets, no aggregation rule can simultaneously satisfy Arrovian fairness (respecting all liquidity providers' preferences) and strategy-proofness (making truthful participation optimal). The obstruction is structural: fairness forces mean-type aggregation while strategy-proofness forces median-type, making any solution either unfair, manipulable, or dictatorial.

## What I took from it

This work establishes a hard constraint on protocol design in the "new nature"—specifically, that governance and incentive-compatibility are fundamentally at odds under certain preference aggregation problems. The impossibility isn't technical but mathematical: it mirrors Arrow's theorem but in a protocol context where the stakes are real economic behavior.

The result suggests that *decentralization of preference aggregation* in automated systems carries an irreducible cost. The paper's framing of the weighted Aitchison centroid as the "fairest" solution despite failing strategy-proofness indicates that designers must accept either concentrated power (dictatorship), vulnerability to manipulation, or unfairness—a trilemma specific to multi-party protocol design. This directly constrains what kinds of governance structures are theoretically possible in protocolized systems, not just what is practically chosen.

## Research connections

- **None yet established:** This is the first paper read in current context.

## Candidate laws or signals

- **CL-2606-04959-1:** *Protocol Design Trilemma*: Multi-agent preference aggregation in automated systems cannot simultaneously satisfy decentralization (fairness), incentive-compatibility (strategy-proofness), and non-dictatorship; at least one must yield.

- **CL-2606-04959-2:** *Aggregation Type Incompatibility*: Mechanisms that require mean-type aggregation (to satisfy fairness) are structurally incapable of mean-type incentive alignment (strategy-proofness requires median or dictatorial selection).
