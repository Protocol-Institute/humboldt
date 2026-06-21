# Deep Read Notes: Arxiv 2606.14533

*Source: `bibliography/deep-reads/arxiv-2606.14533.pdf`*

---

## Reading session: full document (27 pages)

# Deep Read: Tembine, "The Risk Shadow of Principal Component Analysis" (arXiv:2606.14533)

---

## 1. Gestalt

This paper is animated by a single, structurally sharp observation: the optimization objective of PCA — variance maximization — and the optimization objective of consequential decision-making — minimizing tail risk on rare, costly events — are not merely different but can be *provably orthogonal*. The author's central claim is not that PCA is wrong but that it solves the wrong problem when downstream stakes are asymmetric. PCA finds the subspace of maximal variance; the information needed to detect rare catastrophic events may reside *entirely* in the discarded complement. The paper proves this formally, names the phenomenon (the Risk Shadow), introduces an alternative framework (exp2PCA) that directly optimizes the expectile of misclassification cost, and validates on synthetic and real-world benchmarks. What makes this paper worth reading beyond its technical claims is the underlying epistemological move: it asks what metric a representation should be evaluated by, and answers that the metric must be derived from the downstream consequences, not from the geometry of the data itself.

---

## 2. Argument and Structure

**Core claim:** Variance preservation and decision-relevant information preservation are structurally incompatible objectives. PCA can retain >99.9999% of variance while retaining *zero* mutual information about rare target classes — this is not a numerical accident but a theorem.

**The construction [text, pp. 4-5]:** The latent-factor model is the argument's load-bearing example. Class labels Y are generated from *minor* eigenvectors (the discarded subspace S_R), while the major eigenvectors explain nearly all variance. Since Y is a function of z_{r+1,...,d} and these are independent of z_{1,...,r}, the PCA representation contains zero information about Y. Theorem 1 (Information Erasure) makes this formal. Theorem 2 (Bayes Collapse) shows that the optimal classifier on the PCA representation is a *constant predictor* — it doesn't matter what the data says.

**The Risk Shadow [text, pp. 2, 6]:** Definition 6 names the phenomenon: a representation induces a Risk Shadow if I(Y; Ψ(X)) = 0 yet high nominal accuracy is achievable by a constant predictor. This is the key move — it explains why the failure is invisible to standard metrics. The 99.9999% variance retained looks excellent. The 99% accuracy looks excellent. The tail risk is catastrophically wrong, and neither standard metric surfaces this.

**The hierarchy of alternatives [text, pp. 5-6, 11-14]:**
- *TP-PCA* (reweight rare-class samples): fails in both worked examples because the centering correction (μ_w μ_w^T) suppresses the discriminative variance component regardless of how aggressively you weight. There is no valid α that can rescue TP-PCA in Example 2. [text, p.13]
- *exPCA* (minimize expectile of reconstruction error): partially works — as τ→1, the weight function concentrates on reconstruction extremes, which are driven by rare-class samples. It recovers some rare-event information without supervision. But it's still geometric rather than task-aligned.
- *exp2PCA* (minimize expectile of misclassification cost directly): uniquely solves the problem because it optimizes the actual downstream objective. Theorem 6 (Strict Dominance) proves it outperforms PCA under the information erasure + subspace discriminability conditions.

**Where the author is most confident:** The information erasure theorems (1, 2, 3) are crisp and the proofs are clean. The failure of TP-PCA is analytically derived, not just empirically observed — the centering penalty is shown to dominate regardless of α. [text, pp. 12-13]

**Where the author is most speculative:** The extension to Mean-Field-Type Games (Section VIII) is more programmatic than developed — it introduces vocabulary and frames a multi-agent version of the problem but proves no substantive new results. The connection to "responsible machine intelligence" in Section VII has rhetorical energy but the three accountability metrics (RPB, RIM, RLD) are defined without much worked analysis.

**Acknowledged limits [text, p.25]:** The author explicitly states PCA is not obsolete, that variance maximization remains excellent for compression/visualization/exploration, and that the claim is narrower: "when dimensionality reduction serves as a precursor to consequential decision making, variance alone is generally an insufficient design principle."

---

## 3. Conceptual Vocabulary

**Risk Shadow [text, pp. 2, 6]:** A representation that preserves nearly all variance while retaining zero mutual information about rare high-impact classes. The "shadow" is the zone of feature space where standard performance metrics (accuracy, variance explained) appear excellent while tail risk is unbounded. Key feature: the shadow is invisible to conventional auditing.

*Tension with my vocabulary:* I don't have a prior term for this. The closest thing I have is "Goodhart's Law" (optimizing a proxy metric decouples it from the target), but the Risk Shadow is more specific — it's a geometric proof that the proxy and target metrics can be orthogonal under natural conditions, not just decoupled under optimization pressure.

**Expectile [text, p. 5, Definition 1]:** An asymmetrically weighted quadratic analog of a quantile. The τ-expectile minimizes E[|τ - 1_{u<0}| * (W-t)^2]. As τ→1, eτ(W) → ess sup(W). Properties claimed: coherent (under conditions), elicitable, differentiable, tail-sensitive. The author uses this rather than CVaR because it is differentiable and thus amenable to gradient-based optimization.

*Note:* The author treats the expectile as nearly synonymous with tail risk throughout, which is accurate for τ→1 but obscures that the expectile is a specific parameterization of tail sensitivity, not a universal definition of it.

**Information Erasure [text, pp. 5, 17]:** The condition I(Y; P^T X) = 0 — the representation contains *zero* information about the label. This is the extreme case. The paper proves conditions under which PCA achieves this exactly, not approximately.

**Risk-weighted covariance (Στ) [text, p. 6, Proposition 1]:** The covariance matrix exPCA effectively optimizes — it reweights observations by their reconstruction error extremality. As τ→1, this concentrates all weight on reconstruction outliers, which are driven by rare-class samples.

**Subspace truncation risk gap [text, p. 19, Definition 10]:** The excess tail risk incurred by compressing from d dimensions to r dimensions, even with the best possible rank-r projection. This is the irreducible information loss due to dimensionality reduction.

**Representational Price of Blindness / Accountability Index [text, pp. 20-21]:** Multiplicative ratios comparing PCA tail risk to exp2PCA tail risk, and PCA tail risk to full-feature-space tail risk. Framing devices more than deep results.

---

## 4. Analytical Moves

**The latent-factor worst-case construction [text, p. 4-5]:** To prove that PCA can fail maximally, construct a distribution where labels live entirely in the discarded subspace. This is the methodological move that does the most work in the paper. The construction is parametric: Y = g({z_j}_{j∈M}) where M ⊆ {r+1,...,d}. This forces the worst case analytically rather than finding it empirically. Transferable as: *to show a method can fail, construct the distribution that perfectly exploits its optimization objective's blind spots.*

**The diagonal geometry check [text, pp. 12-13]:** In Examples 1 and 2, the covariance matrix is diagonal by construction, so the PCA direction is obvious (horizontal axis). The rare-class signal is on the orthogonal axis. This makes the failure mode analytically transparent. Transferable as: *choose a worked example where the solution is geometrically obvious in order to make the failure mode structurally clear rather than numerically contingent.*

**The centering-penalty trap [text, pp. 12-13]:** The proof that TP-PCA fails not just in practice but in principle — no α can rescue it — uses the specific structure of the weighted covariance. The mean shift μ_w μ_w^T grows faster than the variance gain from upweighting rare samples. This is a structural impossibility result, not a parameter tuning failure. Transferable as: *when a method fails, ask whether the failure is contingent (wrong parameters) or structural (wrong objective) — the latter is more interesting.*

**The constant-predictor collapse argument [text, p. 6, Theorem 2]:** If the representation contains zero information about Y, then the optimal classifier is a constant predictor — it doesn't matter what z says, predicting the prior is as good as any function of z. This argument is clean and general. Transferable as: *I(Y; representation) = 0 implies the classifier degenerates to a prior — any downstream performance from such a representation is due to base rates, not information.*

**Asymptotic regime analysis (τ→1) [text, throughout]:** The paper repeatedly takes τ→1 to isolate the extreme tail regime. In this regime, the expectile converges to the essential supremum, and the weighted covariance concentrates on reconstruction extremes. This limit often makes proofs tractable. Transferable as: *asymptotic regime analysis to isolate the structure of a phenomenon by pushing a parameter to its extreme.*

---

## 5. What It Says About the Nature of Things

**Proxy metric failure is structural, not accidental.** The deepest claim here is that variance and decision risk are not just different metrics that can drift apart — they are defined over fundamentally different objects (unconditional second moments vs. conditional decision losses). Nothing in the PCA objective incorporates labels, costs, or asymmetries. The failure is not a bug in PCA; it is the consequence of using a label-free objective for a label-dependent problem. [text, p. 1]

This generalizes: *any unsupervised objective will have a shadow region where the supervised objective is orthogonal to it.* PCA is the clearest case because its solution is fully characterized (leading eigenvectors), but the principle extends to any representation learning method that optimizes a label-free criterion.

**The most important signal is often the rarest.** [text, p. 2] The events that define institutional liability — fraud, medical diagnosis, safety failures — are structurally low-variance because they are rare. Variance-maximizing methods systematically discard exactly this information. This is not a technical limitation; it is a consequence of how variance is defined. The paper frames this as an ethical issue in Section VII, but the underlying claim is epistemic: *the geometry of importance (measured by stakes) and the geometry of variance (measured by dispersion) are decoupled and can be orthogonal.*

**High accuracy is not a proxy for safety.** The worked example makes this vivid: 99.9999% variance retained, ~99% accuracy, and the classifier is entirely useless for detecting the event that matters. This is a structural warning about audit regimes that rely on aggregate performance metrics. [text, pp. 2, 18]

**Representation choice is a decision, not preprocessing.** The paper's framework treats the choice of projection matrix as a strategic variable — part of the problem, not upstream of it. This reframes dimensionality reduction from a compression step to a decision step with accountability implications. [text, p. 3, Section VIII]

---

## 6. What It Says About Becoming a Better Researcher

This is primarily a technical paper, so this section is thinner than usual — but there are substantive lessons.

**The wrong objective, rigorously pursued, yields catastrophic results.** [text, pp. 1-2] PCA is not wrong; it is spectacularly optimal at what it was designed to do. The failure comes from deploying it in contexts where its optimization objective diverges from the operational goal. This is a lesson about research scope: always ask what objective you are actually optimizing and whether it aligns with what matters. An elegant solution to the wrong problem is dangerous precisely because the elegance is seductive.

*M-016 connection:* This is a version of Hamming's important-problem principle applied at the level of objective function rather than research agenda. Not "am I working on an important problem?" but "is the objective I am optimizing aligned with what actually matters in this problem?"

**Structural impossibility is more valuable than parameter failure.** The paper's cleanest contribution is proving that TP-PCA cannot be rescued by any value of α — not that it performs poorly in practice with typical α values. This transforms a tuning problem into a structural result. [text, pp. 13-14] The lesson: when investigating a method's failure, hunt for the structural explanation, not the parameter explanation. Structural failures generalize; parameter failures are local.

**Limit cases and extreme regimes reveal structure.** The τ→1 analysis throughout the paper shows that asymptotic regimes often admit cleaner proofs and more transparent structural insights than moderate-parameter regimes. When a phenomenon is hard to analyze at a typical operating point, pushing a parameter to its limit often clarifies what is essential. [text, throughout]

**Make the failure mode geometrically visible.** Examples 1 and 2 are constructed so that the PCA failure direction (horizontal) and the discriminative direction (vertical) are orthogonal and obvious. This is not cheating — it is pedagogy. A worked example that makes the failure mode transparent is more valuable than an empirical study where the failure might be attributable to any of a dozen factors.

---

## 7. Where It Touches My Research

**The Risk Shadow as a general protocol phenomenon.** [inference] The Risk Shadow describes what happens when a system optimizes a proxy metric that is structurally decoupled from the operational objective. This is not specific to PCA — it describes any protocol where the evaluation criterion and the performance criterion are defined over different objects. In protocol design: a protocol optimized for throughput (the "variance" of data transmission) may completely destroy the information needed to detect rare but catastrophic failures (the "rare class"). The protocol passes every benchmark while harboring a shadow.

*Specific connection to candidate law territory:* The Risk Shadow is structurally related to Goodhart's Law (when a measure becomes a target, it ceases to be a good measure), but it is more precise. Goodhart's Law describes decoupling under optimization pressure. The Risk Shadow describes *structural orthogonality* — the proxy and target can be provably independent even without optimization pressure, when the events that define the target are rare relative to the events that define the proxy.

**Protocols as coordinate systems (Iverson connection).** [inference] The paper demonstrates that the choice of representation is not neutral — it selects which information survives compression. This is Iverson's claim at a different level of abstraction: the representation (here a projection matrix) is a coordinate system that determines what can be expressed and therefore what decisions can be made. PCA's coordinate system preserves the common; the rare vanishes. This is notation lock-in at the data-processing level.

**The inbox item from 2026-06-17 on "possible futures."** [inference, inbox] The Discord idea — "systems represent possible futures implicitly through their error-correction mechanisms" — connects here. The Risk Shadow is precisely a case where the protocol (PCA) has no error-correction mechanism for the rare class because it was never designed to see it. The futures the protocol guards against (reconstruction errors in common cases) are not the futures that matter (rare catastrophic failures). The protocol's error-correction mechanisms reveal its implicit model of what futures are worth attending to.

**The health-check stigmergy idea from 4umd [inbox, 2026-06-18].** [inference] The claim that "health checks function through stigmergy by creating observable problems at regular intervals" — this is the opposite of the Risk Shadow. Health checks are an intervention designed to make rare-but-important events *legible* by forcing them into the observational frequency range. The protocol generates its own signal about rare failure modes by staging encounters with them. This is a possible anti-Risk-Shadow design pattern.

---

## 8. Candidate Laws

**Candidate: The Proxy-Objective Orthogonality Condition**

*What the text says [text, pp. 1-3, Theorem 1]:* PCA can retain >99.9999% of variance while retaining I(Y; Z) = 0. The condition for this is structural: the class label is a function of the minor eigenvectors (discarded subspace), while the major eigenvectors carry nearly all variance.

*Candidate formulation:* In any system that optimizes a proxy objective over a high-dimensional distribution, there exist configurations where the proxy objective and the operational objective (defined over rare, high-impact events) are structurally independent — the proxy can be near-maximally satisfied while the operational metric is near-zero. The conditions for this are: (1) rare events are low-frequency, (2) the proxy is defined over the high-frequency regime, (3) the rare events' signal lives in the complement of the high-frequency regime.

*Falsification:* This law would be falsified by demonstrating that for some natural class of proxy objectives and operational objectives, maximizing the proxy *provably guarantees* a lower bound on the operational metric. The claim requires the conditions above — if rare events co-vary with the high-variance directions, the shadow does not exist.

*Confidence: speculative* — one domain (statistical learning), mechanism stated but cross-domain generality not yet assessed.

*Note:* This is closely related to Goodhart's Law but distinct. I should resist collapsing them — the structural orthogonality result is sharper than Goodhart's decoupling claim.

---

## 9. What Surprised Me / What Doesn't Fit

**The TP-PCA impossibility result is more interesting than the exp2PCA solution.** [inference] The paper's framing presents exp2PCA as the primary contribution. But to me, the deeper result is the analytical proof that *no* amount of reweighting can rescue TP-PCA in Examples 1 and 2. This is because the centering correction grows faster than the variance amplification from upweighting. The implication is general: any method that operates by reweighting within the existing covariance structure cannot escape the geometric trap — it can only be escaped by changing the optimization objective. The paper buries this inside the TP-PCA analysis rather than foregrounding it.

**The Mean-Field-Type Games section is a category error.** [inference, speculative] Section VIII introduces multi-agent formalism to ask whether agents should use PCA or exp2PCA. But the Risk Shadow is a property of representations, not of strategies. Framing it as a game-theoretic problem adds vocabulary without adding insight. The "Risk Shadow equilibrium" (Definition 16) is just the definition of the Risk Shadow applied to multiple agents — there is no new game-theoretic content. This section reads as if written to connect the paper to the author's broader research program rather than to advance the present argument.

**The paper doesn't distinguish between the Risk Shadow as a property of the distribution and as a property of the method.** [inference] The Risk Shadow exists when the method (PCA) is applied to a distribution where the label-relevant information is in the minor eigenvectors. But a distribution can be *designed* to have or lack this property. For most real-world distributions, the assumption that label information lives *entirely* in the discarded subspace is strong. The paper acknowledges this implicitly in the experiments (which show improvement rather than complete recovery) but doesn't theorize the intermediate case.

**The τ parameter is left under-determined.** [text, p. 25] The author acknowledges that selecting τ is "a central challenge" but doesn't provide practical guidance. The paper demonstrates that high τ recovers rare-event information but increases variance of the estimator. This is not a limitation so much as an open problem — but it means exp2PCA as described cannot be deployed without a principled τ-selection procedure, which the paper defers to future work.

**The "890% excess risk" is headline-grabbing but the setup is chosen to produce it.** [inference] The worked example yields 890% excess risk because the cost ratio C_FN/C_FP = 100 and the rare class prevalence is 1%. This is not a natural finding — it is the result of running the theorem with specific parameters (Remark, p. 23). The result is correct but its magnitude is an artifact of the parameter choice. The structural result (non-zero excess risk exists under these conditions) is robust; the magnitude is not.

---

## 10. What It Opens

**Immediate research questions:**

1. Is the Risk Shadow a special case of a more general principle: *any coordination mechanism that optimizes over the common case will accumulate a shadow over rare-but-important cases*? This seems like a strong candidate for a protocol law. Testing requires cross-domain cases: financial clearing protocols that optimize for normal-volume flows, medical protocols optimized for common presentations, network routing protocols optimized for typical traffic patterns.

2. Can the Risk Shadow be detected without knowing the true operational objective? The paper assumes you know C (the cost matrix). But in practice, cost matrices are often implicit or contested. Is there a representation-agnostic signature of Risk Shadow presence?

3. The health-check stigmergy idea (4umd's inbox item) is a candidate anti-Shadow intervention: force rare events into the observational frequency range by staged encounters. What other protocol design patterns serve this function? Are they generalizable across domains?

**Texts to read:**

- Artzner et al. (1999) on coherent risk measures [text, reference 41] — the foundational paper on CVaR and coherent measures, which provides the theoretical backdrop for the expectile approach.
- Newey and Powell (1987) on asymmetric least squares [text, reference 51] — the original expectile paper; understanding the theoretical properties would deepen the reading of this paper's claims about expectile coherence.
- The information bottleneck paper (Tishby, Pereira, Bialek 2000) [text, reference 44] — the information-theoretic approach to representation learning; the Risk Shadow is in some sense the failure mode of information bottleneck methods when the "relevant" variable is rare.

**Traditions to explore:**

- Decision-theoretic statistics: the tradition that treats statistical procedures as explicit decision problems with specified loss functions (Wald, Savage). The Risk Shadow is a decision-theoretic critique of a statistical procedure — understanding the decision-theoretic statistics tradition would clarify what is new here vs. what is restating classical results in new vocabulary.

---

*Pages read: full document, 27 pages. Complete.*
