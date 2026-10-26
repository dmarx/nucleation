---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'MIB: A Mechanistic Interpretability Benchmark'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T24 the reply cites "the 2025 Mechanistic
    Interpretability Benchmark" with no author or identifier: "in its tested
    causal-variable localization tasks, sparse-autoencoder features did not
    outperform raw neuron representations, while supervised distributed
    alignment search performed best". The abstract says that. Checked on
    2026-10-26 against the arXiv record: Aaron Mueller, Atticus Geiger,
    Sarah Wiegreffe, Dana Arad and 19 further authors, arXiv 2504.13151, v1
    submitted 17 April 2025, which is `published:`; the comment on v2 (9
    June 2025) says it was accepted to ICML 2025. The summary follows the
    arXiv abstract.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2025-04-17'
arxiv: '2504.13151'
first_author: 'Mueller'
keywords:
- 'mechanistic interpretability'
- 'benchmark'
- 'circuit localization'
- 'causal variable localization'
- 'sparse autoencoders'
- 'distributed alignment search'
implementations: []
summary: >-
  Mueller et al. (2025), arXiv:2504.13151, ICML 2025. A benchmark with two
  tracks over four tasks and five models. In circuit localization,
  attribution and mask-optimization methods perform best; in causal variable
  localization, supervised distributed alignment search (DAS) performs best,
  and sparse-autoencoder features are not better than neurons, that is,
  non-featurized hidden vectors (abstract).
---
<!-- inactive-ok-file: CLAIM-tmpwr001 — Proposed; the claim this work bears on, cited as open -->
<!-- inactive-ok-file: THEORY-802 — Proposed; a neighbouring holding on interchange interventions, named, nothing here rests on it -->

# LIT-tmprlq7z: MIB: A Mechanistic Interpretability Benchmark

Mueller, A., Geiger, A., Wiegreffe, S., Arad, D., et al. (2025). MIB: A
mechanistic interpretability benchmark. *ICML 2025*. arXiv:2504.13151.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T24 as a warning that a sophisticated feature detector is not
automatically a better causal explanation. That is [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md)'s point in
the transformer setting: a feature recovered from activity is not yet the
variable that does the work. It bears on [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md). The record's
neighbouring holdings are Makelov et al. ([LIT-968](LIT-968.md)) and Wu et al.'s reply
([LIT-961](LIT-961.md)) on interchange interventions, [LIT-987](LIT-987.md), [THEORY-243](../theory.d/THEORY-243.md) and [THEORY-802](../theory.d/THEORY-802.md)
on basis-relative alignments, and [THEORY-504](../theory.d/THEORY-504.md) on SAE fidelity.
