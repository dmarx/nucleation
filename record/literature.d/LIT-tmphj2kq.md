---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpc1el0](../notes.d/NOTE-tmpc1el0.md)); worth reading as the sparse extension of the Random Hierarchy Model ([LIT-877](LIT-877.md)) and as a model-based account of why a network''s insensitivity to small smooth deformations of its input tracks its test error. Each informative feature of the RHM is padded with s0 uninformative "empty" positions and may sit anywhere in its sub-patch, so the data become very sparse (s^L informative positions among (s(s0 + 1))^L) and the label is unchanged by discrete displacements of the informative features, a stand-in for diffeomorphisms of an image. On this Sparse Random Hierarchy Model, deep locally connected and convolutional networks learn from a number of examples polynomial in the input dimension: measured, P* ≈ s^(L/2)(s0 + 1)^L n_c m^L without weight sharing and P* ≈ C(s0 + 1)^2 n_c m^L with it. At about that training-set size the hidden layers become insensitive both to swapping synonymous tuples and to displacing features, so the two invariances and good performance arrive together; the paper offers this as the explanation of the correlation between deformation stability and test error measured on CIFAR-10. The laws are fitted, the (s0 + 1)^L factor has a one-step-gradient argument for locally connected networks, the CNN''s (s0 + 1)^2 is unexplained, and the image case is an analogy: no synonym sensitivity was measured on images.'
title: 'How Deep Networks Learn Sparse and Hierarchical Data: the Sparse Random Hierarchy Model'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09, as one of the works cited by
    the hierarchy and hyperbolic-geometry batch (nucleation#113, LIT-865 to
    LIT-877) that neither record held; LIT-877 (Cagnetta et al., the Random
    Hierarchy Model) names it among the same group's follow-ups. Read in
    full the same day (NOTE-tmpc1el0) from the PMLR PDF
    (proceedings.mlr.press/v235/tomasini24a, 21 pp. with appendices), text
    extracted with pdftotext; the arXiv v2 PDF (2 May 2024, 21 pp.) was
    compared with it and differs in typesetting only. Checked against the
    arXiv abstract page (arXiv:2404.10727: v1 submitted 16 April 2024, v2
    2 May 2024; authors Umberto M. Tomasini and Matthieu Wyart; "9 pages,
    6 figures"; no journal reference given) and against the PMLR v235
    index and abstract page: Proceedings of the 41st International
    Conference on Machine Learning (ICML 2024, Vienna), PMLR 235:48369–48389,
    same title, authors Umberto Maria Tomasini and Matthieu Wyart,
    citation_publication_date 8 July 2024. PMLR assigns no DOI, and a
    Crossref bibliographic query for the title found no record of it.
    `published:` is the arXiv v1 date, 16 April 2024, the earliest any
    source gives (ADR-002); the PMLR date is the alternative. Not held in
    nucleation before this filing: a grep of record/ for the identifier,
    the title and "Tomasini" found only the mentions in LIT-877, THEORY-195
    and the batch's curation entry. Not held in the Anthology of the SOTA
    as far as its clone shows: a grep of its record/ (clone at commit
    d8b5ba5, 9 October 2026, possibly stale) for the identifier, the title,
    "Sparse Random Hierarchy", "Tomasini", "Wyart", "Petrini", "Cagnetta"
    and "random hierarchy" found nothing ("diffeomorphism" matches only
    the local learning coefficient's invariance, an unrelated sense). The
    anthology's `signal-structure` topic (what the data is like that
    methods exploit) could hold it, hence `anthology-candidate`. The
    architectures' code (github.com/leonardopetrini/diffeo-sota) was not
    inspected.
tags:
- learning-theory
- compositionality
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2024-04-16'
arxiv: '2404.10727'
first_author: 'Tomasini'
keywords:
- 'sparse random hierarchy model'
- 'random hierarchy model'
- 'sparsity'
- 'stability to diffeomorphisms'
- 'synonymic invariance'
- 'sample complexity'
- 'curse of dimensionality'
- 'weight sharing'
- 'locally connected networks'
implementations: []
summary: >-
  Tomasini and Wyart (2024; ICML 2024, PMLR 235). Pads each informative
  feature of the Random Hierarchy Model with uninformative positions, so
  the label is unchanged by discrete displacements of features, a stand-in
  for smooth deformations. Deep networks learn this sparse model from a
  number of examples polynomial in the input dimension, measured as
  (s0 + 1)^L n_c m^L (times s^(L/2)) without weight sharing and
  (s0 + 1)^2 n_c m^L with it, and become insensitive to synonym swaps and
  to feature displacements at the same training-set size as they learn the
  task, which the paper offers as the reason deformation stability tracks
  test error. Fitted laws; the image case is by analogy.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-195 THEORY-186 THEORY-tmpvxccc — Proposed or open; cited as the question this filing answers to, the account it extends and what this reading produced -->

# LIT-tmphj2kq: How Deep Networks Learn Sparse and Hierarchical Data: the Sparse Random Hierarchy Model

Umberto M. Tomasini and Matthieu Wyart (2024), *Proceedings of the 41st
International Conference on Machine Learning*, PMLR 235:48369–48389 —
[ARXIV-2404.10727](https://arxiv.org/abs/2404.10727)

## Key takeaways

- **The model.** The Random Hierarchy Model of [LIT-877](LIT-877.md) (n_c classes, L
  levels of v symbols, each symbol rewriting to m synonymous s-tuples)
  with an uninformative symbol 0 added at every level. In sparsity A, each
  of the s informative children sits in its own sub-patch of s0 + 1
  positions with exactly s0 empties, at a position chosen independently;
  in sparsity B, the s children may sit anywhere in the s(s0 + 1) patch
  in their order. An empty symbol rewrites to an all-empty patch. An input
  has d = (s(s0 + 1))^L positions of which s^L are informative, one-hot
  over v, and the label is unchanged when informative features move within
  their allowed positions: a discrete deformation.
- **Polynomial sample complexity, with sparsity costing differently by
  architecture.** At maximal m = v^(s−1), n_c = v, depth-L networks with
  filter size and stride s(s0 + 1) matched to the tree reach 10% test
  error at P*_LCN ≈ s^(L/2)(s0 + 1)^L n_c m^L without weight sharing
  (Eq. 3, Figs. 4B, 10) and P*_CNN ≈ C(s0 + 1)^2 n_c m^L with it (Eq. 4,
  Figs. 4C, 13). Both are exponential in L, so polynomial in d. Sparsity B
  gives the same collapses (Figs. 7, 8). At fixed d, sparser data
  are easier for the locally connected network, P*_LCN ∝
  F^(log m/log s − 1/2) d^(log m/log s + 1/2) with F = (s0 + 1)^(−L) the
  informative fraction, when m > √s (Eq. 5, Fig. 5).
- **Two invariances learned at once, and with the task.** The second
  layer's sensitivity to swapping synonymous tuples (S_2, Eq. 6) and to
  displacing features within their patches (D_2, Eq. 7) fall below fixed
  thresholds at training-set sizes P*_S and P*_D that match P* across L,
  v, s and s0 (Figs. 6, 11, 14), for LCNs, CNNs and fully connected
  networks (Fig. 16). Invariance to level-l transformations appears from
  layer l + 1 on, all levels at the same P (Figs. 12, 15). The thresholds
  for S_2 and D_2 were tuned per setting (between 10% and 50%) by looking at
  the curves.
- **The correlation of deformation stability with error, reproduced.**
  VGG, ResNet and EfficientNet networks and the matched LCN and CNN,
  trained on one SRHM instance (L = s = s0 = 2, n_c = m = 10, P = 7400) show test
  error rising with the output's sensitivity to deformations and to
  synonym swaps, as Petrini et al. found for deformations on CIFAR-10
  (Figs. 1, 9, 17).
- **The argument.** In a locally connected network each first-layer weight
  sees one input position, which is informative in a fraction
  (s0 + 1)^(−L) of the data. The first gradient step from a symmetric
  initialisation is then the non-sparse RHM's step with P(s0 + 1)^(−L)
  examples (Appendix C, Eq. 12), so the correlation threshold n_c m^L of
  [LIT-877](LIT-877.md) is multiplied by (s0 + 1)^L. Since all displaced and all
  synonymous versions of one parent carry the same class statistics, the
  grouping that gives synonym invariance gives displacement invariance
  too. The s^(L/2) prefactor and the CNN's (s0 + 1)^2 are not derived.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works cited by
the batch on hierarchy and hyperbolic geometry (nucleation#113, [LIT-865](LIT-865.md) to
[LIT-877](LIT-877.md)) that neither record held. [LIT-877](LIT-877.md), which introduces the Random
Hierarchy Model, names it as one of the same group's later papers built on
that model. Read on its own merits ([NOTE-tmpc1el0](../notes.d/NOTE-tmpc1el0.md)); the reading produces
[THEORY-tmpvxccc](../theory.d/THEORY-tmpvxccc.md), which extends [THEORY-195](../theory.d/THEORY-195.md) to sparse data.

It does not bear on [QUESTION-025](../questions.d/QUESTION-025.md) beyond what [LIT-877](LIT-877.md) already does. Its
hierarchy is the same part–whole constituency, and what it adds is a
second kind of nuisance, position, beside the first, synonymy; it measures
no co-occurrence matrix, embedding direction or attribute. What it adds to
the record is a candidate account of why a learned representation is
insensitive to small deformations: not because the architecture was built
for it, but because displaced and synonymous versions of a part carry the
same statistics with respect to the label and are grouped together by the
same learning step. The record's other holding on deformation stability is
the geometric-deep-learning blueprint ([LIT-319](LIT-319.md), §3.3), which imposes it as
a prior rather than measuring when it is learned.
