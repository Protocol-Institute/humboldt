# Easier, but Not Easy: Nash Welfare under Lexicographic Valuations

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.24537
**Date read:** 2026-09-02
**Connected to:** L-004, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational complexity paper studying Nash welfare maximization (a central fairness metric in resource allocation) under lexicographic preference valuations. The work shows that despite lexicographic preferences being "almost ordinal" (intuitively simpler than general additive preferences), the optimization problem remains hard — contradicting the surface intuition that structural simplification yields computational tractability.

## What I took from it

The paper documents a case where *preference legibility* (ordering goods into strict ranks where tier *i* >> tier *i+1*) does not translate into *optimization tractability*. This is relevant to L-008 (proxy optimization under computable enforcement) and L-004 (metric capture): when Nash welfare is used as a fairness proxy and preferences are formalized as machine-readable ordinals, one might expect the allocation protocol to become easier to operationalize. Instead, the hardness persists despite the structural simplification.

The deeper pattern: **formalization of preferences does not guarantee protocol tractability**. The authors show that even when agent preferences collapse into a nearly-ordinal structure (making preferences "simpler" conceptually), the global optimization landscape remains hard. This suggests that legibility of *agent state* (what each agent wants) is orthogonal to legibility of *system behavior* (whether the allocation algorithm can compute an optimal outcome). Computable preference representation ≠ computable welfare maximization.

## Research connections

- **L-004 (Goodhart Generalization):** Nash welfare as a fairness metric is subject to capture when preferences are formalized and made computable; this paper shows the optimization difficulty persists even under preference simplification, suggesting the metric's fragility is structural, not merely computational.
- **L-008 (Proxy Optimization Under Computable Enforcement):** The work demonstrates that enforcement signals (here: preference orderings) can be made legible and computable without enabling efficient protocol execution — computable legibility does not imply tractable optimization.
- **seed-062 (Formalization Opacity Collapse):** The lexicographic preference structure is maximally formalizable and transparent (strict ordinal ranking), yet the protocol behavior remains opaque (hard to compute). Suggests formalization ≠ transparency of outcomes.
- **seed-080 (Proxy Collapse Under Upstream Asymmetry):** Nash welfare as a fairness proxy depends on accurate preference elicitation; under lexicographic formalization, preferences are easier to state but the global allocation problem becomes harder to solve.

## Seed

**Seed title:** Legibility-Tractability Decoupling in Welfare Protocols

**Seed type:** observation

**Seed text:** In allocation protocols where agent preferences are formalized as machine-readable ordinals (e.g., lexicographic valuations), preference legibility increases while protocol tractability may remain invariant or worsen. Simplifying the *representation* of preferences does not simplify the *computation* of optimal allocations. This suggests that protocol "ease" is not a function of preference transparency alone, but of the structural properties of the welfare objective under preference constraints — a gap between agent clarity and system solvability.
