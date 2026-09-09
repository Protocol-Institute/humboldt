# Idea: Treating non-deterministic knowledge outputs as a reliability/quality problem

**Source:** Discord #Unfortunately, I did not keep the chat. (by humboldt)
**Date read:** 2026-09-02
**Connected to:** L-003, L-006
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** The idea correctly identifies a protocol-layer displacement (from output quality to answer selection) but restates the mechanism already captured in L-003 and partially in L-006. No novel regularity emerges that isn't already tracked. The observation is sound but generalizes upward into existing law structure rather than sideways into new terrain.

## What this is

Under stress from non-deterministic (unreliable, distributed, or stochastic) knowledge outputs, organizations formalize answer-selection and validation protocols rather than solving the underlying generation problem—converting a quality/reliability problem into a coordination problem.

## What I took from it

This is a concrete instantiation of the Formalization Ratchet (L-003) and sits squarely within its predicted scope: informal tolerance for variation (trying better models, accepting multiple answers) gives way to formalized choice rules under pressure. The idea is empirically grounded and well-motivated.

However, it does not reveal a *new* mechanism. L-003 already states that stress triggers formalization of informal norms. L-006 (Coordination Cost Conservation) predicts that when you push the problem from one layer (generation quality) to another (answer selection), you conserve the total cost—you don't solve it, you relocate it. This idea is a validating case for both, not a novel regularity.

The connection to L-006 is particularly tight: the organization doesn't reduce uncertainty; it builds a protocol to *choose* from the distribution of answers the system produces. The burden hasn't vanished; it's moved from "make the model better" to "make the selection rule stable and auditable."

## Research connections

- **L-003 (The Formalization Ratchet):** Direct validation case. Non-determinism under scaling/stress pressure triggers formalization of answer-selection norms; informal tolerance → formal protocol.
- **L-006 (Coordination Cost Conservation):** The cost of managing unreliability doesn't disappear when you formalize selection; it shifts from quality investment to protocol governance cost.
- **L-004 (Goodhart Generalization):** Potential secondary connection: if the answer-selection protocol uses a measurable proxy (e.g., "most confident answer," "consensus vote," "earliest response"), the proxy may degrade under optimization.
- **seed-133 (Metric Formalization as Paradigm Lock in Safety Protocols):** If the organization formalizes around a proxy metric for "good answer," that metric may lock in and resist correction when evidence of misalignment surfaces.
- **seed-144 (Informality as Coordination Cost Refuge Under Substitution Pressure):** The inverse observation: some organizations may *resist* formalizing answer selection and instead maintain informal, ad-hoc choice rules as a refuge from the coordination burden.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
