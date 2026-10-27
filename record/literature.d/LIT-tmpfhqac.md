---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmptxvho](../notes.d/NOTE-tmptxvho.md)) in full, from PMLR's own PDF; worth
  reading for the stick-breaking construction of the Indian buffet
  process, in which the feature probabilities in decreasing order are
  products of independent Beta(α, 1) draws, for its duality with the
  Dirichlet process's sticks, and for the slice samplers it licenses,
  which the Markov IBP's inference uses ([THEORY-tmphvhg6](../theory.d/THEORY-tmphvhg6.md)). Read it knowing
  that its truncation is described but its error is not computed, that
  its sampler comparison is reported only as a chart of autocorrelation
  times, and that its MNIST demonstration is a single run judged by eye.
title: 'Stick-breaking Construction for the Indian Buffet Process'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("file the next
    readings"): the curation entry of 2026-10-27 02:06 lists it among the
    works the infinite factorial HMM names (LIT-1577, §2.4, whose
    stick-breaking construction and slice sampler rest on it), and
    NOTE-1172 records the review's citation of it ("Teh et al. 2007").
    Checked on 2026-10-27 against the PMLR abstract page and the PDF's
    header: Yee Whye Teh, Dilan Görür and Zoubin Ghahramani, "Stick-breaking
    Construction for the Indian Buffet Process", Proceedings of the
    Eleventh International Conference on Artificial Intelligence and
    Statistics, PMLR 2: 556–563. PMLR's metadata dates it 2007-03-11, which
    is `published:` (ADR-002, as LIT-1548 takes its PMLR date). PMLR
    misspells the second author "Grür"; the PDF's "Görür" is used. It has
    no arXiv deposit and no DOI; the source is the PMLR page. The summary
    follows the abstract.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmptxvho): §§1–8, the appendix, the figure
    captions and the references, from the PMLR PDF. Status Deferred →
    Active. THEORY-tmphvhg6 filed (Active). The summary is checked against
    the reading and given the construction's form.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
published: '2007-03-11'
url: 'https://proceedings.mlr.press/v2/teh07a.html'
first_author: 'Teh'
keywords:
- 'Indian buffet process'
- 'stick-breaking construction'
- 'slice sampling'
- 'beta process'
- 'nonparametric Bayes'
implementations: []
extends:
- LIT-tmp3u0k8
summary: >-
  Teh, Görür & Ghahramani (2007), AISTATS, PMLR 2: 556–563. In the limit
  of the IBP's finite model, the feature probabilities in decreasing
  order are μ_(k) = ∏_{l≤k} ν_l with ν_l ~ Beta(α, 1) independent; the
  pieces broken off are the Dirichlet process's GEM(α) weights. A slice
  sampler built on it truncates the representation adaptively and needs
  no conjugacy; a semi-ordered variant, on synthetic linear-Gaussian
  data, mixes as fast as the conjugate Gibbs sampler, and it is
  demonstrated on 1000 MNIST threes.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this work bears on, cited as open -->

# LIT-tmpfhqac: Stick-breaking Construction for the Indian Buffet Process

Teh, Y. W., Görür, D. & Ghahramani, Z. (2007). Stick-breaking
construction for the Indian buffet process. In *Proceedings of the
Eleventh International Conference on Artificial Intelligence and
Statistics*, PMLR 2: 556–563.

Read in full on 2026-10-27 ([NOTE-tmptxvho](../notes.d/NOTE-tmptxvho.md)). One account was drawn from
it: [THEORY-tmphvhg6](../theory.d/THEORY-tmphvhg6.md).

## Why this is here

The owner asked on 2026-10-27 to "file the next readings". The Markov IBP
([LIT-1577](LIT-1577.md), §2.4) rests on this construction for its slice sampler, and
the IBP review ([LIT-1556](LIT-1556.md)) names it among the process's variants. [CASE-165](../cases.d/CASE-165.md)
(item 1) says that "a stick-breaking truncation at 16 would be close" to
the buffet's count, 8.97 against 9.31, simulated; this is the
construction that statement is about, and the record held it only by
name.
