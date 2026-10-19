---
status: Active
title: 'In a linear-in-parameters model with Gaussian noise and a Gaussian prior, the evidence is exactly the best-fit likelihood times an Occam factor set by the posterior curvature, and when the design grows linearly with n that factor costs (k/2) log n'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-087 at the owner's direction, as the follow-up to
    the owner's promotion audit of 2026-10-19, and filed Active. The audit
    said THEORY-087's regular half "is established in the sources". On
    checking, it is established exactly only for this case. MacKay's
    factorization is exact for linear-in-parameters models with Gaussian
    noise and prior (NOTE-471: "exact for the linear models used"), and an
    approximation otherwise. Grünwald & Roos (NOTE-760) and Watanabe
    (NOTE-473) cite the general regular asymptotics without proving them.
    This THEORY holds the exact case. The (k/2) log n step is the record's
    algebra on MacKay's formula, written out below. THEORY-087 extends
    it, and its promote_when now names the general regular case as well.
tags:
- model-comparison
- probabilistic-modeling
- mathematics
- anthology-candidate
date: '2026-10-19'
source:
- LIT-623
summary: >-
  MacKay (1992), [LIT-623](../literature.d/LIT-623.md), Eqs. 5–6 with Eqs. 16 and 19–20, read in
  [NOTE-471](../notes.d/NOTE-471.md): for y = Φw + noise with Gaussian noise of precision β and the
  prior w ~ N(0, α⁻¹I) on k weights, the posterior is exactly Gaussian, so
  the evidence is exactly P(D|w_MP) times the Occam factor
  P(w_MP)(2π)^{k/2} det^{-1/2}A, with A = αI + βΦᵀΦ. If ΦᵀΦ/n converges to
  a positive-definite matrix and w_MP stays bounded, the log Occam factor
  is −(k/2) log n + O(1). Exact for this model class only. The general
  regular case and the singular case are [THEORY-087](THEORY-087.md), which is Proposed.
extended_by:
- THEORY-087
---
<!-- inactive-ok-file: THEORY-087 — Proposed; the general and singular account this case was split from and that extends it, cited as open -->

# THEORY-tmp60l2i: In a linear-in-parameters model with Gaussian noise and a Gaussian prior, the evidence is exactly the best-fit likelihood times an Occam factor set by the posterior curvature, and when the design grows linearly with n that factor costs (k/2) log n

## Source

MacKay (1992), [LIT-623](../literature.d/LIT-623.md), §2 (Eqs. 5–6), the linear interpolants of §3
(Eqs. 7–11, 16, 19–20) and the Occam hill of §6, read in [NOTE-471](../notes.d/NOTE-471.md), whose
claim C1 is "strong under the Gaussian approximation (exact for the linear
models used)".

## What was actually shown

Take y(x) = Σ_h w_h φ_h(x) with k weights, n observations with Gaussian
noise of precision β, and a quadratic regularizer, which is the prior
w ~ N(0, α⁻¹I). Write Φ for the n × k design matrix. The negative log
posterior is quadratic in w, with Hessian A = αI + βΦᵀΦ. So the posterior is
exactly Gaussian, and the Gaussian integral gives exactly

log P(D | α, β) = log P(D | w_MP) + log [P(w_MP) (2π)^{k/2} det^{-1/2} A].

The second term is MacKay's Occam factor, "the ratio of the posterior
accessible volume of H's parameter space to the prior accessible volume"
(Eq. 6). For this model class it is not an approximation (Eqs. 16, 19–20).

**The large-n form, by the record's algebra.** Suppose ΦᵀΦ/n → Σ, positive
definite. Then log det A = log det(n(βΦᵀΦ/n + (α/n)I)) =
k log n + log det(βΣ) + o(1). And log P(w_MP) = (k/2) log(α/2π) −
(α/2)‖w_MP‖², which is O(1) when w_MP stays bounded, as it does in
probability when the data come from the model with a fixed weight vector.
So the log Occam factor is −(k/2) log n + O(1). The curvature of the
posterior sets the penalty, and its determinant grows as n^k. MacKay sees
the scaling in his polynomial fits, where the right side of the Occam hill
falls as "k log N" (§6).

The derivation could have gone otherwise in two places. A design whose
ΦᵀΦ grew more slowly than n in some direction would give that direction a
smaller cost. A posterior that was not Gaussian would make the formula an
approximation. Neither happens under these conditions.

## What this does not say

- **Anything for nonlinear models.** There the Occam factor formula is a
  Gaussian approximation, which MacKay justifies by the central limit
  theorem (footnote 2), and for degenerate maxima it needs correction. The
  general regular case, F = nL_n(ŵ) + (d/2) log n + O_p(1), is cited in
  the sources and not proved there. It and the singular case are
  [THEORY-087](THEORY-087.md).
- **That (k/2) log n is the whole story at finite n.** The finite-n
  factor charges ½ log(1 + λ_a/α) for each eigenvalue λ_a of βΦᵀΦ.
  Directions the data barely determine cost almost nothing, and
  γ = Σ λ_a/(λ_a + α) counts the ones that do (Eq. 23).
- **That α and β are integrated out.** The identity is for fixed α and β.
  MacKay sets them at the evidence maximum, which assumes a dominant peak
  (Eq. 18).
- **Anything about which model is true.** The evidence ranks models
  relative to the priors given.
