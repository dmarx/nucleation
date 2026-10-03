---
number: 112
status: Proposed
formerly:
- THEORY-tmpkd2ju
promote_when: >-
  The residual barrier after full-group alignment accounted for at a scale
  the sources do not reach. The zero barriers so far are for MNIST MLPs, a
  32×-wide ResNet-20 on CIFAR-10, and small ViTs and GPT-2s whose alignment
  was learned against the loss at the midpoint. ImageNet ResNet-50 keeps a
  third of its barrier, and BookCorpus keeps 0.42. What would promote:
  independently trained models at standard width, on ImageNet or a language
  corpus, brought to near-zero held-out barrier by a data-free alignment
  over the architecture's full symmetry group. Or the residual barrier shown
  to track a difference in what the endpoints compute, as LIT-669's
  barriers do, so that "most" is the part that is symmetry and the rest is
  identified. What would refute it: same-data, same-procedure solutions
  whose barrier stays near the unaligned value under every alignment the
  full group allows, learned ones included, when the endpoints are shown to
  rely on the same input attributes. A third or fourth permutation-finding
  algorithm on vision models at moderate scale cannot settle it.
title: 'Once the architecture''s symmetries are factored out, most of the linear barrier between independently trained solutions disappears; the group that matters is the full one, permutations for MLPs and CNNs but for transformers also an orthogonal map on the residual stream, without which a barrier remains; and the barrier left after alignment falls with width and rises with depth'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
source:
- LIT-652
- LIT-661
- LIT-680
- LIT-664
- LIT-655
extends:
- THEORY-109
summary: >-
  Entezari et al. (2022), [LIT-652](../literature.d/LIT-652.md), conjectured that SGD solutions are
  one basin modulo permutation. Git Re-Basin (2023), [LIT-661](../literature.d/LIT-661.md), aligned
  MNIST MLPs and 32×-wide ResNet-20s to zero barrier, but not 1×-width
  models or ImageNet ResNet-50. Ferbach et al. (2024), [LIT-680](../literature.d/LIT-680.md), proved
  it for wide nets with independent neurons, with a width requirement
  exponential in the previous layer's width. Theus et al. (2025),
  [LIT-664](../literature.d/LIT-664.md), took transformers to zero only with an orthogonal map on
  the residual stream added; permutations alone left 0.29–1.60. Bo Zhao et
  al. (2025), [LIT-655](../literature.d/LIT-655.md), place permutations inside the full symmetry
  group. Lubana et al.'s barriers between models that compute differently
  are the boundary.
extended_by:
- THEORY-110
---
<!-- inactive-ok-file: THEORY-109 THEORY-114 THEORY-110 — Proposed; the account this extends and the two filed with it, named in the body -->

# THEORY-112: Once the architecture's symmetries are factored out, most of the linear barrier between independently trained solutions disappears; the group that matters is the full one, permutations for MLPs and CNNs but for transformers also an orthogonal map on the residual stream, without which a barrier remains; and the barrier left after alignment falls with width and rises with depth

## Source

- Entezari, Sedghi, Saukh & Neyshabur (2022), [LIT-652](../literature.d/LIT-652.md), read in
  [NOTE-537](../notes.d/NOTE-537.md): Conjecture 1, Theorem 3.1, §2 (Figs. 2–3) and §4.
- Ainsworth, Hayase & Srinivasa (2023), Git Re-Basin, [LIT-661](../literature.d/LIT-661.md), read in
  [NOTE-532](../notes.d/NOTE-532.md): §§3, 5.1, 5.3, Figs. 2 and 4, and Appendix A.6.
- Ferbach, Goujaud, Gidel & Dieuleveut (2024), [LIT-680](../literature.d/LIT-680.md), read in
  [NOTE-543](../notes.d/NOTE-543.md): Theorems 3.1 and 5.2–5.4, Lemma B.3 and §6.
- Theus, Cabodi, Anagnostidis, Orvieto, Singh & Boeva (2025), [LIT-664](../literature.d/LIT-664.md),
  read in [NOTE-540](../notes.d/NOTE-540.md): §§3–4, Table 2, Figs. 5 and 7.
- Bo Zhao, Dehmamy, Walters & Yu (2025), [LIT-655](../literature.d/LIT-655.md), read in
  [NOTE-528](../notes.d/NOTE-528.md): Propositions 4.1, 5.2–5.4 and §5.2.

## The claim, assembled

**The conjecture.** Entezari et al., [LIT-652](../literature.d/LIT-652.md), conjecture that for wide
enough networks most SGD solutions can each be permuted so that the
straight line between any two has about zero barrier: one basin, seen
through different labellings of the hidden units (Conjecture 1). Their own
evidence is indirect. Across width, depth, architecture and dataset, in
more than 3,000 networks, barriers between independent solutions look like
barriers between random permutations of one solution. Their
simulated-annealing search lowered barriers only for shallow networks on
easy data, and did nothing for VGG or ResNet (§4).

**Removing the permutation removes the barrier, where the network is wide.**
Git Re-Basin, [LIT-661](../literature.d/LIT-661.md), aligns one network's units to another's by
weight matching. That is coordinate descent over per-layer assignment
problems, it needs no data, and it runs in seconds. After alignment, MNIST
MLPs show zero barrier, and so do ResNet-20s on CIFAR-10 at 32× width. That
was the first zero-barrier connection between independently trained
ResNets (Figs. 2 and 4). The authors' conclusion is that permutations are
"a necessary piece, though not a complete picture" (§5.3). Ferbach et al.,
[LIT-680](../literature.d/LIT-680.md), prove the conjecture beyond Entezari et al.'s random
one-hidden-layer case. Aligning a layer's neurons is optimal transport
between the empirical distributions of their weights (Lemma B.3). So when
neurons are independent draws, Wasserstein convergence bounds how wide a
layer must be for the permuted line to stay low-loss. That gives
connectivity for wide two-layer networks trained by mean-field SGD
(Theorem 3.1) and for deep networks with i.i.d. neuron weights
(Theorem 5.2).

**The group is the architecture's full one.** Permutations are the
symmetries of an elementwise nonlinearity. Bo Zhao et al., [LIT-655](../literature.d/LIT-655.md),
place them inside a larger group. For a full-rank linear network the
minimum is homeomorphic to GL_h(ℝ)^{l−1} and has 2^{l−1} components
(Proposition 4.1). A permutation with negative determinant joins
components that continuous symmetries cannot, so for h ≥ 2 permutations
connect them all (Proposition 5.2). Theus et al., [LIT-664](../literature.d/LIT-664.md), carry this
to transformers. Feed-forward units take permutations. Attention heads take
a semi-permutation. The residual stream, once LayerNorm is rewritten as
RMSNorm, takes one orthogonal map. Their test-loss barriers (Table 2) are
1.69–4.34 with no alignment. Learned matching restricted to permutations
leaves 0.29–1.60, which already removes 63–90% of the vanilla barrier. The
full group brings it to 0.00 on CIFAR-10, CIFAR-100 and Tiny ImageNet, 0.02
on Tiny Shakespeare and 0.42 on BookCorpus. The data-free version leaves
0.34–1.56. What permutations leave is in the rotation: learned matching
keeps weight matching's permutations and corrects the orthogonal map
(Fig. 5), and iterating orthogonal matching keeps lowering the barrier
while iterating permutation matching does not (Fig. 7). On a transformer,
then, permutations alone already remove most of the barrier, and the
orthogonal map on the residual stream is what removes the rest. This is
narrower than "most of a transformer's barrier is a rotation", which Table
2 does not show.

**Width and depth.** This clause was filed as a candidate theory of its
own and is folded in here, because it is a statement about how much
alignment can remove. Stated on its own, "width lowers barriers and depth
raises them", it is false for curved paths. Draxler et al., [LIT-653](../literature.d/LIT-653.md),
find barriers on their minimum-energy paths falling as networks get "wider
and especially deeper" (Fig. 5). Garipov et al., [LIT-673](../literature.d/LIT-673.md), also find
width easing curved connection (A.7). On straight lines after alignment
the clause holds:

- *Width lowers it.* Git Re-Basin's barrier after weight matching falls with
  width for VGG-16 and ResNet-20 on CIFAR-10, to zero at large width; at 1×
  neither is linearly connected (Fig. 4). Ferbach et al.'s bounds are bounds
  on width. Before any alignment, Entezari et al.'s barrier first rises with
  width, peaking near the width that just fits the training data, then
  falls (Fig. 2). For VGG and ResNet it stays saturated high at every width
  they tried.
- *Depth raises it.* With width fixed, adding layers raises the unaligned
  barrier quickly for MLPs and shallow CNNs. VGG(11–19) and ResNet(18–50)
  saturate high, and depth, not width, is what the authors blame
  (Entezari et al., Fig. 3). The examples they give of zero barrier after
  their search are MNIST MLPs of depth 1 at every width and of depths 2 and
  4 at width 2¹⁰ (Fig. 7), which is suggestive and no more. In Ferbach et al. the width that layer ℓ needs is
  Õ((T_ℓ/ε)^{m̃_{ℓ−1}}), exponential in the width before it, so the
  requirement compounds with depth. Their lower bound shows this rate is
  tight for independent neurons (Theorem 5.3). It falls if weights
  concentrate near a low-dimensional subspace (Theorem 5.4).

## Where it stops

- **Thin models and ImageNet.** At 1× width neither VGG-16 nor ResNet-20 is
  linearly connected after weight matching, and on ImageNet ResNet-50 the
  barrier falls by 67% but not to zero (Git Re-Basin, §§5.1, 5.3). The
  authors cannot rule out a better permutation.
- **Barriers that are disagreement.** Lubana et al., [LIT-669](../literature.d/LIT-669.md), train
  models that do and do not rely on a synthetic cue. They are joined by
  quadratic paths but keep a linear barrier after activation-matching
  permutation, because they compute different things. For a one-hidden-layer
  ReLU network they prove that linear connectivity forces shared activation
  patterns. Their endpoints are trained on different data, so they are not
  the same-data seeds this account is about. But they show that a barrier
  surviving alignment can be real, which is why the claim says "most".
- **Solutions training reaches.** Git Re-Basin constructs two perfect
  solutions of a two-hidden-layer, two-unit network that no permutation
  connects (Appendix A.6). Bo Zhao et al. use rescaling to construct minima
  in one component whose straight-line barrier is unbounded, even under a
  last-layer permutation (Propositions 5.3–5.4). Neither is a minimum SGD is
  shown to find, and both papers say so. As in [THEORY-109](THEORY-109.md), the claim
  is about found solutions.
- **Learned alignment optimises what it reports.** Theus et al.'s zero
  barriers come from alignment trained against the loss at the path's
  midpoint, on training data, and measured on test data. A zero from
  data-free alignment would be stronger evidence of a pre-existing shared
  basin.
- **Small models.** The transformers are 6- to 8-layer ViTs at 44–84%
  accuracy and 6-layer GPT-2s.

## What this does not say

- **It does not say permutation is the whole story anywhere.** For
  transformers the orthogonal map is needed to reach zero. For thin
  convnets nothing found reaches zero.
- **It does not say a barrier is always symmetry.** Lubana et al.'s barriers
  are mechanism. The claim is about same-data solutions, and only "most".
- **It does not say alignment works at initialization.** That is
  [THEORY-114](THEORY-114.md): at practical widths the aligned barrier is high at the
  start of training and falls during it.

## Connections

- **[THEORY-109](THEORY-109.md).** This account extends it. That account says the
  solutions training finds lie in one connected set joined by curves. This
  one says that, once symmetry is factored out, the set is nearly convex:
  the curve straightens. Git Re-Basin reads the pair the same way, crediting
  Benton et al. ([LIT-656](../literature.d/LIT-656.md)) with the connected volume and Entezari et al.
  with conjecturing it convex modulo permutation.
- **[THEORY-110](THEORY-110.md)** keeps the quotient by symmetry and weakens convex to
  star-shaped, which reaches below the widths at which this account holds.
- **[THEORY-114](THEORY-114.md)** is its time axis.
- **Across the boundary.** The anthology's [ANTH-THEORY-010](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-010.md) holds that most
  of the barrier between two independently trained networks is permutation,
  not disagreement. It is Proposed there and names "the account
  demonstrated on a transformer" as one condition for promotion. This
  account agrees with it for MLPs and CNNs. For transformers, Theus et al.
  bear it out in its letter, since permutations alone remove 63–90% of the
  barrier. They also show that reaching zero needs a symmetry that is not a
  permutation. Lubana et al.'s mechanism barriers name the case its account
  leaves out. This is for the coordinator to report there; the anthology is
  not edited from here.
