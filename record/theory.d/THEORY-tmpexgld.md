---
status: Proposed
promote_when: >-
  Held-out barriers to the centre shown to go to zero, not merely below the
  pairwise ones. Sonthalia et al.'s star-to-held-out barriers are about 2–5 times
  lower than the barriers between held-out solutions, and still well above
  zero. They were still falling at 50 source models. What would promote: the
  held-out barrier followed as the number of source models grows, until it
  either reaches the endpoints' own loss or stops falling, with the centre's
  own training loss at a regular solution's, in a network too thin for
  pairwise linear connectivity after alignment. A proof of star-shaped
  connectivity modulo permutation for a non-linear deep network would do it
  from the other side. What would refute it: the held-out barrier levelling
  off at a clearly positive value as source models are added, or falling only
  as the centre's own loss rises, so that the centre is not a solution.
  Larger relative improvements over the pairwise baseline cannot settle it.
title: 'A set of trained solutions has a centre that is linearly connected, after alignment, to the rest of them: the solution set is a star domain even where it is not convex'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmpazv9l
- LIT-tmpziwl2
extends:
- THEORY-tmpkd2ju
- THEORY-tmpcu710
summary: >-
  Sonthalia et al. (2024), [LIT-tmpazv9l](../literature.d/LIT-tmpazv9l.md), conjecture that below the width at
  which SGD solutions become convex modulo permutation they are still a star
  domain, and train a star model whose barriers to held-out solutions,
  after weight matching, are about 2–5 times lower than those between solutions
  (ResNet-18 CIFAR-10 0.078 against 0.383; ImageNet 2.794 against 5.948),
  and not zero. Lin et al. (2024), [LIT-tmpziwl2](../literature.d/LIT-tmpziwl2.md), prove star-shaped linear
  connectivity for wide two-layer teacher–student and deep linear networks,
  and find centres for five trained image classifiers with no permutation.
  Proposed: reduced, not zero, and no held-out test without alignment.
---
<!-- inactive-ok-file: THEORY-tmpkd2ju THEORY-tmpcu710 — Proposed; the accounts this one extends, filed with it -->

# THEORY-tmpexgld: A set of trained solutions has a centre that is linearly connected, after alignment, to the rest of them: the solution set is a star domain even where it is not convex

## Source

- Sonthalia, Rubinstein, Abbasnejad & Oh (2024), [LIT-tmpazv9l](../literature.d/LIT-tmpazv9l.md), read in
  [NOTE-tmpp4hjy](../notes.d/NOTE-tmpp4hjy.md): Conjecture 2, Algorithm 1, Tables 1, 3 and 5, Figs. 1–2
  and Appendix E.
- Lin, Li & Wu (2024), [LIT-tmpziwl2](../literature.d/LIT-tmpziwl2.md), read in [NOTE-tmppznp2](../notes.d/NOTE-tmppznp2.md): Theorems 6,
  10–11, 14 and 18, Tables 1–2.

## The claim, assembled

**A star domain is weaker than convexity.** A set is a star domain if some
point in it, a centre, is joined by a straight segment inside the set to
every other point. A convex set has every point as a centre. Sonthalia et
al., [LIT-tmpazv9l](../literature.d/LIT-tmpazv9l.md), take Entezari et al.'s conjecture, that SGD solutions are
convex modulo permutation once networks are wide enough, as their
Conjecture 1. They propose that below that width the solution set modulo
permutation is still a star domain (Conjecture 2).

**A centre that connects to solutions it never saw.** Their Starlight
trains a candidate centre. Each step it samples one of 50 source solutions
and a point t on the line to it, and descends the loss there. Every epoch it
re-permutes all source solutions to the candidate by Git Re-Basin's weight
matching. The test is on held-out solutions. Training-loss barriers between
the star model and held-out solutions, against barriers between two
held-out solutions, are: ResNet-18 on CIFAR-10 0.078 against 0.383, VGG19
0.336 against 1.281, DenseNet on CIFAR-100 3.735 against 6.920, ResNet-18
on ImageNet-1k 2.794 against 5.948 (Table 1). With 3, 5 or 15 held-out
solutions, the smallest pairwise barrier (0.255) stays above the largest
star barrier (0.117) (Table 5). The star barrier falls as the number of
source models goes from 2 to 50, and had not levelled off (Fig. 1). This
could have failed: a centre fitted to fifty solutions need not connect to
a fifty-first.

**Provable in toy models, without permutations.** Lin et al., [LIT-tmpziwl2](../literature.d/LIT-tmpziwl2.md),
prove star-shaped connectivity where the minimum set can be written down.
For a two-layer ReLU student of an orthonormal teacher, k minima drawn
uniformly share a linearly connected centre with probability at least
1 − M((M^k − 1)/M^k)^{m − kM} (Theorem 10). With width m ≥ kM, a centre
joined to all k by two-piece paths always exists (Theorem 11). For deep
linear networks wider than 1 + r(L − 1), r minima almost surely share a
linearly connected centre (Theorem 18). The mechanism is spare capacity:
each minimum can be moved in a straight line to one that uses only neurons
the others can agree on. Their centre-finding objective, the same idea as
Starlight with no alignment step, finds centres for five trained FNNs,
VGG16s and ResNets on MNIST and CIFAR-10. Barriers through the centre are
3.1e-05 to 1.0e-02, against 1.25 to 16.91 on the direct lines (Table 1).

## What this does not say

- **It does not say the barriers to the centre are zero.** Sonthalia et
  al.'s are lower than the pairwise ones, not zero. In their own words, they
  "often yield values that are significantly greater than zero". That is
  why this is Proposed.
- **It does not say the centre is always a solution.** A star domain's
  centre must lie in the set. Sonthalia et al.'s star model has a training
  loss close to a regular solution's for ResNet-18, but 0.157 against 0.001
  for DenseNet on CIFAR-10, 0.635 against 0.006 on CIFAR-100, and 1.380
  against 0.711 on ImageNet. There the centre is doubtfully a member.
- **"After alignment" is half the evidence.** Sonthalia et al. align by
  permutation. Lin et al. find centres with no alignment, but only for the
  five minima they fitted the centre to, with no held-out test, and their
  minima were trained with Adam. The two results are not one test with and
  without alignment.
- **It does not give the width scaling.** Sonthalia et al.'s claim that the
  width needed is a fixed fraction of the width for convexity rests on an
  informal argument (Appendix E) that assumes barrier ∝ 1/width. Under that
  assumption the barrier never reaches zero, so the width it is a fraction
  of is not defined.
- **The proofs are in toy models.** Orthonormal teacher, spherical inputs
  and population loss, or a linear network.

## Connections

- **[THEORY-tmpkd2ju](THEORY-tmpkd2ju.md).** This account extends it. That account says that once
  symmetry is removed the straight line between solutions loses most of its
  barrier, which makes the solution set nearly convex modulo symmetry. This
  one keeps the quotient by symmetry and asks for less: one centre, not
  every pair. Its evidence comes from networks too thin for the pairwise
  claim. Sonthalia et al.'s pairwise baselines reconfirm Git Re-Basin's
  failure at 1× width. It is declared as `extends`, not `rivals`, because
  the two can both be right. A convex set is a star domain, and Sonthalia et
  al. define their conjecture relative to the width at which Entezari's
  holds, as what holds below it. If the symmetry account held at every
  width, this one would be true and empty. Its content is the regime where
  the other fails.
- **[THEORY-tmpcu710](THEORY-tmpcu710.md).** This account extends it too. The connected low-loss
  set that account describes has, on this one, a point from which the
  connecting curves straighten. Lin et al. get there without any symmetry,
  from spare capacity, as Kuditipudi et al. ([LIT-tmplpsy5](../literature.d/LIT-tmplpsy5.md)) did for curves.
  Benton et al.'s simplexes ([LIT-tmp6yuwj](../literature.d/LIT-tmp6yuwj.md)) are the volume version of
  joining many solutions at once, and Sonthalia et al. place their star
  domains beside them.
