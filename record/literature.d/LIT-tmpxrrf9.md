---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'The Indian Buffet Process: An Introduction and Review'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T22 the reply links "jmlr.org" twice, with no author
    or title, for the classical IBP as a prior over binary
    feature-allocation matrices and for the expected number of occupied
    features, αH_N; at T23 "jmlr.csail.mit.edu" (JMLR's older host) for
    finite beta–Bernoulli approximations, which this review derives in its
    §3, so the three links are taken as this work. Checked on 2026-10-26
    against the JMLR abstract page and the PDF's header: Thomas L. Griffiths
    and Zoubin Ghahramani, JMLR 12(32): 1185–1224, "Submitted 3/10; Revised
    3/11; Published 4/11". JMLR gives no DOI and no day, so `published:` is
    2011-04-01, meaning April 2011 (ADR-002). The original conference paper
    (Griffiths and Ghahramani, NIPS 2005, "Infinite latent feature models
    and the Indian buffet process") was not cited and is not registered. The
    summary follows the JMLR abstract.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
published: '2011-04-01'
url: 'https://jmlr.org/papers/v12/griffiths11a.html'
first_author: 'Griffiths'
keywords:
- 'Indian buffet process'
- 'latent feature model'
- 'beta process'
- 'sparse binary matrices'
- 'nonparametric Bayes'
implementations: []
summary: >-
  Griffiths & Ghahramani (2011), JMLR 12: 1185–1224. The Indian buffet
  process is a distribution over equivalence classes of sparse binary
  matrices with finitely many rows and an unbounded number of columns,
  usable as a prior for objects represented by a potentially infinite array
  of features. The paper derives it as the limit of a finite beta–Bernoulli
  model, illustrates it in an infinite latent feature model, and reviews its
  applications, extensions and connections to other stochastic processes
  (abstract).
---
<!-- inactive-ok-file: CLAIM-tmpwr001 — Proposed; the claim this work bears on, cited as open -->
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction this work bears on, filed from the same exchange, cited as open -->

# LIT-tmpxrrf9: The Indian Buffet Process: An Introduction and Review

Griffiths, T. L. & Ghahramani, Z. (2011). The Indian buffet process: An
introduction and review. *Journal of Machine Learning Research* 12:
1185–1224. https://jmlr.org/papers/v12/griffiths11a.html.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T22, where the owner proposed the Indian buffet process for
inferring employees' overlapping latent features without fixing their
number, and at T23, whose dynamic beta–Bernoulli model starts from an IBP
prior truncated at a finite K. The record held the IBP only as the
alternative Friston et al. name in [NOTE-485](../notes.d/NOTE-485.md) ([LIT-615](LIT-615.md)). The reply's marginal
E[K_N] = αH_N is checked in [CASE-tmplcm41](../cases.d/CASE-tmplcm41.md), with where its finite and dynamic
versions depart from it. It is the candidate method of [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md), and the
IBP is the latent-feature prior on which [CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md)'s distinction turns.
