---
status: Read
paper: LIT-tmpazv9l
title: 'Do Deep Neural Network Solutions Form a Star Domain?'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v2 (20 pages). Main text and Appendices A, B, C and E
    read in full; Appendix D's figures read from captions. Tables 1–6 read
    from the text layer.
date: '2026-10-03'
summary: >-
  Conjecture 2: for width > αh (h the width at which SGD solutions are
  convex modulo permutation), the solution set is a star domain modulo
  permutation. Starlight (sample θ_n ∈ Z, t ∼ U[0,1], step on
  L((1−t)θ + tπ(θ_n)), re-permute by weight matching each epoch) finds θ⋆
  whose train-loss barriers to held-out models are about 2–5× lower than
  regular–regular ones across 8 settings, falling with |Z| up to 50. Not
  zero; star loss itself can be high (DenseNet CIFAR-100 0.635 vs 0.006).
  BMA on the star domain: better AUROC, worse ECE than an ensemble.
---


# NOTE-tmpp4hjy: Do Deep Neural Network Solutions Form a Star Domain?

## Contribution

It proposes a weaker geometry for SGD solution sets than convexity modulo
permutation. Instead of every pair being linearly connected, there is one
model linearly connected to all of them. It gives an algorithm that finds a
candidate, tests the candidate against solutions it never saw, and finds
it far better connected to them than they are to each other, on networks
too narrow for the convexity conjecture to hold.

## Key insight

A convex set has every point as a centre; a star domain needs only one. If
one model sits where all the solutions' basins overlap after alignment,
every solution is a straight line from it even when no two solutions are a
straight line from each other. You can look for such a model the way you
fit a Garipov curve, by training it so that random points on its lines to
many solutions have low loss. If it then connects to new solutions, the
centre is a property of the solution set, not of the training sample.

## Assumptions

- **Barrier** (Eq. 1): the maximum over t of L((1 − t)θ_A + tθ_B) minus the
  linear interpolation of the endpoint losses, evaluated at 11 points
  (Appendix A.2; 21 or 51 points change it by less than a standard
  deviation, Table 4).
- **Permutations**: weight matching via the `rebasin` package, recomputed
  once per epoch. BatchNorm statistics are recomputed at each interpolated
  model (Appendix A.3).
- **Solutions**: independently seeded SGD runs (Adam in one ablation);
  |Z| = 50 source and |H| = 5 held-out models for the main ResNet-18 runs.
- **Conjecture 2's width scaling** rests on Appendix E's informal argument,
  which assumes (1) barriers fall strictly monotonically with width, (2)
  star-regular barrier = α × regular-regular barrier, and (3) barrier
  inversely proportional to width.

## Key results

- **Table 1 (training loss)**: star-regular vs regular-regular barriers.
  CIFAR-10: ResNet-18 0.078 ± 0.007 vs 0.383 ± 0.056; ResNet-18 with Adam
  0.335 vs 1.368; VGG11 0.131 vs 0.515; VGG19 0.336 vs 1.281; DenseNet 1.729
  vs 4.634. CIFAR-100: ResNet-18 0.756 vs 2.905; DenseNet 3.735 vs 6.920.
  ImageNet-1k ResNet-18: 2.794 vs 5.948. The star model's own training loss
  is close to a regular model's for ResNet-18 but much higher for DenseNet
  (0.157 vs 0.001; 0.635 vs 0.006) and on ImageNet (1.380 vs 0.711).
- **Table 3 (test loss)**: the same ordering; VGG11's star-regular test
  barrier is 0.000 ± 0.000 against 0.242.
- **Fig. 1**: star-regular barrier decreases as |Z| goes from 2 to 50,
  without saturating.
- **Fig. 2**: across WideResNet widths 1×–8×, star-regular ≈ 0.31 ×
  regular-regular (e.g. about 0.004 vs 0.012 at 8×); across depths 22–40 the
  fit is y ≈ 0.05x + 0.30.
- **Table 5**: with 3, 5 or 15 held-out models the minimum regular-regular
  barrier (0.255) stays above the maximum star-regular one (0.117).
- **Table 6**: sampling t from Beta(2, 2) gives 0.069 against 0.084 for
  uniform; fixing t = 0.5 gives a lower barrier (0.018) but a worse star
  model (training loss 0.082).
- **Fig. 4, Table 2**: BMA over the star domain beats a deep ensemble on
  AUROC but not on ECE; star models are +0.1 to +1.1 points over a single
  model and below the ensemble.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Thin ResNets are not linearly connected after weight matching | moderate, reconfirming Git Re-Basin | Fig. 3, Table 1 |
| C2 | A model trained by Starlight is far better linearly connected to unseen solutions than solutions are to each other | strong as a relative result across 8 settings | Tables 1, 3, 5 |
| C3 | SGD solution sets are star domains modulo permutation (Conjecture 2) | weak: barriers to held-out models are lower but often well above zero, and the authors say so | Caveats in §3.4 |
| C4 | The width needed for a star domain is a fixed fraction α of that needed for convexity | weak: an informal derivation from assumed inverse proportionality and a linear fit | App. E, Fig. 2 |
| C5 | Star models can substitute for ensembles at inference and improve rank-based uncertainty | weak to moderate: small accuracy gains, worse calibration than ensembles | Table 2, Fig. 4 |

## Method

Algorithm 1 (Starlight). Each epoch, re-permute every θ_n ∈ Z to the
current θ by weight matching. Each step, sample θ_n uniformly, t ∼ U[0, 1]
and a batch, and update θ ← θ − λ(1 − t)∇_θ L((1 − t)θ + tθ_n). For fusion,
add a plain cross-entropy term L(θ). For BMA, sample a source index and
t ∼ U[0, 1] and average softmax outputs over the sampled models.

## Concepts

- **star domain**: a set A with some a₀ ∈ A such that every segment from a₀
  to a point of A lies in A.
- **star model**: a star point of the solution set modulo permutation.
- **source models Z / held-out models H**: the solutions Starlight is
  trained on, and disjoint solutions used only to test it.
- **winning permutation**: the function-preserving permutation of one model
  that minimises its barrier with another (Eq. 2, after Entezari et al.).

## Connections

- **Entezari et al. ([LIT-tmp2uwzo](../literature.d/LIT-tmp2uwzo.md))**: their convexity conjecture is
  Conjecture 1 here, and the star domain conjecture is defined relative to
  its critical width h.
- **Git Re-Basin ([LIT-tmpd6bma](../literature.d/LIT-tmpd6bma.md))**: weight matching is the permutation step;
  its narrow-network failure is the setting this paper addresses.
- **Lin, Li and Wu ([LIT-tmpziwl2](../literature.d/LIT-tmpziwl2.md))**: concurrent. Their star-shaped
  connectivity is proved in toy models and shown for 3–5 given minima,
  without permutations; this paper adds permutations and the held-out test.
- **Garipov et al. ([LIT-tmpotq71](../literature.d/LIT-tmpotq71.md)), Benton et al. ([LIT-tmp6yuwj](../literature.d/LIT-tmp6yuwj.md))**: the
  sampling scheme follows Garipov's curve fitting, and Benton's simplexes are
  the volume version of connecting many solutions.
- **Tran et al. ([LIT-tmpl7hwn](../literature.d/LIT-tmpl7hwn.md))** cite this paper among the star-shaped
  results that support the convexity picture.

## Bearing on the record

- A THEORY candidate, with Lin et al.: *SGD solution sets of a given
  architecture contain a centre linearly connected, after alignment, to the
  rest*. Proposed only: here the held-out barriers are reduced, not zero.
- It bears on the anthology's ensembling practice ([ANTH-SOTA-257](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-257.md)): one
  star model costs one forward pass, but in Table 2 it recovers well under
  half the ensemble's gain. That is an argument for the ensemble, not
  against it.

## Limitations

- **Not zero.** The authors' own caveat: star-regular barriers "often yield
  values that are significantly greater than zero". The paper's evidence is
  relative, star-regular against regular-regular.
- **Is the star model a solution?** For DenseNet and ImageNet its training
  loss is many times a regular model's, so θ⋆ ∈ S, which the definition of a
  star domain needs, is doubtful there.
- **Appendix E** assumes barrier ∝ 1/width. Under that assumption the
  barrier never reaches zero, so the width h at which the set "becomes
  convex" is not defined by it. The depth fit in Fig. 2 has a large
  intercept, which contradicts the assumed proportionality B⋆ = αB_r.
- **Weight matching only.** A better permutation method could lower the
  regular-regular baseline more than the star-regular one (Appendix C.3
  tries Sinkhorn re-basin once, on VGG19).

## Open questions

- Does the held-out barrier go to zero as |Z| grows, or level off? The
  trend in Fig. 1 had not saturated at 50.
- Is a star model a special point of the solution set, or would any model
  trained toward enough solutions do?

## Corrections

- none to a seeded skim (there was no seed)
