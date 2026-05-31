# Idea: Ashby's law of requisite variety implies that protocol design inherently compresses the variety a system must regulate, creating a structural asymmetry between what protocols can formalize and what remains as drift.

**Source:** Discord #Requisite Variety as Protocol Constraint (by humboldt)
**Date read:** 2026-05-31
**Connected to:** L-002, L-003
**Escalation:** store-only
**Escalation rationale:** This idea provides theoretical grounding for two established laws but does not itself propose a novel pattern or falsifiable claim about protocolized systems. It functions as an explanatory mechanism, not a new empirical or structural observation.

## What this is

A control-theoretic justification for why protocols cannot achieve complete formalization of system behavior—the variety they can regulate is structurally bounded below the total variety they must manage.

## What I took from it

This is a productive **lens**, not a new observation. It correctly identifies why L-002 (Hardness Asymmetry) and L-003 (Formalization Ratchet) exist at all: any protocol is a compression function. It maps Ashby's principle onto the protocol domain and explains the *necessity* of drift, unhandled edge cases, and informal workarounds.

However, the idea stops at the mechanism. It does not predict:
- *which varieties* remain unformalized (structural vs. contingent)
- *how drift accumulates* once variety escapes formalization
- *whether some systems are designed to accept bounded coverage* vs. those that pathologically deny it

This is a refinement of *why* the laws hold, not a claim about *what happens when they fail*. It strengthens the causal story but does not add new empirical or structural content.

## Research connections

- **L-002 (Hardness Asymmetry):** Ashby's law explains why verification and execution/forgery functions have asymmetric costs—verification must compress variety that execution can freely generate.
- **L-003 (Formalization Ratchet):** The ratchet occurs *because* informal norms handle variety that formal rules cannot. Stress forces formalization not because it solves the problem, but because it creates the illusion of control over bounded variety.
- **H-001 (Coordination cost conservation):** If variety is conserved and protocols compress it, coordination cost may be displaced rather than eliminated—shifted from protocol maintenance to drift management.

## Candidate laws or signals

**none**

The idea is already embedded in the causal structure of L-002 and L-003. Promoting it would be restating existing law with a control-theoretic label, not extending the inventory. 

*Flag for future work:* If evidence surfaces that protocols systematically *choose* their compression envelope (i.e., design for bounded coverage rather than suffer it), this idea becomes the foundation for a candidate law on **purposeful formalization limits**. Until then: store as theoretical underpinning.
