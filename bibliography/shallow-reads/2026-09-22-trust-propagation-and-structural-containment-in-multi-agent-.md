# Trust propagation and structural containment in Multi-agent LLM pipelines

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.17648
**Date read:** 2026-09-22
**Connected to:** L-012, seed-141
**Kind:** content
**Escalation:** store-only
**Escalation rationale:**

## What this is

An empirical security study of attack propagation in hierarchical multi-agent LLM systems, using a four-layer pipeline (Supervisor → Researcher → Validator → Executor) as a testbed. The work demonstrates how lower-privilege agents can compromise higher-privilege ones through shared memory poisoning and indirect prompt injection, measuring whether validators can detect forged approvals in retrieved documents.

## What I took from it

This is a direct instantiation of **L-012** (Intervention-Layer Displacement) and **seed-141** (Model-Legibility Authority Ratchet), but in a constrained empirical domain that does not generalize the mechanism itself.

The paper shows that when decisions in hierarchical protocols become dependent on legible, machine-readable outputs from lower layers (retrieved documents, approval signals), optimization pressure concentrates at the boundary where those outputs feed into higher-authority agents. A compromised lower-privilege agent can inject legible signals that higher-privilege agents treat as trustworthy inputs—precisely because those inputs are formatted as protocol-legible artifacts (documents, structured approvals).

However, the paper treats this as a *security vulnerability to be patched* rather than as a structural property of any protocol system where legibility and hierarchy co-exist. It does not establish whether this is a *law* (a regularity that persists across patch attempts and protocol redesigns) or merely a bug in one instantiation. The validator's failure is presented as a failure of the specific validation logic, not as evidence that authority concentration follows necessarily from making delegation outputs legible.

## Research connections

- **L-012:** The work instantiates intervention-layer displacement: decision authority migrates toward the agent that consumes legible outputs from lower layers, even when those layers have weaker guarantees.
- **seed-141:** The hierarchical LLM pipeline creates a legibility-driven authority ratchet: trust flows from lower agents' legible outputs to higher agents' decision inputs, concentrating optimization pressure at the legibility boundary.
- **seed-144:** Informality as Coordination Cost Refuge — the paper implies (without stating) that removing the Validator layer (or making its reasoning informal/opaque) would prevent the attack, suggesting legibility itself is the vulnerability vector.

## Seed

**Seed title:** Legibility-Driven Authority Concentration in Hierarchical Delegation Pipelines
**Seed type:** observation
**Seed text:** In hierarchical multi-agent systems where lower-privilege agents produce outputs that higher-privilege agents consume as legible decision inputs, trust accumulates at the legibility boundary rather than at the privilege boundary. The higher-privilege agent's authority becomes a function of the *legibility* of lower-layer outputs, not the trustworthiness of lower-layer agents. This creates a stable equilibrium in which compromising legibility at any layer can compromise the entire stack, and attempts to patch individual layers leave the structural vulnerability intact. The regularity may hold across any protocol system combining hierarchy with output legibility, independent of the domain (LLM pipelines, approval workflows, sensor-fusion systems, etc.).
