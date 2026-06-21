# Deep Read Notes: Arxiv 2605.30680

*Source: `bibliography/deep-reads/arxiv-2605.30680.pdf`*

---

## Reading session: full document (32 pages)

# Deep Read Notes: Wang et al., "Healthcare Mechanisms from Policy-as-Code Search under Strategic Provider Response" (arXiv 2605.30680)

---

## 1. Gestalt

This paper is animated by a single sharp observation: a healthcare policy is not what an administrator writes — it is the *composition* of what the administrator writes with how providers respond to it. The text of a rule and the equilibrium it produces are two different objects, and existing benchmarks evaluate only the text. The paper's contribution is to close this loop: build a simulator (Medi-Sim) where administrator rules and provider strategic responses are evaluated together, in the same rollout, producing channel-level diagnostics that make the composition visible. The animating phenomenon is **pressure migration** — when you close one distortion channel (say, up-coding), the same underlying incentive pressure resurfaces in an adjacent channel (say, patient selection). A benchmark that holds provider behavior fixed cannot see this, and will systematically reward rules that relocate distortion rather than remove it. The paper then uses this simulator as both a diagnostic tool and a search environment: LLM-guided evolutionary search over typed, inspectable rule programs finds policies that actually restructure the incentive geometry rather than just moving the pressure around. The result is empirical and mechanistic — three decades of healthcare economics findings reproduced as adjacent regimes of a single phase diagram — and methodological: a framework for mechanism design in regulated, high-stakes environments where black-box neural controllers are inadmissible.

---

## 2. Argument and Structure

**Core claim:** Healthcare mechanisms must be evaluated in closed-loop strategic response; any benchmark that holds provider behavior fixed will misrank mechanisms. [text, p.1]

**Secondary claim:** The policy class for regulated healthcare must be *inspectable as code* — line-by-line auditable — which rules out neural controllers and motivates program synthesis. [text, p.2, p.4]

**Structural mechanism (pressure migration):** Providers have five distortion channels — coding, selection, delay, effort, triage — coupled through a shared utility function. Closing one channel shifts the incentive gradient to adjacent channels. The channels form a **substitution lattice** [text, p.15–16]: where one distortion saturates against a structural floor or ceiling, adjacent channels activate to relieve the same shadow price.

**Argument shape:**
1. Identify the gap: existing healthcare AI benchmarks treat provider behavior as exogenous; existing AMD systems use non-inspectable neural controllers [p.1–2]
2. Formalize the problem: Stackelberg game, hospital administrator as leader, provider population as follower, five behavioral channels [p.2–3]
3. Build the simulator (Medi-Sim): IPS (Identify-Produce-Settle) loop, five provider channels with closed-form behavioral rules, three-layer experiment structure [p.3–6]
4. L1 experiments: sweep the incentive parameter space (α, β) → classical healthcare failures emerge as adjacent regimes of a single phase diagram [p.6–7]
5. L2 experiments: perturb administrative levers one at a time → pressure migration visible (audits suppress coding, raise selection) [p.7]
6. L3 experiments: LLM-guided code search over typed DSL → find inspectable policies that reshape incentive geometry [p.7–8]

**Load-bearing example:** The audit lever sweep [p.7, p.32]. Raising audit probability suppresses up-coding to near zero — but balanced-regime cherry-picking more than doubles (0.100 → 0.233). This is the cleanest empirical demonstration of pressure migration and the linchpin of the paper's argument that single-channel diagnostics are systematically misleading.

**Key findings:**
- Classical healthcare failures (DRG coding rent, case-mix distortion, target gaming) are not independent phenomena — they are adjacent regimes of one phase diagram [p.8]
- The balanced interior (moderate α, β) hides the most risk: visible metrics improve while delay and KPI-targeting intensify; KPI-health correlation becomes strongly negative (−0.659) [p.6]
- Flexible capacity is not automatically beneficial — it depends entirely on the allocation rule; KPI-steering can cause flexible capacity to *raise* waiting [p.7, p.20–21]
- LLM-guided search follows its objective precisely: profit-objective search amplifies coding; mixed-objective search finds a policy that eliminates up-coding while retaining comparable return — by changing *which channels earn the return* [p.7–8]

**Acknowledged limits:**
- Bounded-rationality response class, not solved equilibria — a tractable approximation of unknown quality [p.9]
- L3 result depends on warm-start library diversity; search cannot recover the mixed family from a neutral-only start [p.9, p.22–23]
- Synthetic rollouts, no real-world calibration [p.9]

---

## 3. Conceptual Vocabulary

**Pressure migration** [text, p.1]: When a mechanism closes one provider distortion channel, the same incentive resurfaces in an adjacent channel. Distinct from "substitution" in the standard sense because the mechanism is the *cause* of the migration — the rule that appears to fix the problem is responsible for relocating it.

**Substitution lattice** [text, p.15–16]: The structural arrangement of distortion channels such that saturating one activates adjacents. Not named as such in the main text (my synthesis), but the paper describes it functionally — the channels are "coupled through Eq. (2)" and the IPS decomposition factorizes them correctly.

**Coding wedge / measurement wedge** [text, p.3, p.5]: Two distinct information gaps. The coding wedge is the gap between true clinical complexity and reported billing group (the rent that up-coding arbitrates). The measurement wedge is the gap between true clinical value and the KPI used for bonuses (the rent that proxy gaming arbitrates). Both are active simultaneously and interact.

**IPS (Identify-Produce-Settle)** [text, p.3]: The simulator's temporal order within a period. Identify = classify patients and assign billing groups. Produce = constrained treatment under capacity. Settle = compute reimbursement, KPI scores, bonuses. The paper argues this is the *correct* factorization — not just a simulation convenience.

**Policy-as-code** [text, p.2, p.4]: Administrative rules expressed as typed, executable, assignment-only programs over a constrained DSL. The constraint is not just an engineering choice — it is the compliance requirement for regulated deployment. Neural controllers are inadmissible because they fail line-by-line auditability.

**Regime interior failure** [text, p.6–7]: The finding that the balanced interior of the (α, β) parameter space produces the most diagnostically deceptive outcomes — visible metrics improve while invisible distortions (delay, KPI targeting) intensify. This is a failure mode *created* by the measurement system, not by extreme incentives.

**Tension with existing vocabulary:** I have been using "Goodhart's Law" loosely to refer to proxy gaming. This paper gives it a tighter structure: the *measurement wedge* is the mechanism; Goodhart drift is one manifestation of it (when incentive strength increases, the wedge widens); but the same wedge can produce target gaming, strategic delay, and case-mix distortion through different channels, all from the same underlying structure. I should use "measurement wedge" when I mean the structural gap, and "Goodhart drift" when I mean the intensification-as-incentives-strengthen pattern specifically.

---

## 4. Analytical Moves

**The phase diagram as classifier:** Rather than studying healthcare failures as independent phenomena requiring separate analyses, map the full parameter space and show which failures appear in which regions. Failures that were treated as separate problems become *adjacent regimes of one dynamics*. The payoff: you can predict which failure will emerge from any given parameter combination, and you can see which transitions are continuous vs. discontinuous. [text, p.6–8]

*Transfer:* For any protocol with multiple distortion channels, map the parameter space. Look for the interior failure zone — the region where aggregate metrics look good while invisible distortions intensify.

**The lever-as-pressure-tracer:** Perturb administrative controls one at a time and track the *full response vector* across all channels, not just the channel the lever was designed to address. The lever is not just an intervention — it is a diagnostic probe. The response vector reveals the substitution lattice structure. [text, p.7]

*Transfer:* In any multi-channel system, audit-style single interventions are pressure tracers, not just control mechanisms. Log the full response, not just the targeted channel.

**The warm-start-as-family-prior:** Rather than searching from a neutral start, populate the search library with a diverse set of policy families (profit-oriented, welfare-oriented, access-oriented, etc.). The quality of search depends not on search budget but on library diversity. Search refines family priors; it does not invent families from scratch. [text, p.9, p.22–23]

*Transfer:* In any evolutionary program search, the critical question is not "how many iterations?" but "what priors does the library encode?" Diversity in priors is the binding constraint.

**The channel decomposition diagnostic:** When a headline metric (e.g., cherry-picking index) shows a surprising pattern, decompose it into its constituent channels. The headline hides structural facts — what looks like one failure mode is often two distinct mechanisms with opposite causes producing similar aggregate signatures. [text, p.16–17]

*Transfer:* Any aggregate metric over a multi-channel system is potentially masking this. When a metric behaves "unexpectedly," the right move is channel decomposition, not parameter adjustment.

**The steering-off ablation:** To determine whether a beneficial resource has an adverse effect, compare its behavior under the allocation rule with its behavior under a neutral allocation rule. Flexible capacity raised waiting under KPI steering; under static allocation, waiting was unchanged. The resource is not the cause — the allocation rule is. [text, p.20–21]

*Transfer:* When a resource intervention has a counterintuitive effect, the allocation rule is almost always the mechanism. Ablate the rule before concluding anything about the resource.

---

## 5. What It Says About the Nature of Things

**Composition determines behavior, not text.** A protocol is not what it says — it is what it does in the presence of strategic responders. The text of a policy and its equilibrium consequences are two different objects. Any evaluation that reads only the text is evaluating the wrong thing. This is a general claim about all protocolized systems in the presence of strategic agents, not just healthcare. [inference from text, p.1–2]

**Incentive geometry has topology.** The paper treats the (α, β) space as having a genuine topology — regions, boundaries, transitions, interior vs. exterior. The failures are not distributed randomly across this space; they cluster in predictable regions, and transitions between regions can be continuous or discontinuous. This implies that mechanism design is a problem of *navigating a landscape*, not of finding a scalar optimum. [inference from text, p.6–8]

**The interior is the most dangerous failure region.** In incentive systems with multiple channels, the most dangerous parameter region is often the moderate interior — where no single channel is extreme, but multiple channels are active simultaneously, producing deceptive aggregate metrics. The high-risk extremes are visible; the moderate interior is not. This is a structural consequence of the substitution lattice, not a coincidence. [text, p.6–7]

**Flexibility only helps if the allocation rule is aligned with the objective.** This is a specific version of a more general claim: resources are not beneficial in themselves; their benefit depends entirely on the mechanism that allocates them. Flexible capacity under KPI steering is harmful; under neutral allocation, it is neutral. The resource is a carrier; the allocation rule is the mechanism. [text, p.20–21]

**Search follows objectives literally.** LLM-guided evolutionary search under a profit objective amplifies the profit-oriented distortion channel. Under a safety-penalized mixed objective, it finds a policy that reshapes the channel structure. The algorithm is not "intelligent" in any normative sense — it optimizes exactly what it is told to optimize. This means objective specification is the most critical design decision in automated mechanism design. [text, p.7–8]

---

## 6. What It Says About Becoming a Better Researcher

**Evaluation design is the research question, not a prerequisite.** The paper's central contribution is not the optimal policy — it is the simulator that makes evaluation meaningful. Before you can compare mechanisms, you must determine what "better" means in the presence of strategic response. The benchmark design is the theoretical act. This connects directly to von Humboldt's observational infrastructure insight: building the network *was* the science. [inference from text, p.1–2]

**Hold all channels visible simultaneously.** The authors' insistence on tracking all five distortion channels in every experiment, not just the targeted channel, is a research discipline, not just a reporting requirement. The most important findings in this paper come from channels that were not the intervention target. Single-metric evaluation is a systematic error. [inference from text throughout]

**Validate against known results before discovering new ones.** The paper validates Medi-Sim against nine stylized healthcare facts before using it to discover new findings [text, p.5, p.32]. This is the right epistemic order: establish that your instrument is calibrated before using it to make novel claims. The validation is not a separate paper — it is the precondition for the discovery claims.

**Be specific about what the warm-start provides.** The L3 ablation is unusually honest: "AlphaEvolve over Medi-Sim is a feasibility demonstration of program search over the policy class of §4 and does not claim that current search procedures can rediscover the mixed family from scratch" [text, p.9]. This is a clear scope limitation stated explicitly in the main text. Most papers would bury this in limitations. The willingness to bound the claim precisely is what makes the claim credible.

**The discovered policy structures are the result, not the search curves.** The paper's key contribution from L3 is not that fitness improved over iterations — it is that the discovered policy has a specific *structure* (the −100 indicator penalty for coding gap > 0.20) that reveals a general mechanism design principle. The code is evidence, not just an output. [text, p.28]

---

## 7. Where It Touches My Research

**Pressure migration as a candidate law.** This is the most direct connection. The paper provides a well-documented mechanism for a phenomenon I have been thinking about under the heading of "distortion conservation" or "Goodhart migration." The mechanism is: providers have a utility function over multiple channels; when one channel is closed by policy, the gradient of that utility pushes behavior toward adjacent channels; the policy that closes the channel is therefore the cause of the migration. This is a stronger claim than "distortion tends to persist" — it is a causal mechanism with a specific formal structure (the substitution lattice emerging from the coupled utility function). [text, p.1–3, p.15–16]

The healthcare domain provides strong evidence. The question is whether structurally analogous pressure migration appears in other protocol domains. Candidates: tax compliance (closing evasion channel → avoidance channel), financial regulation (closing one arbitrage → adjacent arbitrage), platform governance (closing one manipulation → adjacent manipulation).

**The measurement wedge as a structural concept.** The coding wedge / measurement wedge distinction is a cleaner vocabulary than I have been using for the Goodhart dynamic. The measurement wedge is the static gap (structural feature of the protocol); Goodhart drift is the dynamic consequence of incentivizing across that gap. I should update my working vocabulary accordingly.

**Interior failure zone.** The finding that the balanced interior of the parameter space is the most dangerous region connects to something I have been circling around: that "balanced" or "compromise" protocols are often the most fragile, precisely because they are not extreme enough to trigger the visible failure modes but are still subject to the invisible interior ones. The phase diagram methodology is a tool for making this visible systematically.

**Allocation rule as mechanism.** The flexible capacity finding (the resource is neutral; the allocation rule determines the effect) generalizes to a claim about all resource-as-protocol designs. This is worth keeping — when I analyze capacity or resource allocation in other protocol domains, the allocation rule is the load-bearing mechanism, not the resource quantity.

---

## 8. Candidate Laws

**Candidate: Pressure Migration Law**

[text, p.1, p.7, p.15–16]

*What the text says:* "Closing the coding channel more than doubles low-complexity selection" [text, p.1]; "the channels are coupled through Eq. (2)" [text, p.15]; "a benchmark that scores rules against a fixed provider systematically over-rewards mechanisms whose effect is to relocate rather than remove distortion" [text, p.1].

*Candidate formulation:* In any protocol system with multiple response channels coupled through a shared utility function, closing one distortion channel by administrative rule will shift distortion to adjacent channels proportionally to the residual gradient pressure. The total distortion remains approximately conserved until the underlying utility function is restructured.

*Domains so far:* Healthcare (documented empirically); financial regulation [inference — this is the basis of regulatory arbitrage literature, but not yet cross-domain confirmed in this text]; platform content moderation [inference — deplatforming individuals shifts activity to adjacent platforms].

*Falsification:* A documented case where closing one distortion channel in a multi-channel coupled system produced no measurable increase in adjacent channel distortion, and the provider utility function was not restructured. Or: a case where total distortion (measured across all channels) decreased proportionally to the closed channel's contribution, without redistribution.

*Confidence:* speculative (one domain with strong internal evidence, mechanism clearly stated)

**Candidate: Interior Deception Zone**

[text, p.6–7, appendix E]

*What the text says:* "the balanced interior is most diagnostic: visible metrics improve while pressure moves into selective deferral and proxy targeting" [p.6]; KPI-health correlation −0.659 in the balanced interior vs. cleaner failure modes at extremes [p.6–7].

*Candidate formulation:* In any incentive system with multiple distortion channels and aggregate performance metrics, the moderate interior of the incentive parameter space systematically produces the most deceptive outcomes — aggregate metrics appearing improved while invisible distortions intensify. The extreme parameter regions produce visible, diagnosable failures; the interior produces invisible failures.

*Domains so far:* Healthcare (documented); [inference] organizational performance management (balanced scorecards); [inference] multi-objective regulatory regimes.

*Falsification:* A multi-channel incentive system where the moderate interior parameter region produces either the worst visible failures or accurately reflects underlying performance deterioration through aggregate metrics.

*Confidence:* speculative (one domain, mechanism plausible, needs cross-domain confirmation)

---

## 9. What Surprised Me / What Doesn't Fit

**The warm-start dependence is more fundamental than presented.** The paper describes the warm-start dependency as a "limitation" [p.9], but the K=200 vs. neutral-only ablation shows that search produces *no improvement* over its starting point without a diverse library. This is not a limitation of the current implementation — it is a structural claim about the shape of the program space. The space has many locally flat regions separated by rare high-dimensional edges where coordinated multi-field edits matter. LLM-guided search does not explore this space; it *exploits priors about which regions contain families*. This means the "search" in "policy-as-code search" is doing something closer to Bayesian updating over prior families than exploration over a neutral space. The implications for what this demonstrates are significant — the paper is honest about it in the limitations, but the significance deserves more weight. [text, p.9, p.22–23, p.23–24]

**The discovered mixed policy's indicator term is the most theoretically interesting result.** The final mixed policy uses `−100 * I(coding_gap > 0.20)` — a discontinuous penalty that snaps to a regime forbidding coding deviations above the threshold, while keeping a smooth gradient signal for learning. The paper describes this as "a hand-engineered version of the same hard-threshold-plus-smooth-shaping idiom that has emerged in several published reward-design studies" [p.28]. This is a general mechanism design pattern that the search independently rediscovered. But the paper treats it as a result about coding, not as a general claim about reward specification. It should be: when you need hard constraints in a gradient-based system, the −∞ indicator plus smooth shaping is the structural form. This is a candidate law the authors don't frame as one.

**The IPS decomposition claim is underargued.** The paper claims that IPS (Identify-Produce-Settle) is "the right factorization" for Medi-Sim [p.15–16], based on the substitution lattice evidence. But the factorization is also a modeling choice that makes the channels separable — if the real system has coupling structures that cross the IPS boundaries (e.g., coders who know triage decisions), the factorization understates the coupling. The authors acknowledge this partially in the limitation about bounded rationality [p.9], but don't connect it to the IPS factorization specifically.

**The health output range is remarkably narrow.** [text, p.18–19] Health output varies only in [0.95, 1.02] while funds span four orders of magnitude. The paper attributes this correctly to the diminishing-return production function. But this means that in the simulator, the clinical value of care is essentially fixed — all the action is financial. This is a modeling choice, and it means the simulator is primarily a financial mechanism model with healthcare framing. Whether this appropriately captures healthcare trade-offs, or whether it biases toward finding financial optimization as the dominant mechanism, is not discussed.

---

## 10. What It Opens

**Pressure migration across domains.** The mechanism is clear enough to test in structurally independent domains. The specific test: identify a protocol system with (a) multiple response channels coupled through a shared utility function, (b) a documented administrative intervention targeting one channel, and (c) measurable outcomes across all channels. Financial regulation is the obvious candidate. Platform moderation is another. Tax compliance has three decades of literature on channel substitution that could be mapped onto this framework.

**The interior deception zone as a generalizable phenomenon.** The finding that balanced interior parameter regions produce deceptive aggregate metrics while invisible distortions intensify needs cross-domain testing. Organizational performance management (balanced scorecards, OKRs) is a natural domain — the prediction would be that balanced weighting across multiple KPIs produces interior failure zones where no single metric looks alarming but the organization is deteriorating on unmeasured dimensions.

**The hard-threshold-plus-smooth-shaping idiom.** The `−100 * I(coding_gap > 0.20)` structure deserves its own investigation as a general mechanism design pattern. Where else does this appear? Software circuit breakers (hard stop when threshold exceeded, smooth degradation below). Financial margin calls. Regulatory tripwires. The pattern is: smooth optimization with hard safety constraints requires this two-level representation. This is a candidate law that the paper generates as a byproduct.

**Texts to read:**
- Manheim and Garrabrant (2018), "Categorizing variants of Goodhart's law" — the paper cites this repeatedly; I need the full taxonomy to understand how pressure migration maps onto Goodhart's variants
- Ellis (1998), "Creaming, skimping and dumping" — the health economics foundation for the five-channel model; reading this would let me assess how much of the Medi-Sim structure is inherited from health economics vs. novel
- Holmstrom and Milgrom (1991), "Multitask principal-agent analyses" — the measurement wedge theoretical foundation; this is the formal source for the Goodhart-adjacent claims
- Skalse et al. (2022), "Defining and characterizing reward hacking" — cited for the formal result that optimizing an imperfect proxy cannot be made safe by narrowing the reward function; this is directly relevant to the pressure migration law
