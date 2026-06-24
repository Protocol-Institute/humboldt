# Strong duality for the GROW criterion

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2606.24768
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic paper establishing strong duality results for betting-based hypothesis testing, specifically characterizing the "GROW value" (a minimax log-optimality criterion) under composite null and alternative hypotheses. The work extends classical results from Kelly, Breiman, and Shafer by formalizing when a bettor can guarantee asymptotic log-returns against arbitrary composite hypothesis classes.

## What I took from it

This is a **foundational mathematical result in decision protocol design**, not an empirical or theoretical claim about protocolized systems themselves. It provides machinery for *constructing* minimax-optimal betting protocols when the adversary (nature, or misspecified model) belongs to a set of distributions rather than a single one.

The relevance to the "new nature" agenda is *indirect but infrastructural*: GROW duality characterizes when a protocol can simultaneously be robust to multiple failure modes (a composite null) while achieving optimality against a composite alternative. This is a constraint on what *kinds* of protocols are even theoretically possible—a boundary condition on protocol design space, not a law of how protocols behave in deployment.

However, the paper does not study emergent behavior, scaling, or empirical failure modes of such protocols. It is not addressing how duality breaks down, how composite hypotheses are *discovered*, or what happens when the true system is outside both $\mathcal{P}$ and $\mathcal{Q}$.

## Research connections

- **none established:** No current law or active hypothesis yet defined in this research agenda.

## Candidate laws or signals

- **CL-GROW-1:** *Protocols achieving strong duality in composite hypothesis testing become fragile when the true system falls outside the convex hull of both null and alternative hypothesis classes.* (Speculative; would require empirical study of protocol failure modes.)

**Recommendation:** Store as shallow reference. Escalate only if future work identifies empirical cases where duality assumptions fail in deployed protocolized systems, or if we formulate a hypothesis about robustness trade-offs that this work could ground.
