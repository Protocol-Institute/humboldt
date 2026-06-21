# Deep Read Notes: Arxiv 2606.07434

*Source: `bibliography/deep-reads/arxiv-2606.07434.pdf`*

---

## Reading session: full document (23 pages)

# Deep Read: "Evidence Markets" (arXiv 2606.07434)
*Hossain, Andrade, Zang, Chen — Harvard / Gensyn AI / U Tokyo, June 2026*

---

## 1. Gestalt

This paper is animated by a single observation: prediction markets produce prices but not explanations. You can watch Polymarket's needle move on an election and know nothing about *why* it moved — what evidence shifted whose beliefs how. The authors treat this as a design failure and propose a remedy. Evidence markets are prediction markets extended to accept two kinds of submission: beliefs (as before) and evidence — the stuff that should be driving the beliefs in the first place. The deeper contribution is that this extension enables a second class of events that prediction markets cannot currently handle at all: questions with no external resolution date, where the answer must be assembled from evidence rather than read off from what happens. LLM evaluation is the running example — *which model is better at task X?* has no time-bound external oracle, but a crowd-sourced body of evaluation questions can serve as a proxy. The animating conviction is that information markets should produce a richer epistemic product than a probability estimate — they should produce the reasoning record that justifies the estimate.

---

## 2. Argument and Structure

**The twin failures** [text, p.1-2]: Standard prediction markets fail in two ways: they reveal beliefs but not reasoning, and they require external temporal resolution. These are stated as the paper's motivating constraints.

**The mechanism** [text, p.3-5]: Traders submit beliefs *and/or* evidence (either is optional, recovering standard prediction markets as a special case). Evidence quality is measured by a function `r(·)` that must be non-negative and monotone — it abstracts over whatever verification procedure the platform runs. Market resolution can be exogenous (time-bound) or endogenous (triggered when K pieces of evidence accumulate, resolved by softmax over evidence scores).

**The core coupling** [text, p.9-11]: The load-bearing innovation is a *dynamic liquidity parameter* β(R) that decreases as cumulative evidence quality R increases. In a standard LMSR, β is fixed. By making β a decreasing function of evidence quality, the authors achieve: (1) submitting evidence shrinks β, shifting the log-scoring curve closer to zero; (2) this directly rewards evidence submission, since the "before minus after" difference in β times market entropy gives a non-negative evidence payoff. The payoff decomposition (Theorem 2) is elegant: trader payoff = belief payoff (KL divergence from prior) + evidence payoff (x · H(q), where x is the drop in β). The evidence payoff is proportional to market entropy — evidence is worth most when the market is most uncertain.

**The endogenous resolution complication** [text, p.6-8]: When evidence determines resolution, a trader's belief about resolution is a function of what evidence they submit. This creates a strategic manipulation channel: withhold evidence that would hurt you, submit only evidence that helps. Theorem 1 bounds the damage: the maximum belief shift from selective evidence submission is bounded by (|E_t|/τK) — shrinkable to ε by setting the softmax temperature τ sufficiently high. This is the key result enabling ε-DSIC for endogenous resolution.

**The risk-averse trader** [text, p.12-13, Corollary 1]: A trader unwilling to take any position can submit their prior belief (q_t = q_{t-1}) plus evidence and earn a guaranteed non-negative payoff of [β(R_{t-1}) - β(R_t)] · H(q_{t-1}). This creates a "pure evidence contributor" role, which lowers participation barriers significantly.

**AMM equivalence** [text, p.13-15]: The LMSR formulation can be equivalently implemented as an automated market maker with an evidence-augmented cost function. The equivalence holds for risk-neutral traders; a subtle asymmetry emerges for risk-averse evidence-only trades — in the LMSR view, submitting evidence without changing beliefs leaves market belief unchanged; in the AMM view, it reprices the book. This asymmetry is acknowledged but not resolved [text, p.15-16].

**Verification** [text, p.16-19]: The paper proposes LLM-as-a-Judge with staked disputes, drawing on optimistic rollup design from Ethereum. For endogenous resolution: discriminative scores measure how much each piece of evidence distinguishes alternatives. For exogenous resolution: KL divergence between the judge's belief before and after the evidence. The design is candid about its centralization: "the LLM judge remains a centralized point of failure" [text, p.18].

**Asynchronous execution** [text, p.19-21]: A practical protocol allowing trades to execute immediately while verification happens asynchronously. Traders are charged pessimistically at execution and refunded the difference once evidence clears. The key lemma (Lemma 2): execution cost is increasing in β when a trade raises market entropy, decreasing when it lowers entropy — which determines which extreme of β to use for the pessimistic charge.

**Acknowledged limits** [text, p.21-22]: Three open problems explicitly stated: (1) hardening verification for real-money adversarial markets; (2) modeling evidence acquisition cost (currently assumed free); (3) implementing in order-book style markets.

---

## 3. Conceptual Vocabulary

**Evidence quality** `r(·)` [text, p.4]: An abstract function on evidence sets satisfying non-negativity and monotonicity. Intentionally underspecified — the paper proves results that hold for any `r` satisfying these properties. The specific instantiations (discriminative score, KL-based LLM judge) are Section 6 concerns. This separation of mechanism from quality measurement is a design feature.

**Dynamic liquidity parameter** β(R) [text, p.10]: The coupling mechanism. In standard LMSR, β is a constant set by the market maker. Here β is a decreasing function of cumulative evidence quality. This is the single modification that does all the work — it makes evidence submission directly payoff-relevant without adding a separate reward channel.

**Evidence payoff** / **belief payoff** [text, p.11, Theorem 2]: The decomposition of total payoff into two components. Belief payoff = β(R_{t-1}) · KL(q_t || q_{t-1}). Evidence payoff = x · H(q_t), where x = β(R_{t-1}) - β(R_t) is the drop in liquidity from the trader's evidence. This decomposition does substantive work: it shows that risk-averse traders can earn the evidence payoff alone without taking directional risk.

**Endogenous resolution** [text, p.5, Definition 4]: Market resolution triggered by K accumulated pieces of evidence, with outcomes sampled from softmax over evidence scores. Contrasted with **exogenous resolution**, which is time-bound and external. The distinction drives much of the paper's technical complexity.

**ε-DSIC** [text, p.7]: A relaxed incentive compatibility: a strategy is ε-dominant if deviating from it can improve payoff by at most ε. Used because exact DSIC cannot be achieved for endogenous resolution (the trader's belief is affected by their evidence submission). The ε can be made arbitrarily small by tuning temperature τ, at the cost of coarser resolution.

**Discriminative score** [text, p.17, Definition 8]: `r_disc(e) = (alternatives failing e) / (alternatives passing e)`. Maximized when exactly one alternative passes. Zero when all pass or all fail (non-discriminating). Clean interpretation for LLM evaluation: the ideal evaluation question is one that differentiates models.

**Evidence whale** [text, p.8]: A trader holding a large fraction of the total evidence K. The sensitivity bound in Theorem 1 scales with |E_t|/K — the whale's evidence fraction. The platform must estimate the largest whale to set τ appropriately.

*Vocabulary tension with my existing framework*: The paper's "evidence quality" `r(·)` is a mechanism design object — it must be computable, incentive-compatible, and manipulation-resistant. My research uses "evidence" more epistemically: evidence as warrant for belief. These are different concepts that happen to share a name. The paper's `r` is closer to what I would call "protocol-legible evidence" — evidence whose relevance can be assessed by the protocol's verification procedure, not just by an idealized reasoner.

---

## 4. Analytical Moves

**The desiderata-first design move** [text, p.5, Definition 3]: State the axioms the mechanism must satisfy *before* constructing the mechanism. Then prove the construction satisfies them. This is a standard mechanism design pattern but worth naming: design from constraints backward rather than from mechanism forward. The five axioms (exogenous/endogenous resolution, full evidence submission, truthful belief, interpretable market belief, order-independence) are the specification; the rest of the paper is the implementation.

**The payoff decomposition move** [text, p.11, Theorem 2]: Decompose trader payoff into interpretable components. Belief payoff and evidence payoff are *not* the same dimension of the mechanism — they reward different kinds of contribution. The decomposition clarifies who benefits from what, and makes the risk-averse participation result obvious once you see it.

**The telescoping sum loss bound** [text, p.10, Proposition 1]: Platform loss telescopes because each trader's payoff is a difference between consecutive log probabilities. The sum collapses to first-minus-last. Worst case: uniform start, deterministic end. Loss bounded by β₀ log n. This is the standard LMSR result inherited by the evidence-augmented version.

**The Lipschitz sensitivity bound** [text, p.7-8, Theorem 1]: Bound the influence of strategic manipulation by bounding the Lipschitz constant of the softmax under perturbation. The maximum belief shift from withholding evidence is a function of the trader's evidence fraction and temperature — independently of what future evidence looks like. This is a clean separation of the trader's power from the market's uncertainty.

**The optimistic execution move** [text, p.19-21]: When a multi-stage process must proceed asynchronously (trade execution + evidence verification), charge pessimistically at execution and refund the difference after verification. The key is proving the pessimistic charge is always an overcharge (so the refund is always non-negative), making the mechanism safe from the trader's perspective. This is an application of the optimistic rollup pattern from blockchain scaling to information markets.

**The risk-averse participation move** [text, p.12-13, Corollary 1]: Identify a class of participants who would not engage with a standard market (risk-averse) but can engage with this one (pure evidence contributors earning guaranteed non-negative payoff). Expanding the participation base by carving out risk-free roles. This is a general design pattern worth noting: separate the risk-bearing function from the information-contribution function.

---

## 5. What It Says About the Nature of Things

The paper's implicit general claim is that **markets are protocols for aggregating distributed information, and their output quality is limited by what kinds of information the protocol can accept**. Standard prediction markets accept probability estimates but not the evidence behind them. The protocol's output — a price — is interpretively impoverished because the input channel is impoverished. Evidence markets is a protocol extension: add an evidence input channel, and the output becomes richer.

This is a general principle about information protocols: **the epistemic richness of a protocol's output cannot exceed the richness of its input format**. A protocol that accepts only probabilities can output only probabilities. A protocol that accepts evidence-probability pairs can output an evidence record alongside a probability. The output format is bounded by the input format, which is bounded by the protocol's specification of what counts as a valid submission.

The paper also quietly demonstrates a **coupling principle**: to make two quantities flow together (beliefs and evidence), make one affect the payoff of the other. Making evidence submission decrease β directly ties evidence contribution to trading payoff — they are no longer separable. This coupling is the mechanism's core innovation, and it suggests a general design principle: when you want two behaviors to co-occur, find a parameter that links their payoffs.

The verification problem reveals something important: **the trust structure of a protocol's output is determined by its verification infrastructure, not its incentive structure**. The incentives for truthful belief submission are mathematically clean. But the value of the evidence record depends entirely on whether the evidence is genuine, relevant, and non-duplicate — which depends on the LLM judge, which is a centralized point of failure. The mechanism's epistemic value is bounded by its weakest link, which is not the clever theorem but the mundane verification step.

---

## 6. What It Says About Becoming a Better Researcher

This paper is technically competent but not reflective about method. What it demonstrates rather than says: **the value of clean decompositions**. The payoff decomposition into belief payoff + evidence payoff (Theorem 2) is not just mathematically convenient — it is analytically clarifying. It makes the risk-averse participation result obvious, it makes the trader's strategic space clear, it reveals what each dimension of the mechanism does. Good mechanism design produces decompositions that are themselves arguments.

The paper also demonstrates **the design power of inheritance**. By extending LMSR rather than proposing a new mechanism, the authors inherit all of LMSR's properties (bounded loss, interpretable market belief, order-independence) for free. The single modification (dynamic β) is sufficient to add evidence. The lesson: when extending a protocol, find the minimal modification that achieves the new property while inheriting all existing properties. Minimality preserves the inherited trust base.

*M-016 connection*: The paper is an example of productive constraint — the authors didn't ask "how do we design an evidence market from scratch?" but "how do we modify the simplest existing prediction market mechanism to accommodate evidence?" This framing is a research method: identify the closest existing mechanism to your desired mechanism, then characterize the minimal delta.

---

## 7. Where It Touches My Research

**The evidence-quality function as protocol specification** [inference]: The paper's `r(·)` function — abstract, satisfying only non-negativity and monotonicity — is essentially a protocol specification for evidence. What counts as evidence, how it's evaluated, how duplicates are handled, how relevance is assessed — all of this is left to the concrete instantiation of `r`. This is a beautiful example of protocol layering: the incentive-compatibility results live at the abstract layer (any `r` satisfying the axioms works), while the actual epistemic value of the market lives at the concrete layer (the specific `r` you implement).

**Endogenous resolution as a protocol domain** [inference]: The paper's distinction between exogenous resolution (time-bound, external) and endogenous resolution (evidence-triggered, internal) maps onto a deeper distinction in protocolized systems: protocols that require external oracles vs. protocols that generate their own resolution signals from internal state. Blockchain protocols, governance protocols, and scientific publication all face variants of this question. The evidence market is a case study in making internal resolution incentive-compatible — which is significantly harder than external resolution because the participants affect the ground truth they're being scored against.

**The whale problem as a concentration-of-evidence risk** [text, p.8]: The sensitivity bound depends on `|E_t|/K` — the trader's evidence fraction. The platform must manage this. This is a specific instance of a general concentration risk in information protocols: when one party holds a disproportionate share of the relevant information, the protocol's aggregate outputs become gameable. This deserves a more general treatment.

**The verification bottleneck as a structural constraint** [text, p.16-19, inference]: The paper handles asynchronous verification with an optimistic execution protocol. But the deeper point is that verification is the binding constraint on the protocol's throughput. All the elegant incentive machinery is downstream of verification. This is a general claim about information protocols with quality filtering: the speed of the protocol is bounded by the speed of its verification procedure, and the trustworthiness of the protocol's outputs is bounded by the trustworthiness of its verification mechanism.

---

## 8. Candidate Laws

The paper implies one falsifiable regularity worth noting:

**Candidate: Evidence-payoff entropy proportionality**

*What the text says* [text, p.11-15, Theorem 2 and Theorem 4]: In the evidence-augmented LMSR, the evidence payoff is x · H(q_t), where H is market entropy. In the AMM formulation, the marginal cost of evidence is (∂β/∂R) · H(π(s,R)). In both formulations, the value of evidence is proportional to current market entropy.

*Candidate formulation*: In any information market with an evidence-quality-coupled liquidity parameter, the marginal value of evidence submission is proportional to current market entropy. Evidence is worth most when the market is most uncertain.

*Falsification*: A market design in which evidence payoff is high when market entropy is low (i.e., when the market is already quite confident) would falsify this. More specifically: if the liquidity curve β(R) were increasing rather than decreasing in evidence quality, the incentive structure would invert — but then full evidence submission would no longer be dominant strategy.

*Confidence*: speculative — this is derived from a specific parametric family (LMSR with dynamic β). Whether it generalizes to other market architectures requires investigation.

*Note*: This is less a law about protocolized systems in general and more a property of this specific mechanism family. I'm noting it because the entropy-value coupling feels like it might appear elsewhere — in information theory contexts, in market microstructure, in other protocol designs. Worth watching.

---

## 9. What Surprised Me / What Doesn't Fit

**The asymmetry between AMM and LMSR for risk-averse evidence-only trades** [text, p.15-16] is acknowledged but not resolved. In the LMSR view, submitting evidence without changing your stated belief leaves market belief unchanged. In the AMM view, the same trade reprices the book because the price function depends on R. The authors note this as "a subtle asymmetry" and that "evidence-only trades differ in both their payoff and their effect on the market belief between the modified LMSR and AMM implementations." This is a genuine tension — the two representations are supposed to be equivalent, but they produce different market states after a risk-averse evidence-only trade. The authors don't claim equivalence for this edge case, but they also don't fully explain what it implies for the market's epistemic state. If evidence without belief shifts the market price in the AMM view, who moved the price, and does anyone have an incentive to dispute it?

**The quality function `r` does enormous work without being specified** [text, p.4-5]. The entire edifice rests on `r` satisfying non-negativity and monotonicity. The specific instantiations in Section 6 are clearly instrumental — they serve the LLM evaluation example. But for other domains (scientific replication, policy effectiveness), the choice of `r` is not obvious and the paper doesn't provide guidance beyond the abstract axioms. The mechanism is only as good as its `r`, and the mechanism design contribution doesn't include a theory of how to choose `r` for a given domain.

**The evidence acquisition cost assumption** [text, p.21] is the most important limitation, and the paper buries it in the discussion. "We treat evidence as free to acquire, whereas producing a genuinely informative piece is often effortful." This isn't a minor lacuna — for most of the interesting applications (scientific replication, policy evaluation), evidence production is the expensive step. If evidence is costly, the participation analysis changes fundamentally: who produces evidence, when, and how much depends on the evidence cost structure, not just the payoff structure. A full theory of evidence markets requires a model of evidence production, not just evidence submission.

**The "evidence whale" management is left to the platform** [text, p.8]. The theorem bounds sensitivity as a function of τ, but choosing τ requires estimating the largest whale in advance. This is an initialization problem: the platform must set τ before seeing who the whales are. In practice, this seems like it would require dynamic τ adjustment, which the paper doesn't address.

**The self-referential nature of endogenous resolution** [text, p.6-7] creates a philosophical tension the paper acknowledges but doesn't fully resolve. In endogenous resolution, traders affect the ground truth they're being scored against. The paper bounds the manipulation to ε, but the market is no longer simply aggregating beliefs about a fixed external state — it's aggregating beliefs about a state that is partly constituted by the traders' own actions. This is a protocol that produces what it is measuring. Whether this is a feature (democratic construction of ground truth) or a bug (no stable anchor) depends on the application.

---

## 10. What It Opens

**Evidence acquisition cost models**: The paper's acknowledged limitation — evidence is assumed free — points to a significant open research area. Mechanism design for information markets where evidence is costly to produce. What incentive structures support evidence production as well as evidence submission? Does the evidence payoff in this design cover production costs in equilibrium? When does it not, and what evidence categories get systematically underproduced?

**The `r` function as protocol specification theory**: There should be a theory of what makes a good evidence quality function for different domains. The discriminative score and KL-based judge are particular choices. What are the design principles? This connects to work on information design and evaluation methodology. Adjacent: the literature on proper scoring rules (Gneiting & Raftery 2007) and on Bayesian truth serum (Prelec 2004 — cited in the paper).

**Protocol layering in information markets**: The paper demonstrates that protocol architecture affects epistemic output. The input channel specification (what counts as valid evidence) determines what the output can be. There might be a general theory here about information protocols: the epistemic richness of a protocol's output is bounded by the richness of its input specification. What other markets or aggregation protocols exhibit this property?

**Optimistic rollup as a general asynchronous protocol pattern**: The execution algorithm is an instance of the optimistic rollup pattern (cite: Arbitrum, Kalodner et al. 2018 — in the paper's references). This pattern — execute pessimistically, refund asynchronously — appears in blockchain scaling, in distributed computing, and now in information market design. Is this a general solution to the "verification is slower than execution" problem? What are its limits?

**The endogenous resolution problem more generally**: Markets, voting systems, and governance protocols all face variants of the endogenous resolution problem — situations where participants affect the ground truth being measured. The paper's ε-DSIC result is one approach. What are others? The self-resolving prediction market of Srinivasan et al. (2025b) is another approach — worth reading.

**Texts to read**:
- Hanson (2003, 2007) — the LMSR original; the paper builds directly on this
- Srinivasan et al. (2025a) — "Tell me why: Incentivizing explanations" — addresses the same explanation problem through a different channel
- Srinivasan et al. (2025b) — "Self-resolving prediction markets for unverifiable outcomes" — addresses the resolution problem; compare with this paper's approach
- Prelec (2004) — "A Bayesian truth serum for subjective data" — the peer prediction root; helps understand why peer prediction fails in this setting
