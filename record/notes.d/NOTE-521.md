---
number: 521
status: Read
formerly:
- NOTE-tmp7wcsb
paper: LIT-662
title: 'Geodesic Mode Connectivity'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv v1 (4 pages): main text, both figures and both
    appendices. Figure 2's curves were read from its caption and the text;
    no numbers are reported in the text, so none are quoted here.
date: '2026-10-03'
summary: >-
  Length of a path in distribution space = √8 ∫ √dJSD (Fisher–Rao). Minimise
  the discrete energy Σ JSD(pᵢ‖pᵢ₊₁) over 25 interior models between two
  weight-matched ResNet-20 (4×, LayerNorm) CIFAR-10 networks, initialised on
  the line; the result keeps train and test loss low where the line has a
  large barrier, using unlabelled training images. One pair, no numbers in
  the text, hypothesis stated for all geodesics.
---

# NOTE-521: Geodesic Mode Connectivity

## Contribution

It proposes a way to find a low-loss path between two networks without
using the loss. It shortens the path in the space of the networks'
predictive distributions instead. On one pair of permuted ResNet-20s where
the straight line fails, the shortened path succeeds.

## Key insight

If two networks compute nearly the same function, the shortest way between
them in function space should pass only through networks that also compute
nearly that function, so the loss should stay low along it. In parameter
space that path looks curved. The objective needs only inputs, because it
compares the networks' outputs with each other, not with labels.

## Assumptions

- **Model as joint distribution**: p(x, ŷ; θ) = p(x)p(ŷ|x; θ), with p(x)
  the empirical input distribution; "under certain assumptions" this space
  is a Riemannian manifold with the Fisher–Rao metric g_ij(θ) =
  E[∂ᵢ log p · ∂ⱼ log p] (Appendix A.1).
- **Discretisation**: the integral is replaced by a sum of JSDs between
  consecutive models, without the square root, so the energy rather than
  the length is minimised (§2).
- **Setting**: ResNet-20 at 4× width with LayerNorm instead of BatchNorm
  (as in Git Re-Basin; the authors note a few points of test accuracy are
  lost by the swap), CIFAR-10, two seeds, Git Re-Basin weight matching,
  N = 25, SGD with learning rate 0.1 and batch size 256 (Appendix A.2).

## Key results

- **Fig. 2 (left)**: optimisation lowers the summed √JSD along the chain
  while raising its Euclidean length relative to the line.
- **Fig. 2 (right)**: after optimisation, train and test cross-entropy are
  low at every model on the chain; on the straight line both rise sharply in
  the middle.
- No table, error bar, second pair or second architecture.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The JSD-energy chain finds a low-loss path between weight-matched narrow ResNets where the straight line has a barrier | weak: one pair, one figure, no numbers in text | Fig. 2 |
| C2 | Geodesics in distribution space correspond to mode-connecting paths, and all geodesics between SGD solutions are mode-connecting | conjecture, not tested beyond C1 | §1 |
| C3 | Mode connectivity can be found without labels | weak: follows from C1, since only images are used | §3, App. A.2 |

## Method

Initialise θ₂ … θ₂₄ by linear interpolation between θ_a = θ₁ and π(θ_b) =
θ₂₅. Hold the endpoints fixed and minimise Σᵢ₌₁²⁴ JSD(p(·; θᵢ) ‖ p(·;
θᵢ₊₁)) over training images with SGD. Evaluate cross-entropy at each θᵢ on
train and test sets.

## Concepts

- **Fisher–Rao metric**: the Fisher information matrix used as a Riemannian
  metric on the space of distributions.
- **geodesic mode connectivity**: low loss along a (discretised) geodesic
  in that space.
- **energy vs length functional**: minimising Σ JSD instead of Σ √JSD gives
  the geodesic of constant speed.

## Connections

- **Git Re-Basin ([LIT-661](../literature.d/LIT-661.md))**: the permutation, the architecture and the
  failed linear baseline all come from it. This paper starts where its
  straight line breaks.
- **Entezari et al. ([LIT-652](../literature.d/LIT-652.md))**: cited for the permutation symmetry
  that weight matching exploits.
- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md))**: the curved-path phenomenon being
  reframed. Garipov fits a Bezier curve to low *loss*, using labels; this
  paper fits a chain to short *distribution length*, without labels. The
  comparison is left to future work.
- **Lin, Li and Wu ([LIT-682](../literature.d/LIT-682.md))**: their "geodesic connectivity" is a
  different quantity, the Euclidean length of the shortest path that stays
  inside the minimum manifold.

## Bearing on the record

- Bears on `information-geometry` in the record: the Fisher metric used to
  find paths between trained networks, not only to precondition training.
- A possible THEORY, held back here because the evidence is one figure:
  *between functionally similar minima, a short path in output-distribution
  space is a low-loss path in parameter space*.
- No instruction for practice.

## Limitations

- **Evidence**: one model pair, one architecture, no numbers, no baseline
  against Garipov et al.'s curves or Draxler et al.'s ([LIT-653](../literature.d/LIT-653.md)) nudged elastic band.
- **"Narrow"**: the contribution list says narrow ResNets, but the
  experiment is 4× width. That is narrow only next to the 32× width Git
  Re-Basin needed for LMC.
- **Why low JSD gives low loss is not argued.** The endpoints already
  have low loss, and a chain whose neighbours agree in output stays close to
  their outputs. The objective may be finding a path along which the
  function barely changes, which is mode connectivity almost by
  construction, rather than anything special about geodesics.
- **Discretisation**: whether 25 models with a summed JSD approximate the
  continuous geodesic is not checked.

## Open questions

- Do the geodesic paths coincide with, or differ from, Garipov-style
  Bezier curves between the same endpoints?
- Does the method work without the permutation step, or between narrower
  networks?

## Corrections

- none to a seeded skim (there was no seed)
