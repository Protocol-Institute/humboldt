# Deep Read Notes: Arxiv 2606.05363

*Source: `bibliography/deep-reads/arxiv-2606.05363.pdf`*

---

## Reading session: full document (112 pages)

# Deep Read: Wu & Zeevi, "Should Demand Models Incorporate Competitor Prices?" (arXiv 2606.05363)

---

## 1. Gestalt

This paper asks a precise question with a surprising answer: should a pricing algorithm explicitly model competitors' prices when learning demand? The naive answer is yes — ignoring competitors induces misspecification. The algorithmic collusion literature suggested no — "strategic obliviousness" might facilitate tacit price coordination. Wu and Zeevi resolve this tension definitively: oblivious modeling (deliberately ignoring competitor prices) does not robustly produce collusion, and informed modeling dominates oblivious as a pure strategy. The animating insight is that misspecification has a structural cost — the "spiral-up" phenomenon — that forces oblivious sellers into a persistent linear exploration tax that informed sellers avoid. The paper's method is rigorous: formal market dynamics theorems combined with numerical stress tests, organized around convergence to the competitive Nash equilibrium and a strategy game whose unique equilibrium is the all-informed market. The deep conviction is that apparent collusion from oblivious learning is an artifact of insufficient exploration (a learning failure), not an emergent coordination phenomenon.

---

## 2. Argument and Structure

**Core claims:**

1. **Oblivious sellers must explore more aggressively than monopolists** (Section 4). In monopolistic pricing, √n cumulative exploration is near-optimal. In competitive markets, an oblivious seller is subject to the "spiral-up" phenomenon: competitors' price variance contaminates the seller's misspecified regression through the cross-correlation term r_{n,i←j}. To avoid being "variance-dominated" — which leads to either ceding supracompetitive surplus or falling below Nash — rational oblivious sellers escalate exploration until all sellers maintain linear exploration rates J_{n,i} = Θ(n). This is the maximum sustainable rate before price fluctuations become unbounded. [text, §4.2]

2. **Under sufficient exploration (linear rate), all-oblivious markets converge to Nash** (Theorem 4, Theorem 5). The key condition is that exploration strength C_M dominates the strategic feedback γ̄L^ob_ϕ C_x. Crucially, the formal sufficient condition is violated by ~2500× in numerical experiments, yet convergence still obtains — the condition is conservative. [text, §5.1-5.2]

3. **The "excursion" phenomenon explains apparent collusion** (Section 5.3). The mean-dynamics ODE has a unique locally stable equilibrium at Nash, but its trajectories can exhibit transient excursions — prices temporarily overshooting toward the collusive level before returning. These excursions are sample-path dependent and uncontrollable; their direction depends on whether early price movements are co-aligned or opposed. Observed collusive patterns are therefore finite-time transients, not robust equilibria. [text, §5.3]

4. **Diminishing exploration creates a pseudo-equilibrium continuum** (Section 5.3.2). When exploration decays (as in the canonical √n schedule), persistent excitation fails, the ODE drift becomes ill-defined, and the system can freeze anywhere on a continuum from near-competitive to near-collusive. This explains the puzzling Figure 1 outcomes — not tacit collusion, but incomplete learning. [text, §5.3.2]

5. **Informed sellers dominate oblivious in every market composition** (Theorems 6-7, Proposition 8). Informed sellers converge to Nash without persistent exploration tax, achieving O(√T log T) regret. In mixed markets (ob-in), informed sellers learn the true demand model, oblivious sellers pay the linear exploration tax, and informed strictly out-earns oblivious. The strategy game has a unique strict Nash equilibrium: all-informed. [text, §6-7]

**Load-bearing example:** The "variance dominance" scenario (Table 2, Section 4.2) does most of the conceptual work. When one seller's cumulative price variance dwarfs the other's, the dominated seller falls into a trap: either it settles above Nash (ceding most supracompetitive surplus to the dominant seller) or below Nash (dragging both sellers under the competitive baseline). The dominant seller exploits its variance advantage, not through strategy, but through the structural mechanics of OLS misspecification. This makes variance a "strategic resource" — and the spiral-up logic follows immediately.

**Acknowledged limits:** The model distinguishes only fully oblivious vs. fully informed; intermediate strategies are not studied. The running-mean forecast rule is taken as the canonical choice for informed sellers; richer forecast designs are left for future work. The model uses linear demand, which affords analytical tractability but may not capture all competitive dynamics.

---

## 3. Conceptual Vocabulary

**Oblivious seller** [text, Def. 1]: A seller who models demand as a monopolist — ignoring competitor prices in the regression. Not negligent; this is a deliberate modeling choice studied as a strategy.

**Informed seller** [text, Def. 1]: A seller who correctly specifies demand, including all competitors' prices as covariates.

**Strategic obliviousness** [text, §1.2]: The hypothesis (originating in the collusion literature) that ignoring competitors might facilitate tacit price coordination. Wu & Zeevi refute this as a robust outcome.

**Cumulative exploration / exploration rate** [text, §4]: J_{n,i} = Σ(p_{m,i} - p̄_{n,i})² — the accumulated variance injected into prices. Growth rate (linear vs. sublinear) determines whether the seller maintains persistent excitation for demand identification.

**Omitted-variable channel / r_{n,i←j}** [text, §4.2, App. A.4]: The normalized empirical cross-covariance between seller i's prices and seller j's prices. This term mediates how competitor price variation contaminates the oblivious seller's misspecified regression. When prices are correlated, the omitted competitor price loads onto the own-price slope estimate, inflating perceived market power.

**Spiral-up phenomenon** [text, §4.2]: The strategic escalation logic: each oblivious seller, to avoid being variance-dominated, must match competitors' exploration variance order, driving all to linear rates. A structural inefficiency that would be irrational in monopoly but is rational in competition.

**Pseudo-equilibrium continuum** [text, §5.3.2]: The continuum of possible price limits when exploration decays — from near-competitive to near-collusive. Not a coordination phenomenon but a learning failure: the system freezes wherever early dynamics pointed it.

**Excursion** [text, §5.3.1]: A finite-time trajectory in which mean prices overshoot Nash toward the collusive level (or undershoot below Nash) before returning. Sample-path dependent; direction is uncontrollable. The paper proves: at most one overshoot, then monotone return.

**Surplus-capture ratio S_i** [text, §3.4]: Normalized per-seller revenue: 0 = Nash, 1 = collusive. Allows comparison across markets with different demand primitives. Oblivious sellers earn negative S_i (below Nash) due to exploration tax; informed sellers earn S_i = 0 asymptotically.

**Mean-dynamics ODE** [text, §5.2]: A (2N + N(N-1)/2)-dimensional ODE tracking running means and second moments of prices. The deterministic continuous-time skeleton of the discrete stochastic system. Used to characterize stability (Nash is the unique locally stable equilibrium) and excursion structure.

**Stackelberg revenue** [text, §7, App. A.10]: The revenue an informed seller could earn with clairvoyant prediction of the oblivious competitor's next price (including exploration noise). Not implementable in practice; serves as an information upper bracket on informed-side earnings against an oblivious competitor.

**Jensen tax** [text, App. A.10]: The per-period revenue penalty paid by an informed seller who uses the lag-1 forecast rule (ˆp_{n+1,j} = p_{n,j}) instead of the running mean. Because the best-response map is linear but revenue is concave-quadratic, forecasting noisy realized prices instead of de-noised averages incurs a Jensen penalty proportional to the competitor's persistent exploration variance.

*Tension with my vocabulary:* "Oblivious learning" in my existing framework has sometimes meant "learning without awareness of a mechanism" — here it means something precise: deliberate omission of competitor covariates from the demand model. The paper's use is narrower and more operational.

---

## 4. Analytical Moves

**Move 1 — The variance dominance trap argument.** When J_{n,i}/J_{n,j} → 0, r_{n,j←i} → 0 (Lemma 2), so the dominant seller j becomes asymptotically correctly specified with respect to i, while i remains misspecified. Combined with revenue geometry (Proposition 3), this shows the dominated seller is worse off regardless of whether its price settles above or below Nash. *Transferable:* whenever one agent's information environment degrades relative to another's through a structural feedback loop, identify the "dominance trap" — the structural position that makes being the dominated party a pure loss.

**Move 2 — The mean-dynamics ODE skeleton.** Derive the ODE governing the continuous-time flow of running moments (means, variances, covariances) from a discrete stochastic system via stochastic approximation. Use the ODE's fixed-point and stability analysis to characterize what the stochastic system converges to, and the ODE's transient dynamics to characterize finite-time behavior. *Transferable:* when discrete stochastic dynamics are hard to analyze directly, fluid-limit the moment evolution and study the resulting ODE. The excursion structure analysis (single overshoot, monotone return) is only accessible this way.

**Move 3 — Strategy game lift.** Once three market compositions (ob-ob, in-in, ob-in) have been characterized by their convergence theorems, lift to a 2×2 strategy game on {oblivious, informed} and read off the dominant strategy and Nash equilibrium. The convergence theorems do the real work; the game-theoretic framing makes the strategic implication crisp. *Transferable:* when a coordination space has been fully characterized, reframe it as a game to extract strategic implications that were implicit in the analysis.

**Move 4 — Forecast-rule ablation.** To test robustness of the "informed dominates" conclusion, ablate four forecast rules (running mean, lag-1, greedy component, perfect prediction) and show that three collapse to Nash (with running mean and greedy component tying, lag-1 paying a Jensen tax), while only the implementable-in-practice fourth (perfect prediction) achieves Stackelberg. This brackets the informed-seller's achievable revenue between Nash and Stackelberg. *Transferable:* when proving a dominance result, map out the full space of implementable strategies for the dominant type to bound what the dominance is actually worth.

**Move 5 — Conservative sufficient condition acknowledged.** Theorem 4's sufficient condition (C_M > γ̄L^ob_ϕ C_x) is violated by ~2500× in all numerical experiments, yet convergence obtains universally. The paper explicitly acknowledges the gap and uses the mean-dynamics ODE (Theorem 5, local stability) to explain why convergence is observed beyond the formal sufficient regime. *Transferable:* when a formal sufficient condition is far from tight, don't hide it — use it as evidence that the true mechanism is more subtle, and provide a complementary analysis (here, local stability via ODE linearization) that covers the empirically relevant regime.

---

## 5. What It Says About the Nature of Things

**Misspecification has structural costs beyond efficiency loss.** The oblivious seller's problem is not just that it learns more slowly (suboptimal regret). The misspecification creates a *strategic externality*: each oblivious seller's exploration behavior affects other sellers' regression contamination, which drives all sellers to explore more than any one would want to individually. The outcome (persistent linear exploration tax) is a collective bad that no individual seller can escape through unilateral action. This is a prisoners'-dilemma structure at the level of model design, not just pricing behavior. [inference]

**Apparent coordination can be a learning artifact.** The paper's strongest claim: the collusive-looking price trajectories documented in the algorithmic collusion literature are not emergent coordination — they are incomplete learning under insufficient exploration. The continuum of pseudo-equilibria (Section 5.3.2) is the competitive analog of Keskin and Zeevi's "incomplete learning" in the monopolistic case. The system freezes wherever early stochastic dynamics pointed it. This means that regulatory concerns about "algorithmic collusion" through oblivious modeling are misframed: the phenomenon is better described as failed market learning. [text, §5.3.2]

**Exploration is not free but is controllable.** The linear exploration tax is structurally unavoidable for oblivious sellers, but its magnitude is the seller's choice (through ν²). Proposition 11 quantifies the exact per-period revenue cost (|β_i|ν²) and Lemma 16 sharpens this to an exact asymptotic. This is a model of irreducible but calibratable structural cost — unlike the unpredictable losses from learning failure. [text, Prop. 11, Lemma 16]

**Information about the environment is strictly valuable in competitive settings.** The all-informed equilibrium is not just more efficient in aggregate — it is individually dominant. No seller benefits from strategic obliviousness even in expectation of collusive gains. The information advantage of correct specification converts the competitive dynamics into an identification opportunity (treating competitor price movements as informative covariates rather than noise), while misspecification converts the same dynamics into a contamination problem. [inference from §6-7]

**The structure of information asymmetries is self-perpetuating.** Variance dominance (one seller maintaining higher exploration than another) creates a persistent information asymmetry: the dominant seller eventually learns a correctly-specified model while the dominated seller remains misspecified. This is not an equilibrium that can be escaped unilaterally — it's a structural lock-in created by early exploration differences. The feedback runs: more exploration → better specification → higher revenues → more resources for further exploration. [inference from §4.2]

---

## 6. What It Says About Becoming a Better Researcher

The paper itself is not methodological, but several moves are exemplary.

**Commit to a definitive answer to a contested question.** The paper enters a live controversy (does oblivious modeling cause collusion?) with a clear position and defends it rigorously. The abstract states the conclusion directly: "oblivious demand modeling does not robustly sustain collusive pricing." This is courage in a field where hedged claims are common. *M-016 relevance:* choose research problems where you can actually establish something, not just illuminate.

**Acknowledge when your formal conditions are not tight.** The repeated acknowledgment that Theorem 4's sufficient condition is violated by ~2500× in all experiments (Tables 6, Figure 2 caption) is a mark of intellectual honesty. The response is not to hide the gap but to provide a complementary analysis (ODE local stability) that covers the empirically relevant regime. A weaker researcher would either have pretended the condition was tight or not tested it.

**Use numerical experiments to stress-test, not to confirm.** The numerical experiments are consistently designed to violate the formal sufficient conditions — not to illustrate them. This is the right epistemic use of computation: find where your theory's formal boundaries are and show that the phenomenon holds beyond them.

**Separate what the benchmark measures from what you want to measure.** Appendix A.3 is a masterclass in benchmark critique. The dynamic regret benchmark (optimal against realized competitor profile) is standard in the literature, but the paper shows it is *equivalent* to minimizing distance from Nash — making it definitionally hostile to studying collusion. The paper uses this not as a criticism to avoid the benchmark but to understand why a separate metric (surplus-capture ratio) is needed. *M-016 relevance:* when a standard metric is misaligned with the phenomenon of interest, don't ignore the misalignment — make it explicit and introduce a better metric.

---

## 7. Where It Touches My Research

**Protocol ossification and exploration cost.** The "spiral-up" phenomenon is a mechanism I haven't seen before: agents in a competitive protocolized environment are forced into more exploration (higher variance, higher cost) than they would choose individually, as a consequence of structural misspecification in their models of others' behavior. This is a candidate mechanism for *why* protocol participants over-adapt or over-signal in early coordination phases — not because it's efficient but because being variance-dominated is a structural trap. [inference]

**The pseudo-equilibrium continuum as a law candidate.** The finding that decaying exploration produces a continuum of pseudo-equilibria (from near-competitive to near-collusive) has a generalization I want to pursue: *insufficient excitation in a competitive protocolized system leaves it frozen at whatever state early dynamics produced, rather than converging to a well-defined equilibrium*. This is an analog of Keskin-Zeevi's "incomplete learning" result at the protocol level. The mechanism (persistent excitation required for identification of true parameters) might generalize to other protocol adoption dynamics where agents have misspecified models of others' behavior. [inference; this is speculative but structural]

**Information asymmetries in protocol adoption.** The "variance dominance trap" — where one agent with more exploration becomes correctly specified while the dominated agent remains misspecified — maps onto scenarios in protocol adoption where early movers (with more exploration of alternatives) develop better models of the coordination game, while late movers who enter with less variance in their behavior are structurally disadvantaged. The mechanism is specifically about the contamination of misspecified regression by the dominant agent's variance. [inference]

**The Jensen tax as a general phenomenon.** The lag-1 forecast rule's Jensen tax (equation 24) is a clean example of a structural cost created by using a noisy signal when a de-noised average is available. This is a general lesson about protocol design: if you're building a response function that maps noisy observations to actions, and if revenue (or utility) is concave in your response, then forecasting from noise rather than from cleaned signals incurs a structural tax proportional to signal variance. [inference]

---

## 8. Candidate Laws

**CL-Spiral**: *In a competitive market where agents use misspecified models (omitting others' behavior), variance acts as a strategic resource. Agents are forced to maintain higher exploration (higher cost) than they would prefer individually, as a structural defense against being "dominated" by competitors with higher price variance.*

- [text, §4.2, Lemma 2, Proposition 3]
- Candidate formulation: In any protocolized competitive system where agents use locally misspecified models of others' behavior, the strategic dynamics force each agent to maintain variance in its behavior above any single agent's individually optimal level, generating a persistent collective inefficiency.
- Falsification: A competitive market with misspecified agents where one agent achieves stable dominance through low variance (i.e., the "trap" doesn't materialize) would falsify this. Or: a market where the dominated seller can profitably exit the trap through a non-variance strategy.
- Status: `speculative` — observed in one formal domain (linear demand pricing with OLS), mechanism is clear, but needs cross-domain evidence.

**CL-Incomplete-Protocol-Learning**: *A protocolized system with decaying excitation does not converge to a well-defined equilibrium; instead it freezes at a pseudo-equilibrium determined by early stochastic dynamics.*

- [text, §5.3.2]
- Candidate formulation: When agents in a protocolized coordination system reduce their exploratory behavior over time (exploration decays), the system fails to identify the true equilibrium and instead freezes at a state path-dependent on early history.
- Falsification: A system with decaying exploration that nonetheless converges to a unique equilibrium through a mechanism other than persistent excitation (e.g., structural constraints, exogenous anchor).
- Status: `speculative` — strong in the formal model, but needs cross-domain evidence to become candidate.

---

## 9. What Surprised Me / What Doesn't Fit

**The 2500× gap is the most interesting finding the paper half-ignores.** The formal sufficient condition for Theorem 4 is violated by ~2500× in every numerical experiment, yet convergence is universal. The mean-dynamics ODE (Theorem 5) provides local stability but doesn't explain why the global basin of attraction is so much larger than the formal theory predicts. This gap is enormous — it suggests the theorem's sufficient condition is capturing something structurally irrelevant, while the real mechanism is quite different. The paper moves past this relatively quickly. What *is* the true mechanism? [text, §5.1-5.2, Table 6]

**The excursion direction is the most important unresolved question.** Proposition 12 proves that upward excursions are possible; Appendix A.8 proves that downward excursions are also possible, with direction determined by whether early price movements are co-aligned. This means that observed "collusive" trajectories in the algorithmic collusion literature may be artifacts of seed-dependent early co-movement, not anything about the algorithm's strategic sophistication. The regulatory literature is chasing a phenomenon that may be entirely stochastic in nature. This is a stronger claim than the paper explicitly makes. [text, §5.3.1, App. A.8]

**The Stackelberg boundary is an interesting anomaly.** The "perfect prediction" informed seller (with clairvoyant access to the competitor's exploration noise) achieves Stackelberg revenues, not Nash. This means there's a regime where being *more* informed — in a way that's currently not implementable — would enable sustained supracompetitive revenues for the informed seller. The paper brackets this as an "upper bound" and moves on, but it's structurally interesting: the Nash equilibrium is not the unique stable outcome for all possible information environments, only for the subset where real-time competitor exploration noise is unobservable. [text, §7, App. A.10]

**The running-mean forecast as canonical is contested.** The paper argues for running-mean forecast as the "canonical choice for classical adaptive-best-response results" (§6, opener). But the ablation shows that lag-1 and greedy-component rules also converge to Nash (with a small Jensen tax for lag-1). The choice of forecast rule is not innocuous — the Jensen tax in lag-1 (equation 24) is proportional to the competitor's persistent exploration variance, which is determined endogenously by the spiral-up logic. The paper treats forecast-rule choice as secondary, but in a market with high exploration variance (due to the spiral-up), the Jensen tax could be material. [text, App. A.10]

---

## 10. What It Opens

**Specific questions now running:**

1. *Is the spiral-up phenomenon observable in non-pricing competitive protocols?* The formal structure requires: (a) agents use misspecified models that omit others' behavior, (b) the omitted term correlates with own behavior through interaction dynamics, (c) being "variance-dominated" has a structural revenue cost. This structure appears potentially in network protocol competition (TCP variant competition for bandwidth), academic citation dynamics (papers that don't cite competitors may be misspecifying their innovation claims), and standard-setting bodies where participants model the market without adequately modeling other participants' positions. These would need investigation.

2. *What is the correct mechanism for the 2500× gap between formal sufficient conditions and empirical convergence?* This seems like a genuine open mathematical question. The ODE local stability result (Theorem 5) covers it phenomenologically but not mechanistically.

3. *Does the pseudo-equilibrium continuum phenomenon appear in protocol adoption?* The Keskin-Zeevi "incomplete learning" framing suggests: protocols adopted under rapidly decaying experimentation will freeze at path-dependent pseudo-equilibria. This would predict that protocols adopted quickly (low exploration period) should show more variance in their long-run equilibrium behavior than protocols that went through extended competitive exploration.

**Texts worth reading:**
- Keskin & Zeevi (2018), "On Incomplete Learning and Certainty-Equivalence Control" — the monopolistic analog that Wu & Zeevi repeatedly cite as their benchmark. This is the origin of the "incomplete learning" framing.
- Esponda & Pouzo (2016), "Berk-Nash Equilibrium" — the game-theoretic extension of pseudo-true parameter convergence that Wu & Zeevi cite. The Berk-Nash concept (Nash equilibrium under misspecified beliefs) might be a powerful frame for protocol adoption under misspecified models of others' behavior.
- Cooper et al. (2015), "Learning and Pricing with Models That Do Not Explicitly Incorporate Competition" — the founding paper for oblivious learning, which Wu & Zeevi repeatedly extend. Reading the original would clarify what exactly they're adding.
- Milgrom & Roberts (1990, 1991) on adaptive learning in games — the classical convergence results that Wu & Zeevi's results extend to the unknown-demand case.

**Traditions worth exploring:**
- The "mean-field game" literature — which studies competitive dynamics when each agent treats others' strategies as fixed distributions (effectively, a form of misspecification). The spiral-up phenomenon might be a finite-N analog of mean-field instability.
- Behavioral game theory and "level-k thinking" — agents who model others at a finite depth. Oblivious learning is effectively level-0: no modeling of others at all. The question is whether higher-level misspecification (partial modeling) also generates structural exploration costs.
