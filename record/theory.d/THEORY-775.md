---
number: 775
status: Active
formerly:
- THEORY-tmpn460i
title: 'With a Gaussian random-walk prior and an instantaneous unit-variance Gaussian encoder, the KL half of the evidence lower bound is the unordered slowness loss plus a constant; with a linear Gaussian encoder and decoder on whitened input, the bound is maximized on the span of the slowest SFA directions whose lag-one autocorrelation exceeds one half, with the basis inside that span unidentified, and on unwhitened input the maximizer is neither SFA''s subspace nor invariant to rescaling the input'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-1015. The KL identity (Eqs. 26–37) and the
    necessary condition VᵀV = WᵀĊW (Eq. 42, Appendix A) are the paper's,
    re-derived below with two slips corrected: the constant the paper
    cancels in Eq. 35, and the sign of the reconstruction error in Eq. 41.
    The optimum of the linear objective (Steps 4–6) is the record's; the
    paper does not derive it. Every step is re-derived and checked
    numerically (scratchpad script sfa_vi_check.py, reported below), which
    meets the condition for Active under ADR-047 v2.
tags:
- representation-learning
- probabilistic-modeling
- mathematics
date: '2026-10-20'
source:
- LIT-1296
- LIT-1249
answers:
- QUESTION-217
summary: >-
  Schüler and Wiskott (2025), [LIT-1296](../literature.d/LIT-1296.md), read in full in [NOTE-1015](../notes.d/NOTE-1015.md). The ELBO of a dynamical VAE with prior N(z_{t−1}, I) and encoder N(g(x_t), I) is Σ E log p(x_t | z_t) − ½Σ‖g(x_{t−1}) − g(x_t)‖² − (T − 1)d/2, an exact identity. For linear Gaussian encoder and decoder on whitened input, the maximizer spans the bottom eigenvectors of the difference covariance with eigenvalue μ < 1, each scaled by (μ^{−1/2} − 1)^{1/2} and then rotated arbitrarily. So it recovers SFA's slow span, cut at lag-one autocorrelation ½, not SFA's features. On raw input it trades variance against slowness. It says nothing about nonlinear encoders, about predictive sufficiency, or about Turner and Sahani's model.
---
<!-- inactive-ok-file: LIT-1287 — Unavailable; the maximum-likelihood account this one is contrasted with, not read -->
<!-- inactive-ok-file: CLAIM-331 THEORY-257 — Proposed; entries this bears on, nothing here rests on their being settled -->

# THEORY-775: With a Gaussian random-walk prior and an instantaneous unit-variance Gaussian encoder, the KL half of the evidence lower bound is the unordered slowness loss plus a constant; with a linear Gaussian encoder and decoder on whitened input, the bound is maximized on the span of the slowest SFA directions whose lag-one autocorrelation exceeds one half, with the basis inside that span unidentified, and on unwhitened input the maximizer is neither SFA's subspace nor invariant to rescaling the input

## Source

Schüler and Wiskott (2025), "Slow Feature Analysis as Variational
Inference Objective", arXiv:2506.00580v1, [LIT-1296](../literature.d/LIT-1296.md), read in full in
[NOTE-1015](../notes.d/NOTE-1015.md). The model is §§4–5 (Eqs. 12–14, 19–20), the identity §6
(Eqs. 21–40), the linear case §7 (Eqs. 41–42) and Appendix A. SFA's
generalized eigenproblem and the lag-one identity are [THEORY-746](THEORY-746.md)'s, from
Wiskott and Sejnowski (2002), [LIT-1249](../literature.d/LIT-1249.md). Steps 4–6 are the record's.

## What was actually shown

**Model.** Observations x_1, …, x_T in ℝⁿ, latents z_t in ℝ^d. Prior
p(z_t | z_{t−1}) = N(z_{t−1}, I), a random walk with no decay (Eq. 13;
p(z_1) is left unstated). Forward model p_θ(x_{1:T} | z_{1:T}) =
Π p_θ(x_t | z_t), otherwise arbitrary (Eq. 14). Variational family
q(z_{1:T} | x_{1:T}) = Π q(z_t | x_t), q(z_t | x_t) = N(g(x_t), I) (Eqs.
19–20).

**Step 1, the KL identity (the paper's, corrected).** Because q
factorizes, KL(q ‖ p) = Σ_t E_q[log q(z_t | x_t) − log p(z_t | z_{t−1})]
for t ≥ 2, plus a boundary term KL(q(z_1 | x_1) ‖ p(z_1)) that the paper
does not write. The t-th term depends on z_{t−1} and z_t only, and these
are independent under q, so it is E_{z_{t−1}} KL(N(g(x_t), I) ‖
N(z_{t−1}, I)) (Eq. 33). For identity covariances
KL(N(m, I) ‖ N(m′, I)) = ½‖m − m′‖²: in Eq. 34 the terms
tr(Σ_p⁻¹Σ_q) − log(|Σ_q|/|Σ_p|) − d are d − 0 − d = 0. With
z_{t−1} ~ N(g(x_{t−1}), I), E‖z_{t−1} − g(x_t)‖² =
‖g(x_{t−1}) − g(x_t)‖² + d. So

  KL(q ‖ p) = ½ Σ_{t≥2} ‖g(x_{t−1}) − g(x_t)‖² + (T − 1)d/2 + boundary,

and the ELBO is Σ_t E_q log p_θ(x_t | z_t) minus this. The paper's Eq. 35
keeps a "− d" that the trace had already cancelled, and Eq. 36 cancels it
against the + d, so its Eq. 37 lacks the constant (T − 1)d/2. That does
not change any optimizer. A Monte Carlo check (d = 3, 4 × 10⁵ draws) gave
1.6212 against ½‖Δg‖² + d/2 = 1.6205 and the paper's ½‖Δg‖² = 0.1205.

**Step 2, the linear objective (the paper's, corrected).** Take
q(z | x) = N(Wᵀx + b, I) and p(x | z) = N(Vz + o, I), W ∈ ℝ^{n×k},
V ∈ ℝ^{n×k}. Then E_ε‖x − V(Wᵀx + b + ε) − o‖² = ‖x − x̃‖² + tr(VᵀV) with
x̃ = VWᵀx + Vb + o (Eqs. 46–54). Per sample, ignoring the edge terms,

  L/T = c − ½⟨‖x − x̃‖²⟩ − ½ tr(VᵀV) − ½ tr(WᵀĊW),

with Ċ = ⟨(x_t − x_{t−1})(x_t − x_{t−1})ᵀ⟩. The paper's Eq. 41 prints
+½Σ‖x_t − x̃_t‖²; its own Eq. 54 has the minus sign, which is right.

**Step 3, the necessary condition (the paper's).** Only o + Vb is
identified; at the optimum o + Vb = x̄ − VWᵀx̄ (Eq. 80). With centred data
and C = ⟨(x − x̄)(x − x̄)ᵀ⟩, the gradients vanish when
V(WᵀCW + I) = CW and CV − CWVᵀV − ĊW = 0. Multiply the first on the left
by Vᵀ and transpose: WᵀCV = (WᵀCW + I)VᵀV. Multiply the second on the
left by Wᵀ and substitute: VᵀV = WᵀĊW (Eq. 42). It is necessary, not
sufficient: the paper says the stationarity equations "are equivalent to"
it, which is too strong. A random W with V built to satisfy it gave
L/T = −3.35 against the optimum's 0.30 (two latents, whitened data).

**Step 4, the profile in W (the record's).** For fixed W the objective is
a concave quadratic in V, maximized at V* = CW(WᵀCW + I)⁻¹, leaving

  J(W) = −½ tr C + ½ tr((WᵀCW + I)⁻¹WᵀC²W) − ½ tr(WᵀĊW).

**Step 5, whitened input (the record's).** Let C = I and let
Ċ = Σ_i μ_i e_i e_iᵀ with μ_1 ≤ … ≤ μ_n. Write the thin SVD
W = U S Rᵀ, U with orthonormal columns u_i, S = diag(s_1 ≥ … ≥ s_k ≥ 0),
R orthogonal. Then WᵀW = RS²Rᵀ and the first trace is Σ s_i²/(1 + s_i²),
independent of U and R. The second is Σ s_i² u_iᵀĊu_i
= Σ_{j=1}^{k} (s_j² − s_{j+1}²) Σ_{i≤j} u_iᵀĊu_i, with s_{k+1} = 0. Each
coefficient is non-negative and, by Ky Fan's theorem, each inner sum is at
least μ_1 + … + μ_j, so the term is at least Σ s_i²μ_i, with equality at
u_i = e_i. So max J = const + ½ Σ_i max_{t≥0} [t/(1 + t) − μ_i t]. The
bracket is concave in t with derivative (1 + t)⁻² − μ_i, so
t* = μ_i^{−1/2} − 1 when μ_i < 1 and t* = 0 otherwise, with value
(1 − √μ_i)². Since t* decreases in μ, pairing the largest s with the
smallest μ is consistent. The maximizers are therefore

  W = [e_1 … e_k] diag(s_i*) Rᵀ, s_i* = (μ_i^{−1/2} − 1)^{1/2} for μ_i < 1, else 0,

for every orthogonal R. On whitened input Ċ is [THEORY-746](THEORY-746.md)'s matrix M, so
the e_i are SFA's slow features in order. For unit-variance features
μ_i = 2(1 − ρ_i), ρ_i the lag-one autocorrelation ([THEORY-746](THEORY-746.md), Step 8), so
μ_i < 1 is ρ_i > ½. Latent dimensions beyond that cut get zero weight.
The encoder mean R S Uᵀx is a rotation of scaled slow features, so its
coordinates are correlated (covariance RS²Rᵀ) and not ordered: the span is
identified, the features are not. Numerically (five AR(1) sources with
ρ = 0.95, 0.8, 0.6, 0.4, 0.1, orthogonally mixed, 2 × 10⁵ steps,
k = 4), BFGS on J found singular values (1.4674, 0.7673, 0.3374, 0),
equal to the predicted ones to four places, principal angles of 0° with
the three slowest SFA directions, and VᵀV − WᵀĊW of norm 3 × 10⁻⁹.

**Step 6, unwhitened input (the record's).** For a single input of
variance c and lag-one autocorrelation ρ, Ċ = 2c(1 − ρ), and with
u = w²c, J = ½cu/(1 + u) − (1 − ρ)u + const. Its slope at u = 0 is
c/2 − (1 − ρ), so the input is kept iff c > 2(1 − ρ). Rescaling the input
changes c and not ρ, so it can switch a feature on or off. SFA is
invariant to rescaling ([THEORY-746](THEORY-746.md), Step 7). With three independent AR(1)
sources (ρ = 0.95, 0.6, 0.3; variances 0.0025, 100, 1), SFA's slowest
direction is the first source, and the one-latent optimum of J is the
second, to within 0.024 in the first coordinate.

What could have failed. The KL term could have kept a dependence on the
encoder beyond its mean; with fixed unit covariances it cannot. The
linear optimum could have been SFA's ordered features, or a variance-
weighted mixture even on whitened input; it is neither: the span is
exactly SFA's, the basis is free, and a threshold appears that SFA does
not have.

## What this does not say

- **Not that variational SFA is SFA.** The authors say so ("does not
  lead to full equivalence"). Steps 5–6 make the gap exact in the linear
  case: the span is right only on whitened input, features with ρ ≤ ½ are
  dropped, and the basis is unidentified.
- **Not about nonlinear encoders.** Step 1 holds for any g. Steps 2–6
  are linear. The paper's §7 argument that the reconstruction term plays
  the role of SFA's decorrelation constraint is informal, and in the
  linear case it is wrong as stated: the optimal features are correlated
  whenever R is not the identity. What the reconstruction term enforces
  is a non-redundant span, not decorrelated outputs.
- **Not that slow latents are found rather than assumed.** The prior
  makes every latent coordinate an independent random walk, so in the
  model any set of latent coordinates is closed ([THEORY-733](THEORY-733.md) with A = I).
  That is an assumption, not a result about the data.
- **Not predictive sufficiency.** The encoder sees x_t only (Eq. 19).
  Nothing is shown about whether the features carry what the past says
  about the future of x.
- **Not Turner and Sahani's result.** Their model ([LIT-1287](../literature.d/LIT-1287.md)) has a
  decaying, ordered prior and is reported here only from this paper's two
  sentences of related work. The record's own derivation for the
  noise-free linear case of that kind of model is in [NOTE-1015](../notes.d/NOTE-1015.md).

## Connections

- **[QUESTION-217](../questions.d/QUESTION-217.md): answers in part.** In the linear whitened case the
  optimal spans for k and k + 1 latents nest, in slowness order, up to
  the cut at μ = 1, so slowness gives a refinement chain of spans, as in
  [THEORY-746](THEORY-746.md). Inside a span there is no order. Acquisition is not
  touched.
- **[THEORY-746](THEORY-746.md).** The same pencil, reached through a likelihood bound
  instead of a constrained minimum. The unit-variance constraint becomes
  the fixed encoder noise, which sets the scale s_i* and creates the
  threshold.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** The slowness here is written into the prior as the
  absence of decay. It cannot count as evidence that higher-level
  variables are slower.
- **[THEORY-733](THEORY-733.md), [THEORY-257](THEORY-257.md).** The latents are closed by construction.
  Whether the learned features are closed in the data is not addressed.
