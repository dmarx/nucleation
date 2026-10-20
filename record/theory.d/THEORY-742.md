---
number: 742
status: Active
formerly:
- THEORY-tmp1bqec
title: 'For a Boltzmann distribution linear in its couplings, observed through any coarse-graining map, the Fisher information the coarse data lose about the bare couplings is the expected conditional covariance of the energy operators given the coarse state; when the renormalized Hamiltonian stays in the family, the parameter map is linear and the additive constant of the step is analytic, that loss is the constant''s Hessian, so the singular part of the metric passes unchanged to the coarse data. In the hopping model of diffusion at its Gaussian fixed point, keeping every n-th position of a trajectory of fixed duration multiplies the metric by n^(1−μ) in the μ-th Hermite coordinate: the drift''s information is kept exactly, the variance''s falls as 1/n, and higher shape parameters'' faster'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-972. The identity is the paper's Eqs. 14
    and 15, the closure step its Eqs. 11–12 and the line after Eq. 15, and
    the diffusion result its Eqs. 5–9. Each is re-derived below step by
    step, which meets the condition for Active under ADR-047 v2; the
    diffusion scaling was also checked numerically for μ = 3, 4, 5 and
    n = 1, 2, 4, 8. The paper's further claims, that irrelevant directions
    contract as b^−(d−2λ) and that relevant ones are preserved in general,
    rest on a scaling argument and are kept out of the title.
- version: 2
  date: '2026-10-20'
  note: >-
    Machta et al. (2013) is now read (NOTE-tmpfc575). The λ = d/2 dividing
    line, which this entry called the reader's algebra, is credited to
    their supplement, and the numerics behind Eq. 21 are described and
    cited (THEORY-tmpzyxwe). The account is unchanged.
tags:
- information-geometry
- natural-sciences
- information-theory
date: '2026-10-20'
source:
- LIT-1254
summary: >-
  Raju, Machta and Sethna (2018), [LIT-1254](../literature.d/LIT-1254.md), read in [NOTE-972](../notes.d/NOTE-972.md).
  The loss identity holds for any coarse-graining of an exponential family;
  that the loss is analytic, and so spares the singular part of the metric,
  needs an exact renormalization step with linear beta functions and an
  analytic constant. It does not say that relevant directions keep their
  information in general: on the paper's own scalings only directions with
  RG eigenvalue above d/2 do, and away from the Gaussian fixed point even
  the drift loses information.
---
<!-- inactive-ok-file: THEORY-194 THEORY-202 — Proposed; accounts this one is set beside, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-tmpzyxwe — Proposed; the numerics behind Eq. 21, cited for what they are -->
# THEORY-742: For a Boltzmann distribution linear in its couplings, observed through any coarse-graining map, the Fisher information the coarse data lose about the bare couplings is the expected conditional covariance of the energy operators given the coarse state; when the renormalized Hamiltonian stays in the family, the parameter map is linear and the additive constant of the step is analytic, that loss is the constant's Hessian, so the singular part of the metric passes unchanged to the coarse data. In the hopping model of diffusion at its Gaussian fixed point, keeping every n-th position of a trajectory of fixed duration multiplies the metric by n^(1−μ) in the μ-th Hermite coordinate: the drift's information is kept exactly, the variance's falls as 1/n, and higher shape parameters' faster

## Source

Raju, Machta and Sethna (2018), *Phys. Rev. E* 98:052112, [LIT-1254](../literature.d/LIT-1254.md),
arXiv:1710.05787v2, read in full in [NOTE-972](../notes.d/NOTE-972.md). The identity is the
paper's Eqs. 10, 14 and 15. The closure step is Eqs. 11–12 and the line
after Eq. 15 ("g̃µν = gµν − ∂µ∂νG"). The diffusion result is Eqs. 5–9.

## What was actually shown

The metric throughout is the Fisher information of the *whole* data set,
not a density. It is extensive, so a coarse-grained system of the same
physical size, with fewer coarse sites, carries less of it by construction.
That accounting is the paper's choice (its modified Lie derivative
L̄ = L_β − L∂_L), and the statements below use it.

**Re-derivation, step by step.**

1. *The bare metric.* Take P(x | θ) = exp(−Σ_μ θ_μ Φ_μ(x)) / Z(θ). The
   score is ∂_μ log P = −Φ_μ + ⟨Φ_μ⟩, so g_μν = Cov(Φ_μ, Φ_ν) = ∂_μ∂_ν log Z
   (Eq. 10).
2. *The coarse metric.* For a map x̃ = C(x), p(x̃ | θ) = Σ_{x: C(x) = x̃}
   P(x | θ). Differentiating the sum gives ∂_μ log p(x̃) = −E[Φ_μ | x̃] +
   ⟨Φ_μ⟩, so g̃_μν = Cov(E[Φ_μ | x̃], E[Φ_ν | x̃]) (Eq. 15).
3. *The loss.* By the law of total covariance, Cov(Φ_μ, Φ_ν) =
   E[Cov(Φ_μ, Φ_ν | x̃)] + Cov(E[Φ_μ | x̃], E[Φ_ν | x̃]). So g − g̃ =
   E[Cov(Φ | x̃)] (Eq. 14), which is positive semidefinite. Nothing about
   renormalization is used up to here.
4. *Closure.* Suppose the restricted partition function is
   Z̃(x̃) = exp(G(θ) − H̃(x̃; θ̃)), with H̃ = Σ θ̃_μ Φ̃_μ(x̃) of the same form
   on the coarse lattice and θ̃ = Mθ linear. Then −log p(x̃) =
   H̃(x̃; Mθ) − G(θ) + log Z(θ). H̃ is linear in θ, so its second
   derivatives vanish, and taking expectations gives g̃ = g − ∂∂G. With
   step 3, ∂∂G = E[Cov(Φ | x̃)] ⪰ 0. (The sign of G here is chosen so that
   the loss is +∂∂G. The paper's Eq. 11 writes the same relation less
   clearly.)
5. *The singular part.* If G is analytic in θ, then g − g̃ is analytic, so
   g̃ and g have the same singular part as functions of θ. Equivalently,
   summing step 4 over x̃ gives log Z(θ, L) = G(θ) + log Z(Mθ, L/b), and
   differentiating twice gives g^(s)(θ, L) = Mᵀ g^(s)(Mθ, L/b) M. That is
   the finite form of the paper's Eq. 17, L̄_β g^(s) = 0, which the paper
   obtains from the scaling relation Eq. 16 by differentiating twice. The
   term in ∂∂β drops only because β is linear.
6. *Diffusion.* Take increments with kernel
   K(x) = φ(y)[1 + Σ_{μ≥3} θ_μ He_μ(y) / (μ! θ₂^{μ/2})] / √θ₂, with
   y = (x − θ₁)/√θ₂ and He_μ the probabilists' Hermite polynomials. At
   θ_μ = 0 (μ ≥ 3), the score of one increment along θ_μ is
   He_μ(y)/(μ! θ₂^{μ/2}), and E[He_μ He_ν] = μ! δ_μν, so m increments carry
   g_μν = m δ_μν / (μ! θ₂^μ) (Eq. 6). To first order in θ the n-fold
   convolution multiplies the Fourier factor (ik√θ₂)^μ e^{−k²θ₂/2} by
   e^{−(n−1)k²θ₂/2}, which is the μ-th Hermite term of the n-step Gaussian
   with coefficient n·n^{−μ/2}. So the score of one n-step increment along
   θ_μ is n^{1−μ/2} He_μ(y⁽ⁿ⁾)/(μ! θ₂^{μ/2}), with y⁽ⁿ⁾ standard normal; its
   variance is n^{2−μ}/(μ! θ₂^μ); and m/n such increments give
   g⁽ⁿ⁾_μν = n^{1−μ} g⁽⁰⁾_μν (Eq. 9). For the drift and variance directly:
   an n-step increment has mean nθ₁ and variance nθ₂, so m/n of them carry
   (m/n)·n²/(nθ₂) = m/θ₂ about θ₁ (n⁰) and (m/n)·1/(2θ₂²) about θ₂ (n⁻¹),
   both matching n^{1−μ}. Only first order in θ is needed, because the
   metric at θ = 0 depends only on first derivatives of the distribution.

**Checked numerically** (a script in the reader's scratchpad, not the
record): for μ = 3, 4, 5 and n = 1, 2, 4, 8, the Fisher information per
n-step increment of a numerically convolved kernel agrees with
n^{2−μ}/μ! to six figures.

**What could have come out otherwise.** The loss could have contained a
non-analytic part even for an exact step, which would have eroded the
singular part; under closure and an analytic G it cannot. The diffusion
scaling could have been non-monotone in μ, or could have spared the
variance; it is neither.

## What this does not say

- **Not that relevant directions keep their information in general.** The
  title keeps the *singular* part of the metric. The full metric along a
  relevant direction also has an analytic part, which the coarse data
  lose. The paper's own scalings, Eqs. 20–21, put the singular part at
  L^d ξ^{−(d−2λ)} and the analytic part at L^d b^{−(d−2λ)}. For b < ξ the
  singular part dominates only when λ > d/2, where the susceptibility
  diverges. A relevant direction with 0 < λ < d/2, such as the thermal
  direction of a transition with α < 0, would lose information as
  b^{−(d−2λ)} until b reaches ξ. The paper does not state this, but
  Machta et al. (2013, [LIT-tmps1ffa](../literature.d/LIT-tmps1ffa.md)) do: their supplement says the
  singular part dominates "provided 2y_i − d ≥ 0" and that relevant
  directions with 0 < 2y < d contract. This paper dropped it. The diffusion example
  agrees with it: the drift, kept exactly, has λ = 1/2 = d/2.
- **Not that the drift is kept away from the Gaussian fixed point.** The
  paper explains its preservation as "the mean drift is given by the two
  endpoints". The endpoints are sufficient for the drift only when the
  kernel is Gaussian. For a unit-variance Laplace kernel, the reader's
  computation gives the drift information per original step as 2.00, 1.19,
  1.09 and 1.06 at n = 1, 2, 3, 4, falling towards the Gaussian bound 1/θ₂.
  So the non-Gaussian surplus is lost, as the paper's general picture
  would expect, but the relevant direction is not "exactly preserved".
- **Not that irrelevant directions contract as b^−(d−2λ).** Eq. 21 comes
  from a scaling argument ("should be dominated by", "with higher order
  corrections"), and the authors rest their confidence on the numerics of
  Machta et al. (2013), filed as [THEORY-tmpzyxwe](THEORY-tmpzyxwe.md) (Proposed): one 64×64
  lattice at T_c, at most six decimation steps of √2, rates read against
  drawn bands with no fitted exponents or error bars. It is exact only for
  the diffusion model above.
- **Not that the closure holds.** The renormalized Hamiltonian staying in
  the family, a linear parameter map and an analytic G are assumed. A real
  RG step generates new couplings, and in the exact 1D Ising decimation
  the map K′ = ½ ln cosh 2K is not linear.
- **Not that this selects a coarse-graining.** The map C is given. The
  identity of step 3 says how much any map loses, and that a map whose
  coarse state determines the energy operators loses nothing. It does not
  say which maps are renormalizations.
- **Nothing about learning.** The metric measures distinguishability from
  a fixed amount of data. It is not a learning rate, and no training
  dynamics appear in the paper.

## Connections

The loss in step 3 is the coarse-graining analogue of the data-processing
inequality for Fisher information, written out for exponential families.
It gives [THEORY-202](THEORY-202.md)'s "stated target" one concrete form: keep the
singular Fisher metric of the bare couplings. Under that target the
non-interacting construction in [THEORY-202](THEORY-202.md) fails, since its coarse
variables carry no information about θ. The identity map passes,
though, so the target is necessary, not sufficient. [THEORY-194](THEORY-194.md) selects
coarse variables by their mutual information with the far environment,
which is a different quantity from the Fisher information about the
couplings measured here. Whether the coarse-graining that maximizes the
former keeps the singular part of the latter has not been tested. On
[QUESTION-217](../questions.d/QUESTION-217.md), the contraction factors (the generalized eigenvalues
of g̃ relative to g, which do not depend on the parametrization) order
parameter directions from coarse to fine along a chain of nested
coarse-grainings. In the diffusion case that order is by cumulant order.
That is an order of relevance tied to refinement, not an order of
acquisition.
