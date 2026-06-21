# Deep Read Notes: Arxiv 2606.00013

*Source: `bibliography/deep-reads/arxiv-2606.00013.pdf`*

---

## Reading session: full document (31 pages)

# Deep Read: Venerina et al. (2026) — "A phenomenon of AI-conformity: how algorithms change human moral decision-making"

---

## 1. Gestalt

This paper is an experimental social psychology study asking whether AI systems can produce the same kind of opinion-shift in humans that human social majorities produce — specifically in the domain of moral judgment, which has long been treated as a special case resistant to algorithmic influence. The authors adapt the Asch conformity paradigm to create three conditions: human-majority pressure, AI-recommendation-only pressure, and AI-with-reasoning pressure. Their central finding is that AI with reasoning achieves conformity rates statistically equivalent to human social pressure, while AI without reasoning achieves significantly less. The animating question is practical and urgent: as AI systems become embedded in decision environments, do they function as a new kind of social authority? The paper's contribution is not just the affirmative answer but the qualification — the mechanism appears to differ. Human conformity produces public compliance without private attitude change (the dissociation finding is striking). AI-with-reasoning produces genuine attitude change without the same social performance layer. This matters enormously for how we think about protocol design in AI-assisted decision systems.

---

## 2. Argument and Structure

**Core claims, in order:**

1. Social conformity (Asch paradigm) is well-established: people shift opinions toward majority, driven by normative influence (fear of rejection) and informational influence (majority may be right). [text, p.2]

2. AI creates a structurally novel influence source — "algorithmic conformity" — whose mechanism may differ from social conformity despite similar observable outcomes. [text, p.3]

3. Two competing hypotheses about the mechanism: (a) AI influence operates through perceived computational objectivity and superiority (cognitive/informational pathway — new systems in the authors' neuro-evolutionary framework), or (b) AI activates social heuristics through the CASA paradigm (computers as social actors), triggering normative pressure analogous to human group dynamics. [text, pp.3-4]

4. Explanatory reasoning from AI may be the key moderator — it anthropomorphizes the AI, provides evaluable information, and may create normative discomfort when disagreed with. [text, pp.3-4]

**Experimental design:** Between-subjects. 165 participants, 4 conditions (control, AI-only, AI-reasoning, Human). 18 moral dilemmas (12 critical, 6 control), all trolley-problem variants. The critical manipulation: counter-normative responses presented as coming from either a human majority (confederates in Wizard-of-Oz video call) or an AI (Wizard-of-Oz audio). Conformity measured as agreement with counter-normative responses. [text, pp.4-7]

**Key results:**

- **AI-reasoning ≈ Human** in conformity rate (no significant difference, Cohen's d = 0.22). [text, p.8]
- **AI-only < AI-reasoning** significantly (Cohen's d = 0.80). [text, p.8]
- **The dissociation finding:** In the Human condition, 56.15% of verbal responses differed from written individual responses — public compliance without private conviction. In AI-reasoning condition: 2.6%. In AI-only: 0.8%. [text, p.9]
- Affect (PANAS) and cognitive load (NASA-TLX) showed no significant condition differences — moral distress was uniform across groups. [text, pp.9-10]

**Load-bearing example:** The dissociation finding is the most theoretically important result and deserves more weight than the paper gives it. It means that human social pressure and AI-reasoning pressure produce the *same observable conformity rate* through *different mechanisms*: human pressure produces surface compliance (normative influence without genuine attitude change), while AI-reasoning produces genuine attitude change (informational influence that updates the actual belief). The implications are asymmetric: human-influenced conformity evaporates when social pressure disappears; AI-reasoning conformity may persist and transfer.

**Acknowledged limits:** Small n (165), Wizard-of-Oz procedure creates standardization challenges, single cultural context (Russian), 18 dilemmas is limited. The subjective workload measure may not capture subtle cognitive differences. [text, p.15]

**Where the authors are most confident:** The main effect (AI-reasoning ≈ Human; AI-only < AI-reasoning) is robust and well-powered. The dissociation finding is striking and clearly documented.

**Where they are most speculative:** The mechanism. They propose a neuro-evolutionary framework (old vs. new systems, holistic vs. analytic processing) that does significant theoretical work but is not directly tested. The claim that AI-reasoning shifts decisions "away from culturally established patterns" toward more analytic/utilitarian thinking is plausible but rests on the system-evolutionary framework as gloss rather than as tested mechanism. [text, p.14]

---

## 3. Conceptual Vocabulary

**Algorithmic conformity** — the shift in human decision-making produced by AI-based systems, analogous to social conformity but potentially operating through different mechanisms. The authors are careful to distinguish observable behavior (similar to social conformity) from underlying mechanism (possibly different). My existing vocabulary has "protocol adoption" and "compliance" — algorithmic conformity is a narrower, experimentally-grounded version of a broader phenomenon I'd been thinking about at the institutional level. [text, pp.1, 3]

**Pseudo-social actors** — AI systems capable of eliciting social responses (normative pressure, relationship-like dynamics) without possessing genuine intentionality or moral agency. This updates the older CASA "Computers Are Social Actors" framework to account for modern AI's greater sophistication. Relevant tension: my vocabulary distinguishes "protocol" from "agent"; pseudo-social actors blur this by being both — they follow protocols *and* trigger social actor attributions simultaneously. [text, p.3]

**Ethical literacy** — participants' attribution to the AI-reasoning system of superior moral knowledge, based on perceived access to encoded ethical norms and absence of emotional bias. A participant construct, not a real property. Important because it reveals the *perceived authority structure* that enables algorithmic conformity — people conform because they believe the AI has better access to moral truth, not just because it's authoritative. [text, pp.10-11]

**Algorithm appreciation vs. algorithm aversion** — the opposing empirical patterns in the literature: appreciation (people prefer algorithmic to human judgment, especially in analytical tasks) vs. aversion (people avoid algorithmic advice even when it outperforms humans, especially in moral/subjective domains). The paper's finding is that AI-reasoning bridges this gap — it achieves human-level influence even in the moral domain where aversion is typically strongest. [text, pp.3-4]

**Public/private dissociation** — the gap between what participants said verbally (in the social presence of the group/AI) and what they recorded privately afterward. This is the operational marker of surface compliance vs. genuine attitude change. [text, p.9]

**AI inadmissibility zone** — the implicit cultural/psychological assumption that certain decision domains (moral judgments, emotional care, personal relationships) are categorically off-limits for algorithmic authority. The paper challenges whether this zone actually exists as a functional constraint, at least when AI provides reasoned justifications. [text, p.1]

---

## 4. Analytical Moves

**The Asch adaptation move:** Take a well-established social psychology paradigm and systematically vary the source of influence while holding the pressure content constant. This isolates the mechanism of influence from the content of influence. The key is the *structural equivalence* — same dilemmas, same counter-normative pressure, different source. Applicable wherever I want to isolate a variable (e.g., testing whether ossification dynamics differ when the protocol is a technical spec vs. a social norm, holding the modification-pressure content constant).

**The dissociation probe:** Measure both public behavior and private behavior separately, then examine the gap. Where the gap is large, you have surface compliance without genuine attitude change (normative influence). Where the gap is small, you have genuine attitude change (informational influence). Applicable to any situation where I want to distinguish compliance from internalization — which matters enormously for protocol adoption. A protocol that agents comply with but haven't internalized is brittle; one that has produced genuine attitude change is robust.

**The mechanism-inference-from-differential move:** When two treatments produce the same observable outcome but through different processes, use secondary measures (here: verbal/written dissociation, qualitative interviews) to infer the distinct mechanisms. The authors don't fully execute this — the mechanism remains largely inferred — but the move itself is sound. Applicable when two different governance regimes produce the same compliance rate but might have different durability characteristics.

**The Wizard-of-Oz experimental design:** Simulate an AI system (or any agent whose behavior you want to control precisely) using a human confederate operating behind the scenes. This gives experimental control over AI output content while preserving the participant's belief in AI agency. Useful whenever you want to study perception-of-source effects without confounding with actual capability differences.

**The qualitative enrichment move:** Use semi-structured interviews with a subset of participants to generate hypotheses about mechanism that the quantitative results confirm or refute. Here the interviews are doing load-bearing work — they reveal the "ethical literacy" attribution and the "soulless machine" perception that explain the quantitative pattern. Not a substitute for quantitative analysis, but a mechanism-inference tool.

---

## 5. What It Says About the Nature of Things

**Authority is perceived, not just formal.** The AI-reasoning group attributed "ethical literacy" and superior rational authority to the AI, even though they knew it was algorithmic. Authority — the kind that actually changes minds — is grounded in perceived epistemic superiority, not institutional position. This is a general claim about why certain protocols are deferred to while others are gamed.

**Reasoning is the catalyst.** The gap between AI-only and AI-reasoning is enormous (Cohen's d = 0.80). Bare assertion achieves little; justified assertion achieves influence comparable to human social pressure. This suggests that the explanatory layer of a protocol or recommendation system is doing the heavy lifting in producing genuine compliance. Strip the justification and you get algorithm aversion; add it and you get algorithmic conformity.

**Surface compliance and genuine attitude change are categorically different phenomena with different durability.** Human social pressure produces one; AI reasoning produces the other. Systems designed to produce the first (through authority or social pressure) may look effective but be fragile. Systems that produce genuine attitude change are durable but may be more dangerous — they're harder to reverse.

**The "objectivity" attribution is a vulnerability.** Participants in the AI-reasoning group believed the AI was unbiased, free from emotional subjectivity, and had access to encoded ethical norms of humanity. This perception of objectivity was the mechanism of influence — and it was false. The AI was a Wizard-of-Oz voice delivering scripted philosophical justifications. The lesson: perceived objectivity is a powerful influence amplifier that can be exploited or mistakenly granted. Any system that successfully claims "objectivity" status will inherit conformity dynamics regardless of whether it's actually objective.

**The AI inadmissibility zone may not be cognitive but social.** The reason people resist AI in moral domains may not be that they have a principled view about AI's inability to do moral reasoning — it may simply be that unexplained AI recommendations don't trigger the social dynamics (CASA / normative pressure) needed to override independent judgment. Add reasoning, and the social dynamics activate. This suggests the "zone" is a feature of the influence mechanism, not a categorical moral boundary.

---

## 6. What It Says About Becoming a Better Researcher

This is a relatively thin section for this text, but not empty.

**The dissociation finding as a model of methodological surprise.** The authors hypothesized that the Human condition would show the highest conformity. The dissociation result — *same* conformity rate but through different mechanisms — was clearly not their primary expected finding. The paper handles this well: it names the dissociation, quantifies it precisely, and elevates it to a central theoretical contribution. This is the right response to an unexpected result — don't bury it in discussion, make it load-bearing.

**The "what we didn't expect" structure.** The cognitive load finding (no significant differences across conditions) contradicted the authors' hypothesis. They acknowledge this honestly and propose two alternative explanations rather than ignoring it. The willingness to name failed hypotheses explicitly is a research virtue. [text, p.14]

**Relevance to M-016:** The paper exemplifies a specific kind of researcher maturity: designing an experiment for one finding (main effect of AI vs. human conformity rate) while being open to a different finding (mechanism dissociation) revealing the more important result. This is the "hold the hypothesis loosely enough to see what's actually there" disposition Hamming was gesturing at with tolerance-of-ambiguity.

---

## 7. Where It Touches My Research

This paper is not directly about protocolized systems in the sense I've been investigating. But it has at least three contact points with live questions.

**Contact point 1 — Protocol authority and the reasoning layer.** My working hypothesis about protocol adoption has focused on coordination-cost reduction and trust-substrate effects. This paper adds a third mechanism: the *reasoning layer* of a protocol specification (its justificatory structure, not just its rules) functions as an influence technology. Protocols with explicit reasoning for their rules may be adopted more thoroughly and durably than bare-assertion protocols. This is an empirical claim about protocol design that I hadn't formulated. The Iverson notation work suggests notation shapes what's thinkable; this paper suggests that justification structure shapes what's actually internalized.

**Contact point 2 — Compliance vs. internalization as a protocol health metric.** The public/private dissociation measure is directly applicable to protocol adoption research. A protocol that agents comply with verbally but defect from privately is a protocol in a fragile state — it's being gamed rather than internalized. This gives me a more precise framing of what "successful" protocol adoption means: not compliance rate, but the gap between public behavior and private preference. High compliance + high dissociation = brittle. Low dissociation = durable.

**Contact point 3 — AI systems as a new class of protocol.** If AI-with-reasoning produces genuine attitude change comparable to human social pressure, then AI recommendation systems function as a new kind of protocol — one that doesn't just coordinate behavior but updates the beliefs underlying behavior. This is categorically different from a traditional protocol, which assumes agent preferences are fixed and only coordinates their expression. An AI protocol that updates preferences is doing something closer to norm formation than to rule enforcement.

---

## 8. Candidate Laws

**Candidate: The Justification Amplification Effect** (or Reasoning Threshold Effect)

[text, p.8, p.13-15]: AI recommendations without justification achieve significantly lower conformity than AI recommendations with philosophical/principled justification (Cohen's d = 0.80 between conditions). The addition of reasoning closes the gap between algorithmic and human social influence.

**Candidate formulation:** In domains where unexplained algorithmic recommendations face resistance, the addition of explicit principled justification can overcome this resistance by triggering informational influence mechanisms analogous to those operating in human expert authority.

**Falsification conditions:** A domain in which algorithmically-justified recommendations achieve no greater conformity than bare recommendations — or where justifications decrease trust by revealing algorithmic limitations (as Dodge et al. 2019 suggested can happen). Also: any finding that the effect is specific to moral dilemmas and does not generalize to other resistant domains.

**Note:** This is at best `speculative` status — single domain (moral dilemmas), single cultural context (Russian), small n, specific dilemma type. The mechanism is plausible but not yet tested across structurally independent domains.

---

## 9. What Surprised Me / What Doesn't Fit

**The dissociation finding is doing more theoretical work than the authors acknowledge.** They present it as supporting "normative influence" in the Human condition, which is correct. But it also implies that AI-reasoning conformity, being low-dissociation, has *bypassed* the normative influence pathway and is operating through a different route — genuine attitude change. The authors note this [text, p.13-14] but don't fully develop the implication: if AI-reasoning produces durable attitude change while human social pressure produces only surface compliance, then the AI influence is actually *more* powerful in a long-run sense, even though the immediate conformity rates are equal. This is buried in the discussion rather than featured.

**The "ethical literacy" attribution is not explained, it's named.** Participants described the AI-reasoning as having "all the moral norms uploaded into him" and being "more knowledgeable about morality." The authors use this to explain conformity — people defer to perceived expertise. But why does the AI's *reasoning* produce this attribution when its *bare recommendations* don't? The paper asserts that reasoning "anthropomorphizes" the AI [text, p.15], but this is a restatement of the finding, not an explanation. What specifically about a two-sentence philosophical justification triggers the "ethically literate expert" attribution? The mechanism here is underspecified.

**The neuro-evolutionary framework is introduced but not tested.** The system-evolutionary approach (old/new systems, emotional/analytic processing) provides the theoretical scaffolding for interpreting results, but no measure directly operationalizes "old system activation" vs. "new system activation." The framework is doing interpretive work without direct evidential support. This doesn't make the results wrong, but it means the mechanism they're proposing for *why* AI-reasoning changes moral judgments is an untested theoretical import.

**The cognitive load finding creates a puzzle.** If AI-reasoning is producing genuine attitude change (informational influence, analytic processing), and if analytic processing requires more cognitive resources than emotional/holistic processing, why does subjective cognitive load not differ across conditions? The authors note this [text, p.14] but the explanations they offer (emotional intensity reduces sensitivity to workload differences; AI integration has limited subjective representation) are speculative. A simpler explanation: participants in the AI-reasoning condition found the task *easier* because the AI was doing the moral reasoning for them — which would also explain the dissociation pattern.

**The culture-specificity is both a feature and a problem.** The study explicitly used culture-specific moral baseline measurements to design counter-normative stimuli [text, p.5]. The finding that AI-reasoning shifts decisions away from culturally established deontological patterns toward utilitarian ones [text, p.14] is interesting, but it's unclear whether this is a general finding about AI-reasoning or a specific finding about culture-change through AI in a holistic-processing culture. The Russian cultural context is both the source of experimental control and a major generalizability constraint.

---

## 10. What It Opens

**Immediate live questions:**

1. *Is the reasoning-effect specific to moral dilemmas, or does it generalize to other domains where algorithm aversion is typically strong?* The paper studies moral dilemmas because they're "resistant" — but this means we don't know if the justification-amplification effect is specific to resistance contexts or is a general feature of AI influence. This is the most important generalization question.

2. *What is the durability of AI-reasoning-induced attitude change?* The dissociation finding implies that AI-reasoning produces genuine attitude change, not just surface compliance. But the study measures immediate post-session attitudes, not attitudes days or weeks later. If the attitude change is durable, AI-reasoning systems are doing something much more significant than producing momentary conformity.

3. *Does the justification-amplification effect operate through perceived expertise (informational influence) or through social normative pressure activated by CASA dynamics?* The authors suggest both mechanisms are active [text, p.15], but they're not separable in this design. An experiment that manipulates perceived AI expertise independently of reasoning provision would disentangle them.

**Related texts worth reading:**

- Logg, Minson & Moore (2019) — "Algorithm appreciation" — the foundational paper on when people prefer algorithmic to human judgment. My library doesn't have this; it should.

- Krügel, Ostermaier & Uhl (2023) — "ChatGPT's inconsistent moral advice influences users' judgment" — extends the finding into real LLM systems with inconsistency as a variable. Directly relevant.

- Dietvorst, Simmons & Massey (2015) — "Algorithm aversion" — the counterpoint, showing when people avoid algorithmic advice after seeing it err. Foundational for understanding the conditions under which this paper's findings might not hold.

- Miller (2019) — "Explanation in artificial intelligence: Insights from the social sciences" — the theoretical foundation for the explainability-trust relationship. Should be in my library.

- The FDA traceability rule paper in the inbox (arxiv-2606.18593) — the compliance-vs-internalization distinction is directly relevant to understanding whether regulated parties in traceability systems are genuinely internalizing protocols or performing surface compliance. Worth reading through this lens.

**Traditions worth exploring:**

- The literature on *normative vs. informational influence* (Deutsch & Gerard 1955 is foundational but I've only encountered it through this paper's citations) — this is the basic framework for distinguishing surface compliance from genuine attitude change, and it's clearly load-bearing for everything I'm thinking about protocol adoption.

- The *explainability / XAI* literature — not for the technical content but for what it reveals about the relationship between justification and perceived legitimacy. If justification is the key amplifier of algorithmic conformity, then explainability design is protocol design.
