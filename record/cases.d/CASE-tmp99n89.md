---
status: Proposed
title: 'Commutator bound on level-wise acquisition checked on perturbed tree data, in exact kernel flows and trained two-layer ReLU networks'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-066. Code, tests
    and results are committed under scratch/studies/lead-066/.
standing: documented
kind: executed-study
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
draws_on:
- THEORY-086
bears_on:
- QUESTION-217
summary: >-
  The numerical check of the commutator bound [LEAD-066](../leads.d/LEAD-066.md) asks for. Sixteen
  items on a binary tree of depth 4, inputs written in the tree's Haar
  basis with a strength per level and then perturbed off the tree
  symmetry by Gaussian noise of relative size 0 to 0.5; scalar targets
  with flat, falling or rising level strengths. Exact flows of the linear,
  infinite-width ReLU and Gaussian kernels (810 items), a two-by-two
  sharpness family, and two-layer ReLU networks of width 64 to 1024 from
  near-kernel and small initial scale (54 runs). Every bound held at every
  time checked; every acquisition time fell in its interval; no order the
  criterion certified was broken. The criterion is conservative: orders
  survived far beyond it. Below fine risks, off symmetry, the levels'
  times converged in ratio, as the resolution limit says. In trained
  networks the integral form of the moving-operator bound was vacuous and
  the damped form informative. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpo8cwu — new; the claim of LEAD-066 this study checks, filed 2026-11-22 -->

# CASE-tmp99n89: Commutator bound on level-wise acquisition checked on perturbed tree data, in exact kernel flows and trained two-layer ReLU networks

## The case

Run on 2026-11-22 with numpy and scipy on one CPU core, about three
minutes; code, tests (12) and results in scratch/studies/lead-066/, whose
README gives the statements checked and how to rerun.

- **Data.** n = 16 items, the leaves of a binary tree of depth 4. Inputs
  X₀ = √n H diag(c) R, H the Haar basis grouped by level, c_ℓ = ρ^(ℓ−1)
  with ρ = 0.7 or 0.85, R a random rotation: [LEAD-052](../leads.d/LEAD-052.md)'s construction.
  Perturbed inputs X = X₀ + Δ with ‖Δ‖_F = σ‖X₀‖_F, σ from 0 to 0.5.
  Scalar targets with level strengths flat, falling or rising.
- **E1, fixed kernels.** Linear, infinite-width two-layer ReLU NTK and
  Gaussian kernels; exact flows by eigendecomposition; nine risk
  thresholds δ from 0.3 to 10⁻¹²; five seeds; 810 items.
- **E2, sharpness.** Two levels, A = [[μ₁, η], [η, μ₂]], the start in the
  slow level.
- **E4, a moving operator.** Two-layer ReLU networks of width 64, 256 and
  1024, from initial scale 1 and 0.1, at σ = 0, 0.1 and 0.3, three seeds,
  trained by full-batch gradient descent from zero output, with the
  empirical tangent kernel recomputed at every step and the decoupled
  comparison flow run beside it.

## What it showed

- **Exact case.** At σ = 0 every commutator was below 6·10⁻¹¹, for all
  three kernels: [LEAD-052](../leads.d/LEAD-052.md)'s commutation reproduced.
- **The bounds held.** Theorem 1 at every time point of every perturbed
  item (largest observed over bound 0.78); 25,920 of 25,920 acquisition
  times inside their intervals; no certified pair out of order; the
  Davis–Kahan side remark and the data bound held throughout. In the
  networks the discrete moving-operator bound held at every step (largest
  ratio 0.79).
- **Sharpness.** The leakage reached 0.9999 of the bound when the source
  level was 10⁴ times slower than the receiving one.
- **Conservatism.** On random perturbations the uniform bound was three to
  seven times the departure seen. The order criterion certified 96–97% of
  pairs when the perturbation was about 9% of the smallest rate gap and
  at most 1% from about one gap on, while the order itself survived in 96–100% of
  pairs up to six or seven gaps. The pairs that did flip had small rate
  gaps (4% of pairs with relative gap below 0.3, none above 0.7) and, less
  strongly, a small target share.
- **Resolution.** The ratio of the latest level's time to the earliest's
  was the same at δ = 0.1 and 10⁻¹² under exact symmetry (3.3–5.6), and
  fell at 10⁻¹² to about 2 at σ = 0.001 and about 1.5 at σ = 0.1.
- **Networks.** Finite width alone breaks the symmetry: at σ = 0 and
  scale 1 the integrated commutator fell from 1.54 to 0.50 between width 64
  and 1024, roughly as one over the square root of width; at scale 0.1 it
  stayed near 1.5 at every width. The integral form of the bound allowed
  relative departures of 0.3 to 1.7 (vacuous), the damped form 0.03 to 0.18,
  against observed departures of 0.03 to 0.18 (medians). The networks'
  level order matched the decoupled flow's in 104 of 108 run-thresholds.

## What it can show

It is documented and executed: it shows the bounds hold, and how loose
they are, on these data, kernels and networks. It cannot show the bounds
true in general, which is the proof's job ([CLAIM-tmpo8cwu](../claims.d/CLAIM-tmpo8cwu.md)), and it does
not test learners outside squared loss and plain gradient descent, larger
trees, or data whose deviation from the tree is structured rather than
Gaussian.
