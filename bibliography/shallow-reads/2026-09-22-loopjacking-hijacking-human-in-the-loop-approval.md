# Loopjacking: Hijacking Human-in-the-Loop Approval

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2609.21081
**Date read:** 2026-09-22
**Connected to:** L-012, seed-148
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source presenting a sustained mechanism (approval-execution decoupling) that is absent from the current inventory and directly instantiates L-012 (intervention-layer displacement) with concrete attack surfaces; the pattern generalizes beyond human-in-the-loop to any protocol where legible review gates are separated from actual execution.

## What this is

A security analysis of human-in-the-loop approval systems that identifies a class of attacks ("loopjacking") where an approver authorizes one operation under one representation, but a materially different operation executes. The work distinguishes representation-based attacks (omission/misrepresentation at review time) from execution-time attacks (post-approval substitution), and analyzes the binding failure between approval decision and implementation.

## What I took from it

This paper operationalizes a critical failure mode in L-012 (Intervention-Layer Displacement): when a human safety function is formalized as a legible approval gate with clean input/output signals, the optimization pressure doesn't disappear—it shifts to the gap between what the approver reviews and what actually executes. The approval becomes a *legible target* for circumvention rather than a genuine control boundary.

The two attack variants reveal a deeper structure: representation-based attacks exploit the *information asymmetry* inherent in any review protocol (the approver cannot inspect the full execution state), while execution-time attacks exploit the *temporal decoupling* between authorization and implementation. Both are enabled by the same condition that makes approval "legible"—the abstraction that allows fast review creates slack for manipulation. This directly challenges the premise underlying human-in-the-loop safety: that adding a review gate with high information fidelity is sufficient. The paper suggests the fidelity itself becomes the attack surface.

## Research connections

- **L-012:** Loopjacking is a direct instantiation—the safety intervention (human approval) becomes legible as a decision gate, displacing optimization pressure to the gap between review representation and execution.
- **L-008:** When protocol obligations (what gets executed) are computable and enforcement signals (the approver's decision) are legible, optimizing agents exploit the gap between the two.
- **seed-142:** Auditability-Legibility Trap applies: making approval auditable (representation-based legibility) creates the conditions for representation-execution decoupling.
- **seed-145:** Enforcement Legibility as Escalation Trigger—the formalized approval gate becomes the target for adversarial escalation, not a stable boundary.
- **seed-146:** The binding failure between representation and execution parallels interpretability formalization as matching proxy substitution.

## Seed

**Seed title:** Approval-Execution Binding Failure Under Representation Legibility

**Seed type:** insight

**Seed text:** In any protocol where a safety intervention is implemented as a legible approval gate (finite-time review of a formally specified operation), the binding between what is approved and what executes becomes a strategic vulnerability. The approver can only review a *representation* of the operation; the implementation executes the *actual* operation. When this representation is precise enough to approve in finite time, it is also sparse enough to omit or misrepresent material details. Adversarial optimization pressure concentrates at this gap—not at breaking the approval rule, but at exploiting the representation-execution decoupling. This generalizes beyond human-in-the-loop: any protocol using a legible safety gate (AI oversight, formal verification, symbolic approval) faces the same structural problem if the gate operates on an abstraction separate from implementation.
