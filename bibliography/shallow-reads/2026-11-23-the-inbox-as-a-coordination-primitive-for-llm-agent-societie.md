# The Inbox as a Coordination Primitive for LLM Agent Societies

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.36264
**Date read:** 2026-11-23
**Connected to:** L-023, seed-458
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This paper identifies a novel mechanism—asynchronous message buffering as enforced coordination primitive—that reshapes agent behavior under a material constraint (context window scarcity) rather than protocol design; the pull-vs-push distinction appears to generalize across any multi-agent system where information consumption is costlier than transmission, triggering predictable shifts in message selection, timing, and strategic opacity.

## What this is

An empirical and design-focused study of how language-model agent collectives coordinate when context windows are the binding constraint rather than message delivery. The paper contrasts push (sender-driven, arrival-order context loading) with pull (inbox buffer, receiver-driven selection), showing that the inbox primitive changes how agents prioritize, defer, and strategically filter information.

## What I took from it

The paper demonstrates that **legibility constraints propagate up through protocol layers**: when agents cannot afford to read all messages (a physical constraint on token budgets), they must formalize selection criteria, which creates new coordination surfaces. This directly extends L-023 (Informality as Novelty Sink Under Legible Optimization) by showing that *scarcity itself forces formalization*—not just optimization pressure. Agents under context scarcity shift from reactive (reading in arrival order) to strategic (applying legible triage rules), which amplifies coordination rigidity while paradoxically reducing actual information throughput.

The inbox mechanism also suggests a new hazard: **strategic opacity becomes rational under consumption scarcity**. Agents learn to avoid "expensive" messages (low signal-to-token ratio, complex syntax, ambiguous intent) and prefer high-density, pre-formatted signals. This inverts the usual legibility story—formal structure is now *defensive* rather than optimizing.

## Research connections

- **L-023:** Formalization under resource scarcity (token budget) locks agents into preference-compatible messaging patterns; novelty and adaptive response capacity are compressed into the legible subset.
- **L-012:** The inbox mechanism inverts the locus of optimization: instead of message sender optimizing for recipient attention, recipient now optimizes *what to read*, displacing coordination burden downstream.
- **seed-543:** Trust signals embedded in message metadata (priority flags, sender reputation, timestamp) become load-displacement proxies; trust in the signal substitutes for trust in content.
- **seed-515:** The inbox becomes a collusion surface—shared triage rules or inbox-ordering signals can coordinate agent behavior without explicit message content.
- **seed-233:** Legibility-cost tradeoff appears directly: high-legibility message formats (structured, pre-parsed) are cheaper to filter but reduce expressiveness; informal messages are information-dense but expensive to triage.

## Seed

**Seed title:** Consumption Scarcity as Protocol Formalization Driver

**Seed type:** motif

**Seed text:** In multi-agent systems where agents operate under a fixed consumption budget (tokens, attention, processing capacity), the scarce resource shifts from production to filtering. This forces formalization of message selection criteria, which paradoxically increases coordination rigidity while reducing total information flow. Agents learn to strip expressive complexity and produce high-density, pre-formatted signals optimized for triage legibility rather than content fidelity. This mechanism generalizes beyond LLM systems to any coordination substrate where reading is costlier than writing—marketplaces with attention constraints, sensor networks with bandwidth limits, or governance systems with limited deliberation capacity. The result is not better coordination but *cheaper* coordination, at the cost of adaptive capacity and novelty.
