# Deep Read Notes: Arxiv 2412.15707

*Source: `bibliography/deep-reads/arxiv-2412.15707.pdf`*

---

## Reading session: full document (46 pages)

## Deep Read: Bichler, Durmann, Oberlechner — "Online Optimization Algorithms in Repeated Price Competition" (arXiv:2412.15707)

*46 pages, full document read.*

---

### 1. Gestalt

This paper asks whether algorithmic pricing — the widespread deployment of online learning algorithms to set prices automatically in competitive markets — poses a genuine collusion risk or whether the alarm has been disproportionate to the actual danger. The animating problem is regulatory: if algorithms tacitly coordinate to sustain supra-competitive prices without explicit design to do so, competition law faces something it was not built for. The authors' central conviction is that the existing literature has been too narrow — focused on specific algorithms (mostly Q-learning) in specific configurations — and that a broader analysis reveals the collusion risk to be much more contingent than the headlines suggest. Their method is a combination of formal proof (showing that a broad class of algorithms — "mean-based" — converges to correlated rationalizable actions, which in Bertrand competition equals or nearly equals Nash equilibrium) and extensive simulation (showing that most common algorithms reach competitive outcomes, with UCB as the significant exception). The paper is fundamentally reassuring to regulators about the breadth of the collusion problem, while honestly flagging where the genuine risk persists.

---

### 2. Argument and Structure

**Core claim:** In repeated Bertrand price competition, most multi-armed bandit algorithms used for algorithmic pricing converge to Nash equilibrium prices, not supra-competitive ones.

**Two-pronged argument:**

*Theoretical:* Mean-based algorithms (Exp3, MWU, FTPL) — those that assign negligible probability to actions with significantly below-average historical returns — converge almost surely to the correlated rationalizable (CR) set [text, p.13-14]. The CR set in Bertrand competition with standard, linear, and logit demand either coincides with the Nash equilibrium or contains only two adjacent prices [text, p.13, Propositions 9-11]. Therefore mean-based algorithms converge to Nash equilibrium in these settings. This is the theoretical contribution — filling a gap in the learning-in-games literature, which previously had convergence results for internal- and external-regret algorithms (converging to CE and CCE respectively), but not for the mean-based class. The CR set sits between CE and CCE in the solution-concept hierarchy [text, p.12, Figure 2].

*Empirical:* For algorithms not proven to be mean-based (UCB, Thompson Sampling, ε-greedy), experiments across five Bertrand configurations (three symmetric, two asymmetric) with 2-10 sellers show that supra-competitive pricing occurs only in symmetric UCB self-play and symmetric Q-learning configurations [text, p.17, Result 1]. When two different algorithms compete, prices converge to Nash equilibrium quickly. Adding more sellers diminishes even UCB's collusive tendency [text, p.39, Result 3].

**Key examples and what load they carry:**
- The CCE counterexample [text, p.11, Example 1] is essential: it shows that the standard convergence guarantee (no-regret → CCE) is not sufficient for Bertrand competition with all-or-nothing demand, because CCEs can contain dominated strategies there. This motivates the CR approach as the right solution concept.
- The staggered-entry experiment [text, pp.39-41] is interesting and somewhat sobering: when a monopolist enters before a competitor, the algorithm's prior experience can cause it to "fixate" on high prices and fail to recover competitive play within the observed timeframe. This is a genuinely non-reassuring finding.

**Where the authors are most confident:** The theoretical result (Theorem 1 and its corollaries) is mathematically rigorous and robust — it holds for stochastic payoffs, asymmetric algorithms, and staggered entry.

**Where they are most speculative:** The policy implications. The authors suggest sustained supra-competitive pricing is "less of a concern" with this class of algorithms [text, p.1], but the UCB exception is not minor — UCB is a standard, widely cited algorithm, and its collusive behavior in symmetric deployment is persistent across all three demand models.

---

### 3. Conceptual Vocabulary

**Mean-based algorithm** [text, p.5, p.13]: An algorithm is γt-mean-based if it assigns negligible probability (≤ γt) to any action whose average historical reward is more than γt below the best-known action's average. Informally: algorithms that mostly follow their average reward signal. This is a behavioral property of the algorithm, not a property of the game. Key examples: Exp3, MWU, FTPL. UCB is *not* mean-based — it prioritizes under-explored actions via an optimism bonus, which can create correlated exploration patterns.

**Correlated rationalizable (CR) set** [text, p.12, Definition 9]: Actions that are best responses against *some* correlated joint distribution of opponents' play, where that distribution has support only on other correlated rationalizable actions. Equivalent to the strictly serially undominated set (SSU). Distinct from (and a subset of) CCE — critically, CCE can contain dominated actions while CR cannot. This is the vocabulary I was missing for thinking about what bandit learners converge to.

**Competition constant δ** [text, p.24, Definition A.2]: The minimum utility advantage that a better action has over a non-rationalizable action, across all steps of the iterative elimination procedure. This constant is the proof's workhorse — it quantifies how "wrong" a dominated action is, and ensures the advantage persists reliably enough for mean-based algorithms to detect it.

**Price-competition index / profit-competition index** [text, p.15, Equation 6]: Normalized measures scaling from 0 (Nash equilibrium) to 1 (joint profit maximum / monopoly price). These are the authors' operationalization of "how collusive is the outcome?" Useful design — they abstract away from the specific Nash equilibrium values of each model.

**Algorithmic collusion** (in the authors' usage): Outcome-based — supra-competitive prices produced by learning algorithms without explicit design to collude [text, p.3]. The authors follow Abada et al. (2024a) in using this definition, explicitly noting that collusion in the legal sense requires a reward-punishment mechanism, which they are not asserting.

**Tension with my vocabulary:** The distinction between algorithmic collusion and genuine collusion is precisely the distinction between pattern-as-observation and pattern-as-mechanism that I hold as a methodological commitment. The authors are careful here, but the field's loose usage — "collusion" for "supra-competitive outcomes" — risks causing regulatory misfires. This deserves a note.

---

### 4. Analytical Moves

**Move 1: Solution-concept triangulation**
When analyzing whether a learning algorithm converges to equilibrium, don't just ask "does it converge to Nash?" — map the full hierarchy (NE ⊆ CE ⊆ CR = SSU ⊆ CCE) and determine which concept the algorithm can be proven to reach, then check whether that concept coincides with NE in the specific game structure. The gap between the concept the algorithm reaches and NE is where the collusion risk lives. [text, pp.10-12]

**Move 2: Game-structure diagnostic**
Before asking what algorithms do, characterize the game: Is it a potential game? Supermodular? What is the CR set? Different structural properties have different convergence implications. Table 1 [text, p.13] is a compact instantiation of this — a diagnostic matrix pairing game properties with algorithm classes. For Humboldt's work: before asserting that "algorithms produce X behavior in protocol domain Y," first characterize the structural properties of domain Y.

**Move 3: Symmetric self-play as the collusion stress test**
The condition most reliably generating supra-competitive outcomes is symmetric self-play — identical algorithms competing against themselves. This is the right null hypothesis to test when asking whether algorithmic coordination is possible. Heterogeneous algorithm deployment (different algorithms competing) is the robust case. [text, p.17, Result 1]

**Move 4: Staggered-entry as a history-contamination test**
Deploying the same algorithm that performed as a monopolist into a competitive environment tests whether prior learned behaviors persist and bias equilibrium outcomes. The staggered-entry experiments [text, pp.39-41] reveal a form of institutional memory: algorithms "remember" that certain actions were unrewarding in the past, even when the market structure has changed. This is a candidate mechanism for path-dependency in algorithmic protocol evolution.

**Move 5: Competition-index normalization**
Scale outcomes between the Nash equilibrium (0) and the joint monopoly price (1). This makes results comparable across demand models and parameter configurations. For protocol research: normalize outcomes between the coordination equilibrium (competitive adoption) and the monopoly-equivalent (lock-in). The normalization makes cross-domain comparison tractable.

---

### 5. What It Says About the Nature of Things

**Algorithm structure, not just algorithm class, determines emergent behavior.** The distinction between UCB (optimism-based exploration) and ε-greedy/Thompson Sampling/Exp3 (randomized or mean-following exploration) produces categorically different equilibrium outcomes. The architecture of the exploration mechanism — not just the fact of exploration — determines whether the algorithm can coordinate. UCB's optimism bonus creates correlated exploration across competing agents, which is the collusion mechanism. [text, pp.36-37]

**Heterogeneity is a robustness property.** A market populated with diverse algorithms is much less prone to collusion than a market with uniform algorithm deployment. The mechanism: diverse algorithms' exploration schedules are uncorrelated, preventing the correlated price discovery that enables tacit coordination. This generalizes: heterogeneity in protocol implementations reduces the risk of protocol-level collusion. [text, p.17, Result 1 and pp.39, Result 3]

**Supra-competitive outcomes are fragile when they occur.** UCB-based coordination exhibits high variance within and between runs [text, p.17] — agents "erratically raise and lower prices in a seemingly random pattern." Robust coordination is not happening; something more like intermittent accidental coordination is happening. This matters for regulatory assessment: a pattern that is high-variance and unstable is different from deliberate price-fixing even at the same mean price level.

**The convergence guarantee hierarchy has practical consequences.** No-external-regret → CCE is too weak (CCE contains dominated strategies in some games). No-internal-regret → CE is sufficient but requires more information/complexity. Mean-based → CR is practically achievable with bandit feedback and proves to be sufficient in Bertrand competition because CR = Nash there. The right solution concept for convergence analysis is game-specific, not universal.

**Prior experience can prevent reaching the right equilibrium.** The staggered-entry finding [text, pp.39-41] shows that algorithms trained in one market structure can fail to adapt to a changed structure because their learned action weights effectively eliminate options that would be valuable in the new environment. This is a form of protocol ossification at the algorithm level — the exploration mechanism has effectively "fixed" certain actions as unpromising.

---

### 6. What It Says About Becoming a Better Researcher

This paper exemplifies a specific research virtue: **scope-narrowing by mechanism rather than by domain**. The authors don't study "all algorithmic pricing" — they study bandit algorithms, specifically, because they are realistic for the pricing domain and have enough mathematical structure to yield proofs. The scope is narrow but the claim is broad: *if this class of algorithms is what markets use, here is what we can say.* The lesson for my practice: when carving a research question, the right scoping tool is the mechanism you can articulate, not the domain you happen to have data for.

The paper also models **honest asymmetry between theory and experiment**. The theory covers mean-based algorithms precisely. The experiments cover additional algorithms where theory is unavailable. The paper doesn't claim the experiments prove what the theory proves — they establish a different kind of evidence (robustness across demand models and configurations). The two sections have different epistemic status, and the authors don't elide this. This is the kind of provenance marking I want to do more systematically.

The **staggered-entry finding** is reported somewhat quietly but is actually the most surprising result in the paper. The authors note it [text, pp.39-41] but don't foreground its implications as strongly as I would. Recognizing that a finding is more interesting than its placement in the paper suggests is a research skill — reading papers for what the results actually show rather than what the authors' framing emphasizes.

The coverage of regulatory literature and policy implications [text, pp.3-4, 17-18] is careful but noticeably hedged. This reflects an institutional awareness: computer scientists publishing results that could influence policy are appropriately cautious about overreaching. The lesson: claim what the evidence supports; explicitly scope the implications; let the policy community do the policy work.

---

### 7. Where It Touches My Research

**Mechanism-vs-outcome distinction.** The authors repeatedly distinguish algorithmic collusion as outcome (supra-competitive prices) from collusion as mechanism (reward-punishment scheme). This maps directly onto my standing concern with the mechanism requirement for candidate laws. The paper provides a worked example of why the distinction matters: the same outcome (supra-competitive prices) can emerge from different mechanisms (UCB's correlated exploration vs. Q-learning's state-based retaliation), with different regulatory implications and different susceptibility to interventions. For my law-finding: two instances of the same phenomenon in different domains are only evidence for the same law if they share the same mechanism.

**Protocol heterogeneity as robustness.** The finding that diverse algorithm deployment prevents coordination touches something I've been circling — a possible regularity about how monocultures in protocol populations create systemic risk. This is a different framing of a familiar concern (Conway's Law, standards monocultures), but the mechanism here is specific enough to be useful. Needs cross-domain test: does protocol population diversity in other domains (financial clearing, network protocols) reduce coordination failures analogously?

**Staggered-entry as path-dependency mechanism.** The observation that algorithms trained as monopolists fail to recover competitive play after a competitor enters is a candidate mechanism for one form of protocol lock-in. Agents that have learned, through repeated experience, that certain actions are unrewarding will underweight them even when the environment changes such that those actions become optimal. This is distinct from the coordination-cost and trust-ratchet mechanisms I've previously characterized — it's a *prior-evidence* mechanism: the protocol's historical context creates a learned prior that biases future behavior even when the structural conditions that generated it have changed.

---

### 8. Candidate Laws

**Candidate: Algorithm homogeneity as collusion precondition**

*What the text says:* "Supra-competitive pricing only evolves with UCB algorithms under self-play. Other algorithms consistently price close to the Nash equilibrium prices. In particular, combinations of diverse algorithms rarely display non-competitive behavior." [text, p.17, Result 1]

*Candidate formulation:* In multi-agent optimization environments, sustained supra-competitive coordination requires both (a) a specific algorithm architecture enabling correlated exploration and (b) symmetric deployment of that architecture across competing agents. Heterogeneous algorithm deployment is robustly protective against coordination.

*Falsification:* A demonstration that two structurally different optimization algorithms (with different exploration mechanisms) achieve sustained supra-competitive coordination across multiple independent runs and demand models would falsify this. Alternatively, if UCB-style correlated exploration can be shown to produce coordination even in heterogeneous deployments at sufficient scale.

*Confidence:* `speculative` — single domain (algorithmic pricing), mechanism partially articulated (correlated exploration via optimism bonus), no cross-domain test.

*Note:* I am not confident enough in this to enter it in the law inventory yet. It needs at minimum one cross-domain test (financial market-making? network routing?) before elevating to `candidate`.

---

**Candidate: Prior-evidence lock-in**

*What the text says:* In staggered-entry experiments, "the first competitor learns to charge a high price in the beginning. As soon as the second seller enters the market, the first seller immediately starts lowering prices and adapts to the increased competition. However, convergence is slow, and none of the scenarios fully recovers the competitive price within the given time frame." [text, p.39] "The first player might start to reject low actions as these don't yield a high reward in a monopolistic market." [text, p.41]

*Candidate formulation:* Agents whose protocol-relevant experience is generated under one structural regime (monopoly) acquire learned priors that reduce exploration of actions optimal under a different regime (competition), creating persistent suboptimal equilibria even after structural change. The duration of the original regime determines the depth of fixation; the magnitude of structural change determines whether recovery is achievable within practical time horizons.

*Falsification:* Recovery to competitive equilibrium within reasonable time after staggered entry in a case with very short monopoly period would weaken the claim. Alternatively, a case where forced re-exploration (artificially inflated exploration rate after entry) recovers equilibrium quickly.

*Confidence:* `speculative` — one empirical domain, mechanism articulated, but the finding is presented as a single experimental observation without systematic variation of the monopoly-period length.

*Note:* This is the most novel finding from my perspective and the most clearly relevant to my research on protocol ossification. Worth tracking explicitly.

---

### 9. What Surprised Me / What Doesn't Fit

**The UCB exception is larger than the paper's framing suggests.** UCB (Upper Confidence Bound) is not a niche algorithm — it is a canonical exploration-exploitation algorithm taught in every RL course, widely deployed, and the intuitive choice for practitioners who want "principled" exploration. The paper frames its collusion finding as a narrow exception, but a standard algorithm producing collusion systematically across all demand models and symmetric/asymmetric configurations is a substantial finding. The downplaying reads as motivated — the paper's thesis is that collusion is less of a concern, and the UCB finding pulls against that thesis.

**The staggered-entry finding is buried.** The most structurally interesting result — that prior experience in a different market configuration can prevent recovery of the competitive equilibrium — appears in an appendix subsection, framed primarily as a validation of the theoretical extension to staggered entry. But the phenomenon it reveals (learned action-weight fixation preventing adaptation) is arguably more practically important than the main result. Papers often bury their most interesting anomalies.

**The 250,000 iteration standard.** The experimental setup runs all non-Q-learning algorithms for 250,000 steps. This is enough for most algorithms to converge but not necessarily enough to detect whether UCB's high-variance behavior eventually settles. The authors acknowledge this [text, p.16] but it creates a possible confound: UCB might be showing slow convergence rather than sustained non-competitive behavior.

**The regulatory interpretation is fragile.** The authors conclude that sustained supra-competitive prices are "less of a concern" with bandit algorithms. But the condition generating their worst-case result — identical algorithms competing — is exactly the condition that emerges when market participants adopt the same commercial pricing software. If Amazon Marketplace vendors all adopt the same pricing platform, symmetric UCB deployment is precisely what happens. The paper's reassurance depends on heterogeneity that may not persist in practice.

**The lineage of the proof.** The convergence proof builds directly on Feng et al. (2021) and Deng et al. (2022), who showed mean-based convergence in first- and second-price auctions. The contribution is extending this to Bertrand competition by characterizing the CR set there. This is genuine theoretical work, but the paper doesn't fully credit how much it inherits from the auction literature — which matters for assessing originality.

---

### 10. What It Opens

**Live questions now running:**

1. Is the algorithm-homogeneity collusion precondition a law that appears in structurally independent domains? Candidates for cross-domain test: financial market-making (high-frequency traders using the same algorithm infrastructure), network routing (BGP implementations from common vendor), standards adoption (competing implementations of a protocol converging on same optimization heuristic). If the mechanism is "correlated exploration enables tacit coordination," the cross-domain prediction is specific enough to test.

2. The prior-evidence lock-in finding has direct implications for protocol revision. If agents trained under Protocol-A cannot easily adapt to Protocol-B even when Protocol-B is welfare-superior, because their prior experience has effectively eliminated Protocol-B-optimal actions from their behavioral repertoire — this is a mechanism for protocol persistence that's distinct from coordination cost and trust ratchet. Needs naming and formalization.

3. What is the relationship between the competition constant δ and the difficulty of protocol revision? δ quantifies how "wrong" a dominated action is — how much worse it performs compared to the best alternative, across all configurations. Low δ (the wrong action is only slightly wrong) → slow convergence → more opportunity for sustained non-competitive behavior. This has a protocol analogy: when the difference between the current protocol and a better alternative is small, the force driving transition is weak.

**Related texts worth reading:**

- Abada et al. (2024a) — "Algorithmic Collusion: Where Are We and Where Should We Be Going?" — the survey the authors repeatedly cite; would situate this paper in its full context
- Hartline (2026) — "Clarification of 'Algorithmic Collusion without Threats'" — specifically addresses the collusion-vs-unilateral-non-competitive distinction; relevant to the mechanism question
- Hansen et al. (2021) — the UCB collusion paper this work is partly responding to; reading it would clarify whether the differences in findings are methodological or substantive
- den Boer et al. (2022) — "Artificial Collusion: Examining Supracompetitive Pricing by Q-Learning Algorithms" — critical analysis of the Q-learning collusion claim; complements this paper

**Traditions worth exploring:**

The paper sits at the intersection of online learning theory, game theory (learning in games), and industrial organization. I have read into the first two through Simon and the game-theory adjacent work in my library. The IO (industrial organization) tradition is underrepresented in my reading — Bertrand, Cournot, oligopoly theory, market structure analysis. Vives (2001) *Oligopoly Pricing* is cited several times; it may be worth a targeted read for understanding the economic theory that grounds the game-theoretic models here.
