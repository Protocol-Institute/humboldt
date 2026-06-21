# Deep Read Notes: Arxiv 2606.01874

*Source: `bibliography/deep-reads/arxiv-2606.01874.pdf`*

---

## Reading session: full document (37 pages)

# Deep Read: Öz et al., "The Price of Decentralization in Block Building" (arXiv:2606.01874)

---

## 1. Gestalt

This paper asks a sharp, specific question that turns out to have structural depth: when you replace a single transaction-including monopolist with multiple self-interested builders, do you actually get better coverage of the network's transaction space? The authors' answer is: *not necessarily, and the mechanism of failure is precise*. Builders, acting selfishly, will over-concentrate near high-value transaction sources, leaving peripheral sources under-covered — not because anyone is malicious, but because the private marginal return to joining an already-covered region exceeds the social marginal return. The "price of decentralization" is the formal quantification of this gap: at worst, decentralized equilibrium achieves only half the welfare a coordinated planner could. The paper's animating conviction is that *decentralization is a design variable, not a binary property* — having multiple builders is necessary but not sufficient for the censorship-resistance and fair-access properties that motivate multiple-builder designs in the first place.

---

## 2. Argument and Structure

**Core architecture:** The authors model the problem as a *stochastic coverage game*. Builders choose geographic regions; transaction sources emit value-laden transactions over a block-construction round; latency determines whether each builder receives each transaction before the deadline. The equal-split sharing rule divides transaction value equally among all builders who include it.

**Three main theoretical results:**

1. *Pure Nash equilibrium exists* [text, pp. 7–8]. The harmonic-number potential function Φ(s) = E[Σ V_j H_{n_j(s)}] is an exact potential — unilateral deviations shift the potential exactly as they shift the deviating builder's utility. This is a clean structural result: the game has a stable configuration. Better-response dynamics converge.

2. *Factor-2 Price of Anarchy bound, tight* [text, pp. 8–10]. The smoothness framework shows the game is (1,1)-smooth, which together with the accounting identity (aggregate builder utility = welfare) gives PoA ≤ 2. The tightness construction (K builders all crowding a single dominant source, each deviating to a secondary source would reduce private payoff despite improving social welfare) is instructive: the worst case is not pathological but structurally natural.

3. *Utility concentration bounded near egalitarian* [text, pp. 10–11]. The lowest-utility builder earns ≥ 1/2 the highest-utility builder's payoff at any pure Nash equilibrium. The HHI bound (≤ 9/8 × egalitarian baseline) follows. This is perhaps the most surprising result: even though equilibrium placement may be geographically concentrated, the *rewards* are fairly balanced.

**The simulation results do the most interesting work:** They reveal that the PoA bound's bite depends on a *regime* defined by the interaction of two parameters — source-value asymmetry and slot duration [text, pp. 13–18]. The worst welfare losses arise in the *intermediate* slot-duration regime, where peripheral sources are reachable (long enough deadline) but individual incentives still favor high-value source regions (strong enough value asymmetry). Both extremes are relatively efficient: short slots (coverage is local regardless), long slots (coverage saturates).

**The counter-intuitive finding about geographic vs. utility concentration** [text, pp. 18–19]: planner allocations may be more *geographically* dispersed but more *utility-unequal* (because peripheral-region builders earn less). Equilibrium is more geographically *concentrated* but more utility-*balanced*. These objectives point in opposite directions, which is a genuine design insight, not just an artifact.

**Limits the authors acknowledge:** No block-capacity constraints (which might strengthen the welfare loss channel by crowding out otherwise-covered transactions); no endogenous transaction routing (users don't choose which builders to send to); no Sybils, entry/exit dynamics, or collusion; simulations use stylized source values rather than empirical order-flow data.

---

## 3. Conceptual Vocabulary

**Price of Anarchy (PoA)** [text, p. 8]: Ratio of optimal (planner) welfare to worst-case equilibrium welfare. Used here as "price of decentralization" — the welfare cost of uncoordinated self-interest. Standard algorithmic game theory term; carries the same meaning I would use.

**Exact potential game** [text, p. 7]: A game in which a single real-valued function (the potential) captures the *exact* change in any player's utility from a unilateral deviation. Stronger than ordinal potential (where only the sign must agree). Implies pure Nash equilibrium existence and finite better-response convergence. Key import: it lets the welfare analysis proceed through a known toolkit.

**Valid utility game / smoothness** [text, pp. 8–9]: A class of games where agent utilities are tied to a monotone submodular social objective. The smoothness framework [Roughgarden 2015] provides PoA bounds through a single inequality relating deviation payoffs to welfare gaps. The authors verify this structure holds in their stochastic setting.

**Coverage probability** f_I(t; s) [text, p. 9]: Probability that a transaction from source I emitted at time t is received by at least one builder. The key welfare quantity — welfare is just the integral of this over all sources and emission times.

**HHI (Herfindahl–Hirschman Index)** [text, p. 10]: Standard concentration metric from industrial economics. Here applied to builder *utility shares* (not market shares). The 1/K egalitarian baseline is what you get if all builders earn equally; 9/8K is the worst-case equilibrium bound.

**Geographic HHI vs. Utility HHI** [text, pp. 12, 18–19]: Two *different* HHI measures tracking different phenomena. Geographic HHI measures co-location of builders in regions. Utility HHI measures inequality of expected payoffs. These diverge — planner solutions can be geographically dispersed but utility-concentrated; equilibrium solutions can be geographically concentrated but utility-balanced. I want to hold this distinction carefully.

**Peripheral sources / high-value sources** [text, pp. 11, 13]: The paper's partition of transaction sources by geographic location and value. "Peripheral" means geographically remote from financial/tech centers and lower value. The welfare loss story turns entirely on whether peripheral sources remain under-covered.

---

## 4. Analytical Moves

**The intermediate-regime diagnosis:** When studying a system with two competing parameters (here: latency sensitivity and value asymmetry), look for the regime where *both* parameters create pressure. Extreme values of either parameter often collapse the tension (coverage saturates, or coverage is purely local). The welfare loss lives in the middle. This is a general move: find the regime where two forces are simultaneously active and study the interaction.

**The geographic-utility decoupling:** When studying concentration in a distributed system, decompose the "concentration" question into *geographic* concentration (where are the agents?) and *utility/payoff* concentration (how unequal are the outcomes?). These can move in opposite directions. A design that appears "decentralized" by one metric may appear highly concentrated by the other.

**The tightness construction:** To show a worst-case bound is tight, construct an instance where rational agents face a situation in which covering an already-covered dominant source is individually rational while covering a secondary source would be individually irrational. The "K builders all at one dominant source" construction is a template for showing PoA = 2 is achievable.

**Aggregate utility = welfare identity:** Under equal-split, the total rewards distributed exactly equals the value of covered transactions (Lemma 5). This is a clean accounting identity that enables the smoothness proof. Look for analogous identities in other covering/sharing settings — they often unlock efficiency analysis.

**The planner-vs-equilibrium differential:** Don't just compare welfare; decompose the welfare gap by *which* sources are differentially covered. Here: high-value cluster coverage is nearly equal (both planner and equilibrium saturate it); the entire welfare gap lives in peripheral source coverage. This cluster-coverage decomposition makes the mechanism legible.

---

## 5. What It Says About the Nature of Things

**Structural under-provision of marginal coverage.** Any system with submodular social benefit and additive private sharing will exhibit systematic under-provision of marginal coverage. The first builder to cover a source captures the full social value but shares it with later duplicators; later duplicators reduce each other's per-builder payoff without reducing the social value already captured. This is the general mechanism behind the PoA = 2 result. It applies far beyond block building — anywhere multiple agents can redundantly cover a common-pool resource.

**The count-versus-distribution failure mode.** Adding more builders doesn't fix coverage if incentives keep them clustered. The builders-as-decentralization narrative commits a category error: it treats count as a proxy for distribution. The paper shows these come apart systematically. This is a specific instance of a more general observation: increasing the number of agents in a protocol does not by itself produce the structural benefits attributed to "decentralization."

**Regime-dependence of governance failure.** The paper shows that the same institutional arrangement (decentralized builder placement, equal sharing) performs efficiently in some regimes and poorly in others. The governance failure isn't categorical — it's regime-conditional. This should make us suspicious of blanket claims about whether a protocol "is" or "isn't" decentralized.

**The tradeoff between geographic and utility equality.** These are distinct dimensions of fairness in distributed systems, and optimizing one can require sacrificing the other. Planner allocations that maximize welfare may be more utility-unequal than equilibrium allocations. This suggests that "fair" is genuinely multi-dimensional in protocol design, not a single criterion.

---

## 6. What It Says About Becoming a Better Researcher

This is primarily a technical paper, but there are craft lessons embedded in the structure.

**Don't accept the problem as posed.** The paper's contribution isn't just analyzing a game — it's *reframing* the decentralization question. The community debate is about "how many builders." The paper's move is to say: that's the wrong variable. *Where* builders locate is the operative question. This reframing is the creative act; the analysis follows from it. [Connects to M-016: recognizing when the received framing of a problem is obscuring the productive question.]

**Use the parameter sweep to find the regime.** Rather than analyzing a single scenario, the paper systematically varies slot duration, value asymmetry, and builder count. The most interesting findings (non-monotonicity, geographic-utility decoupling) only appear when looking across the full parameter space. A single case study would have missed them. [Connects to M-016: the value of exploring the full parameter space rather than working in a single representative case.]

**State the mechanism before the policy implication.** The paper's Section 6 is scrupulously careful to trace policy implications back to identified mechanisms (slot duration relative to propagation latency; value asymmetry; peripheral-source reachability). This makes the implications robust — they're contingent on clearly-stated mechanisms, not asserted directly from empirical patterns. [Connects to METHOD.md: mechanism requirement for law claims.]

---

## 7. Where It Touches My Research

**The count-versus-distribution failure mode is a potential law candidate.** The observation that increasing the count of participants in a decentralized protocol does not, by itself, produce the structural benefits of decentralization — because incentives may keep participants clustered — may generalize well beyond block building. This pattern might hold anywhere:
- Self-interested agents can choose their domain of coverage
- Social benefit is submodular (marginal benefit of redundant coverage is low)
- Private incentives favor high-value clusters over peripheral ones

[inference] This might be a mechanism contributing to what I've been tracking as coverage failures in multi-party protocols generally. Needs cross-domain validation.

**The geographic-utility decoupling is a useful diagnostic tool.** In any protocol where agents are distributed and rewards are shared, "concentration" is underspecified unless decomposed. [inference] This might reveal something about why seemingly "distributed" protocols exhibit governance centralization: the relevant concentration dimension is payoff or decision power, not geography.

**The intermediate-regime fragility observation.** Protocol governance failures may be most visible not at extremes but in intermediate regimes — where the capacity for distributed behavior exists but incentives still favor concentration. [inference] This could be a scope condition for protocol coverage laws: "applies when the marginal benefit of peripheral coverage is positive but smaller than the marginal private return to the dominant cluster."

---

## 8. Candidate Laws

**CL-X: Decentralization Count-Coverage Independence**

*What the text says:* "Replacing a single proposer with multiple builders is not sufficient, by itself, for broad transaction coverage" [text, p. 19]. "Adding builders increases the system's potential coverage capacity, but when source values are asymmetric, additional builders may still prefer regions with strong access to high-value sources" [text, p. 17].

*Candidate formulation:* In any coverage system where (a) agents choose their coverage domain, (b) social benefit is submodular in coverage, and (c) private payoffs are determined by sharing among agents covering the same value sources, the number of participating agents does not monotonically increase the geographic or domain diversity of coverage at equilibrium. Additional agents may duplicate coverage of high-value domains while peripheral domains remain under-served.

*Domains:* block building (explicit), financial market-making (multiple liquidity providers may cluster on liquid instruments, leaving illiquid instruments under-served), content delivery networks (CDN nodes may concentrate in high-traffic markets), sensor network deployment (sensors may cluster near data-rich environments)

*Falsification:* An instance where increasing builder/agent count causes peripheral-source coverage to increase monotonically, under conditions of significant value asymmetry, would constitute evidence against this candidate law.

*Confidence:* speculative — one domain, mechanism partially stated

---

**CL-Y: Geographic-Utility Concentration Decoupling**

*What the text says:* "Geographic decentralization and builder-utility equality need not coincide: improving source coverage and total welfare may require distributing builders into lower-payoff regions, while selfish behavior can achieve a more utility-balanced but geographically more centralized outcome in equilibrium" [text, p. 18].

*Candidate formulation:* In distributed systems with shared-value protocols, geographic concentration and payoff concentration are distinct dimensions that can move in opposite directions. Welfare-maximizing designs may require placing agents in lower-payoff positions, producing geographic dispersion at the cost of payoff equality; self-interested equilibria may achieve payoff equality through geographic concentration.

*Domains:* block building (explicit), judicial/regulatory system staffing (rural jurisdictions are geographic dispersal but lower-prestige), academic institution geography (research clusters in high-value centers; dispersed institutions face resource disadvantages)

*Falsification:* A case where decentralized equilibrium produces both geographic dispersal and utility equality simultaneously, without coordination, would complicate this claim.

*Confidence:* speculative — needs cross-domain investigation

---

## 9. What Surprised Me / What Doesn't Fit

**The non-monotone welfare ratio in builder count** [text, pp. 17–18] is genuinely surprising. More builders initially *helps* (welfare ratio rises), then *hurts* (welfare ratio falls) — because additional builders pile onto already-saturated high-value coverage. The welfare loss comes not from having too few builders but from having the wrong distribution. I hadn't expected non-monotonicity; I expected monotone improvement with diminishing returns.

**The utility-concentration result cuts against my intuitions.** I would have predicted that equilibrium concentration of builders in high-value regions would produce both geographic AND utility concentration (the rich get richer). The paper shows the opposite: equal sharing *balances* utilities even when geography is concentrated, because all K builders in the same region split the same pool. The HHI bound of 9/8K is quite tight — almost egalitarian. The inequality lives in coverage outcomes, not builder payoffs. This is unexpected and important.

**The model's strongest assumption is also the most consequential.** The paper treats transaction sources as exogenous — they emit value and builders receive it or not. But in reality, valuable order flow is actively routed by users/applications who may preferentially send to builders they trust to include their transactions. This endogeneity could *strengthen* the concentration effect (high-value senders co-locate with high-value builders), or it could create counter-pressures (competition for order flow gives peripheral builders a value proposition). The authors flag this as future work, but it's not a minor extension — it could change the direction of some results.

**The factor-2 PoA is described as "the price of decentralization"** but it's really an upper bound on the price, not the price itself. The simulations show that in most regimes, the actual welfare ratio is well above 0.5 (often above 0.9). The theoretical bound frames the result as a worst-case guarantee, but the real policy question is about typical cases, not worst cases. The paper is honest about this [text, p. 21], but the framing in the title and abstract leans harder on the bound than the simulation results warrant.

---

## 10. What It Opens

**Immediate cross-domain test for CL-X:** Does the count-coverage failure mode appear in:
- *Financial market-making:* Do additional market makers in an exchange cluster on high-volume instruments, leaving low-liquidity instruments under-served? Literature on dealer-of-last-resort and thin markets may bear on this.
- *CDN deployment:* Is there evidence that CDN nodes concentrate in high-traffic markets even when peripheral coverage would improve aggregate welfare?
- *Healthcare provider distribution:* Medical providers cluster in high-income urban areas despite demonstrated social welfare gains from rural coverage — is the mechanism the same? (This would be cross-domain in a structurally interesting way.)

**The peripheral-source coverage gap as a general phenomenon:** The finding that welfare losses come specifically from under-coverage of peripheral sources, not from overall coverage failures, suggests a general principle: in any system with heterogeneous value sources and self-interested coverage agents, the *margin* of the value distribution (peripheral, low-value, remote) will be systematically under-served at equilibrium. This might be formalizable as a scope condition for coverage laws.

**Endogenous routing as a separate paper:** The authors flag this as future work [text, p. 20]. From my perspective, the question is whether endogenous routing strengthens or weakens the concentration effect. If high-value users preferentially route to well-located builders, the concentration pressure intensifies (Matthew effect). If users have censorship-resistance preferences and actively diversify routing, concentration might be self-limiting. This is a real open question.

**The Roughgarden smoothness framework** [Roughgarden 2015, cited as [27]]: The paper depends heavily on this. The framework seems to be a general tool for bounding welfare loss from selfish behavior in a wide class of games. Worth reading — it might provide a formal apparatus for other law candidates where I'm currently working from informal mechanism arguments.

**Related paper: Elsheimy et al. on censorship resistance vs. throughput in multi-proposer BFT** [cited as [7] in the paper]: The finding that stronger censorship resistance requires more transaction duplication (and hence lower throughput) is a direct complement to this paper's results. The two papers together suggest a multi-dimensional tradeoff space: coverage, throughput, geographic decentralization, and utility equality are four distinct objectives that cannot all be simultaneously optimized.
