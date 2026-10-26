---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmp9d3rs) in full, from PMLR's own PDF; worth
  reading for the beta process as the IBP's de Finetti measure, with the
  predictive and the count of distinct features that follow
  (THEORY-tmpgy035), and for the hierarchical beta process, the
  established way for groups to share one feature library at
  group-specific prevalences (THEORY-tmpz726y). Read it knowing that
  conjugacy is cited rather than proved, that its groups are disjoint and
  static, that its one experiment is a single text-classification split,
  and that its stated reason for a small group concentration reads
  against its own (9).
title: 'Hierarchical Beta Processes and the Indian Buffet Process'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T22 the reply cites "Thibaux and Jordan's
    construction" for sharing latent features across related groups with
    different frequencies in each, and at T23 for a hierarchical
    beta-process prior letting formal teams share a feature library, both
    linking "proceedings.mlr.press" with no title. Checked on 2026-10-26
    against the PMLR page: Romain Thibaux and Michael I. Jordan, Proceedings
    of the Eleventh International Conference on Artificial Intelligence and
    Statistics, PMLR 2: 564–571, dated 11 March 2007, which is `published:`.
    No DOI or arXiv copy. The summary follows the PMLR abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmp9d3rs) from PMLR's PDF,
    https://proceedings.mlr.press/v2/thibaux07a/thibaux07a.pdf, §§1–8 and
    the appendix. Status Deferred → Active. THEORY-tmpgy035 and
    THEORY-tmpz726y filed. The summary is checked against the reading and
    kept.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
published: '2007-03-11'
url: 'https://proceedings.mlr.press/v2/thibaux07a.html'
first_author: 'Thibaux'
keywords:
- 'beta process'
- 'Indian buffet process'
- 'de Finetti'
- 'hierarchical beta process'
- 'document classification'
implementations: []
summary: >-
  Thibaux & Jordan (2007), AISTATS 2007, PMLR 2: 564–571. The beta process
  is the de Finetti mixing distribution underlying the Indian buffet
  process, playing for it the role the Dirichlet process plays for the
  Chinese restaurant process. The paper uses the parallel to define
  hierarchies of beta processes and to derive posterior inference algorithms
  for the IBP, with an application to document classification related to
  smoothed naive Bayes (abstract).
---
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction this work bears on, filed from the same exchange, cited as open -->

# LIT-tmpday8e: Hierarchical Beta Processes and the Indian Buffet Process

Thibaux, R. & Jordan, M. I. (2007). Hierarchical beta processes and the
Indian buffet process. In *Proceedings of the Eleventh International
Conference on Artificial Intelligence and Statistics*, PMLR 2: 564–571.
https://proceedings.mlr.press/v2/thibaux07a.html.

Read 2026-10-26 in full, in NOTE-tmp9d3rs. The summary was checked
against the reading and holds.

## Why this is here

Cited at T22 and T23 as the established way for teams to share a feature
library at team-specific prevalences, the alternative to the team-level
structure that T23's model writes by hand. It bears on [CASE-tmplcm41](../cases.d/CASE-tmplcm41.md) and on
[QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).
