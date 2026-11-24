# Hardening Soft Information: Evidence on Analyst Integration Costs

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2505.12269
**Date read:** 2026-11-23
**Connected to:** L-004, seed-241
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

An empirical study using analyst reports to isolate the cost of converting qualitative information into numerical forecasts. The work treats "integration cost"—the friction imposed by formalization itself, independent of information acquisition—as a measurable quantity, using the gap between textual and numerical outputs from the same forecaster as evidence.

## What I took from it

This is a competent decomposition of a real phenomenon: formalization imposes transaction costs that are orthogonal to information availability. The finding that soft information and hard estimates systematically diverge even when produced by the same agent with the same underlying knowledge is empirically clean and domain-specific. 

However, the paper does not theorize *why* this friction exists, what makes it irreducible, or how it generalizes across protocol regimes. It documents a gap; it does not explain whether that gap reflects cognitive load, incentive misalignment, strategic opacity, or the intrinsic incommensurability of narrative and scalar representations. The work is valuable as empirical confirmation that formalization is *costly*, but it does not advance mechanism-level understanding of when that cost is recoverable, when it drives protocol failure, or how systems adapt under sustained formalization pressure. It is bounded to the analyst report domain.

## Research connections

- **L-004 (Goodhart Generalization):** Confirms that transformation of soft into hard signals introduces friction, though does not distinguish between metric capture *per se* and the cost of measurement itself.
- **seed-241:** Direct confirmation that qualitative-to-quantitative translation carries integrative friction; gap size is quantifiable.
- **L-023 (Informality as Novelty Sink):** Tangentially relevant — if formalization is costly, informal channels may survive longer; not explored in this paper.
- **seed-544 (Metalinguistic Displacement Under Formalization Pressure):** Soft information and hard estimates may inhabit incompatible semantic spaces; gap may reflect that incommensurability rather than pure cost.

## Seed

**Seed title:** Formalization Cost as Non-Recoverable Load Under Scalar Compression

**Seed type:** observation

**Seed text:** When qualitative information is compressed into scalar or formal estimates by the same agent using the same underlying knowledge, systematic divergence emerges between soft and hard outputs. This gap reflects not information asymmetry or acquisition cost, but the irreducible friction of translating distributed, context-laden representation into legible form. The cost may be partly cognitive (attention, working memory), partly incentive-driven (signaling or noise injection), and partly representational (narrative and scalar forms may be incommensurable). If this formalization cost is structurally non-recoverable—cannot be eliminated through better tools, training, or incentives—then protocols that mandate scalar outputs may incur persistent efficiency loss independent of their coordination benefits. This warrants investigation across domains where soft and hard representations coexist in the same decision layer.
