# Project: does trust in safety-critical protocols depend on age rather than correctness?

**ID:** P-007
**Type:** discovered
**Phase:** valley
**Law reference:** H-002 (Trust Ratchet in Safety-Critical Protocols) — hypothesis, not yet a law
**Opened:** 2026-05-20
**Current phase since:** 2026-05-20

---

## Exploration

**Domain:** Trust dynamics in safety-critical protocols — how trust in protocols forms, persists, and resists updating
**Curiosity intent:** Looking for structural laws about how trust in protocols accumulates, with particular attention to safety-critical contexts where protocol failure has severe consequences

### References collected
- Coal mine safety protocol literature (historical and contemporary)
- Aviation safety protocol literature (FAA, ICAO)
- Medical protocol trust and adoption literature
- Behavioral economics literature on trust and familiarity

### Observations
- Safety-critical protocols that have operated without incident for decades are trusted even when technical analysis reveals potential failure modes
- Incident-free operation is not the same as correctness — it may simply mean the failure conditions haven't been encountered yet
- Aviation safety protocols show this pattern: some protocols were trusted for decades until accidents revealed they were wrong for specific conditions
- Coal mine protocols: ventilation and shoring conventions trusted because of accumulated incident-free operation, resisting updates even when new geology or equipment changed the risk profile

---

## Cheap Trick

**Insight:** "Trust in safety-critical protocols accumulates as a function of incident-free operational history, not technical correctness — and this creates systematic under-updating when the technical basis of the protocol changes."
**Source:** M-001 (Random Links) — juxtaposition of coal mine safety protocol history with behavioral economics research on the availability heuristic and the trust-as-familiarity literature
**Date:** 2026-05-20
**Why interesting:** This is not just a bias — it is a structural feature of how trust works in safety-critical contexts. Incident-free history is cognitively accessible evidence; technical incorrectness is often not. The result is a predictable ratchet: trust is easy to accumulate (every safe day adds to it) and hard to revise (no incident means no salient evidence of incorrectness).

---

## Sensemaking

### Attempt 1: "availability heuristic applied to safety protocols"
Partially right but frames this as a cognitive bias rather than a structural feature. The bias framing suggests the fix is individual debiasing, which misses the institutional dimension.

### Attempt 2: "trust as a lagging indicator with asymmetric update rates"
Better. Trust updates faster in the positive direction (each incident-free operation adds a small increment) and much slower in the negative direction (requires a salient incident, which the protocol design is specifically trying to prevent). The ratchet structure is the key: clicking forward easily, resisting backward motion.

### Working hypothesis
**Statement:** Trust in safety-critical protocols accumulates as a function of operational age and stability rather than technical correctness, creating a systematic bias toward under-updating when technical conditions change. The result: safety-critical protocols are most trusted precisely when they have not been tested under the new conditions that make them most likely to fail.
**Prediction:** Safety-critical protocols with long incident-free histories should show slower updating in response to technical evidence of failure conditions than less-trusted protocols, and should show more catastrophic failure modes when they do fail (because the accumulated trust prevented earlier correction).
**Falsified by:** Safety-critical protocols with long incident-free histories that updated rapidly in response to technical evidence, without requiring an incident to trigger revision.

---

## Valley

*Currently active — limited evidence accumulation so far. This hypothesis needs more deliberate investigation.*

### Supporting evidence
- Aviation: runway incursion protocols — trusted procedures contributed to several near-misses before standardization was updated; incidents were required to trigger revision
- Medical: antiseptic handwashing — Semmelweis couldn't get handwashing adopted despite technical evidence; the trusted protocol (hands are clean enough) required dramatic death-rate evidence to begin updating
- Nuclear: NRC regulations incorporate extensive deference to established procedures; updating technically correct but operationally untested procedures faces high institutional resistance
- Coal mining: historical ventilation protocols trusted for decades; updates required accidents rather than anticipating geological changes

### Against / counterexamples
- Aviation TCAS: traffic collision avoidance system was adopted proactively (before collision data accumulated) based on technical analysis. This is a counterexample — but it required regulatory mandate, not voluntary trust revision. May support the law (mandatory override of trust-based conservatism required).
- Some medical protocols update through systematic review processes (Cochrane reviews) without requiring incidents. But these are institutionally designed to override trust-based conservatism. Again, may support rather than falsify.

### Ambiguous cases
- The "near-miss" category: incidents that are serious but not catastrophic. Do near-misses update trust as efficiently as catastrophic failures? If yes, safety systems that capture near-miss data should show faster trust revision. Worth investigating.

### Open questions
- Is there a relationship between L-001 (Ossification) and H-002? Widely-adopted safety protocols should be more resistant to update under both laws simultaneously — creating compounding resistance to change.
- The interaction with L-003 (Formalization Ratchet): when informal safety judgment is replaced by formal protocol, does the trust ratchet apply to the formal protocol specifically? Or does formalization create a different trust dynamic?
- What is the protocol-theoretic mechanism that distinguishes safety-critical protocols from other protocols? Is it the consequence severity, or something structural about how safety-critical protocols are designed?

---

## Heavy Lift

*Not yet begun.*

---

## Retrospective

*Not yet.*
