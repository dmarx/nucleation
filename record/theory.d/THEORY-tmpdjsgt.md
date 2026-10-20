---
status: Proposed
promote_when: >-
  A rerun of the two-scale Lorenz 96 test at the paper's parameters
  (ε = 0.5, K = 18, J = 20, F = 10, h_x = −1, h_y = 1), by the record or
  another group, that fits the discrepancy NARMAX with a structure chosen by
  a rule fixed before scoring, and reports the Kolmogorov–Smirnov distance
  of x₁ and the lead time at anomaly correlation 0.6 against the full system
  and against the polynomial-plus-AR(1) closure, at δ = 0.05 at least. A
  rerun whose model orders were tuned on the scored statistics, or a
  comparison read off figures, does not settle it. The promotion audit's
  one-study rule (ADR-047 v3) may also apply, since the title claims no more
  than this study measured.
title: 'In two-scale Lorenz 96 without time-scale separation (ε = 0.5, K = 18, J = 20, F = 10), a discrete-time closure for each resolved variable that fits the one-step discrepancy of a fourth-order Runge–Kutta step as a NARMAX series, with one autoregressive lag, at most two lags of the resolved variable and at most one moving-average term, reproduces the mean, spread, distribution, autocorrelation and neighbour cross-correlation of x₁ (Kolmogorov–Smirnov distance 0.005) and, with observations every 0.05, extends the 20-member ensemble forecast lead time at anomaly correlation 0.6 from 2 to 4 time units over a polynomial-plus-AR(1) closure; the model structure was chosen by trial and error, differs between the two observation spacings, and carries no error bound'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-tmpejcu2. The numbers are the paper's
    Tables 2–3 and Figs. 1–2, the figures read from the rendered arXiv
    pages, which match the published text on PMC. Proposed because the
    evidence is one numerical study whose model orders were selected by
    trial and error against the same long-run statistics that are then
    reported, with no held-out selection rule, and because the forecast
    comparison is read from plotted curves.
tags:
- probabilistic-modeling
- complex-systems
- natural-sciences
date: '2026-10-20'
source:
- LIT-tmp6gimq
answers:
- QUESTION-222
summary: >-
  Chorin and Lu (2015), [LIT-tmp6gimq](../literature.d/LIT-tmp6gimq.md), read in [NOTE-tmpejcu2](../notes.d/NOTE-tmpejcu2.md). A data-driven
  closure with one or two steps of discrete memory, plus one moving-average
  innovation, is enough on this test to reproduce the resolved statistics
  and to double forecast skill against a memoryless-in-x closure. It is the
  record's first evidence that a short discrete memory suffices in a
  chaotic system with no scale gap. It is one system, the structure was
  tuned, and there is no bound, so it does not give the controlled
  prediction error [QUESTION-222](../questions.d/QUESTION-222.md) asks for.
---
<!-- inactive-ok-file: THEORY-747 — Proposed; the analogous empirical account from the turbulence reading -->

# THEORY-tmpdjsgt: In two-scale Lorenz 96 without time-scale separation (ε = 0.5, K = 18, J = 20, F = 10), a discrete-time closure for each resolved variable that fits the one-step discrepancy of a fourth-order Runge–Kutta step as a NARMAX series, with one autoregressive lag, at most two lags of the resolved variable and at most one moving-average term, reproduces the mean, spread, distribution, autocorrelation and neighbour cross-correlation of x₁ (Kolmogorov–Smirnov distance 0.005) and, with observations every 0.05, extends the 20-member ensemble forecast lead time at anomaly correlation 0.6 from 2 to 4 time units over a polynomial-plus-AR(1) closure; the model structure was chosen by trial and error, differs between the two observation spacings, and carries no error bound

## Source

Chorin and Lu (2015), *PNAS* 112(32):9804–9809, [LIT-tmp6gimq](../literature.d/LIT-tmp6gimq.md), read in full
in [NOTE-tmpejcu2](../notes.d/NOTE-tmpejcu2.md). The closure is the paper's Eqs. 5–7 and 10. The results
are its Tables 2–3 and Figs. 1–2.

## What was actually shown

**The system.** dx_k/dt = x_{k−1}(x_{k+1} − x_{k−2}) − x_k + F + z_k, with
z_k = (h_x/J)Σ_j y_{j,k}, and εdy_{j,k}/dt = y_{j+1,k}(y_{j−1,k} − y_{j+2,k}) −
y_{j,k} + h_y x_k, cyclic indices, at ε = 0.5, K = 18, J = 20, F = 10,
h_x = −1, h_y = 1. At ε = 0.5 the 360 eliminated variables are not fast.
Data: the full system integrated by RK4 at step 0.001 and observed at
spacing δ = 0.01 or δ = 0.05, N = 5 × 10⁵ observations each.

**The closure.** x^{n+1} = x^n + δR_δ(x^n) + δz^{n+1}, where R_δ is one RK4
step of the resolved equations with the unresolved term dropped, and
z^{n+1} = Φ^{n+1} + ξ^{n+1} with ξ iid Gaussian. Each component's Φ uses
only its own past and that of its own x_k (Eq. 10). The orders fitted:

- δ = 0.01: (p, r, s, q) = (1, 2, 0, 1), d_x = 1, so
  Φ^n = μ + a₁z^{n−1} + b x^{n−1} + b′ x^{n−2} + d₁ξ^{n−1}, with
  a₁ = 0.9782, b = −0.1271, b′ = 0.1132, d₁ = 0.9997, μ = 0.0115,
  σ² = 0.0004.
- δ = 0.05: (p, r, s, q) = (1, 1, 1, 0), (d_x, d_R) = (3, 1), so
  Φ^n = μ + a₁z^{n−1} + cubic in x^{n−1} + c R_δ(x^{n−1}), with
  a₁ = 0.8879, cubic coefficients −0.0712, −0.0002, 0.0002, c = −0.0084,
  μ = 0.0556, σ² = 0.0284.

The parameters are maximum-likelihood (least-squares) estimates given the
structure; the structure was chosen "by trial and error" so that the
long-run mean and autocorrelation fit, the estimates converge with more
data, and they respect the system's symmetry.

**The results, which could have come out otherwise.**

| | δ = 0.01 mean | sd | KS D | δ = 0.05 mean | sd | KS D |
|---|---|---|---|---|---|---|
| Lorenz 96 | 2.4506 | 3.5230 | | 2.3978 | 3.5222 | |
| POLYAR | 2.5335 | 3.3807 | 0.0183 | 2.6031 | 2.8564 | 0.0747 |
| NARMAX | 2.4113 | 3.5270 | 0.0055 | 2.4293 | 3.5402 | 0.0049 |

In Fig. 1, at δ = 0.05, POLYAR's pdf of x₁ is visibly bimodal where the
true one is not, and its autocorrelation and x₁–x₂ cross-correlation
overshoot in amplitude and drift in phase over ten time units. NARMAX's
curves lie on the true ones. At δ = 0.01 both closures are close. In
Fig. 2, over 10,000 ten-unit trajectories and ensembles of 1, 5 and 20,
at δ = 0.05 NARMAX has the lower RMSE and the higher anomaly correlation at
every lead time and ensemble size; with 20 members the anomaly correlation
falls below 0.6 at about 4 time units against about 2 for POLYAR. At
δ = 0.01 the gain is small and not uniform: NARMAX is better up to a lead
time of about 2.5, but beyond about 2.7 POLYAR's 5- and 20-member RMSE
curves lie slightly below NARMAX's (about 14.3 against 14.7 at lead 5),
though NARMAX keeps the higher anomaly correlation at equal ensemble size.
The caption's "NARMAX has smaller RMSE … than the POLYAR" is therefore not
true at every lead time for δ = 0.01 (read from the figure at 250 dpi).

The memory used is short in the variables kept: the closure looks back one
step in z, one or two in x, and one in ξ, that is 0.01 to 0.05 time units.
But the autoregressive and moving-average terms make its implied
dependence on the past of x non-zero at every lag, decaying geometrically.

## What this does not say

- **Not that a finite discrete memory suffices in general,** nor in this
  system with a stated error. There is no bound, no study of how the error
  moves with the orders, and no out-of-sample rule for choosing them. The
  statistics used to choose the structure are among those reported.
- **Not that the closure approximates the Mori–Zwanzig memory.** The paper
  draws the link by analogy only ([NOTE-tmpejcu2](../notes.d/NOTE-tmpejcu2.md)). The fitted Φ is whatever
  predicts z best within the chosen family; it also absorbs the RK4
  scheme's own error at step δ, which the paper intends.
- **Not a property of the system independent of the sampling.** The fitted
  structure differs between δ = 0.01 and δ = 0.05, and the coefficients
  are tied to the integrator. What has finite memory is the sampled,
  discretized process, not the flow.
- **Not a comparison with the strongest alternatives.** The baseline is
  Wilks's POLYAR, whose noise has no memory of x. Conditional Markov chain
  closures are excluded because they need exact observations of z.
- **Not more than x₁ and its neighbour.** The figures show one component
  and one cross-correlation; translation symmetry makes this
  representative of single-site statistics, not of spatial patterns.

## Connections

[THEORY-760](THEORY-760.md) and [THEORY-747](THEORY-747.md) are the continuous-time analogue from
turbulence: a finite set of memory coordinates whose length is fitted and
whose error is not bounded. This account is the discrete, data-driven
version of the same shape, in a chaotic system without a scale gap. The
record's linear check in [NOTE-tmpejcu2](../notes.d/NOTE-tmpejcu2.md) shows the mechanism by which a few
lags can be exact: a partially observed linear Gaussian VAR(1) is an ARMA
process whose order matches the rank of its MZ memory kernels ([CLAIM-389](../claims.d/CLAIM-389.md),
[NOTE-989](../notes.d/NOTE-989.md)), so a memory non-zero at every lag is carried exactly by
finitely many coordinates. [THEORY-tmpcfuar](THEORY-tmpcfuar.md) is the opposite case: where the
eliminated variables are fast and contracting, no memory is needed at all.
Here ε = 0.5, so that theorem's hypothesis fails and memory helps.
