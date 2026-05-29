# From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2605.27547
**Date read:** 2026-05-29
**Connected to:** L-001, L-005, H-001
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems design paper proposing Risk-Aware Option Clearing (ROC), a coordination mechanism for mixed human-agent teams in safety-critical environments. The work addresses the gap between rigid static task allocation and opaque learned policies by introducing a protocol layer in which agents expose temporally extended capabilities with attached risk summaries.

## What I took from it

This is a solution paper rather than a laws-discovery paper. It demonstrates *awareness* of coordination costs and protocol brittleness (touching L-001, L-005), but does not investigate the *mechanism* by which these costs emerge or persist. The ROC mechanism itself appears to be a practical engineering response to known problems—exposing options + risk metadata to enable human-legible negotiation—rather than an empirical or theoretical investigation of why such intermediation becomes necessary.

The work does not test whether coordination costs are conserved or transferred across layers (H-001); it assumes a new protocol layer will reduce friction, but provides no measurement of costs before/after or at different levels of abstraction. Similarly, it does not examine whether trust accumulates independently of technical correctness (H-002), though the emphasis on human interpretability suggests an implicit hypothesis that legibility matters more than optimality for safety-critical coordination.

## Research connections

- **L-001:** The paper acknowledges that static protocols fail under adoption pressure (rigid task allocation doesn't scale to mixed teams) but treats this as a design problem, not a law-discovery opportunity.
- **L-005:** Implicitly respects Gall's principle by not proposing to redesign team coordination from scratch; instead, it layers an intermediary (options + risk summaries) between agents and humans.
- **H-001:** No empirical test of cost conservation across layers; assumes cost reduction through protocol redesign without measurement.

## Candidate laws or signals

none
