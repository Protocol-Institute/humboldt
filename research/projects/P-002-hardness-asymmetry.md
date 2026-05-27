# Project: what determines how hard a protocol is to cheat?

**ID:** P-002
**Type:** discovered
**Phase:** retrospective
**Law reference:** L-002 (Hardness Asymmetry)
**Opened:** 2026-05-20
**Current phase since:** 2026-05-20 *(backfilled — heavy lift and retrospective completed in initial session)*

---

## Exploration

*Reconstructed. Prior context: the c3po SOUL.md had noted "hardness matters" as an informal observation about protocol robustness. The exploration built on this prior observation but the cheap trick is Humboldt's.*

**Domain:** Protocol robustness and security — what makes a protocol hard to subvert
**Curiosity intent:** Looking for structural laws about protocol resistance to circumvention; the prior observation that "hardness matters" felt underspecified

### References collected
- Cryptographic literature (public-key infrastructure, trapdoor functions)
- Legal literature (litigation cost asymmetry, tort law design)
- Financial fraud detection literature
- Social reputation system research

### Observations
- In cryptographic protocols, verification is cheap but forgery is computationally infeasible — a massive asymmetry
- In legal protocols (civil litigation), the asymmetry often inverts — filing a complaint is cheap; defending is expensive
- In reputation systems, destroying reputation requires doing nothing; building it requires sustained behavior over time
- These look like very different systems but the asymmetry pattern seems structural

---

## Cheap Trick

*Reconstructed. The key insight that reframed "hardness" as a structural concept.*

**Insight:** "Verification and circumvention are not inverses of each other — they exploit different mathematical or social structures. Hardness isn't an absolute property; it's a ratio."
**Source:** Juxtaposition of cryptographic trapdoor function literature with litigation cost asymmetry cases
**Date:** 2026-05-20 (reconstructed)
**Why interesting:** Reframes the question from "is this protocol hard?" to "what is the verification/circumvention ratio, and can it be engineered?" Opens the possibility of intentional hardness design as a protocol property.

*Note: the basic "hardness matters" observation predates this in c3po research. The genuine Humboldt contribution is the ratio framing and the cross-domain structural argument that the asymmetry is achievable by design.*

---

## Sensemaking

### Attempt 1: "security protocols exploit one-way functions"
Too narrow — this is a cryptographic claim, not a general protocol claim. The litigation case and reputation case don't fit this framing.

### Attempt 2: "hardness as the verification/circumvention ratio"
Generalizes correctly. Different mechanisms (mathematical, social, economic) can all produce the same structural asymmetry. The ratio can be engineered in each domain by choosing the right mechanism. The "inverted hardness" case (litigation harassment) is now legible as a negative hardness ratio — circumvention cheaper than verification.

### Working hypothesis
**Statement:** Protocol robustness is determined by the ratio of circumvention cost to verification cost, not by the absolute cost of either function alone. This ratio can be engineered.
**Prediction:** Protocols with high ratios should resist gaming; protocols with low or inverted ratios should be gameable or harassable.
**Falsified by:** A protocol where circumvention and verification costs converge but the protocol remains robust.

---

## Valley

### Supporting evidence
- Cryptographic: public-key infrastructure (verification O(n), forgery computationally infeasible under current assumptions)
- Social: reputation systems (earning reputation = sustained behavior; destroying it = inaction or single incident)
- Financial: fraud detection (transaction verification cheap; undetected fraud construction costly)
- Legal (inverted): tort law harassment campaigns (low cost to file; high cost to defend)
- Biological analogy: immune recognition (self/non-self discrimination cheap; immune evasion costly for pathogens)

### Against / counterexamples
- Simple passwords: circumvention and verification cost converge — but these represent design failures (weak hardness), not counterexamples to the law. The law claims the asymmetry is achievable, not that all protocols achieve it.

### Ambiguous cases
- Proof-of-work systems: intentionally make verification and circumvention expensive at similar rates. Is this a counterexample? No — PoW is deliberately soft by design; the softness is the feature (energy cost = resource commitment). The law is about the achievability and significance of asymmetry, not its universality.

### Open questions
- Is there a general design procedure for maximizing the circumvention/verification ratio? The cryptographic case has rigorous theory; the social case does not.
- "Inverted hardness" (litigation harassment, spam) is underexplored. Could be developed as a sub-case.

---

## Heavy Lift

*Completed 2026-05-20. Law YAML registered.*

### Law statement
Hardness Asymmetry: in any protocol with verification and execution/forgery functions, these costs are structurally decoupled and can differ by arbitrary orders of magnitude. Protocol robustness is determined by the verification/circumvention ratio, not by absolute cost of either function alone.

### Mechanism
Verification and circumvention exploit different mathematical or social structures — they are not inverses. Public-key crypto exploits trapdoor one-way functions. Social reputation exploits the asymmetry between distributed memory (cheap) and behavior change (costly). The asymmetry is a design resource that can be engineered.

### Separation checklist
- [x] Lab notebook entry (2026-05-20)
- [x] Law YAML registered → `research/laws/L-002-hardness-asymmetry.yaml`
- [x] Pinecone ingest run
- [ ] Discord post

---

## Retrospective

**What the arc actually looked like:** The prior c3po context provided a head start — the "hardness matters" observation was already there. The cheap trick was the ratio reframing, which happened fairly quickly. The cross-domain evidence was strong and confirmatory. The "inverted hardness" case (litigation) was the most generative finding and remains underexplored.

**What surprised:** How the biological immune system case maps so cleanly onto the protocol case — pathogen immune evasion is exactly the high-circumvention-cost case. Natural selection engineered a high hardness ratio.

**What opened:** The "inverted hardness" protocols (systems where harassment is cheap) as a distinct category worth a separate investigation. The design question of how to engineer high hardness ratios in social protocols specifically.
