---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'Mixed Membership Stochastic Blockmodels'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T21 the reply says "mixed-membership stochastic
    blockmodels similarly permit people to participate in different latent
    interaction roles rather than belong exclusively to one community",
    linking "jmlr.org" with no author or title. Checked on 2026-10-26
    against the JMLR abstract page and the arXiv record: Edoardo M. Airoldi,
    David M. Blei, Stephen E. Fienberg and Eric P. Xing, JMLR 9(65):
    1981–2014 (2008); arXiv 0705.4485, v1 submitted 30 May 2007, which is
    `published:` (ADR-002). JMLR gives no DOI. The summary follows the JMLR
    abstract.
tags:
- network-science
- probabilistic-modeling
date: '2026-10-26'
published: '2007-05-30'
arxiv: '0705.4485'
url: 'https://jmlr.org/papers/v9/airoldi08a.html'
first_author: 'Airoldi'
keywords:
- 'mixed membership'
- 'stochastic blockmodel'
- 'relational data'
- 'variational inference'
- 'social networks'
implementations: []
summary: >-
  Airoldi, Blei, Fienberg & Xing (2008), JMLR 9: 1981–2014. For pairwise
  measurements such as links between objects, where the usual
  exchangeability assumptions fail, mixed membership stochastic blockmodels
  combine global parameters for dense patches of connectivity (the
  blockmodel) with node-specific mixed memberships. A variational algorithm
  gives fast approximate inference, applied to social and
  protein-interaction networks (abstract).
---

# LIT-tmpt5wer: Mixed Membership Stochastic Blockmodels

Airoldi, E. M., Blei, D. M., Fienberg, S. E. & Xing, E. P. (2008). Mixed
membership stochastic blockmodels. *Journal of Machine Learning Research* 9:
1981–2014. arXiv:0705.4485.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T21 for the relational component of the reply's combined model:
members occupying several latent roles in their interactions. The record
held no blockmodel. It bears on [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md), whose last clause asks whether
inferred higher-level structure predicts responses to interventions beyond
what the communication and authority graph already gives; a mixed-membership
blockmodel of that graph is the baseline such inference must beat.
