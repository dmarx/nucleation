---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp571ty](../notes.d/NOTE-tmp571ty.md)); worth reading as a short, correct proof that permutation symmetry constrains how neurons can move under training: if the update rule is permutation-equivariant (gradient descent, SGD or Adam on a permutation-symmetric loss), neurons that coincide stay coincident at every step size, and if the update map is K-Lipschitz each step moves every pair of neurons apart or together by at most a factor 1 ± ηK. So below η = 1/K the induced map on the set of neuron vectors is a bi-Lipschitz homeomorphism (a C¹ diffeomorphism under a smoothness condition) and distinct neurons cannot merge in finitely many steps; above it only a continuous surjection is guaranteed. The proofs are a few lines and hold. What they do not carry is the paper''s larger picture: for finitely many neurons a homeomorphism of the neuron set is only a bijection, "topological simplification" above 1/K is permitted, not shown, and the experiments measure Betti numbers of point clouds at a fixed scale, which the theorem does not protect. The large-step runs show the clouds fragmenting (more components), not merging, and in the Adam runs the step size times the measured top Hessian eigenvalue stays below 0.05 where the topology changes.'
title: 'Topological Invariance and Breakdown in Learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 and read the same day
    (NOTE-tmp571ty) from the arXiv PDF of v1 (3 October 2025, 22 pp.):
    main text, Appendices A–D, every proof followed; figures read from
    the rendered pages (Figures 3, 5, 11 and 12 looked at, the rest from
    their captions). Identified from the arXiv abstract page: authors
    Yongyi Yang (Michigan, NTT Research), Tomaso Poggio and Isaac Chuang
    (MIT) and Liu Ziyin (MIT, NTT Research); v1 submitted 3 October
    2025, the only version listed on 2026-10-09; subject cs.LG; no
    journal reference or comment. `published:` is that date (ADR-002).
    A Crossref bibliographic query for the title found no published
    version. Not held in nucleation before this filing (grep of record/
    for the arXiv id, the title and the first author found nothing). Not
    held in the Anthology of the SOTA as far as its clone shows: a grep
    of its record/ (clone at commit d8b5ba5, 9 October 2026, possibly
    stale) for the arXiv id, the title, "topological critical" and the
    first author found nothing, and nothing by Ziyin. It holds the
    edge-of-stability paper this one leans on (ANTH-LIT-461) and the NTK
    paper (ANTH-LIT-360); its `training-optimization` topic (training
    dynamics, learning rates) could hold this one, hence
    `anthology-candidate`.
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-10-09'
published: '2025-10-03'
arxiv: '2510.02670'
first_author: 'Yang'
keywords:
- 'permutation symmetry'
- 'permutation equivariance'
- 'learning dynamics'
- 'learning rate'
- 'topological critical point'
- 'bi-Lipschitz map'
- 'homeomorphism'
- 'edge of stability'
- 'Betti numbers'
- 'neuron merging'
implementations: []
summary: >-
  Yang, Poggio, Chuang and Ziyin (2025), [ARXIV-2510.02670](https://arxiv.org/abs/2510.02670). For any
  permutation-equivariant update rule whose map is K-Lipschitz, one step
  of size η changes the distance between any two neurons by a factor in
  [1 − ηK, 1 + ηK], and coincident neurons stay coincident. Below
  η* = 1/K the induced map on the set of neuron vectors is therefore a
  homeomorphism, measure-preserving for the pushed-forward neuron
  distribution and a C¹ diffeomorphism under a smoothness condition;
  above it only a continuous surjection is guaranteed. The paper reads
  this, with the edge of stability, as two phases of training, the second
  a topological simplification; the proofs hold, but that reading and the
  Betti-number experiments go beyond them.
---

<!-- inactive-ok-file: THEORY-tmpmh1ao — Proposed; the THEORY this reading produced -->
<!-- inactive-ok-file: THEORY-039 — Proposed; the record's account of later training phases, which this paper's two-phase picture bears on -->
<!-- inactive-ok-file: LIT-370 — Proposed; the two-phase paper this one cites as its empirical source, named for the lineage -->

# LIT-tmpacvdl: Topological Invariance and Breakdown in Learning

Yongyi Yang, Tomaso Poggio, Isaac Chuang and Liu Ziyin (2025), arXiv preprint
— [ARXIV-2510.02670](https://arxiv.org/abs/2510.02670)

## Key takeaways

- **Equivariance alone forbids splitting.** If the update commutes with
  permuting neurons, two neurons with identical weights receive identical
  updates, so they stay identical at every step size (Lemma 1). For gradient
  descent this follows from the loss being permutation-symmetric
  (Proposition 1); for Adam the optimizer's moment estimates are carried as
  part of each neuron, and equivariance still holds (Proposition 3).
- **A step moves pairs of neurons by a bounded factor.** If the whole update
  map is K-Lipschitz, then for every pair
  (1 − ηK)‖xᵢ − xⱼ‖ ≤ ‖xᵢ′ − xⱼ′‖ ≤ (1 + ηK)‖xᵢ − xⱼ‖ (Lemma 2). The proof
  swaps the two neurons and applies the Lipschitz bound to the swap. So for
  ηK < 1 the map from the neuron set at step t to the set at t + 1 is a
  bi-Lipschitz homeomorphism (Theorem 1), and it carries the neuron
  distribution to the next one (Theorem 2). Under a further smoothness
  condition it is a C¹ diffeomorphism. For ηK ≥ 1 it is still a continuous
  surjection, and a quotient map when the set is compact.
- **1/K is a sufficient threshold, not an observed transition.** Below it no
  two distinct neurons can coincide after finitely many steps. Above it the
  theorem permits merging and does not show it happens. For gradient descent
  with an L-smooth loss, 1/K is the step size that minimises the descent-lemma
  bound, half the classical stability limit 2/K.
- **What the theorem covers in a real network is narrow.** With finitely many
  neurons, a homeomorphism of the neuron set is just a bijection, so
  "topology is preserved" means "no two neurons merge". Genus, loops and
  Betti numbers of the point cloud are scale-dependent, and the theorem does
  not protect them: the distortion bounds compound over steps. Merging in
  the limit of infinitely many steps is not excluded at any step size. The
  global Lipschitz constant K does not exist for the paper's own sigmoid
  networks. For Adam the paper proves equivariance but no continuity
  constant.
- **The experiments do not test the theorem.** In two- and three-dimensional
  toy networks, a figure-eight or genus-2 cloud of neurons keeps its shape at
  a small step size and is torn apart at a larger one. For a two-layer MNIST
  MLP the Betti numbers of the neuron cloud, at a scale of a quarter of its
  diameter, stay fixed at a small step size and change at a large one. The
  change is fragmentation: b₀ rises from 1 to about 6 (GD) or past 50 (Adam). The
  theory describes merging, and in the continuum a continuous map cannot add
  components. In the Adam runs, the step size times the measured top Hessian
  eigenvalue stays below 0.05, far below 1, when the topology changes.

## Standing in the record

Filed on 2026-10-09 at the owner's request, with no stated context. It was
filed right after the five papers on the theory of trained networks
([LIT-855](LIT-855.md) to [LIT-859](LIT-859.md), curation entry of that day) and together with
arXiv 2602.15029. Read on its own merits.

Read on 2026-10-09 ([NOTE-tmp571ty](../notes.d/NOTE-tmp571ty.md)). The reading is the source of
[THEORY-tmpmh1ao](../theory.d/THEORY-tmpmh1ao.md), which states the proved result at its true scope. The
record's account of later training phases, [THEORY-039](../theory.d/THEORY-039.md), does not change: the
paper adds a sixth two-phase picture, measured in yet another quantity. The
empirical two-phase paper it cites, by an overlapping author group, is
[LIT-370](LIT-370.md). The anthology holds the edge-of-stability paper it leans on,
[ANTH-LIT-461](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-461.md).
