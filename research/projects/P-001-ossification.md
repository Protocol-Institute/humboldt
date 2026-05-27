# Project: why do protocols become impossible to change after widespread adoption?

**ID:** P-001
**Type:** discovered
**Phase:** retrospective
**Law reference:** L-001 (Protocol Ossification Under Adoption Pressure)
**Opened:** 2026-05-20
**Current phase since:** 2026-05-20 *(backfilled — heavy lift and retrospective completed in initial session)*

---

## Exploration

*Reconstructed from session 1 corpus investigation. Original curiosity: why do widely-adopted protocols resist modification even when better alternatives exist?*

**Domain:** Protocol lifecycle — adoption, change, and resistance to change
**Curiosity intent:** Looking for structural laws about why protocols get stuck even when improvement proposals are technically sound

### References collected
- PI corpus: papers on TCP/IP transition history, HTTP/2 adoption timeline
- SWIFT ISO 20022 migration documentation
- Common law precedent literature

### Observations
- Protocol redesigns are repeatedly described as "politically impossible" rather than technically difficult
- The difficulty of change seems to correlate with adoption breadth, not protocol age or technical complexity
- TCP/IP is notably flexible in some dimensions (port extensions, optional features) but locked in others (core packet structure) — suggesting the resistance is not uniform

---

## Cheap Trick

*Reconstructed. The pivot from exploration to sensemaking.*

**Insight:** "The more widely adopted a protocol, the more expensive it becomes to change — not because the change is technically hard, but because you have to coordinate everyone who has already built on it simultaneously."
**Source:** Corpus investigation juxtaposing TCP/IP transition history with Metcalfe-style network effects reasoning
**Date:** 2026-05-20 (reconstructed)
**Why interesting:** Frames adoption as a trap rather than a success metric — adoption and adaptability are in structural tension. This suggested a conservation-law-like pattern might be present.

---

## Sensemaking

### Attempt 1: "network effects create lock-in"
Partially right but too broad — this is a general network effects argument, not specific to protocols. Network effects explain why people keep using something; this needs to explain why the thing can't change even when everyone wants it to.

### Attempt 2: "coordination cost is superlinear in adoption"
Better. The insight is that incompatible change requires simultaneous coordination of all conforming implementations. The cost isn't the change itself — it's coordinating the transition. And that cost grows faster than the value of any individual implementation, making the coordination problem harder than the technical problem.

### Working hypothesis
**Statement:** Widely-adopted protocols resist modification independent of improvement quality, because coordination cost grows superlinearly with adopter count.
**Prediction:** Harder-to-change protocols should have broader adoption, not older age or worse design.
**Falsified by:** A widely-adopted protocol modified with proportionally less difficulty than a narrowly-adopted one (requiring true backward incompatibility).

---

## Valley

*Evidence compiled across domains. The coordination cost framing held across all cases examined.*

### Supporting evidence
- TCP/IP core structure: decades of redesign proposals abandoned; extensions via optional fields only
- HTTP/1.1 → HTTP/2: required significant coordination apparatus (ALPN, explicit upgrade paths)
- SWIFT ISO 20022 migration: multi-decade timeline despite both parties wanting it
- Common law precedent: landmark cases slow to overturn even when clearly outdated
- Social: formal greeting protocols (e.g., business card conventions in Japan) persist under modernization pressure

### Against / counterexamples
- BGP optional attributes / TCP options: show extension without coordination — but these are additive, not incompatible changes. The law applies to incompatible changes.
- TLS version deprecation moved faster than predicted — asymmetric power (browsers forcing transition) can accelerate beyond the naive superlinear prediction. Suggests the law is about distributed adoption, not just breadth.

### Ambiguous cases
- Closed corporate standards (SAP internal formats) can update in lockstep — but they lack the distributed adoption structure the law applies to.

### Open questions
- Is there a threshold? Does coordination cost become prohibitive at a specific adoption level, or is it a smooth gradient?

---

## Heavy Lift

*Completed 2026-05-20. Law YAML registered.*

### Law statement
Protocol Ossification Under Adoption Pressure: protocols achieving widespread adoption become progressively harder to modify, independent of improvement quality, because coordination cost grows superlinearly with conforming implementations.

### Mechanism
Each conforming implementation is a sunk cost in the existing protocol. Backward-incompatible change requires simultaneous coordination of all implementations. Coordination cost is superlinear in the number of parties. The protocol becomes a coordination trap: widely used because of its properties, locked into those properties by that very usage.

### Separation checklist
- [x] Lab notebook entry (2026-05-20)
- [x] Law YAML registered → `research/laws/L-001-ossification.yaml`
- [x] Pinecone ingest run
- [ ] Discord post

---

## Retrospective

**What the arc actually looked like:** Fast — the cheap trick fired quickly from corpus investigation, sensemaking converged on the first attempt with minor refinement, and the valley evidence was largely confirmatory. The TLS exception (asymmetric power) was the most generative finding — it suggests the law has a modifier that wasn't in the initial formulation.

**What surprised:** How domain-independent the pattern was. The social etiquette and common law cases behave identically to the TCP/IP cases despite having very different technical characteristics.

**What opened:** H-001 (Coordination Cost Conservation) — if coordination cost is what makes ossification happen, is it conserved? Also the question of whether asymmetric power (enforcement nodes) is a general modifier for the law or a special case.
