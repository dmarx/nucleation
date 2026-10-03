---
number: 109
status: Proposed
formerly:
- THEORY-tmpcu710
promote_when: >-
  Evidence that the set is one set, not a set of joined pairs. Every source
  connects pairs, or at most seven modes, of image classifiers on CIFAR (and
  one recurrent model on PTB), with one curve or complex per setting and no
  seeds. What would promote: many independently trained solutions of a
  standard-width architecture, on a task beyond CIFAR, all shown joined to
  one another through low-loss paths or complexes whose worst loss is
  reported against the endpoints' with error bars. A proof that the
  training procedure itself produces dropout- or noise-stable solutions in a
  deep setting would do it from the other side, since LIT-671 then
  supplies the path. What would refute it: a pair of solutions of one
  architecture, trained on the same data by the same standard procedure,
  between which neither curve fitting nor AutoNEB, run with an adequate
  budget, finds a path whose barrier is small against the untrained loss.
  More single curves between more pairs cannot settle it, since that is the
  evidence already held.
title: 'The solutions SGD finds in a deep network lie in one connected low-loss set, joined by simple curves and spanning volumes of measurable dimension, and this is a property of the solutions training finds, not of every minimum'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
source:
- LIT-673
- LIT-653
- LIT-656
- LIT-671
summary: >-
  Garipov et al. (2018), [LIT-673](../literature.d/LIT-673.md), and Draxler et al. (2018),
  [LIT-653](../literature.d/LIT-653.md), found independently that minima of deep networks trained
  from different initializations are joined by paths of near-constant loss,
  a one-bend curve or an AutoNEB path, while the straight line between them
  climbs to near-chance error. Benton et al. (2021), [LIT-656](../literature.d/LIT-656.md), widened
  curves to simplicial complexes joining up to seven modes and a low-loss
  region of at least 10 dimensions. Kuditipudi et al. (2019), [LIT-671](../literature.d/LIT-671.md),
  proved that dropout-stable solutions are always joined, and constructed
  global minima that are not, so connectivity belongs to found solutions.
  Proposed: the evidence is pairs and small complexes of CIFAR classifiers.
extended_by:
- THEORY-110
- THEORY-112
- THEORY-114
---
<!-- inactive-ok-file: THEORY-114 THEORY-112 THEORY-110 — Proposed; the accounts filed with this one that extend it, named in the body and in Connections -->

# THEORY-109: The solutions SGD finds in a deep network lie in one connected low-loss set, joined by simple curves and spanning volumes of measurable dimension, and this is a property of the solutions training finds, not of every minimum

## Source

- Garipov, Izmailov, Podoprikhin, Vetrov & Wilson (2018), [LIT-673](../literature.d/LIT-673.md),
  read in [NOTE-527](../notes.d/NOTE-527.md): §§3–4, Table 2, Fig. 2 and supplement A.6–A.8.
- Draxler, Veschgini, Salmhofer & Hamprecht (2018), [LIT-653](../literature.d/LIT-653.md), read in
  [NOTE-531](../notes.d/NOTE-531.md): §§3–5, Fig. 5 and Appendix B.
- Benton, Maddox, Lotfi & Wilson (2021), [LIT-656](../literature.d/LIT-656.md), read in
  [NOTE-539](../notes.d/NOTE-539.md): §4 (Figs. 3–5) and Appendix A.
- Kuditipudi, Wang, Lee, Zhang, Li, Hu, Arora & Ge (2019), [LIT-671](../literature.d/LIT-671.md),
  read in [NOTE-544](../notes.d/NOTE-544.md): Theorems 1–4, Lemma 4 and §6.

## The claim, assembled

**Pairs of solutions are joined by simple curves.** Garipov et al.,
[LIT-673](../literature.d/LIT-673.md), fitted the bend of a one-bend polygonal chain or a quadratic
Bezier curve between two networks trained from different initializations.
They minimized the loss averaged over points sampled uniformly along the
curve. On the curves they found, train loss and test error stay near the
endpoints'. On the straight segment they do not. For VGG-16 on CIFAR-10 the
segment's midpoint reaches 90% test error, against at most 7.01% on the
Bezier curve, and for ResNet-164 on CIFAR-100 it reaches 98.83% against
26.1% (Table 2). It holds for fully connected, convolutional, residual and
recurrent networks. The curve is not a reparametrization: an ensemble of an
endpoint with the point at t ≥ 0.4 already does as well as the two
endpoints (Fig. 2).

Draxler et al., [LIT-653](../literature.d/LIT-653.md), reached the same result at the same time by
another method, AutoNEB, a minimum-energy-path search from chemical
physics. Over ten minima per architecture, the highest training loss on the
best paths for deep ResNets and DenseNets on CIFAR-10 is almost the minima's
own, and test error rises by at most 0.5% (2.2% on CIFAR-100) (§4.3). Each
barrier is an upper bound, since AutoNEB can stall above the true saddle.
Their concatenation bound, L*_AC ≤ max{L_AB, L_BC}, is what turns pairwise
paths into a claim about one connected set: the best paths among the ten
minima form a spanning tree, and every pair is joined through it at no more
than the tree's highest edge.

**The connecting region has volume.** Benton et al., [LIT-656](../literature.d/LIT-656.md), trained
vertices so that loss stays low at points sampled uniformly inside the
simplexes they span. They found simplicial complexes of low loss joining 4
VGG-16 modes on CIFAR-100 and 7 on CIFAR-10 (Fig. 4). Adding connectors
between two VGG-16 modes on CIFAR-10, the complex kept its volume, with all
25 sampled models above 98% train accuracy, until the eleventh connector,
when it collapsed. So the low-loss region there has at least 10 dimensions
(§4.3, Fig. 5). That is a lower bound for one architecture.

**Found solutions, not all minima.** Kuditipudi et al., [LIT-671](../literature.d/LIT-671.md),
explain why trained networks are joined and show that the explanation is
needed. A solution is ε-dropout stable if, layer by layer, half its units
can be zeroed and the rest rescaled at a loss cost of at most ε. Two such
solutions are joined by a piecewise-linear path whose loss never exceeds
the worse endpoint by more than ε (Theorem 1). The spare half is scratch
space in which the working units can be permuted at no cost (Lemma 4). A
noise-stability condition from compression bounds gives a 10-segment path
with barrier Õ(ε) (Theorem 2). Conversely, for any student width and any
convex loss there is a dataset, labelled by a two-unit teacher, on which the
student's global minimizers are not connected (Theorem 4).
Overparametrization alone does not give connectivity. So the claim is
restricted to what training reaches, robust solutions, and Kuditipudi et
al. check that MNIST convnets and a VGG-11 trained with channel-wise dropout
roughly satisfy their conditions (§6).

**Width makes the connection easier.** In Garipov et al.'s supplement
(A.7), widening a small CNN brings the curve's worst train loss closer to
the endpoints' and shortens the curve relative to the segment. Draxler et
al. find barriers on their paths falling as CNNs get "wider and especially
deeper" (Fig. 5). Depth helps here, on curved paths. On straight lines
depth does the opposite, and that belongs to [THEORY-112](THEORY-112.md).

## What this does not say

- **It does not say the straight line works.** In every source the straight
  segment between two independent solutions has a large barrier. Linear
  connectivity is a further claim, made for copies sharing a start in
  [THEORY-114](THEORY-114.md) and after symmetry removal in [THEORY-112](THEORY-112.md).
- **It does not say every minimum is connected.** Kuditipudi et al.'s
  Theorem 4 constructs disconnected global minima at any width. The claim is
  about the solutions training reaches. How often disconnected minima occur
  on real data, Theorem 4 does not say.
- **"One set" is extrapolated.** Each source joins pairs, or complexes of
  at most seven modes. Draxler et al.'s spanning tree covers ten minima per
  architecture. Benton et al.'s picture of every SGD solution on one volume
  (their Fig. 1) is a framing, not a test.
- **"Near-constant" is relative.** On CIFAR-100 Garipov et al.'s curves
  peak 25–40% above the endpoints' train loss, and their WRN-28-10 polychain
  more than doubles test error at its worst point. Draxler et al. keep a
  small gap on CIFAR-100.
- **The evidence is image classification at CIFAR scale**, apart from one
  recurrent language model (Garipov et al., Table 3), with one curve per
  setting and no error bars.
- **It is not an explanation of why one bend suffices.** Kuditipudi et al.'s
  paths have many segments, and none of the sources explains why Garipov
  et al.'s one bend is enough.

## Connections

- **[THEORY-114](THEORY-114.md)** extends this account to straight lines, and says
  when during training they appear.
- **[THEORY-112](THEORY-112.md)** extends it from curves to straight lines once the
  architecture's symmetries are removed. It reads the connected volume as
  nearly convex modulo symmetry.
- **[THEORY-110](THEORY-110.md)** takes the weaker geometry: a centre linearly joined to
  the rest.
