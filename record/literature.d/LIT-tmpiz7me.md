---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-025](../questions.d/QUESTION-025.md), where it tests empirically when linear relation directions form. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'On Linear Representations and Pretraining Data Frequency in Language Models'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding similarity
    to QUESTION-025 and judged from the abstract. Citation checked against arXiv on 2026-10-12: Jack
    Merullo, Noah A. Smith, Sarah Wiegreffe and Yanai Elazar, arXiv:2504.12459, ICLR 2025
    (OpenReview EDoD3DgivF), 2025-04-16, which is the `published:` date. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone at commit d8b5ba5) for the identifier and title found
    nothing.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-12'
published: '2025-04-16'
arxiv: '2504.12459'
first_author: 'Merullo'
keywords:
- 'linear representations'
- 'pretraining data frequency'
- 'co-occurrence'
- 'factual relations'
- 'language models'
implementations: []
summary: >-
  Merullo et al. (2025). The paper reports that linear representations of factual relations in
  language models track pretraining term frequencies. For subject–relation–object triples,
  subject–object co-occurrence frequency is highly correlated with linear representation quality. In
  OLMo-7B and GPT-J, a linear representation consistently forms once subjects and objects co-occur
  about 1k and 2k times. A regression on representation quality can then estimate how often a term
  was seen in pretraining. Not read.
---

# LIT-tmpiz7me: On Linear Representations and Pretraining Data Frequency in Language Models

Jack Merullo, Noah A. Smith, Sarah Wiegreffe and Yanai Elazar (2025), *ICLR 2025*.

Filed for [QUESTION-025](../questions.d/QUESTION-025.md): it measures when linear relation directions form, as a function of how often
subject and object co-occur. That is an empirical test of the question's premise that co-occurrence
statistics give linear attribute directions.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
