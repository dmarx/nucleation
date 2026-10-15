---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' arXiv preprint, version 4 of 14 August
  2018 (arxiv.org/pdf/1603.09320v4, 13 pp., the last arXiv version, whose abstract
  matches the published one apart from copy-editing; the TPAMI body was not seen).
  Version 1 (2016) was compared: it claimed deletion, which v4 drops and lists as
  future work. Unpaywall and OpenAlex list no open-access copy of the TPAMI version.
  Worth reading as the source of the hierarchical graph index: nested proximity
  graphs on geometrically sampled layers, with a neighbour rule that keeps links
  between clusters. Its logarithmic search cost is derived only for exact Delaunay
  graphs of bounded degree, which it does not build, and is measured only on uniform
  random data in 4 and 8 dimensions; on 200M SIFT the scaling "deviates from the
  pure logarithm". It gives no worst-case or recall guarantee and no deletion. For
  [CLAIM-310](../claims.d/CLAIM-310.md) it shows, with bins replaced by graphs, that the arrangement of fixed
  data under a fixed distance decides cost and, on clustered data, whether items
  can be found at all; it narrows part 2, since the index is built without any query
  mix and every test drew its queries from the data. For [QUESTION-114](../questions.d/QUESTION-114.md) it supplies
  a measured build-time against query-time curve and O(N log N) construction argued
  at low dimension, with insertion upkeep only.
title: Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical
  Navigable Small World Graphs
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: IEEE TPAMI 2020. arXiv v1 submitted
    30 March 2016. Not held in the Anthology of the SOTA: a grep of its record/
    (clone of 2026-10-15, commit d1573d2) for the title and authors found nothing.
    Read the same day (NOTE-tmpkpp45).
tags:
- information-retrieval
- network-science
- anthology-candidate
date: '2026-10-15'
published: '2016-03-30'
arxiv: '1603.09320'
first_author: Malkov
keywords: []
implementations: []
summary: >-
  Malkov and Yashunin (2020), IEEE TPAMI 2020. HNSW is a stack of proximity graphs
  on nested random subsets of the data. Each element's top layer is drawn from a
  geometric distribution, and new neighbours are chosen by a pruning rule that favours
  diverse directions. Searching from the sparse top layer down makes per-query cost
  grow about logarithmically with N on uniform random data in 4 and 8 dimensions,
  which flat NSW graphs did not. The logarithmic bound is derived only for exact
  Delaunay graphs of bounded mean degree, which HNSW does not build. For the graphs
  it does build, logarithmic scaling is measured, at low dimension only, and on
  200M SIFT vectors the paper reports the scaling "deviates from the pure logarithm".
  The neighbour-selection rule is what keeps clustered data searchable: in the paper's
  synthetic test with 100 isolated clusters, linking each element to its nearest
  neighbours fails to reach high recall. There is no worst-case or recall guarantee,
  no deletion, and no analysis of query distributions unlike the data.
---

# LIT-tmp08vve: Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs

Malkov, Y. A. and Yashunin, D. A. (2020). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 42(4), 824–836. DOI 10.1109/TPAMI.2018.2889473

## Key takeaways

Read in full ([NOTE-tmpkpp45](../notes.d/NOTE-tmpkpp45.md)). HNSW is a stack of proximity graphs on nested random subsets of the data. Each element's top layer is drawn from a geometric distribution, and new neighbours are chosen by a pruning rule that favours diverse directions. Searching from the sparse top layer down makes per-query cost grow about logarithmically with N on uniform random data in 4 and 8 dimensions, which flat NSW graphs did not. The logarithmic bound is derived only for exact Delaunay graphs of bounded mean degree, which HNSW does not build. For the graphs it does build, logarithmic scaling is measured, at low dimension only, and on 200M SIFT vectors the paper reports the scaling "deviates from the pure logarithm". The neighbour-selection rule is what keeps clustered data searchable: in the paper's synthetic test with 100 isolated clusters, linking each element to its nearest neighbours fails to reach high recall. There is no worst-case or recall guarantee, no deletion, and no analysis of query distributions unlike the data.

## Why this is here

[CLAIM-310](../claims.d/CLAIM-310.md), with [LIT-tmp7dffg](LIT-tmp7dffg.md) and [LIT-tmpllfsb](LIT-tmpllfsb.md): the graph index in widest use. Its logarithmic search time is proved only for idealized graphs it does not build and measured only at low dimension; its clearest result is that the neighbour-selection rule decides whether clustered items are findable. The final version supports insertion only.
