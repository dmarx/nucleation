---
status: Active
status_note: >-
  read in full 2026-10-27 (NOTE-tmplhrxg), from arXiv v2; worth reading as
  the paper that posed angular synchronization with outliers and sketched
  its extension to other groups, and as a clean case that
  separates what pairwise evidence determines from what a cheap method can
  recover: an information bound that binds every algorithm, and a spectral
  relaxation whose threshold sits within an L-dependent factor of it. The
  spectral threshold is a careful heuristic confirmed by simulation, not a
  theorem.
title: 'Angular synchronization by eigenvectors and semidefinite programming'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read. Checked against Crossref and the arXiv API on
    2026-10-27: Amit Singer, Applied and Computational Harmonic Analysis
    30(1), 20–36, January 2011. arXiv 0905.3174 v1 was submitted on 20
    May 2009, which is `published:` per ADR-002.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full from the arXiv preprint 0905.3174v2 (20 November 2009),
    25 pp.: §§1–7, Figures 4.1–4.3, Tables 4.1–4.3 and the references; the
    first NOTE on the work (NOTE-tmplhrxg). The published text was not
    read. Status set from the reading: Active. `published:` and the
    identifiers stand; the preprint's title is the journal's. Tags
    widened to information-theory and network-science (§5 is an
    information-theoretic bound; synchronization is in the
    network-science blurb). The summary is replaced by one from the text.
    The registration's summary held up, with two corrections: the angles
    are recovered only up to one common additive phase, and the
    outlier-robustness is shown by a random-matrix threshold argument
    (p > 1/√n on the complete graph) and simulation, not for "most"
    outliers in general. The exchange (A21 §8) said the paper addresses
    "the computational cost" of recovery: it does, but as complexity
    (O(n²) or O(m) per power iteration, O(mLⁿ) for exhaustive maximum
    likelihood, NP-hardness of Max-2-Lin cited), and its finding is that
    the polynomial method is near the information bound, so evidence,
    not computation, is what mostly limits recovery. Two THEORYs are filed
    from it (THEORY-tmpco2va, THEORY-tmp24sxe).
tags:
- mathematics
- information-theory
- network-science
date: '2026-10-27'
published: '2009-05-20'
arxiv: '0905.3174'
doi: '10.1016/j.acha.2010.02.001'
first_author: 'Singer'
keywords:
- 'angular synchronization'
- 'group synchronization'
- 'spectral relaxation'
- 'semidefinite programming'
implementations: []
summary: >-
  Singer (2011). Estimates n angles, up to one common phase, from noisy
  measurements of their pairwise offsets when an unknown share are
  outliers uniform on the circle, by the top eigenvector of the Hermitian
  matrix of e^{iδᵢⱼ} or by a complex Goemans–Williamson SDP. A
  random-matrix argument puts the eigenvector's threshold at a share
  p > 1/√n of good offsets on the complete graph, and simulations recover
  400 angles with 85% outliers at correlation 0.97. Fano's inequality
  shows no algorithm can succeed below a threshold of order √(n/m), and
  the eigenvector method is within a factor √((L − 1)/(2 log₂ L)) of it,
  where exhaustive maximum likelihood costs O(mLⁿ). Extensions to other
  compact groups, cryo-EM and clock synchronization are sketched.
---
<!-- inactive-ok-file: CLAIM-tmpdjt64 CLAIM-tmpi1bjh THEORY-tmp24sxe — Proposed; the claims it was filed for and a THEORY filed from it, cited as open -->

# LIT-tmpjnkzw: Angular synchronization by eigenvectors and semidefinite programming

Singer, A. (2011). Angular synchronization by eigenvectors and semidefinite programming. *Applied and Computational Harmonic Analysis*, 30(1), 20–36. doi:10.1016/j.acha.2010.02.001.

Read in full on 2026-10-27 (NOTE-tmplhrxg).

## Why this is here

A21 §8 cited it for the gap between a compatible global configuration
existing and an apparatus recovering it from pairwise evidence at a
cost: "Interaction produces relational evidence, but recovering a larger
structure from that evidence is itself a resource-bounded process." It
bears on CLAIM-tmpdjt64 and CLAIM-tmpi1bjh.
