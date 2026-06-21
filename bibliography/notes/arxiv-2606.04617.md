# Deep Read Notes: Arxiv 2606.04617

*Source: `bibliography/deep-reads/arxiv-2606.04617.pdf`*

---

## Reading session: full document (10 pages)

# Deep Read: arxiv-2606.04617 — "When Firms Learn to Game the Rules"

*He, Xufeng. Agent-Based Reinforcement Learning Simulation of Boundary Search and Adaptive Enforcement. arXiv:2606.04617v1, 3 Jun 2026. 10 pages, complete.*

---

## 1. Gestalt

This paper is animated by a specific worry about a specific reform: Rules-as-Code — the project of making legal obligations machine-readable — is widely praised for reducing inconsistency and improving compliance testing. He asks: but what happens to the firms being regulated? If the rule is now a crisp computable object, firms can now *learn* that object systematically. The paper's central question is whether machine-readable rules make the *boundary* of legality cheaper to find and exploit — not whether they enable violation, but whether they enable the more interesting and legally invisible behavior of clustering just inside the legal line.

The key intellectual move is the **estimand distinction**: separating conduct boundary mass (where firms actually are in risk-space) from signal boundary mass (what the enforcement sensor shows). Without this distinction, a cleaner measurement system could be mistaken for behavioral change, or behavioral change dismissed as measurement artifact. He uses a synthetic ABM/RL simulation not to estimate real behavior but to show that the mechanism — firms learning a computable boundary, imitating profitable edge strategies, regulators adapting, firms re-searching — can generate boundary clustering as a structural dynamic under explicit, inspectable assumptions.

The paper is honest about its scope: it makes mechanism claims, not jurisdiction-specific estimates. The contribution is a *possibility result* — these dynamics can emerge from plausible behavioral primitives — paired with a design-oriented finding: ordinary adaptive rule updates don't fix the problem, but a specific anti-gaming design (randomized audit attention + outcome guardrails, budget-neutral) reduces both conduct boundary mass and harm.

---

## 2. Argument and Structure

**Core claim sequence:**

1. Computable rules reduce the cost of boundary search, not just the cost of compliance. [text, p.1]

2. These effects must be measured separately on conduct (where firms actually are) and on the enforcement signal (what regulators see). Conflating them produces false inferences. [text, p.3, the estimand construction]

3. *Static computability result:* Under computable static rules, conduct boundary mass rises from 0.367 to 0.411 (ambiguous baseline); signal boundary mass rises more sharply, from 0.281 to 0.403. The conduct measure moves *after* the signal-conduct separation is enforced — so this is a real behavioral shift, not measurement artifact. [text, p.4–5]

4. *Ordinary adaptation result:* Adaptive threshold updates reduce consumer harm (0.202 → 0.194) but do not reliably reduce conduct boundary mass (effect: -0.002, CIs crossing zero). Faster updating is not the same as anti-gaming design. The RL regulator makes this vivid: it further lowers harm but produces rule churn of 3.111, far above all other regimes. Learning capacity is not institutional design. [text, p.5]

5. *Anti-gaming result:* Adding randomized audit margins and outcome guardrails (budget-neutral) reduces conduct boundary mass by 0.032 and consumer harm by 0.025 relative to computable static rules. Edge strategies persist (0.868 → 0.802) but the equilibrium shifts — harmful strategies become less attractive, not absent. [text, p.5]

6. *Mechanism decomposition:* Latin-hypercube sensitivity shows computability is the dominant predictor of both signal boundary mass (β=0.972) and conduct boundary mass (β=0.780). Imitation amplifies conduct clustering but is secondary. Outcome guardrails are the key anti-gaming mechanism (harm coefficient: -0.144). [text, p.6–7]

**Load-bearing examples/structures:**

The firm action parameter table [text, p.4] is doing significant load — it makes visible that there is a spectrum from quality_overcompliance to open_noncompliance, with the interesting strategies (boundary_test, aggressive_edge, loophole_shift) in the middle: formally compliant or near-compliant, but progressively cheaper and higher-harm. The model's insight is precisely that computable rules make *this region* more navigable, not that they enable open violation.

The event study finding [text, p.7] is important and under-emphasized: post-rule-change harm reduction is 0.002 per period — essentially nothing. Firms don't return to thick compliance after a threshold moves; they relocate around the *new* computable boundary. This is the regulatory chase cycle.

**Where the argument is most confident:** The signal-conduct distinction and the static computability result. These survive multiple robustness checks (epsilon variations, penalty variants, channel ablations).

**Where it is most speculative:** The anti-gaming design's generalizability. The ablation shows guardrails do more work than randomization, but the author acknowledges this is conditional on the harm signal being observable and the harm target being demanding [text, p.5]. In real regulatory domains, the harm signal is often precisely what is *not* observable, which could reverse the result.

---

## 3. Conceptual Vocabulary

**Conduct boundary mass (B_t):** The population share of firms in the region (0 ≤ θ_t − r_it ≤ ε) — actually near the legal threshold in their underlying risk behavior. The author's preferred measure of gaming. [text, p.2]

**Signal boundary mass:** The same region measured in the enforcement signal space (which is noisier or cleaner depending on computability). What regulators observe. [text, p.3]

*Tension with my vocabulary:* I have been thinking about protocol gaming primarily through Goodhart's Law as a named phenomenon. He is careful to distinguish his setup from generic Goodhart [text, p.1]: "Legal rules create administrable boundaries, not only performance scores." This is a useful refinement — legal rules create *lines*, not just *metrics*, and line-walking has distinctive dynamics (discrete threshold structure, imitation of profitable crossing patterns, regulator-as-threshold-mover). I should carry this distinction.

**Regulatory arbitrage cycle / regulatory chase cycle:** The dynamic where ordinary adaptive updating produces threshold movement, firms relocate around the new boundary, regulators move again — cycling without convergence to thick compliance. Distinct from the gaming equilibrium (no updates, just edge clustering). [text, p.6, Table 7]

**Rule churn:** Frequency of threshold or audit-rate movement. The RL regulator produces churn of 3.111 vs. 0.200–0.244 for other adaptive designs. High churn is a distinctive institutional failure mode, separate from harm levels. [text, p.5]

**Anti-gaming design:** Specifically, the combination of *randomized audit margins* (unpredictable search of the edge region) and *outcome guardrails* (harm-based backstop triggers). Budget-neutral — reallocates audit attention rather than increasing it. [text, p.3]

**Boundary compliance / edge strategies:** Formal compliance achieved by operating just inside the legal line — not violation, not thick compliance. The regime of interest. [text, p.1]

---

## 4. Analytical Moves

**The conduct/signal separation:** When studying any system where behavior and measurement are distinct processes, construct separate measures for each before drawing conclusions about behavioral change. A cleaner sensor does not imply behavioral improvement; behavioral change does not imply cleaner signals. *Transfer application:* Whenever a protocol is made more legible (better monitoring, computable compliance checks), ask separately: did conduct change, or only the signal?

**The mechanism-before-estimation move:** Use synthetic simulation not to estimate magnitudes but to establish that a proposed mechanism is sufficient to generate the pattern of interest under transparent assumptions. This immunizes the core contribution from objections about data availability while keeping the argument empirical (not just theoretical). *Transfer application:* For candidate laws that are hard to test empirically, an ABM possibility result is a legitimate intermediate step — stronger than pure theory, weaker than empirical confirmation.

**The ablation-as-mechanism-decomposition:** Remove each component of a multi-channel treatment one at a time to isolate which channels carry the effect. Here: anti-gaming = randomized margins + outcome guardrails; guardrails do more harm reduction; randomization does more boundary-mass reduction. [text, p.5] *Transfer application:* When a protocol feature bundle produces an effect, ablate components to identify load-bearing mechanisms.

**The policy frontier construction:** Rather than claiming dominance for one design, identify the non-dominated set across multiple outcome dimensions (boundary mass, harm, edge-strategy share, rule churn). Some ambiguous-static runs remain on the frontier (zero churn). "Dominance" is multi-dimensional and the tradeoffs are part of the finding. [text, p.6]

**Rule-churn as an independent outcome:** Tracking institutional stability separately from harm and boundary mass. This catches failure modes (RL regulator) that harm-only metrics miss. *Transfer application:* For any protocol governance design, measure revision frequency as an outcome in its own right, not just as a cost.

---

## 5. What It Says About the Nature of Things

The deepest implicit commitment in this paper is that **legibility and exploitability are coupled**. Making a system easier to understand for legitimate users makes it easier to navigate for strategic users. This is not a defect of specific implementations — it is a structural feature of any system where rules are represented in a shared, inspectable form. Transparency creates a legible target.

The second deep commitment is that **optimization pressure finds the representation**. Firms don't game the underlying purpose of the rule; they game its computable representation. Once a rule has a machine-readable form, that form becomes the object of optimization. The rule's intent and the rule's representation diverge over time as strategic search concentrates at the boundary.

Third, and most important for my research: **adaptive response without anti-gaming structure produces a chase cycle, not convergence**. The regulator updates, the firms relocate, the regulator updates again. This is a feedback system with no attractor at thick compliance. Faster adaptation makes the cycle faster, not smaller. The escape condition requires a different structural element — not more responsiveness, but a randomized or outcome-based element that disrupts the learnability of the boundary.

---

## 6. What It Says About Becoming a Better Researcher

The paper models epistemic honesty about scope as an active intellectual commitment, not just a disclaimer. He is explicit about what the simulation can and cannot show: "mechanism claims rather than jurisdiction-specific estimates" [text, p.2], "cautious claim about sufficient conditions, not a universal prediction" [text, p.5]. This level of scope-marking is unusual and worth emulating. M-016 connection: the habit of explicitly naming the *type* of claim being made (possibility result / mechanism claim / empirical estimate / universal law) before presenting evidence is a calibration practice.

The "estimand first" move is a research design discipline: before running the experiment, formalize exactly what you are trying to measure and make sure that measure is not contaminated by the measurement instrument. He built the conduct/signal distinction into the model *because* an earlier construction produced a measurement artifact [text, p.3]. This is an example of the researcher catching their own confound through a design check, not through reviewer critique.

The use of synthetic data is defended explicitly and carefully [text, p.1, p.7]. The defense is: the point is to make assumptions transparent and mechanisms inspectable, not to fit a dataset. For my research, this is permission to use thought experiments and design fictions (M-012, M-013) as legitimate research moves — not second-class to empirical evidence, but serving a different evidentiary role.

---

## 7. Where It Touches My Research

**Direct connection to Goodhart's Law territory:** He explicitly cites Goodhart [text, p.1, reference 5] and then distinguishes his setup. The distinction is worth formalizing: Goodhart is about measure-as-target; this paper is about *line-as-target*. Legal/protocol boundaries have a discrete threshold structure that metrics don't. Gaming a metric means optimizing a continuous score; gaming a boundary means finding the edge of a binary compliance region. The dynamics differ — boundary gaming produces clustering, metric gaming produces score inflation without clustering necessarily. [inference]

**Connection to the formalization ratchet theme:** The paper implies that making protocols computable is not neutral — it changes the strategic environment. This is a specific instance of a broader pattern I've been tracking: increasing the legibility of a protocol changes how it is used, not just how efficiently it is used. The notation lock-in (from Iverson) was about cognitive access; this paper is about strategic access. Both point to the same structural fact: representation shapes behavior. [inference]

**Connection to the 4umd discord observation (June 17):** "Systems represent possible futures implicitly through their error-correction mechanisms — the futures a protocol guards against are visible in what constraints it enforces." The anti-gaming design in this paper is precisely such a mechanism: the outcome guardrail represents the future of harmful edge behavior and constrains it before it fully materializes. The randomized audit margin represents uncertainty about which boundary region will be examined — it represents possible futures for the firm by making those futures unpredictable. [inference — connection to inbox item]

**Connection to the health-check stigmergy observation (4umd, June 18):** The regulatory-chase-cycle dynamic here — firms relocating around a new threshold after it moves — is the failure mode when health checks are too legible. If firms can read the health-check protocol, they optimize for the check, not the health. The anti-gaming move (randomization, outcome guardrails) is the stigmergy-enabling design: it creates observational conditions that can't be fully anticipated. [inference]

---

## 8. Candidate Laws

**CL-X: The Legibility-Exploitability Coupling**

*What the text says:* "Once firms can read the boundary more clearly, what do they learn?" [text, p.1]. Computable static rules raise conduct boundary mass from 0.367 to 0.411 and signal boundary mass from 0.281 to 0.403. The conduct measure moves after the signal-conduct separation is enforced [text, p.4–5].

*Candidate formulation:* As the legibility of a protocol boundary increases, the cost of strategic search near that boundary decreases, causing conduct to cluster toward the boundary even when the boundary itself is unchanged. The magnitude of conduct clustering increases with the computability of the boundary representation.

*Falsification:* A protocol transition that significantly increases computable legibility of a compliance boundary while producing no increase in boundary-adjacent conduct (measured separately from signal), in a setting with sufficient agent learning capacity and competitive pressure. He's careful to note his result is a sufficient-conditions claim, not universal — so a domain where the mechanism is absent (no imitation, no learning pressure) would not falsify but would scope.

*Confidence:* speculative — single-domain (synthetic regulatory simulation), mechanism stated but untested across structurally independent domains.

**CL-Y: Adaptive Chasing Without Anti-Gaming Structure Produces No Convergence**

*What the text says:* "Ordinary adaptation reduces harm but does not reliably reduce boundary mass" [text, p.5]. Firms "relocate around the next computable boundary" after threshold moves [text, p.7]. Rule churn under the RL regulator is 3.111 versus 0.200 for anti-gaming design.

*Candidate formulation:* Adaptive rule revision that does not include a randomization or outcome-based structural element produces a regulatory chase cycle: faster revision accelerates boundary relocation without converging to substantive compliance. The escape condition requires disrupting the learnability of the boundary representation, not increasing revision frequency.

*Falsification:* An adaptive regulation design with no randomization or outcome guardrails that achieves convergence to substantive compliance (reduced conduct boundary mass, not just reduced harm) across multiple competitive markets with learning firms.

*Confidence:* speculative — again, single-domain synthetic. But the mechanism is clean enough and the implications specific enough to register formally.

---

## 9. What Surprised Me / What Doesn't Fit

**The event study non-result is the most interesting finding.** Post-rule-change harm reduction is 0.002 per period [text, p.7]. He presents this as a warning "against treating rule revision as an immediate reset." But I think it's stronger than that: it means the regulatory-chase-cycle equilibrium is sticky. Firms don't just adapt to new thresholds — they *expect* threshold movement and pre-adapt their learning strategies. The event study suggests that by the time a threshold moves, the firm's Q-table has already been conditioned on the dynamics of threshold movement, not just the current threshold. This is a second-order strategic adaptation that the paper describes but doesn't fully theorize. [inference]

**The loophole-shift paradox:** Under anti-gaming design, the loophole-shift strategy share actually *increases* slightly (0.114 → 0.126) even as conduct boundary mass falls and harm falls [text, p.5, Table 2]. He notes this without fully explaining it. My reading: the anti-gaming design makes harmful edge strategies more costly (guardrail triggers) but doesn't touch formal loophole use that produces lower harm. This implies the anti-gaming intervention is harm-targeted, not boundary-targeted — it rearranges the strategy distribution rather than shrinking the edge region overall. This is a meaningful scope condition for CL-Y: the intervention targets harm, not gaming per se.

**The framework strain at "computable as a bundle":** He acknowledges [text, p.3, p.7] that computability enters through multiple channels at once and that he can't achieve component-level causal identification in the core scenarios. The channel ablation is a diagnostic, not an estimate. This is honest but means the core mechanism claim is somewhat underspecified — we know the bundle produces the effect, but the relative contribution of threshold clarity vs. signal precision vs. imitation-amplification vs. adjustment speed is known only in the simulated design space. In real regulatory transitions, these channels often move together and in different proportions. [text, p.7]

**The RL regulator as cautionary tale is too quickly dismissed.** He says "I do not read this as evidence against reinforcement learning in regulation" and attributes the high churn to undertraining and reward misspecification [text, p.5]. This may be right, but it's also possible that the high-churn result is a structural property of any fast-learning regulator in a competitive firm-learning environment — not a training artifact but a general instability result when regulator learning rate exceeds firm adaptation lag. That would be a much more significant finding about the governance of adaptive regulation. The paper leaves this open.

---

## 10. What It Opens

**Immediate questions:**

1. Does the legibility-exploitability coupling appear in structurally independent domains? Candidates: financial reporting standards (XBRL adoption and earnings management at reported thresholds), tax code clarity and tax shelter proliferation near explicit deduction thresholds, FDA regulatory guidance documents and pharmaceutical label-gaming near clinical endpoints. If the pattern holds across these domains with independent causal actors, CL-X becomes a candidate law.

2. What is the relationship between the regulatory chase cycle here and the formalization ratchet I've been developing? He's describing a feedback loop between rule formalization and strategic adaptation. The ratchet I've been tracking is about increasing rigidity; this paper is about increasing strategic alignment with the formalized boundary. Are these the same phenomenon at different scales, or structurally different?

3. The boundary between "anti-gaming design" and "obscurantism" deserves formal treatment. Randomized audit margins are anti-gaming; deliberately ambiguous rules are just another form of ambiguity with different costs. What is the structural distinction? He gestures at this but doesn't formalize it [text, p.8: "randomization should select review or inspection attention rather than make hidden substantive law"].

**Texts to read:**

- Schauer (1991), *Playing by the Rules* [reference 9, text p.10] — the philosophical account of rule-based decision making and strategic line-walking. He invokes it; I should read it directly. Likely to have significant implications for the formalization ratchet.
- Ayres and Braithwaite (1992), *Responsive Regulation* [reference 1, text p.8] — the source of the responsive regulation tradition He is trying to extend/qualify. This is the tradition within which anti-gaming design sits.
- Campbell (1979) [reference 3] — the original "assessing the impact of planned social change" paper, which He cites as the source of the Goodhart-adjacent Campbell's Law. Should read to understand the genealogy.

**Traditions to investigate:**

- The responsive regulation tradition (Ayres, Braithwaite, Baldwin, Black) — seems like a rich domain for cross-checking whether the chase-cycle failure mode has been theorized independently of computable rules, and whether anti-gaming design has precedents.
- The literature on bright-line rules vs. standards in law and economics (Kaplow 1992 being the canonical reference) — directly relevant to the legibility-exploitability tradeoff. A bright-line rule is maximally computable; a standard is maximally ambiguous. The tradeoff He is studying is the bright-line side of this classic debate.

**Live question to sit with:** He separates conduct from signal throughout. My candidate law framework needs this distinction too. When I look at a protocol and claim "firms cluster near the boundary," I need to ask: am I measuring actual conduct or measurement artifacts? This is a discipline for how I read empirical protocol research going forward.
