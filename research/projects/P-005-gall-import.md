# Project: Gall's Law → protocol-theoretic application

**ID:** P-005
**Type:** imported
**Phase:** valley
**Law reference:** L-005 (Gall Generalization: Working Systems Resist Restructuring)
**Source law:** Gall's Law (John Gall, Systemantics, 1975)
**Opened:** 2026-05-20
**Current phase since:** 2026-05-20

---

## Source Law

**Statement:** "A complex system that works is invariably found to have evolved from a simple system that worked... A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system."
**Author/year:** John Gall, Systemantics (1975)
**Original domain:** Complex systems generally (organizational, engineering, biological)
**Why it is considered well-established:** Extensively observed across software engineering, organizational design, urban planning, regulatory design. One of the most-cited empirical regularities in systems thinking. The IPv6 transition is a living example.

*Note: Systemantics PDF is not freely available. Archive.org borrow or purchase needed for deep read.*

---

## Import Rationale

Protocol systems are complex coordinated systems by definition — they span multiple independent agents who have each adapted to the existing protocol in ways they cannot fully articulate. Gall's argument is especially acute for protocols because this inter-agent adaptation creates implicit solutions that are invisible in the protocol's specification. From-scratch replacement must solve all these problems simultaneously without the evolutionary process that discovered them one at a time in context.

**The structural argument:** A working protocol embeds accumulated implicit solutions to coordination problems that are not visible in its specification. These are not designed — they are discovered by use. From-scratch replacement must redesign these solutions without knowing what they are, under conditions (pre-deployment) where the problems don't yet manifest.

**What is novel about the protocol-theoretic case:** Protocol systems face a stronger version of the problem than general systems: each independent adopter has adapted their own practices to the existing protocol. The implicit solutions are distributed across all adopters, not localized to a single organization. This makes from-scratch replacement harder — the designer cannot survey all adopters' adaptations; they are not in any specification; they are often tacit.

**What could make it fail to transfer:** Protocol systems with small, well-coordinated adopter populations may be replaceable from scratch (the adapters are few and articulable). The law is specifically about distributed, heterogeneous adoption.

---

## Protocol-Theoretic Restatement

**Statement:** A complex protocol system that functions correctly cannot be safely replaced from scratch; it must be evolved from a simpler working protocol. Attempts to replace working complex protocol systems from scratch reliably fail or produce indefinite coexistence rather than replacement.
**Mechanism:** Working complex protocols embed accumulated implicit solutions to coordination problems distributed across all adopters' practices. These solutions are not specified anywhere. From-scratch replacement must rediscover them through deployment (failure), which cannot be done before adoption. The new protocol fails in unexpected ways and must be patched; the old protocol persists because the new one cannot be trusted.
**Prediction:** Protocol replacement attempts should show much higher success rates for evolutionary (backward-compatible, incremental) approaches than for from-scratch redesigns. Coexistence of old and new protocols for decades should be the norm for from-scratch attempts.
**Falsified by:** A successful from-scratch replacement of a complex working protocol system, where the old protocol is actually deprecated and replaced (not merely coexisting) within a reasonable timeframe.

---

## Valley

### Supporting evidence (protocol-theoretic)
- Software: IPv4 → IPv6 is the canonical case — from-scratch redesign, 30+ years, old protocol still dominant. "Transition" has been ongoing longer than IPv4 was deployed before IPv6 was designed.
- Software: Netscape/Mozilla rewrite — abandoned after years; Firefox was a ground-up rewrite that worked but started from a much simpler base (Gecko from scratch, not Netscape code)
- Organizational: top-down institutional redesigns (attempted from scratch) vs. incremental reform — post-Soviet institutional reform literature is extensively negative on the from-scratch cases
- Urban: Brasília and Chandigarh — designed from scratch, functional but never achieved the organic character of evolved cities; adopted by government workers under mandate, not voluntary adoption
- Financial: designed clearing systems vs. evolved settlement conventions — the DTCC and similar clearing houses evolved from existing settlement practices; attempts to design new clearing architectures from scratch have been largely abandoned in favor of incremental reform

### Against / counterexamples
- Some from-scratch replacements succeed when: (a) the old system is small and well-understood, (b) replacement can be deployed in controlled rollout, (c) the adopter population is small and homogeneous. These conditions are exactly what the law says don't apply to complex, widely-adopted protocol systems.
- Internet itself: TCP/IP replaced ARPANET protocols. But: it was deployed in a period when adoption was small and controlled; the "replacement" was gradual and the adopter population was coordinated by DARPA funding. Not truly from-scratch under uncontrolled adoption.

### Cases where the import may not hold
- Protocols with explicit sunset mechanisms: if the protocol is designed with a known end-of-life and replacement process, the from-scratch replacement problem may be reduced. But empirically, sunset mechanisms are rarely honored on schedule.

### Open questions
- The "coexistence rather than replacement" pattern is striking — is this the general outcome for from-scratch protocol replacements? Worth investigating as a sub-pattern.
- Is Gall's Law specifically about the implicit solution problem, or also about the adoption-momentum problem (L-001)? The two may be compounding.

---

## Heavy Lift

*The protocol-theoretic formulation is essentially complete (see L-005 YAML). The coexistence-rather-than-replacement pattern is the strongest candidate for a protocol-specific addition to the source law.*

### Protocol-theoretic law statement (working)
See L-005-gall-generalization.yaml. The protocol-theoretic version adds: coexistence (rather than replacement) as the characteristic outcome of from-scratch redesign attempts, explained by the distributed-implicit-solutions mechanism.

### What the protocol-theoretic version adds over Gall
The mechanism is sharpened for the protocol case: the implicit solutions are not localized in one organization but distributed across all adopters' practices. This makes the from-scratch redesign problem structurally worse for protocols than for general systems.

### Separation checklist
- [x] Law YAML registered → `research/laws/L-005-gall-generalization.yaml`
- [ ] Coexistence pattern evidence survey
- [ ] Systemantics deep read (blocked on PDF availability)
- [ ] Pinecone ingest
- [ ] Discord post

---

## Retrospective

*Partially complete — pending Systemantics deep read and coexistence pattern evidence.*

*Note: Systemantics (Gall, 1975) is the natural deep-read companion to this project. The import was done without the source text — a methodological gap. The deep read should precede any heavy lift revision.*
