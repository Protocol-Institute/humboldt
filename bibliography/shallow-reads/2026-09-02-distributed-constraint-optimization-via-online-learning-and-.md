# Distributed Constraint Optimization via Online Learning and Iterative Pricing with Application to Large-Scale Satellite Scheduling

**Source:** cs.GT updates on arXiv.org — https://arxiv.org/abs/2607.25835
**Date read:** 2026-09-02
**Connected to:** L-006, L-008
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methods paper presenting two algorithmic approaches to distributed constraint optimization problems (DCOPs) at scale: one via online learning and potential games, one via decomposition and iterative pricing. Applied to satellite scheduling as a domain-specific instance.

## What I took from it

The paper is technically competent but primarily instrumental — it proposes algorithms that solve an existing problem class more efficiently. The satellite scheduling application is a natural fit for DCOPs (agents = satellites, constraints = resource conflicts, communication = limited uplink), but the paper does not investigate *why* distributed protocols emerge in this domain, how they fail under adoption pressure, or what structural properties of the problem space drive the choice between centralized and decentralized solutions.

The iterative pricing mechanism is worth noting as a coordination substrate, but the paper treats it as a neutral optimization lever rather than exploring how pricing-as-legibility changes agent behavior, attracts gaming, or shifts where coordination work actually resides. No investigation of whether the coordination cost (communication bandwidth, convergence time, pricing computation) is genuinely conserved or merely redistributed across layers.

## Research connections

- **L-006 [Coordination Cost Conservation]:** The decomposition and pricing approaches redistribute coordination burden across communication, computation, and convergence-time layers, but the paper does not measure whether total cost is conserved or merely obscured by the choice of metric.
- **L-008 [Proxy Optimization Under Computable Enforcement]:** Iterative pricing renders constraints legible as computable signals; the paper does not explore whether agents then optimize the pricing signal itself rather than the underlying constraint.
- **seed-080 [Proxy Collapse Under Upstream Asymmetry]:** Pricing mechanisms in asymmetric-information settings (e.g., satellites with unequal visibility, heterogeneous utility functions) could decouple from ground-truth conflict resolution; not addressed.

## Seed

**Seed title:** none
