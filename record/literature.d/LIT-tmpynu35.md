---
status: Active
status_note: 'read in full 2026-09-27 (NOTE-tmpk6gen); worth reading as the clearest statement of the SDM–attention correspondence. Its exact circle-intersection formula and its eight-algorithm convergence comparison are the parts to take away. Treat its analytic exponential derivation, its GPT-2 "confirmation" and its cerebellar implementation of attention as argument, not demonstration.'
title: 'Attention Approximates Sparse Distributed Memory'
version: 2
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Filed here as well as in the anthology (ANTH-LIT-641), under ADR-013, to
    be read as associative memory: Kanerva's content-addressable retrieval,
    its cerebellar mapping, and attention as a kernel read.
- version: 2
  date: '2026-09-27'
  note: >-
    Read in full (Full text of arXiv:2111.05498v2 (17 Jan 2022; NeurIPS 2021
    camera-ready), 57 pp., via PyMuPDF text extraction. I read the abstract,
    Introduction, §1–§8, the acknowledgements, the reference list and
    Appendices A.1–A.4 and B.1–B.7 (including B.7.1 Random Patterns and
    B.7.2 Learnt Projections). Figures 1–31 are plots or diagrams. I read
    their captions and the prose around them, not the images, so any value
    that appears only in a figure is unverified. That includes the βCD and
    βSNR marks in Fig. 4 and the Fig. 3 insets. No skim dossier existed for
    this work. I started from the Anthology's entry ANTH-LIT-641 and its
    theory ANTH-THEORY-097, and I checked both against the text. I
    recomputed the paper's exact circle-intersection formula (Eq. 2) and its
    β regression (Eq. 10) myself for n = 64 and n = 1000. Where those
    numbers are mine, the note says so.); the first NOTE on it, since it was
    seeded from the abstract alone. Status set from the reading: Active.
tags:
- neuroscience
- mathematics
- information-retrieval
- representation-learning
date: '2026-09-27'
published: '2021-11-10'
arxiv: '2111.05498'
first_author: 'Bricken'
keywords:
- 'sparse distributed memory'
- 'attention'
- 'associative memory'
- 'cerebellum'
implementations: []
summary: >-
  Bricken & Pehlevan (2021),
  [ARXIV-2111.05498](https://arxiv.org/abs/2111.05498). Kanerva's SDM read
  weights each stored pointer by the number of neurons in the intersection
  of two Hamming balls of radius d. The paper shows that this weight is
  roughly log-linear in Hamming distance for close patterns. As a result,
  with L²-normalised vectors and a regression-fitted β, softmax attention
  reproduces SDM's retrieval behaviour on random and learnt-projection
  data (App. B.7). Two things are weaker than they look. The analytic
  derivation (App. B.2, Eqs. 16–21) gets the exponent wrong: by my
  recomputation its β is ≈2–2.5× too small. The biological case is
  Kanerva's 1988 cerebellar mapping, restated rather than re-argued. It
  also needs r = 2⁶⁴ ≈ 1.8×10¹⁹ neurons in the Attention setting, which
  the paper itself calls "biologically implausible" (App. B.5).
---

# LIT-tmpynu35: Attention Approximates Sparse Distributed Memory

Bricken & Pehlevan (2021), *NeurIPS 2021* — [ARXIV-2111.05498](https://arxiv.org/abs/2111.05498)

## Standing in the record

Held in both records under [ADR-013](../decisions.d/ADR-013.md). The anthology holds it as [ANTH-LIT-641](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-641.md),
read for what it implies about attention in practice (the QK-norm
retrodiction), with its account [ANTH-THEORY-097](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-097.md).

It is filed here at the owner's request of 2026-09-27, to be read for a
question the anthology does not ask: the mathematics and neuroscience of
associative memory. That means Kanerva's content-addressable retrieval, its
cerebellar mapping, and the SDM read as a kernel smoother. The reading sets
it against the record's retrieval-geometry and kernel threads ([LIT-262](LIT-262.md),
[THEORY-004](../theory.d/THEORY-004.md), [THEORY-008](../theory.d/THEORY-008.md)).

It was filed `Deferred`, unread. [NOTE-tmpk6gen](../notes.d/NOTE-tmpk6gen.md) is the close reading of 2026-09-27, and it placed the work: **Active** — worth reading as the clearest statement of the SDM–attention correspondence. Its exact circle-intersection formula and its eight-algorithm convergence comparison are the parts to take away. Treat its analytic exponential derivation, its GPT-2 "confirmation" and its cerebellar implementation of attention as argument, not demonstration.
