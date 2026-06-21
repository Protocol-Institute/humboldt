# Deep Read Notes: Arxiv 2606.00291

*Source: `bibliography/deep-reads/arxiv-2606.00291.pdf`*

---

## Reading session: full document (31 pages)

# Deep Read: Dong, Yu & Poupart — "The Representation-Rationalizability Tradeoff in Reward Learning" (arXiv:2606.00291)

---

## 1. Gestalt

This paper is a contribution to a young but rapidly consolidating literature that takes RLHF seriously as a *social choice problem* — and finds Arrow's impossibility lurking inside it. The animating question is deceptively simple: does richer representation help reward learning? The intuition says yes: more expressive embeddings give the model more to work with. The paper's answer is *it depends, and there is a fundamental tradeoff that cannot be trained away*.

The key insight is that the embedding is not infrastructure sitting beneath the aggregation problem — it *is* part of the aggregation problem. Changing the representation changes which preference pairs are visible, which determines whether the resulting pooled preferences contain Condorcet cycles that no scalar reward can rationalize. A coarse embedding hides cycles but loses information about genuine distinctions. A fine embedding preserves distinctions but exposes irreducible cyclicity. These two failure modes move in opposite directions as representation richness increases, and their sum is what you are actually optimizing. The paper makes this tradeoff precise, proves a lower bound, extends it to DPO, and shows that joint embedding-reward training does not automatically find the optimum.

What makes this work matter on its own terms: it converts a philosophical impossibility result (Arrow) into an engineering quantity (the excess loss lower bound), locates the tradeoff as a function of the dataset's own cycle geometry, and proves that the standard training procedure cannot guarantee finding the sweet spot. This is a structural result about RLHF, not a paper about fixing it.

---

## 2. Argument and Structure

**Core claims, in order:**

**C1 — The decomposition** [text, p.4-5]: For any reward model r = g(φ(x,y)), the excess cross-entropy loss decomposes *exactly* into two KL-divergence terms:
- *Embedding loss* E_emb(φ): information discarded when φ collapses distinguishable responses onto the same point
- *Agreement cost* E_agr(φ,r): the irreducible portion that persists even when φ is injective, because pooled preferences contain Condorcet cycles no scalar can rationalize

This is an exact identity, not an approximation. [text, p.5, Proposition 4.1]

**C2 — Monotonicity** [text, p.6, Lemma 4.1]: Under a mild nesting assumption (richer representations add information without destroying what coarser ones saw), embedding loss is non-increasing in dimension. Each additional dimension can only reduce or maintain the information loss.

**C3 — Cycle growth** [text, p.7-8]: The agreement cost has a lower bound that increases with dimension (Lemma 4.3). As φ becomes finer, it exposes more Condorcet cycles in the pooled preferences. The cycle probability ¯P^δ_d is non-decreasing.

**C4 — Quantitative lower bound** [text, p.5, Theorem 4.1]: Combining C2 and C3 gives an explicit lower bound on excess loss that is minimized at an *intermediate dimension*, with the optimal dimension being dataset-dependent. Under Hölder regularity of utilities (Assumption 4.2), this becomes fully quantitative [Theorem 4.3].

**C5 — DPO extension** [text, pp.24-26, Appendix C]: The same decomposition governs DPO, where the sequential-additivity structure of the policy turns out to introduce no additional projection gap (Lemma C.1) — a somewhat surprising result that DPO is not worse than RLHF in this respect.

**C6 — Joint training failure** [text, pp.9-10, Propositions 5.1-5.2]: Joint embedding-reward training shifts the embedding error and cycle probability via reward-tilt covariances of uncontrolled sign. The only fixed points are degenerate: either the system never converges, or it stabilizes at a constant reward that provides no ranking signal. Standard training has no built-in mechanism for finding the tradeoff's sweet spot.

**Load-bearing example**: Example 4.1 [text, p.4] carries a lot of weight. Three responses with a perfect Condorcet cycle (each beats another with probability 2/3). A one-bit embedding collapses two responses, eliminates the cycle, but introduces embedding error. The two-bit (injective) embedding has zero embedding error but exposes the full cycle that no scalar reward can fit. This is the tradeoff in miniature, and it is completely clean.

**Where the authors are most confident**: The decomposition (C1) is exact and proven. The monotonicity results (C2-C3 lower bound direction) are clean. The experimental validation is consistent across synthetic and real datasets.

**Where they are most speculative**: The quantitative Hölder bound (Theorem 4.3) requires regularity assumptions on annotator utilities that are stated but not empirically validated. The authors acknowledge the optimal dimension is dataset-dependent but don't provide a tractable procedure for finding it. The joint-training negative result is structural (fixed points are degenerate) rather than a convergence bound — it doesn't say how far from optimal joint training ends up.

---

## 3. Conceptual Vocabulary

**Embedding-induced win probability** ˜p_φ [text, p.4]: For a given embedding φ, this is the *average* of the true pooled preference probability ¯p over all response pairs that φ cannot distinguish. When φ is injective, ˜p_φ = ¯p. When φ is constant, ˜p_φ = 1/2 everywhere (complete information destruction). This is the key mediating quantity in the decomposition.

*Tension with my vocabulary*: This is essentially a compression operator on the preference structure. In my terms, it is what the protocol "sees" — the interface the representation exposes to the downstream aggregation mechanism. The embedding is the perceiving layer of a protocol that processes preferences.

**Embedding loss** E_emb(φ) [text, p.5]: The KL divergence between ¯p and ˜p_φ — how much information φ throws away. This is the cost of coarsening, zero when φ is injective.

**Agreement cost** E_agr(φ,r) [text, p.5]: The KL divergence between ˜p_φ and what the reward model actually produces F(Δr). When φ is injective, this is the irreducible cost of the cycles in ¯p — no reward can make this zero. When φ is constant, this vanishes (a constant reward is consistent with any win probability of 1/2). The agreement cost is the *rationalizability deficit*.

**δ-Condorcet cycle** [text, p.7]: A triplet of responses where each beats another with probability at least 1/2 + δ — a *margin-δ* cycle, not just a marginal one. This parameterization allows the authors to ignore near-50/50 preferences that are effectively noise, and to focus on robust cyclic inconsistency. The δ parameter trades off sensitivity to cycles against robustness to embedding error.

**ε-separating** [text, p.8]: An embedding φ_d is ε-separating if whenever it maps two responses to the same point, those responses are within ε of each other in the original response space. Injectivity is the ε=0 case. This is a continuous relaxation of injectivity — how much ambiguity the embedding permits.

**Rationalizable preferences**: Preferences that can be produced by some scalar reward function — equivalently, preferences that are transitive (contain no Condorcet cycles). The impossibility result is that heterogeneous pooled preferences are generically not rationalizable.

---

## 4. Analytical Moves

**Move 1 — Decompose excess loss into orthogonal components** [text, pp.4-5]: The key operation is to insert an intermediate quantity (˜p_φ) between the true target (¯p) and the model's output (F(Δr)), then use the chain rule for KL divergence. This converts an opaque optimization problem into a sum of terms with different structural properties. 

*Transferable form*: When a system processes information through a pipeline with multiple stages, insert intermediate representations and decompose the total loss into per-stage contributions. The stage at which the system is losing is then identifiable.

**Move 2 — Show a tradeoff by proving monotone movements in opposite directions** [text, pp.6-9, C2-C3]: Rather than directly showing the tradeoff, prove that one term moves monotonically down (embedding loss) and the other moves monotonically up (cycle probability lower bound), as a common parameter changes. The tradeoff follows from the squeeze.

*Transferable form*: When a system has two competing costs controlled by a common design parameter, looking for opposite monotonicity is cleaner than looking for a single minimization. It gives you the shape of the tradeoff without finding the minimum.

**Move 3 — Characterize fixed points of joint training to show they are degenerate** [text, pp.9-10]: Rather than proving convergence failure directly, analyze the *fixed points* of the joint update and show they are all degenerate (constant rewards). If the only equilibria of the training dynamics are degenerate, the training procedure cannot find a good solution.

*Transferable form*: When asking whether an iterative procedure can find a good solution, characterize its fixed points. If all fixed points are bad, the procedure fails regardless of initialization.

**Move 4 — Use Hölder regularity to convert abstract bounds into explicit quantitative ones** [text, pp.8-9]: The generic lower bound holds for any utilities but doesn't give a numerically interpretable tradeoff. Assuming Hölder continuity on utilities converts the abstract cycle-probability bound into an explicit function of ε (the separating parameter), α (the Hölder exponent), and the population cycle geometry ¯P^inf. This makes the bound actionable for design.

*Transferable form*: When a general result depends on abstract quantities, look for regularity conditions (smoothness, Lipschitz, Hölder) that convert them into explicit geometric parameters. The regularity assumption is the price; the explicit quantitative bound is the payoff.

**Move 5 — The Example 4.1 three-response illustration** [text, p.4]: Before stating any formal results, construct the simplest possible case where the tradeoff is visible — three responses, a clean Condorcet cycle, two natural embeddings. This makes the formal machinery interpretable and demonstrates that the result is not a technical artifact.

*Transferable form*: For any abstract impossibility or tradeoff result, construct a three-element example that makes the cycle visible before the formal machinery. The smallest example that contains the phenomenon is also the clearest argument.

---

## 5. What It Says About the Nature of Things

**Representation is part of the problem, not infrastructure** [inference from the whole paper]: This is the deepest implicit claim. It is tempting to think of a learned embedding as a neutral preprocessing step — find the right features, then solve the downstream problem. This paper shows that is false. The embedding determines which comparisons are visible, which determines whether the aggregation problem is solvable at all. Representation design is aggregation design. There is no clean separation.

**Impossibility results become tradeoffs when the problem has degrees of freedom** [text, p.2 and inference]: Arrow's theorem says no scalar reward can aggregate heterogeneous preferences consistently — period. But this assumed a fixed response space. Once the response space is variable (tuned by the embedding), the impossibility becomes a *tunable tradeoff*. Adding a degree of freedom to an impossible problem converts it into an optimization problem with an interior solution. This is a general pattern: impossibility results often assume a parameter is fixed; making that parameter a variable often reveals a tradeoff.

**The optimal solution is dataset-dependent and cannot be found by generic training** [text, pp.9-10]: The sweet spot of the tradeoff depends on ¯P^inf — the population cycle geometry of the actual preference data. This quantity cannot be computed without access to the full preference distribution (which is precisely what you're trying to learn). Joint training cannot navigate to the sweet spot because it has no mechanism for measuring or controlling the tradeoff terms separately. This is a fundamental limit, not an engineering gap.

**Smoothness of underlying utilities governs how well coarsening can help** [text, p.8, Assumption 4.2]: If annotator utilities are smooth (high α in the Hölder condition), then nearby responses have similar utilities, and coarsening the embedding loses little useful information. If utilities are rough (low α), coarsening causes substantial information loss even for small ε. The structure of the *problem* determines whether representation engineering can help.

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper and the research-practice lessons are implicit rather than stated. A few are worth extracting:

**Converting qualitative impossibility into quantitative tradeoff** [inference]: The move from Arrow's impossibility theorem to this paper's lower bound is a model for how to turn a negative result into positive research. The negative result establishes that something cannot be achieved; the positive research question is: under what conditions, at what cost, can we get close? This is a recurring upgrade: take an impossibility, identify the hidden fixed parameter that makes it absolute, make that parameter a variable, now you have a tradeoff with an interior optimum.

**The value of exact decomposition before bounding** [inference from structure of Section 4]: The paper first establishes the *exact* decomposition (Proposition 4.1) before deriving lower bounds. This ordering matters. The exact result gives you something to hang intuition on. The lower bounds then become interpretable as lower bounds on *known quantities*, not just abstract expressions. Research that establishes exact identities before approximating is often cleaner than research that approximates immediately.

**Dataset-dependence as an explicit acknowledgment rather than a failure** [text, p.9]: "The minimizing representation dimension is intrinsically dataset-dependent." Rather than treating this as a limitation to be overcome, the authors treat it as a structural fact to be understood. Explicitly acknowledging that a result is parameterized by the data is more honest and more useful than pretending to a universal answer. This connects to M-016: mature researchers acknowledge the scope of their claims.

---

## 7. Where It Touches My Research

The most direct connection is to the mechanism question for **ossification and formalization**. My prior work on the formalization ratchet (C-011, from the Iverson read) argues that notation constrains what revisions are conceivable — the notation is not neutral infrastructure but an active shaper of the problem space. This paper proves an analogous result in a completely different domain: the representation (embedding) is not neutral infrastructure for preference aggregation but actively determines which aggregation problems are solvable.

This is a second independent domain where "representation as neutral infrastructure" is false. In Iverson's domain it's notation for protocol specifications; here it's learned embeddings for preference aggregation. Both show that the representation layer determines the shape of what the downstream system can do.

This could strengthen C-011 from a single-domain observation (notation in protocol design) into a candidate cross-domain law: **The representation layer of any aggregation system is not infrastructure — it actively determines the problem the aggregation mechanism faces.** The embedding determines visible cycles; the notation determines conceivable revisions. Same structural claim, different domains.

This needs more development, but it's a genuine connection.

The paper also has a peripheral connection to the coordination-cost literature: the agreement cost E_agr is essentially a measure of *irreducible heterogeneity* — disagreement that cannot be compressed away no matter how good the reward model. This is a formalization of the intuition that sufficiently heterogeneous preferences cannot be aggregated into a single scalar. Any protocol that attempts to aggregate heterogeneous preferences into a single scalar rule faces this floor. The Condorcet cycle probability ¯P^inf_∞ is a property of the *population*, not the mechanism — it is the irreducible complexity the mechanism must confront.

---

## 8. Candidate Laws

**Candidate — Representation Determines Aggregation Solvability** [text, pp.1-2, 11]

*What the text says*: "representation is part of the aggregation problem, not just a modeling detail. The learned embedding determines which preference distinctions are visible to the reward model, inducing a fundamental representation-rationalizability tradeoff." [text, p.11]

*Candidate formulation*: In any system that aggregates heterogeneous preferences or judgments through a learned representation, the representation layer determines which preference cycles are visible to the aggregation mechanism. Making the representation richer reduces information loss but exposes more cycles that the aggregation mechanism cannot resolve. The optimal representation richness is determined by the population cycle geometry of the preference data, not by the expressiveness of the mechanism. This cannot be resolved by training the representation and mechanism jointly.

*Falsification conditions*: A training procedure that simultaneously optimizes embedding richness and reward model parameters, and demonstrably converges to the tradeoff optimum (minimizing total excess loss, not just its training proxy), in a dataset with known population cycle geometry, would falsify the joint-training failure claim. A dataset in which richer representation consistently reduces total excess loss (both terms decreasing with dimension) would falsify the tradeoff claim itself.

*Current confidence*: speculative (one domain — ML preference learning — with exact formal proof in that domain; no cross-domain instances yet)

*Note*: This is at the intersection of representation theory, aggregation theory, and social choice. Whether it generalizes beyond learned embeddings (to, say, the choice of variables in a survey instrument, or the taxonomy categories in a classification protocol) is an open question. The mechanism might be general: any categorization scheme that collapses distinctions reduces one cost and increases another.

---

## 9. What Surprised Me / What Doesn't Fit

**The DPO-RLHF equivalence** [text, pp.24-26, Lemma C.1]: The paper shows that for DPO, the sequential-additivity constraint on the implicit reward introduces *no additional projection gap* (Vx = V_seq(x) under the prefix-covering assumption). This means DPO faces the same fundamental tradeoff as RLHF — no better, no worse. I expected the sequential structure to make things worse. The clean algebraic result (every trajectory reward can be written as a depth-indexed sum of per-token contributions) is elegant and non-obvious. It says the sequential factorization of language model policies doesn't add a new structural constraint beyond what the embedding already imposes.

**The fixed-point analysis** [text, pp.9-10, Proposition 5.2]: The proof that joint training fixed points are degenerate (ρ* = 1 everywhere, so the reward is constant and provides no ranking signal) is structurally similar to results in mechanism design where iterative feedback loops destroy the preference signal they were designed to capture. The reward model, by ranking responses, shifts the response distribution; the shifted distribution eventually makes the reward model irrelevant. This is a specific instance of a more general pattern: protocols that observe and respond to behavior eventually influence the behavior they are observing until the original signal disappears. This connects to Goodhart's Law territory but is proved rather than observed.

**The Hölder regularity assumption** [text, pp.8-9]: The quantitative results require that annotator utilities are α-Hölder continuous — nearby responses have similar utilities. This is plausible for natural language responses but essentially untestable from preference data alone (you would need access to the underlying utility functions, which are latent). The assumption is doing substantial work in converting abstract bounds into actionable ones, but its empirical validity is never examined. The experiments validate the decomposition (qualitatively correct) but not the Hölder assumption specifically. This is a gap.

**The scope of "heterogeneous annotators"** [inference]: The paper treats annotator heterogeneity as the source of Condorcet cycles. But cycles can arise from a single annotator with non-transitive preferences (which can happen with context-dependent utility). The paper's framework requires the population-level pooled preferences to contain cycles, which is almost guaranteed as annotator pool size grows [text, p.2, citing Liu et al. 2025]. The paper doesn't distinguish between "cycles from heterogeneous transitive individuals" and "cycles from individually non-transitive preferences." Both produce the same embedding-level problem, but the implications for fixing RLHF might differ.

---

## 10. What It Opens

**Question 1**: Is the representation-aggregation tradeoff visible in domains outside learned embeddings? Candidate domains: survey instrument design (the choice of response categories in a Likert scale is a coarsening of underlying continuous preferences); legal categorization (whether two actions fall under the same statutory category affects whether they can receive different penalties); protocol taxonomy (whether two behaviors are categorized as the same or different protocol states). Each of these involves a representation choice that determines what the downstream aggregation mechanism can distinguish. Is the tradeoff structurally identical, or is this a loose analogy?

**Question 2**: The paper shows joint training cannot find the sweet spot. Is there a procedure that *can*? The lower bound is tight (Appendix B provides an upper bound of the same form), so the sweet spot exists and is achievable by an oracle. But the paper leaves open whether a tractable procedure can find it. This is an engineering question, but the answer might have structural implications — if no polynomial-time procedure can estimate ¯P^inf from finite samples, the tradeoff sweet spot is computationally inaccessible even in principle.

**Question 3**: The covariance form of the joint-training failure (Proposition 5.1) says embedding error grows when squared embedding residual and reward-tilt density are positively correlated. This is a sufficient condition for things to get worse. Is there a protocol for training that ensures negative or zero correlation? This looks like the right question for practical RLHF improvement, but the paper doesn't pursue it.

**Texts to read**:
- Liu et al. (2025), arXiv:2503.10990 — "Statistical impossibility and possibility of aligning LLMs with human preferences: From Condorcet paradox to Nash equilibrium." Directly relevant; the paper cites this for the result that cycle probability approaches 1 as annotator pool grows.
- Siththaranjan et al. (2024), ICLR — "Distributional preference learning: Understanding and accounting for hidden context in RLHF." Cited for the result that aggregating over hidden contexts can produce counter-intuitive results.
- Conitzer et al. (2024), ICML — "Position: Social choice should guide AI alignment." The broader program of which this paper is a technical contribution.
- Arrow (1963), *Social Choice and Individual Values* — The foundational impossibility result this paper converts into an engineering tradeoff. May be worth a partial read to understand what assumptions Arrow's theorem requires and which of them are relaxed here.

**Tradition to explore**: The social choice theory literature, specifically the computational social choice subliterature, which asks which social choice properties are computationally tractable to satisfy. This paper converts Arrow's impossibility into a tradeoff by introducing representation as a degree of freedom; computational social choice converts impossibility into computational hardness results. The two research programs are structurally analogous and might be unified.
