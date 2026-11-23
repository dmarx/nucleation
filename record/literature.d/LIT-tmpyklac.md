---
status: Active
status_note: >-
  Skimmed 2026-11-23 ([NOTE-tmpv196v](../notes.d/NOTE-tmpv196v.md)) from arXiv 1811.11636 v3: §§1.2, 4.4,
  8 and 8.2–8.3.1 read closely, the rest by headings. Worth reading as the
  one accessible restatement of the biorthogonal diffusion-wavelet
  construction ([LIT-tmpzikaq](LIT-tmpzikaq.md), Unfetched) and its extension to directed
  graphs, with T = Π^{1/2}PΠ^{−1/2}. Read it knowing that it gives the
  construction and examples, not error bounds.
title: 'Harmonic analysis on directed graphs and applications: From Fourier analysis to wavelets'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Registered and read on 2026-11-23 by the lead run of that date, as a
    stand-in for Maggioni, Bremer, Coifman and Szlam (2005),
    LIT-tmpzikaq, which stays Unfetched (ADR-114). Found by a web search
    for the 2005 report; its reference [36] is that report. Read from
    arXiv 1811.11636 v3 (stamped 1 Nov 2021, 51 pages), text extracted
    with pdftotext. Citation checked against Crossref: Harry Sevi,
    Gabriel Rilling and Pierre Borgnat, Applied and Computational
    Harmonic Analysis 62 (2023) 390–440, doi 10.1016/j.acha.2022.10.003.
    `published:` is the arXiv v1 date, 28 Nov 2018, from the abstract
    page. Held check: searched record/literature.d by arXiv id, DOI,
    title and first author; not held.
tags:
- mathematics
- network-science
- complex-systems
date: '2026-11-23'
published: '2018-11-28'
arxiv: '1811.11636'
doi: '10.1016/j.acha.2022.10.003'
first_author: 'Sevi'
keywords:
- 'harmonic analysis'
- 'graph signal processing'
- 'Fourier analysis'
- 'wavelets'
- 'directed graphs'
- 'random walks'
- 'semi-supervised learning'
implementations: []
summary: >-
  Sevi, Rilling and Borgnat (2018; ACHA 2023). On a strongly connected
  directed graph the eigenvectors of the random walk operator serve as a
  non-orthogonal Fourier basis, and diffusion wavelets extend to the
  directed case with T = Π^{1/2}PΠ^{−1/2}, lazy where needed: at each
  level a subset of the columns of the restricted dyadic power is
  selected, kept as a non-orthogonal basis of scaling functions, and the
  operator is compressed by the pseudo-inverse; wavelets and their duals
  are defined from the projector onto the complement. They say the
  scaling-function construction is that of the 2005 biorthogonal report,
  [LIT-tmpzikaq](LIT-tmpzikaq.md). On the directed cycle of 256 vertices the biorthogonal
  inverse transform has condition number about 2 × 10⁴ against 33 for the
  orthogonal one. Read as the stand-in for the 2005 report.
---
<!-- inactive-ok-file: NOTE-tmpv196v LIT-tmpzikaq — new and Unfetched; the reading of this work and the report it stands in for, filed by the lead run of 2026-11-23 -->

# LIT-tmpyklac: Harmonic analysis on directed graphs and applications: From Fourier analysis to wavelets

Sevi, H., Rilling, G. and Borgnat, P. (2023). Harmonic analysis on
directed graphs and applications: From Fourier analysis to wavelets.
*Applied and Computational Harmonic Analysis* 62, 390–440.
doi:10.1016/j.acha.2022.10.003. arXiv:1811.11636.

## Key takeaways

- The critically sampled construction of §8.2 is the diffusion-wavelet
  chain with the scaling functions left non-orthogonal: selected columns,
  a pseudo-inverse compression, and dual bases. The subspaces it builds
  are the same kind of object as Coifman and Maggioni's, and the
  projector onto each is still orthogonal.
- Non-orthogonal bases cost conditioning: κ ≈ 2 × 10⁴ for the
  biorthogonal transform against 33 for the orthogonal one, on one
  example (§8.3.1).
- No error bound is given for the compressed chain, symmetric or not.

## Standing in the record

Read in place of [LIT-tmpzikaq](LIT-tmpzikaq.md), for the scaling-function construction
only, as the NOTE says.
