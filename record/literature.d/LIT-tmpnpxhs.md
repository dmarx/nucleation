---
status: Active
status_note: >-
  read in full 2026-10-27 (NOTE-tmpzqos6), from arXiv v2; worth reading
  as the standard introduction to sheaf Laplacians: the kernel is the
  global sections, the heat flow projects onto them, and a set of spectral
  graph theory's basics lift with short proofs. Exploratory by its own
  account: no Cheeger inequality, and the applications are sketches.
title: 'Toward a spectral theory of cellular sheaves'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Checked against Crossref and the arXiv API on
    2026-10-27: Jakob Hansen and Robert Ghrist, Journal of Applied and
    Computational Topology 3(4), 315–358, online 30 August 2019. arXiv
    1808.01513 v1 was submitted on 4 August 2018, which is `published:`
    per ADR-002.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full from arXiv 1808.01513v2 (16 August 2019), 46 pp.: all
    nine sections, proofs, figures, footnotes and references; the first
    NOTE on the work (NOTE-tmpzqos6). The journal text was not read.
    Status set from the reading: Active. `published:` (the v1 date) and
    the identifiers stand; the v2 PDF shows only its own date, so the v1
    date rests on the registration's arXiv check. The summary is
    replaced by one from the text. The registration's summary was right
    that the kernel is the global sections and that the heat flow
    converges to the projection onto them (Proposition 8.1, stated for
    ẋ = −Δ^k x in any degree), and right on sparsification and effective
    resistance. It was wrong on "Cheeger-type bounds": the paper proves
    none, and shows the rounding lemma behind the O(n)-bundle inequality
    fails for more general sheaves (§7). "Synchronization" in the paper is
    the estimation problem of finding an approximate global section of
    measured pairwise relations, not oscillator synchronization. Two
    THEORYs are filed from it (THEORY-tmpga5mk, THEORY-tmpvecoh).
tags:
- mathematics
- network-science
date: '2026-10-27'
published: '2018-08-04'
arxiv: '1808.01513'
doi: '10.1007/s41468-019-00038-7'
first_author: 'Hansen'
keywords:
- 'cellular sheaves'
- 'sheaf Laplacian'
- 'spectral theory'
- 'synchronization'
- 'consensus'
implementations: []
summary: >-
  Hansen & Ghrist (2019), J. Appl. Comput. Topology 3. Defines the Hodge
  Laplacians of a cellular sheaf of inner-product spaces; by discrete Hodge
  theory the degree-k kernel is the cohomology H^k, in degree 0 the global
  sections, and the flow ẋ = −Δ^k x converges exponentially to the
  orthogonal projection onto it (Prop. 8.1). Lifts spectral graph theory's
  basics with short proofs: harmonic extension, a bound k + 2 for
  normalized sheaves, interlacing, pushforward, covering and product
  spectra, effective resistance and spectral sparsification. The
  Laplacian does not determine the sheaf, Kron reduction fails in general
  because an interior vertex can impose a non-pairwise boundary
  constraint, and no Cheeger inequality is proved. Consensus, flocking,
  opinion dynamics, communication compression and synchronization are
  sketched as applications.
---
<!-- inactive-ok-file: CLAIM-tmpdjt64 CLAIM-tmpfw510 CLAIM-tmpmx2ql — Proposed or Rejected; the claims it was filed for, cited as open -->

# LIT-tmpnpxhs: Toward a spectral theory of cellular sheaves

Hansen, J., & Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. *Journal of Applied and Computational Topology*, 3(4), 315–358. doi:10.1007/s41468-019-00038-7. Preprint: arXiv:1808.01513.

Read in full on 2026-10-27 (NOTE-tmpzqos6).

## Why this is here

A21 made it the mathematical core of the owner's U20: one operator whose
kernel is exact compatibility and whose spectrum sets the relaxation
rates, so "A mathematically specified system of compatibility
constraints can also determine a hierarchy of dynamical relaxation
rates, when the physical coupling realizes an appropriate Laplacian
flow." The record held the same authors' knowledge-sheaf paper ([LIT-232](LIT-232.md);
[THEORY-299](../theory.d/THEORY-299.md)). It bears on [CLAIM-tmpdjt64](../claims.d/CLAIM-tmpdjt64.md), [CLAIM-tmpfw510](../claims.d/CLAIM-tmpfw510.md) and
[CLAIM-tmpmx2ql](../claims.d/CLAIM-tmpmx2ql.md).
