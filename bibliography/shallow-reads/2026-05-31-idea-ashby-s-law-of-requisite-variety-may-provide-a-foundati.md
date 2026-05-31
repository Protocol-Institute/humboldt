# Idea: Ashby's Law of Requisite Variety may provide a foundation for deriving a corollary law about information processing requirements across protocol layer transitions

**Source:** Discord #new-nature (by _vgr)
**Date read:** 2026-05-31
**Connected to:** H-001, L-002
**Escalation:** store-only
**Escalation rationale:** Promising formal grounding for an active hypothesis; does not yet constitute a distinct empirical claim about protocolized systems, but warrants observation as H-001 develops.

## What this is

Ashby's Law (system controller must possess at least as much complexity as the system it controls) may formalize the mechanism by which coordination costs are conserved or transformed when protocols transition between abstraction layers, rather than eliminated.

## What I took from it

This is a useful *structural lens* rather than a novel observation about artificial systems. The idea correctly identifies that H-001 (coordination cost conservation) lacks formal grounding—it currently rests on empirical pattern-matching. Ashby's Law offers a candidate mechanism: if a protocol system exhibits V bits of variety, any layer-transition that obscures or simplifies that variety must route it somewhere (into implementation complexity, governance overhead, monitoring infrastructure, or user friction). The claim does not predict *where* complexity goes, only that it cannot vanish.

This refines rather than challenges the current inventory. It aligns with L-002 (Hardness Asymmetry), which already captures asymmetric cost distribution; Ashby's formulation would explain *why* such asymmetries are inevitable rather than contingent.

The idea opens a testable pathway: measure variety at protocol layer N and layer N+1, then track where unmeasured complexity re-emerges.

## Research connections

- **H-001:** Ashby's Law provides a formal constraint on whether coordination costs can be genuinely conserved vs. merely displaced across transitions.
- **L-002:** Hardness Asymmetry may be a *consequence* of requisite variety rather than an independent phenomenon—the verification function's lower cost reflects compressed variety, while circumvention costs reflect variety re-emergence elsewhere.
- **L-003:** The Formalization Ratchet could be reframed as a manifestation of variety management: formalization *increases measurable variety* in rules, often at the cost of hidden variety in enforcement and exception-handling.

## Candidate laws or signals

**CL-vgr-001:** *Variety Conservation in Protocol Transitions* — The total information-theoretic variety in a protocolized system is not reduced by abstraction or layer transition; it is redistributed across implementation, governance, and user-side friction. Systems that appear to simplify often externalize complexity rather than eliminate it.

(Status: **candidate hypothesis**, not yet law—requires operationalization of "variety" in protocol contexts and comparative case studies across known layer transitions.)
