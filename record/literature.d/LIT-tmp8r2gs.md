---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-027](../questions.d/QUESTION-027.md), where it proves which linear properties hold in every next-token predictor that induces the same distribution. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'All or None: Identifiable Linear Properties of Next-token Predictors in Language Modeling'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding
    similarity to QUESTION-027 and judged from the abstract. Citation checked against arXiv on
    2026-10-12: Emanuele Marconato, Sébastien Lachapelle, Sebastian Weichwald et al.,
    arXiv:2410.23501 (AISTATS 2025), 2024-10-30, which is the `published:` date. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone at commit d8b5ba5) for the identifier
    and title found nothing.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-12'
published: '2024-10-30'
arxiv: '2410.23501'
first_author: 'Marconato'
keywords:
- 'identifiability'
- 'next-token prediction'
- 'linear representations'
- 'relational linearity'
- 'distribution equivalence'
implementations: []
summary: >-
  Marconato et al. (2024). The paper asks whether a linear property found in one language model,
  such as parallel difference vectors for "easy/easiest" and "lucky/luckiest", must hold in every
  model that induces the same distribution. It proves an identifiability result for
  distribution-equivalent next-token predictors that drops an earlier diversity requirement. Using
  a refinement of relational linearity, it shows that under suitable conditions such linear
  properties hold in all such predictors or in none. Not read.
---

# LIT-tmp8r2gs: All or None: Identifiable Linear Properties of Next-token Predictors in Language Modeling

Emanuele Marconato, Sébastien Lachapelle, Sebastian Weichwald, Luigi Gresele (2024), *AISTATS 2025; arXiv:2410.23501*.

Filed for [QUESTION-027](../questions.d/QUESTION-027.md): it shows which linear properties are fixed by the observable distribution
alone, even though the full latent model is not identified. That is the question's pattern: a
signature identified from what can be observed when the latent model cannot be.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
