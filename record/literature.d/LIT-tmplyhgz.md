---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'Correlated Non-Parametric Latent Feature Models'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T22 the reply lists "Correlated nonparametric latent
    feature models" as a heading, with a link to "proceedings.mlr.press" and
    no authors, for latent features that "reinforce, inhibit, or depend on
    one another". Identified by title as Finale Doshi-Velez and Zoubin
    Ghahramani, Proceedings of the 25th Conference on Uncertainty in
    Artificial Intelligence (UAI 2009), reissued as PMLR R7: 143–150;
    checked on 2026-10-26 against the PMLR page (dated 18 June 2009) and the
    arXiv record (1205.2650, v1 submitted 9 May 2012, the UAI paper posted
    later). Under ADR-002's earlier-date rule `published:` is 2009-06-18.
    The summary follows the abstract.
tags:
- probabilistic-modeling
date: '2026-10-26'
published: '2009-06-18'
arxiv: '1205.2650'
url: 'https://proceedings.mlr.press/r7/doshi-velez09a.html'
first_author: 'Doshi-Velez'
keywords:
- 'Indian buffet process'
- 'correlated features'
- 'nonparametric latent feature model'
- 'hidden factors'
implementations: []
summary: >-
  Doshi-Velez & Ghahramani (2009), UAI 2009, PMLR R7: 143–150. The Indian
  buffet process does not bound the number of active features but assumes
  them uncorrelated, which fits many real problems badly. The paper gives a
  framework for correlated nonparametric feature models generalising the
  IBP, derives several specific models from it, and applies them to real
  datasets (abstract).
---
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction this work bears on, filed from the same exchange, cited as open -->

# LIT-tmplyhgz: Correlated Non-Parametric Latent Feature Models

Doshi-Velez, F. & Ghahramani, Z. (2009). Correlated non-parametric latent
feature models. In *Proceedings of the 25th Conference on Uncertainty in
Artificial Intelligence* (UAI 2009). PMLR R7: 143–150. arXiv:1205.2650.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T22. The independence of IBP features is one source of the
identifiability gaps that [CASE-tmplcm41](../cases.d/CASE-tmplcm41.md) records for T23's model, where features
that co-occur are identified only as a sum; this is the established
generalisation that models their correlation. It bears on [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).
