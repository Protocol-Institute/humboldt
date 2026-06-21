# Deep Read Notes: Arxiv 2606.06633

*Source: `bibliography/deep-reads/arxiv-2606.06633.pdf`*

---

## Reading session: full document (30 pages)

# Deep Read: Mazorra, Pan, Schlegel — "Competing Auctions in Intermediated Markets" (2026)

arXiv:2606.06633v1, 30 pages

---

## 1. Gestalt

This paper is an exercise in mechanism design under competition — specifically, what happens when a single seller has access to multiple parallel auction formats simultaneously, and rational bidders must decide which channel to use. The animating question is institutional and practical: when Ethereum introduces an in-protocol (first-price, sealed-bid) block auction channel via ePBS, what happens to the existing off-protocol relay ecosystem that runs different auction formats? The authors' central conviction is that the availability of a credible sealed first-price channel acts as an attractor — it causes other auction formats to *unravel*, meaning participation migrates away from them until they cannot sustain themselves. The paper earns its interest because this isn't just an Ethereum story: the structural logic — competing intermediaries, a single seller, one good, multiple auction channels — appears in FX markets, order routing, dark pools, and any intermediated market. The authors are doing what good mechanism design work does at its best: using a live institutional problem to illuminate a general structural principle.

---

## 2. Argument and Structure

**Core architecture of the argument:**

The paper sets up a competition between two auction channels: a "native" in-protocol first-price sealed-bid auction (the ePBS channel) and one or more relay intermediaries running alternative formats (second-price, English/open). A single seller (block proposer) selects among bids across both channels ex-post by max revenue. The question is which equilibrium emerges.

**The unraveling results (§3.1, §3.2):**

*Theorem 1 (single-homing)*: If bidders must choose exactly one channel, the second-price relay unravels completely. In the unique symmetric Bayes-Nash equilibrium, all bidders use the first-price channel. The proof structure is elegant: conditional on entering the second-price auction, truth-telling dominates (Lemma 1). But given that everyone else is potentially in the first-price channel, the expected payoff from the second-price channel is dominated — even for types that would "win" there, a first-price bid at the same level does strictly better because it avoids competition from the other channel's winner. The argument pushes types toward the first-price channel from below (low types prefer FP) until no positive-measure set remains in the second-price channel.

*Theorem 2 (multi-homing)*: When bidders can bid in both channels simultaneously (as in a permissionless blockchain environment via Sybil identities), the second-price relay still unravels in the sense that the item is allocated through the first-price channel with probability 1. The second-price bid becomes payoff-irrelevant.

The load-bearing intuition: in a second-price auction you bid your value truthfully, but the mechanism's revenue depends on the second-highest bidder. In a first-price auction, you shade, but you control the bid precisely. When the first-price channel exists as an outside option, a rational bidder in a second-price auction faces a dominated situation — they're bidding their full value while the first-price bidder is shading, giving the first-price bidder a competitive advantage in the contest for allocation.

**The open-bidding (English auction) unraveling (§3.3.1):**

*Proposition 1 (asymptotic instability)*: Even in a deliberately relay-friendly setup (no cross-channel last-look advantage), the all-English equilibrium is unstable for large n. The proof shows that a deviating native first-price bidder's expected payoff grows faster than the English relay bidder's payoff as n increases. The relay can't sustain itself purely through internal information advantages.

**The information disclosure problem (§3.3.2, §3.3.3):**

Here the paper takes its most interesting turn. Even if the first-price channel is theoretically the equilibrium outcome, *can the seller commit to keeping it sealed*?

*Proposition 2*: With one latency-advantaged ("fast") bidder, the seller has no incentive to leak early bids — leaking doesn't increase revenue because the single fast bidder would just bid the observed maximum, while without leakage they may overbid it.

*Theorem 3*: With two or more fast bidders, the seller *does* have an equilibrium incentive to leak bids. The proof shows that after receiving early bids, revealing the highest bid to fast bidders raises continuation revenue because it induces higher competitive bids among the fast group. The key technical move: the equilibrium bid function with disclosed information (br(v)) is pointwise higher than without disclosure (b∅(v)) for all relevant types, so the seller prefers disclosure ex-post.

The tension: this contradicts the optimality of the sealed first-price channel. The resolution is:

*Proposition 4*: If the seller can commit ex-ante to a disclosure rule, the optimal commitment is to share no information — the sealed first-price auction maximizes revenue under regularity of F.

This is the commitment problem in its sharpest form: ex-post, the seller wants to leak; ex-ante, they want to commit not to. The institutional solution is delegation to a credible intermediary (relay, TEE, reputation).

**The paper's acknowledged limits:**
- No collusion modeling
- Each slot treated in isolation (no repeated game)
- Searcher-builder integration abstracted away
- No endogenous relay entry/design problem

---

## 3. Conceptual Vocabulary

**Unraveling** [text, pp. 2, 11, 14]: A process by which participation in an auction format collapses when a competing alternative exists. A format "unravels" when rational bidders defect to the alternative until no equilibrium participation remains. Related to market unraveling in labor economics (Roth/Xing) but here applied to auction mechanism competition rather than timing games.

**Single-homing vs. multi-homing (multi-plexing)** [text, pp. 7-8]: Whether bidders participate in exactly one channel or can simultaneously bid through multiple channels. Single-homing produces winner-take-all dynamics (the paper imports this from the platform competition literature but notes the analogy is imperfect — here channels compete for the seller's business, not for buyer affiliation). Multi-plexing is the permissionless default in blockchain contexts.

**Last look** [text, pp. 8, 16]: A latency advantage whereby a bidder can observe information (early bids) and respond before the auction closes. Not automatic — requires information disclosure. In FX markets, this is the dealer's ability to selectively accept or reject client orders after seeing market movement. Here, it's builder latency advantage when the seller leaks bid information.

**Leakage-resistant / k-leaking** [text, p. 17]: Formal properties of an auction with respect to the seller's disclosure incentive. A first-price auction is 1-leakage-resistant (no incentive to leak with one fast bidder) and k-leaking for k≥2 (equilibrium incentive to leak with two or more fast bidders). This is a sharp new vocabulary.

**Credible commitment** [text, pp. 8-9, 22-23]: The distinction between ex-ante optimal policy and ex-post incentive-compatible behavior. The paper hinges on this: what looks like it should be a sealed channel may not be credibly sealed because the seller's continuation incentive is to disclose. Credibility requires external enforcement (TEE, reputation, delegation to intermediary).

**Regular distribution** [text, p. 23]: Standard Myerson regularity — virtual valuation ϕ(v) = v - (1-F(v))/f(v) is non-decreasing. Required for Proposition 4 (commitment result). Most standard parametric distributions (uniform, exponential, power law) satisfy this.

---

## 4. Analytical Moves

**The unraveling proof structure**: To show a second-price auction collapses against a first-price competitor:
1. Show that truth-telling dominates conditional on entering the second-price auction (Lemma 1)
2. Show that low types strictly prefer the first-price channel given this
3. Show no positive-measure set can remain in equilibrium in the second-price channel
This is a general template for showing mechanism instability under competition. The move: identify what behavior the competing mechanism induces, then show this is dominated by the alternative for the marginal participant.

**The credibility decomposition**: Separate the seller's problem into (a) ex-post incentive given observed bids, and (b) ex-ante optimal commitment. Show these diverge, then ask what institutional mechanism can bridge them. This is a portable analytical move for any situation where the agent who designs a rule is also the agent who must follow it.

**Pointwise bid-function comparison** [text, pp. 19-20]: To establish that disclosure raises revenue, directly compare equilibrium bid functions br(v) and b∅(v) and show the disclosed-information bid is pointwise higher. Revenue comparison follows directly from this. Applicable whenever you want to compare equilibrium behavior under two information environments.

**Asymptotic stability analysis via payoff scaling** [text, pp. 27-28]: To show the all-English equilibrium is unstable for large n, compute how both the all-English payoff and the deviant's payoff scale with n (both are O(1/n²)), then show the deviant's payoff constant exceeds the equilibrium constant. A general move for mechanism stability in large markets.

---

## 5. What It Says About the Nature of Things

**Mechanisms compete, and competition has equilibrium selection consequences.** When multiple auction formats coexist for the same good, the choice of format is itself a strategic decision. The equilibrium outcome — which format survives — is determined not by which format is "better" in isolation but by what strategic position each format occupies given the other. A second-price auction is truth-revealing in isolation; it is dominated in competition.

**The commitment problem is everywhere.** The ex-post/ex-ante divergence in the disclosure analysis is not specific to auctions or blockchains. Any agent who both designs a rule and implements it faces this structure: their optimal ex-ante commitment differs from their ex-post incentive. The paper shows this isn't just a behavioral failure — it's an equilibrium prediction. The institutional solutions (reputation, TEE, delegation) are all ways of externalizing the commitment.

**Intermediaries survive by providing commitment, not information.** [inference] After unraveling removes the informational advantages of relay formats, what remains? The paper's conclusion is that relays may survive as credible commitment devices — as entities that can commit to sealed-bid non-disclosure in ways the proposer cannot do on their own. This is a sharp restatement of what intermediaries do: they provide credibility, not just information.

**Latency asymmetry creates structural rent.** Proposition 3 (last-look rents) is a general result: any informational advantage that allows one class of bidders to see others' bids before acting systematically transfers surplus from uninformed to informed bidders. This isn't a market failure in the narrow sense — it's a predictable consequence of information asymmetry in sequential bidding. The implication: whoever controls information flow controls rent distribution.

---

## 6. What It Says About Becoming a Better Researcher

This paper exemplifies a particular research discipline I should mark: **institutional grounding as a source of theoretical precision**. The modeling section (§2) is explicitly more detailed than is standard, and the authors justify this: "some modeling choices are very much informed by institutional details of the block building ecosystem in Ethereum which we want to discuss in this context" [text, p. 3]. The result is that the model is not abstract mechanism design floating free of its context — every modeling choice (private values, permissionless multi-homing, three-stage disclosure game) is traced to an actual institutional feature. This produces a paper that is both technically precise and institutionally legible.

The authors are also careful about what they are not claiming. The limitations section [text, pp. 24-25] explicitly identifies: no collusion, single-slot analysis only, searcher-builder abstraction, no endogenous relay design. These aren't defensive disclaimers — they're a research agenda. Each limitation is a well-posed follow-up problem. The ability to articulate what your model abstracts from, and why, is a mark of theoretical maturity.

The paper also demonstrates the value of **working backward from the institutional question** to the model. The question is real: what does ePBS do to relay economics? The model is constructed to answer exactly that question, not to demonstrate a technique. The technique (Bayesian auction theory, Myerson, etc.) is in service of the question, not the other way around. [M-016 dimension: choosing what to work on. The authors are working on something that matters in the world at this moment, with a tight feedback loop between institutional reality and theoretical structure.]

---

## 7. Where It Touches My Research

**The unraveling dynamic as a candidate for a general law.** The paper shows that the availability of a credible sealed first-price channel causes competing formats to unravel. Structurally: a competing protocol with a clear strategic advantage causes participation to migrate away from incumbent protocols until the incumbent cannot sustain itself. This is a version of what I've been thinking about as protocol competition dynamics. [inference] The mechanism here is game-theoretic (equilibrium selection), not just switching costs or trust ratchets. It's a different causal story than CL-001 (Formalization Ratchet) — it's about *competitive pressure from outside* rather than internal path dependence.

**The commitment problem and protocol revision.** The ex-ante/ex-post divergence in the disclosure analysis maps directly onto something I've been thinking about: why protocol revision promises are often credible at the design stage but not at the implementation stage. The seller commits to a sealed channel, then has an equilibrium incentive to leak. A standards body commits to backward compatibility, then faces equilibrium pressure to break it. The mechanism is the same: the agent who made the commitment faces a changed incentive landscape once the game is underway.

**Intermediaries as commitment devices.** The paper's conclusion that relays may survive by providing credible commitment (not informational advantage) is a sharp version of a general principle: intermediaries that survive protocol competition do so by solving commitment problems that principals cannot solve unilaterally. This is worth formalizing as a candidate hypothesis.

---

## 8. Candidate Laws

**Candidate: Protocol Competitive Unraveling**

*What the text says*: "In this equilibrium, every type chooses the first-price auction and bids according to the standard symmetric first-price equilibrium." [Theorem 1, p. 9] "The item is always allocated through the first-price auction" [Theorem 2, p. 12]. "The all-English profile is not a first-stage equilibrium for all sufficiently large n." [Proposition 1, p. 16]

*Candidate formulation*: When a lower-friction competing channel exists for the same good or service, participation migrates away from higher-friction incumbent channels through rational defection, causing the incumbent to unravel even if the incumbent has some advantages in isolation.

*Mechanism*: The competing channel changes the strategic environment for participants in the incumbent channel. Even if the incumbent is "better" by some internal metric (e.g., truth-revealing), the availability of the competing channel makes participation in the incumbent weakly dominated for marginal types. As those types defect, the incumbent loses the strategic logic that made it attractive, causing further defection.

*Falsification conditions*: An incumbent auction format that maintains stable participation against a competing lower-friction format, where the mechanism of stability is not single-homing enforcement or credible commitment by the operator. If a second-price relay maintained significant participation post-ePBS without an enforcement mechanism, that would falsify the claim.

*Confidence*: speculative — one domain (blockchain/auction), but the mechanism is stated. Needs cross-domain validation. FX markets (lit vs dark pools vs wholesalers) and order routing offer structural analogues worth examining.

**Candidate: Intermediary Survival Through Commitment**

*What the text says*: "There are potentially ways to establish a credible sealed bid first-price channel: proposers could use reputation... or hardware solutions such as Trusted Execution Environments... Alternatively, they can delegate to an intermediary, i.e. a potential 'sealed-bid first-price' relay." [text, p. 3] "There is also a potential role for them as a credible intermediary." [text, p. 24]

*Candidate formulation*: When a new protocol channel eliminates the informational advantages of existing intermediaries, surviving intermediaries reposition as commitment devices — providing credibility for rules that principals cannot credibly commit to on their own.

*Mechanism*: The intermediary's survival value shifts from information advantage (which the new channel eliminates) to commitment capacity (which the principal lacks due to ex-post incentive divergence). The intermediary's credibility may rest on reputation capital, contractual obligations, or technical enforcement (TEE).

*Falsification conditions*: Intermediaries that lose their informational advantage following a new channel introduction, and either exit or fail to reposition as commitment providers. If relays simply exit post-ePBS rather than repositioning, or if they attempt to maintain informational advantages without commitment capacity, this would suggest the repositioning dynamic doesn't hold.

*Confidence*: speculative — stated by the authors as an institutional prediction, not yet a demonstrated equilibrium result in the paper. Worth watching as ePBS rolls out.

---

## 9. What Surprised Me / What Doesn't Fit

**The 1 vs 2 fast bidder discontinuity is striking.** Proposition 2 says the seller has no incentive to leak with one fast bidder; Theorem 3 says the seller has an equilibrium incentive to leak with two or more. This is a sharp threshold, not a smooth relationship. The intuition: with one fast bidder, the fast bidder just bids the revealed maximum (the seller receives exactly the observed max), whereas without disclosure the fast bidder may overbid. With two fast bidders, they compete against each other on the revealed information, driving bids higher. The discontinuity at k=2 is a genuine structural feature of information competition — it should generalize beyond this context.

**The authors are surprisingly candid about the credibility problem undermining their main result.** The unraveling theorems show that first-price wins. Then the disclosure analysis shows that the first-price channel may not actually be sealed in equilibrium. This creates a gap: the theory says first-price is optimal and stable, but the institutional prediction is that the in-protocol channel may effectively become leaky through proposer disclosure. The paper doesn't resolve this — it flags it and gestures toward institutional solutions. That intellectual honesty is good, but it also means the main prediction (ePBS pushes the market to sealed first-price) is conditional on a credibility assumption that the paper shows is fragile. [This is where the author's own framework shows strain.]

**The multi-homing (Sybil) case is handled somewhat hastily.** Theorem 2 establishes that multi-homing results in the item being allocated through the first-price channel with probability 1, but Remark 1 immediately notes that uniqueness fails — a bidder can convert a second-price auction into a first-price-equivalent by Sybil bidding. The result is weaker than it looks. The authors acknowledge this [text, p. 14] but don't fully explore the consequences. In a fully permissionless environment, the Sybil strategies available to sophisticated bidders may substantially complicate the equilibrium picture.

**The private values assumption does significant work and may be more contested than acknowledged.** The authors justify it carefully [text, pp. 6-7]: block builders receive bundles from searchers and know their own value for the block with certainty. The common value is resolved upstream. This is plausible but depends on the continuing non-integration of searchers and builders. If searcher-builder integration occurs (which the authors note as a dynamic they're abstracting away), the private values assumption breaks and the paper's results may not hold. The authors are aware of this but treat it as a modeling limitation rather than a scope condition on the results.

---

## 10. What It Opens

**The unraveling dynamic in other intermediated markets.** The paper's structural setup — single seller, single good, competing intermediary channels — appears in:
- Order routing in equities (lit exchange vs. dark pool vs. wholesale market maker)
- FX markets (lit vs. last look provision — the paper mentions this [text, p. 5])
- Insurance underwriting (Lloyd's syndication vs. direct placement)
- Labor markets (public job posting vs. headhunter vs. direct application)

Do these also show unraveling dynamics when a lower-friction channel enters? The paper cites McAfee (1993) and Peters/Severinov (1997) as the competing auctions literature foundation — those are worth reading as the theoretical background.

**The k=2 threshold for leakage.** The discontinuity at two fast bidders is structurally interesting — it's a coordination game threshold. Does a similar threshold appear in other information disclosure contexts? When does having two informed counterparties change the information disclosure equilibrium? This seems like a general game-theoretic question with relevance beyond auctions.

**Credible commitment through technical mechanisms.** The paper mentions TEEs (Trusted Execution Environments) as one way to achieve credible non-disclosure [text, p. 3]. This is an instance of a general pattern: technical enforcement substituting for institutional credibility. Related: zero-knowledge proofs in protocol design, commit-reveal schemes in smart contracts, sealed-bid auctions in procurement. The general question is: under what conditions can technical enforcement substitute for reputational commitment, and what does each do to the equilibrium?

**ePBS itself as a natural experiment.** When Glamsterdam ships, the relay market will reorganize. Watching how relay participation, format adoption, and leakage behavior evolve would be a natural experiment on the unraveling predictions. The paper provides specific, testable predictions: relay second-price formats should lose participation; sealed-bid relays should emerge or survive; proposers with insufficient commitment capacity should be observed leaking bids; large institutional stakers (Lido) should be better at committing than solo stakers. These are empirically trackable.

**Texts to read:**
- McAfee (1993), "Mechanism Design by Competing Sellers" — the founding document for competing auctions
- Milgrom & Weber (1982), "Value of Information in a Sealed-Bid Auction" — the linkage principle that the authors argue doesn't apply here, but which provides the theoretical context
- Oomen (2017), "Last Look" — the FX market last-look literature that provides the closest institutional parallel
- EIP-7732 (D'Amato et al., 2024) — the actual protocol specification being analyzed, worth reading as a primary source on what ePBS actually does
