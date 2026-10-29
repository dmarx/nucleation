---
status: Active
status_note: >-
  read in full 2026-10-29 (NOTE-tmp6nipz) from the ACL Anthology PDF;
  worth reading for the proof that, under a metric random walk, log
  co-occurrence over long windows converges to squared latent distance
  whatever the one-step link, so embeddings identify a metric and
  coordinates only up to isometry; its evidence that real corpora have
  a Euclidean semantic space is weaker than its theorem.
title: 'Word Embeddings as Metric Recovery in Semantic Spaces'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A6 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is Crossref, December 2016 only, so
    `published:` means December 2016 (TACL 4, 273–286). The MIT Press
    page answered with a bot challenge. A broader earlier preprint by
    the same authors, arXiv 1509.05808 ("Word, graph and manifold
    embedding from Markov processes"), is not taken as this work
    (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full in NOTE-tmp6nipz, from aclanthology.org/Q16-1020.pdf
    (the published version, CC BY 4.0), including Appendices A–C. Filed
    THEORY-tmp6quku (log co-occurrence recovers the metric under the
    random-walk model; Active, checked numerically) and THEORY-tmp259r0
    (corpus co-occurrences fit a Euclidean semantic space; Proposed).
    Status Deferred → Active; summary rewritten from the text. Citation
    corrected: the paper's first page reads "Published 7/2016", earlier
    than Crossref's December 2016 print date, so `published:` becomes
    2016-07-01 by ADR-002's earlier-date rule (no day is given; the
    alternative is Crossref's 2016-12). The flag `anthology-candidate`
    is added for its embedding method and benchmark comparison.
tags:
- representation-learning
- mathematics
- anthology-candidate
date: '2026-10-29'
published: '2016-07-01'
doi: '10.1162/tacl_a_00098'
first_author: 'Hashimoto'
keywords:
- 'word embeddings'
- 'metric recovery'
- 'semantic spaces'
- 'manifold learning'
- 'random walks'
implementations: []
summary: >-
  Hashimoto, Alvarez-Melis & Jaakkola (2016). If text were a random walk
  whose steps depend on distance in a latent space, negative log
  co-occurrence over a long window, less per-word terms, would converge to
  squared latent (geodesic) distance whatever the one-step link. Under
  that toy model, which the authors say is not a model of language,
  GloVe, softmax word2vec and PMI-SVD have the true embedding among their
  optima, up to isometry; a negative-binomial "metric regression" matches
  them on analogy, series and classification tasks, and word embedding of
  graph random walks does manifold learning on MNIST. Evidence that real
  co-occurrences form a Euclidean space is a correlation of 0.75 with
  human similarity and two nearest-neighbour statistics.
---

# LIT-tmp6ic5n: Word Embeddings as Metric Recovery in Semantic Spaces

Hashimoto, T. B., Alvarez-Melis, D., & Jaakkola, T. S. (2016). Word embeddings as metric recovery in semantic spaces. *TACL*, 4, 273–286.

Read in full in NOTE-tmp6nipz.

## Why this is here

A6's precursor to [LIT-tmpprsxm](LIT-tmpprsxm.md): a coordinate system may be arbitrary while the relations it represents are not. A6's caution is kept: a co-occurrence geometry is not a geometry of pragmatic meaning, and the record's version would recover distances from receivers' responses ([CLAIM-046](../claims.d/CLAIM-046.md)).
