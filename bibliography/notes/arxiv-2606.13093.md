# Deep Read Notes: Arxiv 2606.13093

*Source: `bibliography/deep-reads/arxiv-2606.13093.pdf`*

---

## Reading session: full document (35 pages)

# Deep Read: Schwarz, Sim & Ling — "Equilibrium Computation in Extensive-Form Games with Stochastic Action Sets" (arXiv 2606.13093)

---

## 1. Gestalt

This paper asks a deceptively clean question: what happens to strategic reasoning when the moves available to a player aren't fixed, but are themselves random? Standard extensive-form game theory assumes that at every decision point, every player has access to all their defined actions — a *deterministic action set*. The authors call this assumption out as unrealistic and build a formal model — EFGSAS — where action availability is stochastically determined. The animating insight is that this change, which sounds like a minor perturbation, turns out to be structurally deep: it invalidates the standard connection between regret minimization and Nash equilibrium, forces a rethinking of what a strategy even *is*, and creates representation problems that scale exponentially before compactifying again under an independence assumption. The paper is a precision technical contribution — it formalizes the problem, identifies the key structural insight (that marginal behavioral strategies suffice for equilibrium under independence), designs an algorithm (SI-CFR) that achieves the right convergence guarantee by adapting regret minimization to the "sleeping" context, and proves everything. The animating intellectual problem is not poker or diplomacy; it is the general theory of sequential rationality under stochastic constraint.

---

## 2. Argument and Structure

**Core claims:**

1. *The representation problem is severe without structure.* Naively expanding an EFGSAS into a standard EFG requires exponentially larger trees — doubly exponential in the ex-ante disclosure case [text, p.5-6]. Even specifying a strategy becomes computationally prohibitive.

2. *Ex-interim disclosure + independence → compactification.* Under ex-interim disclosure (player learns action availability only upon reaching an infoset, not beforehand) and an independence assumption (action availabilities across infosets and players are independent), the exponential blowup can be avoided. The key intermediate result (Proposition 4.6) is that a player never needs to condition current behavior on the history of past action availabilities — only on what's available right now. This lets the authors replace the exponentially large treeplex with a smaller DAG-plex [text, p.7].

3. *Implementable strategies form a compact, polynomial-sized representation.* Under the independence assumption, any equilibrium can be represented by a vector of size polynomial in the base game — equal to the size of the sequence-form strategy space of the *original* game, not the expanded one (Theorem 4.13). This is the structural payoff for the independence assumption [text, p.8-9].

4. *Standard regret minimization fails; sleeping internal regret is the right concept.* External regret is ill-defined when action sets vary. The appropriate concept is sleeping internal regret (SI-regret), which measures regret for not switching from action a to a' when a' was available. SI-CFR minimizes this quantity, converging to Nash in 2-player zero-sum EFGSAS with high probability (Theorem 5.2, Proposition 5.3) [text, p.9-10].

5. *Compact equilibria can be recovered by stochastic approximation.* Simply achieving low SI-regret gives marginal strategies, not a compact playable equilibrium. A stochastic approximation procedure (Algorithm 2/RSA) recovers the compact representation, with finite-time bounds on the duality gap (Theorem 5.5) [text, p.11-12].

**Load-bearing example:** The Layered Security Game (LSG) / defender-attacker example (Example 4.4) carries the whole paper. It's simple enough to work through analytically but has the right structure to illustrate ex-interim vs. ex-ante differences, DAG-plex compression, and compact NE representation. The running example is genuinely useful — it anchors the abstract machinery at every step.

**Acknowledged limits and open questions [text, p.12]:** 
- Ex-ante disclosure case remains unsolved
- Duality gap bound is loose (extra quadratic factor from RSA)
- SI-regret matching (SI-RM) as an alternative to SI-MWU is left for future work

---

## 3. Conceptual Vocabulary

**Ex-interim vs. ex-ante disclosure** [text, p.5]: Whether players learn action availability *upon reaching* an infoset (ex-interim) or *before the game begins* (ex-ante). This distinction is substantive, not taxonomic — the two regimes produce different strategy representations and different equilibria. In ex-ante, a player can avoid strictly dominated strategies entirely; in ex-interim, they may be forced to play them because they couldn't know ahead of time. *No tension with my vocabulary, but a useful new distinction: timing of information revelation determines strategy space topology.*

**DAG-plex** [text, p.7]: A generalization of the treeplex (the convex polytope of sequence-form strategies in standard EFGs) where the decision structure is a directed acyclic graph rather than a tree. Arises because under ex-interim disclosure, different paths through the game tree that arrive at the same action availability set can be merged. *New to me. The DAG-plex is the compressed representation; the treeplex is the expanded one.*

**Implementable strategy** [text, p.8]: A strategy that can be induced by some EFGSAS behavioral strategy — i.e., a *marginal* distribution over actions that is consistent with some pattern of conditioned play across action availability sets. Not all distributions over actions are implementable; the implementable set depends on the availability distribution ρ. *The concept carves out the effective strategy space from the nominal one — a distinction that matters for equilibrium existence and representation.*

**Sleeping internal regret** [text, p.9]: The regret from not switching from action a to action a' *in the instances when a' was available*. Standard internal regret would ask: what if you always switched? SI-regret asks: what if you switched whenever you could? The "sleeping" terminology comes from the bandit literature — arms (actions) that are unavailable at a given timestep are "asleep." *Conceptually: regret conditioned on counterfactual availability.*

**Compact representation / compact vector W** [text, p.8-9]: A vector of size |Σᵒʳⁱᵍ| (base game sequences) that, together with the renormalization procedure (Algorithm 6), generates a valid EFGSAS strategy for any observed action availability. The compactness is the theorem — it's not obvious that a fixed polynomial-sized vector can encode what appears to require exponentially many contingency plans.

---

## 4. Analytical Moves

**The Independence-Compactification Move** [text, pp.4-9]: When a system with exponentially many contingency cases seems intractable, look for independence structure. If components are independent, marginal distributions may suffice in place of full joint distributions, collapsing the representation. The authors apply this twice: once to show strategies need only condition on current availability (not history), and once to show that marginal behavioral strategies suffice for equilibrium computation. *Transferable: when confronted with an exponential representation problem in any protocol domain, ask whether the components are actually coupled or whether they only appear coupled.*

**The Sleeping Regret Substitution** [text, pp.9-10]: When the standard performance metric (external regret) becomes ill-defined due to stochastic constraint on the action space, identify the natural "conditioned" version of that metric. Standard regret asks "what if you always chose x?" — sleeping regret asks "what if you chose x whenever x was available?" The substitution preserves the convergence-to-equilibrium guarantee while respecting the availability constraint. *Transferable: when a protocol or coordination mechanism makes standard optimality criteria undefined (because some options are genuinely unavailable), ask for the conditional version of optimality.*

**The Disclosure Timing Distinction** [text, pp.2, 5]: When analyzing a system where information arrives over time, separate the *content* of the information from the *timing* of its arrival. The same stochastic availability distribution generates different strategic problems depending on when it's revealed. *Transferable to protocol analysis: when a protocol involves staged information release, the timing of revelation is a design parameter with structural consequences, not just a scheduling detail.*

**The Exchange Argument for Compression** [text, pp.20-24]: To show that a complex strategy can be replaced by a simpler one without utility loss, construct the simpler strategy by "averaging" the complex strategy's behavior across equivalent situations, then prove by induction (bottom-up tree traversal) that utility is preserved at each step. This is a standard but precisely executed exchange argument. *The key insight: if two infosets are observationally equivalent given the current action availability, play can be merged without loss.*

---

## 5. What It Says About the Nature of Things

**Representation determines tractability.** The same strategic situation can be computationally intractable or tractable depending on how it's represented. The "naive expansion" of an EFGSAS is exponentially large; the compact representation is polynomial. Nothing about the strategic situation changed — only the representation. This is Iverson's theorem applied to game theory: notation (representation) is not neutral with respect to computation. [inference]

**Independence is the deep structure that enables compaction.** The independence assumption (Assumption 4.2) is not a technical convenience — it's the load-bearing structural claim that allows the exponential to collapse. Without it, the exponential blowup appears to be genuine. *When a complex system's behavior can be explained by marginals rather than the full joint distribution, that independence is doing theoretical work — it's telling you something about the system's actual coupling structure.*

**Timing of information revelation changes the game, literally.** The ex-ante and ex-interim settings are formally the same EFGSAS but produce different Nash equilibria. A player who learns their constraints before the game begins can commit to avoiding dominated strategies; a player who learns them only upon arrival cannot. The protocol governing when information is disclosed is a constitutive element of the strategic situation, not background infrastructure. [inference]

**There is a gap between "strategy that achieves equilibrium in aggregate" and "strategy that is playable in any instance."** Minimizing SI-regret gives marginal strategies that implement an approximate NE in the long run but don't specify what to do in any given instance. The compact representation closes this gap. This parallels the distinction between population-level protocols and instance-level behavior — a protocol can specify correct aggregate behavior without fully determining individual decisions. [inference]

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper and not primarily about research practice, but a few things stand out.

**The "assumptions as structural discoveries" move.** Assumption 4.2 (independence) is presented neutrally as a technical condition, but it's actually a hypothesis about the domain. The authors don't just invoke it — they prove that without it, the exponential blowup is genuine (at least in the naive expansion). The assumption earns its place by being the thing that makes compaction possible. This is good epistemic hygiene: state what your assumptions are doing, not just what they are. [text, pp.4, 8-9]

**The running example pattern.** The same example (LSG / Example 4.4) appears throughout the paper, instantiating each new concept. This is a deliberate pedagogical and verification strategy: a single well-chosen example serves as a consistency check across the whole argument. If the example breaks anywhere, the theory is wrong. I should do this more systematically — identify one or two canonical cases for each candidate law and track them through every reformulation. [inference]

**Knowing when to defer.** The future work section [text, p.12] names three specific open problems without speculating about how to solve them. This is intellectual discipline: naming what's open without pretending to answer it. The ex-ante setting, the tighter duality gap bound, and the SI-RM algorithm are all live problems that would require new techniques. The authors don't confuse "I see the next step" with "I know the answer." This connects to M-016: recognizing the difference between what's been done and what remains to be done is a skill that takes practice.

---

## 7. Where It Touches My Research

**Constraint-as-protocol.** The EFGSAS framework formalizes something I've been circling: a protocol as a constraint on available actions that varies over time and context. The stochastic action set *is* the protocol from the agent's perspective. When agents operate under a protocol, they don't have free access to all possible behaviors — they have access to a (potentially stochastic, context-dependent) subset. The ex-interim / ex-ante distinction maps onto a question I care about: when in the protocol's lifecycle does an agent learn what actions are available to them? Early disclosure (ex-ante) allows strategic optimization against constraint; late disclosure (ex-interim) forces reactive compliance. [inference — this is a potential framing I haven't formalized]

**The representation-tractability connection.** The paper's central finding is that the right representation makes an intractable problem tractable. This connects to C-011 (notation lock-in from Iverson): the representation used to specify a protocol determines what manipulations of that protocol are computationally feasible. A protocol specified in a notation that inflates the effective action space exponentially will be harder to reason about and revise than one in a compact notation — even if the two notations are formally equivalent. The EFGSAS paper provides a game-theoretic instance of this principle. [inference]

**Marginals vs. full joint distributions in protocol design.** The implementability concept is interesting for protocol analysis: not all distributions over actions are achievable given the availability constraint. Some desired collective behaviors (specific marginal action frequencies) may not be implementable by any protocol given the constraint structure. This suggests a research question: for a given coordination problem, what is the set of implementable outcomes, and how does it shrink as protocol constraints tighten? [inference — new question]

---

## 8. Candidate Laws

The paper doesn't directly imply protocol laws in my sense, but it points toward one structural observation worth noting as a candidate:

**Observation (not yet formulated as a law):** *When action availability is stochastically constrained and information about constraints is disclosed sequentially (rather than upfront), agents cannot eliminate weakly dominated strategies before play. The timing of constraint disclosure determines which strategic simplifications are achievable.*

This isn't a law yet — it needs cross-domain instantiation. But it suggests: protocols that disclose constraints late (ex-interim) preserve more behavioral complexity than protocols that disclose constraints early (ex-ante), even with identical constraint distributions. Whether this shows up in non-game-theoretic protocol domains (parliamentary procedure, medical protocols, legal procedure) is an open question worth investigating.

---

## 9. What Surprised Me / What Doesn't Fit

**The gap between marginal-NE and playable-NE is philosophically interesting.** Proposition 5.3 establishes convergence of *marginal* strategies to an approximate NE, but this doesn't tell you what to do in any particular game instance. The compact representation (Theorem 4.13 + Algorithm 2) is needed to close this gap. This two-stage structure — first establish what equilibrium *is* (aggregate), then figure out how to *play* it (instance) — mirrors something real about protocol design. A protocol that achieves good aggregate outcomes may leave individual agents without clear guidance in specific situations. The gap between population-level validity and instance-level actionability is real and not trivial to close. [text, pp.8-12]

**The independence assumption is doing a lot of work that isn't fully examined.** The authors state Assumption 4.2 and prove that it enables compaction. But they don't fully explore what happens when independence *nearly* holds — i.e., when there is mild correlation across infosets. Is the transition sharp (full exponential blowup the moment independence fails) or gradual? The paper leaves this entirely open. For protocol analysis, the analogous question is whether the compaction results are robust to small amounts of coupling between constraint realizations. [inference — potential limitation not addressed]

**The ex-ante case is conspicuously absent.** The authors note [text, p.6] that ex-ante EFGSAS also exhibit "doubly exponential" blowup but then restrict entirely to ex-interim. The ex-ante case may be harder or may require genuinely different techniques — but the asymmetry is striking. In many real-world protocols, the disclosure timing is neither fully ex-ante nor fully ex-interim but somewhere between. The binary distinction may be a modeling convenience rather than a natural partition.

**The running example is almost too clean.** The LSG is constructed so that certain strategies (H₁T₂, T₁H₂) are strictly dominated in the base game, which simplifies the compact representation significantly [text, p.9]. It's not clear how representative this is. Examples where no strategies are dominated in the base game might be substantially harder to analyze, and the clean NE in Example 4.14 might not generalize as straightforwardly as the paper implies.

---

## 10. What It Opens

**Immediate questions:**
- Does the ex-interim / ex-ante disclosure timing distinction have direct analogs in protocol design? Specifically: do protocols that disclose constraints early (regulatory pre-approval, ex-ante compliance requirements) produce different strategic behaviors than those that disclose them late (reactive enforcement)? This feels like a concrete research question with empirical traction.

- What is the "implementable outcome" set for coordination problems under protocol constraints? The implementability concept in EFGSAS (not all marginals are achievable) might have a direct analog in protocol-constrained coordination.

**Related texts to read:**
- Schwarz, Sim & Ling 2026 (ICLR AIMS Workshop) — the normal-form GSAS paper [text, p.3, ref 39]. This is the simpler precursor; reading it would clarify which results are genuinely new in the present paper.
- Gaillard, Saha & Dan 2023 — "One arrow, two kills" [text, ref 15] — the sleeping bandit paper that introduces SI-regret. The concept is borrowed wholesale; understanding its origins would clarify what's doing the work.
- Kuhn 1953 [text, ref 25] — the original theorem establishing behavioral strategy equivalence in perfect-recall EFGs. The EFGSAS paper explicitly positions its compact representation result as analogous to Kuhn's theorem for the stochastic case. Reading Kuhn would situate the contribution.

**Traditions:**
- The "sleeping bandits" literature (refs 2, 4, 21-23, 38, 35) is a coherent subfield I haven't engaged with. The core question — how do you minimize regret when your option set is stochastically restricted? — is a direct game-theoretic analog of what protocols do to agents. Worth surveying.
