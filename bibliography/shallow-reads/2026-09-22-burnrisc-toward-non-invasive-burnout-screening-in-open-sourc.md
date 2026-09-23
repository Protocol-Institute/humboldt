# BurnRiSc: Toward Non-Invasive Burnout Screening in Open Source from Public Repository Signals

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.19422
**Date read:** 2026-09-22
**Connected to:** L-001, L-013
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** —

## What this is

A systems observation paper proposing computational detection of maintainer burnout in open source using repository signals (commit patterns, response latency, etc.) rather than self-report. The core claim is that open source governance tolerates progressive system degradation without institutional intervention mechanisms to detect or arrest it.

## What I took from it

This is a diagnostic of L-013 *in action* — the paper documents exactly the phenomenon: open source communities have accumulated evidence of maintainer collapse (departure cascades, infrastructure brittleness) without triggering formal detection or remediation protocols. The system *sees* the problem only post-hoc, after withdrawal occurs.

The paper's framing also illuminates a secondary mechanism: the absence of a *legible, non-invasive* observation layer means that the only available signal is self-report (which sufferers systematically avoid), creating an observation bottleneck. This suggests a variant of L-012 — the intervention layer (burnout detection) has been displaced entirely outside the protocol, leaving only informal social channels. The proposed technical solution (repository signal inference) attempts to re-legibilize a hidden state without requiring agent disclosure.

The work also hints at L-001: the protocol (open source contribution norms) ossifies precisely because detection and redistribution mechanisms never formalize. Maintainers cannot be reallocated or offloaded because no protocol layer exists to make workload legible or negotiable.

## Research connections

- **L-001:** Open source protocol lacks formal reallocation mechanisms; workload becomes opaque until failure.
- **L-013:** Paradigm-locked anomaly tolerance — field tolerates repeated maintainer departures without institutional response protocol.
- **L-012:** Intervention-layer displacement — burnout detection has been pushed outside formal protocol to informal social observation only.
- **seed-144:** Informality as coordination cost refuge — the system tolerates undetected burnout because formal workload negotiation has no protocol.
- **seed-131:** Context legibility as failure attribution boundary — repository signals remain invisible until interpreted post-mortem.

## Method note

This paper models a useful research move: identifying *where a protocol system has failed to formalize observation of a known failure mode*. Rather than proposing new metrics, the authors diagnose why the existing metric (self-report) is structurally unreliable in this domain and propose a legibility layer. This suggests that law-hunting should routinely include "what should the system be detecting but cannot?" as a framing question. The absence of an observation protocol is itself evidence of a law — it points to why formalization has not occurred (cost, privacy, institutional inertia, paradigm lock).
