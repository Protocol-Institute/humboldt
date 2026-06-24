# A Technical Taxonomy of LLM Agent Communication Protocols

**Source:** cs.MA updates on arXiv.org — https://arxiv.org/abs/2606.19135
**Date read:** 2026-06-24
**Connected to:** none
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A systematic taxonomy paper classifying LLM agent communication protocols to address interoperability fragmentation in multi-agent systems. The work applies established taxonomic methodology (iterative refinement of purpose, meta-characteristics, and ending conditions) to formalize the protocol design space without presenting novel theoretical claims or empirical mechanisms.

## What I took from it

This is infrastructure documentation rather than primary research. The paper acknowledges a real coordination problem—protocol fragmentation limiting multi-agent scaling—but treats taxonomy construction as the solution domain rather than investigating *why* such fragmentation emerges or *what principles* govern effective protocol design under computational constraints.

The work is potentially useful as a reference artifact (which protocols exist, how they cluster) but does not advance understanding of communication costs, emergence of standardization, or whether communication protocol choice is downstream of agent architecture or upstream constraint. It does not investigate whether fragmentation itself signals something about the problem space (e.g., task-specificity of coordination, or limits to universal protocols).

## Research connections

- None yet identified. No established laws or active hypotheses in current context to anchor against.

## Candidate laws or signals

none

**Disposition:** File as reference material. Revisit only if future work uses this taxonomy to support mechanistic or generalizable claims about protocol selection or multi-agent coordination costs.
