# When Does the Public Become Suspicious of Bots? Demand-Side Evidence from Botometer Query Logs

**Source:** cs.CY updates on arXiv.org — https://arxiv.org/abs/2609.20661
**Date read:** 2026-09-22
**Connected to:** L-013, seed-131
**Kind:** content
**Escalation:** store-only

## What this is

An empirical study of bot-detection query logs (1M+ Botometer checks, 2020–2023) treating each query as a behavioral trace of public suspicion. The work maps when and whom users suspect of automation, finding that collective suspicion spikes sharply around platform crises—particularly the 2022 Musk-Twitter bot dispute—rather than responding smoothly to actual bot prevalence.

## What I took from it

The paper documents a clear case of **paradigm-locked anomaly tolerance** (L-013): users and platforms maintain stable verification practices and credibility frames until external shock forces rapid recalibration. The bot-detection system (Botometer) itself remained functionally unchanged during the period; what changed was demand for verification, not the protocol's technical integrity. This suggests that suspicion and verification are not calibrated to actual system state, but to narrative landmarks and crisis events.

More subtly, the work reveals **intent legibility as coordination target displacement** (seed-138 adjacent): users query Botometer not primarily to obtain ground truth about individual accounts, but to externalize and legitimize suspicion within a social frame. The spike around the Musk crisis is a coordination event—a moment when suspicion became collectively legible and sharable. The protocol (Botometer) serves as a *normalization interface* for otherwise private doubt, not as an information source.

## Research connections

- **L-013:** Direct confirmation—bot-detection and verification demand remain stable across long periods of accumulating evidence (rising actual bot populations, protocol degradation), then spike sharply at narrative/crisis boundaries rather than at technical thresholds.
- **seed-131:** Context legibility (the Musk-Twitter dispute, platform crisis framing) becomes the failure attribution boundary—users begin querying Botometer not because bot behavior changed, but because the interpretive context shifted, making suspicion legible and shareable.
- **seed-128:** Legibility-driven agent convergence—the 2022 spike shows mass coordination on verification behavior once suspicion became publicly discussed and socially legible.

## Seed

**Seed title:** Verification Demand Decoupling from System State

**Seed type:** observation

**Seed text:** In protocol systems that provide verification or detection services, demand for verification correlates weakly with actual system degradation or prevalence of the phenomenon being detected, but correlates strongly with narrative legibility and crisis events that make suspicion collectively expressible. Users employ verification protocols not primarily to obtain state information, but to externalize private doubt into a socially sharable form. This suggests verification systems function as *legitimacy interfaces* rather than information channels, and their effectiveness is governed by whether they align with the current interpretive paradigm rather than by their technical accuracy relative to ground truth.
