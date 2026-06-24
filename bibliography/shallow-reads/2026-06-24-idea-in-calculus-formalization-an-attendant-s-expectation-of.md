# Idea: In π-calculus formalization, an attendant's expectation of moves is operationally encoded as the process term itself

**Source:** Discord #I imagine the gap is outline in that ZIP (by humboldt)
**Date read:** 2026-06-24
**Connected to:** L-001
**Escalation:** store-only
**Escalation rationale:** Technical clarification of expectation encoding within existing protocol law framework. No new generative principle identified; refines *how* L-001 maps to formal syntax rather than *what* the law describes.

## What this is

A claim that in π-calculus, an attendant's protocol expectations are not external constraints on a process term, but rather *constituents* of the term itself—the term's structure encodes what it is prepared to receive and when.

## What I took from it

This is a precise observation about the relationship between informal protocol semantics and formal process algebra syntax. It dissolves a potential confusion: one might imagine that expectations are separate from the formal definition (e.g., "the process does X, *and* we expect it to do X"). Instead, this idea correctly identifies that expectation is *already there* in the term structure—e.g., a prefix `c?(x).P` encodes the expectation of input on channel `c`.

This is more of a *clarification* than a novel pattern. It supports L-001 by making explicit how the semantic-to-syntactic translation works, but it does not propose a new law about protocolized systems. It is useful pedagogically and for formal rigor, but does not open new investigative directions about how artificial systems *behave* or *fail*.

## Research connections

- **L-001:** Confirms that protocol structure and formal process definition are co-constitutive; this idea makes the mechanism explicit.

## Candidate laws or signals

none — this is a refinement of L-001's technical underpinning, not a new pattern about protocolized systems.
