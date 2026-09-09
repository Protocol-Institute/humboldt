# JustAct: A Framework for Auditable Multi-Agent Systems Regulated by Inter-Organisational Policies

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2502.00138
**Date read:** 2026-09-01
**Connected to:** L-003, L-015
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systems paper proposing a distributed software framework for enforcing layered policies (generic legal + participant-specific consent constraints) across multi-agent systems crossing organizational boundaries. The work treats policy specification and auditability as implementation problems, with focus on composability of policy languages and verification traces.

## What I took from it

The paper is competent technical work addressing a real coordination problem: how to make policy obligations legible and machine-enforceable when they span multiple legal regimes and consent layers. It confirms the Formalization Ratchet (L-003)—the pressure to render informal consent and contextual rules into computable policy specifications—and touches the edges of L-015 (Interpretive Continuity Decay), since distributed audit traces must remain interpretable across organizational boundaries and time.

However, the work does not engage with the generative problem: *what happens to the meaning and enforceability of policy when it is formalized and distributed across agents with misaligned incentives?* The paper assumes policies are stable, unambiguous, and that auditability solves compliance. It does not investigate whether formal policy enforcement creates new failure modes (Goodhart capture, optimization pressure displacement, or norm drift under distributed enforcement). The framework is solution-focused rather than mechanism-focused.

## Research connections

- **L-003 [Formalization Ratchet]:** Confirms that coordination pressure drives formalization of consent and policy from informal to computable form, but does not examine the cognitive or governance costs of this transition.
- **L-015 [Interpretive Continuity Decay]:** Touches but does not investigate: as policy audit traces become formally preserved and distributed, does institutional understanding of *why* the policy exists decay? Does formalization ossify interpretation?
- **L-008 [Proxy Optimization Under Computable Enforcement]:** Implicitly relevant: once policy obligations are "precisely computable," do agents optimize the letter over intent? The paper treats this as solved by audit rather than as a live risk.

## Seed

**Seed title:** none

---

**Rationale for store-only:** This is a capable engineering contribution addressing a real problem, but it is not a primary source making a sustained theoretical or empirical argument about protocol behavior under stress. It does not challenge or extend existing laws; it implements a solution downstream of formalization rather than investigating what formalization itself does to coordination. The mechanism it assumes (audit → compliance) is already well-understood. No fragment generalizes beyond the narrow domain of cross-organizational policy specification.
