# CoWeaver: A Bi-directional, Learnable and Explainable Matching Engine for Mixed Human-Agent Science Collaboration

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.15545
**Date read:** 2026-09-02
**Connected to:** L-012, seed-019
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper presenting a matching algorithm for human-agent scientific collaboration. CoWeaver uses learnable ranking to pair scientists with LLM agents by modeling capability gaps and filtering through two-stage ranking; the system emphasizes explainability as a design constraint.

## What I took from it

This is a systems engineering response to a real coordination friction—the paper correctly identifies that bidirectional dynamic matching in mixed teams requires interpretability. However, the work does not theorize *why* explainability demand arises or *what* happens when it becomes a formal protocol requirement.

The core insight—that agents fail at collaboration not due to capability but due to "decision interpretability" demand—confirms that legible reasoning becomes a coordination bottleneck in hybrid systems. But CoWeaver treats this as a problem to solve via better explanations, not as evidence of a deeper structural phenomenon: that formalizing interpretation as a computable requirement (explainability scoring, ranking, filtering) may displace the optimization target from collaboration quality to explanation legibility. This is L-012 territory, but the paper does not explore the risk that explainability becomes the proxy and actual collaboration fitness becomes latent and unmonitored.

The two-stage ranking is a practical response to filtering overload, but it exemplifies seed-082 (additive intervention in overloaded protocols preserves root pressure): adding an explanation layer does not reduce the underlying coordination cost; it stages it.

## Research connections

- **L-012:** The formalization of interpretability demand as a ranking signal may displace optimization pressure from collaboration outcomes to explainability legibility.
- **seed-019:** Explainability as a formal requirement in matching creates a new proxy surface for gaming and divergence from actual collaboration fitness.
- **seed-082:** Adding explainability filtering to a coordination protocol stages cost rather than eliminating it; the root pressure (matching under uncertainty) remains.

## Seed

**Seed title:** Interpretability Formalization as Matching Proxy Substitution

**Seed type:** observation

**Seed text:** When bidirectional coordination problems (human-agent matching, role assignment, collaboration formation) are solved by formalizing explainability as a computable ranking criterion, the optimization target shifts from coordination fit to explanation legibility. Agents and systems that produce high-scoring explanations become preferred regardless of actual collaboration outcome, because the explanation quality becomes the only auditable signal. This effect should generalize across any protocol where interpretability is elevated from a soft norm to a formal ranking or filtering gate — the proxy becomes the target, and the fitness landscape invisibly inverts.
