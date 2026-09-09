# Differentially Private Auditing Under Strategic Response

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2605.07674
**Date read:** 2026-09-02
**Connected to:** L-008, L-014
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic analysis of auditing design when an auditor commits to a differential privacy budget and query policy, and the audited developer responds by reallocating mitigation effort across harm dimensions. The work formalizes this as a bilevel Stackelberg game and introduces a welfare-weighted under-detection gap metric.

## What I took from it

This is competent technical work on a real coordination problem: when audit legibility is constrained by privacy, the developer's response becomes predictable and exploitable. The bilevel structure confirms that computable constraints create optimization targets (the DP budget and query allocation become the surface to game around), but the paper treats this as a technical problem to be solved via better mechanism design rather than as evidence of a deeper regularity.

The work does not establish or argue for a mechanism absent from the inventory. It shows strategic response to privacy-constrained audit interfaces, which is consistent with L-008 (proxy optimization under computable enforcement) and L-014 (strategic boundary concentration under computable legality), but it does not extend, challenge, or ground these laws—it is a case study within their domain.

## Research connections

- **L-008:** Confirms that when enforcement signals become legible and computable (here: the DP budget allocation), optimizing agents exploit the structure of the legible interface.
- **L-014:** Shows concentration of optimization pressure at the boundary of what is computable/auditable (developers reallocate mitigation effort away from privacy-constrained audit dimensions).
- **seed-080:** Proxy collapse under upstream asymmetry: the DP-constrained audit serves as a proxy for harm; developers exploit the asymmetry between what the audit can detect and what it cannot.

## Seed

**Seed title:** none

---

**Justification for store-only:** This is a solid applied game-theory paper on a specific regulatory problem. It does not present a sustained theoretical argument that challenges or extends existing law candidates. It instantiates L-008 and L-014 in a narrow domain (AI auditing) without offering new mechanism insight or cross-domain generalization. The welfare-weighted under-detection gap is a useful metric but a tool, not a law fragment.
