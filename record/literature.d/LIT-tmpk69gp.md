---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpcuo7o) in full, from arXiv 0710.0845v3, the
  authors' revision; worth reading for the nested Chinese restaurant
  process as a prior on trees of unbounded depth and branching (THEORY-tmp5t37f), for hLDA's single-path model of a document and what that does
  to overlap, and for a careful simulated-recovery test (THEORY-tmpvs18m).
  Read it knowing that §5.1's level conditional does not match §2.4's
  parameterization of the GEM and §6.2's hyperparameters are out of range
  as printed, that it has no identifiability result, that its comparison
  with LDA rests on harmonic-mean estimates on one corpus (THEORY-tmpi9pkg, Proposed), and that the typeset JACM text was not compared.
title: 'The nested Chinese restaurant process and Bayesian nonparametric inference of topic hierarchies'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T21 the owner proposed hierarchical LDA, and the
    reply attributes classical hLDA to "Blei, Griffiths, and Jordan" with a
    link to "Journal of the ACM" and no title, which is this paper. Checked
    on 2026-10-26 against Crossref and the arXiv record: David M. Blei,
    Thomas L. Griffiths and Michael I. Jordan, Journal of the ACM 57(2),
    1–30, online 8 February 2010; arXiv 0710.0845, v1 submitted 3 October
    2007, which is earlier and is `published:` (ADR-002). hLDA was
    introduced earlier still, in a different paper (Blei, Griffiths, Jordan
    and Tenenbaum, NIPS 2003, "Hierarchical topic models and the nested
    Chinese restaurant process"), which no reply cited and which is not
    registered. OpenAlex lists the arXiv copy as open. The summary follows
    the abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full at the owner's request (NOTE-tmpcuo7o), from arXiv
    0710.0845v3, which OpenAlex lists as the open copy. Status Deferred
    → Active. Three THEORYs filed: THEORY-tmp5t37f and THEORY-tmpvs18m
    Active, THEORY-tmpi9pkg Proposed. The summary is checked against the
    reading and kept, without its "(abstract)" marker.
tags:
- probabilistic-modeling
- information-retrieval
date: '2026-10-26'
published: '2007-10-03'
arxiv: '0710.0845'
doi: '10.1145/1667053.1667056'
first_author: 'Blei'
keywords:
- 'nested Chinese restaurant process'
- 'hierarchical topic model'
- 'hLDA'
- 'Bayesian nonparametrics'
- 'topic hierarchies'
implementations: []
summary: >-
  Blei, Griffiths & Jordan (2010), J. ACM 57(2). The nested Chinese
  restaurant process (nCRP) assigns probability distributions to infinitely
  deep, infinitely branching trees and serves as a prior in a nonparametric
  model of document collections: each document is a path down a random tree,
  its words are allocated to levels along the path, and the nCRP's
  preferential attachment clusters documents by topics shared at several
  levels of abstraction. Posterior inference over trees, topics and
  allocations is demonstrated on scientific abstracts.
---
<!-- inactive-ok-file: THEORY-tmpi9pkg — Proposed; filed from this reading, cited as open -->

# LIT-tmpk69gp: The nested Chinese restaurant process and Bayesian nonparametric inference of topic hierarchies

Blei, D. M., Griffiths, T. L. & Jordan, M. I. (2010). The nested Chinese
restaurant process and Bayesian nonparametric inference of topic
hierarchies. *Journal of the ACM* 57(2): 1–30. doi:10.1145/1667053.1667056.
arXiv:0710.0845.

Read in full on 2026-10-26 from arXiv 0710.0845v3 (NOTE-tmpcuo7o). The
summary is checked against the reading.

## Why this is here

Cited at T21, where the owner asked whether hLDA could infer higher-level
perspectives from employees' activity, and the reply took it as the starting
point while warning that its topics are not perspectives. The record held
the nCRP only as the single-path limit that the nested HDP of [LIT-002](LIT-002.md)
([NOTE-023](../notes.d/NOTE-023.md)) relaxes, and the hierarchical Pitman–Yor topic models of [LIT-013](LIT-013.md),
which T21 did not use. It is one of the candidate methods of [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).
