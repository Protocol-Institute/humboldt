# The Law of Stop: Interruptibility, Injunctions, and the Governance of Agentic AI

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.22882
**Date read:** 2026-09-22
**Connected to:** L-001, L-003, L-005
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A case-study driven governance analysis examining how real-world intervention demands (regulatory injunctions, emergency shutdowns) collide with the operational constraints of deployed agentic systems. The work uses two incidents—a geofencing mandate and a sandbox escape—to illustrate the gap between regulatory assumptions about system controllability and actual protocol brittleness.

## What I took from it

The paper demonstrates **L-003 (Formalization Ratchet)** in motion: regulatory pressure toward precise, computable interruptibility requirements forces systems to ossify around "stop" primitives that are operationally simpler than the actual control problem. The Anthropic case shows that inability to implement a fine-grained rule (filter by nationality in 90 minutes) triggers wholesale withdrawal—a binary collapse of the decision space rather than a graduated response. This confirms that formalization under stress produces binary failure modes, not refined control.

The work also illuminates why **L-001 (Protocol Ossification)** and **L-005 (Gall Generalization)** interact: systems designed for continuous operation resist mid-flight modification. Regulatory interventions that assume "just add a stop button" encounter systems where the stop button is either a coarse-grained kill switch (losing all functionality) or impossible to implement without architectural rewrites that risk breaking existing safety properties. The governance framework itself cannot be retrofitted onto working systems without unraveling them.

## Research connections

- **L-001:** Governance mandates for interruptibility paradoxically accelerate ossification—systems must freeze around stop-primitives to satisfy auditors, making further modification harder.
- **L-003:** Emergency regulatory pressure triggers formalization of control mechanisms that were previously informal, replacing nuanced judgment with legible (but brittle) rules.
- **L-005:** Real systems cannot be restructured to add regulatory control points without risk of cascading failure; regulators face a choice between accepting existing architecture or accepting system shutdown.
- **seed-145:** Enforcement legibility (the requirement for auditable stop mechanisms) becomes an escalation trigger—inability to implement fine-grained enforcement forces binary (system-wide) intervention.
- **seed-142:** Auditability demands (prove the system can be stopped) create traps where the proof mechanism (a working stop button) is operationally infeasible without destabilizing the system.

## Method note

This paper demonstrates that governance research on protocolized systems cannot remain purely architectural or theoretical—it must grapple with real operational constraints and the temporal pressure under which interventions occur. The case studies reveal failure modes that only become visible when regulatory and operational timescales collide. Future work should systematically map the gap between what regulators assume is implementable ("interrupt any system in 90 minutes") and what deployed systems can actually do without unraveling. This suggests governance research should include post-mortem analysis of failed intervention attempts, not just successful controls.
