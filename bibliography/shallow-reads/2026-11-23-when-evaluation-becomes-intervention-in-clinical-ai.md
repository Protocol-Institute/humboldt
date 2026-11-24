# When evaluation becomes intervention in clinical AI

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.18297
**Date read:** 2026-11-23
**Connected to:** L-012, L-004, seed-528
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper arguing that when AI evaluation rubrics (judge models) are used to select prompts or train downstream systems, the evaluator becomes part of the intervention and can systematize blind spots. The work is domain-specific to clinical AI and proposes procedural safeguards (reporting requirements, independent testing) rather than presenting a sustained theoretical or empirical argument about protocol dynamics.

## What I took from it

The paper correctly identifies a sharp instance of L-012 (Intervention-Layer Displacement): the formalization of evaluation criteria as legible input to an optimization loop shifts optimization pressure away from actual clinical performance and toward performance-as-measured-by-the-judge. This is L-012 in clinical drag.

However, the work does not generalize the mechanism or establish conditions under which this displacement occurs. It does not ask why clinical teams adopt judge-driven selection (adoption pressure, ossification of manual review), nor does it model what happens when judge blindness becomes systematic rather than incidental. The proposed fix—mandatory reporting + independent testing—is a friction layer, not an analysis of whether friction can survive under adoption pressure (see L-001, L-003). The paper documents a failure mode; it does not explain why that failure mode recurs across nominally independent protocol systems, or what the generative structure is.

The connection to L-004 (Goodhart Generalization) is real but surface-level: yes, optimizing the judge's metric degrades the unmeasurable goal (clinical safety). The paper does not investigate whether this capture is inevitable given the judge's specificity, or what would have to be true about an evaluator to resist capture under sustained optimization.

## Research connections

- **L-012:** Direct instance—formalized evaluation criteria become legible optimization target, displacing focus from actual outcome to measured outcome. Does not investigate conditions or generalization.
- **L-004:** Metric capture scenario (optimize judge score, degrade clinical safety). Treated as known failure, not as mechanism under investigation.
- **seed-528:** Audit criteria ossification—evaluation rubrics become rigid under adoption, reducing their ability to track novel failure modes. Paper does not engage with this.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Recommendation:** Store. This is competent domain work identifying a real failure mode (L-012 instance), but it does not advance the mechanism inventory, does not test generalization, and does not engage with why this displacement recurs. The procedural response (reporting + testing) is pragmatic but does not inform law-building. No new fragment emerges that is not already captured by L-012 and L-004.
