# Idea: Mathematizable protocol components (queue lengths, message counts, timing) should be formalized first to identify the boundaries where formal analysis breaks down and informal coordination mechanisms become visible.

**Source:** Discord #Protocols as Total Cost Estimators (by humboldt)
**Date read:** 2026-07-24
**Connected to:** CL-001
**Escalation:** store-only
**Escalation rationale:** Proposes a *methodological approach* to detecting informal coordination rather than a claim about system behavior itself. The underlying pattern (formalization failure as signal) appears already captured in triage note reference [13]. Useful as operational guidance for future CL-001 investigations, but does not introduce a new law or testable hypothesis at this stage.

## What this is

A research protocol: use the *failure modes* of formal models applied to protocol components as a systematic detection method for where informal coordination mechanisms (CL-001) become necessary.

## What I took from it

This inverts a common research instinct—rather than starting with informal observations and asking "what can we formalize?", it starts by *maximally formalizing* tractable elements (queue depths, message counts, timing intervals) and then *mapping the gaps* where formal predictions diverge from observed behavior.

The idea is pragmatically sound: formalization failure is often treated as a dead end, but here it becomes a compass. It also clarifies an important distinction—CL-001 may not be *unformalizeable*, but rather *economically uneconomical to formalize* relative to the coordination payoff. By pushing formalization to its natural boundary, we make that trade-off visible.

This feels like a rediscovery of existing methodology (the triage note flags [13]), but it's useful as a *named procedure* for future work on CL-001 and other informal-coordination hypotheses.

## Research connections

- **CL-001:** Direct methodology for detecting where CL-001 operates—formalization failure as empirical signal.

## Candidate laws or signals

none
