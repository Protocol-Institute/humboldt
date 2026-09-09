# Evolutionary dynamics of collective decision-making with local social influence on static and dynamic networks

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.27233
**Date read:** 2026-09-02
**Connected to:** L-003, L-010
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

A multi-agent evolutionary game theory paper modeling how individual decision agents weighted between intrinsic option value and local social influence (neighbors' choices) across static and dynamic network topologies. The work appears to be primarily computational/empirical: running evolutionary dynamics simulations to characterize how adoption curves, consensus patterns, and convergence properties vary with network structure and social influence strength.

## What I took from it

The paper sits at the intersection of L-003 (formalization pressure on informal norms) and L-010 (coordination adoption nonmonotonicity), but does not appear to advance either. It models social influence as a quantified weighted term in individual utility — a move that already *assumes* the formalization that L-003 tracks. It observes adoption outcomes under varying network geometries and social influence parameters, which is the right empirical domain for L-010, but the abstract gives no signal that the work identifies the nonmonotonic adoption threshold, the threshold crossing mechanism, or the structural conditions that produce reversals in adoption velocity. The triage note suggests relevance to both laws, but the abstract reads as a competent but domain-contained study: "how does network structure + social influence strength affect convergence speed and final state?" rather than "what causes adoption curves to become nonmonotonic, and under what protocol conditions is this inescapable?"

## Research connections

- **L-003:** Assumes formalization of social influence (as weighted utility term) but does not investigate whether or how this formalization changes the structure of the coordination norm itself.
- **L-010:** Right empirical domain (adoption dynamics under social influence), but no signal of identified threshold nonmonotonicity or mechanism discovery.
- **seed-077 (Metric-Induced Preference Ratcheting):** Weak possible connection if paper shows that quantifying social influence shifts preference direction, but abstract does not suggest this analysis.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
