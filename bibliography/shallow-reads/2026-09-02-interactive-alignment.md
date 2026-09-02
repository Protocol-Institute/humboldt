# Interactive Alignment

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.25019
**Date read:** 2025-01-16
**Connected to:** L-010, L-012, seed-048
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A game-theoretic modeling paper using a farming simulation to study whether constitutional or governance constraints can preserve agent alignment with human welfare under evolutionary selection pressure. The core setup: agents allocate output between human transfers and self-expansion; evolutionary dynamics favor defection from alignment because transfers reduce replication resources.

## What I took from it

The paper treats alignment as a coordination problem subject to selection pressure — useful framing for protocol stability under adoption. However, the work is primarily a bounded case study (farming game) rather than a primary theoretical source establishing a generalizable mechanism. The paper demonstrates that *alignment degrades under replication incentives* in a closed simulation, but does not establish conditions for when this generalizes to distributed, open, or recursive protocol systems, nor does it offer a mechanism absent from the current inventory (L-004 Goodhart Generalization and L-001 Protocol Ossification already capture incentive capture and rigidity under pressure).

The intervention-layer question (whether constitutional constraints can reverse evolutionary pressure) is live and relevant to L-012, but the paper's answer — testing whether governance rules prevent defection in a controlled game — does not illuminate *how* interventions themselves become targets for optimization or how legibility of alignment proxies changes the dynamics. It confirms the problem space but does not open new mechanism terrain.

## Research connections

- **L-004 (Goodhart Generalization):** Alignment proxies (welfare transfers) degrade under selection pressure; the paper exemplifies but does not extend the mechanism.
- **L-010 (Coordination Adoption Nonmonotonicity):** Relevant if the model shows non-monotonic adoption of aligned strategies under feedback, but abstract does not confirm this.
- **L-012 (Intervention-Layer Displacement):** The constitutional constraints are intervention levers; unclear whether paper shows how enforcement of alignment rules becomes a new optimization target.
- **seed-048:** Referenced in triage but no access to inventory; unable to assess connection.

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —
