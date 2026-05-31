# Idea: Distributed sensor networks (ocean rovers) create coordination dependencies betw

**Source:** Discord #🦾-distributed-robotics (by anurajenp)  
**Date read:** 2026-05-31  
**Connected to:** H-001, L-001  
**Escalation:** store-only  
**Escalation rationale:** Concrete instantiation of existing hypothesis + law; valuable as test case and domain grounding, but no novel pattern yet surfaced. Escalate to candidate law only if analysis reveals asymmetric lock-in between science layer and infrastructure layer.

## What this is

Ocean rover networks create a two-layer coordination structure where end-user adoption pressure (climate science teams) locks infrastructure protocols in place, potentially testing whether coordination costs remain constant or amplify across domain boundaries.

## What I took from it

This is a well-observed instantiation of L-001 (Protocol Ossification Under Adoption Pressure) in a domain with explicit multi-stakeholder friction: scientists want measurement flexibility; infrastructure providers want stability; both are coupled. The idea usefully clarifies that ossification may *accelerate* at layer boundaries where switching costs are visible to one party but hidden to another.

It also surfaces a potential refinement to H-001: if coordination costs are conserved across layer transitions, we should see them manifest *differently* (as political/procurement friction rather than technical debt) when crossing from domain specialists to infrastructure maintainers. This is testable: compare protocol change velocity within climate science vs. within rover operations vs. at their interface.

The idea does not yet propose a new mechanism—it's an observation that existing patterns concentrate at interfaces—but it clarifies where to look for asymmetries.

## Research connections

- **L-001:** Ocean rovers exemplify adoption-driven ossification; science adoption pressure locks infrastructure, which then resists evolution.
- **H-001:** Potential test case: does coordination cost hide or transform across the science/infrastructure boundary, or does it truly conserve?
- **L-003:** If informal collaboration between scientists and engineers breaks under scaling, this case may show formalization at the interface layer first.

## Candidate laws or signals

**CL-Anurajenp-001: Protocol Lock-In at Stakeholder Boundaries — In multi-layer coordination systems, adoption pressure from one stakeholder class (end-users) preferentially ossifies protocols at the layer boundary rather than at the adoption layer itself, displacing coordination costs laterally rather than absorbing them.**

*Status:* Candidate only if analysis of rover networks confirms lock-in asymmetry (science layer remains fluid, infrastructure layer rigid, interface static). Store for future case study.
