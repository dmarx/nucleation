---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'Dependent Indian Buffet Processes'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T22 the reply says "Williamson, Orbanz, and
    Ghahramani introduce dependence on time or other covariates", and at T23
    that its own model "is not automatically the exact dependent IBP of
    Williamson, Orbanz, and Ghahramani, whose construction uses
    covariate-dependent Gaussian processes", both linking
    "proceedings.mlr.press" with no title. Checked on 2026-10-26 against the
    PMLR page: Sinead Williamson, Peter Orbanz and Zoubin Ghahramani,
    Proceedings of the Thirteenth International Conference on Artificial
    Intelligence and Statistics, PMLR 9: 924–931, dated 31 March 2010, which
    is `published:`. It is not the IBP compound Dirichlet process of
    Williamson, Wang, Heller and Blei (ICML 2010), a different work, which
    no reply cited. No DOI or arXiv copy. The summary follows the PMLR
    abstract.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
published: '2010-03-31'
url: 'https://proceedings.mlr.press/v9/williamson10a.html'
first_author: 'Williamson'
keywords:
- 'dependent Indian buffet process'
- 'covariate dependence'
- 'binary latent features'
- 'Gaussian process'
- 'MCMC'
implementations: []
summary: >-
  Williamson, Orbanz & Ghahramani (2010), AISTATS 2010, PMLR 9: 924–931. To
  let binary latent feature models follow a distribution that changes over
  time, space or another covariate, a dependent IBP generates for each
  covariate value a binary matrix with unboundedly many columns, its
  evolution over the covariate controlled by a hierarchical Gaussian process
  whose covariance sets the dependence and exchangeability. MCMC inference;
  experiments find explicit dependence improves prediction (abstract).
---
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction this work bears on, filed from the same exchange, cited as open -->

# LIT-tmpporrt: Dependent Indian Buffet Processes

Williamson, S., Orbanz, P. & Ghahramani, Z. (2010). Dependent Indian buffet
processes. In *Proceedings of the Thirteenth International Conference on
Artificial Intelligence and Statistics*, PMLR 9: 924–931.
https://proceedings.mlr.press/v9/williamson10a.html.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T22 for perspectives becoming active, inactive or reorganized as a
company changes, and at T23 as the construction its dynamic model is not.
T23's model keeps the IBP prior only at its first time step ([CASE-tmplcm41](../cases.d/CASE-tmplcm41.md));
this is the established model in which the feature allocation stays
IBP-distributed at every covariate value, and so the comparator for that
case and for [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).
