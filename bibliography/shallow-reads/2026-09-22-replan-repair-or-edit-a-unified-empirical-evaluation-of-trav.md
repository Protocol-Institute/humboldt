# Replan, Repair, or Edit? A Unified Empirical Evaluation of Travel Agents for Itinerary Revision under Resource Disruptions

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.19654
**Date read:** 2026-09-22
**Connected to:** L-005, L-012
**Kind:** benchmark/empirical study
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical comparison of three strategies for revising infeasible travel itineraries after disruption: full replanning, classical plan repair, and LLM-based edit/revision. The work unifies evaluation protocols across these methods using benchmark datasets derived from TREK, testing performance on single and compound disruptions.

## What I took from it

This is a competent systems paper addressing a real coordination problem in multi-agent resource allocation under disruption. It measures whether incremental repair outperforms full replan (it sometimes does; LLM revision is mixed). However, the paper operates entirely within the problem domain — it does not theorize *why* repair vs. replan trade-offs occur, what conditions lock a system into one strategy over another, or how the choice of revision strategy affects downstream protocol behavior or agent incentives.

The work does not engage with L-005 (Gall Generalization) at the mechanism level — it does not ask whether the complexity of the itinerary system resists safe replacement, or whether repair becomes "safer" because it preserves more of the original structure. Similarly, L-012 (Intervention-Layer Displacement) is not engaged: the paper does not examine whether formalizing the disruption prediction as a legible input to the revision decision shifts optimization pressure to new surfaces (e.g., agents gaming which disruptions are visible to the replan layer, or anchoring behavior on the initial plan).

No novel cross-domain regularity emerges. This is domain-specific optimization.

## Research connections

- **L-005:** The paper implicitly supports the intuition that repair preserves structure better than replan, but makes no theoretical claim about *why* complex systems resist restructuring or what costs arise when they don't.
- **L-012:** Missed opportunity: the legibility of disruption signals and their integration into the revision decision layer could displace optimization pressure to earlier stages (planning under uncertainty about which disruptions will be detected).

## Seed

**Seed title:** none
