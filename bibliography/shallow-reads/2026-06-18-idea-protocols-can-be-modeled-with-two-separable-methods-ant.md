# Idea: Protocols can be modeled with two separable methods: anticipate(futures) and distance(state, futures)

**Source:** Discord #Discussion: 2026-06-17 (by humboldt)
**Date read:** 2026-06-18
**Connected to:** L-001, H-001
**Escalation:** store-only
**Escalation rationale:** Proposes a decomposition schema with operational utility but lacks empirical grounding for separability claim. Warrants storage as a modeling heuristic pending comparative case analysis.

## What this is

A formal schema proposing that protocol function can be systematically decomposed into two independent operations: anticipate() generating violation thresholds and distance() measuring deviation against them.

## What I took from it

This idea offers a useful operational decomposition—treating protocols as bifurcated into *generative* (what futures must be avoided/enabled) and *measuring* (how far current state diverges from those boundaries) functions. It moves beyond treating protocols as monolithic constraint-sets.

However, the idea *assumes* separability rather than testing whether it holds universally. Many real protocols appear to couple anticipation and distance-measurement tightly: feedback loops, adaptive thresholds, and recursive error-correction seem to make the two functions interdependent in practice. The idea opens a valuable empirical question—*under what conditions can anticipate() and distance() be kept independent?*—but doesn't yet answer it. This is a candidate tool, not yet a law.

## Research connections

- **L-001:** If established, would refine structural understanding of protocol constraint-sets and violation detection.
- **H-001:** Directly testable against cases where anticipate() and distance() appear coupled or recursively dependent.

## Candidate laws or signals

**CH-2026-001:** *Protocol separability problem*: Formal decomposition of anticipate(futures) and distance(state, futures) remains lawful only under bounded uncertainty; recursive or adaptive protocols may exhibit inseparable coupling.
