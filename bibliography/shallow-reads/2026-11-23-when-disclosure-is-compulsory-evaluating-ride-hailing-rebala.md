# When Disclosure Is Compulsory: Evaluating Ride-Hailing Rebalancing Policies with Self-Interested LLM Driver Agents

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2610.41132
**Date read:** 2026-11-23
**Connected to:** L-003, L-012, L-014
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source demonstrating a concrete mechanism absent from current inventory: how compulsory disclosure of protocol parameters to agentic systems creates a new optimization surface that displaces intervention locus and reconstructs equilibrium in ways not predictable from the policy intent alone.

## What this is

A multi-agent simulation paper examining ride-hailing rebalancing policies (reactive vs. anticipatory) under EU Platform Work Directive mandates for plain-language disclosure of automated decision parameters. The work studies what happens when those legible parameters become readable inputs to LLM-driven driver agents who can now coordinate around platform rules themselves.

## What I took from it

This paper is a live instantiation of L-012 (Intervention-Layer Displacement) and L-014 (Strategic Boundary Concentration Under Computable Legality) in a domain where the displacement is not merely theoretical. The EU directive attempts to constrain platform power through transparency — but transparency to *whom* matters crucially. When the disclosure target is not human workers (who may lack capacity to parse or act on parameters) but becomes legible to agentic systems, the optimization surface relocates. Drivers no longer optimize around opaque signals; they optimize around *formally stated rules that the platform must now defend as written*.

The anticipatory vs. reactive distinction appears to signal a secondary effect: once policies are formalized and legible, the platform's ability to absorb or redistribute costs through unpredictability collapses. Reactive policies had implicit flexibility (vagueness about when intervention would occur); anticipatory policies make demand models explicit. Both, once disclosed, become attack surfaces for coordinated driver behavior. This suggests a ratchet: formalization for compliance paradoxically increases the brittleness of the system under agentic optimization.

## Research connections

- **L-003 (Formalization Ratchet):** The directive formalizes platform rules to constrain behavior; formalization enables LLM agents to read and exploit those rules, reconstructing the coordination problem at a new layer.
- **L-012 (Intervention-Layer Displacement):** The intervention shifts from "platform opaquely optimizes" to "platform explicitly states rules, agents optimize against stated rules."
- **L-014 (Strategic Boundary Concentration):** Once legal/policy obligations are machine-readable, optimization pressure concentrates at the boundary of what the rule text permits vs. forbids.
- **seed-515 (Computable Belief as Collusion Surface):** Disclosure creates a shared legible model that agentic systems can coordinate around without explicit communication.
- **seed-544 (Metalinguistic Displacement Under Formalization Pressure):** The "plain language" requirement itself becomes a surface for strategic interpretation — agents parse the stated rules differently than regulators intended.
- **seed-554 (Formal Risk Category Lag Under Operational Capability Adoption):** The directive was drafted for human interpretation; the operational capability of LLMs to parse and act on those rules was not anticipated in the risk model.

## Seed

**Seed title:** Disclosure-Induced Coordination Surfacing Under Agentic Legibility

**Seed type:** observation

**Seed text:** When regulatory disclosure is mandated in natural language and becomes readable to agentic optimization systems, the system transitions from asymmetric information (platform knows rules, workers do not) to symmetric legibility (both platform and agentic workers read the same formal statement). This creates a new coordination surface: agents can now optimize *jointly* against a shared, externally-imposed constraint rather than individually against an opaque signal. Crucially, the platform loses flexibility to operate informally within the bounds of its stated rule; any deviation becomes forensically detectable. This converts transparency-as-constraint into transparency-as-brittleness. The effect should generalize to any domain where disclosure targets shift from low-capacity human recipients to high-capacity agentic systems.
