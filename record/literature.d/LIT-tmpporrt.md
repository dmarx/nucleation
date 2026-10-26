---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpcg7gu) in full, from PMLR's own PDF; worth
  reading for the thresholded-Gaussian-process construction that keeps
  each feature's prevalence fixed over a covariate while its covariance
  sets persistence, the established comparator for a dynamic latent
  feature model (THEORY-tmpumk4q). Read it knowing that its claim of IBP
  marginals at every covariate value holds for the whole matrix only in
  its collapsed model, that features stay independent of one another, and
  that its evidence is two prediction comparisons with the plain IBP.
title: 'Dependent Indian Buffet Processes'
version: 2
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
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpcg7gu) from PMLR's PDF,
    https://proceedings.mlr.press/v9/williamson10a/williamson10a.pdf,
    §§1–6 and Appendix A. Status Deferred → Active. THEORY-tmpumk4q filed.
    The summary is checked against the reading and kept. "Why this is
    here" said the feature allocation stays IBP-distributed at every
    covariate value; the reading narrows that to the collapsed model, and
    the sentence is corrected.
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

Read 2026-10-26 in full, in NOTE-tmpcg7gu. The summary was checked
against the reading and holds.

## Why this is here

Cited at T22 for perspectives becoming active, inactive or reorganized as a
company changes, and at T23 as the construction its dynamic model is not.
T23's model keeps the IBP prior only at its first time step ([CASE-tmplcm41](../cases.d/CASE-tmplcm41.md));
this is the established model in which every item's feature keeps the
same prevalence at every covariate value, the whole allocation staying
IBP-distributed in its collapsed form (THEORY-tmpumk4q), and so the
comparator for that case and for [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).
