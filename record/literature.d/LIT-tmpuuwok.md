---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmpq065x](../notes.d/NOTE-tmpq065x.md)) in full, from the arXiv PDF of v2
  (30 April 2026); worth reading for the method of tracking features
  across pretraining checkpoints with one joint dictionary, and for
  separating a feature's presence (decoder norm) from its causal use
  (RelIE). Read it knowing that its developmental trends rest on the
  authors' annotation of a few top features ([THEORY-tmpt45mh](../theory.d/THEORY-tmpt45mh.md), Proposed),
  that it covers one layer and two or three checkpoints at a time, and
  that a feature shared across checkpoints is shared by construction of
  the dictionary, not shown to be carried forward.
title: 'Crosscoding Through Time: Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T24 the reply says "Recent cross-checkpoint
    crosscoder research directly tracks feature emergence, maintenance, and
    discontinuation", with no author or title. The abstract of this paper
    ends in those words, and an arXiv search on 2026-10-26 for crosscoders
    across checkpoints found no other paper that does. Checked against the
    arXiv record: Deniz Bayazit, Aaron Mueller and Antoine Bosselut, arXiv
    2509.05291, v1 submitted 5 September 2025, which is `published:`; v2 (30
    April 2026) says it was accepted to ACL 2026. The summary follows the
    arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpq065x) from the arXiv PDF of 2509.05291v2. Status
    Deferred → Active. One account filed: THEORY-tmpt45mh (Proposed). The
    summary is checked against the reading; "checkpoint triplets" is
    widened to "pairs and triplets", which the paper uses both.
tags:
- representation-learning
- linguistics
- anthology-candidate
date: '2026-10-26'
published: '2025-09-05'
arxiv: '2509.05291'
first_author: 'Bayazit'
keywords:
- 'sparse crosscoders'
- 'model checkpoints'
- 'pretraining'
- 'feature emergence'
- 'Relative Indirect Effects'
- 'RelIE'
implementations: []
summary: >-
  Bayazit, Mueller & Bosselut (2025), arXiv:2509.05291, ACL 2026. Sparse
  crosscoders trained between pairs and triplets of pretraining checkpoints with large
  performance and representation shifts discover and align features across
  checkpoints; a metric, Relative Indirect Effects (RelIE), traces the stage
  at which a feature becomes causally important for a task. Crosscoders
  detect feature emergence, maintenance and discontinuation during
  pretraining (abstract).
---
<!-- inactive-ok-file: THEORY-tmpt45mh — Proposed; the account filed from this reading, cited as open -->
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction this work bears on, filed from the same exchange, cited as open -->

# LIT-tmpuuwok: Crosscoding Through Time: Tracking Emergence & Consolidation Of Linguistic Representations Throughout LLM Pretraining

Bayazit, D., Mueller, A. & Bosselut, A. (2025). Crosscoding through time:
Tracking emergence & consolidation of linguistic representations throughout
LLM pretraining. *ACL 2026*. arXiv:2509.05291.

Read in full on 2026-10-26 ([NOTE-tmpq065x](../notes.d/NOTE-tmpq065x.md)). The summary is checked
against the reading.

## Why this is here

Cited at T24 as the methods and baselines for tracking which features
appear, persist and disappear over training, the comparator the reply's
dynamic latent-feature model must beat ("The dynamic IBP must earn its
complexity"). The record had no crosscoder work. It bears on [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md) and
[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md).
