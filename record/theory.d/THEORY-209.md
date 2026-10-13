---
number: 209
status: Proposed
formerly:
- THEORY-tmp4lwrf
promote_when: >-
  The two assumptions that carry the account, gradient-noise covariance
  proportional to the Hessian and a positive semidefinite quadratic loss,
  tested in a deep network outside one projection. What would promote: in
  an architecture other than a convnet, a measured noise covariance whose
  eigenvectors and eigenvalues track the Hessian's, and a limiting
  trajectory whose spread across many Hessian eigendirections, bulk
  included, matches the modified loss's isotropic prediction. What would
  refute it: a converged network whose limiting trajectory is anisotropic
  in the Hessian's column space in proportion to the training loss's
  curvature, as a Gibbs distribution on the training loss would be. Or an
  instantaneous speed that does not scale as η²/(S(1 − β²)) across a sweep.
  More two-dimensional projections of the same ResNet cannot settle it.
title: 'A converged network trained with SGD is not at a point and does not sample its training loss: under a quadratic approximation it samples a Gibbs distribution on a modified loss, isotropic in the Hessian''s column space, with probability currents that keep it oscillating, so its speed and spread are set by the learning rate, momentum and batch size'
version: 1
tags:
- learning-theory
- loss-landscapes
- thermodynamics
- anthology-candidate
date: '2026-10-13'
source:
- LIT-1011
answers:
- QUESTION-069
summary: >-
  Kunin et al. (2021), [LIT-1011](../literature.d/LIT-1011.md), read in [NOTE-711](../notes.d/NOTE-711.md). Modelled as an
  underdamped Langevin equation with noise covariance proportional to the
  Hessian, SGD at the end of training converges to a nonequilibrium
  stationary state: Gibbs on a modified loss whose curvature undoes the
  Hessian's anisotropy, with inverse temperature S(1 − β²), in broken
  detailed balance. A ResNet-18 on ImageNet explores isotropically in a
  plane where the loss is anisotropic, oscillates at Hessian-dependent
  rates, and moves at the predicted speed across a hyperparameter sweep.
  For the learned-structure line, a trained solution is in part a property
  of the regime that trained it. Proposed: the deep-learning evidence is
  one network, under assumptions the paper concedes are strained.
---
<!-- inactive-ok-file: THEORY-211 — Proposed; the account of the law of balance set beside this one, open -->
<!-- inactive-ok-file: THEORY-085 THEORY-083 THEORY-210 QUESTION-080 — Proposed or Open; readings and a question set beside this account on 2026-10-13, open -->
<!-- inactive-ok-file: THEORY-108 — Proposed; the reading whose temperature axis this account interprets, open -->

# THEORY-209: A converged network trained with SGD is not at a point and does not sample its training loss: under a quadratic approximation it samples a Gibbs distribution on a modified loss, isotropic in the Hessian's column space, with probability currents that keep it oscillating, so its speed and spread are set by the learning rate, momentum and batch size

## Source

Kunin, Sagastuy-Brena, Gillespie, Margalit, Tanaka, Ganguli & Yamins (2021),
[LIT-1011](../literature.d/LIT-1011.md), read in [NOTE-711](../notes.d/NOTE-711.md): §§1–9 and Appendices A–C and H. The
derivations in Appendices D–G were not checked.

## The claim

**What a converged run is.** Resumed training of pre-trained ImageNet
convnets keeps moving at a near-constant step size, and drifts away from
its starting weights as a power law in steps, with exponents from about
1.07 to 1.62. On the paper's account this is not noise around a minimum.
It is a stationary process with three properties:

- **It samples a modified loss.** For linear regression with noise
  covariance σ²H, the stationary distribution is Gibbs on a modified loss.
  Its parameter part has curvature H⁻¹(H + λI)/(η(1 + β)), which for small
  weight decay is isotropic on the Hessian's column space. The run spreads
  equally along sharp and flat-but-nonzero directions, not more along the
  flat ones as a Gibbs distribution on the training loss would.
- **It circulates.** The stationary state is in broken detailed balance.
  A non-zero probability current rotates the run in each eigen-plane of the
  Hessian, in position and velocity, at rates set by the eigenvalues. With
  many incommensurate rates the paths fill the level sets of the modified
  loss rather than closing into cycles.
- **The optimizer sets its scale.** The inverse temperature is
  κ = S(1 − β²), the instantaneous speed is η²σ²tr(H)/(S(1 − β²)), and the
  damping of each mode is (1 − β)/√(2η(1 + β)(ρ + λ)). A larger learning
  rate makes modes underdamped and slows global transport.

**The evidence in deep networks.** Under a quadratic approximation of the
loss at the end of training, a pre-trained ResNet-18 on ImageNet shows the
three properties: isotropic coverage in the plane of Hessian eigenvectors
1 and 30 where both losses are anisotropic, velocity contours following
the inverse Hessian, and rotations at different rates in the two
eigen-planes. Its speed follows the formula across sweeps of learning
rate, batch size and momentum, from one fitted constant.

## What it bears on

[QUESTION-069](../questions.d/QUESTION-069.md) asks whether the connectedness of trained solutions belongs
to the solutions, the instrument, the shared history or the regime. This
account bears on the last. Before connectivity between two runs can be
asked about, each run is a distribution whose spread, shape and
correlations depend on η, β and S. [THEORY-108](THEORY-108.md)'s temperature axis (learning
rate, batch size, weight decay) is, at the end of training, this account's
inverse temperature and damping. The account does not measure
connectivity, and does not say how two runs' distributions relate.

## What this does not say

- **It does not cover flat directions.** Noise and drift both vanish on
  the Hessian's null space, so travel along flat or symmetric directions,
  where re-basin and connectivity results live, is outside the model.
- **It does not establish the assumptions for deep networks.** Σ ∝ H is
  derived for a noisy linear teacher, not measured in the ResNet. The
  paper concedes the end-of-training Hessian has negative eigenvalues,
  which the quadratic assumption excludes.
- **It does not say the isotropy holds beyond the top thirty
  eigenvectors.** It is shown in one two-dimensional projection, with an
  eigenvalue ratio of about 6.
- **It does not say anything about adaptive optimizers or test
  accuracy.**
- **It does not instruct.** That the loss curve hides this motion, and
  what to do about it, is the anthology's reading ([ANTH-THEORY-031](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-031.md),
  [ANTH-SOTA-270](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-270.md)).

## Note of 2026-10-13: what other readings say about the assumptions and the gap

**On the noise-covariance assumption ([THEORY-085](THEORY-085.md)).** The account needs
gradient-noise covariance proportional to the Hessian. At a minimum the
gradient covariance is close to the Fisher. [THEORY-085](THEORY-085.md) (Papyan) reads the
Fisher's top eigenspace as class outliers built from class means. That
gives partial support for the assumption in the top eigenspace, and marks
the limit of the test: the isotropy result projects onto Hessian
eigenvectors 1 and 30 of a 1000-class ImageNet model, inside that outlier
structure. The bulk, which the outlier structure leaves out, is untested.
No typed edge: [THEORY-085](THEORY-085.md) neither grounds nor contradicts the account.

**On the null space ([THEORY-210](THEORY-210.md), from [LIT-970](../literature.d/LIT-970.md)).** This account is
silent on the Hessian's null space, where continuous parameter symmetries
put the flat directions. [THEORY-210](THEORY-210.md) describes what happens there.
Under gradient flow, position along a symmetry orbit is conserved. Under
SGD, the results the survey reports find conserved quantities drifting
toward balance. One of them (Ziyin et al. 2023a) finds a stationary
distribution "different from predictions from a Langevin model". So the
two accounts cover complementary halves of the limiting dynamics, and
may disagree about the null-space half.

**On neural collapse ([QUESTION-080](../questions.d/QUESTION-080.md)).** [THEORY-083](THEORY-083.md)'s terminal-phase
convergence and this account's perpetual motion are both pictures of the
end of training. The question of what stays fixed while the parameters
move is filed as [QUESTION-080](../questions.d/QUESTION-080.md).

## Note of 2026-10-13: the null space, read first-hand

The note above left open whether this account and [THEORY-210](THEORY-210.md) disagree on
the Hessian's null space. Reading Neural Mechanics ([LIT-1013](../literature.d/LIT-1013.md)) and
Ziyin et al. ([LIT-1012](../literature.d/LIT-1012.md)) settles where and why.

- **The shared property.** Minibatch noise has no component along a
  symmetry's generator (Neural Mechanics, §5). This account's assumption,
  noise covariance proportional to the Hessian, has the same property.
- **The difference.** This account also takes the covariance to be
  independent of the parameters (Assumption 3). Under that assumption the
  Itô drift along a symmetry vanishes, and the coordinate along it is
  frozen. With the covariance's real dependence on the parameters, a
  rescaling symmetry's coordinate is driven to the point where the two
  layers' gradient noise balances, at a rate proportional to η/S
  ([THEORY-211](THEORY-211.md)).

So the two accounts describe one stationary state from two sides. This
account covers the Hessian's image, where the run oscillates
isotropically on a modified loss. [THEORY-211](THEORY-211.md) covers the symmetry
directions, where the run is driven to a balance. The cost of
Assumption 3 is that it misdescribes the second.
