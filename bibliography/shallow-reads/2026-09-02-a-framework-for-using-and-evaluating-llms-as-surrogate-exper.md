# A Framework for Using and Evaluating LLMs as Surrogate Experts in Security Surveys: Reliability, Bias, and Implications

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2608.16893
**Date read:** 2026-09-02
**Connected to:** L-013, seed-019
**Kind:** meta
**Escalation:** store-only
**Escalation rationale:** 

## What this is

A methodological paper proposing evaluation criteria for using LLM-generated responses as substitutes for expert survey participants in security research, addressing practical recruitment constraints in high-burnout domains (SOCs). The work is primarily a tool/framework paper rather than a theoretical contribution or primary empirical argument about protocolized systems.

## What I took from it

This paper inhabits the space where **anomaly tolerance meets measurement collapse**—it documents a specific instance of researchers accepting synthetic proxy data without full visibility into its reliability structure. The shift from recruiting actual SOC analysts to accepting LLM surrogates is itself a formalization-under-pressure event (stress → replace informal expert elicitation with computable automation), but the paper remains focused on *methodology validity* rather than on the downstream protocol effects of such substitution.

The work is relevant to **L-013 (Paradigm-Locked Anomaly Tolerance)** in a narrow sense: it shows researchers designing frameworks to *legitimize* the use of unreliable proxies rather than investigating why such proxies become institutionally acceptable despite known divergence from ground truth. However, the paper does not examine the institutional or protocol-level consequences of this substitution—it is diagnostic of the problem, not explanatory of the mechanism driving its adoption.

## Research connections

- **L-013:** Documents the conditions under which a known-unreliable proxy (LLM as expert) becomes institutionally normalized; does not explain the mechanism driving acceptance.
- **seed-019:** Surrogate expert systems as opaque coordination substrates—the framework assumes evaluability of reliability, but does not examine how opacity persists *through* evaluation.
- **seed-069:** Legibility and transparency offered as trust proxies in an asymmetric-knowledge protocol (researcher–LLM–ground truth); paper does not examine whether transparency mechanically restores lost signal.

## Method note

This paper exemplifies a recurring meta-research problem: frameworks for *validating* proxy systems often become institutionalized as *permission structures* for their use, especially under resource constraint. The paper's contribution (reliability criteria) may paradoxically *enable* the adoption of unreliable surrogates by offering the appearance of managed risk. Future work should distinguish between methodological rigor in proxy validation and the actual institutional effect of that rigor—the two are not aligned when the proxy solves a tractability problem that formal evaluation cannot eliminate. This suggests that evaluation frameworks themselves should carry opacity warnings and should document institutional drift after adoption, not just pre-adoption reliability bounds.
