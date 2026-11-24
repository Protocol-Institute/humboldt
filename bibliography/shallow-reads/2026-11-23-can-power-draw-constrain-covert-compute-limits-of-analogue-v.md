# Can Power Draw Constrain Covert Compute? Limits of Analogue Verification for AI Governance

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2610.07476
**Date read:** 2026-11-23
**Connected to:** L-002, L-020
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source deriving a closed-form bound on verification evasion in safety-critical protocols; it directly extends L-002 (Hardness Asymmetry) with a computable mechanism and challenges the feasibility of L-020 (Safety Channel Capacity Concentration), establishing that physical observables cannot close the verification-evasion gap.

## What this is

A theoretical paper deriving formal bounds on the maximum covert computation an adversary can hide from power-draw auditing in AI compute treaties. The work establishes that analogue verification channels (power traces, thermal signatures) have inherent information-theoretic limits that cannot constrain a sophisticated adversary, regardless of audit resolution or frequency.

## What I took from it

This paper is a **direct mechanism proof** for the asymmetry between verification cost and evasion cost in safety-critical protocols. It shows that when verification is delegated to a physical observable (power draw), the adversary gains a systematic advantage: they can trade off hidden computation against measurable noise, with the asymmetry formalized as a closed-form expression β. This confirms L-002 in a new domain (compute governance) but more importantly identifies the **specific mechanism** by which the asymmetry arises—not from protocol complexity, but from the fundamental illegibility of computation to external physical sensors.

The finding also bears directly on L-020 (Safety Channel Capacity Concentration). The paper shows that "safety capacity" (the ability to detect norm violations) is *not* equally distributed across observables: power draw provides a provably exploitable channel precisely because it conflates computation with thermal dissipation. This suggests that strategic agents will concentrate evasion effort at the boundary between internal (opaque) and external (legible) representations—a refinement of the seed-515 (Computable Belief as Collusion Surface) pattern.

## Research connections

- **L-002:** Extends Hardness Asymmetry from protocol design to physical verification; proves the asymmetry is *not* eliminable by increasing audit resolution.
- **L-020:** Instantiates Safety Channel Capacity Concentration; shows the capacity is a function of the observable's coupling to computation, not audit effort.
- **seed-515:** Computable belief (power signature) becomes a collusion surface when agents can decouple internal computation from external legibility.
- **seed-554:** Formal Risk Category Lag — the paper implies that formal compute limits ("we will run ≤ 10^24 FLOPs") fail because the risk category (covert compute) is structurally unobservable to the chosen measurement.
- **L-012:** Intervention-Layer Displacement — the locus of optimization shifts from "how to run more compute" to "how to run compute that leaves no power signature," moving the problem to a new layer.

## Seed

**Seed title:** Measurement-Computation Decoupling as Non-Recoverable Verification Gap

**Seed type:** observation

**Seed text:** In any safety-critical protocol where verification relies on a physical observable to constrain a computational process, there exists a fundamental decoupling: the adversary can perform computation that is functionally identical to the target but causally detached from the measurement surface. The gap is quantifiable (as a closed-form bound on hidden computation) and grows with adversary sophistication, not audit fidelity. This suggests a general principle: verification asymmetry in protocols is not primarily a function of cost (time, money, complexity) but of *observability structure*—the degree to which the constrained quantity is causally coupled to the measurement used to verify it. This may generalize beyond compute governance to any protocol system where the verification observable and the target quantity are physically or informationally distinct.
