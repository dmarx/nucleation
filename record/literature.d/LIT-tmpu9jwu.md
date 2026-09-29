---
status: Active
status_note: 'read in full 2026-09-29 ([NOTE-tmp86hqi](../notes.d/NOTE-tmp86hqi.md)); worth reading as the earliest ML paper in this batch to state that the "elementary components" of a representation are the irreps of a symmetry group and to learn them from data; read it as learning the irreducible decomposition of an assumed abelian group class from transformation pairs on raw pixels, not as detecting an unknown symmetry in a trained network, and with an experiment that is a one-group proof of concept on noise patches.'
title: 'Learning the Irreducible Representations of Commutative Lie Groups'
version: 2
history:
- version: 2
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 1402.4437 v2 (25 May 2014; the PDF
    carries "Proceedings of the 31st International Conference on Machine
    Learning, Beijing, China, 2014. JMLR: W&CP volume 32"), from the arXiv
    PDF, 9 pp.: abstract, §1 with related work §1.1, §2 (2.1 equivalence,
    invariance and reducibility; 2.2 maximal tori in SO(D)), §3 (Toroidal
    Subgroup Analysis; 3.1 invariant representation and metric; 3.2 relation
    to the DFT; 3.3 Lie subalgebra model; 3.4 maximum marginal likelihood
    learning), §4 experiments, §5 conclusions, all footnotes and the
    references. Nothing in the PDF was skipped. The text was extracted with
    PyMuPDF; Figures 1–4 survive as axis labels and captions only, so their
    content is taken from the captions and the prose. The "supplementary
    material" the text cites four times (the generalized-Bessel-function
    algorithm, the coupled-model marginal likelihood derivation, MAP
    inference) is not in the arXiv PDF and was not read. `published:` is the
    arXiv v1 date (18 Feb 2014). No anthology entry exists for this paper
    (grep of record/literature.d for the arXiv id and title: no hit). No
    nucleation entry either; the only mention is NOTE-288's second-hand
    description.); the first NOTE on it, since it was seeded from the
    abstract alone. Status set from the reading: Active.
tags:
- representation-learning
- mathematics
- probabilistic-modeling
date: '2026-09-29'
published: '2014-02-18'
arxiv: '1402.4437'
first_author: 'Cohen'
keywords:
- 'prior-art novelty map'
implementations: []
summary: >-
  Cohen & Welling (2014), arXiv:1402.4437. Proposes "Weyl's principle"
  (via Kanatani 1990) as a definition of disentangling: the elementary
  components of data are the irreducible subspaces of the representation
  of a symmetry group acting on it. It learns such a decomposition for one
  class of group fixed in advance, compact commutative subgroups of SO(D)
  ("toroidal"), from pairs (x, y) of raw data vectors related by an
  unobserved group element, y = W R(φ) Wᵀx + ε. The orthogonal basis W
  (2-D invariant subspaces) is fitted by SGD on a closed-form marginal
  likelihood, and the integer weights ω_j are then read off a batch
  rotated by a known 0.1°. The only experiment trains 100 filters on
  250,000 white-noise 16×16 patches paired with random rotations of
  themselves (learned ω from −11 to 12), and uses the invariant √κ̂ for
  1-NN on rotated MNIST, reported in a figure with no numbers. Spectral
  degeneracy plays no role.
---

# LIT-tmpu9jwu: Learning the Irreducible Representations of Commutative Lie Groups

Cohen & Welling (2014), *Proceedings of the 31st International Conference on Machine Learning (ICML 2014), Beijing, PMLR 32(2):1755–1763 (verified on the PMLR page, proceedings.mlr.press/v32/cohen14.html); arXiv v1 18 Feb 2014, v2 25 May 2014 (the version read); arXiv DOI 10.48550/arXiv.1402.4437* — arXiv:1402.4437

## Standing in the record

Filed on 2026-09-29 as a supplemental reading. The close readings of the owner's prior-art novelty map's
references found the map's citation for this point wrong, or its source unreachable, and this work is the
candidate replacement. `published:` is the first appearance ([ADR-002](../decisions.d/ADR-002.md)).

It was filed `Deferred`, unread. [NOTE-tmp86hqi](../notes.d/NOTE-tmp86hqi.md) is the close reading of 2026-09-29, and it placed the work: **Active** — worth reading as the earliest ML paper in this batch to state that the "elementary components" of a representation are the irreps of a symmetry group and to learn them from data; read it as learning the irreducible decomposition of an assumed abelian group class from transformation pairs on raw pixels, not as detecting an unknown symmetry in a trained network, and with an experiment that is a one-group proof of concept on noise patches.
