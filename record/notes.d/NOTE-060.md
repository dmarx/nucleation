---
number: 60
status: Skimmed
formerly:
- NOTE-tmpj7uks
paper: LIT-084
title: '3rd EEAS report on FIMI threats (2025)'
version: 1
date: '2026-09-25'
summary: >-
  The EEAS proposes a "FIMI Exposure Matrix" that sorts channels into four tiers by how closely they are tied to a state actor. Applied to 505 incidents from 2024 involving about 38,000 channels, it finds that overt Russian and Chinese state media are the tip of a much larger covert and non-attributed infrastructure; non-attributed channels are 76.5% of those investigated.
---

<!-- inactive-ok-file: LIT-084 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-060: 3rd EEAS report on FIMI threats (2025)

## Contribution

This is the EU diplomatic service's third annual threat report on foreign information manipulation and interference (FIMI). It introduces the Exposure Matrix as a systematic way to classify channels and attribute them to threat actors. It then applies the Matrix to the incidents the EEAS detected between November 2023 and November 2024. The report summarises the year's trends by target country, platform and technique, and then maps the network structure of Russian and Chinese FIMI infrastructure. Case studies cover Moldova, Sub-Saharan Africa and Chinese influence-for-hire operations. The report's stated aim is to support attribution and give a basis for costs such as exposure and sanctions.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Scope and caveat (pp. 6, 9): 505 incidents, 38,000 unique channels on 25 platforms, and more than 68,000 observables. All are encoded in STIX. The report itself says the sample is illustrative and "should not be used to draw conclusions about general trends".
- Trends (pp. 5, 9–11): 90 countries were targeted, and Ukraine accounts for almost half of the incidents. 42 Russian attempts were recorded around the June 2024 European elections. X accounts for 88% of detected activity. At least 349 incidents localised their content, and 28 used online ads. Doppelgänger and False Façade are named.
- The Exposure Matrix (pp. 14–18) has four categories: official state channels, state-controlled outlets, state-linked channels (covert), and state-aligned (non-attributed). The evidence behind each is sorted into technical indicators (shared infrastructure, IPs, domains, ad networks) and behavioural indicators (coordinated messaging, synchronised timing, AI-generated content, repeated playbooks), with open, proprietary or classified sourcing.
- Network analysis (pp. 20–23): 2,055 core channels and 8,056 connections, after filtering out about 28,000 disposable CIB assets. The report describes Russian and Chinese clusters and "booster nodes", and finds occasional cross-amplification between Russian and Chinese channels.
- Conclusions (p. 37): the report expects covert and non-attributed channels, 76.5% of the sample, to stay central. It says FIMI analysis needs to be integrated with cyber threat intelligence, and it frames FIMI as a strategic, embedded foreign-policy instrument.

## Open questions

- It is an institutional source and states its own sampling limits. It is useful as the EEAS's stated methodology and taxonomy, not as a measurement of prevalence.
- The network section's construction (co-involvement edges, filtering thresholds) should be checked before any figure is cited.
- It links to c01 (STIX/DISARM encoding) and c11 (the Russian framing of "information war"), and to the earlier EEAS reports it cites (1st report Feb 2023, 2nd report 2024).
- The report mentions generative AI as a threat-actor tool, but I did not read what it says about it.
