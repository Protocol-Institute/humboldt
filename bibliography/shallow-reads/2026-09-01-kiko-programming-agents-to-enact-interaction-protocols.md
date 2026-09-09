# Kiko: Programming Agents to Enact Interaction Protocols

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.26156
**Date read:** 2026-09-01
**Connected to:** L-003, L-005
**Kind:** tool/systems paper
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A programming model and toolkit for implementing decentralized multiagent systems where agents enact formal interaction protocols. The work addresses the gap between an agent's internal decision logic and its public protocol commitments by providing abstractions for decision making that preserve protocol invariants.

## What I took from it

This is competent systems work—it solves a real engineering problem (how to implement agents that reliably enact protocols without violating compatibility constraints). However, it operates *within* the assumption that protocols are already well-specified and stable. It does not investigate the conditions under which protocols become formalized, why formalization pressures arise, what resistance emerges during that process, or how formalizable abstractions fail to capture informal norms that keep real systems working.

The paper treats L-003 (Formalization Ratchet) and L-005 (Gall Generalization) as solved problems: it assumes you can write decision makers that satisfy protocol constraints, and that doing so is the right way to build robust systems. It does not ask whether the act of formalizing a protocol to the point where it can be programmed into agents systematically erases or damages the informal coordination structures that made the protocol work before. This is the opposite direction from where the inquiry points.

## Research connections

- **L-003 (Formalization Ratchet):** Kiko is a tool that *enables* formalization — it assumes the protocol is already legible enough to encode in a programming model. No evidence offered on whether or how this formalization changes the protocol's actual operation or creates new failure modes.
- **L-005 (Gall Generalization):** The paper claims safe evolution through constraint satisfaction but does not test this against complex, functioning systems being retrofitted to Kiko. No comparison to what is lost in the translation.
- **L-001 (Protocol Ossification):** Mechanizing protocols via Kiko might accelerate ossification by making modification require code changes rather than norm negotiation, but this is not studied.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**Classification note:** This is a well-executed tool paper. Store in systems/implementation archive. Does not warrant deep read under escalation criteria: it is not a primary theoretical or empirical argument about regularities in protocol systems; it does not challenge or extend the current laws; it introduces no new mechanism for how protocolized systems behave under pressure. It solves a problem *after* the formalization has already occurred.
