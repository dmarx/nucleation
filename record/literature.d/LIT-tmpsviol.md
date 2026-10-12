---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-030](../questions.d/QUESTION-030.md), where features with a distinctive causal role predict out-of-distribution behaviour better than merely correlated features. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding similarity to QUESTION-030
    and judged from the abstract. Citation checked against arXiv on 2026-10-12: Jing Huang, Junyi Tao, Thomas Icard et
    al., arXiv:2505.11770 (ICML 2025, per the arXiv comment), submitted 2025-05-17, which is the `published:` date.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d8b5ba5) for the identifier and
    title found nothing.
tags:
- causality
- representation-learning
- anthology-candidate
date: '2026-10-12'
published: '2025-05-17'
arxiv: '2505.11770'
first_author: 'Huang'
keywords:
- 'causal abstraction'
- 'interpretability'
- 'out-of-distribution prediction'
- 'counterfactual simulation'
- 'value probing'
implementations: []
summary: >-
  Huang et al. (2025). The paper asks whether internal mechanisms found by interpretability methods can predict how a
  language model behaves out of distribution. Across symbol manipulation, knowledge retrieval and instruction
  following, it reports that the features most robust for predicting correctness are those with a distinctive causal
  role. Its two methods, counterfactual simulation and value probing, outperform causal-agnostic features out of
  distribution. Not read.
---

# LIT-tmpsviol: Internal Causal Mechanisms Robustly Predict Language Model Out-of-Distribution Behaviors

Jing Huang, Junyi Tao, Thomas Icard, Diyi Yang and Christopher Potts (2025), *arXiv:2505.11770* (ICML 2025).

Filed for [QUESTION-030](../questions.d/QUESTION-030.md): a measured case where features that play a distinctive causal role predict behaviour out of distribution better than features that only correlate with it. Intervention here separates constitutive structure from diagnostic structure. It also bears on [QUESTION-028](../questions.d/QUESTION-028.md).

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
