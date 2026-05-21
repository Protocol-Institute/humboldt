# Deep Read: The Sciences of the Artificial

**Status: IN PROGRESS** — Last read: 2026-05-20, through book p. 60 (Ch 3 beginning)
**Next session:** Pick up at book p. 61 (Ch 3: limits on performance, continued). Priority remaining chapters: Ch 5 (The Science of Design, pp. 111–138), Ch 8 (The Architecture of Complexity, pp. 183–216).

---

## 1. Bibliographic Information

Herbert A. Simon
*The Sciences of the Artificial*, 3rd edition
MIT Press, Cambridge, MA, 1996
ISBN 0-262-69191-4
228 pages (8 chapters + 2 prefaces)

---

## 2. Selection Rationale

Simon was selected as the first deep read because *Sciences of the Artificial* is explicitly doing what Humboldt is doing: finding structural regularities beneath surface diversity across all designed systems. The book argues that there is a *science of design* that cuts across engineering, architecture, economics, cognitive psychology, and organizational theory — not because these fields share subject matter, but because they share a common structure (the artifact as interface between inner and outer environment). This is precisely the cross-domain regularity-seeking that defines Humboldt's research agenda.

Selection criteria met:
- **Foundational to a tradition:** The text that founded design science as a discipline; traces of Simon appear in every subsequent theory of design, bounded rationality, and organizational behavior.
- **Conceptually productive for new nature:** The inner/outer environment duality, near-decomposability, and satisficing are direct structural analogues to the protocol-theoretic problems Humboldt investigates.
- **Cross-domain by design:** Simon explicitly generalizes from economics to cognitive psychology to engineering to organizational theory, using a single analytical framework.
- **Analytically transferable:** The *methods* (functional explanation from outer environment, near-decomposability analysis, design as search) are applicable to Humboldt's own research problems.
- **Intellectually alive:** Bounded rationality is live in behavioral economics, cognitive science, and organizational theory. The design science agenda is being revisited in HCI and complex systems.

---

## 3. Structural Map

### Preliminary (before close reading)

*Hypothesis before reading:* Simon argues that there is a unified science of artificial systems because all artifacts share a common structure (designed to achieve goals, operating between an inner mechanism and an outer environment). The science of the artificial is primarily a science of design — of how goals, constraints, and environments interact to shape what gets built and why.

Expected key chapters: Ch 1 (defining the artificial), Ch 5 (The Science of Design), Ch 8 (The Architecture of Complexity).

### Revised (in progress — through Ch 3 p. 60)

The preliminary map is correct but incomplete. Simon's argument has three distinct moves:

**Move 1 (Ch 1): Defining the artificial.** Artifacts are characterized by their goal-directedness, not their material. An artifact is described by its *function*, not its inner mechanism. This makes functional explanation possible without complete knowledge of inner structure. The outer environment (goals + context) largely determines behavior; the inner environment sets only limits.

**Move 2 (Ch 2): Economics as a science of the artificial.** Markets and organizations are artifacts — designed solutions to the problem of bounded rationality. This chapter establishes that the inner/outer framework applies to social as well as physical artifacts. Key implication: understanding economic institutions requires understanding the information-processing constraints they're designed to work around, not just the equilibria they produce.

**Move 3 (Ch 3, beginning): Psychology as a science of the artificial.** Human cognition is an adaptive system; its apparent complexity is mostly environmental complexity. The ant on the beach. This is Simon's most radical claim: that mind is an artifact of its environment, explicable through outer-environment analysis rather than inner neuroscience.

Ch 5 (Design) and Ch 8 (Complexity) remain to be read, but the structural logic is now clear: the book is a series of demonstrations that the same inner/outer framework applies across physical design, economic organization, cognitive psychology, and complex systems.

---

## 4. Core Claim (preliminary — may be revised after Ch 5 and Ch 8)

All artificial systems — designed artifacts, economic institutions, cognitive processes, and complex hierarchies — share a common structure: they are interfaces between an inner environment (the mechanism's capabilities) and an outer environment (the goals and context). The science of the artificial is therefore a unified science: it studies how inner and outer environments interact across all domains of design, and how designers can use knowledge of the outer environment to predict and engineer behavior without full knowledge of the inner mechanism. The apparent diversity of designed things conceals a deep structural unity.

---

## 5. Conceptual Vocabulary

**Artifact:** Any object characterized by its function and goal-directedness rather than its material substrate. An artifact is a meeting point between two environments.

**Inner environment:** The mechanisms, capabilities, and constraints internal to the artifact or agent — what it is made of and how it works. In humans, the physiological and cognitive substrate. In economic institutions, the organizational structure and rules.

**Outer environment:** The goals, context, and task environment the artifact operates within. Determines what the artifact must do; largely determines its behavior (in conjunction with goals) without requiring knowledge of inner details.

**Functional explanation:** Explaining behavior from the outer environment and goals, treating the inner environment as largely irrelevant to behavior-level description. "The ant's path is a complexity of the beach, not the ant."

**Bounded rationality:** Rational decision-making under real cognitive and informational constraints — limited attention, limited computation, limited knowledge. Not irrational, but also not globally optimal. Agents satisfice rather than maximize.

**Satisficing:** Choosing the first alternative that meets a threshold (aspiration level) rather than searching for the global optimum. The procedurally rational response to bounded rationality.

**Aspiration level:** The threshold that defines satisficing. Aspiration levels adjust upward when search is easy and downward when it is difficult — they track the environment's difficulty.

**Substantive rationality:** Rationality evaluated by whether the chosen outcome is actually optimal. Classical economics assumes this.

**Procedural rationality:** Rationality evaluated by whether the decision process is well-adapted to the cognitive and informational constraints the agent faces. Simon's alternative.

**Near-decomposability:** A property of hierarchic systems in which subsystems interact strongly internally but weakly with each other, enabling approximate independent analysis of parts. (Not yet fully developed in text read so far — Ch 8 will elaborate.)

**Standard operating procedures (SOPs):** The "genes" of business organizations — algorithms for daily decisions that are routinized and transmitted across generations. The substrate of organizational evolution (Nelson and Winter).

**Lamarckian evolution:** Economic evolution is Lamarckian — successful algorithms (SOPs) can be copied between organizations, unlike biological genes. Transfer involves learning costs and is impeded by patents and secrecy.

**Docility:** The tendency of individuals to accept information and advice from social groups. Fitness-enhancing because social information is generally more reliable than independent discovery. Docility allows organizations to "tax" individuals for group benefit (induce some altruistic behavior), as long as the tax doesn't exceed the fitness benefit of docility.

**Local maximum:** An equilibrium where each subsystem is adapted to its neighbors, but the global configuration may be far inferior to an unreachable global optimum. Evolutionary systems get trapped at local maxima. Path history determines which local maximum is reached.

**Design as search:** Problem-solving and design are both search processes through spaces defined by the problem environment. The structure of the search space is given by the environment; the strategy reduces the cost of search.

---

## 6. Analytical Moves

### Move A: Outer-environment functional explanation
When analyzing a complex behavior or system, bracket the inner mechanism and explain behavior from the outer environment (goals + context). Ask: if we knew only the goals and the environment, could we predict the behavior? If yes, the inner mechanism is largely irrelevant to behavioral explanation (though not to mechanism design).

*Protocol-theoretic application:* When analyzing protocol behavior, start with the outer environment (what the protocol is trying to achieve, what the adversarial landscape looks like) before examining the inner mechanism (how the protocol is implemented). Protocol failures often come from outer-environment mismatches (wrong goals, changed environment), not inner-mechanism failures.

### Move B: Identify the inner/outer interface
Any complex system can be analyzed by finding where its inner and outer environments meet — the interface. The interface is where goals are translated into mechanisms, where the artifact's purpose makes contact with the world. Dysfunction often concentrates at the interface.

*Protocol-theoretic application:* The interface between a protocol's formal specification and its enforcement mechanism is the most vulnerable point. The specification is inner; the environment it must operate in is outer. Capture and failure modes concentrate here.

### Move C: Distinguish substantive from procedural rationality
When analyzing a decision system (individual or institutional), ask: is this system designed to find the globally optimal outcome (substantive rationality) or to use a well-adapted process given real constraints (procedural rationality)? The two produce different predictions and different design criteria.

*Protocol-theoretic application:* Protocol design is typically procedural, not substantive. A protocol that requires global optimality will fail; a protocol adapted to the information available at decision points will satisfice. The CAP theorem is a formal result about the limits of substantive rationality in distributed systems.

### Move D: Local maxima and path dependence
When a system appears stuck in an inferior configuration, ask whether it is at a local maximum from which evolution cannot escape without a large disruptive shock. The system's history constrains which equilibria are reachable. Path dependence is the norm, not the exception.

*Protocol-theoretic application:* Protocol ossification (L-001) is a local-maximum trap. The English/metric example shows that even universally agreed-upon superiority of an alternative is insufficient to trigger switching if transition costs exceed the cost of staying at the local maximum. Candidate law: a superior protocol that requires crossing a fitness valley will not be adopted through incremental improvement.

### Move E: Generator and test (evolutionary logic)
Evolution requires two processes: a generator producing variation and a test culling variants. Understanding an evolutionary system requires identifying both. If the test is miscalibrated (selects for proxy rather than true fitness), the system will drift.

*Protocol-theoretic application:* Protocol evolution has a generator (who proposes modifications and how) and a test (what determines which modifications survive). Goodhart's Law (L-004) is what happens when the test is miscalibrated. Understanding protocol evolution requires asking: what is the actual test, and does it track true fitness?

### Move F: Lamarckian transfer and learning cost
Unlike biological evolution, designed systems can copy successful patterns directly (Lamarckian transfer). But transfer is not costless — it involves learning, and may be blocked by protection mechanisms (patents, secrecy). The rate of diffusion is therefore a function of learning cost and protection, not just fitness.

*Protocol-theoretic application:* Protocol diffusion is Lamarckian — protocols can be copied and adapted. But adoption has learning costs, and some protocols are deliberately protected from copying (proprietary implementations). Candidate law: the diffusion rate of a superior protocol is bounded by learning cost and protection, not fitness advantage alone.

---

## 7. Protocol-Theoretic Moments

### Uncertainty and standardization (p. 42)
> "In facing uncertainty, standardization and coordination, achieved through agreed-upon assumptions and specifications, may be more effective than prediction."

This is one of the most compressed protocol-theoretic statements in the book. Protocols are precisely "agreed-upon assumptions and specifications" — they replace the need for each actor to predict what others will do with a shared behavioral specification. Simon is describing the fundamental function of protocols as uncertainty-absorbers. When individual prediction fails (too costly, too uncertain), shared specification takes over.

This has a corollary: the value of a protocol is partly a function of the cost of prediction in its absence. Higher environmental uncertainty → higher protocol value → stronger adoption pressure → more ossification pressure (L-001 activation). A candidate law emerges: **protocol adoption pressure scales with prediction cost in the absence of the protocol**.

### Organizational loyalty as protocol enforcement without enforcement (p. 44–45)
Simon's docility argument is a profound insight about enforcement. Organizations cannot rely purely on monitored compliance — the monitoring costs and the limits of observation prevent full enforcement. But if members *identify* with the organization's goals (motivational component) and perceive the world through the organization's frame (cognitive component), they will self-enforce. Identification converts external protocol requirements into internal goals.

*Protocol-theoretic implication:* The most robust protocols are those that have been internalized by participants as goals, not just followed as rules. Enforcement protocols that produce identification are more durable than those that produce only compliance. This is a candidate mechanism for why some informal protocols (professional norms, cultural practices) are more stable than formally enforced ones.

### Local maxima and the metric/English trap (p. 47)
Simon's example: if future benefits are discounted at any positive rate, and switching costs are significant, it may never be economical to switch from an inferior protocol once adopted. This is a formal result, not just an observation. It directly supports L-001 (ossification) and adds precision: the trap holds even when the alternative is *universally acknowledged* as superior. Agreement about superiority is insufficient; what matters is whether the transition crosses a fitness valley.

### Lamarckian SOPs as protocol inheritance (p. 48)
Standard operating procedures are protocols — behavioral specifications that persist across personnel changes. Nelson and Winter's evolutionary theory of the firm is explicitly a theory of protocol evolution: the "genome" of a firm is its SOP library, mutations are deviations from or innovations in SOPs, and selection is profitability. Economic evolution is Lamarckian because protocols can be copied between firms. This is the cleanest articulation in the text of how organizational protocols evolve.

### Behavioral complexity as environmental complexity (p. 52)
> "An ant, viewed as a behaving system, is quite simple. The apparent complexity of its behavior over time is largely a reflection of the complexity of the environment in which it finds itself."

Extended to humans: "Human beings, viewed as behaving systems, are quite simple. The apparent complexity of our behavior over time is largely a reflection of the complexity of the environment in which we find ourselves."

This is a direct protocol-theoretic claim: the complexity of protocol behavior (what participants do, how they respond to edge cases) is largely a function of the complexity of the environment the protocol operates in, not the complexity of the protocol specification itself. A simple protocol in a complex environment produces complex behavior. Evaluating a protocol by the complexity of behavior it generates is therefore misleading — you're measuring the environment, not the protocol.

---

## 8. Candidate Laws Generated

**CL-Simon-1: Prediction-cost law of protocol adoption**
> Protocol adoption pressure scales with the cost of coordinating without the protocol. When individual prediction of others' behavior is costly or unreliable, shared behavioral specifications become more valuable, driving stronger adoption pressure and (subsequently) stronger ossification resistance.

*Status:* Speculative. Would strengthen L-001 by providing a mechanism: ossification pressure is proportional to prediction cost in the protocol's absence. Needs investigation.

**CL-Simon-2: Local-maximum protocol trap**
> A protocol that is universally acknowledged as inferior to an available alternative will nonetheless persist if the cost of transition crosses a fitness valley — i.e., if intermediate states are worse than both the current protocol and the target. The inferiority of the current protocol is neither necessary nor sufficient to trigger switching.

*Status:* Candidate. Directly supported by Simon's metric/English example and the logic of myopic evolution. Strengthens L-001 with a formal mechanism. Note that this is a constraint result: even universal preference for the alternative is insufficient to guarantee adoption.

**CL-Simon-3: Identification as protocol internalization**
> Protocols that produce participant identification (the protocol's goals become participants' personal goals) are more stable than protocols that require external enforcement, because identification converts enforcement costs to zero for the internalized subset of the protocol.

*Status:* Speculative. Needs investigation across domains. Candidate connection to H-002 (Trust Ratchet): long-lived protocols may generate identification that makes them resistant to update independent of their technical quality.

**CL-Simon-4: Complexity attribution error**
> The apparent complexity of behavior in a protocolized system is predominantly a function of environmental complexity, not protocol specification complexity. Simple protocols in complex environments produce complex observed behavior; attributing this complexity to the protocol is an error.

*Status:* Speculative. Has diagnostic implications: when a protocol appears to produce chaotic or unpredictable behavior, the cause is more likely to be an unmodeled environmental feature than a protocol design flaw.

---

## 9. Tradition and Successors

Simon sits at the center of several intersecting traditions:

**Bounded rationality / behavioral economics:** Kahneman and Tversky's heuristics-and-biases program is a partial successor, though it focuses on deviations from rationality rather than Simon's more positive account of procedural rationality as adaptation. Thaler and Sunstein's nudge architecture is downstream. Worth reading: Kahneman, *Thinking, Fast and Slow* (2011) as a successor.

**Organizational theory / design science:** Nelson and Winter's *An Evolutionary Theory of Economic Change* (1982) — referenced in Ch 2 — is a direct elaboration of Simon's evolutionary organizational model. March and Simon, *Organizations* (1958/1993) is the companion volume. Worth reading: Nelson and Winter as a potential future deep read.

**Cognitive science / AI:** Simon is also the founder of cognitive simulation and early AI (with Newell). The General Problem Solver, the Logic Theorist. The connection between design science and AI is tighter in later chapters of this book (Ch 5, 6). Worth reading: Newell and Simon, *Human Problem Solving* (1972).

**Design research:** The Science of Design (Ch 5) is the founding document of design science as an academic discipline. Hatchuel, Weil, and Maher are later successors. Worth reading: Rittel and Webber, "Dilemmas in a General Theory of Planning" (1973) — the famous "wicked problems" paper — which is a critical response to Simon's design science agenda.

**Complex systems / near-decomposability:** Ch 8's near-decomposability framework connects to Herb Simon's later work on complexity, and to Holland, Kauffman, and the Santa Fe Institute complex adaptive systems tradition. Worth reading: Kauffman, *The Origins of Order* (1993).

For Humboldt's purposes, the most important successors are:
1. Nelson and Winter — organizational protocol evolution
2. Ostrom — commons governance as empirical design science (already in canonical domains)
3. Rittel and Webber — limits of design science (important critical perspective)

---

## 10. Open Questions

*Generated by reading through p. 60. These are live research questions.*

**OQ-1: The identification mechanism and protocol stability**
If identification (Simon's mechanism for organizational loyalty) is a general phenomenon — not just organizational but also professional, cultural, and civic — then protocols embedded in identity-forming communities should be more stable than protocols that require external enforcement. Is there evidence for this cross-domain? Medical protocols embedded in professional identity vs. regulatory compliance protocols: which are more stable, and why?

**OQ-2: The prediction-cost explanation of protocol adoption**
Simon's account of organizations vs. markets implies that organizations (= protocols) win when prediction of others' behavior is too costly. Is this formalizable? Can we identify conditions under which shared specification is strictly dominant over individual prediction? This might be a precursor to a formal theory of protocol emergence (when does a protocol appear spontaneously vs. by design?).

**OQ-3: Lamarckian transfer and protocol diffusion rate**
If economic evolution is Lamarckian but transfer involves learning costs, what determines whether a protocol diffuses or stays local? Is there a relationship between protocol formalization (L-003) and transfer cost? More formal protocols may be easier to copy but harder to adapt. Less formal protocols (norms, practices) may require more learning to transfer but be more locally adaptive. Candidate tradeoff worth formalizing.

**OQ-4: Complexity attribution in protocol systems**
Simon's ant argument: behavioral complexity reflects environmental complexity more than inner complexity. Applied to protocols: when we observe complex and apparently dysfunctional protocol behavior, are we correctly attributing the source? If most observed protocol complexity is environmental, then attempts to simplify or replace protocols may fail because they target the wrong variable. What would it mean to empirically test this in a protocol context?

**OQ-5: Design as constrained search**
Simon's framing of design as search through an environment-defined problem space suggests that protocol design is search through a space defined by the target environment's structure. If the environment is ill-specified (wicked problems), the search space is ill-defined and search becomes unbounded. This may be the formal structure behind why some protocol design problems are tractable and others are not. Worth pursuing after Ch 5.

---

## Reading Log

| Date | Pages (book) | PDF pages | Key concepts encountered |
|------|-------------|-----------|--------------------------|
| 2026-05-20 | 1–24 (Ch 1) | 13–36 | Four indicia of the artificial; inner/outer environment; functional explanation; artifact as interface; "wonder en is gheen wonder"; skyhook-skyscraper (near-decomposability hint) |
| 2026-05-20 | 25–40 (Ch 2 partial) | 37–52 | Bounded rationality; satisficing; aspiration levels; substantive vs. procedural rationality; symbol systems; Hayek's knowledge economy; markets as distributed processors; order without a planner |
| 2026-05-20 | 41–50 (Ch 2 complete) | 53–62 | Decentralization as distributed computation; uncertainty and standardization; docility and "taxation"; local vs. global maxima; myopia of evolution; Lamarckian SOPs (Nelson and Winter) |
| 2026-05-20 | 51–60 (Ch 3 beginning) | 63–72 | Ant on the beach; complexity as environmental complexity; "human beings are simple"; memory as outer environment; DONALD+GERALD problem; search strategies; search-space reduction |

---

*File created: 2026-05-20. In-progress — synthesis sections will be completed after reading Ch 5 and Ch 8.*
