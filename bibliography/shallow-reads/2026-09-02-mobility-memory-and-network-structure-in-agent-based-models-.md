# Mobility, Memory, and Network Structure in Agent-Based Models of Convention Tipping and Convergence

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.07810
**Date read:** 2026-09-02
**Connected to:** L-010, seed-052
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An agent-based model studying how spatial mobility, memory constraints, and network topology jointly influence convention-tipping thresholds—the critical conditions under which a minority minority can overturn an incumbent behavioral norm. The work is domain-specific (convention dynamics) and appears to be a competent methodological contribution to multi-agent simulation rather than a primary theoretical argument about protocol systems generally.

## What I took from it

The paper tests L-010 (Coordination Adoption Nonmonotonicity) by introducing realistic constraints—bounded memory and localized mobility—into a tipping-point model. This is valuable empirical work on *when and how* adoption curves become non-monotonic under spatial friction. However, the contribution appears to be parametric rather than mechanistic: it documents that mobility, memory, and topology *matter* and interact, but the abstract does not yet signal a novel generalizable mechanism about how protocol systems behave under adoption pressure.

The work is most valuable as a probe into the microstructure of L-010. If the findings show that coordination adoption becomes predictably *easier* under certain mobility regimes and *harder* under others (nonmonotonically), that would sharpen the law. But the current read does not reveal the directionality or the abstract principle governing when memory decay aids versus impedes tipping.

## Research connections

- **L-010:** Tests coordination adoption nonmonotonicity empirically; adds spatial friction and memory constraints to the tipping-point model.
- **seed-052:** Implied by triage note; not examined in detail here.

## Seed

**Seed title:** Memory Decay as Tipping Substrate Modifier

**Seed type:** question

**Seed text:** In coordination systems where agents hold local memory of peer states (not global history), does bounded memory horizon act as a *noise filter* that destabilizes incumbent conventions, or as a *stabilizing friction* that raises tipping thresholds? The answer may depend on whether the minority signal is spatially clustered or distributed. If memory decay selectively erases minority-generated coordination signals before they propagate, it may raise the effective minority threshold; if it erases incumbent-convention reinforcement equally, it may lower it. This generalizes beyond convention tipping to any protocol where peer-state legibility and retention jointly govern cascade dynamics.
