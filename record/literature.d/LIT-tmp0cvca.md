---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' University of Wisconsin–Madison technical
  report of the same title (CS TR [#1377](https://github.com/dmarx/nucleation/issues/1377), June 1998, 19 pp.), served by the department's
  archive (research.cs.wisc.edu/techreports/1998/TR1377.pdf) and, byte-identical,
  by the MINDS@UW repository (minds.wisconsin.edu/handle/1793/60174), which OpenAlex
  lists as the submitted version. The ICDT '99 chapter itself is closed (Unpaywall,
  OpenAlex, Semantic Scholar) and was not seen; the CiteSeerX copy redirects to
  the Internet Archive, which was unreachable. The report is a scan, read by OCR
  and page images. Worth reading as the source of the sufficient condition for nearest-neighbour
  contrast to vanish: if the variance of the p-th power of the query-to-point distance,
  divided by its mean, goes to zero, then with a fixed number of points the farthest
  is within any factor 1 + ε of the nearest with probability tending to one. IID
  coordinates satisfy it, and so do several correlated or non-identical workloads.
  Data on a low-dimensional subspace, and queries that land in well-separated clusters,
  do not. Simulations put the loss of contrast within 10 to 20 dimensions for IID
  data. The condition is sufficient and not shown necessary, n is held fixed, the
  result concerns the ratio of distances, and the paper measures no index. For [CLAIM-309](../claims.d/CLAIM-309.md)
  it has no bearing, and the filing's "no arrangement by similarity discriminates"
  overstates it. For [CLAIM-310](../claims.d/CLAIM-310.md) it corroborates that what serves retrieval depends
  on the query distribution: the same clustered data is meaningful for queries inside
  clusters and not for uniform ones, and the meaningful answer there is the whole
  cluster. For [QUESTION-114](../questions.d/QUESTION-114.md) it sets a precondition: under its condition there is
  no nearest neighbour worth organizing to find.
title: When Is "Nearest Neighbor" Meaningful?
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: ICDT '99. Crossref gives 1999
    only; ICDT '99 opened in Jerusalem on 10 January 1999, which `published:` uses.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15,
    commit d1573d2) for the title and authors found nothing. Read the same day (NOTE-tmps473y).
tags:
- databases
- information-retrieval
- mathematics
date: '2026-10-15'
published: '1999-01-10'
doi: 10.1007/3-540-49257-7_15
first_author: Beyer
keywords: []
implementations: []
summary: >-
  Beyer et al. (1999), ICDT '99. For a fixed number n of data points and a query
  drawn independently of them, if the variance of the p-th power of the query-to-point
  distance, divided by its mean, goes to zero as dimension m grows, then the farthest
  point is, with probability tending to one, within any factor 1 + ε of the nearest
  (Theorem 1). The condition holds for IID dimensions and for several correlated
  or non-identical workloads, and fails when data and queries lie on a low-dimensional
  subspace or when queries fall inside well-separated clusters. Simulations put
  the collapse of contrast within 10 to 20 dimensions for IID data, and two real
  image-feature sets showed weak contrast. The condition is sufficient, not shown
  necessary; the theorem is about the ratio of distances with n held fixed, and
  says nothing about real data of low intrinsic dimension except that such data
  can escape it.
---

# LIT-tmp0cvca: When Is "Nearest Neighbor" Meaningful?

Beyer, K., Goldstein, J., Ramakrishnan, R. and Shaft, U. (1999). When is "nearest neighbor" meaningful? In *Database Theory — ICDT'99*, LNCS 1540, pp. 217–235. DOI 10.1007/3-540-49257-7_15

## Key takeaways

Read in full ([NOTE-tmps473y](../notes.d/NOTE-tmps473y.md)). For a fixed number n of data points and a query drawn independently of them, if the variance of the p-th power of the query-to-point distance, divided by its mean, goes to zero as dimension m grows, then the farthest point is, with probability tending to one, within any factor 1 + ε of the nearest (Theorem 1). The condition holds for IID dimensions and for several correlated or non-identical workloads, and fails when data and queries lie on a low-dimensional subspace or when queries fall inside well-separated clusters. Simulations put the collapse of contrast within 10 to 20 dimensions for IID data, and two real image-feature sets showed weak contrast. The condition is sufficient, not shown necessary; the theorem is about the ratio of distances with n held fixed, and says nothing about real data of low intrinsic dimension except that such data can escape it.

## Why this is here

[CLAIM-310](../claims.d/CLAIM-310.md) and [QUESTION-114](../questions.d/QUESTION-114.md): under a variance condition on data and queries jointly, the nearest and farthest neighbours become nearly equidistant as dimension grows. The condition is sufficient only, and clustered queries, near matches and data with few latent degrees of freedom escape it; the paper's remedy for clustered data is to return the whole nearest cluster.
