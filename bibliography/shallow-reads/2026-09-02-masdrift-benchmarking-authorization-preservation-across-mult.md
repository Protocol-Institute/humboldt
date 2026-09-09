# MasDrift: Benchmarking Authorization Preservation Across Multi-Agent Architectures

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2608.07556
**Date read:** 2026-09-02
**Connected to:** L-005, L-012
**Kind:** benchmark/tool paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A benchmark measuring whether delegated goals in multi-agent systems preserve their original authorization boundaries across different coordination architectures. The work constructs 600 benign tasks across eight domains, each pairing required work with reserved actions, and compares authorization drift under single-agent, centralized, and decentralized coordination patterns.

## What I took from it

This is a competent engineering study that operationalizes a real problem—goal delegation creates authorization leakage—but it does so as a containment evaluation rather than as mechanism discovery. The paper measures *whether* drift occurs across architectures but does not articulate *why* delegation architectures necessarily decouple authorization intent from execution authority, nor does it establish a generalizable condition under which this decoupling becomes inevitable.

The connection to L-012 (Intervention-Layer Displacement) is surface-level: the paper documents that the locus of authorization control shifts across coordination layers, but does not probe whether this is a consequence of formalization, optimization pressure, or structural asymmetry in how goals are legible to subagents. L-005 (Gall Generalization) is mentioned in the triage note but the paper does not engage with the claim that functional systems resist safe restructuring; instead it benchmarks how much drift *is tolerable* under different architectures—a safety engineering question, not a law-seeking one.

## Research connections

- **L-005:** The paper shows that authorization boundaries in delegated systems are fragile, but does not test whether attempting to preserve them creates latent brittleness or coordination cost displacement (the core claim of L-005).
- **L-012:** Documents that authorization legibility shifts across coordination layers, but does not establish whether this displacement is driven by optimization pressure on computable proxies or is a necessary consequence of decentralization.
- **seed-066 (Control Inversion Under Computable Compliance):** Tangentially relevant—the paper operationalizes reserved actions as computable constraints, but does not examine whether legibility of those constraints becomes itself a target of optimization.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**RATIONALE FOR STORE-ONLY:** This is a tool paper (benchmark construction) that documents a phenomenon (authorization drift in delegated multi-agent systems) but does not present a sustained theoretical argument or introduce a mechanism absent from the current inventory. It measures containment rather than discovers law. It should be indexed as a reference for L-012 and L-005 evaluation but does not warrant deep read unless a future paper uses MasDrift to isolate a causal mechanism or to test a prediction about when authorization preservation becomes computationally impossible.
