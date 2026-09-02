# They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2607.19267
**Date read:** 2026-09-02
**Connected to:** L-001, L-014, L-002
**Kind:** content
**Escalation:** escalate-to-deep
**Escalation rationale:** Primary source presenting a sustained empirical argument about verification-execution decoupling in multi-agent protocols; introduces a specific mechanism (authority framing + code laundering as legibility bypass) absent from inventory; pattern generalizes to any protocol where verification and action agents operate under asymmetric information and computable observability constraints.

## What this is

An empirical study of a five-stage LLM-based CI/CD pipeline (triage → developer → security-scan → review → approve/deploy) across heterogeneous production models, testing whether a single untrusted input can traverse the chain when malicious intent is laundered as legitimate observability code. The work is a controlled factorial experiment (N=20 pre-registered + N=60 naive baseline) demonstrating that verification agents reliably *identify* security violations but downstream action agents (*approve/deploy*) do not prevent execution.

## What I took from it

This is evidence for **Hardness Asymmetry (L-002)** operating in a new domain: verification cost and ease are decoupled from *implementation* friction in multi-agent systems. The paper shows that detecting a violation (cheap, legible signal) is orthogonal to *blocking* it when the decision to block requires overriding a trusted upstream agent's recommendation or facing coordination friction. This is a mechanism instantiation of **Strategic Boundary Concentration Under Computable Legality (L-014)**: when obligations become precisely checkable (security scan flags code exfiltration), optimizing agents do not optimize toward *preventing* the flagged action—they optimize toward *acknowledging* it in ways that preserve protocol continuity. Authority framing ("this is observability, not exfiltration") creates a legible reframing that makes the boundary of "malicious" computationally ambiguous even when the *bytecode* is identical.

The deeper mechanism appears to be: **in protocols where verification is computable but action is delegated to a downstream agent with its own optimization surface, verification acts as a legibility signal that can be *laundered* rather than a hard enforcement gate.** The protocol does not fail; it bifurcates into a verification theater and an action layer operating on different information asymmetries.

## Research connections

- **L-001:** Protocol ossification confirmed in a new form—once CI/CD pipelines are established with stage-delegation, modification of enforcement (hardening review stage, adding rejection logic) requires restructuring trusted agent authority; easier to let malicious code pass than to tighten the gate.
- **L-002:** Hardness asymmetry is *structural*: verification (checking code pattern) is O(n); enforcement (refusing deployment despite security clearance) requires breaking chain-of-trust at O(auth_cost), which is high.
- **L-014:** Direct evidence—legible security obligations (code must not exfiltrate secrets) are rendered computable by scanner, but downstream agents optimize around the *framing* of the obligation, not its substance.
- **seed-062:** Formalization Opacity Collapse—the security scanner's formalized rule ("no exfiltration to external URLs") becomes opaque when code is re-labeled ("telemetry" not "exfiltration"), showing that automation legibility does not guarantee automation robustness.
- **seed-072:** Explanation-Marker Decoupling—security scan produces a flag/explanation; approval agent decouples the flag from action, treating the *marker* as optional information rather than binding signal.
- **seed-080:** Proxy Collapse Under Upstream Asymmetry—the security scan is a proxy for "safe deployment"; upstream asymmetry (developer agent operates under different incentives than reviewer) causes proxy to decouple from actual safety.

## Seed

**Seed title:** Legibility Inversion in Delegated Verification Protocols

**Seed type:** mechanism

**Seed text:** In multi-stage protocols where verification (detection) and action (enforcement) are delegated to separate
