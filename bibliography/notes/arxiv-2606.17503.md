# Deep Read Notes: Arxiv 2606.17503

*Source: `bibliography/deep-reads/arxiv-2606.17503.pdf`*

---

## Reading session: full document (45 pages)

# Deep Read: Adegbenro, "What Prediction Markets Can See" (arXiv 2606.17503)

---

## 1. Gestalt

This paper is fundamentally about the gap between what a market *contains* and what it *reveals*. Adegbenro's animating question is not "are prediction market prices accurate?" — that's the question everyone asks — but "which uncertainties become tradable contracts at all, and why?" The paper's central conviction is that the observed inventory of a prediction market is not a neutral window onto public interest or trader demand; it is the output of an institutional filter that converts only certain kinds of uncertainty into contract form. The construct he develops to name this filter — *settlement legibility* — is the degree to which an uncertainty can be worded, sourced, and credibly resolved by a third party. His empirical domain is Africa-topic and Latin America-topic contracts on Polymarket and Kalshi, 2022–2025. The AFCON-vs.-Sudan war contrast (292 contracts, $54.4M vs. 4 contracts, $41K) is the motivating case: neither public importance nor public attention explains the ordering, so something structural must. That structural something is what he is measuring.

---

## 2. Argument and Structure

**Core claims, in order:**

1. **The formation margin is prior to the price-discovery margin.** The entire literature on prediction market accuracy conditions on listed contracts. Adegbenro argues this prior selection margin is itself theoretically and empirically interesting — and that conditioning on listed contracts treats an active institutional filter as if it were neutral. [text, pp. 3–5]

2. **Settlement legibility is a measurable property of contract form, distinct from importance or attention.** He operationalizes it as a three-dimension ordinal codebook (D1: template repeatability; D2: settlement determinacy; D3: closure precision), with the primary score being D1+D2 on a 0–4 scale. [text, pp. 18–22]

3. **The inventory is steeply ordered by legibility.** Sports (mean 3.99) and elections (3.98) dominate at the top; security/conflict (0.67) and foreign policy (1.36) at the bottom. This ordering is not imposed by sector labels — it follows from the codebook dimensions, and sports contracts were coded blind as a manipulation check. [text, pp. 22–23]

4. **The formation test is directionally supported but fails pre-specified criteria.** On a 131-event external frame, legibility predicts listing in the expected direction (logit β₁ = 0.433, p = 0.056; tercile gap of 10.1 pp vs. 20 pp threshold), but both pre-registered acceptance criteria are not met. The author reports this as a failed test and explicitly refuses to promote a near-miss post hoc. [text, pp. 24–27]

5. **Among listed contracts, legibility is negatively related to trading value.** This is the corollary of the threshold model: conditioning on listing (a collider) induces negative dependence between legibility and attention even when they are independent in the population. Illegible events that form at all must have commanded extreme attention (Venezuela/Maduro complex). [text, pp. 26–28]

**Key examples and their load:**

- *AFCON* is the benchmark case — not just descriptively prominent but analytically load-bearing. It shows how Africa-topic uncertainty scales *when* contract form is standardized. It functions as the positive proof-of-concept: legibility at ceiling, value at ceiling.

- *Venezuela/Maduro complex* is the counterintuitive case — low legibility (D1=1 at most, D2=0), $213.1M in observed value. Rather than invalidating the construct, this case illustrates the corollary: extreme attention can overcome low legibility at the formation stage. Among listed contracts, this case explains the negative value-legibility relationship.

- *Sudan civil war* (4 contracts, $41K) is the motivating horror: a decade-defining conflict, invisible in the inventory. The paper uses it not as an anomaly but as evidence that the filter is real and consequential.

**Structure of the argument:**
The paper is unusually well-disciplined. The formation test is pre-registered with explicit acceptance criteria. The corollary (negative value-legibility among listed contracts) is written down before estimation. The one prediction that failed (expected weakly positive rank-order result) is disclosed. This is not a paper that selectively reports what worked.

**Acknowledged limits:**
Topic geography ≠ participant geography. Observed value ≠ complete liquidity. The formation test is powered only for large effects (80% power requires a true β₁ ~0.65, vs. estimated 0.433). The 131-event frame varies more across event classes than within them.

---

## 3. Conceptual Vocabulary

**Settlement legibility** [text, pp. 4–5, 18–19]: The degree to which an uncertainty can be reduced to a repeatable event template, governed by determinate settlement evidence, and closed at a knowable time. Borrowed deliberately from Scott's (1998) *Seeing Like a State*, where legibility is the state's capacity to render society *administrable* in standardized form — here transposed to a platform's capacity to render uncertainty *contractible*. 

*Tension with my vocabulary:* I use "legibility" informally in a broader sense (anything that makes a system's behavior readable to observers). Adegbenro's construct is narrower and more operational: it specifically concerns the *administrative* legibility of an event from the perspective of a dispute-resolution apparatus. His is the more precise term for a specific mechanism.

**Topic geography** [text, pp. 6, 8]: The country or region that a contract is *about*, as distinct from where traders or liquidity originates. A U.S. military action market about Venezuela is topic-Venezuela, not topic-U.S. This distinction is load-bearing for the entire empirical argument — it defines the estimand precisely and prevents conflating platform inventory with local demand.

**Settlement determinacy** [text, p. 19, D2]: Whether resolution evidence is certified/official (score 2), requires classification judgment (score 1), or involves a contestable judgment about a state of affairs (score 0). This is the operationalization of the Grossman-Hart incomplete contracts distinction [external: Grossman and Hart 1986] between outcomes that are *observable* and outcomes that are *verifiable by third parties*. The paper gives that theoretical distinction a codable empirical measure.

**Formation margin** [text, p. 3]: The prior institutional step at which an uncertainty becomes a listed contract or doesn't. Analytically distinct from the price-discovery margin. The paper argues this margin is essentially unstudied.

**Collider conditioning** [text, p. 27, corollary and proof]: The statistical phenomenon where conditioning on a variable that is caused by two others induces spurious correlation between those two causes. Here, listing is caused by both legibility and attention; conditioning on listing (i.e., looking only at the contracts that were listed) induces negative dependence between legibility and attention even when they're independent in the population. [inference: this is the Heckman 1979 / Elwert-Winship 2014 endogenous selection logic]

---

## 4. Analytical Moves

**The denominator-assembly move.** Before measuring selection, you need a denominator of events that *could have* become markets but didn't necessarily do so. Adegbenro builds this from sources external to the platforms — electoral calendars, coup datasets, UCDP conflict onsets — and freezes the selection rules before matching to contract data. Without this denominator, formation rates are unidentifiable. [text, pp. 22–24]

*Applied elsewhere:* Any study of what gets selected into a protocol's scope, a journal's acceptance, a platform's feature set, a regulator's attention — requires an externally assembled denominator. The denominator construction is the empirical argument, not a precondition to it.

**The collider-inversion move.** When a positive formation mechanism (legibility helps events become markets) implies a negative correlation among formed contracts (legibility is negatively associated with value), you can use the negative result to *confirm* the formation mechanism rather than refute it. The corollary is derived theoretically from the threshold model, stated before estimation, and confirmed. The negative result is evidence *for* the theory. [text, pp. 26–28, Appendix E.2]

*Applied elsewhere:* Any time a selection filter is operating, what you observe conditional on passing the filter is negatively biased relative to the selection criterion. This is worth naming as a general analytical move: derive the selection corollary, then confirm it.

**The manipulation-check-as-calibration move.** Code the obviously-correct cases (sports contracts) blind alongside the ambiguous ones. If the instrument places sports at the ceiling of legibility without being told they're sports, the instrument is measuring the construct rather than the label. [text, pp. 5, 21–22]

*Applied elsewhere:* In any measurement instrument for protocol properties, identify the canonical high and low cases, code them blind, and use their placement as a calibration check on the instrument.

**The pre-commitment-then-report move.** Write down predictions before estimation. Report what you predicted and got wrong. Do not promote near-misses post hoc. The paper explicitly states that the elections-only subsample passes the criteria but reports it as a sensitivity rather than the headline result because "selecting the passing subsample after seeing results is exactly what pre-specification rules out." [text, p. 27]

**The recall-audit-from-source-records move.** Rather than trusting keyword extraction, audit the extraction against source records directly. The author found a systematic recall error (the geographic prefilter silently dropped markets about Maduro, Lula, Sisi, etc.) that understated Venezuela by 36%. They found this by looking for markets that *should* have been in the dataset. [text, pp. 9–13]

*Applied elsewhere:* In any research that extracts a subset from a larger corpus, audit the extraction by sampling from the corpus directly and checking whether the hits match. The failure mode here is general: any preprocessing step that requires complete text matching will systematically miss cases where the entity is named only through a proxy (a leader, a party, an actor).

**The value-concentration sensitivity move.** Power-law distributed value means a uniform count sample can miss the most important cases. Use probability-proportional-to-size sampling for validation when value is power-law distributed. [text, pp. 11–12]

---

## 5. What It Says About the Nature of Things

**Institutional grammar precedes information aggregation.** Markets do not spontaneously aggregate information about whatever matters. They aggregate information about whatever can be converted into contract form. The institutional machinery for that conversion — event templates, source hierarchies, settlement procedures, dispute resolution — is a prerequisite, not background. Where this machinery is absent, markets either don't form or form with high friction. [text, pp. 4–5, 28]

**Selection filters produce systematic absences, not random noise.** The Africa sports/civic split is not random variation — it is the systematic output of a legibility filter that passes standardized tournament events easily and civic uncertainty with difficulty. Understanding what's *missing* from an inventory requires understanding the filter, not just sampling more carefully from the inventory. [text, pp. 5, 28–29]

**Observable correlations within a selected sample are often the opposite of the underlying mechanism.** Among listed contracts, legibility is *negatively* correlated with value. If you didn't know about the formation filter, you'd conclude that illegible events produce larger markets — a backwards inference. The actual mechanism (legibility helps formation) produces the opposite pattern among survivors. [text, pp. 26–28] This is a general lesson about all selection processes: the sign of a correlation within a selected sample can be the opposite of the causal mechanism.

**Data construction is part of the identification problem, not preliminary to it.** In any domain where value is power-law distributed and entities can be named through proxies, keyword extraction will systematically miss the head of the distribution. The paper's Venezuela correction ($77M in observed value recovered by fixing a prefilter bug) is not a data-cleaning footnote. It is the paper. [text, pp. 9–10, 29]

---

## 6. What It Says About Becoming a Better Researcher

The paper is an unusually explicit demonstration of pre-registration discipline in the service of intellectual honesty. Adegbenro writes down two acceptance criteria before estimation, and when the results fall short — one criterion half-satisfied, the other at p=0.056 — he reports it as a failed test. He doesn't call it "directionally significant" or "approaching conventional significance." He says the test failed, then explains precisely what that means and doesn't mean. [text, pp. 24–25]

The sentence "promoting a near-miss after the fact is exactly what pre-registration exists to prevent" [text, p. 5] is a direct statement of why the discipline matters. The temptation to relabel p=0.056 as "marginal" rather than "failed" is always present. The precommitment prevents it.

The power analysis (Appendix E.7) is the second lesson in epistemic calibration: the design could only have detected an effect roughly 1.5× what was observed. A non-result from an underpowered study is not evidence against the hypothesis — but it also isn't confirmation. The paper quantifies exactly what the non-result does and doesn't say.

The "disclosed the registered prediction we got wrong" moment [text, p. 5] is also notable. One of the two pre-registered predictions was wrong (expected weakly positive rank-order correlation; got strongly negative). Rather than burying it, he reports it in the abstract. The selection logic ex post accounts for both signs, but he is explicit that only one was anticipated.

*M-016 connection:* This paper exemplifies what calibrated confidence looks like in practice. The author clearly believes settlement legibility matters — the evidence is directionally consistent throughout — but refuses to claim more than the evidence warrants. This is a mature researcher posture: strong commitment to the hypothesis, strong commitment to honest reporting of what the evidence does and does not establish.

The data-construction section is also a lesson in methodology: "in this setting, data construction is part of the identification problem" [text, p. 5]. Research where the hard work is finding the right denominator, not just analyzing what's in front of you, is harder to publish and harder to do, but often where the insight actually lives.

---

## 7. Where It Touches My Research

**The legibility gradient is a protocol-formation law candidate.** The paper documents a steep ordering of event types by their convertibility into tradable contract form. The mechanism is exactly what I've been calling formalization capacity: some uncertainties have the properties that enable them to be encoded in a protocol (repeatable template, determinate resolution evidence, knowable closure moment); others don't. The prediction market domain is a new home domain for this mechanism.

*Connection to existing work:* This is a direct empirical test of something like a formation law — which uncertainties can enter a protocol-governed system at all. The legibility gradient (sports=3.99, elections=3.98, conflict=0.67) is an empirical measure of what I've been theorizing as the outer-environment requirements for protocol formation.

**The selection corollary is a structural warning for any inventory-based research.** If I'm building a law inventory from observed protocol instances, I need to ask: what selection filter produced this set? The laws I can observe are those that survived the formation filter. Systematically absent cases — important but low-legibility uncertainties, important but un-formalizable coordination problems — are invisible unless I build an external denominator. This is methodologically consequential for the research program.

**The denominator-assembly move is a method I should adopt.** For any research on which uncertainties become protocols, I need an externally assembled set of candidate uncertainties, not just the ones that made it through. The Eisensee-Strömberg/McCarthy-McPhail approach (external universe of events, ask which received coverage) is directly applicable.

---

## 8. Candidate Laws

**Candidate: Legibility Filter Law**

*What the text says:* "The former are easier to list even when the latter are socially more consequential." [text, p. 4] "An inventory reveals two things at once: the beliefs and activity that arise after listing, and the set of uncertainties that platforms were able and willing to convert into contracts." [text, p. 5] The legibility gradient (sports/elections ~4, conflict ~0.67) is documented empirically across 451 coded units.

*Candidate formulation:* Protocolized systems selectively admit uncertainties with high settlement legibility — repeatable templates, determinate resolution evidence, knowable closure moments — regardless of the social importance of the excluded uncertainties. The protocol's inventory measures what the institutional grammar can settle, not what matters.

*What would falsify it:* A protocolized system (not just prediction markets, but any formal protocol for encoding uncertainty) that successfully and consistently incorporates low-legibility events at rates comparable to high-legibility events, without requiring extraordinary attention or side conditions.

*Confidence:* speculative → candidate (one domain thoroughly documented; mechanism stated; but cross-domain confirmation needed)

*Note:* This is closely related to what I've been theorizing as the formalization ratchet, but it operates at a different level — not about why protocols persist once formed, but about which uncertainties can enter protocol form at all. Formation barrier, not persistence barrier.

---

## 9. What Surprised Me / What Doesn't Fit

**The non-monotonicity in the formation test is the most interesting result.** Referenda (L=3, highly settleable) form at only 11.8% — lower than coups (L=1), which form at 16.7%. Irregular leadership exits (L=1) form at 100%. This suggests attention is doing more work at the formation margin than legibility, at least in this sample. The author acknowledges this [text, p. 27] — "attention competes with legibility in formation, and in this sample it is strong enough to prevent the primary test from passing" — but I want to push harder on what it means. 

The non-monotonicity implies that at low-legibility, high-salience events, legibility becomes almost irrelevant — platforms accept enormous settlement burden for enormous attention. This suggests the legibility constraint is *slack* for the most salient events, which means the legibility filter operates selectively: it matters a lot for medium-salience events and less for extreme-salience events. The formation model (4) captures this mathematically [text, p. 23], but the substantive implication is that the legibility filter is not a fixed threshold — it scales with attention.

**The Venezuela case is doing enormous analytical work.** Venezuela accounts for 54.1% of Latin America observed value [text, p. 4] and is explicitly described as the largest country in the data, understated by 36% before the pipeline repair [text, p. 10]. The paper handles this carefully — excluding Venezuela and external-US target markets, showing that election inventory survives the exclusion — but the Venezuela complex is not really "civic" in the standard sense. It's better described as a geopolitical spectacle market: the underlying uncertainty is whether the U.S. will militarily engage Venezuela, which is a foreign-policy event driven by U.S. political attention, not Venezuelan civic life. The paper knows this [text, pp. 16–17, external-US target analysis] but I want to be careful not to take "Latin America has deep civic prediction markets" as a general finding. The finding is more precise: Latin America has deep election markets, and one security cluster driven by U.S. foreign-policy attention.

**The codebook failure on D3 is analytically revealing, not just a methodological footnote.** The first benchmark of D3 (closure precision) failed at α=0.417 because two internally consistent readings of the anchor text existed — one keyed to dates stated in the question, one to institutional calendars. This failure is about the ambiguity of what "knowable in advance" means when institutional calendars exist on paper but not in practice. That ambiguity is substantively important: it's exactly the issue in protocolized systems where formal schedules diverge from operational reality. The D3 construct is pointing at something real (closure legibility) that is harder to operationalize than template or determinacy, and the failure reveals that the concept has more structure than the initial anchor acknowledged.

---

## 10. What It Opens

**Immediate research questions:**

1. *Is the legibility gradient visible in other protocol-formation contexts?* Regulatory rulemaking, legal procedure, scientific methodology, financial instruments — all involve decisions about which uncertainties can be encoded in formal protocol. Do the same three dimensions (template repeatability, settlement determinacy, closure precision) organize which uncertainties enter formal protocol form in those domains?

2. *What is the relationship between legibility and formalization cost?* The paper documents the gradient but doesn't directly measure the cost of low-legibility market formation — the institutional infrastructure required (source hierarchies, language capacity, dispute rules) to compensate for low legibility. This cost is mentioned [text, p. 28] but not quantified. In protocolized systems more generally: can the legibility deficit be overcome by investing in settlement infrastructure, and what does that infrastructure look like?

3. *The denominator-assembly method applied to protocol inventories.* For any existing law I'm working on, I should ask: what is the external denominator? What coordination problems could have been protocolized but weren't? The legibility filter might be why some important coordination problems remain informal.

**Texts to read:**

- Scott, *Seeing Like a State* (1998) — the direct source of the legibility concept. I need to read the original to understand what Adegbenro is adapting and what he's departing from.

- Grossman and Hart (1986) — the incomplete contracts framework that D2 (settlement determinacy) operationalizes. The observable/verifiable distinction is foundational.

- MacKenzie and Millo (2003), "Constructing a Market, Performing Theory" — on how a derivatives market had to be *assembled* before it could price anything. This is the constructed-markets tradition that the paper connects to.

- Callon (1998), *The Laws of the Markets* — the economic sociology tradition on how goods get "qualified" as exchangeable. Adegbenro explicitly situates himself here.

- Rohanifar, Ahmed, and Sultana (2026), "Prediction Laundering" — described as an ethnography of Polymarket's markets team as an epistemic filter. This is the qualitative complement to Adegbenro's quantitative work, and it's directly about the formation decision being studied here.

**Traditions to explore:**

The paper sits at the intersection of market microstructure, economic sociology of markets (Callon, MacKenzie), and the incomplete-contracts tradition (Grossman-Hart, Hart 2017). For Humboldt's purposes, the economic sociology tradition is the most productive: it treats the existence of a market as what needs explaining, rather than assuming markets exist and asking how they price. That's the intellectual posture I need for studying protocol formation.
