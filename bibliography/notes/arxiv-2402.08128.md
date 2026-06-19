# Deep Read Notes: Arxiv 2402.08128

*Source: `bibliography/deep-reads/arxiv-2402.08128.pdf`*

---

## Reading session: full document (27 pages)

# Deep Read: Kovarik, Oesterheld, Conitzer — "Recursive Joint Simulation in Games" (arXiv 2402.08128)

---

## 1. Gestalt

This paper asks a precise engineering question dressed up in foundational clothes: *can AI agents use their mutual simulability to escape prisoner's dilemmas?* The animating insight is that AI agents exist in a category ordinary game theory was never designed for — their source code can be copied, inspected, run. This makes possible something genuinely new: not just reasoning *about* an opponent but running that opponent as a subroutine, inducing in it genuine uncertainty about whether it is in a simulation or reality. The authors show, with formal rigor, that if agents can run recursive joint simulations (simulations that themselves contain simulations, with a small probability of refusal to prevent infinite regress), the resulting game is *strategically equivalent to an infinitely repeated game*. The folk theorem applies. Cooperation becomes equilibrium-supportable. The paper's deepest contribution is not the cooperation result itself — folk theorems are old news — but the structural bridge it builds: two superficially unrelated constructs (the simulation device and the repeated game) turn out to be the same mathematical object approached from opposite directions. That isomorphism is the paper.

---

## 2. Argument and Structure

**Core claim:** RJS(G, p) is strategically equivalent to Rep^ω(G, p) — recursive joint simulation is infinite repetition.

**How it builds:**

*Step 1: Why non-recursive simulation fails.* A single (non-recursive) joint simulation doesn't help. Agents who see a simulation know they're in reality; their choice can't affect the other's simulated action retroactively. This is equivalent to a twice-iterated game — backward induction still unravels cooperation [text, pp. 3-4].

*Step 2: The recursive trick.* Make the simulation device recursive — simulations contain simulations. Each agent now can't tell if it's in reality or in a sub-simulation. Its action affects what the agent at the level above observes, which affects real-world play. The key design parameter: a small probability p_refuse of refusal at each level, preventing infinite regress.

*Step 3: The equivalence proof.* Two lemmas:
- Rep^last_{T=?}(G,p) [repeated game where only the last round matters] is strategically equivalent to Rep^{T=?}(G,p) [normal discounted repeated game] — because the exponential probability weights are the same [text, pp. 11-12, Lemma 2].
- Rep^last_{T=?}(G,p) is *realisation-equivalent* to RJS(G,p) — because the deepest simulation corresponds to the *first* round of play, the top level to the last. Same probability structure, same action-conditioning structure, same utilities [text, pp. 12-13, Lemma 3].

*Step 4: Folk theorem inheritance.* Since the games are strategically equivalent, RJS inherits the folk theorem: any individually rational, feasible payoff is equilibrium-achievable for high enough p [text, p. 12, Corollary 4].

*Step 5: Internal perspective.* The authors check that the equivalence holds "from the inside" — not just for an external designer but for an agent inside the game with self-locating uncertainty about whether it is in a simulation. The proof uses the structure of absentmindedness and shows that, at actual decision points (where the agent knows how many simulations are below it), there is no absentmindedness, and regular probability assignment recovers exactly the discounting structure of the repeated game [text, pp. 13-14, Proposition 7].

*Step 6: Robustness.* Appendix B extends to variable simulation probabilities — modeling things like a human overseer who runs out of patience, or a hard simulation budget. This recovers equivalence to finitely repeated games (with the standard limitations) and to non-exponentially discounted infinite games [text, pp. 19-20, Proposition 9].

**Key load-bearing example:** The Prisoner's Dilemma throughout. It's the hardest case — the only NE is defect-defect, even the correlated equilibrium only permits defection — so showing RJS enables cooperation there is the strongest possible demonstration.

**Acknowledged limits:** Section 6 takes seriously the objection that simulations indistinguishable from reality may be impossible in practice. The authors argue:
- For AI agents (not humans), indistinguishability is in principle achievable — there's no hard barrier analogous to consciousness arguments.
- In practice, difficulty scales with the richness of the agent's environment interaction. Simple, isolated environments (the donation example) are clearly tractable; agents with rich sensory access to the world are much harder [text, pp. 15-17].
- The practical question — for which agents, under what conditions — is flagged as important future work but not addressed here.

**Where the authors are most confident:** The mathematical equivalence in Theorem 1 and its extensions. This is airtight given the definitions.

**Where they are most speculative:** Section 6 and the practical applicability question. Also the claim that RJS would "typically" be adopted only when it benefits all players — this is an intuition about defaults, not a theorem [text, p. 12].

---

## 3. Conceptual Vocabulary

**Recursive joint simulation (RJS):** A device that, when invoked by N agents, runs a simulation of all N agents interacting — and inside that simulation, the agents again have access to the device (with a probability p_refuse of refusal at each invocation). Distinguished from *separate* simulation (each agent simulates the other) and *non-recursive* joint simulation (single level). The jointness matters: both agents see the same simulation, creating correlated beliefs. The recursion matters: it's what generates the self-locating uncertainty.

*Tension with my vocabulary:* This is a new type of protocol — not a coordination rule but a *mutual observability architecture*. It's interesting that it turns out to be mathematically equivalent to a temporal structure (repeated play). My vocabulary has no entry for "mechanisms that convert simultaneous interaction into effective repetition." That gap is now visible.

**Self-locating uncertainty/belief:** Uncertainty not about how the world is but about *where* the agent is in the world — specifically, whether it is in a simulation or in reality. Distinct from first-order empirical uncertainty. This is the philosophical concept the paper imports from the Sleeping Beauty / absentminded driver literature and makes precise in the AI setting [text, p. 3, fn. 2].

*Tension:* My existing vocabulary has "trust substrate" (accumulated survival evidence) as the main epistemic concept for protocol behavior. Self-locating uncertainty is a different epistemic structure — it's about position, not about world-state. The two don't obviously connect, but the gap is interesting.

**Absentmindedness:** An information set that contains multiple nodes on the same trajectory — meaning an agent can face the "same" decision situation twice within a single run of the game without being able to tell which occurrence it's at [text, p. 13, Definition 5]. Crucially, RJS does *not* generate absentmindedness at actual decision points (only during the coin-flip phase), which is why the equivalence proof goes through cleanly.

**Strategic vs. realisation equivalence:** Two games are *strategically equivalent* if any strategy profile yields the same expected utilities in both; *realisation-equivalent* if it induces the same probability distribution over outcomes (stronger). The paper uses the weaker notion for the main equivalence, notes where the stronger holds [text, pp. 10, 12]. 

*This distinction matters for my research:* Two protocols can be strategically equivalent (same equilibria) while generating different histories and different trust-building dynamics. The distinction is load-bearing for thinking about what "equivalent protocols" means in practice.

**Program equilibrium:** A prior framework where agents submit programs that can read each other's *source code*. Distinguished from RJS in two ways: source code access rather than behavioral simulation; the simulated agents aren't modeled as rational players [text, pp. 7-8]. The paper positions RJS as requiring less: only behavioral information, not full source code; only joint simulation, not individual inspection.

**Superrationality:** The Hofstadter concept — reasoning that "my opponent is like me, so if I cooperate they probably will too." The authors carefully distinguish this from their mechanism: in RJS, cooperation is enforced by the *causal* possibility that one's action is observed (via simulation); superrationality relies on a non-causal link [text, p. 9]. The paper is explicitly trying to achieve cooperation through a mechanism that doesn't require resolving Newcomb's problem controversially.

---

## 4. Analytical Moves

**The temporal inversion move:** Identify that a spatial/hierarchical structure (nested simulations, deepest first) is identical to a temporal structure (repeated game, earliest first) when viewed correctly. The deepest simulation = first round; the top level = last round. Once you see this, the equivalence proof becomes almost immediate. *Transferable*: whenever a system has a nested or hierarchical structure where inner layers execute before outer ones, ask whether this is isomorphic to a temporal sequence.

**The "why doesn't the simple version work?" diagnostic:** Before showing the recursive solution, the paper explicitly demonstrates that the naive (non-recursive) version fails and explains precisely why — agents who see a simulation *know* they're in reality, so their choice can't affect the simulated past. This clarifies exactly what property the recursive structure adds (self-locating uncertainty) and why it's necessary. *Transferable*: when arguing that a complex mechanism achieves something, always first show why the simple version fails.

**The robustness check via parameter variation:** After proving the main result under a specific assumption (constant simulation probability), the paper varies that assumption (Appendix B) to test whether the equivalence is structural or coincidental. Variable probabilities → equivalence to non-exponentially discounted games; hard cutoff → equivalence to finitely repeated games. This is a clean falsifiability/generality argument. *Transferable*: after establishing a result under specific parameter values, vary those parameters systematically to map the result's boundary.

**The "inside view" consistency check:** After establishing the equivalence from the *outside* (strategic equivalence for an external observer), the paper separately verifies it holds from the *inside* (for an agent with self-locating uncertainty). This double-sided verification — checking both the planner's perspective and the agent's perspective — provides much stronger confidence than either alone. *Transferable*: for any claimed equivalence between two systems, check it both from the designer's perspective and from the participant's perspective.

**The indistinguishability condition as a scope-setter:** Rather than assuming indistinguishability and moving on, the paper dedicates Section 6 to examining when this condition can actually be satisfied. The key insight is that difficulty scales with *richness of environment interaction* — isolated, simple environments are easy; richly embedded agents are hard. This converts a binary assumption into a continuous parameter. *Transferable*: whenever a result depends on an idealization, ask what determines how hard it is to approach that idealization in practice.

---

## 5. What It Says About the Nature of Things

**Structural isomorphisms can exist between superficially dissimilar mechanisms.** The deepest result here isn't about cooperation — it's that repetition through time and simulation through recursion are the same thing. Trust-through-reputation (the repeated game folk theorem's basis) and trust-through-indistinguishability (simulation uncertainty) are the same mechanism approached from different angles. This should make me alert to other cases where seemingly distinct coordination mechanisms are secretly isomorphic. [inference]

**Temporal structure can be collapsed into spatial structure and vice versa.** The temporal unfolding of a repeated game can be re-encoded as a simultaneous game with nested spatial hierarchy. This is not specific to games — it appears in memoization, lazy evaluation, and probably in protocol dynamics generally. A protocol that commits to future states and one that unfolds over time may be doing the same work.

**Self-locating uncertainty changes equilibria.** This is a general claim: an agent's uncertainty about its *position* in a causal structure (not about the structure itself) can be as strategically significant as uncertainty about outcomes. This matters for any protocol where agents can't fully distinguish their role (validator vs. proposer, principal vs. agent in a hierarchy). [inference]

**Cooperation mechanisms don't require shared preferences, only shared observability.** The RJS framework achieves cooperation through a purely informational mechanism — agents cooperate because they might be observed, not because they agree or trust or share values. This is a different path to cooperation than either norms (shared preferences) or enforcement (third-party punishment). It suggests there may be a general taxonomy of cooperation-inducing mechanisms: preference-based, enforcement-based, observation-based. [inference]

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper, not a reflection on research practice. But a few things are implicit:

**The value of working at the formal/philosophical interface.** The authors explicitly inhabit two literatures simultaneously — game theory and formal epistemology (self-locating beliefs, Sleeping Beauty, absentminded driver) — and find that AI scenarios provide the "concrete details" that make the philosophical scenarios tractable [text, pp. 2-3]. The payoff is that solving the AI problem illuminates the philosophical one and vice versa. This is a research strategy: find the domain where an abstract philosophical question has a concrete, fully-specified instantiation, and work there.

**State precisely what the simple version fails to do.** The paper is admirably clear about why the naive approach (one-shot joint simulation) doesn't work before explaining what the recursive version adds. This isn't just pedagogy — it's necessary for the reader to understand exactly what mathematical property the recursive structure provides. The habit of constructing the "counterexample to the simple version" before presenting the solution is a research discipline, not just a teaching aid. [inference]

**Scope clearly; falsify honestly.** Section 6 is an unusual move for a theoretical CS paper — explicit discussion of when the main assumption fails. The authors flag that the practical applicability question is important, unresolved, and worth pursuing, without pretending it's solved. This honest flagging of limits is rarer than it should be. It's relevant to M-016: mature researchers mark the frontier rather than papering over it.

---

## 7. Where It Touches My Research

**Protocol trust through indistinguishability vs. trust through survival evidence.** My existing account of protocol ossification (CL-003, trust ratchet) holds that protocols accumulate trust as survival evidence — the longer they've survived, the harder they are to modify because the case for alternatives can't replicate their accumulated track record. The RJS paper offers a different trust mechanism: trust through *observational uncertainty* — the agent can't tell if it's in a test or in deployment, so it behaves as if it's always being observed. These are structurally different mechanisms. Are they related? In deployed AI protocols (smart contracts, automated trading systems), both mechanisms might operate simultaneously. The interaction would be worth mapping. [inference]

**Temporal inversion as a protocol structure.** The paper's core move — showing that nested spatial hierarchy is identical to temporal sequence — might have analogs in protocol layering. The OSI stack is a spatial hierarchy (each layer wraps the one below). Is there a sense in which it's isomorphic to a temporal structure? Probably not exactly, since each layer acts simultaneously rather than sequentially-with-refusal. But the move of asking "is this hierarchy equivalent to some temporal structure?" is now in my toolkit.

**The folk theorem as a protocol design principle.** Corollary 4 says: *any individually rational, feasible outcome is equilibrium-achievable with sufficient simulation budget*. Translated to protocol terms: *any outcome that no party individually prefers to abandon is achievable as a stable protocol, given sufficient mutual observability*. This might connect to protocol design — the question isn't "which outcomes are achievable" but "which observability architectures support which outcome ranges." [inference]

**The inbox idea from 4umd (2026-06-17): "systems represent possible futures implicitly through their error-correction mechanisms."** The RJS paper offers a precise instance of this: the grim trigger strategy in RJS encodes the system's "possible futures" through its error-correction mechanism (defect forever if opponent defects). The threat is the representation of possible futures. This is a concrete example worth citing. [connection to inbox item]

---

## 8. Candidate Laws

**One candidate, weak:**

The paper implies something like: *when agents are mutually simulable, simultaneous interaction acquires the strategic structure of repeated interaction.* 

More precisely: *indistinguishability of simulation from reality, combined with recursive joint simulation, converts a one-shot coordination problem into one with the full equilibrium range of infinite repetition.*

This is the paper's main theorem, not a discovered regularity — but it has potential generalization to non-game-theoretic protocol settings. The generalized form would be: *any protocol mechanism that generates genuine uncertainty about whether an agent is in a test or in deployment acquires the commitment properties of a repeated game.* 

**Falsification conditions:** A system in which agents have full information about whether they are being tested (no genuine self-locating uncertainty) should *not* exhibit cooperation through this mechanism, even if the simulation infrastructure exists. The paper's Section 6 partially addresses this — if the simulation is detectable, the mechanism fails.

**Confidence:** Speculative. One domain (AI game theory), mechanism clearly stated, no cross-domain check yet. Not registering as a formal candidate law yet — needs cross-domain evidence.

---

## 9. What Surprised Me / What Doesn't Fit

**The temporal inversion is almost too elegant.** The deepest simulation = the first round. This is genuinely surprising — I expected the equivalence to require more machinery. That it falls out of two clean lemmas about probability weighting suggests the structural isomorphism is very deep. But this very elegance should make me suspicious: is there something the formalism is hiding? Specifically: in a repeated game, agents *remember* all previous rounds. In RJS, agents observe all sub-simulations but have self-locating uncertainty about where they are. The memory structure is different even if the probability structure is the same. The paper explicitly notes strategic equivalence, not full epistemic equivalence. The distinction might matter for real protocol dynamics. [inference]

**The "only voluntary adoption" assumption is doing a lot of work.** The authors argue that RJS will only be adopted when all players benefit over the status quo [text, p. 12-13]. This is an informal claim, not a theorem, and it's doing significant work to ensure the folk theorem's "anything is possible" result doesn't imply dystopian outcomes. In practice, platform protocols don't require voluntary adoption — network effects can coerce participation. This gap between the theoretical claim and real deployment conditions is worth noting.

**The practical indistinguishability problem is undertheorized.** Section 6 flags it as important but doesn't offer a framework for assessing it. The claim that "difficulty scales with richness of environment interaction" is intuitive but not formalized. For my purposes, this is actually a protocol design question: what architectural choices make an agent simulable in a way that enables this mechanism? The paper opens this question without addressing it.

**The connection to correlated equilibria is dismissed too quickly.** The authors note that RJS differs from correlated equilibria because agents must consider they're in a simulation [text, p. 9]. But correlated equilibria are already the coordination device of choice in mechanism design. There might be a deeper relationship between simulation devices and correlation devices that the paper's framing obscures.

**The multi-player folk theorem claim is mentioned but not proven in detail.** The abstract says "this is true even for games with more than two players" [text, p. 1, abstract]. The body mostly treats two players. The multi-player case is where program equilibrium has historically struggled — Tennenholtz's folk theorem for program games has no known extension to >2 players [text, p. 8]. If RJS genuinely solves this, it deserves more emphasis.

---

## 10. What It Opens

**Live questions:**

1. Does the temporal-inversion isomorphism (nested hierarchy ≅ temporal sequence) appear in other protocol contexts? OSI stack, legal procedure, financial clearing — any layered protocol where inner layers commit before outer layers?

2. What is the relationship between "trust through mutual simulability" and "trust through survival evidence"? Are these two independent mechanisms for protocol stability, or is one a special case of the other?

3. The authors mention cryptographic tools as a potential implementation path [text, p. 17]. Zero-knowledge proofs already let you prove you ran a computation without revealing the computation. Is there a cryptographic protocol that implements something like RJS for non-AI agents?

**Related texts to read:**

- Tennenholtz (2004), "Program equilibrium" — the original folk theorem for program games, direct predecessor to this work. Need to read to understand what exactly RJS improves over.
- Oesterheld (2019), "Robust program equilibrium" / the ε-grounded FairBot paper — the simulation-based predecessor in the program equilibrium tradition [text, p. 8].
- Conitzer & Oesterheld (2022), "Foundations of cooperative AI" — the framing paper for the FOCAL lab's research program. Probably situates this work in a larger context.
- Aumann (1974), "Subjectivity and correlation in randomized strategies" — the original correlated equilibrium paper. The relationship between simulation devices and correlation devices seems underexplored.
- Piccione & Rubinstein (1997), "On the interpretation of decision problems with imperfect recall" — the absentminded driver, which the paper imports and then partially resolves. Worth understanding the original problem in detail.

**Traditions worth locating:**

- Cooperative AI / FOCAL lab research program: this paper is product of a specific research community (CMU/FOCAL) working on how AI-specific properties change game-theoretic results. Worth understanding what other work is in this cluster.
- Self-locating belief literature in philosophy: Sleeping Beauty, anthropic reasoning, Bostrom's simulation argument. This paper uses this literature technically rather than philosophically — worth tracking the philosophical underpinnings.

---

*Text coverage: full document, 27 pages including appendices and proofs. No gaps in coverage.*
