---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp8r19k](../notes.d/NOTE-tmp8r19k.md)); worth reading here as the paper that uses the Marchenko–Pastur law as a null model for where a trained weight matrix holds information, and so notices what a magnitude-ordered reading misses: a rectangular matrix''s null spectrum has a lower edge above zero, so learning can push singular values below the bulk as well as above it. In three transformers the departures line up with activation-covariance directions, at the lower end in the MLP up and gate projections, and zeroing the smallest decile of a rectangular matrix can cost more than zeroing most larger deciles; in square matrices it never does. A two-layer linear teacher–student ensemble produces such a lower outlier when the loss suppresses the noise along a learned direction. The evidence is measured, not proved, and it is uneven: overlap and ablation importance disagree for several matrix types, and the decile ablation does not isolate the outliers it is meant to test.'
title: 'Small Singular Values Matter: A Random Matrix Analysis of Transformer Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmp8r19k) from the arXiv PDF of v3
    (6 November 2025, 29 pages, the NeurIPS 2025 camera-ready): main text,
    every appendix (A–J) and all tables; the figures read from their
    captions and text, since their plots do not survive text extraction.
    Details checked against the arXiv abstract page: title, the three
    authors (Max Staats, Matthias Thamm, Bernd Rosenow, Leipzig), v1
    submitted 23 October 2024, v2 13 February 2025, v3 6 November 2025;
    the v3 footer says NeurIPS 2025. v1 was titled "Locating Information
    in Large Language Models via Random Matrix Theory"; the title here is
    v2's and v3's. `published:` is the v1 date. Held in the Anthology of
    the SOTA as ANTH-LIT-517 (clone of 2026-10-09, commit d8b5ba5), read
    there (ANTH-NOTE-263) for what the bottom of the spectrum means for
    low-rank-plus-quantization practice; filed here as well under ADR-013
    for this record's question. Not previously held in nucleation (checked
    by arXiv id, title and first author).
tags:
- representation-learning
- mathematics
date: '2026-10-09'
published: '2024-10-23'
arxiv: '2410.17770'
first_author: 'Staats'
keywords:
- 'random matrix theory'
- 'Marchenko-Pastur'
- 'singular value spectra'
- 'weight matrices'
- 'activation covariance'
- 'SVD-based pruning'
- 'teacher-student model'
implementations: []
summary: >-
  Staats, Thamm & Rosenow (2024; NeurIPS 2025). Taking the
  Marchenko–Pastur law as the zero-information null for a weight matrix,
  trained transformer matrices (BERT, Pythia-410M, Llama-3.1-8B) show
  outliers above the bulk and, in rectangular matrices only, below it,
  since only there does the null spectrum have a positive lower edge.
  In the MLP projections the singular vectors of both kinds of outlier
  align with activation-covariance eigenvectors, and zeroing the
  smallest decile of a rectangular matrix can hurt more than zeroing
  most larger ones. A linear teacher–student ensemble yields a
  below-bulk outlier when the noise is suppressed along a learned
  direction.
---
<!-- inactive-ok-file: LIT-369 — Proposed; named as a neighbour in the random-matrix reading of trained weights, not leaned on -->
<!-- inactive-ok-file: THEORY-078 — Proposed; named for the bulk-plus-outliers picture this paper extends to the lower edge, not as settled -->

# LIT-tmp55jc0: Small Singular Values Matter: A Random Matrix Analysis of Transformer Models

Max Staats, Matthias Thamm and Bernd Rosenow (2024), *NeurIPS 2025* —
[ARXIV-2410.17770](https://arxiv.org/abs/2410.17770)

## Key takeaways

- **The null and its two edges** (Section 3). For an m × n matrix with
  i.i.d. zero-mean entries and q = n/m fixed, the singular values follow
  the Marchenko–Pastur law on [ν₋, ν₊], ν± = σ̃(1 ± √(1/q)). Freshly
  initialized transformer matrices match it closely. A square matrix has
  ν₋ = 0, so learning can only push values out above the bulk; a
  rectangular one has ν₋ > 0, so it can push them out below as well. The
  paper reads agreement with the law as randomness and departures as
  learning.
- **Departures carry data directions, in some matrices** (Section 4,
  Appendices A–C). The overlap O_k of each right singular vector with the
  eigenvectors of the covariance of the activations entering the matrix
  (WikiText; BookCorpus in Appendix B) rises above a random-vector 3σ
  band for the above-bulk outliers generally, and for the below-bulk
  outliers of the Up-Projection (Pythia, Llama) and Gate-Projection
  (Llama). It does not for the Attention-Output matrix in any of the three
  models, nor for Llama's Down-Projection, nor for the below-bulk outliers
  of Llama's rectangular Key and Value.
- **The ablation** (Section 5, Tables 1, 2 and 5). Zeroing one decile of
  rank-ordered singular values in every matrix of one type: in square
  matrices the damage falls monotonically from the largest decile down; in
  rectangular ones the smallest decile is always worse than some larger
  ones. Llama-3 8B on GSM8K (43.2%): the smallest decile of the
  Down-Projection leaves 2.0%, worse than every decile but the largest;
  the same decile of the square Attention-Output leaves 40.0%.
- **Order of operations** (Figure 6, BERT on BoolQ, RTE, SST-2). Pruning
  the smallest decile and then fine-tuning mostly recovers; fine-tuning
  and then pruning does not. The authors use this to reconcile Hsu et al.
  (small values matter) with Sharma et al. (removing them helps).
- **A solvable mechanism** (Section 6, Appendix F). A Gaussian Gibbs
  ensemble over the first-layer weights W of a two-layer linear student
  learning a rank-one linear teacher has mean W₀ ∝ v uᵀ and row covariance
  Σ = α𝟙 − α²β/(1 + αβ) vvᵀ: the loss suppresses the noise along the
  second-layer direction v. That negative spike in the noise lets the
  teacher's singular value sit below the bulk, and the student's singular
  vectors overlap the teacher's more the farther the outlier sits below
  the bulk, falling to chance where it merges.

## Standing in the record

Filed on 2026-10-09 at the owner's request, with no context stated; it came
in a batch with arXiv 2509.24914, 2502.09863, 2504.12916 and 2205.10343. It
is read here on its own merits. See the curation entry of that day.

It is also held in the Anthology of the SOTA as [ANTH-LIT-517](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-517.md), read there
([ANTH-NOTE-263](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-263.md)) for what the bottom of the spectrum implies for
low-rank-plus-quantization methods and for its account of steep weight
spectra. The second question here, per [ADR-013](../decisions.d/ADR-013.md), is the reading on this
record's terms: what the paper shows about using a random-matrix null to
locate information in a learned matrix, and how far that inference holds.
Its point for this record is that the null spectrum, not the magnitude
order, is the reference: the Frobenius-optimal truncation of Eckart and
Young ([LIT-330](LIT-330.md)) discards by size, while this paper locates information by
distance from the bulk, at either edge ([NOTE-tmp8r19k](../notes.d/NOTE-tmp8r19k.md)). It sits in the line
of random-matrix readings of trained networks that the record holds through
Martin and Mahoney ([LIT-672](LIT-672.md)), the HTSR grokking study ([LIT-369](LIT-369.md)) and Papyan's
Hessian spectra ([LIT-617](LIT-617.md), [LIT-619](LIT-619.md)), whose bulk-plus-outliers picture
[THEORY-078](../theory.d/THEORY-078.md) states for the Fisher.
