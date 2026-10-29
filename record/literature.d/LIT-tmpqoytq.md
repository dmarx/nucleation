---
status: Active
status_note: >-
  read in full 2026-10-29 ([NOTE-tmpi3f1e](../notes.d/NOTE-tmpi3f1e.md)); worth reading as the first
  systematic test of when unsupervised dictionary induction fails, and
  for its finding that whether two embedding spaces align depends on
  the corpus domain and the embedding algorithm as much as on the
  languages ([THEORY-tmpox88b](../theory.d/THEORY-tmpox88b.md)). The method tested is adversarial
  (Conneau et al. 2018), not GW.
title: 'On the Limitations of Unsupervised Bilingual Dictionary Induction'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A5 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2018-05-09 (ACL 2018,
    doi 10.18653/v1/P18-1072) (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 1805.03620v1, 11 pp., in
    NOTE-tmpi3f1e; status Deferred → Active. The citation stands. The
    summary is rewritten from the text: the paper tests one adversarial
    method, its failures are partly seed instability, and its reported
    correlation is negative in sign. Tagged anthology-candidate
    (ADR-005): it recommends weak supervision from identical words for
    ML practice.
tags:
- translation
- representation-learning
- anthology-candidate
date: '2026-10-29'
published: '2018-05-09'
arxiv: '1805.03620'
first_author: 'Søgaard'
keywords:
- 'bilingual dictionary induction'
- 'cross-lingual word embeddings'
- 'isomorphism'
- 'graph similarity'
- 'morphologically rich languages'
implementations: []
summary: >-
  Søgaard, Ruder & Vulić (2018). Tests the adversarial unsupervised
  dictionary induction of Conneau et al. (2018) outside its reported
  conditions. It fails (P@1 ≈ 0) for English paired with Estonian or
  Finnish, also with a 1.7B-word Finnish corpus; across corpus domains,
  even for English–Spanish; and between a skip-gram and a CBOW space.
  A seed of identically spelled words does as well or better. A
  Laplacian-spectrum dissimilarity of 10-node nearest-neighbour graphs
  tracks success across eight pairs (|ρ| = 0.89; negative, since it is a
  dissimilarity), but is computed with the gold translations. About one
  seed in ten succeeds for Estonian, Finnish and Greek, so part of the
  failure is the optimiser.
---

# LIT-tmpqoytq: On the Limitations of Unsupervised Bilingual Dictionary Induction

Søgaard, A., Ruder, S., & Vulić, I. (2018). On the limitations of unsupervised bilingual dictionary induction. *Proceedings of ACL 2018*, 778–788.

Read in full in [NOTE-tmpi3f1e](../notes.d/NOTE-tmpi3f1e.md).

## Why this is here

A5's counterweight to [LIT-tmpprsxm](LIT-tmpprsxm.md): structural alignment recovers correspondence only where the two structures are alike, so a good fit is not established identity. It bears on [CLAIM-135](../claims.d/CLAIM-135.md) and on the identification threat in [CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md). One correction to that description: the paper tests Conneau et al.'s adversarial method, not GW, so it is a counterweight to [LIT-tmpprsxm](LIT-tmpprsxm.md) by shared premise, not by direct test. It adds that the likeness of two structures depends on how they were built: two spaces of the same language pair trained by different algorithms do not align at all ([THEORY-tmpox88b](../theory.d/THEORY-tmpox88b.md)).
