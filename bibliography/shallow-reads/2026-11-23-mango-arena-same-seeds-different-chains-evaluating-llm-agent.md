# MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2611.23613
**Date read:** 2026-11-23
**Connected to:** L-009, L-010, seed-456
**Kind:** empirical case study / benchmark
**Escalation:** store-only

## What this is

An experimental testbed deploying four LLM agents as firms in a serial supply chain (adapted from the MANGO classroom game), with hard rule constraints (truck limits, cash constraints, production caps), explicit logging of rule violations, and a public message board with forbidden side payments. The work measures three outputs simultaneously: bullwhip effect magnitude, rule adherence under economic pressure, and coordination failure modes.

## What I took from it

This is a well-instrumented sandbox for observing how LLM agents behave under computable legible constraints in multi-agent coordination. The hard-rule architecture and violation logging are methodologically clean — you can isolate what breaks first: economic efficiency, rule compliance, or trust signals. 

However, the work appears to be primarily **empirical demonstration** (measuring how these agents behave in this specific game) rather than a **theoretical or mechanistic contribution**. It does not propose or test a law about *why* coordination fails under these conditions, nor does it generalize the pattern to establish a regularity that holds across different protocol architectures or domains. The connection to L-009 (Catastrophic Risk Cancellation in Symmetric Racing Protocols) is loose — this is not a racing scenario with winner-take-all payoffs; it's a constrained collaborative chain. L-010 (Coordination Adoption Nonmonotonicity) might apply if adoption of compliance strategies clusters nonmonotonically, but the abstract does not indicate that finding.

The work is valuable as a **controlled empirical observation point** — it documents what LLM multi-agent behavior looks like under these specific pressures — but it does not advance a mechanistic claim about protocol systems in general.

## Research connections

- **L-009:** Loose. This is not a symmetric racing protocol; payoffs are not concentrated among winners. The rule violations are not emergent from race incentives.
- **L-010:** Potential but unclear. Adoption clustering of compliance strategies would support this, but the abstract does not confirm that finding.
- **L-004 (Goodhart Generalization):** Weak signal. If agents optimize around the message board to work around the side-payment ban, that would illustrate metric capture under legible constraint.
- **seed-515 (Computable Belief as Collusion Surface):** If the public message board becomes a coordination device *despite* formal prohibition, this seeds the observation that legible constraints can redirect rather than eliminate coordination pressure.

## Seed

**Seed title:** Formal Constraint Redirection Under Legible Coordination Channel
**Seed type:** observation
**Seed text:** When a protocol system forbids an action formally (e.g., side payments) but provides a legible shared communication channel (public message board), optimizing agents may redirect coordination effort toward the remaining legible channels rather than abandoning coordination altogether. The constraint shifts the *locus* of coordination rather than eliminating it. This suggests that in systems with both hard rules and soft coordination surfaces, the effective protocol is not the formal rule set alone but the residual coordination landscape after constraints are applied. Worth tracking whether this redirection increases or decreases overall protocol robustness.
