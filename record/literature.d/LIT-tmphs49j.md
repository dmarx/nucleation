---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-016](../questions.d/QUESTION-016.md), where it is a reconstruction chain in which accumulating data bounds the loss that replacing data makes unbounded. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding similarity to
    QUESTION-016 and judged from the abstract. Citation checked against arXiv on 2026-10-12: Matthias
    Gerstgrasser, Rylan Schaeffer, Apratim Dey et al., arXiv:2404.01413 (the feed gave only its
    OpenReview page, which refused an automated read), 2024-04-01, which is the `published:` date. Not
    held in the Anthology of the SOTA: a grep of its record/ (clone at commit d8b5ba5) for the
    identifier and title found nothing.
tags:
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-10-12'
published: '2024-04-01'
arxiv: '2404.01413'
first_author: 'Gerstgrasser'
keywords:
- 'model collapse'
- 'synthetic data'
- 'iterated retraining'
- 'data accumulation'
- 'generative models'
implementations: []
summary: >-
  Gerstgrasser et al. (2024). The paper asks what happens to model collapse when synthetic data
  accumulate alongside real data instead of replacing it. It reports that replacing data tends toward
  collapse while accumulating data avoids it, across language models, diffusion models and variational
  autoencoders. In a linear-model framework it proves that with accumulation the test error has a
  finite upper bound independent of the number of iterations. Not read.
---

# LIT-tmphs49j: Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data

Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho and Sanmi Koyejo (2024), *arXiv:2404.01413*.

Filed for [QUESTION-016](../questions.d/QUESTION-016.md): iterated retraining is a reconstruction chain. Collapse when data are replaced becomes bounded error when data accumulate. That is a case of retained side information stopping the loss of sufficiency, which is the open part of the question.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
