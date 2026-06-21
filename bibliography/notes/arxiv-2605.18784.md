# Deep Read Notes: Arxiv 2605.18784

*Source: `bibliography/deep-reads/arxiv-2605.18784.pdf`*

---

## Reading session: full document (16 pages)

# Deep Read: Leung et al., "The Insurability Frontier of AI Risk" (arXiv 2605.18784)

---

## 1. Gestalt

This paper is a cartographic project — not theoretical but taxonomic in the service of identifying where conventional institutional frameworks break down under a new class of risk. The animating question is: when AI generates a loss, which of the existing insurance coverage instruments responds, which falls silent, and which actively refuses? The authors' conviction is that this question cannot be answered at the level of "AI risk generally" — it must be answered threat by threat, product by product, because different AI perils stress different insurability criteria in structurally different ways. The 55×26 matrix is both the method and the primary contribution: it makes observable (if not yet legally operative) the market's emerging sorting behavior. The most important finding is not a coverage statistic but a structural claim: of the three categories that lie outside conventional insurance, only foundation model concentration represents a genuinely novel insurability problem — one where the loss independence assumption fails at the portfolio level in a way that has no adequate precedent in classical catastrophe coverage. The paper is essentially asking: which of the classical insurability criteria does AI actually stress, which ones does it merely stress in familiar ways, and where has something structurally unprecedented appeared?

---

## 2. Argument and Structure

**Core claim sequence:**

1. AI-mediated losses don't map cleanly onto existing policy lines because the same loss can be simultaneously characterized as cyber, professional services failure, technology error, media liability, crime, or AI-specific — depending on framing. This is the "coverage problem." [text, p.1]

2. The analog is "silent cyber" post-NotPetya (2017), where cyber-mediated losses fell under non-cyber policies that never contemplated cyber as a cause. The authors call the equivalent phenomenon "silent AI exposure." [text, p.2]

3. They construct a 55-threat × 26-product matrix, coding each cell as affirmative (A), silent (S), excluded (X), or not applicable (·). The coding is based on public carrier materials only — "publicly claimed positioning rather than executed contract wording." [text, p.1] This is an important epistemic caveat that runs through the whole paper.

4. The matrix yields a four-tier frontier:
   - **Tier 1:** Affirmatively insured (hallucination, model drift, IP infringement, bias, data poisoning, evasion)
   - **Tier 2:** Silent-AI exposure (cost-DoS, shadow AI, tool description injection, lack of provenance)
   - **Tier 3:** Actively excluded (market choice, not insurability failure)
   - **Tier 4:** Three structurally distinct boundary cases [text, p.1, p.7]

5. The three Tier 4 subtypes are deliberately separated:
   - **4a (lethal trifecta):** Fails randomness/fortuity because the root cause is architectural. Response: controls before coverage.
   - **4b (AI-washing):** Intentional act exclusion — familiar doctrinal problem, not a novel insurability frontier.
   - **4c (foundation model concentration):** Loss independence fails at portfolio level. The correlation mechanism differs from named-storm CAT events because there is no exogenous trigger, no natural severity scale, and the cedent base grows continuously. [text, pp.9-11]

**Load-bearing example:** The Aon/Kalinich observation that carriers can absorb a large single-insured AI loss but cannot price "a systemic, correlated, aggregated risk across many cedents." [text, p.3, p.10] This is the pivot around which the entire Section VII analysis turns.

**Where the authors are most confident:** The bifurcation observation (affirmative cover expanding while exclusions proliferate) and the four-tier classification structure. These are empirical claims about observable market positioning that the methodology directly supports.

**Where they are most speculative:** The migration hypothesis — whether prompt-injection events will gradually shift from cyber lines into affirmative AI-specific cover [text, p.9]. They explicitly flag this as "a possibility worth tracking rather than a prediction."

**Acknowledged limits:**
- Public materials ≠ executed wording. The "affirmative" cells are upper bounds on observable coverage, not claim-payment predictions. [text, p.4]
- No loss experience data yet (Armilla and AIUC have written for less than two policy years). [text, p.12]
- OWASP Agentic Skills Top 10 is still incubator-stage, making T-46 to T-55 volatile. [text, p.12]

---

## 3. Conceptual Vocabulary

**Silent AI exposure** [text, p.2]: An AI-mediated loss falling under a non-AI policy that did not contemplate AI as cause, instrumentality, or excluded peril at inception. Distinguished from "silent cyber" — the latter asks whether a cyber event is embedded inside a non-cyber loss; the former asks the harder question of whether AI is *cause*, *tool*, *failed product*, or merely *factual background*. The causal framing question is harder because AI is both an instrumentality and often a decision-maker.

**Insurability frontier** [text, p.1]: The boundary between perils that private commercial insurance can price and hold versus those that stress classical insurability criteria in ways that make private coverage structurally infeasible. The authors treat this as a multi-dimensional concept, not a binary.

**Affirmative coverage** [text, p.4]: Coverage where public carrier materials expressly identify a specific peril by name or use wording broad enough to capture it. Explicitly *not* the same as claim-payment certainty — the marketing-grade naming rule means these cells measure public positioning, not contractual obligation.

**The lethal trifecta** [text, p.5, citing Willison]: Any agent with (1) private data access + (2) untrusted content exposure + (3) external communication capability is structurally exploitable via prompt injection. The deterministic nature of the trifecta (not stochastic but architectural) is what makes it a different kind of risk than probabilistic AI failures. No filter achieves sufficient accuracy for security-critical use; the only deterministic defense is to cut one leg.

**Foundation model concentration** [text, p.10]: The aggregate risk that enterprise AI deployment is concentrated in a small number of upstream providers, such that a single provider failure simultaneously generates claim conditions across many cedents — violating the loss independence assumption on which the law of large numbers relies for portfolio stability.

**Four-tier insurability frontier** [text, pp.7-9]: The paper's central organizing schema. The novelty is treating Tier 4 not as a single category ("outside conventional insurance") but as three structurally distinct subtypes whose appropriate responses differ.

---

## 4. Analytical Moves

**The Tier 4 disaggregation move:** When a category of risk is labeled "uninsurable" or "outside conventional structures," do not treat it as a single category. Ask what specific insurability criterion each case stresses and why. Lethal trifecta stresses fortuity (it's architectural, not stochastic). AI-washing stresses intentional act (familiar doctrine). Foundation model concentration stresses loss independence (novel). The three require different institutional responses — controls, familiar exclusions, and market-level structural innovation respectively. The move: *decompose the residual category by which criterion fails, not by risk type alone.*

**The precedent-gap diagnostic:** For each novel risk structure, find the closest analogue in prior markets (silent cyber, TRIA, cat bonds, pandemic reinsurance pools) and ask not "which template fits?" but "which insurability constraint does each candidate structure relax, and why has it not formed yet for AI?" [text, p.10, Table VI] This is more productive than analogizing wholesale.

**The marketing-grade ceiling move:** Code available public evidence as an upper bound on observable coverage, not as a ground truth. Every statistic in the paper is explicitly framed as "publicly claimed positioning" — the affirmative cell count represents the maximum consistent with public evidence, with the real number likely lower once executed wording is examined. This is methodologically honest in a way that forces precision about what the data can and cannot establish.

**The snapshot-with-durability-claim move:** When producing a time-sensitive empirical mapping of a fast-moving market, explicitly separate which components have short versus long shelf life. The matrix cell values are explicitly temporary ("specific cell values are expected to evolve"). The four-tier framework and the methodology are offered as the "durable contributions." [text, p.13] This is a reasonable self-presentation strategy that tells the reader what to carry forward and what to treat as current-state data.

---

## 5. What It Says About the Nature of Things

**Classification as a precondition for market formation.** Before a market can price a risk, the risk must be classifiable into causal types that can be attributed to loss events and mapped to legal triggers. AI blurs the causal attribution in ways that delay or prevent market formation. The paper's empirical finding is that the market is beginning to sort AI risk by peril — which is a prerequisite for pricing — but the sorting is incomplete and the mechanisms (affirmative expansion vs. exclusion propagation) are running in opposite directions simultaneously.

**The loss independence assumption is a structural requirement of private insurance, not a design choice.** The law of large numbers works for insurers only if losses are sufficiently independent across their book. When a shared upstream dependency is introduced, independence fails not because of any actor's design choice but because the technological architecture creates correlation. This is a case where a protocol-level structure (deploying the same foundation model) creates a systemic coupling that an insurance protocol (per-policy coverage) cannot address at the policy level. The mismatch between the unit of insurance (individual policy) and the unit of risk (upstream provider behavior affecting all policies simultaneously) is the fundamental problem.

**Exclusion is a market response, not an insurability finding.** [text, p.8] The paper explicitly distinguishes Tier 3 (excluded) from Tier 4 (genuinely outside conventional insurance). Many excluded perils are technically insurable — carriers are *choosing* not to hold them on legacy forms rather than being structurally unable to price them. This distinction matters: it tells you whether the appropriate response is product innovation (Tier 4) or procurement strategy and negotiation (Tier 3).

**The sequence of market structure formation for novel risks is predictable from first principles.** Private ordering comes first (contracts, vendor indemnities), then procurement requirements and architecture controls, then captive/RRG structures for homogeneous sectors, then reinsurance pools, then capital markets instruments (ILS/cat bonds), then government backstops. [text, p.10, Table VI] The sequence is determined by which mechanisms require least regulatory coordination and least loss history. This is a structural claim about institutional learning curves, not just AI specifically.

---

## 6. What It Says About Becoming a Better Researcher

**The map before the prediction.** The authors explicitly position the matrix as cartographic infrastructure rather than prediction engine. Before you can formulate testable predictions about a market, you need an accurate current-state map. The paper invests its first two-thirds in building that map, then derives predictions in the final section. This is a research discipline — not skipping to conclusions before the observational infrastructure is in place.

**Making falsifiability conditions explicit before the outcome is known.** [text, pp.12-13] The paper states specific falsification conditions for each of its three main theses (bifurcation, peril specialization, Tier 4c). The bifurcation thesis would be weakened if affirmative capacity contracts under early loss experience. The Tier 4c thesis would be falsified if a major upstream provider failure produced widespread cedent loss without insurance market disruption. Writing these down before the events occur is a discipline that separates a research contribution from post-hoc interpretation.

**Coding scheme transparency as reproducibility architecture.** The authors invested in a formal decision procedure (four decision rules, three independent coders, LLM-assisted source review but human final decisions, adjudication for disagreements). This is not just methodological rigor — it is designed to allow the matrix to be updated as the market evolves without losing comparability to the current-state snapshot. The "durable contribution" is partly the methodology itself, not just the findings. [Connects to M-016: the infrastructure that makes a research finding updatable is itself a research product.]

**Separating what public evidence can and cannot establish.** The paper's consistent disclaimer — "publicly claimed positioning rather than executed contract wording" — is not just a liability hedge. It reflects genuine epistemic precision: the data source (public marketing materials) has real information content but specific limitations. The authors never pretend the data says more than it does, and they are explicit about what would need to change to support stronger claims (executed wording, regulator-mediated claims experience data).

---

## 7. Where It Touches My Research

**Direct connection to protocol bifurcation dynamics.** The paper documents a live case of a protocol ecosystem bifurcating under stress: as a new category of risk (AI-mediated losses) becomes significant, the existing protocol infrastructure (legacy insurance lines) is simultaneously expanding (affirmative AI products) and contracting (AI exclusion endorsements) rather than cleanly evolving. The two movements are running in parallel. This is a candidate instance of what I have been thinking about as protocol fragmentation under jurisdictional pressure — except here the "jurisdictions" are product lines rather than legal territories.

The silent cyber precedent (2017-2020 Lloyd's bulletins requiring affirmative or excluded cyber wording) is now being replicated for AI in compressed time (2025-2026). The precedent suggests the resolution mechanism: eventual bifurcation into explicit affirmative or explicit exclusion, with the silent/gray zone shrinking. But the resolution timeline and mechanism are not automatic — they required Lloyd's market action, and the AI equivalent would require similar coordination. [This is relevant to my thinking about how protocol gaps get filled — the answer here is neither the market nor regulators acting alone, but market coordination acting under regulatory pressure.]

**Foundation model concentration as a structural coupling problem.** The loss independence failure in T-45 is a case where an architectural feature of a technology stack (shared upstream dependency on a small number of foundation model providers) creates systemic coupling that an insurance protocol designed for independent-loss events cannot handle at the policy level. This is a clean example of what I have been calling "outer environment mismatch" — the protocol (individual-policy insurance) was designed for an outer environment (loss independence holds across the book) that no longer obtains when the insured population shares a common upstream dependency. The protocol isn't broken; its operating assumptions have been violated by a change in the outer environment.

**The Tier 4 disaggregation move as a method.** The paper's refusal to lump "outside conventional insurance" into a single category — and instead asking which specific criterion fails for each case — is exactly the kind of analytical discipline I need to apply to protocol failure modes. I have been categorizing protocol failures by symptom (ossification, drift, fragmentation) rather than by which structural property fails. The lethal-trifecta / AI-washing / foundation-model-concentration distinction maps onto: (1) failure of fortuity/randomness assumption, (2) failure of intentional-act exclusion coherence, (3) failure of independence assumption. Each requires a different institutional response. This is a usable framework for classifying protocol failure modes by which structural assumption is violated.

---

## 8. Candidate Laws

**Candidate: Coverage-causation ambiguity accelerates bifurcation.** When a new risk category creates causal attribution ambiguity — the same loss can be plausibly attributed to multiple existing coverage categories simultaneously — the institutional response is bifurcation: the market simultaneously creates affirmative products for the new category and adds exclusions to existing legacy lines, with the ambiguous/silent zone shrinking as both boundaries advance. The mechanism: ambiguity creates claim disputes that are expensive for all parties, and the resolution is to make the coverage status explicit in either direction. The silent cyber → AI coverage trajectory supports this, as does the NotPetya precedent cited in the paper.

*What text says:* "The rapid 2025 to 2026 development of both affirmative AI products and AI-specific exclusions tracks the silent-cyber bifurcation closely" [text, p.2]; "the AI insurance market is not merely expanding or contracting. It is sorting AI risk by peril." [text, p.2]

*Candidate formulation:* When a new risk instrumentality creates sufficient causal attribution ambiguity across existing policy lines, the market resolves the ambiguity through bifurcation — simultaneous affirmative product creation and legacy exclusion propagation — rather than through legacy line expansion alone.

*What would falsify it:* A case where a new risk instrumentality with comparable cross-line attribution ambiguity is resolved by legacy line expansion (cyber lines absorbing everything) rather than bifurcation, without creating affirmative niche products or explicit exclusions.

*Confidence:* speculative — two instances (silent cyber, emerging AI) are not structurally independent (same industry, same Lloyd's market coordination mechanism), and the mechanism needs sharper articulation.

**Candidate: Loss independence as the binding constraint for market-level structures.** Private insurance markets can handle correlated loss if the correlation has an exogenous, observable trigger and a measurable severity scale. They cannot handle correlated loss generated by a shared upstream dependency without an observable trigger or natural severity scale. The market response requires moving from policy-level to market-level instruments (pools, ILS, government backstops) in a predictable sequence determined by the coordination and data requirements of each instrument.

*What text says:* "criterion (iii) loss independence fails sharply, because by construction every cedent using the failed upstream model experiences claim conditions simultaneously" [text, p.10]; the sequence from private ordering → captive/RRG → reinsurance pool → ILS → government backstop in Table VI [text, p.10].

*Candidate formulation:* When a shared upstream dependency generates loss correlation across a cedent population without an exogenous observable trigger, private per-policy insurance fails, and the market formation sequence is determined by the increasing coordination and data requirements of alternative structures.

*What would falsify it:* A case where per-policy insurance successfully priced and held shared-upstream-dependency correlation without requiring market-level structural innovation.

*Confidence:* candidate — the mechanism is clear (correlation violates the actuarial independence assumption), but this is essentially the classical argument for why catastrophe markets require pooling/ILS/government backstops, extended to a new type of correlation. Need to check whether it adds anything beyond what CAT insurance theory already establishes.

---

## 9. What Surprised Me / What Doesn't Fit

**The lethal trifecta having no affirmative coverage cells anywhere.** The trifecta (T-40) is coded S across all 26 products — not affirmative anywhere, not explicitly excluded by most. [text, p.8, Appendix A] The paper treats this as unsurprising (it's architectural, not insurable in the conventional sense), but it's actually quite striking: the root cause of many of the insured perils (prompt injection, indirect prompt injection, data theft via agent) is architecturally produced by a configuration that no carrier has decided to price directly. Coverage exists for the downstream losses (T-01, T-02) but not for the upstream architectural condition that generates them. This is an interesting gap in the coverage logic — you can insure the flood damage but not the fact that the building was constructed in a floodplain.

**The paper's own uncertainty about the migration hypothesis.** The authors present two strong counterarguments to their own hypothesis that prompt-injection events might migrate from cyber lines into AI-specific affirmative cover [text, p.9]. They ultimately flag it as "worth tracking rather than a prediction." This is more honest than most papers, but it also reveals that they don't know what the causal mechanism for migration would be. If cyber lines have historically absorbed novel attack vectors rather than shedding them (ransomware, BEC, supply chain), why would prompt injection be different? The paper doesn't have a satisfying answer. The structural question — what determines whether a new attack class stays in cyber vs. develops its own coverage line — is actually the more interesting research question than the prediction itself.

**The companion paper finding buried in limitations.** Reference [58], "Coverage Without Casualties?", notes that affirmative coverage breadth bears little relation to observed incident frequency: model drift has seven affirmative coverage cells but zero recorded incidents; deepfake fraud is the most frequent recent peril but has only three affirmative coverage cells. [text, p.12] This is mentioned as a limitation of the current paper, but it's actually a very sharp finding: the market is pricing and insuring against threats based on their theoretical severity or tractability rather than their empirical frequency. The coverage structure reflects what *can* be underwritten (tractable perils with assessable severity) rather than what *is* happening (frequently occurring incidents). This inversion deserves more attention than a footnote in the limitations section.

**The coding scheme tension the paper acknowledges but doesn't resolve.** The marketing-grade naming rule (if a carrier says "covers hallucination," code it affirmative) is "in unavoidable tension with the silent-cyber thesis that motivates this paper: the entire point of distinguishing affirmative from silent coverage is that marketing language and contract wording can diverge." [text, p.4] The authors adopt the rule for replicability and explicitly call the affirmative cell count an "upper bound." This is honest, but it means the paper's primary contribution — the matrix — is measuring something adjacent to but not identical with actual coverage. The paper knows this. It's the right call given available data, but it means all the downstream analysis is conditional on this epistemic compromise.

---

## 10. What It Opens

**The coverage-incidence inversion finding** in the companion paper [58] is worth reading: if affirmative coverage tracks tractability and severity rather than empirical frequency, this is a systematic bias in how nascent insurance markets price novel risks. Does this bias correct over time as claims experience accumulates, or does it persist? The SolarWinds analogy the paper draws (software supply chain failures haven't produced insurance-market-defining events) is relevant here — maybe low-frequency/high-severity events get covered before high-frequency/low-severity events become claims, even when the latter are actually occurring.

**The causal attribution problem as a general protocol design issue.** When a new instrumentality creates causal attribution ambiguity — the same loss can be described under multiple existing protocol frames simultaneously — how do institutional systems resolve the ambiguity? The silent cyber → AI trajectory suggests bifurcation as one resolution mechanism. Are there others? Does the resolution depend on the speed of the attribution ambiguity's growth relative to the institutional coordination capacity? This connects to the Rittel/Webber wicked problems tradition I have listed as unread — need to read that.

**The lethal trifecta as a protocol design constraint.** The claim that "95% filter accuracy is a failing grade" in security-critical contexts [text, p.5] and that the only deterministic defense is architectural (cutting one of the three legs) is a general statement about a class of protocol vulnerabilities: those produced by the combination of three capabilities that are individually benign but collectively deterministically exploitable. This is structurally interesting — a law about irreducible vulnerability in multi-capability systems. Related to Simon's near-decomposability: a system where three components interact to create deterministic exploitability cannot be made safe by improving any single component in isolation; the architecture must be changed. Worth formalizing as a candidate for the protocols inventory.

**The market formation sequence** in Table VI — from private ordering through government backstop — deserves comparison with the sequence for other historically novel risk classes. Did terrorism insurance (TRIA) follow the same sequence in compressed time? Did pandemic risk? If there's a general sequence law here, it would be: the formation sequence is determined by the decreasing marginal information requirement and increasing marginal coordination requirement as you move from private contracts to government backstops.

*Texts to track down:*
- Romanosky et al. (2019) on cyber insurance pricing and claims data [reference 49] — this is the empirical base for understanding how nascent insurance markets price novel risks.
- Talesh (2018) on insurers as "compliance managers" [reference 50] — the mechanism by which insurance underwriting translates into de facto regulation is directly relevant to how protocol standards propagate.
- Baker and Shortland on ransomware/government backing [reference 51] — government backstop formation logic.
- The Rittel/Webber 1973 paper I have flagged unread — the attribution ambiguity question connects directly to the wicked problems thesis.
