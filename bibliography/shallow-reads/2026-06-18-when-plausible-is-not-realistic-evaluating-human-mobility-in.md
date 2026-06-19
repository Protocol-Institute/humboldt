# When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.13835
**Date read:** 2026-06-18
**Connected to:** none
**Escalation:** escalate-to-deep
**Escalation rationale:** This is a primary source introducing a systematic validation framework (mobility laws, temporal rhythms, network motifs, semantic transitions, behavioral profiles) that operationalizes the plausibility-realism gap in artificial agent systems—a foundational distinction for the new nature research agenda with generalizable diagnostic value across LLM-based simulators.

## What this is

An empirical validation study that introduces a multi-dimensional framework for testing whether LLM-based generative agents in urban simulators actually reproduce realistic human mobility patterns or merely generate narratives that *sound* plausible. The work applies formal mobility metrics against real-world data from Paris and Shanghai to detect where agent behavior diverges from empirical regularities.

## What I took from it

This work directly addresses a critical blindspot in protocolized systems: the distinction between local narrative coherence and global statistical realism. An LLM agent's individual movement decisions may be semantically justified and contextually plausible, but aggregate mobility may violate empirical laws (power-law distance decay, recurrence patterns, temporal rhythms). This suggests that plausibility at the token/action level does not propagate to system-level fidelity—a fracture point that likely generalizes beyond mobility to any domain where local coherence masks distributional error.

The validation framework itself (mobility laws, temporal rhythms, network motifs, semantic transitions, behavioral profiles) is a methodological contribution. It treats realism as multidimensional and measurable, offering a template for detecting similar gaps in other artificial systems. The finding that agents can be convincing locally while failing globally suggests a design principle: protocolized systems may require explicit constraint-injection or learned statistical regularities, not just language coherence.

## Research connections

- **Plausibility-Realism Gap (candidate):** Language-coherent behavior does not guarantee distributional realism; local semantic validity can mask aggregate statistical violation.
- **Agent Design in Urban Sim:** LLM-based agents may require explicit grounding in empirical mobility laws, not emergent from language alone.

## Candidate laws or signals

- **CL-Mobility-001:** LLM-based generative agents show plausible narrative mobility but systematically underfit to empirical mobility laws (power-law distance, return probability, temporal periodicity); plausibility and realism decouple at the aggregate level.
- **CL-Validation-001:** Artificial behavioral systems require multi-level validation (action coherence + distributional realism + temporal rhythm + network structure); single-level assessment misses critical failure modes.
