# QueenBee: A Recursively Self-Improving Harness for Communication Topology Design in LLM-Based Multi-Agent Systems

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.27492
**Date read:** 2026-11-23
**Connected to:** L-023, seed-458
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A tool paper presenting QueenBee, a framework for iteratively redesigning communication topologies in LLM-based multi-agent systems. The work focuses on workflow-as-code abstraction and experience reuse to avoid redundant topology search rather than proposing a theoretical mechanism or empirical law about protocol behavior.

## What I took from it

The paper operationalizes topology design as a learnable, reusable domain — storing and retrieving past communication patterns to seed future designs. This is competent systems work but does not establish a *regularity* about how adaptive protocols behave under pressure or scale.

The triage note flags L-023 (Informality as Novelty Sink Under Legible Optimization), which claims that formal optimization pressure suppresses output diversity. QueenBee's design *assumes* the opposite: that sustained experience reuse preserves functional novelty by avoiding rote pattern ossification. This is a surface tension worth noting, but the paper does not investigate the mechanism or test the boundary conditions. It describes an engineering solution (experience pools, DAG reuse) without probing when or why such solutions fail.

The underlying question — whether accumulated coordination experience naturally prevents topology ossification or merely delays it — is live, but this paper does not contribute empirical evidence or mechanism clarity. It is a case study in one domain with one technique.

## Research connections

- **L-023:** QueenBee assumes that legible optimization (via experience pool + DAG reuse) can sustain novelty; the law claims the opposite. No direct test here, but the assumption deserves scrutiny.
- **seed-458:** Referenced as connected; no claim about how or why recursive topology design maintains novelty under what conditions.
- **L-011 (Causal Detachment):** Tangentially: if communication topologies become autoregressive (each agent's input is prior agent output), operationally functional but causally decoupled configurations may be stable; QueenBee does not examine this risk.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
