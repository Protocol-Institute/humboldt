# Deep Read Notes: Arxiv 2606.18479

*Source: `bibliography/deep-reads/arxiv-2606.18479.pdf`*

---

## Reading session: full document (28 pages)

# Deep Read: Scarone & Baeza-Yates, "The Illusion of Improvement" (arXiv 2606.18479)

---

## 1. Gestalt

This paper is about a specific and nasty kind of protocol failure: when the measurement system that tells you a protocol is working is structurally coupled to the protocol itself in a way that makes deterioration look like improvement. The domain is credit scoring — iterative model-based lending — but the authors are really documenting a general class of feedback loop where selection produces the training data, and the training data shapes selection, and the evaluation metrics are computed on the surviving population rather than the full population. The animating problem is not "how do we build better credit models" but "why would a competent practitioner, following standard evaluation protocols, rationally choose the worst possible strategy?" The answer they find is that standard evaluation metrics — accuracy, precision, recall — are not merely noisy under survival bias; they are *structurally biased* toward strategies that amplify the bias. The paper earns its title: the improvement is real by the metric, and the metric is wrong. This is a contribution to understanding how protocols can embed their own failure modes into their governance mechanisms.

---

## 2. Argument and Structure

**Core claim:** In iterative model-based lending, survival bias creates a feedback loop where:
1. The model rejects applicants it classifies as risky
2. Only accepted applicants' outcomes are observed
3. The training data therefore progressively underrepresents defaulters
4. The model retrains on this impoverished distribution
5. Standard metrics (accuracy) improve because the model now faces a more homogeneous, easier problem — not because it's solving the real problem better

**The Oracle Paradox** is the load-bearing example. A model with access to all true labels — the theoretically optimal information state — consistently *underperforms* on accuracy and recall compared to Simple Extrapolation, which has no true labels at all and just assumes all rejected applicants would have defaulted. This inversion is not noise; it's structural. The explanation: Oracle introduces genuine label diversity, making the learning harder; Extrapolation creates a self-reinforcing feedback loop that inflates the training default rate, making the model increasingly aggressive, improving performance on the increasingly skewed evaluation population while diverging from the true population distribution.

**The formal backbone** (Section 4.2, Appendix D) is elegant and minimal:
- Lemma 1: Accepted applicants default less than the population (proved from informative screening assumption)
- Proposition 1: Therefore training default rate deflates after each retraining cycle
- Proposition 2: Accuracy decomposes as `(1−π_t)·spec + π_t·rec`; as π_t falls, recall's contribution to accuracy shrinks toward zero, so accuracy and recall decouple

This is not a simulation artifact — the authors derive it analytically and then confirm it empirically across three datasets and two model families.

**The proposed fix** is controlled exploration: deliberately approve a fraction `r` of rejected applicants and observe their true outcomes. The key finding: even 2–5% exploration is sufficient to *diagnose* the severity of the feedback loop, at near-zero cost in terms of accuracy degradation. The diagnostic zone is `r ∈ [0.01, 0.05]`.

**Most confident:** The formal results and the Oracle Paradox. The mathematical derivation is clean; the empirical confirmation is consistent across six configurations (3 datasets × 2 models).

**Most speculative:** The scale-to-other-domains generalization (predictive policing is cited but not analyzed), and the claim that controlled exploration is practically deployable — the authors acknowledge regulatory and ethical constraints they do not address.

---

## 3. Conceptual Vocabulary

**Survival bias / survivorship bias** [text, p.2]: Selection bias arising from observing only outcomes of those who "survived" (passed) the selection criterion. Here: we see repayment outcomes only for accepted applicants, never for rejected ones. Not new as a concept, but applied here specifically to iteratively self-reinforcing model-driven selection.

**Reject inference (RI)** [text, p.3]: The family of techniques attempting to recover missing outcome information for rejected applicants — probabilistic imputation, extrapolation, nearest-neighbor transfer, etc. The paper treats these as a protocol class and evaluates them as such.

**Kickout (KO)** [text, p.5, Eq. 1]: `(true_defaulters_rejected − true_non-defaulters_rejected) / (true_defaulters_rejected + true_non-defaulters_rejected)`. A rejection quality metric ranging [-1, 1]. KO = 1: every rejection is a true defaulter. KO = 0: rejections are no better than random. KO < 0: actively rejecting creditworthy applicants. This is the paper's contribution to measurement — the metric that escapes the circularity that accuracy, precision, and recall cannot.

*Tension with my vocabulary:* The Kickout metric is interesting because it is evaluated on the full applicant pool, not just the accepted population. This makes it partially immune to the feedback loop. But it still depends on knowing true labels for the rejected applicants who were accepted during exploration — which is precisely what normal operations don't provide. So KO is only measurable in a controlled exploration context, not in standard deployment. The paper uses it as both a performance target and a diagnostic, but conflates these somewhat.

**Training Default Rate (TDR)** [text, p.4]: The proportion of defaulters in the training set at each iteration. The key diagnostic: divergence from the population default rate measures the degree of distributional distortion. This is the only metric evaluated in the paper that the model cannot influence — it measures training data composition against a known external reference.

**Oracle Paradox** [text, p.10]: The finding that a model with access to all true labels consistently underperforms on standard metrics compared to Simple Extrapolation. Named by me; the paper doesn't name it explicitly.

**Diagnostic zone** [text, p.14]: `r ∈ [0.01, 0.05]`, exploration rates at which the presence and severity of survival bias can be diagnosed without materially harming accuracy performance.

**Performative prediction** [text, p.3, citing Perdomo et al. 2020]: Model deployment shifts the data distribution that future models are trained on. The paper situates its work explicitly in this literature.

---

## 4. Analytical Moves

**The circularity test:** Ask whether the evaluation metric is computed on a population that the evaluated strategy itself shaped. If yes, the metric cannot distinguish genuine improvement from selection-induced homogenization. Applied here: accuracy and recall are computed on the accepted population, which the model selected. Therefore they cannot detect when the model is solving an easier problem of its own construction rather than the original problem.

*This is a general analytical move, not specific to credit scoring. Any protocol that governs a population and is evaluated on that population faces the same structural vulnerability.*

**The inversion move:** When the full-information baseline (Oracle) underperforms a no-information-access strategy (Simple Extrapolation), this is not a statistical anomaly but a diagnostic signal about the evaluation framework. More information yielding lower measured performance means the metric is not measuring what you think it is. Invert: what would have to be true about the metric for this ranking to be correct?

**The population-anchor diagnostic:** Identify a metric whose reference point is external to and independent of the selection process. Here: TDR compared to the known population default rate. The model cannot influence the population default rate; therefore TDR is the only metric that escapes the feedback loop. More generally: in any evaluation-under-selection-bias scenario, hunt for a metric anchored to a reference the selection process cannot reach.

**The symmetric distortion test:** Scarone & Baeza-Yates notice that Biased deflates TDR by ~22% relative to population rate, and Extrapolation inflates it by ~22% — symmetric distortions in opposite directions [text, p.10]. This symmetry is itself informative: it suggests Extrapolation is not correcting survival bias but reversing its sign, substituting one distributional distortion for another. Look for symmetric distortions as evidence that a "correction" strategy is inverting rather than fixing.

**The diagnostic zone identification:** Given a continuous intervention parameter (here: exploration rate `r`), find the regime where the signal about the underlying pathology is maximally informative while the cost in operational performance is minimal. The authors find this at `r ∈ [0.01, 0.05]`. The general form: when full correction is too costly to deploy, find the minimum perturbation that reveals whether you're in a pathological regime.

---

## 5. What It Says About the Nature of Things

**Metrics are not neutral observers; they participate in the dynamics they measure.** The deepest lesson here is not about credit scoring — it's about what happens when the measurement protocol is designed without accounting for the fact that the system under measurement shapes its own evaluation population. Accuracy is not a bad metric in general; it becomes pathological specifically when the selection process that the metric evaluates is the same process that determines what the metric is computed on. The feedback loop is between the protocol and its governance, not just internal to the protocol.

**Apparent improvement can be structurally guaranteed by the feedback loop itself.** The paper proves, not just shows, that accuracy will tend to rise as recall collapses under iterative biased retraining. This is not bad luck or poor design — it follows mathematically from (a) the model screens informatively, (b) only approved outcomes are observed, (c) evaluation is on the approved population. Any lender following standard practices in this regime will experience measured improvement while actual performance degrades. The improvement is an artifact, but it is a *structural* artifact — guaranteed by the setup.

**Optimizing against the wrong metric is not a failure of rationality; it is a protocol failure.** The paper's practitioners are behaving rationally: they observe accuracy improving, they choose the strategy that maximizes accuracy. The problem is not their reasoning — it is that the evaluation protocol they inherited does not measure what matters. This distinction is important: the failure is upstream of the decision, in the protocol design, not in the decision itself.

**The scale modulates severity, not structure.** Larger training sets buffer against the feedback loop (LendingClub: 2.6% TDR distortion; Default: 30%). The qualitative patterns are identical; the magnitudes compress. This is exactly what we'd expect from a structural mechanism: the mechanism is the same, the parameters set the rate.

---

## 6. What It Says About Becoming a Better Researcher

This text is a technical paper, not a research-methods text. But several methodological commitments are visible:

**The authors did not accept that standard metrics were adequate.** They could have run a standard RI comparison and been done. The insight that standard metrics are structurally inadequate required asking a second-order question: what does the evaluation framework itself assume, and when are those assumptions violated? This is exactly the kind of question Hamming (in my reading of that text) would identify as the "next level up" from the standard framing. [Connects to M-016: the disposition to ask whether the evaluation framework is adequate, not just whether the results are significant.]

**They invented a metric (Kickout) rather than accepting the existing ones.** When the existing evaluation vocabulary is systematically misleading, the right move is not to report caveats — it is to construct the metric that measures what you actually care about. This is an instance of Iverson's notation-as-tool-of-thought principle [from my LINEAGE.md reading]: the representation determines what you can see.

**The formal structure was used to explain, not just confirm.** The Propositions and Lemmas in Section 4.2 don't just verify that the simulation results are real — they explain why they are necessary, given the setup. The formal result converts an empirical observation into a structural claim. This is the difference between a paper that shows something and a paper that shows *why* it must be so.

**The Oracle Paradox was not buried in a footnote.** The fact that the full-information baseline underperforms is genuinely surprising and potentially embarrassing to the standard evaluation framework. The authors name it, center it, and make it the paper's sharpest result rather than treating it as an anomaly to be explained away. This is intellectual courage about counterintuitive findings — relevant to M-016's emphasis on not filtering out surprising observations.

---

## 7. Where It Touches My Research

**Direct relevance to protocol self-measurement failure.** The paper documents a specific mechanism by which a protocol's governance system (evaluation metrics + retraining cycle) can become coupled to the protocol's operations in a way that makes pathological states look healthy. This is a concrete instantiation of a class of failure I've been circling: protocols that embed their own evaluation criteria in ways that cannot detect their own degradation.

**Connection to the 2026-06-17 Discord idea (from inbox):** "Systems represent possible futures implicitly through their error-correction mechanisms — the futures a protocol guards against are visible in what constraints it enforces." This paper is an example of that logic inverted: the credit scoring protocol implicitly represents a future (applicants who would have defaulted if approved) through its rejection mechanism. But because those futures are never actualized, the protocol cannot observe whether its model of them is deteriorating. The possible futures that the protocol guards against are structurally invisible to its governance layer.

**The population-anchor diagnostic** is directly relevant to my general research program. Any system that both governs a population and is evaluated on that population faces this structure. Candidate domains: predictive policing (cited in the paper), parole/bail algorithms, content moderation systems, hiring algorithms, standardized test score cutoffs. The question: in which of these is there an analog of TDR — a metric anchored to a reference the system cannot reach?

**Metric capture as a protocol failure mode.** This paper gives a concrete mechanism for how protocols can develop what I might call "metric capture" — the evaluation criteria drift to measure what the protocol produces rather than what the protocol was designed to produce. This is related to Goodhart's Law but is structurally different: Goodhart's Law is about gaming (agents optimize the metric rather than the goal); this is about structural coupling (the evaluation method is computed on the population the protocol shaped, not the population it's supposed to serve).

---

## 8. Candidate Laws

**Candidate: Evaluation Population Capture**

[text, pp. 7, 10-12] Scarone & Baeza-Yates show that when (a) a selection-making protocol is evaluated on the population it selected, and (b) the protocol screens informatively, then standard classification metrics will systematically reward strategies that increase selection stringency, regardless of whether that stringency reflects genuine signal about the full population. The Oracle Paradox demonstrates this: more information yields lower measured performance because the evaluation population becomes harder precisely when information is more complete.

**Candidate formulation:** A selection protocol evaluated on its own output population will systematically reward strategies that narrow and homogenize the evaluation population over strategies that maintain distributional fidelity to the target population, even when the latter strategies have strictly superior information access.

**What would falsify this:** A selection protocol evaluated on its own output population that correctly identifies and penalizes strategies which narrow the evaluation population, without requiring metrics specifically designed for this purpose. Or: a setting where standard metrics and TDR-analog give the same recommendations under iterative retraining with informative screening.

**Confidence:** candidate. Two structurally independent domains are cited (credit scoring, predictive policing [external, Ensign et al. 2018]). Mechanism is formally stated. Needs cross-domain verification outside financial/criminal justice contexts.

---

## 9. What Surprised Me / What Doesn't Fit

**The most surprising thing is the formal proof.** I expected an empirical paper. The derivation of the accuracy-recall decomposition and the proof that TDR deflation is monotone under informative screening is clean and unexpectedly strong. It converts what could have been a dataset-specific curiosity into a structural claim. The proof doesn't require any properties of the model except that it screens informatively (A5) — which means the result is model-agnostic.

**The paper underexplores the deeper diagnostic implication of TDR.** TDR works as a diagnostic precisely because it's anchored to the population default rate, which the model cannot change. This is noted but not theorized. The authors treat it as a practical diagnostic tool; I think it's a more general principle: every evaluation-under-selection-bias problem needs at least one metric anchored to a reference the selection process cannot reach. The paper discovers this but doesn't name it as a design principle.

**Simple Extrapolation is not really a reject inference strategy.** The authors note this: Extrapolation "does not mitigate survival bias but reverses its sign." They observe that it "substitutes one distributional distortion for another, casting doubt on whether it should be considered an RI strategy at all" [text, p.10]. But it's in the comparison anyway, and it "wins" by every standard metric. This is a useful case of a protocol that satisfies the formal criteria for membership in a category (RI strategy: imputes labels for rejected applicants) while systematically working against the category's purpose.

**The regulatory constraint acknowledgment is too brief.** Controlled exploration requires deliberately approving some applicants you expect to default, in order to observe whether your model is calibrated. The ethical and regulatory issues with this are substantial — you're knowingly issuing loans you predict will fail, to people who will suffer the consequences. The paper mentions this in the Limitations section in one sentence. For a paper that frames itself in terms of EU AI regulation, this is a gap.

**The connection to performative prediction is underdeveloped.** The paper cites Perdomo et al. 2020 once [text, p.3] and doesn't return to it. The framing of performative prediction — model deployment shifts the data distribution — is exactly the right theoretical home for this paper, but the authors don't develop the connection. There's a stronger paper here that situates this work explicitly in that literature and shows what the credit-scoring case adds.

---

## 10. What It Opens

**Live questions:**

1. Where else does the evaluation-population-capture mechanism operate? Predictive policing (cited, Ensign et al. 2018) is the obvious one. But: content moderation (posts that the moderation model flags are removed, so the training data for the next model is the set of posts that survived), bail/parole algorithms, hiring screening systems. The mechanism requires only: (a) iterative deployment with retraining, (b) outcomes observable only for the accepted population, (c) evaluation on the accepted population. This is a surprisingly common structure.

2. Can the TDR-analog principle be generalized? The paper discovers that TDR works because it's anchored to a reference (population default rate) the selection process cannot reach. Is there a general design criterion for evaluation metrics in selection-protocol contexts? Something like: "a valid evaluation metric for an iterative selection protocol must have at least one reference point outside the selected population."

3. What is the relationship between this and Goodhart's Law? Goodhart: "When a measure becomes a target, it ceases to be a good measure." This paper: the measure never became a target — the practitioners were trying to improve loan portfolio quality, not accuracy — but the measure still ceased to be a good measure because of the structural coupling between the selection process and the evaluation population. This suggests a class of metric-degradation failures that are distinct from Goodhart's Law and may be more insidious because they don't require anyone to be gaming the metric.

**Texts worth reading:**

- Perdomo et al. (2020), "Performative Prediction" — the theoretical home for this paper; I should read the original
- Ensign et al. (2018), "Runaway Feedback Loops in Predictive Policing" — the cleanest cross-domain instance of the same mechanism
- Selbst et al. (2019), "Fairness and Abstraction in Sociotechnical Systems" — the broader framing of how ML evaluation frameworks can be structurally inadequate (this is in the fairness literature, which has grappled with this more explicitly than the ML systems literature)

**A tradition worth exploring:** The "performative prediction" literature (Perdomo et al., Hardt, Zrnic) is studying exactly the class of systems where model deployment changes the distribution the model was trained on. This is a natural home for the structural observation in this paper, and might already have the generalization I'm reaching toward.
