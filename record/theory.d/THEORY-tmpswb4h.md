---
status: Active
title: 'The finite-memory Mori–Zwanzig closure that Parish and Duraisamy take from Stinis, truncated at order m with one trapezoidal sub-interval and constant memory lengths, is a finite-dimensional Markovian augmentation: m + 1 auxiliary variables per resolved mode, each relaxing at rate 2/τ; at first order it replaces the memory integral by the kernel 2e^{−2s/τ₀} acting on the first-order term, which tends to τ₀ times that term, the t-model with t replaced by τ₀, when τ₀ is short against the resolved dynamics; its kernel is twice the true one at zero lag for every τ₀, so it is not exact even where the true memory is a single exponential, and nothing in the construction bounds its error'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-tmpg06if. The closure is the paper's Eq. 26
    (with Eqs. 21–22 and the trapezoidal step between them), credited
    there to Stinis. Its solution as an exponential kernel, the
    quasi-steady limit, the zero-lag amplitude and the linear test are the
    record's, re-derived below step by step and checked numerically, which
    meets the condition for Active under ADR-047 v2. The empirical
    performance of the closure is a separate account, THEORY-tmp4ou43.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
source:
- LIT-tmpvihtb
answers:
- QUESTION-tmpxapb2
summary: >-
  Parish and Duraisamy (2017), [LIT-tmpvihtb](../literature.d/LIT-tmpvihtb.md), read in [NOTE-tmpg06if](../notes.d/NOTE-tmpg06if.md). The
  finite-memory closure turns the Mori–Zwanzig memory integral into
  auxiliary ordinary differential equations, so the reduced model is the
  resolved variables plus finitely many memory coordinates: the shape of
  augmentation [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md) asks about. But the truncation drops the
  next auxiliary term without a bound, the memory length is fitted, and
  the kernel's form is fixed by the quadrature, not by the eliminated
  dynamics. It is an augmentation with uncontrolled error, not the
  controlled one the question asks for.
---
<!-- inactive-ok-file: THEORY-tmp4ou43 — Proposed; the empirical companion account from the same reading -->
<!-- inactive-ok-file: THEORY-257 CLAIM-327 — Proposed; the record's criteria this account is set beside, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpai9kc LIT-tmple6xy — Deferred; Chorin, Hald and Kupferman, registered unread, cited as open -->

# THEORY-tmpswb4h: The finite-memory Mori–Zwanzig closure that Parish and Duraisamy take from Stinis, truncated at order m with one trapezoidal sub-interval and constant memory lengths, is a finite-dimensional Markovian augmentation: m + 1 auxiliary variables per resolved mode, each relaxing at rate 2/τ; at first order it replaces the memory integral by the kernel 2e^{−2s/τ₀} acting on the first-order term, which tends to τ₀ times that term, the t-model with t replaced by τ₀, when τ₀ is short against the resolved dynamics; its kernel is twice the true one at zero lag for every τ₀, so it is not exact even where the true memory is a single exponential, and nothing in the construction bounds its error

## Source

Parish and Duraisamy (2017), *Physical Review Fluids* 2: 014604,
[LIT-tmpvihtb](../literature.d/LIT-tmpvihtb.md), read in full in [NOTE-tmpg06if](../notes.d/NOTE-tmpg06if.md) from arXiv:1611.03311v2. The
closure is the paper's §II.B, Eqs. 20–26, which it credits to Stinis
(2006, 2012). The derivations below are the record's.

## What was actually shown

**Setting.** The paper's Mori–Zwanzig identity (its Eq. 10) splits the
evolution of a resolved variable φ_j into a Markovian term, a noise term
and the memory integral

M_j(t) = ∫₀ᵗ e^{(t−s)L} P L e^{sQL} Q L φ₀ⱼ ds.

Its projection is P f(φ̂₀, φ̃₀) = f(φ̂₀, 0): the unresolved modes are set to
zero (a Gaussian initial density in the zero-variance limit). Write
g_j^{(m)}(t) = e^{tL} P L (QL)^{m+1} φ₀ⱼ, which needs only the resolved
state at time t; g^{(0)} is the "first-order term" (its Eq. 31 for
Burgers, Eq. 36 for Navier–Stokes).

**Step 1: the closure.** Define w_j^{(0)}(t) as M_j restricted to lags in
[0, τ₀] (its Eq. 21, m = 0). Differentiating (its Eq. 22, with τ₀
constant) gives

dw^{(0)}/dt = g^{(0)}(t) − B(t) + w^{(1)}(t),

where B(t) = e^{(t−τ₀)L} P L e^{τ₀QL} Q L φ₀ⱼ is the integrand at the far
end of the window, which needs the orthogonal dynamics, and w^{(1)} is the
same construction one order up. The trapezoidal rule on [t − τ₀, t] gives
w^{(0)} ≈ (τ₀/2)(g^{(0)} + B), so B ≈ 2w^{(0)}/τ₀ − g^{(0)}. Substituting,

dw^{(0)}/dt = −(2/τ₀) w^{(0)} + 2 g^{(0)}(t) + w^{(1)}(t),

the paper's Eq. 26 at m = 0. The same steps one order up give Eq. 26 for
each m, with τ_m and g^{(m)}. The hierarchy is closed by setting
w^{(m+1)} = 0.

**Step 2: it is a finite Markovian augmentation.** After truncation, the
reduced model is dφ̂/dt = R̂(φ̂) + w^{(0)} together with m + 1 linear
relaxation equations, one per order, for each resolved mode. Every
right-hand side depends only on the current resolved state and the
current auxiliary variables. So the state (φ̂, w^{(0)}, …, w^{(m)}) of
dimension (m + 2)N evolves Markovianly. That is the "coarse variable plus
k memory coordinates" of [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md), with k = (m + 1)N.

**Step 3: the kernel it implies.** At m = 0 with w^{(1)} = 0 and
w^{(0)}(0) = 0 (the paper's initially resolved runs), the relaxation
equation solves to

w^{(0)}(t) = 2 ∫₀ᵗ e^{−2(t−s)/τ₀} g^{(0)}(s) ds.

So the closure replaces the true memory by an exponential kernel of decay
rate 2/τ₀ and amplitude 2 applied to the history of the first-order term.
The kernel's total weight is ∫₀^∞ 2e^{−2u/τ₀} du = τ₀.

**Step 4: the quasi-steady limit is a rescaled t-model.** If g^{(0)}
changes little over a time τ₀, then w^{(0)}(t) → τ₀ g^{(0)}(t) for
t ≫ τ₀. The paper's t-model (its Eq. 20) is w = t g^{(0)}(t). The
first-order finite-memory model therefore relaxes to the t-model with the
elapsed time t replaced by the memory length τ₀. That is consistent with
the paper's finding that the t-model removes too much energy at late
times: its coefficient grows without limit, while this one saturates. The paper
does not draw this connection, though its Table 1 lists the t-model's
constant as "τ₀ = t".

**Step 5: the zero-lag amplitude is wrong for every τ₀.** The exact
memory integrand at lag zero is e^{tL} P L Q L φ₀ⱼ = g^{(0)}(t), with
coefficient 1. The closure's kernel at lag zero is 2. No choice of τ₀
changes this, because the factor 2 comes from the trapezoidal weights,
not from τ₀.

**Step 6: a linear test.** For ẋ = a₁₁x + a₁₂y, ẏ = a₂₁x + a₂₂y with
a₂₂ < 0 and y(0) = 0, the projection gives g^{(0)} = a₁₂a₂₁ x(t), and the
exact memory is a₁₂a₂₁ ∫₀ᵗ e^{a₂₂s} x(t − s) ds: one exponential, with
amplitude 1 and rate |a₂₂|. The augmentation w′ = a₂₂w + a₁₂a₂₁x (w is
a₁₂y) is exact with one coordinate. The closure's kernel is
2a₁₂a₂₁e^{−2s/τ₀}. It matches the exact kernel's total weight when
τ₀ = 1/|a₂₂|, and then decays at twice the true rate. No τ₀ matches both
amplitude and rate. Checked numerically with (a₁₁, a₁₂, a₂₁, a₂₂) =
(−0.5, 1, −2, −3) and x(0) = 1 over t ∈ [0, 6]. The exact one-coordinate
augmentation has zero error. The finite-memory closure's maximum error in
x is 4.7 × 10⁻² at τ₀ = 1/3, and 3.5 × 10⁻² at its best τ₀ ≈ 0.30. The
t-model's is 1.2 × 10⁻¹. A Markovian closure with the exact kernel's
total weight, x′ = (a₁₁ + a₁₂a₂₁/|a₂₂|)x, gives 9.8 × 10⁻².

What could have failed: the closure could have reproduced the exact
kernel in the linear case where one memory coordinate suffices, and Step 6
would then have been a check that its form is right. It does not. Its
form is fixed by the quadrature.

## What this does not say

- **Not that the closure's error is bounded.** The paper justifies
  dropping w^{(m+1)} only "if the support or magnitude of the integrand
  decreases with the repeated application of QL", and gives no bound. The
  trapezoidal error is stated as O(τ₀²), with no constant. τ₀ is fitted to DNS for Burgers and set to 0.1 for
  Navier–Stokes. So this is a Markovian augmentation without the
  controlled prediction error [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md) asks for.
- **Not that the true memory has finite support.** The paper's linear
  analysis (its Eqs. 15–19) shows that the memory integrand decays like
  e^{Λs} for the eigenvalues Λ of the unresolved block. Exponential decay
  is not finite support. "Finite memory" is an approximation the paper
  motivates, not a property it shows.
- **Not that it is a statistical closure.** Under the zero-variance
  projection, P is evaluation at φ̃ = 0. Then P commutes with every
  function of the state, so the paper's "casual" commuting of the
  nonlinear Markovian term is exact, and the projected equation is just
  the full dynamics started from a fully resolved state. Nothing is
  averaged. The closures approximate one deterministic trajectory's
  memory. Applied to flows whose unresolved modes are not zero at the
  start (the paper's isotropic turbulence and channel runs), they are used
  outside the setting they were derived in.
- **Nothing about which coarse variable to use.** The cutoff is a
  Fourier wavenumber chosen by the modeller, and the paper calls the
  memory "numerical memory, as opposed to physical memory", whose length
  depends "both on the physics of the problem at hand and the level of
  coarse-graining".

## Connections

- **[QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md): answers in part.** It asks for a class in which
  the reduced process has a finite Markovian augmentation with bounded
  prediction error, with k and the error in terms of the eliminated
  dynamics' spectrum. This shows the turbulence literature's working
  answer has the shape asked for (k = (m + 1)N memory coordinates) and
  lacks the bound, and that its kernel form comes from a quadrature rule,
  not from the spectrum. A5's linear example in the question is Step 6's
  system. There the exact augmentation is trivial (keep y), and the
  finite-memory closure still misses it.
- **The augmenting coordinate is the subgrid force.** w^{(0)} is the
  closure's estimate of i k τ^{SGS}, the subgrid force on each resolved
  mode (the paper's Fig. 3 caption). In physical space (its Appendix C,
  Eq. 46, pressure neglected), the divergence of the subgrid stress
  becomes a field that relaxes at rate 2/τ₀, driven by the resolved field
  and the Leonard stress. A5's "additional internal memory coordinate" is
  here a named physical quantity, the stress the unresolved scales exert.
- **[THEORY-257](THEORY-257.md).** Dynamical independence conditions on the coarse
  variable's own history, so a coarse variable with memory need not fail
  it. This closure gives one way such a history could be summarised by a
  finite state. Whether the record's criteria should be applied to φ̂ or
  to (φ̂, w) is what [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md) asks, and this account does not
  decide it.
- **Chorin, Hald and Kupferman** ([LIT-tmpai9kc](../literature.d/LIT-tmpai9kc.md), [LIT-tmple6xy](../literature.d/LIT-tmple6xy.md), registered
  unread) are the optimal-prediction source of the projection and of the
  t-model. Their readings may say whether a bound exists for any class.
