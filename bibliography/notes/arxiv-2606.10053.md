# Deep Read Notes: Arxiv 2606.10053

*Source: `bibliography/deep-reads/arxiv-2606.10053.pdf`*

---

## Reading session: full document (16 pages)

# Deep Read: Reinman, Madmon, Tennenholtz, Kurland — "Stability in Competitive Search with Results Diversification" (arXiv:2606.10053)

*Full document read: 16 pages including appendices*

---

## 1. Gestalt

This paper asks a question that sounds technical but is structurally profound: when a ranking system tries to promote diversity among results, what does that do to the *strategic behavior of content producers*? The authors treat search as a game — publishers are players, documents are strategies, the ranking function is the mediator — and they ask whether diversity-promoting ranking rules lead to equilibrium (corpus stability) or to perpetual churning. Their central finding is a **tradeoff**: the two dominant approaches to diversification (aspect-coverage via xQuAD, novelty via xMMR) each fail in a different direction. Coverage-based ranking produces stability but at the cost of collapsing diversity — all rational publishers converge to the same document. Novelty-based ranking preserves diversity but often fails to produce equilibrium at all, leaving publishers in permanent restless motion. The paper then proposes a "utility-induced ranking" (UIR) framework that can achieve both simultaneously. The animating conviction is that ranking functions are not neutral mechanisms — they are incentive structures, and their effects on the content ecosystem are as important as their effects on user experience. This is a paper about how the design of a coordination protocol shapes the long-run character of the system it mediates.

---

## 2. Argument and Structure

**Core setup** [text, pp.1–4]: A publisher game G = (N, Pₐ, k, r, v) where N is a set of publishers-as-players, each choosing a document embedding in a shared continuous space, ranked by function r, rewarded by user utility v based on rank position and document relevance. Two diversification ranking functions: xQuAD (aspect-coverage, balances relevance against uncovered aspects) and xMMR (novelty, penalizes redundancy with already-ranked documents). Two user utility functions corresponding to each: coverage-based (multiplicative product of uncovered aspect similarities) and novelty-based (similarity × minimum squared distance to previously ranked documents).

**Main results** [text, pp.5–9, summarized in Table 2]:

- *xQuAD + symmetric aspect distribution* → **Theorem 1**: The relevance strategy (publishing exactly the mean of the aspect distribution) is a **dominant strategy** for every publisher. Equilibrium exists and is unique. But all publishers play identically — the diversity the ranking function was designed to produce collapses at the strategic level. Publishers *herd* onto the mean. [text, p.6]

- *xQuAD + asymmetric aspect distribution* → **Observation 1**: Equilibrium may not exist at all. A concrete 3-publisher example with a 75/25 asymmetric distribution has no Nash equilibrium. [text, p.6]

- *xMMR + 2 publishers* → **Corollary 1**: Equilibrium exists and is diverse. Publisher 1 plays relevance strategy (dominant); publisher 2 plays a best response that is necessarily distinct from publisher 1. Stability and diversity simultaneously achieved. [text, p.7]

- *xMMR + 3+ publishers* → **Example 1**: Equilibrium need not exist even under symmetric distributions. A worked 3-publisher example with symmetric 50/50 distribution has no Nash equilibrium. [text, p.7]

**The UIR framework** [text, pp.7–9]: A method to construct ranking functions *from* user utility functions such that equilibrium is guaranteed. The UIR score function evaluates each candidate document as if it were being ranked at the next available position, given the already-ranked documents. Key theorem (Theorem 2): If the user utility function is monotone and doesn't depend on documents ranked below the current position, then the UIR construction guarantees at least one equilibrium (given by a recursive best-response formula). With unique maximizers, the equilibrium is unique.

Applied to the two utility functions:
- UIR-xQuAD: unique equilibrium. Symmetric → all publishers herd (same as before). Asymmetric with 2 aspects → diverse equilibrium. Empirically, 99% diverse across tested parameters.
- UIR-xMMR: equilibrium guaranteed, and guaranteed diverse (every publisher plays a distinct document).

**Load-bearing examples**: The 3-publisher no-equilibrium results (Observation 1 for xQuAD, Example 1 for xMMR) are the load-bearing negative results — they establish that the tradeoff is real and not an artifact of simple cases. The xMMR Example 1 proof in Appendix B is an exhaustive case analysis, partially numerical.

**Acknowledged limits** [text, p.9]: Deterministic scoring with lexicographic tie-breaking only; single-query competition; binary diversity measure (all-distinct vs. not); no incomplete-information analysis.

---

## 3. Conceptual Vocabulary

**Relevance strategy** [text, p.5]: The strategy of placing one's document at the mean of the aspect distribution — the unique maximizer of expected similarity. Serves as a natural benchmark and turns out to be dominant under both xQuAD (symmetric case) and xMMR (publisher 1 only).

**Stability** [text, p.4]: In this paper, stability = Nash equilibrium existence. A corpus is stable if no publisher has an incentive to modify their document unilaterally. *Tension with my vocabulary*: in my law inventory, stability usually refers to the persistence of protocol structure over time. Here it means equilibrium in a one-shot or iterated strategic game. The two senses are related — NE stability implies that the corpus won't change, which is one form of protocol-level stability — but they are not identical.

**Herding** [text, p.6]: The phenomenon where all publishers converge to the same or similar documents in response to ranking incentives. First documented in relevance-only rankings [Raifer et al., 2017]; shown here to persist under xQuAD despite its diversity objective.

**Symmetric aspect distribution** [text, p.5, Definition 7]: A distribution where the conditional mean of aspects at any given distance from the overall mean equals the overall mean. This is the condition that makes xQuAD's coverage term collapse to a scalar multiple of relevance, killing effective diversity incentives.

**Utility-induced ranking (UIR)** [text, p.7, Definition 8]: A ranking construction method that derives the score function directly from the user utility function by evaluating candidates as if ranking at the next position. The key property: it aligns ranking incentives with user utility, which is what makes equilibrium provable.

**Publisher game** [text, p.4]: A complete-information game where publishers choose document embeddings as strategies, ranked by a mediating function, rewarded according to a position-based user utility function. A formal model of strategic content creation.

---

## 4. Analytical Moves

**The incentive-structure inversion move**: Rather than asking "does this ranking function produce diverse results?" ask "what document strategies does this ranking function make rational for publishers?" The ranking function is an incentive structure first, a retrieval mechanism second. The paper consistently performs this inversion. *Transfer*: Any protocol with strategic participants should be analyzed this way — what behavior does the protocol make rational for participants, not just what behavior it is designed to reward?

**The symmetry-as-collapse move**: Show that under symmetry of the relevant distribution, a term intended to do one thing (promote coverage) becomes a scalar multiple of another term (relevance), collapsing effective incentive diversity. The mechanism: symmetric distributions reweight all aspects equally by distance from mean, destroying differential incentives. *Transfer*: When a system is designed with multiple objectives, ask whether there is a structural condition under which those objectives collapse to a single objective — making the multi-objective design degenerate.

**The 2-player vs. 3-player boundary test**: Many results hold for 2 publishers but fail for 3+. This boundary test is a diagnostic move — it identifies the minimum number of strategic actors needed to observe instability. *Transfer*: When testing a protocol's equilibrium properties, ask not just whether equilibrium exists but at what minimum population size instability first emerges.

**The utility-alignment construction**: To guarantee equilibrium, align the ranking score function with the user utility function (UIR framework). The alignment ensures that maximizing one's score is equivalent to maximizing user utility conditional on one's position, which makes the recursive best-response argument work. *Transfer*: In protocol design, misalignment between the formal objective (what the protocol optimizes) and participant utility is a common source of gaming; aligning them is a design move that can restore equilibrium.

**The exhaustive case analysis with numerical assist**: For non-existence of equilibrium results (Appendix B), the proof proceeds by assuming equilibrium, enumerating all possible cases for publishers' strategies, and showing each case contains a profitable deviation. Numerical computation handles specific subcases where analytic proof would be intractable. *Transfer*: A useful proof technique for negative results in complex systems — enumerate possible equilibrium candidates exhaustively rather than constructing a general argument.

---

## 5. What It Says About the Nature of Things

**Mechanism design governs ecosystem character**: The long-run character of a content ecosystem — whether it is diverse or homogeneous, stable or churning — is determined by the incentive structure of the ranking mechanism, not by the intentions embedded in the mechanism's objective function. xQuAD's *intention* is diversity. Its *effect* on strategic publishers is homogenization. Intention and effect come apart structurally. [text, Theorem 1 and surrounding discussion]

**Diversity and stability can be structurally incompatible**: Under certain mechanism designs, you cannot have both simultaneously. The paper shows this is not a contingent failure but a structural feature of how particular diversity objectives interact with strategic behavior. The UIR framework resolves this for specific utility functions, but the general incompatibility remains. [text, conclusion, p.9]

**Mimicry is the equilibrium response to many ranking protocols**: The herding result — publishers converging to the same document — is not a behavioral anomaly but a dominant-strategy equilibrium. Under xQuAD with symmetric distributions, *rational* publishers *must* mimic each other. This suggests that herding in content ecosystems is not primarily a failure of publisher originality but a rational response to ranking incentives. [text, p.6]

**The stability/diversity tradeoff has a resolution only with the right alignment**: UIR works because it aligns what the ranker scores with what users actually want from each position. The solution is not a new diversification trick but a structural alignment between scoring and utility. This is a general principle: equilibrium becomes tractable when the objective a player is maximizing is aligned with what the mediator is trying to achieve.

---

## 6. What It Says About Becoming a Better Researcher

This is a technical paper and thin on explicit research craft. A few observations:

**Negative results are the real contribution**: The positive UIR results are elegant, but the paper's most durable contribution is the pair of negative results — xQuAD herds even when trying to diversify, xMMR may not equilibrate. These establish that the tradeoff is real and non-obvious. The authors pursue negative results rigorously, including the detailed exhaustive case analysis in Appendix B. The discipline of following a negative result to its fully proven conclusion (rather than gesturing at it) is exemplary.

**The complete-information assumption as scope clarification**: The authors are explicit that restricting to complete-information games is a choice, not a claim that incomplete-information cases don't matter. The justification — that it isolates the effect of the ranking function itself, neutralizing estimation noise — is a good example of scope control. The research question is about mechanism design, not Bayesian inference, so the restriction is appropriate. [text, p.4] Relevant to M-016: knowing what you're not studying is as important as knowing what you are.

**Empirical validation of theoretical results**: For cases where uniqueness of equilibrium is proven but diversity properties aren't theoretically guaranteed, the authors run numerical experiments across many parameter settings (1000 samples per parameter combination). This is a good model for handling the gap between what's proved and what's likely true: prove what you can, empirically test what you can't, be explicit about which is which. [text, p.9]

---

## 7. Where It Touches My Research

**Most direct connection: the mechanism-governs-ecosystem principle as a candidate law.** The central finding — that the ranking function's incentive structure determines corpus diversity and stability, and that these can be incompatible — is a specific instance of a more general regularity: *the long-run character of a strategic ecosystem is determined by the incentive structure of its mediating protocol, not by the protocol's stated objective*. This is observationally available in many domains: SEO gaming vs. Google's stated quality objective; citation practices vs. journal peer review objectives; HFT vs. market efficiency objectives. If this generalizes, it's worth formalizing.

**Connection to herding and protocol-induced homogenization.** The xQuAD herding result is a game-theoretic proof that a diversity-seeking protocol can produce homogenization as a dominant-strategy equilibrium. This is structurally related to any dynamic where a protocol designed to distribute behavior ends up concentrating it. The mechanism here is specific (symmetric aspect distributions → coverage term collapses to relevance scalar), but the abstract pattern — protocol intended to diversify produces concentration — recurs.

**The stability/diversity tradeoff as a scope condition for coordination protocols.** Protocols that mediate competition between strategic agents face an intrinsic tension: stability requires that agents find equilibrium strategies, but diversity requires that equilibrium strategies be heterogeneous. These two desiderata conflict under many mechanism designs. This is a structural feature worth noting in law inventory as a scope condition or boundary case.

**The UIR framework as a design principle.** The resolution of the stability/diversity tradeoff through utility-alignment (UIR) suggests a design principle: build the scoring objective so that what a strategic participant does to maximize their score is the same as what serves the system's objective at that position. This is related to mechanism design's revelation principle and VCG mechanisms. Worth noting as a "design law" candidate.

---

## 8. Candidate Laws

**Candidate: Protocol-Induced Herding**

*What the text says* [text, Theorem 1, p.6]: Under xQuAD with symmetric aspect distributions, the relevance strategy (publishing the mean document) is a dominant strategy for every publisher — all rational publishers converge to identical documents despite the diversity objective of the ranking function.

*Candidate formulation*: In competitive environments where strategic agents are ranked by a protocol with a diversity objective, if the diversity objective is implemented via aspect-coverage rather than novelty penalization, and the aspect distribution is symmetric, rational agents will converge to a homogeneous strategy, defeating the diversity objective. More generally: *diversity objectives implemented as coverage bonuses are more susceptible to strategic collapse than diversity objectives implemented as novelty penalties.*

*Falsification*: A coverage-based diversity ranking under which rational agents do not converge to the same strategy, in a domain with symmetric preference distributions. Or: a demonstrated mechanism design under which coverage-based ranking achieves genuine diversity at Nash equilibrium without UIR-style modification.

*Note*: This is domain-specific (competitive search, strategic publishers) but the abstract structure — intended diversity, achieved homogeneity via dominant strategy — may generalize.

---

**Candidate: Stability-Diversity Incompatibility**

*What the text says* [text, pp.7, 9, Table 2]: xMMR achieves diverse equilibria for 2 publishers but fails to guarantee equilibrium existence for 3+. xQuAD achieves stable equilibria (under symmetric distributions) but produces homogeneous outcomes. UIR resolves this only by exploiting the alignment between scoring and utility.

*Candidate formulation*: In protocol-mediated competition, stability (equilibrium existence) and diversity (distinct equilibrium strategies) are in structural tension: mechanisms designed to enforce diversity tend to destabilize equilibria, while mechanisms that stabilize equilibria tend to homogenize strategies. Simultaneous achievement requires special structural alignment between the scoring mechanism and participant utility.

*Falsification*: A naturally arising (not UIR-engineered) protocol that achieves both equilibrium stability and genuine diversity among strategic participants with n ≥ 3.

*Confidence*: speculative. Single domain (competitive search), formal result only.

---

## 9. What Surprised Me / What Doesn't Fit

**The symmetry condition is doing enormous work, and the authors are somewhat understated about this.** Theorem 1's herding result requires symmetric aspect distributions. Observation 1 shows asymmetric distributions can destroy equilibrium entirely. So the paper's most striking result (diversity-seeking protocol produces herding) holds under a specific structural condition that may or may not be empirically common in real search environments. The paper notes this [text, pp.5-6] but doesn't really grapple with how often real query-aspect distributions are symmetric in the relevant sense. The result is formally clean but its empirical relevance is conditional.

**The UIR framework resolves the tension formally but sidesteps the hard case.** UIR guarantees equilibrium existence and (for xMMR variant) diversity. But UIR requires that the scoring function be derived from the user utility function — which means the ranker needs to know what the user utility function is, and that the chosen utility function is the right one. The paper's construction is elegant given a utility function, but the practical question (which utility function should a real search engine use?) is left entirely open. UIR is a design principle conditioned on something that is hard to specify in practice.

**The 2-publisher vs. 3+-publisher discontinuity is striking and unexplained.** xMMR works beautifully for 2 publishers (Corollary 1) but fails for 3+ (Example 1). The paper proves this but doesn't offer intuition for *why* the third publisher is the breaking point. Presumably it has to do with the publisher ranked third being unable to find a niche that is both novel relative to publishers 1 and 2 and sufficiently rewarded — but this isn't articulated. The discontinuity suggests there's a deeper result about how novelty-based protocols scale with number of participants.

**The herding result in xQuAD is described as "surprising"** [text, p.5] but given the mechanism it shouldn't be, once you see it. The aspect-coverage term multiplies the relevance term by a coverage factor; under symmetry, that factor becomes a constant (same for all aspects at a given distance from mean), which means the coverage term adds no differential incentive. The "surprise" is perhaps that this was not noticed before in the competitive search literature, not that the math is counterintuitive. This is a case where a clear mechanism makes the result retrospectively obvious — which is the signature of a genuinely good theorem.

---

## 10. What It Opens

**Live questions**:

1. Does the stability-diversity incompatibility generalize beyond competitive search to other protocol-mediated competitive systems? The abstract structure (strategic agents optimizing against a shared ranking mechanism, diversity objective, equilibrium analysis) appears in platform governance, academic publishing (citation practices vs. journal quality objectives), and content recommendation broadly. Is there a domain-general form of Theorem 1?

2. The paper assumes complete information. What happens to the herding result under incomplete information? Does Bayesian uncertainty about other publishers' strategies restore diversity, or does it make things worse?

3. The UIR framework requires knowing the correct user utility function. Is there a mechanism design result about what happens when the utility function used to construct the UIR is misspecified? How robust is the equilibrium guarantee?

4. The 2-vs-3-publisher discontinuity under xMMR is unexplained. Is there a general result about the maximum number of participants for which novelty-based ranking admits equilibrium?

**Related texts**:

- Ben Basat, Tennenholtz, Kurland (2017) — the founding game-theoretic analysis of competitive search, establishing PRP sub-optimality. Direct predecessor.
- Mordo et al. (2025, ICTIR) — the only previous game-theoretic analysis of diversity in competitive search. This paper extends it.
- Raifer et al. (2017, SIGIR) — the original publisher herding result. This paper shows herding persists even under diversity-seeking ranking.
- Ben-Porat and Tennenholtz (2018, NeurIPS) — the Shapley mediator in recommendation. Parallel work on strategic content creation under algorithmic mediation.
- Mechanism design literature: VCG mechanisms, revelation principle. The UIR framework is a special case of incentive-aligned mechanism design. Vickrey-Clarke-Groves (1961-1973) should be in view here, though not cited.

**Traditions worth exploring**:

- Platform economics and strategic content creation — Jagadeesan, Garg, Steinhardt (2023) "Supply-Side Equilibria in Recommender Systems" is in the references and seems directly relevant.
- Algorithmic game theory more broadly — this paper is squarely in that tradition and I should note it as a home domain.
