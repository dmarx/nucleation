---
number: 777
status: Proposed
formerly:
- THEORY-tmpzyxwe
promote_when: >-
  A computation of the Fisher spectrum of the bare couplings from decimated
  spins of the square-lattice Ising model at its critical point that
  reports, for each eigenvalue, a per-step decay factor with a statistical
  error and the noise floor of the estimator, at two or more lattice sizes,
  and finds the field and temperature eigenvalues constant within error
  until b^n nears the system size and the others decaying at factors
  matching b^(2y−d) for named irrelevant exponents y. An exact computation
  on a lattice small enough to enumerate would serve for the first few
  steps. A further scaling argument does not settle it, since the claim at
  issue is what the numbers are.
title: 'In Monte Carlo on a 64×64 periodic square-lattice Ising model at its critical point, parametrized by a field and 13 nearby couplings and observed only through the spins left after n checkerboard decimations (b = √2 per step, n ≤ 6), the two Fisher eigenvalues along the field and the gradient of T_c stay within a factor of about two of their microscopic values, while the others fall by up to about six decades, in three groups whose decay is consistent with b^(2y−d) per step for y = 0, −2 and −4'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-1018. This is the paper's Fig. 3 and
    supplement §§VI–VII, the numerics on which LIT-1254's Eq. 21 rests.
    The decay factors were read from the rendered figure by the reader;
    the paper reports none, and no error bars.
tags:
- information-geometry
- natural-sciences
date: '2026-10-20'
source:
- LIT-1299
summary: >-
  Machta, Chachra, Transtrum and Sethna (2013), [LIT-1299](../literature.d/LIT-1299.md), Fig. 3, read
  in [NOTE-1018](../notes.d/NOTE-1018.md). One lattice size, one temperature, at most six steps of
  b = √2 (so b^n ≤ 8), no error bars, and no fitted rates. The groups and
  their rates are bands the authors drew. The value y = 0 is not an
  operator of the 2D Ising model: it is the rate at which any direction
  without singular support loses information as sites are discarded. The
  caption's rate 2^(−d−y) disagrees with the bands and with the
  supplement's b^(2y−d).
---

# THEORY-777: In Monte Carlo on a 64×64 periodic square-lattice Ising model at its critical point, parametrized by a field and 13 nearby couplings and observed only through the spins left after n checkerboard decimations (b = √2 per step, n ≤ 6), the two Fisher eigenvalues along the field and the gradient of T_c stay within a factor of about two of their microscopic values, while the others fall by up to about six decades, in three groups whose decay is consistent with b^(2y−d) per step for y = 0, −2 and −4

## Source

Machta, Chachra, Transtrum and Sethna (2013), *Science* 342:604,
[LIT-1299](../literature.d/LIT-1299.md), arXiv:1303.6738v1, read in full in [NOTE-1018](../notes.d/NOTE-1018.md): main
text Fig. 3, supplement §IV (the model), §V (the metric before
coarsening, Fig. 4), §VI (after coarsening, Eqs. 32–41) and §VII (the
compatible Monte Carlo).

## What was actually shown

**The computation.** H = Σ θ_αβ Φ_αβ + θ_h Φ_h with Φ_αβ = Σ s_ij
s_{i+α, j+β} over nearby offsets and Φ_h = Σ s_ij, evaluated on the
ordinary Ising line (θ₀₁ = θ₁₀ = J, the rest 0, h = 0) at J_c. The data
at level n are the spins on the n-th checkerboard sublattice, still drawn
from the full-lattice ensemble. The coarse metric is
g^n = Cov({Φ_μ}, {Φ_ν}), with {Φ} the mean of Φ conditional on the
observed sublattice (Eq. 34; the same identity as [THEORY-742](THEORY-742.md), step 2). It
is estimated from M = 10⁴–10⁵ Wolff configurations and, for each, a
sub-ensemble drawn by compatible Monte Carlo with the observed spins
frozen, using products over distinct replicas to remove the bias
(Eqs. 36, 46). At level 1 the conditional means are exact, because the
free spins are conditionally independent (Eq. 42).

**The result, as plotted.** The field eigenvalue sits near 10⁵ at every
level. The ∇T_c eigenvalue sits near 4 × 10³ and falls to about 2 × 10³ by
step 6. The other eigenvalues start clustered between about 3 and 40 and
are coloured into three groups, with shaded bands. Read from the
rendered figure, the bands fall by about 0.27, 0.87 and 1.35 decades per
step, against 0.30, 0.90 and 1.51 for 2^{y−1} with y = 0, −2, −4. The
lowest group leaves the plot after step 4, near 10⁻⁵.

**The explanation offered.** Supplement Eqs. 29–41. Split F into singular
and analytic parts in scaling variables u_α with u′ = b^{y_α} u. The
singular part of the metric is ∼ A ξ^{2y−d}, the analytic part ∼ A, so
near criticality only directions with 2y ≥ d are dominated by the
singular part (the field, y = 15/8, and temperature, y = 1 = d/2,
logarithmically). After n steps the singular part is unchanged and the
analytic part is ∼ A b^{n(2y−d)}, because the matrix it multiplies
"should be smoothly varying" and its eigenvalues "should continue to take
a characteristic value". This is a scaling argument. It also assumes
(Eqs. 37–40) that the coarse metric in the bare coordinates is the
Hessian of a coarse free energy, which needs the closure and linear
parameter map that [THEORY-742](THEORY-742.md) states.

**What could have come out otherwise.** The field and temperature
eigenvalues could have fallen with the rest. The others could have
fallen at one common rate (b^{−d}, the rate of losing sites) rather than
at separated ones. Neither happens in the figure.

## What this does not say

- **Not a measured rate.** No exponent is fitted and no error is
  reported. The rates are those of bands drawn by the authors, and the
  assignment of each eigenvalue to a band is by colour. The agreement is
  "quantitative", in the supplement's word, only by eye.
- **Not the 2D Ising irrelevant spectrum, as such.** The bands are
  labelled y = 0, −2, −4, "assuming that our variables project onto
  irrelevant and marginal scaling variables" with those dimensions, with
  the authors citing Caselle et al. (2002) for −2 and −4. The 2D Ising
  model has no marginal operator; a direction with no singular part and
  no RG scaling loses information at b^{−d} per step simply because half
  the sites are dropped, and the y = 0 band is that rate.
- **Not more than one size or temperature.** At T_c on a 64×64 lattice,
  ξ is the system size, and six steps reach an 8×8 lattice. The slight
  fall of the ∇T_c eigenvalue at steps 5 and 6 is consistent with the
  logarithmic case and with b^n nearing L. Nothing is shown off
  criticality.
- **Not a noise-free spectrum.** Eigenvalues ten decades below the
  largest are reported from Monte Carlo covariances with no estimate of
  the estimator's floor, and the sub-ensemble sizes are not given.
- **Not that relevant directions are exactly those that do not
  contract.** The main text says so. The supplement says that relevant
  directions with 0 < 2y < d contract like irrelevant ones. The 2D Ising
  model has none, so the figure cannot test the line.
- **The caption's rate is wrong.** "Further eigenvalues shrink by a
  factor of 2^{−d−y_i} in each step" gives 1/4, 1 and 4 for y = 0, −2, −4.
  The bands and the supplement's Eq. 41 give b^{2y−d} = 2^{y−d/2}, that is
  1/2, 1/8 and 1/32.

## Connections

This is the numerical support that [LIT-1254](../literature.d/LIT-1254.md) cites for its Eq. 21
("our confidence in the result comes from the numerical work in
Ref. [15]"), whose derivation it repeats in Fisher-metric language. The
proved part of that later paper is [THEORY-742](THEORY-742.md); this entry is the
empirical part it leans on. The same paper's diffusion half is
[THEORY-774](THEORY-774.md), which is proved. On [QUESTION-217](../questions.d/QUESTION-217.md), the contraction order
here is an order of relevance to the bare couplings along a refinement
chain of sublattices. It says nothing about acquisition.
