# Constitutional governance for societies of AI agents in the built environment: a research agenda

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.23336
**Date read:** 2026-09-02
**Connected to:** L-001, L-003
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A research agenda paper proposing a shift in framing for multi-agent AI governance in physical infrastructure (buildings, streets, cities) — from single-agent safety to multi-agent coordination problem. The work identifies that autonomous systems are being deployed faster than their collective behavior is studied, and positions "constitutional governance" as a potential framework for negotiating conflicts among heterogeneous stakeholders (occupants, owners, operators, regulators, artificial agents).

## What I took from it

The paper confirms the **formalization pressure** documented in L-003 (Formalization Ratchet) by identifying built environment governance as a domain where informal coordination norms cannot scale with agent density and heterogeneity. It frames the transition from tool-centric to society-centric modeling as necessary under scaling pressure.

However, the work is primarily *programmatic* — it identifies the problem space and proposes a research direction rather than presenting sustained empirical or theoretical argument about how formalization actually proceeds, what gets locked in, or what the failure modes are. It does not provide mechanisms for ossification (L-001), nor does it probe what happens to coordination costs when governance is formalized (L-006). The "constitutional" framing is borrowed but not analyzed for its applicability to artificial agent societies.

The most interesting aperture is the implicit claim that built environments constitute a **test domain for multi-stakeholder protocol design** — but this remains a framing, not a mechanism or law fragment.

## Research connections

- **L-001:** Confirms scaling pressure driving protocol formalization; does not examine ossification dynamics or adoption lock-in in this domain.
- **L-003:** Directly supported — informal norms in built environment governance being replaced by formalized coordination rules as agent density increases.
- **L-006:** Implicit claim that coordination cost is being displaced across institutional layers (occupant → operator → regulator → artificial agent); not examined empirically.
- **seed-070:** Obligate-Coordination-as-Infrastructure-Constraint — built environment is infrastructure; coordination becomes load-bearing constraint on agent deployment.

## Seed

**Seed title:** Heterogeneous-Stakeholder Protocol Ossification Under Physical Constraint
**Seed type:** motif
**Seed text:** In protocol systems governing shared physical resources where stakeholders have asymmetric control and verification authority (occupants cannot inspect operator decisions; regulators cannot observe real-time occupant preferences), formal coordination rules tend to ossify around the most legible enforcement layer rather than the most effective coordination mechanism. The built environment is a test domain: as agent density increases, governance formalization will concentrate authority in layers with direct observability of agent behavior (operators, systems logs), while displacing coordination costs onto less-formalized layers (occupant negotiation, regulatory lag). Track whether formalization here reproduces L-001 or produces novel resistance patterns.
