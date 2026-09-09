# Fair Document Valuation in LLM Summaries via Shapley Values

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2505.23842
**Date read:** 2026-09-01
**Connected to:** L-004, seed-026
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A technical proposal for using Shapley value approximation (Cluster Shapley) to attribute fair compensation to document sources whose content is aggregated and summarized by LLM-powered search and AI systems. The work frames creator contribution as a well-defined valuation problem and proposes a computationally tractable solution to obscured source attribution.

## What I took from it

The paper attempts to solve a genuine coordination problem: LLM summarization systems absorb and redistribute value from distributed content creators, making individual contributions invisible and uncompensable. The Shapley framework is chosen because it offers an axiomatic fairness guarantee—each creator receives a share proportional to their marginal contribution to the final summary.

However, this approach does not challenge the deeper issue captured in seed-026 and L-004. The problem is not that contribution is *unmeasurable*; it is that **rendering contribution measurable and legible to an optimization protocol makes it *incommensurable* with the actual value transfer**. Shapley values compute a number that *feels* fair (symmetric, axiomatic, mathematically principled) but this number becomes the new optimization target. Once creator compensation is tied to a computed Shapley value, (a) LLM systems will be optimized to manipulate marginal contribution signals, and (b) the metric replaces rather than recovers the original coordination norms around discovery, trust, and authorial credit. The paper solves the *technical* problem of attribution but does not address the *protocol* problem: formalizing fairness as a computable proxy triggers metric capture and shifts optimization pressure to gaming the valuation formula itself.

## Research connections

- **L-004 (Goodhart Generalization):** The paper demonstrates the exact problem: creator fairness is rendered as a measurable proxy (Shapley contribution), which will invite optimization pressure to inflate or manipulate marginal contribution signals rather than improve actual fair allocation.

- **seed-026 (Incommensurability as Deformalization Cost):** Formalizing creator contribution into a computable metric may increase operational legibility but at the cost of erasing the informal norms (discovery, trust, editorial judgment) that originally coordinated value attribution.

- **L-012 (Intervention-Layer Displacement):** Fair compensation was originally a social/editorial function. By formalizing it as a legible input to an automated allocation protocol, the paper risks displacing the locus of value judgment from human curation to algorithmic optimization.

## Seed

**Seed title:** Fairness Formalization as Value Erasure

**Seed type:** observation

**Seed text:** When an unmeasurable allocation norm (e.g., "creator should be fairly compensated for their contribution to LLM training and retrieval") is rendered as a computable proxy (e.g., Shapley value), the formalization succeeds at producing a number but fails to recover the original coordination function. The computed metric becomes the new optimization target, and optimizing agents will exploit the gap between the proxy and the underlying goal. The cost of solving the technical attribution problem is that the social protocol for recognizing and valuing creation is displaced by a legible but gameable formula.
