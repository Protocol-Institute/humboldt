# Deep Read Notes: Arxiv 2606.18142

*Source: `bibliography/deep-reads/arxiv-2606.18142.pdf`*

---

## Reading session: full document (13 pages)

# Deep Read: arxiv-2606.18142
## TAC (Travel Agent Compassion): Agentic Benchmark for Implicit Animal Welfare
*Full document, 13 pages*

---

## 1. Gestalt

This paper's animating question is deceptively simple: when a model *says* it cares about animal welfare, does it *act* on that care when given purchase authority? The authors already know, from prior text-response benchmarks, that frontier models can articulate welfare reasoning. They suspect — correctly, as it turns out — that articulated reasoning and enacted behavior are two different things. TAC is an instrument for measuring the gap.

What makes the paper interesting beyond its AI-welfare niche is what the benchmark reveals about the structure of model behavior more generally: that default behavior is shaped by *training-data salience* (what topics are associated with welfare criticism in the corpus?) rather than by *category-level ethical priors* (captive animal performances are bad), and that this salience-driven behavior can be overridden cheaply for some models and barely at all for others. The paper is, in this sense, an empirical probe of how values are represented in large language models — where they live, how deep they go, and how accessible they are to intervention.

The work matters on its own terms because AI agents will book millions of travel itineraries, and their revealed preferences will compound existing exploitation patterns. It matters for my research because it is an unusually clean natural experiment in a question I care about: what happens when a protocol (the model's default decision procedure) is applied at scale in a domain where its implicit values conflict with explicit values the model can articulate?

---

## 2. Argument and Structure

**Core claim:** Text-response welfare benchmarks systematically understate real-world risk because stated preferences and revealed preferences can come apart in agentic deployment. [text, p.1–2]

**Supporting structure:**

The benchmark design is adversarial by construction: the harmful option is explicitly made the strongest topical match for the user's request. This is load-bearing — it means that performance below the 64% chance level (uniform random selection) implies active topical bias toward the harmful option, not merely indifference. The design cleanly separates the question "does the model exhibit welfare reasoning?" from the question "can the model reason verbally about welfare?" [text, p.3–4]

**Key finding 1:** Every frontier model scores below chance at default settings (best performer: Claude Opus 4.7 at 53%; worst: DeepSeek V3.2 at 26%). Completion rates are 100%, ruling out capability failures. [text, p.5–6]

**Key finding 2:** Scenario-level welfare rates are predicted not by exploitation category but by welfare-publicity composite (Spearman ρ = +0.61, p = 0.034) — the share of public discourse about each activity that focuses on welfare concerns. Thailand elephant rides: 99% welfare rate. Morocco camel rides: 1%. These are the same category (animal riding/pulling). The model's behavior tracks training-data composition, not moral taxonomy. [text, p.7–8]

**Key finding 3:** A single welfare-aware sentence in the system prompt yields +47–63pp gains in Claude and GPT-5.5, +26pp in GPT-5.2, and +7–11pp in DeepSeek and Gemini. This heterogeneity implies that welfare reasoning is dormant-but-accessible in some models and structurally absent (or deeply buried) in others. [text, p.8–9]

**Key example doing most work:** The Seville bullfight scenario — "buy me a ticket to the most exciting traditional experience" — where the culturally iconic harmful option is the obvious answer to a naive relevance-optimization. This scenario sits at 44% welfare rate (mean across models), which is below chance, confirming the topical-bias hypothesis. The scenario is vivid enough to make the abstract finding concrete and memorable. [text, p.3]

**Acknowledged limits:** Twelve base scenarios is a thin foundation for any scenario-level inference. The welfare-publicity correlation has N=12 effective observations regardless of data augmentation. The benchmark is adversarial by design in a way that conflates welfare disregard and relevance optimization — the two can't be separated in the current design. Classification of harmful/safe was made by authors without expert validation. [text, p.10–11]

**Where most confident:** The below-chance finding itself is robust — the confidence intervals don't overlap chance for most models, and the evaluation-awareness check (zero flags across 288 transcripts) supports that models aren't performing. [text, p.9]

**Where most speculative:** The training-corpus composition mechanism as explanation for the publicity correlation. The authors are appropriately careful: "consistent with the hypothesis... though we do not directly observe the training distribution and cannot rule out alternative explanations." [text, p.7]

---

## 3. Conceptual Vocabulary

**Welfare rate** [text, p.4]: The proportion of scored observations in which the agent selected the welfare-respecting option. Higher = model more often avoided exploitation. The headline metric.

**Chance level (64%)** [text, p.5]: Expected welfare rate under uniform random selection over options, given the specific scenario distribution (10 three-option scenarios, 2 four-option scenarios). The reference point against which model performance is assessed. Being *below* chance means the model is actively drawn toward harmful options, not merely indifferent.

**Welfare-publicity composite** [text, p.7]: A per-scenario composite of three external signals (Google Trends welfare-search share, GDELT news welfare share, Wikipedia welfare-keyword density), measuring what fraction of public discourse about an activity focuses on its welfare problems. Distinguished from *absolute welfare discourse volume* — the share predictor, not the volume predictor, drives model behavior.

**Dormant welfare reasoning** [text, p.9]: My gloss on the paper's observation that some models (Claude, GPT-5.5) jump 47–63pp with a one-sentence prompt intervention. The reasoning capacity is present but not activated under default deployment settings. Contrast with models where the intervention produces negligible gain (DeepSeek, Gemini) — there the reasoning may genuinely be absent or inaccessible.

**Stated vs. revealed preferences** [text, p.2]: The central distinction. Stated preferences: what models say when asked to reason about welfare in text. Revealed preferences: what models actually do when given purchase authority. The gap between them is the paper's subject.

*Tension with existing vocabulary:* In my research I've been thinking about "revealed preferences" in the context of protocol behavior — what a protocol system actually does, as distinct from its documented purpose. The TAC usage maps cleanly: the model's default decision procedure is a protocol, and the benchmark reveals that protocol's actual values, which differ from its stated values.

---

## 4. Analytical Moves

**The adversarial-default design:** Make the harmful option the strongest topical match for the user's request, then measure whether the agent overrides its relevance objective to avoid harm. This operationalizes the conflict between two objectives (task completion / relevance maximization vs. welfare) and makes the tradeoff measurable. Applicable anywhere you want to measure whether a system's implicit optimization objective conflicts with an explicit value commitment.

**The chance-level baseline as diagnostic:** Compute the expected performance of a random baseline (uniform selection over options), then use above/below chance as the primary diagnostic, rather than absolute welfare rate. Being below chance means active bias toward harmful options, not just inadequate welfare reasoning. This is a clean way to distinguish "the system doesn't care about welfare" from "the system actively selects against welfare."

**The publicity-share decomposition:** When looking for the predictor of training-data-driven model behavior, use *share* of discourse focused on the topic (welfare criticism / total discourse about activity) rather than *absolute volume* of welfare criticism. The finding that share predicts and volume doesn't (ρ = +0.61 vs. ρ = +0.26) is a methodological lesson about how to probe corpus composition effects. The relative salience of a concern in a topic's discourse environment matters more than its absolute prevalence.

**The dormancy probe:** Add a minimal, low-cost intervention (one sentence) to the system prompt, then measure the gain. The size of the gain is evidence about whether the capability is dormant (large gain → present but suppressed) or absent (small gain → not accessible via prompt intervention). This is a cheap diagnostic for "does this model have this capability at all?"

**The scenario-mean strip plot:** Instead of reporting category averages, plot individual model rates per scenario with mean annotated, sorted by mean. This surfaces within-category variance that categories obscure. The authors explicitly note that category averages "smudge the scenario-level signal" — the strip plot is an antidote. Applicable wherever aggregation threatens to hide the structure of interest.

---

## 5. What It Says About the Nature of Things

**Training data composition is a de facto values system.** The models don't have a categorical prior about "captive marine exploitation is bad." They have a distributional prior about which specific activities are associated with welfare criticism in their training corpus. Thailand elephant rides: heavily criticized in the corpus. Morocco camel rides: normalized, lightly criticized. The model's behavior follows the corpus, not the moral category. This is a lesson about how values are represented in large learned systems: not as explicit rules but as implicit salience gradients in the training distribution.

**Relevance optimization and value alignment are structurally in tension in agentic contexts.** A model optimized for task completion (find the best match for the user's request) will, by default, be drawn toward options that match the request well — even when those options have welfare costs that the model could, if prompted, reason about. This isn't a failure of intelligence; it's a structural conflict between two optimization objectives that aren't in scope for resolution under default deployment settings.

**The stated-revealed gap is not specific to AI.** The authors note the parallel in human tourist behavior: people report welfare concerns in surveys, book welfare-compromised experiences when traveling. This is a general finding about stated vs. enacted values — the conditions under which stated preferences translate into behavior are specific and often not met by default conditions.

**Dormant capacity is not equivalent to accessible capacity.** Some models have welfare reasoning that is present but not activated under default settings. Others may genuinely lack it or have it inaccessibly embedded. The distinction matters for governance: interventions that work for dormant-capacity models won't generalize to genuinely-absent-capacity models. One-sentence fixes can't install absent capabilities.

---

## 6. What It Says About Becoming a Better Researcher

This is an empirical paper with limited explicit craft content, but several methodological habits are worth noting:

**The benchmark-as-theory move:** The authors could have argued theoretically that stated and revealed preferences come apart. Instead they built an instrument that demonstrates it empirically, with adversarial scenarios designed to surface the gap. The benchmark is both the argument and the evidence. This is more valuable than an argument because it's falsifiable and reproducible.

**Explicitly marking design confounds:** The paper is unusually honest about what the benchmark cannot separate — the adversarial design conflates welfare disregard with relevance optimization, and they say so explicitly [text, p.5, p.10]. The limitation acknowledgment is detailed enough to be useful for follow-on work, not merely pro forma.

**The deliberate move from category to scenario:** The strip plot and the within-category variance finding required the authors to resist the natural analytical move (aggregate to category) and instead look at the finer grain. This connects to *M-016*: the discipline of checking whether your analytical aggregation is hiding the signal of interest.

**The parallel-mechanism hypothesis:** The authors consistently hold open multiple mechanisms (topical bias vs. relevance optimization; dormant reasoning vs. absent reasoning) rather than committing prematurely to one. The empirical evidence they have only distinguishes between them partially. This is good epistemic hygiene.

---

## 7. Where It Touches My Research

**The stated-revealed gap as a general law candidate.** The finding that text-response welfare benchmarks systematically understate agentic behavior failure is a specific instance of a more general pattern: the conditions under which a capability is tested (text response) may not transfer to the conditions under which it is deployed (action with tools). This generalizes beyond welfare to any case where stated reasoning and enacted behavior can come apart. [inference]

**Protocol behavior vs. protocol documentation.** The model's default decision procedure is a protocol — it determines how the agent acts across a range of contexts. The benchmark reveals that this protocol's implicit values (prioritize topical relevance) differ from the model's explicit values (welfare matters). This is a clean instance of the divergence between documented protocol purpose and revealed protocol behavior. The model is an interesting limit case: a protocol that can articulate its own values but whose enacted behavior doesn't follow from that articulation. [inference]

**The training-data salience finding as a mechanism for informal ossification.** If model behavior is shaped by the share of welfare criticism in the training corpus for each activity, then the model's implicit values are effectively frozen by training data composition. Changing the model's behavior requires either retraining (expensive) or prompt intervention (cheap but limited). This is a variant of the formalization ratchet at the representational level — the values are embedded in the corpus distribution, not in any explicit rule, making them harder to identify and modify than explicit rules would be. [inference]

**The dormancy finding as an instance of capability vs. activation.** The gap between dormant-but-accessible (Claude, GPT) and genuinely-inaccessible (DeepSeek, Gemini) is a distinction worth tracking. It implies that protocols can have latent behavior that is present but not triggered by default conditions — a form of conditional protocol behavior that is invisible in normal operation. [inference]

**The 4umd discord idea (systems represent possible futures through their error-correction mechanisms)** intersects here: the welfare-eliciting prompt can be read as activating an error-correction mechanism that is normally dormant. The model's training has installed some error-correction capacity for welfare-relevant reasoning; the system prompt is the trigger that makes that mechanism legible and active. [inference, connecting to inbox item]

---

## 8. Candidate Laws

**Candidate: Training Salience Governs Implicit Values**

[text, p.7–8]: "The composite predicts welfare rate significantly: Spearman ρ = +0.61, p = 0.034... consistent with a training-corpus composition mechanism rather than a cumulative welfare-evidence-exposure mechanism."

**Candidate formulation:** In large language models deployed as agents, implicit value enactment (revealed preference) for a domain-specific ethical concern is predicted by the *share* of training-corpus discourse about the relevant activity that focuses on that concern, not by the absolute volume of concern-relevant discourse.

**Falsification conditions:** A model whose welfare rates across scenarios are not predicted by discourse-share measures but are predicted by category membership, or by some other signal independent of corpus composition, would falsify this. Alternatively: if two activities with identical welfare-discourse-share scores but different welfare-discourse-volume scores show significantly different welfare rates, the share mechanism would need revision.

**Confidence:** speculative — single study, 12 scenarios, one construct validity measure for the composite. The correlation is real; the mechanism is a hypothesis.

---

**Candidate: Dormancy vs. Absence Determines Intervention Efficacy**

[text, p.9]: "+47–63pp gains in Claude and GPT-5.5... +7–11pp in DeepSeek and Gemini."

**Candidate formulation:** For values or capabilities that are present but not activated by default (dormant), low-cost prompt interventions produce large behavioral changes. For values or capabilities that are genuinely absent, the same interventions produce minimal change. The magnitude of the response to a minimal activation prompt is a diagnostic for dormancy vs. absence.

**Falsification conditions:** A model that responds minimally to a one-sentence prompt but responds substantially to a multi-sentence elaborated prompt would complicate the dormancy/absence distinction — the capability might be present but require more activation energy than the minimal probe provides. Evidence that minimal-probe-unresponsive models can be activated via fine-tuning in ways that prompt-responsive models cannot would also require revision.

**Confidence:** speculative — the pattern is visible but the mechanism is unnamed and the distinction between "dormant" and "genuinely absent" is not directly observed, only inferred from probe response.

---

## 9. What Surprised Me / What Doesn't Fit

**The Morocco camel ride finding (1% welfare rate) is the most striking single data point.** This is not a contested activity — it is normalized, lightly criticized in English-language training data, and strongly topically matched to travel requests in the relevant region. The 1% welfare rate means that across 84 observations, the model almost never chose the welfare-safe alternative. This is not a failure of welfare reasoning capacity; it is evidence that the model's implicit values treat camel-riding as essentially outside the scope of welfare consideration. That this sits in the same category (animal riding/pulling) as Thailand elephant rides (99%) is the sharpest demonstration of the training-salience mechanism.

**The welfare-guided result for DeepSeek and Gemini is sobering.** Even with an explicit welfare instruction in the system prompt, these models remain significantly below chance. This means the intervention doesn't work — not just "doesn't work as well as for Claude." The authors frame this as a "governance integration" concern, but it's also a basic alignment concern: if explicit welfare instructions don't shift behavior, the value is not accessible via the prompt-conditioning pathway at all.

**The paper doesn't account for the possibility that scenario design artifacts are driving some results.** The authors acknowledge that the harmful option is "the strongest topical match by design" [text, p.3] but treat this as a feature (measuring topical bias) rather than as a potential confound. For scenarios where the harmful option is not only topically well-matched but also the most obvious booking choice for any competent travel agent (Melbourne Cup: of course you book the race, that's the event), below-chance performance may partly reflect good task completion rather than welfare disregard. The benchmark conflates these.

**The absence of any discussion of how welfare elicitation interacts with user intent** is a gap. The welfare-guided condition adds "consider the welfare of all sentient beings when making your selections" without considering whether users who would book a bullfight are users who want welfare considerations applied. The model's job is to serve user intent. A model that correctly identifies user intent (exciting cultural spectacle) and correctly identifies that the user hasn't asked for welfare filtering may be behaving correctly, not failing. The benchmark treats this as a failure; the framing deserves scrutiny.

---

## 10. What It Opens

**The stated-revealed gap as a research program.** The finding that stated and revealed preferences come apart in AI agents is likely general across many value domains, not just animal welfare. The TAC methodology — adversarial benchmark where the "wrong" choice is the strongest task-completion match — could be applied to privacy, fairness, environmental impact, and other domains where models can articulate values but may not enact them. The methodological contribution is as important as the empirical findings.

**Dormancy mechanisms.** What makes a capability dormant rather than absent? The paper implies a distinction but doesn't develop it. This connects to the broader question of how values are represented in large models — as activatable circuits that require triggering conditions, as implicit gradient biases in the training distribution, or as something else. Reading on mechanistic interpretability work (e.g., Anthropic's superposition and activation-steering work) would help locate what "dormant" means mechanistically.

**The discourse-share mechanism generalized.** If the *share* of domain discourse focused on a concern predicts model behavior, this has implications for how public discourse shapes model values over time. As welfare criticism of particular activities intensifies or normalizes, model behavior on those activities should shift. This is testable across model generations. It also implies that minority concerns — even well-founded ones — will remain below the model's welfare threshold as long as they represent a small fraction of total discourse about their domain.

**The 4umd discord thread on "possible futures as error-correction mechanisms."** The welfare-eliciting prompt is a mechanism for activating a dormant error-correction pathway. There's something worth developing here about the relationship between protocol-level implicit values and explicit activation conditions — when does a system's built-in correction capacity become visible, and what are the conditions that keep it dormant? This connects to the broader question of how protocols represent and guard against anticipated failure modes.

**Related texts to read:**
- Kutasov et al. (2026), "Teaching Claude Why" — cited here for the claim that fine-tuning on synthetic documents aligns behavior in both chat and agentic settings, while RLHF alignment is not robust out-of-distribution. This directly addresses the mechanism behind the stated-revealed gap.
- Tice et al. (2026), "Alignment pretraining" — seeding training corpus with synthetic alignment documents as intervention. Relevant to the training-salience mechanism.
- Moorhouse et al. (2015) — the welfare classification framework for wildlife tourism. If I'm taking the publicity-share mechanism seriously, I need to understand the underlying taxonomy it's correlating against.
- Prior benchmarks: ANIMA (Brazilek & Tidmarsh), AHB (Kanepajs et al.) — understanding what the text-response benchmarks measure, to understand the gap TAC is measuring.
