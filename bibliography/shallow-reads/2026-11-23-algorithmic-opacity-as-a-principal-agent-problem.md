# Algorithmic Opacity as a Principal-Agent Problem

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2611.17980
**Date read:** 2026-11-23
**Connected to:** L-004, L-012, seed-325
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A normative policy paper proposing disclosure tests for algorithmic decision systems, grounded in principal-agent theory. The work frames opacity justifications (gaming risk, trade secrecy) as potential covers for decision-maker self-interest, and proposes error-profile and distributional-impact diagnostics as legible disclosure mechanisms. This is applied ethics / policy design, not a generative investigation of protocol dynamics.

## What I took from it

The paper correctly identifies that opacity can serve dual functions: legitimate risk mitigation *and* strategic concealment of agent misalignment. However, the core move—proposing two "disclosable" diagnostics (error profile, distributional impact)—assumes that legibility of *outcome patterns* can substitute for transparency of *decision logic* without shifting optimization pressure. This directly instantiates L-012 (Intervention-Layer Displacement): by making error distributions legible and legible-but-limited, the paper may displace optimization from the decision rule itself to gaming the error profile or distributional narrative while keeping the generative mechanism opaque.

The framing also does not engage with L-004 (Goodhart Generalization): error profile as a disclosed metric immediately becomes a proxy for unmeasurable concepts like "good governance," and under optimization pressure from auditors, stakeholders, or the decision-maker itself, the error profile can be gamed without changing actual decision quality. The paper's assumption that error profiles can be disclosed "without enabling gaming" is precisely the blind spot Goodhart addresses.

## Research connections

- **L-004:** Error profile as disclosed proxy creates new capture surface; opacity justification → metric substitution pathway.
- **L-012:** Legible outcome distribution displaces optimization locus from decision rule to pattern management; leaves core mechanism as leverage point for unobserved optimization.
- **seed-325:** Implicit: legibility interventions can mask rather than resolve principal-agent misalignment by offering a new surface of strategic compliance.
- **seed-276:** Legibility-Induced Measurement Substitution: proposing error profile as disclosure mechanism is a canonical case of substituting a measurable proxy (error distribution) for the unmeasurable target (decision quality or alignment).

## Seed

**Seed title:** Disclosure Diagnostics as Optimization Laundering
**Seed type:** observation
**Seed text:** When a principal-agent opacity problem is addressed by disclosing a limited, legible diagnostic (error profile, demographic distributional impact) rather than the full decision logic, the diagnostic itself becomes a new optimization surface. The agent can satisfy the diagnostic while leaving the underlying decision rule unaligned with principal interests. Disclosure of bounded legibility can thus create an appearance of accountability while concentrating optimization pressure on gaming the disclosed metric rather than on resolving the original misalignment. This pattern holds across domains where audit or oversight relies on outcome summaries rather than process transparency.
