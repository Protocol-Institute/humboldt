# Idea: Protocol theory could be used to estimate systems' total cost of ownership, extending protocol analysis into resource and sustainability accounting.

**Source:** Discord #🎩-formal-protocol-theory (by 4umd)
**Date read:** 2026-07-24
**Connected to:** CL-002
**Escalation:** store-only
**Escalation rationale:** Idea proposes an operationalization method for an existing hypothesis rather than a novel structural claim. Warrants observation and method development, but does not yet constitute a testable law or falsifiable hypothesis in its current form.

## What this is

The claim that total cost of ownership (TCO) metrics can serve as an empirical proxy for measuring coordination costs as protocols transition between architectural layers or system boundaries.

## What I took from it

This idea attempts to bridge protocol theory into resource accounting — a natural extension, but one that requires clarification about what is being measured. If CL-002 posits that coordination costs are conserved (or transferred) across protocol layers, then TCO provides a measurement surface. However, the idea remains soft because:

1. **Measurement conflation risk:** TCO typically aggregates operational, maintenance, and capital costs. It is not clear whether all components of TCO correlate with *coordination cost* specifically, or whether TCO simply aggregates heterogeneous resource expenditures that mask rather than reveal protocol-layer dynamics.

2. **Valuable if scoped:** If the idea is narrowed to claim that *coordination overhead* (time, tokens, state synchronization) can be quantified through TCO decomposition, it becomes a useful operationalization. This would require disaggregating TCO by cost source (e.g., verification overhead, consensus round-trips, storage redundancy) and mapping each to layer transitions.

3. **Opens comparative protocol analysis:** Using TCO as a proxy could enable empirical comparison of protocol families (e.g., PoW vs. PoS vs. state channels) and support or refute CL-002 through cost-transfer patterns across abstraction levels.

## Research connections

- **CL-002:** TCO decomposition could test whether coordination costs are conserved or shifted when protocols abstract or delegate functions to lower layers.

## Candidate laws or signals

**CL-4umd-TCO-001 (preliminary):** Coordination cost conservation in protocol transitions can be operationalized and tested by decomposing total cost of ownership into layer-specific expenditures and tracking cost redistribution across abstraction boundaries.

*(Status: Requires operationalization. Next step: develop disaggregation schema for TCO in protocolized systems and validate against 2–3 case studies before promoting to hypothesis.)*
