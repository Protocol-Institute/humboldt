# Project: is coordination cost conserved across protocol layer transitions?

**ID:** DS-006
**Type:** discovered
**Phase:** valley
**Phase artifact:** CL-002 (Coordination Cost Conservation)
**Opened:** 2026-05-20
**Current phase since:** 2026-05-20

---

## Exploration

**Domain:** Protocol design and its effects — specifically, whether protocol redesign actually reduces coordination cost or just moves it
**Curiosity intent:** Practitioners frequently describe protocol simplification as producing new complexity elsewhere. Is this a real structural pattern or just a complaint about change?

### References collected
- OSI model vs. TCP/IP comparison literature
- OAuth and identity infrastructure literature
- Protocol layer design papers from PI corpus
- Coordination cost / transaction cost economics literature

### Observations
- TCP/IP is frequently described as "simpler" than OSI, but the simplicity pushed significant complexity to the application layer
- OAuth simplified application-level authentication but produced enormous complexity in identity provider infrastructure
- The pattern appears repeatedly: simplify layer N, create problems at layer N+1 or N-1
- Coase's transaction cost framing might be relevant — coordination cost as a conserved economic quantity?

---

## Cheap Trick

**Insight:** "Coordination cost in protocol systems behaves like energy in thermodynamics — it cannot be destroyed, only redistributed. Protocol redesign moves coordination cost between layers but cannot eliminate it."
**Source:** The thermodynamics analogy emerged from juxtaposing the TCP/IP / OSI comparison with the observation about OAuth — both are "simplifications" that produced new complexity in adjacent layers
**Date:** 2026-05-20 (reconstructed)
**Why interesting:** If true, this is a conservation law — a much stronger claim than "protocol changes have tradeoffs." Conservation laws are rare and valuable; they set hard limits on what protocol design can achieve.

---

## Sensemaking

### Attempt 1: "complexity is conserved"
Too vague. "Complexity" is not well-defined. The thermodynamics analogy requires a specific quantity, not a general vague property.

### Attempt 2: "coordination cost specifically is conserved"
Better. Coordination cost is more tractable — it is the cost borne by participants in achieving the coordination that the protocol is designed to enable. This can in principle be measured (transaction costs, time, error rates, overhead). The claim is that this quantity is conserved: redistribution is possible, elimination is not.

### Working hypothesis
**Statement:** The total coordination cost in a protocol system is conserved across protocol layer transitions — when a protocol redesign reduces coordination cost at one layer, it increases it at adjacent layers by at least the same amount.
**Prediction:** Documented protocol simplifications should show measurable coordination cost increases at adjacent layers proportional to the savings at the redesigned layer.
**Falsified by:** A protocol redesign that demonstrably reduced total system coordination cost (not just moved it), sustained over time after full adoption.

---

## Valley

*Currently active. This is the long phase — the conservation claim is strong and requires careful evidence.*

### Supporting evidence
- TCP/IP vs. OSI: TCP/IP simplified the network layer; application-layer complexity (everything that HTTP, SMTP, etc. now handle) is significantly higher than in the OSI model's application layer design. Coordination cost moved up.
- OAuth: simplified per-application authentication by moving complexity to identity provider infrastructure and to the user experience of permission management. The OAuth "simplified" experience produces more total coordination work than the per-site password it replaced — it just concentrates the complexity differently.
- DNS: simplified application-layer address resolution; produced significant coordination complexity in the DNS infrastructure layer (DNSSEC, anycast routing, registrar coordination)
- REST APIs: simplified protocol design compared to SOAP/WS-*, but moved coordination cost to documentation, versioning management, and backward-compatibility maintenance

### Against / counterexamples
- **The strong falsification test:** Find a protocol redesign that provably reduced total system coordination cost (not just moved it), sustained after full adoption. None found in corpus to date — but absence of evidence is not evidence of absence.
- Compression protocols: DEFLATE/gzip reduce coordination cost (bandwidth, storage) at what appears to be a genuine reduction rather than redistribution. But this may be energy-like (compression extracts actual information-theoretic efficiency) rather than coordination cost. The comparison may not apply.

### Ambiguous cases
- Automation of coordination: when coordination cost is automated (moved from human effort to machine effort), does it "count" as eliminated or as redistributed to the machine layer? This is the key ambiguity in the hypothesis. If machine coordination cost counts, the conservation law is more likely to hold. If only human coordination cost counts, automation is a genuine escape.

### Open questions
- **The automation question is the crux.** If automation can genuinely eliminate coordination cost (not just move it to machines), the conservation law fails. This is the most important falsification test to run.
- How to measure coordination cost across layers in a way that allows the conservation claim to be tested? The hypothesis requires a unit of account.
- Is this a strict conservation law or a tendency? The thermodynamics analogy suggests strict conservation, but protocol systems are not closed systems.

---

## Heavy Lift

*Not yet begun. Valley needs the automation question resolved before heavy lift is possible.*

---

## Retrospective

*Not yet.*

---

## Arc Diagnosis

**Current phase:** `valley_productive`
**Phase tempo:** Continued investigation with diminishing but nonzero returns. The cheap trick has fired and the working hypothesis is formed. The automation question is the unresolved crux — retrieval keeps circling it without closing it. This is expected valley behavior.
**Transition trigger:** Automation question resolved in either direction: either a principled argument that machine coordination cost counts as coordination cost for conservation purposes (law holds), or a documented case of genuine coordination-cost elimination via automation (law fails or needs scoping). Either closes the valley and opens the heavy lift.
**Blocking behavior:** none
