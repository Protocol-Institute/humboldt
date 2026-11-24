# Right Order, Wrong Scale: Auditing LLM Judges for Occupational AI Measurement

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2610.02492
**Date read:** 2026-11-23
**Connected to:** L-004, L-019
**Kind:** content
**Escalation:** store-only

## What this is

An empirical audit paper testing whether LLM-based judges that rank AI outputs correctly also produce correct acceptance rates or aggregate occupational judgments. Using O*NET-BENCH (4,501 worker ratings across 45,796 source responses), the authors evaluate 33 judge configurations and find that high pair-ranking accuracy does not transfer to aggregate-level correctness; a simple TF-IDF baseline achieves near-parity with sophisticated models on ranking despite systematic failures at the aggregation layer.

## What I took from it

This is a narrow but sharp case of **Goodhart generalization** (L-004) operating at a measurement architecture boundary. The paper documents that optimization for a legible local proxy (pairwise ranking agreement) produces models that fail on the unmeasured aggregate (acceptance thresholds, occupational sufficiency judgments). Critically, this is not measurement noise or statistical artifact — it appears to be a *structural decoupling*: the ranking and acceptance functions operate under different information geometries. The finding also bears on **L-019** (representation-rationalizability tradeoff): the reduction of occupational judgment to scalar ranking creates a lossy compression that preserves order but destroys the threshold semantics required for accept/reject decisions.

The paper does not theorize this as a law or generalize beyond occupational AI assessment. It treats the phenomenon as a configuration problem ("wrong scale") solvable by engineering better prompts or architectures. However, the core observation — that legible optimization for one layer of a decision protocol can produce systematic failure in the adjacent layer — points to a potential regularity in hierarchical protocol systems where optimization pressure is unevenly distributed across layers.

## Research connections

- **L-004 (Goodhart Generalization):** Directly instantiates metric capture under proxy optimization: high ranking accuracy under optimization does not predict acceptance accuracy because the proxy does not preserve the target decision function's threshold semantics.
- **L-019 (Representation-Rationalizability Tradeoff):** The reduction of occupational judgment to pairwise rankings trades functional accuracy (acceptance decisions) for representational simplicity (scalar ordering).
- **seed-276 (Legibility-Induced Measurement Substitution):** The choice to optimize for ranking agreement (legible, computable) may displace optimization for aggregate occupational correctness (illegible, interpretively distributed).

## Seed

**Seed title:** Layer-Wise Metric Capture in Decision Hierarchies

**Seed type:** observation

**Seed text:** In hierarchical decision protocols where local optimization (e.g., ranking agreement) is decoupled from aggregate optimization (e.g., acceptance thresholds), high performance on the legible local proxy does not guarantee correctness on the unmeasured global target. This decoupling may be structural: the information geometry that preserves order does not preserve the boundary conditions required for downstream decisions. The regularity may generalize beyond ranking-to-acceptance: any stacked protocol where the upper layer optimizes for a compressed or projected representation of the lower layer's output is at risk of this failure mode.
