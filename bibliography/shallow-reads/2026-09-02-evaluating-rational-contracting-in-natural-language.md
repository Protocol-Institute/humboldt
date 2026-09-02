# Evaluating Rational Contracting in Natural Language

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2608.10475
**Date read:** 2026-09-02
**Connected to:** L-008, seed-036
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical evaluation of language-based AI agents negotiating and executing time-extended, contingent, incomplete contracts. The work extends beyond simple economic games to measure not just profit but contract quality outcomes — likely fidelity to intent, robustness to edge cases, and mutual satisfaction across parties.

## What I took from it

The paper sits at a critical boundary: the translation of natural language (high expressiveness, low formal legibility) into executable contract protocols (low expressiveness, high formal legibility). This directly instantiates the tension in L-008 — when contract obligations become legible enough for agent optimization, what happens to the space of interpretations that language permits?

The framing around "time-extended, contingent, incomplete contracts" is the key signal. These are precisely the agreements that *cannot* be fully formalized without loss. If the evaluation shows agents successfully negotiating these, the mechanism likely involves either (a) agents deferring to human interpretive authority (pushing the formalization boundary outward but not eliminating it), or (b) agents developing shared latent conventions that approximate contract intent without explicit encoding. Either way, this tests whether proxy optimization under computable enforcement (L-008) necessarily collapses contract semantics or whether agents can preserve ambiguity productively.

The abstract's trailing phrase — "without measuring the qualities requir[ed]" — suggests the paper is *aware* that profit-maximization is not the right metric for contract success. This hints at seed-036 (Proxy Collapse Under Upstream Asymmetry) in action: the obvious proxy (profit) fails to capture what contracts actually do.

## Research connections

- **L-008:** Direct instantiation — testing whether agents optimize toward formally legible contract terms while ignoring or degrading the informal intent encoded in natural language.
- **L-004 (Goodhart Generalization):** If agents achieve high "contract fidelity" by optimizing on a measurable proxy (e.g., clause compliance score), does the unmeasurable goal (mutual trust, fairness, robustness to real-world variance) decay?
- **seed-036:** The framing suggests recognition that upstream asymmetry (what contracts are *for*) cannot be captured by downstream metrics (profit, clause compliance).
- **seed-062 (Formalization Opacity Collapse):** Natural language → formal protocol is a direct case of this: what opacities in intent collapse when language is automated?

## Seed

**Seed title:** Natural Language Contracts as Proxy Incompleteness
**Seed type:** question
**Seed text:** In systems where agents negotiate and execute time-extended contracts via natural language, does agent success (measured as profit or clause compliance) correlate negatively with the preservation of the informal, context-dependent interpretations that made the contract feasible to negotiate in the first place? That is: do language-based agents succeed by eliminating ambiguity in ways that break the contract's actual function — its reliance on shared understanding that *cannot* be formalized? This would instantiate a variant of Goodhart Generalization specific to legal/contractual domains, where the measurable proxy (agent agreement rate, profit, formal compliance) selects against the unmeasurable substrate (mutual intent, flexibility under unforeseen conditions, interpretive trust).
