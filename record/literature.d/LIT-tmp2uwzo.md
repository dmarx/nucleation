---
status: 'Active'
status_note: 'read in full 2026-10-03 ([NOTE-tmprlsgq](../notes.d/NOTE-tmprlsgq.md)); the source of the conjecture that SGD solutions, once their hidden units are suitably permuted, have no barrier on the straight line between them: one basin modulo permutation. Its proof covers only a one-hidden-layer network at uniform random initialization, and its main evidence is indirect: barriers between independently trained networks behave like barriers between random permutations of a single trained network, across width, depth and dataset, in more than 3,000 networks. Its own permutation search lowers barriers only for shallow nets on easy data and fails for VGGs and ResNets. Second reading under [ADR-013](../decisions.d/ADR-013.md); the anthology holds it as [ANTH-LIT-251](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-251.md), and that entry misstates the theorem.'
title: 'The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Second reading under ADR-013. The Anthology of the SOTA holds this work as
    ANTH-LIT-251, read for practice (why naive weight averaging fails); this
    record reads it as the statement of the convexity-modulo-permutation
    conjecture and of the evidence for it. Read in full from the arXiv PDF of
    2110.06296 v2 (5 July 2022, the ICLR 2022 camera-ready; 27 pages), text
    extracted with PyMuPDF: §§1–5 and Appendices A–E, including the proof of
    Theorem 3.1 in Appendix D. Figures read from captions and text.
    `published:` is the v1 date, 12 October 2021.
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
published: '2021-10-12'
arxiv: '2110.06296'
first_author: 'Entezari'
keywords:
- 'permutation invariance'
- 'linear mode connectivity'
- 'loss barrier'
- 'simulated annealing'
- 'single basin conjecture'
implementations:
- 'https://github.com/rahimentezari/PermutationInvariance'
extends:
- LIT-tmp3owu9
summary: >-
  Entezari, Sedghi, Saukh & Neyshabur (2022), ICLR 2022. Conjecture: most
  SGD solutions lie in a set whose members can be permuted so that no
  barrier remains on the line between any two. Barriers between networks
  from different initializations first rise then fall with width, rise with
  depth, and saturate high for VGGs and ResNets. A proof covers a wide
  one-hidden-layer net at uniform random initialization. The evidence is a
  model: random permutations of one SGD solution show the same barriers as
  independent solutions across width, depth and dataset. A simulated
  annealing search lowers barriers only for shallow networks.
extended_by:
- LIT-tmpazv9l
- LIT-tmpd6bma
- LIT-tmpgqi24
- LIT-tmpyiw0q
---

# LIT-tmp2uwzo: The Role of Permutation Invariance in Linear Mode Connectivity of Neural Networks

Rahim Entezari, Hanie Sedghi, Olga Saukh and Behnam Neyshabur (2022),
*International Conference on Learning Representations* (ICLR 2022) —
[ARXIV-2110.06296](https://arxiv.org/abs/2110.06296)

## Key takeaways

- **The conjecture** (Conjecture 1, §3.2). For networks wide enough, there is
  a set S of solutions, containing SGD solutions with high probability, and a
  permutation for each member, such that the barrier on the straight line
  between any two permuted members is about zero. Most SGD solutions end in
  one basin once permutation invariance is taken into account.
- **Barriers, measured** (§2). With the barrier defined against the linear
  interpolation of endpoint losses (Eq. 1), barriers between networks from
  different initializations first rise then fall with width. They peak at the
  width that just fits the training data, which the authors liken to double
  descent. They grow with depth, and for VGG and ResNet families they saturate
  at a high value that width does not change (Figs. 2–4).
- **A narrow proof** (Theorem 3.1). For a one-hidden-layer ReLU network
  f(x) = vᵀσ(Ux) with h hidden units and weights drawn *uniformly at
  initialization*, there is with probability 1 − δ a permutation such that,
  for any input with ‖x‖₂ = √d, the network on the line differs from the line
  between the two networks' outputs by Õ(h^{−1/(2d+4)}). Nothing is proved
  about trained networks.
- **Evidence by model** (§4). Let S′ be all permutations of one SGD solution;
  S′ satisfies the conjecture by construction. If independent solutions S
  behave like S′, the conjecture plausibly holds. Across width, depth,
  architecture and dataset, barriers in S and S′ are "strikingly similar"
  before and after a permutation search (Figs. 1, 5, 7; over 3,000 trained
  networks).
- **The search mostly fails** (§4.2). Simulated annealing barely improves
  barriers when aligning five networks at once. Restricted to two, it finds
  zero-barrier permutations for some MLPs on MNIST and lowers barriers for
  shallow MLPs and CNNs on easy data, but does nothing for VGG and ResNet.
  It fails on S′ exactly where it fails on S, which the authors count as more
  evidence.

## Standing in the record

**Second reading under [ADR-013](../decisions.d/ADR-013.md).** The anthology holds this paper as
[ANTH-LIT-251](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-251.md) (read 2026-09-15, its [NOTE-131](../notes.d/NOTE-131.md)), for a practical question: why
averaging the weights of independently trained networks degrades them, and
that alignment must come first. This record reads it for a different
question: what the conjecture actually claims about the geometry of solution
sets, how much of it is proved, and how the evidence is built. That question
belongs with the rest of the `loss-landscapes` line ([ADR-027](../decisions.d/ADR-027.md)), where the
conjecture is tested, proved in special cases, and argued against.

**The anthology entry misstates the paper**, as this reading finds it. Per
[ADR-013](../decisions.d/ADR-013.md) the disagreement is reported here and in [NOTE-tmprlsgq](../notes.d/NOTE-tmprlsgq.md), and the
anthology entry is not edited:

- [ANTH-LIT-251](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-251.md) and its reading give the theorem as "if no neuron in either
  network is dead, there exists a permutation … [with] no loss barrier",
  with "no dead neurons" as its condition. The paper's only theorem
  (Theorem 3.1, proved in Appendix D) has no such condition. It is about a
  *one-hidden-layer* network at *uniform random initialization*, and it
  bounds an output difference at a fixed input by Õ(h^{−1/(2d+4)}), not a
  loss barrier.
- [ANTH-LIT-251](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-251.md) says that "with alignment, barriers vanish", demonstrated on
  "CIFAR-10, ResNets, VGGs". The paper's search did not reduce barriers for
  VGG or ResNet (§4.1, Appendix E.2); zero barriers were found only for some
  MLPs on MNIST.

The paper **extends** Frankle et al. ([LIT-tmp3owu9](LIT-tmp3owu9.md)). It adopts their
definition of linear mode connectivity and their framing of a basin as a
region SGD is stable in, and changes the barrier's baseline from the mean of
the endpoint losses to their linear interpolation, so that a loss changing
linearly along the path counts as no barrier (§2.1). Frankle et al. needed a
shared initialization; this paper asks whether permutations can stand in for
one.

Git Re-Basin ([LIT-tmpd6bma](LIT-tmpd6bma.md)) states this conjecture as its Conjecture 1 and
gives the first zero-barrier connection between independently trained
ResNets. Ferbach et al. ([LIT-tmpyiw0q](LIT-tmpyiw0q.md)) generalize Theorem 3.1 to deep
networks with a better width bound. The conjecture's convexity claim is also
what the star-domain papers in this batch push against, Sonthalia et al.,
"Do Deep Neural Network Solutions Form a Star Domain?" ([LIT-tmpazv9l](LIT-tmpazv9l.md)), and
Lin et al. on star-shaped and geodesic connectivity ([LIT-tmpziwl2](LIT-tmpziwl2.md)). They propose
that the solution set is star-shaped around a centre rather than convex
modulo permutation. Those readings were filed by other readers in this batch
and declare their own relations; none is declared from this side.
