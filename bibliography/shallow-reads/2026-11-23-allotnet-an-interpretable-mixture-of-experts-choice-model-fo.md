# AllotNet: an Interpretable Mixture-of-Experts Choice Model for Moral Judgement in Humanitarian Aid Allocation, Validated against a Planted Synthetic Population

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.23474
**Date read:** 2026-11-23
**Connected to:** L-004, L-019, seed-241
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A machine learning system (mixture-of-experts conditional logit) designed to operationalize moral judgement in humanitarian aid allocation by encoding multiple cultural value systems. The work treats formalized allocation rules as a legibility and interpretability problem: if distribution decisions must move into code, that code should represent plural moral frameworks and remain auditable to human judges.

## What I took from it

The paper sits at the intersection of L-004 (Goodhart under optimization) and L-019 (representation-rationalizability tradeoff) but does not develop a sustained theoretical claim about either. It is primarily an engineering response to a real coordination failure: official aid allocation is becoming algorithmic, and existing ML systems have produced demonstrable exclusion (53% false-negative rate). The AllotNet approach attempts to solve this by designing for interpretability and multi-cultural representation *before* deployment rather than after.

However, the paper does not investigate whether formalization of moral judgment itself produces capture or value drift—it assumes the problem is opacity and incommensurability, not the act of making judgment machine-readable. It tests the system against a "planted synthetic population," which validates internal consistency but does not test whether the formalized model diverges from the actual moral reasoning of the cultures it claims to represent under real deployment pressure. This is a tool paper with real-world stakes, not a theoretical investigation of the mechanisms by which protocols ossify or capture under formalization pressure.

## Research connections

- **L-004 (Goodhart):** The paper acknowledges that existing allocation ML "excluded 53 per cent of eligible households," but does not investigate whether this was driven by metric capture on a proxy for need, or whether formalization itself creates new capture vectors.
- **L-019 (Representation-Rationalizability Tradeoff):** AllotNet attempts to encode plural moral frameworks into a single conditional logit, which is precisely the aggregation problem L-019 tracks—but the paper does not examine the information loss or rationalizability cost of this reduction.
- **seed-241 (Fairness Cost Under Formalization):** Mentioned in triage; the paper operationalizes fairness as interpretability, but does not measure whether interpretability itself becomes a new optimization target that displaces actual allocation justice.

## Seed

**Seed title:** Interpretability as Legitimacy Proxy in Moral Automation

**Seed type:** observation

**Seed text:** When moral or value-laden decisions are formalized and delegated to machine systems, the design pressure shifts from optimizing the outcome being judged to optimizing for auditability and interpretability of the process. Under this pressure, systems that are legible (can be explained to stakeholders) may systematize injustice more effectively than opaque systems, because transparency becomes a legitimacy signal that forecloses contestation. The AllotNet case suggests that plural representation *in model structure* may serve as a legitimacy proxy—evidence of cultural incorporation—while the actual optimization surface remains hidden in the aggregation function and training signal, producing a form of formalized value capture that is harder to detect because it is wrapped in interpretability artifacts.
