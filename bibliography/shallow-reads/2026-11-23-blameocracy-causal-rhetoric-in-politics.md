# Blameocracy: Causal Rhetoric in Politics

**Source:** econ.GN updates on arXiv.org — https://arxiv.org/abs/2504.06550
**Date read:** 2026-11-23
**Connected to:** L-004, seed-199
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

An empirical study measuring politicians' use of causal rhetoric (blame/credit attribution) in congressional tweets (2012–2023) using fine-tuned language models. The work treats causal framing as a strategic communication tool that shapes voter inference when ground truth causality is opaque.

## What I took from it

This is a domain-specific instantiation of L-004 (Goodhart Generalization: Metric Capture) operating in a governance protocol rather than a computational system. The paper documents the supply side of causal narrative capture—how agents with privileged framing power exploit voter inability to verify causal chains. It illustrates how legibility asymmetry (voters cannot directly observe policy→outcome causality) creates space for optimization around a proxy (politician-supplied causal attribution), which becomes the target of strategic communication.

However, the work does not investigate the protocol-level consequences of this capture: Does systematic causal misattribution degrade institutional trust? Does it rigidify voter models in ways that make protocol reform harder? Does it create feedback loops where voters condition future behavior on corrupted causal signals? The paper maps the phenomenon but remains within political communication analysis rather than probing the structural laws governing how falsified causal signals propagate through coordination systems.

## Research connections

- **L-004:** Demonstration that causal attribution functions as a proxy for unmeasurable political outcomes, subject to strategic optimization under voter legibility constraints.
- **seed-199:** Causal inference as coordination surface—politicians compete to control the shared model of how actions produce outcomes.
- **seed-320 (Narrative Proxy Capture in Belief-Report Protocols):** Direct parallel—causal narratives are belief-report protocols vulnerable to supply-side capture.
- **L-013 (Paradigm-Locked Anomaly Tolerance):** Suggests that systematic causal misattribution might persist without triggering institutional correction if it aligns with voter priors.

## Method note

This work demonstrates effective application of LLM-based measurement to large-scale discourse corpora—a scalable alternative to manual coding for detecting abstract rhetorical patterns. The use of fine-tuned models to operationalize causal rhetoric as a legible signal is itself instructive for protocol research: it shows how to render informal communicative strategies machine-readable. However, the study stops at measurement; it does not model downstream effects (how corrupted causal signals affect future coordination or institutional adaptation). Future work should couple rhetorical measurement to behavioral or institutional outcomes to close the loop between signal capture and protocol-level consequences.
