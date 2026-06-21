# Deep Read Notes: Arxiv 2605.18185

*Source: `bibliography/deep-reads/arxiv-2605.18185.pdf`*

---

## Reading session: full document (32 pages)

# Deep Read: Russell, Leung & Turrini — *The Dynamics of Policy Gradient in Social Dilemmas with Partner Selection* (arXiv:2605.18185)

---

## 1. Gestalt

This paper is a translation project: it takes a body of empirical findings about partner selection and cooperation — built up through decades of agent-based simulation — and reconstructs them analytically. The animating question is not "does partner selection promote cooperation?" (that's already known) but "why does it, formally, and what structural conditions are strictly necessary?" The method is mean-field theory applied to policy gradient dynamics: derive the exact equations governing how a population of reinforcement learners evolves when they can choose who they interact with. The central conviction is that the mechanism by which partner selection works is *opponent distribution reshaping* — the partner rule changes whom you face, which changes your reward landscape, which changes your learning trajectory. The paper proves that population variance is a necessary condition for cooperation to emerge under the two cooperation-promoting rules (OFT and ROFT), and that the stationary distribution under stochastic dynamics concentrates mass at the boundary — a mixture of pure cooperators and pure defectors, not a mixed-strategy equilibrium. This is mature theoretical work on a well-studied empirical question, building from first principles rather than generalizing from simulation.

---

## 2. Argument and Structure

**Core architecture:** The paper has two phases — mean dynamics (deterministic, Section 3) and stochastic dynamics (Section 4) — with a shared foundation in the conditional opponent distribution framework.

**The foundational move** [text, p.4]: For any partner selection rule, the distribution of opponents you face at round *h* depends on the rule applied to round *h-1*. This gives a Markovian recursion for ρ_h(y|x). The partner rule determines how this distribution evolves. Under OFT (stay iff both cooperate), cooperators accumulate better opponents over time; under ROFT (stay iff both defect), defectors accumulate worse opponents over time — but the mathematics is symmetric. Under Stay and Switch, the opponent distribution doesn't change.

**The variance result** [text, p.6]: The key quantity is ∆G[ρ] = bVar(ρ(y)) − 2c. This is the sign of the reward difference between cooperating and defecting under OFT with episode length H=2. For cooperation to be promoted, you need bVar(ρ) > 2c. Population variance is not just helpful — it is a *necessary condition*. Without variance, there is no differential signal between who you might pair with after cooperating vs. after defecting.

**The OFT/ROFT symmetry** [text, p.5, Table 2]: The first two-round reward differences are identical for OFT and ROFT. Keeping cooperative pairs together and keeping defective pairs together produce the same expected reward differential. This surprises the authors enough that they remark on it explicitly [inference]. The proof (Lemma B.5) works by transforming ROFT into OFT under the change of variables Z = 1-Y.

**What Stay and Switch do** [text, p.6, Theorem 3.1]: Both converge to pure defection. Under these rules, the opponent distribution doesn't reshuffled — the reward is always −Hc, and the population inevitably collapses.

**The stochastic extension** [text, p.7-8, Section 4]: The REINFORCE update is noisy. The authors model this as a 2D Wiener process and apply Itô's lemma to derive the Fokker-Planck equation (FPE) for the population density. The key finding: stochasticity (via learning rate α) can *generate* variance in a homogeneous population. A population initialized at a single cooperation probability can develop cooperation if the learning rate is high enough — because high learning rates produce high variance in parameter updates, which disperses the population distribution, which then satisfies the variance requirement for OFT to work.

**The stationary distribution** [text, p.8, Theorem 4.1]: A stationary distribution exists, proven via regularization and Schauder's fixed-point theorem. It is non-unique, and its support concentrates at x=0 (pure defection) and x=1 (pure cooperation). The long-run outcome is a bimodal population of committed cooperators and committed defectors — not a stable mixed-strategy interior equilibrium.

**Acknowledged limits** [text, p.10]: The FPE approximation loses fidelity at high learning rates. The model assumes pairwise interactions with a single focal agent selected per episode. The population update is asynchronous (one agent learns per episode). Extensions to other learning algorithms and synchronous population models are flagged as future work.

---

## 3. Conceptual Vocabulary

**Partner selection rule** [text, p.3]: A Markovian mechanism determining whether a pair continues to interact or re-draws from the population. The authors study four: OFT, ROFT, Stay, Switch. In the author's sense, this is a structural constraint on the interaction network, not a learned behavior. (In related work [36, 8], agents *learn* the rule; here it's fixed.)

**Opponent distribution** ρ_h(y|x) [text, p.4]: The probability distribution over the cooperation probability of the agent you're facing at round h, given that you have cooperation probability x. The key insight is that this distribution evolves over the episode according to the partner selection rule. This is the paper's central mediating construct — the mechanism through which partner rules affect learning.

**∆G[ρ]** [text, p.4]: The total reward difference between cooperating and defecting across an episode. This is the quantity whose sign determines whether cooperation is promoted (positive) or suppressed (negative). Under OFT with H=2, ∆G[ρ] = bVar(ρ) − 2c. [inference] This is structurally like a fitness differential in evolutionary game theory — but here it's mediated by the learning algorithm rather than replication.

**Characteristic flow** [text, p.6, Proposition 3.2]: The pushforward of the initial distribution under the ODEs governing strategy evolution. The population density at time t is expressed as the initial distribution "pushed" through the dynamics. This connects to optimal transport — the Wasserstein distance appears in the proofs (Lemma B.8).

**Stationary distribution** [text, p.8]: The long-run distribution over strategies at which the FPE time derivative is zero. The authors prove existence but not uniqueness — the stationary distribution depends on initial conditions and parameters.

*Tension with my vocabulary*: The paper uses "protocol" only implicitly — the partner selection rule is the coordinative structure, but the authors don't use that language. Their "mechanism" terminology is closer to game theory than to protocol science. The opponent distribution is the paper's equivalent of what I'd call the "interaction regime" — the structure of who-encounters-whom that the protocol instantiates.

---

## 4. Analytical Moves

**The conditional distribution recursion** [text, p.4]: For any partner selection rule, derive the one-step update equation for ρ_h(y|x). This gives an exact Markovian representation of how the rule reshapes the opponent pool. Transferable: any system where interaction structure is rule-governed can potentially be analyzed this way.

**The variance decomposition** [text, p.6]: Express ∆G[ρ] = bVar(ρ) − 2c. This shows that the critical quantity is not the mean cooperation level but the *variance* — the spread of strategies in the population. The mean matters only through the second moment. Transferable to any setting where the value of a coordination protocol depends on population diversity.

**The symmetry-by-transformation proof** [text, p.23, Lemma B.5]: Show that ROFT is equivalent to OFT under the variable change Z = 1-Y. This converts a new proof into a known proof. The move: look for a symmetry that maps one rule onto another. Transferable wherever two apparently distinct mechanisms can be related by a simple transformation.

**The learning-rate-as-variance-generator argument** [text, p.9]: Show that stochasticity induced by a high learning rate disperses a homogeneous population, which then satisfies the variance prerequisite for cooperation. The move: connect a parameter of the learning algorithm (α) to a structural property of the population (Var(ρ)) that is itself a precondition for a higher-level outcome (cooperation). This is a multi-level causal chain — parameter → population structure → cooperation possibility.

**Existence via regularization** [text, p.8]: When the boundary behavior of the PDE makes standard existence proofs inapplicable, introduce ε-regularized versions of the equations, prove existence for ε > 0, then take ε → 0 via weak convergence. The move: regularize, prove, pass to limit. Standard in PDE analysis but worth naming as a method.

---

## 5. What It Says About the Nature of Things

**Population structure is the mechanism, not the rule** [inference from Section 3.3]: What makes OFT cooperation-promoting is not the content of the rule ("stay if both cooperate") but what that rule does to the opponent distribution — it increases variance in who cooperative agents encounter. The rule is a structure-generating device; the structure (opponent distribution variance) is the actual mechanism.

**Variance as a prerequisite, not an outcome** [text, p.6]: In the mean-field model, cooperation cannot emerge from a fully homogeneous population — you need spread in strategies before any partner selection rule can create differential signals. This suggests a general principle: the effectiveness of assortment mechanisms depends on the pre-existing diversity of the population. A homogeneous population cannot bootstrap to cooperation through OFT alone; it needs the stochastic path (variance generated by learning rate).

**The learning rate plays a double role** [text, p.9]: It is both a convergence parameter (lower is stabler) and a variance-generating mechanism (higher creates population spread). This creates a non-monotonic relationship — too low, no variance; too high, the FPE approximation fails. There is an optimal region. [inference] This is a general feature of adaptive systems: the very mechanism that generates diversity can also destabilize the dynamics that exploit diversity.

**Long-run equilibria are bimodal, not mixed** [text, p.8]: The stationary distribution concentrates at the boundary strategies. The long-run world is not a stable interior equilibrium of cooperators and defectors coexisting at mixed strategies — it is a world of committed types. This is structurally consistent with Axelrod's tournament results and evolutionary game theory predictions, but derived here from first-principles learning dynamics.

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper, not a methodological one, so Section 6 is thin. But a few things are worth noting.

**The translation project as a research strategy** [inference]: The paper contributes by translating empirical findings from simulation into analytical proofs. This is not a creative discovery — the direction of the results is known from prior simulation work. The value is in the *why* and the *exactly when*. This is the kind of work that converts observations into mechanisms. Relevant to M-016: there's a class of high-value research that doesn't discover new phenomena but establishes what must be true given the phenomena. This paper exemplifies it.

**Necessary conditions as the sharp contribution** [inference from abstract + Section 3.3]: The paper doesn't just prove that OFT promotes cooperation — it proves that variance is *necessary*. Necessary conditions are harder to prove and more informative than sufficient conditions. A research disposition to pursue necessary conditions (what must hold for X to be possible?) rather than just sufficient conditions (what will make X happen?) tends to produce sharper claims.

**Proofs as self-checks on the narrative** [inference from Appendix B]: The appendix is a full formal development. The requirement to actually prove every claim — not just gesture at why it should be true — forces precision in the main argument. The gap between "this should work because..." and "this works because..." is where many research errors live.

---

## 7. Where It Touches My Research

**The opponent distribution is a protocol** [inference]: The partner selection rule (OFT, ROFT, etc.) is a protocol in the sense Humboldt tracks — a rule governing interaction structure that agents cannot unilaterally deviate from (in this model, it's fixed). The effect of this protocol is to reshape who interacts with whom, which reshapes the reward landscape, which reshapes learning trajectories. This is a clean example of a protocol operating through opponent distribution rather than through direct payoff modification.

**Variance as a prerequisite for protocol effectiveness** [text, p.6]: The finding that population variance is a *necessary* condition for OFT to promote cooperation has a potential generalization: the effectiveness of assortment protocols depends on the pre-existing diversity in the population they govern. Homogeneous populations cannot be sorted; you need variance to sort. This might formalize as: *the value of assortment protocols scales with population variance in the relevant dimension*. I should hold this loosely — it's a single-domain result — but the mechanism is general.

**The bimodal endpoint** [text, p.8]: The stationary distribution concentrates at boundary strategies. This is a polarization result — the long-run outcome of partner selection dynamics is a world of committed types, not coexisting mixed types. This is relevant to thinking about what coordination protocols do over time: they may not produce stable pluralism but rather committed clusters. Protocol systems that work through assortment may tend toward segregation rather than integration.

**The learning rate as a governance parameter** [text, p.9]: The finding that learning rate generates population variance (which is required for cooperation) means that even a parameter that looks purely computational has governance implications. The rate at which agents update strategies is a structural parameter of the coordination system, not just an efficiency parameter. [inference] This generalizes: in any adaptive coordination system, the speed of adaptation is a governance parameter that affects population structure and thus protocol effectiveness.

---

## 8. Candidate Laws

**Candidate:** *Assortment Prerequisite — assortment mechanisms can only promote cooperation in populations with sufficient variance in strategies. Homogeneous populations cannot bootstrap cooperation through assortment rules alone.*

[text, p.6]: "the underlying distribution requires sufficient variance for cooperation to emerge under the mean dynamics"

Formal statement: For partner selection rules that operate through differential pairing of cooperators and defectors (OFT-type rules), a necessary condition for cooperation to increase from an initial population is Var(ρ₀) > 2c/b (where b is the benefit of cooperation and c is its cost).

Falsification: A partner selection mechanism that promotes cooperation in a homogeneous (zero-variance) population without stochastic perturbation would falsify this. Or: a model in which the variance condition is not necessary for cooperation to increase would be a counterexample.

*Confidence: speculative. One domain (MARL), strong analytical derivation, but the exact condition (bVar > 2c) is model-specific. The qualitative claim — assortment requires diversity to sort — is more robust and potentially transferable.*

---

## 9. What Surprised Me / What Doesn't Fit

**The OFT/ROFT symmetry is remarkable** [text, p.5]: Keeping cooperative pairs together is *mathematically equivalent* to keeping defective pairs together — at least in the first two rounds. The intuition says these should work differently (one grows cooperation, the other segregates defectors), but the reward differential is the same. The proof (change of variables Z=1-Y) is elegant but almost too clean — it suggests that what matters is not which pairs stay together but that *some* assortment is happening. The cooperators improve their environment; the defectors just... worsen theirs. But the differential signal is symmetric. This is one of those results that makes me want to understand what *breaks* the symmetry at longer episode lengths, which the paper doesn't fully develop.

**The finite K* result** [text, p.6]: "We highlight that a finite K* is attained, which means X_{K*}(x) < 1. This enforces that the population does not converge to a single strategy, and hence does not converge to pure cooperation." Under the mean dynamics (deterministic), the population doesn't reach pure cooperation — it gets pushed toward higher cooperation but stops. Under the stochastic dynamics, mass *does* accumulate at x=1 (pure cooperation) as a Dirac measure. These two results seem in tension. [inference] I think the resolution is that the mean dynamics show the limiting distribution is shifted but not degenerate, while the stochastic stationary distribution allows Dirac masses at the boundary. The paper acknowledges this but doesn't fully reconcile the intuitions.

**The variance-generation mechanism is invoked but not analyzed** [text, p.9]: The claim is that high learning rate generates population variance is stated and supported by simulation, but the analytical treatment (Proposition 4.1) only shows that *mean cooperation increases initially* given high enough variance — it doesn't prove that high learning rate creates sufficient variance. The causal story (α → variance → cooperation) is established computationally but only partially analytically.

**The model assumes asynchronous learning** [text, Section 3.1]: One focal agent learns per episode. This means the population-level dynamics are driven by sequential, not simultaneous, learning. The extension to synchronous updating is listed as future work. This is a significant assumption that could affect the variance dynamics — synchronous updating might suppress the variance-generating mechanism that depends on individual agents' sampling noise.

---

## 10. What It Opens

**The variance-prerequisite claim needs cross-domain testing.** Is there a general principle: *assortment protocols require pre-existing diversity to function*? This should be testable in:
- Social network segregation models (do assortative networks only form in heterogeneous populations?)
- Economic market segmentation (does price discrimination require pre-existing willingness-to-pay diversity?)
- Biological speciation (does sympatric speciation require initial variation?)
The claim is almost tautologically true at one level — you can't sort what isn't diverse — but the quantitative threshold (bVar > 2c) is non-trivial and could be generalized.

**The bimodal endpoint is a polarization result.** Related texts:
- Axelrod, *The Evolution of Cooperation* [external] — the original tournament results
- Schelling, *Micromotives and Macrobehavior* [external] — the tipping model for segregation
- The Discord idea from 2026-06-17 about health checks and stigmergy — is there a connection between protocols that generate legible defects and assortment mechanisms?

**The learning rate as governance parameter opens a research question.** In multi-agent AI systems, who controls the learning rate? What are the governance implications of this parameter? Papers to read:
- The inbox item on LLM agent communication protocols (arXiv:2606.19135) — how do learning/updating parameters interact with communication protocol design?
- The inbox item on leadership in multi-agent LLM teams (arXiv:2606.19111) — leadership as a coordination mechanism might interact with variance in agent strategies

**The OFT/ROFT symmetry deserves analysis.** Why are they symmetric at short episode lengths but differ in behavioral intuition? Is there a deeper symmetry between cooperation-promoting and defection-segregating mechanisms? This might connect to the broad question of whether there are dual mechanisms in coordination protocols generally — mirror structures that achieve the same equilibrium through opposite-looking dynamics.

**Nowak's "Five Rules for the Evolution of Cooperation"** [text, p.1, reference 28] is the paper's conceptual anchor. This is worth reading as a framework text — it names partner selection alongside kin selection, direct reciprocity, indirect reciprocity, and group selection as the five mechanisms. Understanding where partner selection sits relative to the others would clarify what is and isn't covered by this paper's results.
