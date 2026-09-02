# CRAFT: Learn the Schema, Execute the Plan

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.22642
**Date read:** 2026-09-02
**Connected to:** L-003, L-012
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems engineering paper proposing post-training schema acquisition for enterprise coding agents, replacing the pattern of injecting exhaustive schema documentation into each prompt. The work is a deployment optimization study focused on inference overhead and schema evolution, not a primary theoretical or empirical investigation of underlying coordination or protocol dynamics.

## What I took from it

The paper illustrates L-003 (Formalization Ratchet) and L-012 (Intervention-Layer Displacement) in applied form: as enterprises move from ad-hoc schema communication (informal, adaptive) to formalized, post-trained schema representations (fixed, learnable), the locus of optimization and brittleness shifts. However, the paper does not *investigate* this shift — it accepts it as a deployment constraint and attempts to mitigate its costs (inference overhead, evolution difficulty) through technical means (post-training). It does not ask whether formalization itself creates new failure modes, coordination rigidity, or opacity in the agent-schema relationship.

The observation that "schema evolution complicates" in a formalized regime is noted but not interrogated as a mechanism. The work is pragmatic: it solves a known engineering problem without theorizing the protocol-level consequences of the formalization choice itself.

## Research connections

- **L-003 (Formalization Ratchet):** Confirms the empirical observation that schema knowledge moves from informal documentation injection to formal post-trained representation, but does not examine the resistance to schema modification or the conditions under which this transition becomes irreversible.
- **L-012 (Intervention-Layer Displacement):** The shift from prompt-level schema specification to learned representation is a displacement of the intervention locus, but the paper does not analyze where optimization pressure concentrates as a result.
- **seed-076 (Handler-Lodged Ossification in Opaque Protocols):** Post-trained schema knowledge becomes a "handler" — operationally crucial but interpretively opaque. Worth tracking whether this design pattern increases brittleness or slows schema iteration.

## Seed

**Seed title:** Schema Formalization Costs in Agentic Coordination
**Seed type:** observation
**Seed text:** When protocol schema knowledge transitions from legible, mutable, prompt-injected form to learned, post-trained form, schema evolution becomes harder and inference becomes cheaper. This is not merely a speed-accuracy tradeoff — it is a *localization of coordination cost*: flexibility is traded for consistency. The question is whether learned schemas create "handler-lodged" brittleness where the agent becomes unable to operate under schema drift, and whether distributed teams lose the ability to coordinate around schema changes once knowledge is embedded in model weights rather than documentary records. This pattern may generalize beyond coding agents to any system where coordination knowledge moves from explicit to embedded form.
