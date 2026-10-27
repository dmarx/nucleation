---
number: 774
status: Active
formerly:
- THEORY-tmpcvqfo
title: 'In a one-dimensional lattice hopping model with 2N+1 free hopping probabilities, all particles starting at the origin and the density after t steps observed with fixed Gaussian error, the Fisher metric is exactly t² times the distribution of the difference of two independent (t−1)-step walks, evaluated at the lag between the two hops, so it does not depend on the drift; when the walk is aperiodic with nonzero variance, its k-th largest eigenvalue is of order t^(3/2−k) for k = 0, …, 2N, so successive eigenvalues separate by a factor of order t'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-1018. The identity is implicit in the
    paper's supplement, Eq. 19, and the scaling is its Eq. 23, obtained
    there by a series argument that is loose (see below). Both are
    re-derived here step by step, the scaling with a bound that holds for
    every k, which meets the condition for Active under ADR-047 v2. The
    identity was checked numerically to machine precision, and the
    exponents for N = 3 at t = 20 to 160.
tags:
- information-geometry
- natural-sciences
date: '2026-10-20'
source:
- LIT-1299
summary: >-
  Machta, Chachra, Transtrum and Sethna (2013), [LIT-1299](../literature.d/LIT-1299.md), supplement
  §III, read in [NOTE-1018](../notes.d/NOTE-1018.md). The eigenvalues grow for particle creation
  (t^(3/2)) and drift (t^(1/2)) and fall from the diffusion constant on
  (t^(−1/2), t^(−3/2), …). The data are not a coarse-graining of one fixed
  data set, so nothing forbids growth. The metric is a least-squares metric
  with an arbitrary unit of error, and its eigenvalues depend on the
  coordinates θ_μ. The ratio between successive eigenvalues matches the
  1/n per Hermite order of [THEORY-742](THEORY-742.md)'s diffusion result, though the two
  set-ups differ.
bears_on:
- QUESTION-217
---
<!-- inactive-ok-file: THEORY-777 — Proposed; the same paper's Ising claim, set beside this one -->

# THEORY-774: In a one-dimensional lattice hopping model with 2N+1 free hopping probabilities, all particles starting at the origin and the density after t steps observed with fixed Gaussian error, the Fisher metric is exactly t² times the distribution of the difference of two independent (t−1)-step walks, evaluated at the lag between the two hops, so it does not depend on the drift; when the walk is aperiodic with nonzero variance, its k-th largest eigenvalue is of order t^(3/2−k) for k = 0, …, 2N, so successive eigenvalues separate by a factor of order t

## Source

Machta, Chachra, Transtrum and Sethna (2013), *Science* 342:604,
[LIT-1299](../literature.d/LIT-1299.md), arXiv:1303.6738v1, read in full in [NOTE-1018](../notes.d/NOTE-1018.md). The model
is the main text's Fig. 2 and supplement §III, Eqs. 14–23.

## What was actually shown

**The model.** Sites j ∈ ℤ. Parameters θ_μ, −N ≤ μ ≤ N, are the
probabilities of a hop by μ in one step. They are treated as free: their
sum is not fixed, so a direction that changes the number of particles
exists. The density after t steps from ρ₀ = δ_{j,0} is ρ_t = θ^{*t}, the
t-fold convolution. The data are ρ_t(j) at every j, each with independent
Gaussian error of width 1. The Fisher metric is then the least-squares
metric g = JᵀJ, J_{jμ} = ∂ρ_t(j)/∂θ_μ (the paper's Eqs. 10–11).

**Re-derivation, step by step.**

1. *The Jacobian.* ρ_t is a product of t copies of θ under convolution,
   so ∂ρ_t/∂θ_μ = t · (δ_μ * θ^{*(t−1)}), which gives
   J_{jμ} = t p_{t−1}(j − μ) with p_{t−1} = θ^{*(t−1)}.
2. *The identity.* g_μν = Σ_j J_{jμ}J_{jν} = t² Σ_i p_{t−1}(i)
   p_{t−1}(i + μ − ν) = t² q_t(μ − ν), where q_t is the autocorrelation of
   p_{t−1}: the law of X − X′ for two independent (t−1)-step walks. The
   drift cancels in X − X′, so g does not depend on it. The difference
   walk has mean 0 and variance 2(t−1)D, with D = Σθ_μ μ² − (Σθ_μ μ)²
   at Σθ_μ = 1. (The paper's Eq. 19 contains this, as the integrand
   |θ̃_k|^{2(t−1)}, but its Eq. 21 is written "for the case where the
   drift v = 0", a restriction the identity shows is not needed.)
3. *Fourier form.* q_t(d) = (1/2π) ∫_{−π}^{π} e^{ikd} w_t(k) dk with
   w_t(k) = |θ̃(k)|^{2(t−1)}, and |θ̃(k)|² = 1 − Dk² + O(k⁴) at Σθ = 1.
   If the walk is aperiodic, |θ̃(k)| < 1 for k ≠ 0, so all of the weight
   of w_t outside |k| < t^{−1/2+ε} is exponentially small, and with
   k = s/√t, w_t → e^{−Ds²} (Laplace's method).
4. *Grading.* Put M = 2N + 1 and expand e^{ikμ} = Σ_{a<M} (ikμ)^a/a! + r,
   with |r| ≤ (N|k|)^M/M!. Then g = t² · V S [K_t] S Vᵀ + (remainder),
   where V_{μa} = μ^a is the M × M Vandermonde matrix on −N, …, N
   (invertible), S = t^{−1/4} diag(t^{−a/2}), and
   K_t = (1/2π)∫ u(s) u(s)* w_t(s/√t) ds, u_a(s) = (is)^a/a!. In the
   graded frame S^{−1}V^{−1}(·)V^{−ᵀ}S^{−1}, the cross terms with r are of order
   t^{(b−M)/2} ≤ t^{−1/2} and the r r* term of order t^{−1}, so they
   vanish as t grows. K_t tends to
   K_∞ = (1/2π)∫ u u* e^{−Ds²} ds, the Gram matrix of the monomials
   (is)^a/a! under a Gaussian weight. Monomials are linearly independent,
   so K_∞ is positive definite.
5. *The eigenvalues.* g = X X* with X = t V S K_t^{1/2} (up to the
   vanishing remainder), so λ_k(g) = σ_k(X)². For invertible A and C,
   σ_k(B)/(‖A^{−1}‖‖C^{−1}‖) ≤ σ_k(ABC) ≤ ‖A‖‖C‖σ_k(B). With A = V,
   B = S, C = K_t^{1/2}, whose norms and inverse norms are bounded for
   large t by step 4, σ_k(S) = t^{−1/4 − k/2} gives
   λ_k(g) = Θ(t² · t^{−1/2−k}) = Θ(t^{3/2−k}), k = 0, …, 2N. The constants
   depend on N and on D, not on t.

**Checked numerically** (a script in the reader's scratchpad, not the
record). For N = 3 and θ_μ = 1/7, the paper's Fig. 2 case, the local
exponents of the seven eigenvalues between t = 40 and t = 80 are 1.501,
0.496, −0.514, −1.517, −2.515 and −3.517 (the seventh is below float
precision there); the prediction is 1.5, 0.5, −0.5, −1.5, −2.5, −3.5.
λ₂ t^{1/2} is 0.096, 0.094, 0.094 and 0.093 at t = 20, 40, 80, 160. For a
random kernel with drift v = 0.60, the identity of step 2 holds to 3 × 10⁻¹⁴
and the exponents are the same. At t = 7 the spectrum spans 7.6 × 10⁹,
which matches the figure. The top three eigenvectors at t = 80 are the
uniform vector (particle creation), the vector ∝ μ (drift) and a
quadratic one (the diffusion constant), as the paper says. When Σθ_μ is
held at 1, the creation direction goes and the rest keep their exponents.

**What could have come out otherwise.** The spectrum could have stayed
clustered, as at t = 1 where g is the identity. It could have separated
at a rate other than t per order, or depended on the drift. None of these
happens.

## What this does not say

- **Not that information is lost under coarse-graining.** The density at
  time t is not a function of the density at time 1. It is a different
  experiment with the same error per site, so the data-processing
  inequality does not apply and the creation and drift eigenvalues *grow*.
  This is unlike [THEORY-742](THEORY-742.md)'s diffusion model, where a trajectory of fixed
  duration is subsampled and no eigenvalue grows. The two agree in
  relative terms: here λ_k/λ₁ ∝ t^{1−k}, there g_μ/g₁ = n^{1−μ}, with k
  and μ both the Hermite order.
- **Not a coordinate-free hierarchy.** The metric is a least-squares
  metric with an arbitrary error width (σ = 1, which scales every
  eigenvalue alike), and its eigenvalues depend on using the θ_μ as
  coordinates. The paper's sloppiness is the spread of these eigenvalues.
  The invariant statement is the relative one: against the metric at
  t = 1, which is the identity in these coordinates, the generalized
  eigenvalues are the same numbers.
- **Not that the paper's own derivation is sound as written.** Its
  Eq. 22 expands g in powers of (μ − ν)² and says that "each term in the
  series contributes a single new non-zero eigenvalue". But the matrix
  [(μ − ν)^{2n}] has rank 2n + 1, not 1. The result is right, by the
  grading argument above, not by that one.
- **Nothing about critical systems.** Fluctuations here are short-range.
  The Ising half of the paper is [THEORY-777](THEORY-777.md).

## Connections

[THEORY-742](THEORY-742.md) is the information-geometric reformulation of the same
diffusion example by two of the same authors, with stochastic Fisher
information of a subsampled trajectory in place of a least-squares metric
on densities. It gives exact n^{1−μ} scaling at the Gaussian fixed point.
On [QUESTION-217](../questions.d/QUESTION-217.md), a reader's remark, not the paper's: in this model g is
exactly the Gauss–Newton Hessian of the sum-of-squares cost, so gradient
flow in the θ coordinates near a zero-residual fit converges along
eigendirection k at rate λ_k ∝ t^{3/2−k}. Creation, drift, diffusion
constant and then the higher moments are then fitted in the order of their
relevance. The nested effective models (creation; creation and drift;
creation, drift and diffusion) that the paper reads off the same
eigenvectors are a refinement chain by construction. All three orders
come from one eigenbasis, as in [THEORY-745](THEORY-745.md), and depend on the
coordinates: natural-gradient flow would fit every direction at the same
rate.
