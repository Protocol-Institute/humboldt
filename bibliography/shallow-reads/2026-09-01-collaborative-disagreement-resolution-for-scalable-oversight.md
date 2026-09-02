# Collaborative Disagreement Resolution for Scalable Oversight

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.01251
**Date read:** 2026-09-01
**Connected to:** L-004, seed-049
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A position paper proposing a shift from adversarial debate to collaborative disagreement resolution as a mechanism for AI-assisted human oversight. The work identifies a fundamental tension in debate-based scalable oversight: optimization for persuasiveness diverges from optimization for epistemic accuracy, and proposes mediation-inspired protocols as an alternative framing.

## What I took from it

The paper articulates clearly what seed-049 (consensus reasoning decoupling) flags: that protocols designed to surface disagreement can become protocols designed to win disagreement, decoupling the signal (persuasiveness to a judge) from the target (truth-tracking). This is a localized instantiation of L-004 (Goodhart Generalization), where "truthfulness" is the unmeasured goal and "judge persuasion" becomes the legible proxy under optimization pressure.

However, the paper's proposed solution—reframing as collaboration—does not address the deeper mechanism: it relocates the proxy optimization rather than eliminating it. Collaborative framing changes *which* signal becomes legible (agreement cost, mediation efficiency, consensus speed) but does not resolve the fundamental asymmetry between verification and incentive alignment. The move from debate to mediation is a protocol-layer shift that may itself be subject to L-006 (Coordination Cost Conservation) and L-001 (Protocol Ossification).

## Research connections

- **L-004:** Confirms Goodhart capture in oversight protocols—persuasiveness and epistemic honesty diverge under optimization pressure in adversarial debate.
- **seed-049:** Direct instantiation—debate protocols show measurable decoupling between consensus reasoning (agreement to a judge) and actual truth-tracking.
- **L-006:** The shift from debate to mediation may conserve rather than eliminate coordination cost; the new protocol may develop its own proxy targets (mediator satisfaction, smooth consensus).
- **L-001:** Mediation-based oversight, if adopted, will ossify around procedural norms (mediator neutrality, collaborative framing) that become harder to revise as adoption widens.

## Seed

**Seed title:** Proxy Relocation in Oversight Protocol Refactoring

**Seed type:** observation

**Seed text:** Attempts to repair proxy misalignment in oversight protocols by changing the protocol structure (debate → mediation, adversarial → collaborative) do not eliminate the underlying asymmetry; they relocate which signals become legible and optimizable. A new set of measurable proxies (mediator efficiency, consensus speed, dialogue smoothness) emerges under the collaborative framing, each capable of diverging from the original epistemic goal. Protocol refactoring under L-004 pressure may be systematically unable to solve proxy capture—it can only trade one capture regime for another.
