# When Should AI Follow? Task Structure and Joint Adaptation by Human and AI Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2504.20903
**Date read:** 2026-09-02
**Connected to:** L-012, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A computational model of task division between human and AI agents, parametrized by memory regime (recency-weighted vs. uniform). The paper investigates which decision-sequencing architectures should assign leadership to which agent type under different task structures, treating memory as the sole differentiator between agent classes.

## What I took from it

The paper operationalizes a narrow but clean mechanistic distinction—recency bias vs. scale-free memory—and uses it to predict task allocation equilibria. This is competent and relevant to L-012 (Intervention-Layer Displacement), insofar as it demonstrates that formalizing *where* a decision sits in a protocol sequence is itself a choice that reshapes optimization pressure. However, the work does not investigate what happens *after* that choice is made: it does not track whether the formalization of task boundaries itself becomes a target of optimization, whether agents learn to game the boundary, or whether the legibility of the memory regime invites strategic adaptation. The paper treats memory regime as fixed and external; it does not ask whether agents under computable audit (seed-128) will converge on exploiting the boundary itself.

The contribution is task-design engineering, not a mechanism of protocol dynamics. It confirms that task structure matters to outcome, but does not isolate a law about how formalization of task structure changes agent behavior *over time*.

## Research connections

- **L-012:** Task sequencing is an intervention-layer choice; the paper shows this choice is consequential, but does not track how legibility of the boundary invites optimization pressure.
- **seed-048:** Memory regime as capability asymmetry is correctly identified; the paper does not investigate whether this asymmetry becomes the target of strategic behavior once the boundary is formalized.

## Seed

**Seed title:** none

**Seed type:** 

**Seed text:**
