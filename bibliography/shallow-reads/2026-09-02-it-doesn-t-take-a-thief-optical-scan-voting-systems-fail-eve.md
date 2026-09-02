# It Doesn't Take a Thief: Optical-Scan Voting Systems Fail Even Without Adversaries

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2607.27101
**Date read:** 2026-09-02
**Connected to:** L-001, L-007, seed-027
**Kind:** content
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A taxonomy paper documenting non-adversarial failure modes in optical-scan voting systems, organized by failure category (recording, scanning, tabulation, etc.). The work uses real-world failure accounts to persuade stakeholders that equipment and procedural brittleness exists independent of deliberate attack, challenging the assumption that voting system failures require adversarial intent.

## What I took from it

The paper is a competent empirical catalog of failure modes and serves a useful communicative function in jurisdictions where adversarial threat models fail to persuade. However, it is not presenting a sustained theoretical argument about the *conditions under which non-adversarial failure emerges in safety-critical protocols*, nor is it offering a mechanism for why systems ossify into brittle configurations despite long operational history.

The framing does confirm the presence of L-007 (trust accumulated through operational age rather than technical merit), but the paper does not investigate *why* stakeholders discount non-adversarial failure accounts or *how* trust ratchets prevent the internalization of brittleness signals. It documents the symptom (failures occur; stakeholders don't believe them until shown real cases) without analyzing the meta-protocol that locks stakeholders into dismissal.

The connection to L-001 (protocol ossification under adoption pressure) is indirect: voting systems may be hard to modify not because they have achieved widespread adoption, but because modification itself requires revalidation against trust ratchets, creating a secondary lock-in independent of adoption pressure.

## Research connections

- **L-001:** Voting systems may exhibit ossification not through adoption pressure but through trust-ratchet enforcement of modification barriers; the paper does not investigate this mechanism.
- **L-007:** Trust in voting systems appears to accumulate from operational age and stakeholder familiarity rather than from detection of failure modes; real-world failure accounts persuade some stakeholders where hypothetical attacks do not.
- **seed-027:** [connection unclear in inventory; assumed proximity to trust and safety-critical protocol brittleness]

## Seed

**Seed title:** none

**Seed type:** —

**Seed text:** —

---

**DECISION:** This is a domain-specific failure taxonomy with communication intent, not a law-shaped investigation. It documents L-007 but does not mechanistically explain it. Store as shallow reference for voting system case material; no escalation.
