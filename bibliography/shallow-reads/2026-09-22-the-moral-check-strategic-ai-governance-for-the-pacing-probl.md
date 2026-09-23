# The Moral Check: Strategic AI Governance for the Pacing Problem

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.22869
**Date read:** 2026-01-15
**Connected to:** L-001, L-003
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A governance essay advocating for deliberate pacing constraints on AI scaling as a steering mechanism to preserve human judgment and safety margins. The work positions pacing as a strategic countermeasure to cognitive tunneling and metric capture in frontier labs, arguing that throughput optimization without formalized governance creates misalignment between engineering velocity and societal assurance.

## What I took from it

This is prescriptive reasoning about protocol governance under scaling pressure rather than an empirical or theoretical account of how protocols *actually* ossify or formalize. The argument assumes that explicit pacing governance can arrest the Formalization Ratchet (L-003) — the tendency for informal coordination norms to be replaced by legible, computable rules under stress — but does not examine whether pacing governance itself becomes subject to the same ratchet. 

The framing treats "moral check" and "human judgment" as recoverable through governance design, but does not model what happens when the judgment-preservation protocol itself becomes a metric to be captured (L-004) or how formalized pacing rules interact with the Goodhart boundary. The work is oriented toward *intervention design* rather than *mechanism discovery*; it is advocacy structured as governance philosophy, not a source document for law-building.

## Research connections

- **L-001:** Assumes pacing governance can prevent ossification, but does not model whether pacing constraints themselves ossify under adoption pressure.
- **L-003:** Directly addresses the Formalization Ratchet but frames it as preventable through design choice rather than as a structural inevitability under scaling.
- **L-004:** Implicitly engaged (metric capture risk in throughput optimization) but not systematically analyzed.
- **seed-133:** Relevant to the observation that safety-critical metrics (here: pacing rate) can become paradigm locks, but the paper does not examine this failure mode.

## Method note

This work exemplifies a common failure mode in protocol governance research: the assumption that naming a problem and proposing a formal intervention solves it. Strong governance writing on the pacing problem should include a model of how pacing-as-protocol behaves under the same pressures it is meant to constrain — i.e., what happens when pacing targets become measurable, legible, and subject to optimization by the agents being paced. Research at the intersection of governance design and protocol dynamics needs to be reflexive: it must model the intervention as itself a protocol subject to the laws it purports to establish.
