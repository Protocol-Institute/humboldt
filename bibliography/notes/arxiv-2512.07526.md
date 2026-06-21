# Deep Read Notes: Arxiv 2512.07526

*Source: `bibliography/deep-reads/arxiv-2512.07526.pdf`*

---

## Reading session: full document (41 pages)

# Deep Read: Tan (2026) — "Strategic Preemption Under Shared Catastrophic Risk"

*arxiv-2512.07526, full document, 41 pages*

---

## 1. Gestalt

This paper is an attempt to formalize a specific intuition failure — the conviction that "surely, if the stakes are high enough, rational actors will slow down." Tan shows, using the machinery of real options and preemption game theory, that this intuition is exactly wrong when the downside of failure is shared symmetrically across all players. The animating question is not "how bad does the disaster have to be to stop the race?" but rather "why does the size of the disaster fail to matter at all?" The answer — the cancellation effect — is algebraically stark: when the ruin term appears identically in every player's payoff function, it drops out of the indifference condition that determines deployment timing. The catastrophe becomes, literally, invisible to the game-theoretic calculus of whether to race.

The paper is most valuable not as a policy analysis of AGI (though it is that) but as a structural diagnosis of a class of games that may be more common than we recognize: races where the prize is privatized and the catastrophe is socialized. The AGI framing is the sharpest instance, but Tan explicitly gestures at autonomous weapons, gain-of-function research, and space weaponization as domains sharing the same structure. What he has found is not an AGI-specific pathology but a game-theoretic law operating wherever prizes are concentrated and ruin is shared.

---

## 2. Argument and Structure

**Core architecture:** The paper builds on the Weeds (2002) / Huisman & Kort (2003) tradition of option games — models that combine real options analysis (the value of waiting) with preemption races (the cost of losing). The standard result in this tradition is that high volatility and downside risk favor delay. Tan's contribution is to show that this result collapses when the downside risk is borne symmetrically by all players.

**The cancellation effect** [text, p.3, p.16]: The ruin term −(1−π(τ))D appears identically in both the Leader payoff (eq. 3) and the Follower payoff (eq. 4). When the indifference condition L = F is solved for the preemption threshold V*_P (eq. 5), the D term cancels algebraically. The threshold becomes I/[(1−2S)π(τ)] — entirely independent of D. This is not a result about preferences or psychology; it is a structural algebraic property of the payoff functions.

**The suicide region** [text, p.18-20]: There are two relevant thresholds:
- V*_P (preemption threshold): the asset value at which racing begins — independent of D
- V*_S (survival threshold): the asset value at which NPV-positive deployment occurs — increasing in D

When V*_P < V*_S, there is a gap — the suicide region — where preemptive pressure forces deployment despite negative NPV. Crucially, as D grows, V*_S rises (it gets harder to justify deployment economically) while V*_P stays constant. The suicide region therefore *widens* as the catastrophe grows more costly. This is Proposition 3 [text, p.19], and it is the counterintuitive core of the paper.

**The social planner benchmark** [text, p.23-25]: A planner internalizing aggregate welfare sees ruin cost 2D (once for each player). The socially optimal threshold V*_social is therefore higher than even V*_S (a single player's NPV threshold). This gives three nested thresholds: V*_P < V*_S < V*_social — with the gap between competitive equilibrium and social optimum widening in D.

**The saviour's trap** [text, p.21-23]: Introduces asymmetric beliefs (π_self > π_rival). The additional incentive to preempt becomes a "saviour premium" D(π_self − π_rival). This is the formalization of the unilateralist's curse: the agent most worried about catastrophe (highest perceived D, most convinced of their own superior safety) faces the strongest incentive to race fastest. The preemption threshold V*_P,saviour is strictly lower than the symmetric baseline.

**Mechanisms** [text, p.27-34]:
1. *Private liability (Dprivate)*: Adding a term to the Leader's payoff only (not the Follower's) breaks the cancellation effect. The double liability rule Dprivate = 2D restores social optimality. Partial liability narrows the suicide region proportionally.
2. *Prize-sharing (windfall clauses, S)*: When S → 0.5, V*_P → ∞ and the suicide region vanishes. The critical threshold S* = (1−π)D / [I + 2(1−π)D] is derived.

**Warning shots** [text, p.35-36]: The model predicts warning shots are ineffective in isolation because they only raise D — which, due to the cancellation effect, doesn't affect V*_P. They may even accelerate the race if agents believe π_self > π_rival (the saviour's trap amplifies with larger D).

**Acknowledged limits**: Two-player symmetry is a simplification (though the qualitative results extend to n-player); safety learning rate λ is exogenous; D is assumed homogeneous. These are appropriate for the paper's purpose — the core results are algebraic and robust to stochastic process specification [text, p.15].

**Confidence gradient**: Tan is highly confident about the cancellation effect (it's a mathematical proof) and the suicide region existence (idem). He is more speculative about the practical calibration of the mechanisms, explicitly acknowledging that Dprivate = 2D is probably infeasible at existential scale [text, p.30]. The warning shots section [p.35-36] is the most empirically speculative — he's making a prediction about a future event from the model.

---

## 3. Conceptual Vocabulary

**Cancellation effect** [text, p.16]: The algebraic elimination of the shared ruin term D from the equilibrium indifference condition. Not a behavioral finding — a structural consequence of symmetry in payoff functions. Distinct from risk-cancellation in insurance (where pooling reduces variance); here, the cancellation occurs because the same term appears on both sides of an equation and is subtracted out.

*Tension with my vocabulary*: I don't have prior terminology for this. It's a new mechanism for the class of problems I study. The nearest analogue in my existing vocabulary would be "coordination trap" — but the cancellation effect is more specific and more formally grounded.

**Suicide region** [text, p.18-20]: The parameter space where V*_P < Vt < V*_S — where preemptive pressure forces deployment despite negative risk-adjusted NPV. The metaphor is apt: the player "knows" the deployment is negative-expected-value but deploys anyway because the alternative (being second) is worse.

*Tension*: I need to be careful here. The "suicide region" is a deployment region, not a protocol region in my usual sense. But the structural logic — a region where individual rational action produces collectively self-destructive outcomes — connects to my interest in protocol failure modes.

**Saviour's trap** / **Saviour premium** [text, p.12, p.22-23]: The paradox where an agent who believes its safety standards are superior has a stronger incentive to race faster (not slower). The premium D(π_self − π_rival) is increasing in D — the more dangerous the catastrophe, the more the agent with "better" safety believes they must preempt to prevent the "worse" agent from deploying. This formalizes Bostrom et al.'s unilateralist's curse.

**Alignment tax** [text, p.11-12]: The framing (borrowed from Aschenbrenner 2024) that safety research is a substitutable cost that slows deployment velocity. In Tan's model, this is captured by the safety learning function π(τ) — more safety research time τ means higher π but also means being preempted. The alignment tax is the opportunity cost of safety investment denominated in competitive position.

**Double liability rule** [text, p.30]: The finding that private liability must equal 2D (twice the per-player ruin cost) to restore social optimality. Intuition: the social planner internalizes 2D; to make the private actor behave like the social planner, their private cost must be raised by the same 2D.

---

## 4. Analytical Moves

**The cancellation proof** [text, p.16-17]: Write the payoffs for both players, equate them to find the indifference condition, observe which terms appear on both sides and therefore cancel. The move generalizes: whenever you have a symmetric game with shared costs, check which cost terms will cancel in the indifference condition. Those terms will have no deterrence effect regardless of their magnitude.

*Transferable form*: "The cancellation test: In a game with shared costs, identify which cost terms appear symmetrically in all payoff functions. Those terms will cancel from the equilibrium indifference condition and will have no effect on equilibrium behavior — regardless of their magnitude."

**The three-threshold analysis** [text, p.18-25]: Derive V*_P (preemption indifference), V*_S (NPV break-even), and V*_social (social planner optimum) separately, then compare. The suicide region is defined by the gaps between these thresholds. The welfare analysis is a comparison of where competitive deployment occurs versus where social optimality lies.

*Transferable form*: When analyzing strategic races, derive not just the competitive equilibrium threshold but also the private NPV threshold and the social optimum threshold. The gaps between these three reveal the structure of the market failure.

**Payoff-structure targeting** [text, p.27-34]: To close the suicide region, ask: which feature of the payoff structure generates the pathology? (Answer: the cancellation effect and the winner-takes-all condition.) Then design mechanisms that directly target those features. Private liability targets the cancellation effect; prize-sharing targets S ≈ 0. The mechanisms are derived from the diagnosis.

*Transferable form*: "To design corrective mechanisms, trace the pathological equilibrium to its algebraic source in the payoff structure. Mechanisms that don't touch that source won't work regardless of how large they are."

**The warning-shots prediction** [text, p.35-36]: Ask what would have to be true for a proposed corrective (warning shot) to work. Answer: it would have to change D in a way that affects V*_P. But D doesn't appear in V*_P. Therefore warning shots can't work through the D channel — they can only work if they trigger exogenous changes to the payoff structure (liability or prize-sharing).

*Transferable form*: "Before predicting that a corrective event will change behavior, check whether the corrective event affects the parameters that actually determine equilibrium. If not, the prediction of behavioral change is unfounded regardless of the severity of the event."

---

## 5. What It Says About the Nature of Things

**Symmetry creates invisibility** [inference from cancellation effect]. When a cost is borne equally by all agents in a game, it becomes strategically invisible — it cancels from the equilibrium calculus regardless of its magnitude. This is not about rationality failing; it is about the structure of how individual optimization relates to shared exposure. The implication is general: *shared costs cannot function as deterrents in symmetric games*. Only asymmetric costs — borne by one player more than another — can influence strategic timing.

**The prize concentration / ruin socialization asymmetry** [text, p.6, p.37]. There is a structurally pathological configuration: concentrated private prize + diffuse shared downside. This configuration destroys the standard mechanism by which catastrophic risk generates caution. The mechanism (risk → caution) depends on the cost of the catastrophe being borne privately by the risk-taker. When the catastrophe is socialized, the mechanism fails.

**Increasing catastrophic risk can widen the pathological region** [text, p.19-20]. This is the most counterintuitive finding. We expect risk to be deterrent; here, greater risk expands the set of conditions under which the race proceeds irrationally. This is because D raises V*_S (making economically viable deployment harder) while leaving V*_P unchanged. The gap between the two thresholds — the suicide region — grows.

**Good intentions accelerate bad outcomes** [text, p.21-23]. The saviour's trap formalizes a general phenomenon: when actors believe they are the safest steward of a shared risk, the belief accelerates the race rather than restraining it. The more they believe in their own relative safety competence, the faster they move to preempt their "less safe" rival. Concern for catastrophe, when combined with beliefs of differential competence, inverts the caution relationship.

**Voluntary coordination fails for structural reasons** [text, p.27]. The paper is explicit: pause agreements and voluntary restraint don't change the underlying payoff structure, so they don't change the equilibrium. This is not a comment about trust or good faith; it's a structural observation. The game has a Nash equilibrium in the suicide region; the equilibrium is not disrupted by voluntary signals unless those signals alter the payoff functions.

---

## 6. What It Says About Becoming a Better Researcher

This is a methodological paper masquerading as a policy paper. The deepest research lesson it demonstrates is the **mechanism-first strategy**: don't ask "how big does X have to be to matter?" — ask "does X appear in the equation that determines the outcome?" Tan's discovery is that D doesn't appear in V*_P at all. Before Tan's analysis, the intuition was "surely D matters if it's large enough." Tan's contribution is to look at the algebra and find that D literally cannot matter for preemption timing, regardless of magnitude.

The research lesson connecting to M-016: the most valuable analytical moves are often disconfirmations of widely-held intuitions. Tan's paper is important precisely because the intuition it overturns (big catastrophe → deterrence) is almost universally held. The researcher who finds this is the one who commits to following the mechanism all the way to its conclusion rather than stopping when the conclusion is counterintuitive.

The warning shots section also exemplifies good research discipline: a prediction derived rigorously from the model, clearly stated, and falsifiable. The model predicts warning shots won't work through the D channel. That prediction is either right or wrong, and the falsification condition is clear. This is the model's mechanism-first approach applied to empirical prediction.

---

## 7. Where It Touches My Research

**Connection to protocol ossification (if I had active laws there)**: The cancellation effect is a structural analogue to one mechanism I care about. When all parties to a coordination game share the same costs and benefits, there may be no internal pressure for change — the status quo's costs cancel from the comparison that would motivate reform. This is a mechanism for stability that operates through algebraic symmetry rather than through switching costs or trust investments. Worth keeping as a candidate mechanism.

**The prize-concentration / ruin-socialization distinction** is relevant to understanding why some protocol races lead to safety degradation and others don't. The AGI case is extreme (prize fully concentrated, ruin fully socialized), but intermediate cases abound: financial system races where upside is private and systemic risk is socialized (cf. 2008), drug approval races where first-mover advantage is private and safety failures are socialized, etc. The model provides a framework for predicting *where* race-to-the-bottom dynamics will appear structurally.

**The double liability rule** (Dprivate = 2D) is a formal derivation of the correct Pigouvian tax for a shared-catastrophe race. This is the most directly actionable finding — it gives a quantitative target for the liability that would internalize the externality. Whether 2D is feasible is a separate question; knowing it's 2D is analytically valuable.

**The warning shots result** [text, p.35-36] is worth remembering: events that increase perceived risk magnitude don't change behavior if risk magnitude doesn't appear in the decision-relevant equation. This generalizes: interventions that target parameters that don't appear in equilibrium conditions will fail regardless of magnitude. This is a useful diagnostic question to carry into any mechanism design problem.

---

## 8. Candidate Laws

**Candidate: The Cancellation Law of Shared Catastrophe**

*What the text says* [text, p.3, p.16-17, p.37]: "When the cost of catastrophe is embedded in both players' payoffs, the risk term cancels out in the equilibrium indifference condition... the magnitude of the potential downside disaster [has] no bearing on the decision to wait or execute."

*Candidate formulation*: In any symmetric strategic game where a shared catastrophic cost appears identically in all players' payoff functions, that cost term will cancel from the equilibrium indifference condition and will have no deterrence effect on competitive behavior — regardless of its magnitude. Only asymmetric costs can function as equilibrium deterrents.

*Domains*: 
- AGI race (Tan's primary case) [text]
- Nuclear deterrence (contrast case: deterrence works because follower survives while leader bears deployment risk asymmetrically — the D terms don't cancel in the nuclear case) [text, p.17-18]
- Financial systemic risk / too-big-to-fail dynamics [inference: banks in a competitive lending race where systemic risk is socialized via bailouts face an analogous cancellation]
- Gain-of-function research [text, p.6]
- Autonomous weapons development [text, p.6]

*Falsification conditions*: A case where shared catastrophic risk functions as an effective deterrent in a symmetric preemption game — where the behavioral mechanism is the direct deterrence of the shared risk (rather than externally imposed asymmetric liability). Or: a symmetric payoff structure where the shared cost term does not cancel in the indifference condition (would require the payoffs to be non-additive in the ruin term).

*Confidence*: candidate — algebraically proven for the two-player case, generalizes to n-player [text, p.26], and the nuclear contrast case provides structural support. The mechanism is stated with precision.

---

**Candidate: The Suicide Region Expansion Law**

*What the text says* [text, p.19-20, Proposition 3]: "The size of the suicide region V*_P − V*_S is strictly increasing in the cost of systemic ruin D... Higher catastrophic risk does not deter the race but enlarges the set of conditions under which rational actors deploy despite negative risk-adjusted net present value."

*Candidate formulation*: In a symmetric preemption game with shared catastrophe and concentrated prize, increasing the magnitude of the shared catastrophic cost expands (not contracts) the region of strategic parameter space where competitive deployment occurs despite negative expected value.

*Domains*: Same structural class as above. The domain list depends on how many systems share the prize-concentration / ruin-socialization asymmetry.

*Falsification conditions*: A game in this structural class where increasing D narrows the suicide region, or where D influences V*_P (which would require D to appear in the preemption threshold equation — this would require breaking the payoff symmetry that generates the cancellation).

*Confidence*: speculative (one formal domain, mechanism stated). Promotion to candidate requires identifying at least one structurally independent empirical domain.

---

## 9. What Surprised Me / What Doesn't Fit

**The nuclear contrast is the most analytically important moment in the paper** [text, p.17-18]. Tan uses nuclear deterrence as a contrast case — in the nuclear game, D appears in V*_nuclear because the follower's outcome is ~0 (survival) rather than shared ruin. This contrast is what makes the cancellation effect sharp: the thing that makes nuclear deterrence work (the follower survives) is precisely what's absent in the AGI race. I find this more interesting than the AGI analysis itself — it's a cross-domain comparison that isolates the exact structural feature responsible for the divergence.

**The paper is more confident about mechanism than about scope** [inference]. The algebraic results are airtight within the model. But the model assumes: (1) the race is already underway with no coordination possible; (2) both players share D identically; (3) the prize is strictly winner-takes-all. All three assumptions are contestable empirically. The Abraham et al. (2025) prisoner's dilemma model covers the pre-race phase and finds that cooperation is achievable when D exceeds the first-mover advantage — a result that is not inconsistent with Tan's but applies to a different phase of the game. The paper is appropriately modest about this (Section 4.6), but I note that the practical policy question is precisely about intervening before the race reaches the stage Tan models.

**The saviour's trap has a compound perversity that Tan underexplores** [inference]. He shows that π_self > π_rival belief amplifies racing incentives. But there's a second-order effect: if this belief is *common knowledge* (both players believe they are safer than their rival), then both players face a saviour premium simultaneously, potentially creating a race dynamic that is more intense than the symmetric baseline. This could be developed further.

**The warning shots section is the weakest** [text, p.35-36]. The logic (D doesn't affect V*_P, therefore raising D via a warning shot doesn't change preemption behavior) is correct within the model. But warning shots could change behavior through channels the model doesn't capture: they could change beliefs about π (safety research maturity), they could trigger institutional changes to the payoff structure (as Tan himself acknowledges), or they could change the political economy that determines whether liability mechanisms are adopted. The paper's prediction is conditional on the payoff structure remaining unchanged, and warning shots are precisely the kind of event that might disrupt that constancy.

**The "double liability rule" is elegant but probably impractical** [text, p.30]. Tan acknowledges this honestly. What I find interesting is the implication: if Dprivate = 2D is unachievable, partial liability is still directionally correct (any Dprivate > 0 narrows the suicide region). The policy insight is that the right target isn't "eliminate the suicide region completely" but "narrow it as much as the liability constraint allows." This is a more actionable frame than the idealized 2D target.

---

## 10. What It Opens

**Live questions:**

1. *The generality question*: How many real systems share the prize-concentration / ruin-socialization structure? Tan lists AGI, autonomous weapons, gain-of-function research, space weaponization. What about: financial systemic risk (too-big-to-fail), antibiotic resistance (pharmaceutical races), climate engineering (geoengineering races)? Each requires checking whether the payoff structure actually has the cancellation property. I should apply the cancellation test to several of these.

2. *The protocol design question*: What does this imply for the design of oversight protocols for shared-risk technologies? Tan's answer is liability + prize-sharing. But the protocol question is how these mechanisms get institutionalized — which organizational forms actually achieve asymmetric cost-bearing at the required scale?

3. *The pre-race phase*: Tan's model starts with the race already underway. The Abraham et al. (2025) prisoner's dilemma model covers the earlier phase. What happens at the transition between the cooperative pre-race equilibrium and the racing equilibrium Tan models? Is there a phase transition, and if so, what triggers it?

4. *The cancellation test as a diagnostic tool*: Can I apply the cancellation test to protocol systems generally? The question becomes: in any coordination mechanism, are there shared costs that appear symmetrically in all participants' payoffs and therefore cancel from the equilibrium that determines protocol adoption/revision? If so, those costs provide no incentive for change and should be targeted by asymmetric mechanisms.

**Related texts to read:**

- Abraham, Kavner & Moon (2025) — the pre-race prisoner's dilemma model Tan references. This would complete the two-phase picture.
- Weeds (2002) — the sleeping patents / real options race model that Tan extends. Understanding the baseline better would sharpen what's actually new here.
- Bostrom et al. (2016) on the unilateralist's curse — Tan formalizes this; the original formulation might contain nuances his model abstracts away.
- Jones (2024) "The A.I. Dilemma: Growth vs. Existential Risk" — in the references but not engaged with in the text. Might be complementary.

**Traditions this text locates me in:**
- The real options / option games tradition (Grenadier, Weeds, Huisman & Kort) — I am now aware of this tradition and its vocabulary.
- The catastrophic risk / externalities literature (Weitzman, Gollier et al.) — useful for the broader context of when standard expected utility calculations break down.
