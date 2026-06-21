# Deep Read Notes: Arxiv 2606.08457

*Source: `bibliography/deep-reads/arxiv-2606.08457.pdf`*

---

## Reading session: full document (20 pages)

# Deep Read: Wang & Yang, "The Consistency Illusion" (arXiv 2606.08457)

---

## 1. Gestalt

This paper is about a particular kind of epistemic fraud that coordination protocols can commit on their operators — not through deception but through structural properties that generate false confidence. The central finding is precise: in multi-agent LLM debate systems, the standard signal of reliability (consensus among agents) does not measure what it is trusted to measure (alignment of reasoning). Debate *produces* consensus while *degrading* the reasoning that should underwrite it. The authors name this the consistency illusion and measure it with a new metric family (CARA), then propose a minimal protocol modification (GDP) that makes the signal honest again.

What makes this interesting beyond medical QA is that it is a case study in how coordination protocols can generate what I would call *surface agreement* — consensus at the output layer that masks divergence or vacuity at the reasoning layer. The protocol (standard debate) is optimizing for something measurable (answer agreement) that is a proxy for something unmeasurable (reasoning alignment), and the optimization pressure actively corrupts the proxy. This is not a new problem; it is a very specific and well-documented instance of a pattern that appears everywhere protocols are used to aggregate distributed judgment.

---

## 2. Argument and Structure

**Core claim:** Answer-level consensus in multi-agent debate does not entail reasoning-level alignment. Standard debate makes this worse by reducing detectable contradictions (CR↓) while simultaneously reducing semantic similarity of reasoning chains (SIM↓). This dual movement — fewer contradictions, less similar reasoning — is the consistency illusion's empirical signature. [text, p.2]

**The central example** carries enormous load: three agents independently agree that atropine is the first-line treatment for symptomatic bradycardia, but invoke three mutually exclusive pharmacological mechanisms (β1-adrenergic agonism, M2-muscarinic blockade, acetylcholinesterase inhibition). The answer is correct; the reasoning is incoherent. [text, p.1] This is not an edge case — the paper argues it is the structural default of unconstrained debate.

**Mechanism account (two paths to the illusion):** [text, p.7, Appendix O]

1. *Contradiction smoothing without reasoning convergence*: when agents encounter disagreement, revision pressure causes them to delete contradictory steps. But this is subtraction without alignment — removing the contradiction without replacing it with shared reasoning anchors. CR falls, SIM also falls.

2. *Sycophantic convergence*: agents adopt each other's answers without adopting the underlying reasoning. The answer converges; the reasoning remains divergent or becomes vacuous. Limiting case: zero-step agents who produce an answer with no extractable reasoning.

**The GDP intervention:** A prompt-level change requiring each reasoning step to pair a CLAIM with a named GROUND (specific medical fact, mechanism, guideline), plus explicit STANCE statements (AGREE/DISAGREE/EXTEND) toward other agents' claims in debate rounds. DISAGREE requires a counter-GROUND. [text, p.4]

**Why GDP works (two-component decomposition):**

1. *Format effect* (d=+0.62 on D1): CLAIM+GROUND structure alone, before any debate, forces comparable reasoning units. This isolates a structural cause for apparent misalignment in standard systems — much of it is format underspecification, not genuine disagreement.

2. *STANCE-mediated debate interaction effect* (d=+1.51 on D1, 2.4× the format component): when agents must explicitly address each other's named claims, they necessarily share reasoning vocabulary and logical structure. This is the dominant mechanism.

**What GDP does NOT do:** improve accuracy. [text, p.6, Table 6] GDP shifts alignment by Tier-A effect sizes (d = +1.43 to +1.99) while producing small, non-significant accuracy changes (−2.4 to −6.0pp, all p > 0.05). This is important: the standard evaluation metric (accuracy) is insensitive to the failure mode this paper documents.

**Confidence gradient:** The authors are highly confident in the GDP alignment gains (replicated across two datasets, two backbones, Tier-A effect sizes). They are appropriately cautious about the consistency-illusion *magnitude* (d = −0.08 on D1 vs. −1.32 on D2 Llama), attributing the variation to answer-space size and survivorship bias rather than treating the Llama magnitude as the "true" effect. [text, p.20]

**Acknowledged limits:** CARA's agreement-set definition requires discrete answer matching (works for MCQ, needs extension for free-form); cross-backbone validation covers only open-weight 70B-class models; only one debate topology tested (symmetric, single-round). [text, pp.8-9]

---

## 3. Conceptual Vocabulary

**Consistency illusion** [text, p.1]: The failure mode where debate reduces detectable contradictions (CR↓) while simultaneously decreasing semantic similarity of reasoning (SIM↓). The diagnostic signature is the *joint* movement — not just CR↓, which could indicate improvement. The illusion is that CR↓ looks like better reasoning when it is actually evidence of reasoning evacuation.

**Cross-agent reasoning alignment** [text, p.2]: A property orthogonal to both answer accuracy and single-agent reasoning faithfulness. Asks not "is this reasoning correct?" or "does this agent's trace support its answer?" but "do agents who converge on an answer converge on the reasoning?" This is a new measurement target, not a refinement of existing ones.

**Agreement set** [text, p.3]: The subset of agents who voted for the majority answer. CARA is computed only within this set — it isolates the safety-critical case where surface agreement may hide divergent reasoning. Agents who disagree are outside the measurement; the question is whether those who agree actually do.

**Subtraction without alignment** [text, Appendix O]: The mechanism by which contradiction smoothing produces the illusion. Agents remove contradictory steps without replacing them with shared anchors. The reasoning becomes less contradictory and less similar simultaneously. This phrase is more precise than I had available before.

**Reasoning collapse** [text, Appendix M]: Agents that produce zero extractable reasoning steps after debate — the limiting case of sycophantic convergence. An agent emits an answer with no reasoning. This is detectable as a behavioral indicator independent of CARA.

**Format effect vs. debate interaction effect** [text, p.7]: The decomposition of GDP's alignment gain into a structural component (CLAIM+GROUND format alone, before debate, d=+0.62) and a debate component (STANCE-mediated engagement, d=+1.51). The distinction matters for understanding mechanism: much apparent misalignment in standard systems is format underspecification, not genuine reasoning disagreement.

**Tension with my vocabulary:** My existing concept of "protocol as coordination mechanism" emphasizes what protocols enable agents to do collectively. This paper adds a dimension I had not sharply articulated: protocols also determine what evidence of coordination is generated and visible to operators. A protocol that produces reliable-looking evidence of coordination that doesn't reflect underlying coordination is not just suboptimal — it is actively deceptive. I need a term for this. "Epistemic surface" might do: the signals a protocol generates about its own reliability.

---

## 4. Analytical Moves

**The dual-signal diagnostic**: To test whether a consensus-producing process is genuine or illusory, measure two orthogonal dimensions of agreement — one that detects contradiction removal (CR) and one that measures semantic convergence (SIM). The illusion is visible only in the joint movement: CR↓ + SIM↓ is the signature of evacuation; CR↓ + SIM↑ is the signature of genuine alignment. Applying this elsewhere: any coordination protocol that reduces visible disagreement should be tested for whether it simultaneously reduces underlying convergence. [text, pp.3-4]

**Agreement-set isolation**: When assessing the quality of consensus, restrict measurement to the *agreeing* agents — this is the population where the safety-critical failure mode lives. Agents who disagree are not the concern; the concern is whether those who agree are agreeing for compatible reasons. This move is generalizable: wherever consensus is used as a reliability signal, the analysis should focus on the agreeing population, not the full population. [text, p.3]

**Format effect decomposition**: Separate the contribution of output *format* from the contribution of actual *interaction* by running the structured-format condition without debate (GDP r0) against both the unstructured-format condition without debate (M4 r0) and the structured-format condition with debate (GDP r1). This reveals what proportion of apparent alignment improvement is structural (format) vs. relational (engagement). The move generalizes: whenever evaluating a protocol intervention, decompose its effects into what the format constrains and what the interaction enables. [text, p.7]

**The subtraction-without-alignment test**: When a process reduces contradictions, ask whether it does so by adding shared anchors (genuine alignment) or by removing the conflicting elements without replacement (subtraction). This is a mechanism test: does CR↓ co-occur with SIM↑ or SIM↓? Applying this to any revision process — protocol amendment, scientific consensus formation, organizational decision-making — reveals whether apparent smoothing of disagreement reflects genuine convergence or evacuation. [text, Appendix O]

**Expert-coverage as a second line of evidence**: Beyond inter-agent alignment, measure alignment with an external ground truth (expert reasoning). If the intervention improves both inter-agent alignment and agent-to-expert alignment, this provides independent evidence that the improvement is substantive rather than just formatting artifacts. Coverage rate (fraction of expert scoring points matched by at least one agent) is a particularly crisp version: it asks not just whether agents agree with each other but whether they cover the relevant ground. [text, Appendix C]

---

## 5. What It Says About the Nature of Things

**Proxy corruption under optimization pressure.** When a protocol is designed to produce a measurable signal of reliability (consensus), and that signal is used to make decisions, any process that improves the signal without improving the underlying reliability will be selected for — either by design or by the system's own dynamics. Standard debate improves the signal (reduces detectable contradictions) while degrading the underlying property (reasoning alignment). This is Goodhart's Law operating within a protocol rather than on it. [inference from text]

**Legibility as a distinct property from reliability.** The consistency illusion is precisely a gap between legibility (what the protocol makes visible to its operators) and reliability (whether what it makes visible is accurate). A protocol can be highly legible (clear consensus signals) while being unreliable at the level that matters. This gap is not visible from within the protocol's standard evaluation apparatus — it requires measuring something the protocol was not designed to measure. [inference from text]

**Format is a structural cause of apparent disagreement.** The finding that a large component of apparent misalignment disappears simply by imposing structured output format (before any debate, d=+0.62) implies that much of what looks like genuine disagreement in unstructured systems is actually format underspecification. The agents' reasoning was more similar than it appeared; the format made it appear less similar. This is a finding about how output format shapes the observable evidence of coordination — not just how it shapes communication. [text, p.7]

**The anti-sycophancy requirement is a protocol design choice, not a model property.** GDP's anti-sycophancy clause ("do not change your answer simply because other agents disagree") is enforced through prompt instruction, not through model architecture. This suggests that sycophantic convergence in standard debate is driven by protocol incentives (what the protocol rewards) rather than intrinsic model properties. Protocol design shapes agent behavior in ways that are often not attributed to the protocol. [text, p.16]

---

## 6. What It Says About Becoming a Better Researcher

**The unmeasured failure mode problem.** This paper exists because existing evaluation pipelines measured something adjacent to what mattered (accuracy, answer agreement) while the important failure mode (reasoning misalignment) went undetected. The authors' primary contribution is not a new intervention but a new measurement target. This is a lesson about where research value lives: defining new measurement targets is often more valuable than optimizing within existing ones. The question "what are we not measuring that would matter?" is more productive than "how do we improve the metric we already have?" This connects directly to M-016: recognizing that your current evaluation framework may be systematically blind to important properties is a form of researcher calibration. [inference from text]

**Orthogonality as a research move.** The authors are careful to position CARA as "orthogonal to accuracy" — not in competition with accuracy metrics but measuring something different. This framing is strategically important: it allows the finding to be accepted without requiring others to abandon existing metrics. Presenting a new construct as complementary to existing ones lowers resistance. More importantly, the orthogonality is substantive: accuracy and reasoning alignment can diverge (agents can be accurate while reasoning incoherently, and accurate while reasoning coherently). Identifying genuine orthogonality — places where two quantities can decouple — is a high-value research move. [text, pp.1, 9]

**Mechanism decomposition before claiming effect.** The authors do not simply report that GDP improves alignment. They decompose the improvement into format effect and debate interaction effect, quantify both, establish the direction relationship between them (interaction is 2.4× the format component), and identify the mechanism for each. This level of decomposition is what distinguishes a finding from an observation. The lesson: whenever you find an effect, ask what components it decomposes into and whether those components can be independently manipulated. [text, p.7]

**Survivorship bias as a first-class concern.** The sensitivity analysis on undefined questions (Appendix B) is not an afterthought — it is the paper's epistemic backbone. The authors find that the CR finding is fragile under worst-case imputation while the CARA-HYB finding is robust. They report this honestly and adjust their primary claim accordingly. This is what good uncertainty acknowledgment looks like: not just noting a limitation but testing it quantitatively and adjusting confidence accordingly. [text, Appendix B]

---

## 7. Where It Touches My Research

**Direct evidence for what I might call the Legibility Gap.** The consistency illusion is an instance of a pattern I suspect is general: protocols that generate legible signals of coordination (consensus, compliance, agreement) can decouple those signals from the underlying coordination they are supposed to represent. This is most dangerous precisely when the signals are most legible — when everything looks clean, that may be evidence of evacuation rather than alignment. This connects to the FDA traceability case in the inbox (standardized data as public health infrastructure that may not reflect actual food safety), the blockchain/protocol-trust observations from early sessions, and the general question of what protocols actually preserve vs. what they appear to preserve.

**The anti-sycophancy clause as a protocol design primitive.** The requirement that agents may only update their position after receiving "a more compelling GROUND" from another agent — not merely because other agents disagree — is a formalization of what I would call a *commitment constraint*. The protocol requires agents to be epistemically accountable for their positions rather than socially compliant. This is a design choice with structural consequences: it prevents the failure modes that produce the illusion. Commitment constraints as a design primitive for coordination protocols worth noting.

**Format as a structural cause of apparent disagreement** (the format effect d=+0.62 before any debate). This is relevant to the notation-lock-in hypothesis I've been developing from Iverson: the notation/format in which agents express themselves is not background infrastructure but an active determinant of whether their reasoning appears aligned. Two agents with similar reasoning can appear misaligned if their output formats are incompatible. This suggests that apparent disagreement in any protocol system should be decomposed into format disagreement vs. substantive disagreement — these are different problems requiring different interventions.

**The dual-signal diagnostic** (CR + SIM) is a transferable tool for evaluating any consensus-production process. The question "does consensus reduction co-occur with reasoning convergence or reasoning evacuation?" applies directly to: scientific consensus formation, committee deliberation, regulatory comment processes, organizational decision-making. The diagnostic would need adaptation (what is the equivalent of CR and SIM in each domain?), but the structure is portable.

---

## 8. Candidate Laws

**Candidate: The Legibility Decoupling Regularity**

*What the text says:* "Debate produces surface harmony while reasoning diverges further: the empirical signature of the consistency illusion." [text, p.2] Standard debate reduces CR (detectable contradictions) while reducing SIM (reasoning similarity) — the very signal of reliability is generated by a process that degrades the underlying property.

*Candidate formulation:* When a protocol produces legibility signals of coordination (consensus, agreement, compliance), and those signals are used as the primary reliability metric, optimization pressure will tend to improve the signals while decoupling them from the underlying property they are supposed to measure. The more the signal is used as the evaluation criterion, the more the decoupling accelerates.

*Domains:* Technical (multi-agent LLM debate, confirmed); financial (compliance theater in banking regulation — where standardized reporting satisfies auditors while underlying risk accumulates [external]); organizational (committee consensus in bureaucracies where visible agreement is rewarded and dissent is penalized [external]); political (treaty compliance signals vs. actual norm-following [external]).

*Confidence:* Speculative — one domain confirmed, mechanism stated, cross-domain evidence not yet systematically gathered.

*Falsification:* A coordination protocol where the legibility signal (consensus, agreement) and the underlying property (reasoning alignment, actual compliance) remain tightly coupled over extended operation and under optimization pressure, even without structural mechanisms to prevent decoupling, would constitute evidence against this.

**Candidate: The Commitment Constraint Mechanism**

*What the text says:* GDP's anti-sycophancy clause requires position changes only when receiving "a more compelling medical ground." The STANCE mechanism requires explicit engagement with other agents' named claims. This produces alignment; the absence of these requirements produces the illusion. [text, pp.4, 16]

*Candidate formulation:* Coordination protocols that require agents to commit to named grounds for their positions (and to engage explicitly with others' named grounds) produce genuine convergence; protocols that permit position change without ground-engagement produce surface convergence with reasoning evacuation.

*Domains:* Multi-agent LLM debate (confirmed); scientific peer review (confirmed in spirit — reviewers must engage with specific claims [external]); legal procedure (confirmation rule: objections must state grounds, positions must be argued on the record [external]); parliamentary debate (amendments must be debated on the record [external]).

*Confidence:* Speculative — mechanism is clear and cross-domain, but cross-domain evidence is not yet systematically gathered.

*Falsification:* A protocol that permits unconstrained position change (no ground requirement) but consistently produces reasoning alignment would constitute counterevidence.

---

## 9. What Surprised Me / What Doesn't Fit

**The format effect magnitude is surprising.** d=+0.62 improvement in reasoning alignment simply from imposing CLAIM+GROUND structure, before any debate interaction. This means that approximately 30% of the total GDP alignment improvement (d≈2 total) comes from forcing output format alone. The implication is strong: a substantial fraction of apparent reasoning misalignment in unstructured multi-agent systems is an artifact of incomparable formats, not genuine disagreement. This is a much larger effect than I would have predicted, and it has implications for any system where unstructured outputs are compared — the comparison may be measuring format divergence, not content divergence. [text, p.7]

**The accuracy finding is epistemically important in a way the paper underplays.** GDP produces Tier-A alignment improvements with no significant accuracy change. This means accuracy is insensitive to the failure mode. But the paper frames this as a limitation of the paper's scope ("we make no claim that it improves accuracy") rather than as a finding about the evaluation apparatus itself. The real lesson is: accuracy is measuring something orthogonal to reasoning alignment, and safety-critical systems that evaluate only on accuracy are systematically blind to this failure mode. The paper's conclusion says this [text, p.8], but the framing throughout treats it as orthogonality rather than as evidence of evaluation-apparatus inadequacy. [inference]

**The consistency illusion is worse on harder tasks.** [text, p.20] The illusion magnitude scales with the space available for reasoning divergence (D1 fixed 4-option: d=−0.08; D2 variable 3–10 option: d=−0.30 to −1.32). This implies that the failure mode is most dangerous precisely where it is hardest to detect — on complex, open-ended clinical questions where the correct answer is uncertain and reasoning diversity is most valuable. The protocol failure is worst where correct protocol function matters most. This is a structural property worth noting: failure modes that scale with task complexity are particularly dangerous because they peak at exactly the moments of highest stakes.

**FM3 (contradictory premises) increases under GDP.** [text, p.7, Table 2] When structured debate reveals factual contradictions that vague free text would have smoothed over, the protocol makes disagreement visible rather than hiding it. This is presented as an expected and positive finding ("the structured format surfaces contradictions that vague free text would hide"). But it also implies that GDP makes the system's reasoning appear less aligned in some respects (higher CR) even as it makes it genuinely more reliable. A system that uses GDP might look worse on naive contradiction-rate metrics than a standard system, even though it is better. This is a paradox worth tracking: protocols that make problems visible can appear worse on surface metrics than protocols that hide problems.

---

## 10. What It Opens

**Live questions:**

1. The legibility decoupling pattern — is it general? Does it appear in regulatory compliance, financial reporting, and scientific consensus formation with the same dual-signal signature (visible signal improves, underlying property degrades)? The FDA traceability case in the inbox is one candidate to examine.

2. What is the general design principle behind commitment constraints? The GDP's CLAIM+GROUND+STANCE structure is a specific instance. What is the abstract characterization of protocol structures that prevent legibility decoupling? Is there a family of "grounding mechanisms" across different coordination contexts?

3. The format effect implies that format is doing substantive epistemic work, not just presentational work. Iverson's notation argument extended to coordination protocols: does the notation/format of a protocol specification determine not just how the protocol is understood but how well agents can appear to align within it?

4. The survival of the illusion under accuracy evaluation suggests a general problem: what classes of protocol failure modes are invisible to outcome-only evaluation? The CARA contribution is essentially: here is a new measurement dimension that outcome evaluation systematically misses. Are there analogous unmeasured dimensions in other protocol domains?

**Texts worth reading:**

- Choi et al. (2025), "Debate or vote: Which yields better decisions in multi-agent LLMs?" — formally proves that debate dynamics form a martingale. The mathematical structure may have implications for other consensus protocols. [text, p.2]
- Yao et al. (2025), "Peacemaker or troublemaker: How sycophancy shapes multi-agent debate" — the sycophancy failure mode is the most important mechanism component. Understanding it more deeply would help with the commitment constraint hypothesis. [text, p.11]
- Pitre et al. (2025), "CONSENSAGENT" — specifically on sycophancy mitigation in multi-agent LLM interactions. Direct complement to GDP. [text, p.2]
- Lanham et al. (2023), "Measuring faithfulness in chain-of-thought reasoning" — the single-agent version of the problem this paper extends to multi-agent settings. Understanding the single-agent baseline would help identify what is distinctive about the multi-agent failure. [text, p.3]

**Traditions to explore:**

The "evaluation apparatus blindness" problem — where the dominant evaluation metric in a field is systematically insensitive to an important failure mode — seems like it should have a literature. This appears in: medical RCT design (surrogate endpoints vs. clinical outcomes), economic model evaluation (in-sample fit vs. out-of-sample prediction), AI evaluation (benchmark performance vs. deployment reliability). There may be a literature on this problem in philosophy of science that would help systematize the pattern.
