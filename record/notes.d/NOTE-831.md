---
number: 831
status: Read
formerly:
- NOTE-tmp9vrtb
paper: LIT-931
title: 'Farrell & Ioannou — Generalized Stability Theory I'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the authors' own copy of the published article
    (users.uoa.gr/~pjioannou/papers/genstab1.pdf, linked from Ioannou's
    publication list at the University of Athens; 16 pages, J. Atmos.
    Sci. 53(14):2025–2040). The publisher's bronze copy at
    journals.ametsoc.org returned 403 to curl's default user agent on
    2026-10-14. Text extracted with pdftotext; equations (5)–(8), (32),
    (33) and (41)–(43), which the extraction garbled, were checked
    against page images. Every section, all twelve figures and both
    footnotes on discretization and the continuous spectrum were read.
date: '2026-10-14'
summary: >-
  For a linear system du/dt = Au with A non-normal, the eigenvalues fix
  only the t → ∞ behaviour. Growth over a finite time t is the largest
  singular value of e^{At}, bounded below by the fastest mode and at
  t → 0 set by the numerical abscissa, the top eigenvalue of (A + A†)/2.
  A system with every mode damped can amplify a perturbation a
  hundredfold, and its forced and stochastic responses exceed those of
  the normal system with the same spectrum.
---
<!-- inactive-ok-file: CLAIM-186 — Proposed; the claim this reading bears on, open -->
<!-- inactive-ok-file: THEORY-323 — Proposed; the account this reading files -->

# NOTE-831: Farrell & Ioannou — Generalized Stability Theory I

## Contribution

The paper collects the non-modal results of the preceding decade into one
stability theory for time-independent linear operators. Modal theory
becomes its t → ∞ limit. The finite-time, short-time and forced
behaviour, which eigenvalues do not give when the operator is non-normal,
comes from the singular value decomposition of the propagator and of the
resolvent. The paper says it organises "recent advances into a
systematic stability theory" (§5). Most of the results are earlier, many
of them the authors' own, and it is a synthesis with worked examples
rather than a source of new theorems.

## Key insight

Eigenvalues tell you what wins in the end, not what happens on the way.
When the eigenvectors of A are not orthogonal, a combination of decaying
modes can grow for a long time before the slowest mode takes over, and
the perturbation that grows most is not a mode at all. The right object
is the propagator e^{At} over the interval of interest. Its singular
vectors are the optimal perturbations and its norm is the growth.

## Assumptions

- **Linear, autonomous dynamics.** du/dt = Au (eq. 1), A independent of
  time. "Only the existence of a propagator is required for the following
  development, and stationarity is assumed for convenience only" (§2).
- **Finite dimension.** A is a discretized matrix. Footnote 2 notes that
  convergence of a discretization to the continuous problem in time is
  not assured.
- **A chosen inner product.** Growth is measured in a norm ‖u‖ =
  (u†Mu)^{1/2}, and the change of variables v = M^{1/2}u, D =
  M^{1/2}AM^{−1/2} reduces any such norm to the Euclidean. Non-normality
  is a property of A in that norm: "it is always possible to find a
  (usually unphysical) norm that renders the operator normal" (§2). The
  results hold for the chosen norm, which "should be made on physical
  grounds", usually energy.
- **For the stochastic results:** additive white noise, delta-correlated
  in time, with spatial structure F (eqs. 23–24), and A asymptotically
  stable for a stationary state.

## Key results

- **Normality decides whether eigenvalues suffice (§2).** A is normal if
  AA† = A†A. Then ‖e^{At}‖ = e^{λ^R_max(A)t}, with λ^R_max(A) =
  max Re λ(A) the spectral abscissa, and "the stability of a normal
  dynamical system is determined for all time by its eigenspectrum".
- **Finite-time growth (eqs. 4–6).** The growth of u(0) over time t
  satisfies σ² = (e^{A†t}e^{At}u(0), u(0))/(u(0), u(0)). The maximum is
  λ_max(e^{A†t}e^{At}) = ‖e^{At}‖². With e^{At} = UΣV† (eq. 5), the
  columns of V ordered by growth are the optimal perturbations, and the
  maximum over all t is the global optimal. For every eigenvalue λ_i,
  σ²_min ≤ e^{(λ_i+λ_i*)t} ≤ σ²_max (eq. 6): the optimal does at least as
  well as the fastest mode.
- **The t → ∞ limit (eqs. 7–9).** The leading mode dominates, as modal
  theory says. But the unit initial condition that excites it most is the
  conjugate of its biorthogonal (the adjoint eigenvector), not the mode.
  In two dimensions, with eigenvectors at angle θ, the gain is csc θ
  (Fig. 1).
- **The t → 0 limit (eq. 10).** e^{A†t}e^{At} ≈ I + (A + A†)t, so the
  maximum instantaneous growth rate is the numerical abscissa a(A), the
  largest eigenvalue of (A + A†)/2. It can be positive "even though all
  normal modes of A are damped".
- **Forced response (eqs. 14–19).** With resolvent R(ω) = (iωI − A)^{−1},
  a normal system has ‖R(ω)‖ = 1/dist(iω, Λ(A)) (eq. 16), resonance at
  the least-damped mode. For non-normal A the optimal forcing is the
  leading right singular vector of R(ω), and ‖R(ω)‖ ≤ κ(E)/dist(iω,
  Λ(A)) (eq. 19), with κ(E) = ‖E‖‖E^{−1}‖ the condition number of the
  eigenvector matrix. The maximum response need not be at the
  least-damped mode's frequency and "can be orders of magnitude greater".
- **Variance under white noise (eqs. 20–22).** Forced by spatially
  uncorrelated white noise, ⟨u²⟩ = (1/2π)∫F(ω)dω with F(ω) =
  trace(R†(ω)R(ω)) ≥ Σ_i 1/|iω − λ_i|², "with equality only when A is
  normal" (eq. 22, cited to Ioannou 1995). A non-normal system maintains
  more variance than the sum over its poles.
- **Stochastic optimals and EOFs (eqs. 23–31).** The variance is
  F†B_tF with B_t = ∫_0^t e^{A†s}e^{As}ds (eqs. 26–27). At stationarity
  B_∞ and the covariance C_∞ solve the Lyapunov equations A†B_∞ + B_∞A =
  −I and AC_∞ + C_∞A† = −FF† (eq. 31). The leading eigenvectors of B_∞
  (stochastic optimals: the forcings that maintain most variance) and of
  C_∞ (EOFs: the patterns that hold it) coincide with the modes only if A
  is normal and FF† = I.
- **The 2 × 2 example (§4a, eqs. 32–43).** A = [[−1, −cot θ], [0, −2]]:
  eigenvalues −1 and −2, eigenvectors at angle θ, normal only at θ = π/2.
  - Numerical abscissa a(A) = (−3 + csc θ)/2 for 0 < θ < π/2, so some
    perturbation grows at first when θ < π/9.244.
  - Bound ‖e^{At}‖ ≤ κ(E)e^{λ^R_max t} = cot(θ/2)e^{−t} (eq. 40), which
    this operator does not attain. The optimal growth peaks near 8, at
    t ≈ 0.7, for θ = π/100; at θ = π/10 there is none (Fig. 4).
  - Maintained variance under unit white noise ⟨‖u‖²⟩ = 3/4 + cot²θ/12
    (eq. 43). The 3/4 is the equivalent normal response.
- **Damped Eady model (§4b).** Zonal wavenumber k = 2.5 (on the stable
  side of the modal short-wave cutoff at 2.39), l = π/5, damping r = 0.1
  (e-folding 2.9 days). Asymptotically stable, yet the global optimal
  grows in energy by about 100 over 4 days (Fig. 8). The numerical
  abscissa has no short-wave cutoff (Fig. 7). Stochastically forced, the
  first stochastic optimal accounts for 32% of the maintained energy and
  the first EOF for 69%, and the system carries a heat flux of about
  0.5 PW per W m⁻² of forcing at 30°.
- **Convective instability (§4c).** An Eady channel with damping zones at
  both ends (x_m = 20, r = 100) has only decaying modes. Its two-day
  optimal grows in energy by a factor of 111.6 (Fig. 12).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For non-normal A, eigenvalues govern only the t → ∞ limit; finite-time growth is ‖e^{At}‖ and can exceed every modal growth | strong | linear algebra, eqs. 4–6 and 10, with standard SVD facts |
| C2 | A system with every mode damped can amplify perturbations by large factors before decaying | strong | eq. 36 and Figs. 3–4; Eady example, Fig. 8; convective example, Fig. 12 |
| C3 | The optimal excitation of a mode is its adjoint (biorthogonal), not the mode | strong | eqs. 8–9, the 2 × 2 calculation (eq. 39) |
| C4 | Under white-noise forcing a non-normal system maintains more variance than the normal system with the same spectrum | strong for the inequality, cited | eq. 22, cited to Ioannou 1995, not proved here; eq. 43 in the example |
| C5 | Atmospheric phenomena (cyclogenesis, forecast error growth, maintained turbulent variance, heat flux) are better described by this theory than by modal theory | moderate | worked models and cited literature, not a comparison with data in this paper |

## Method

Discretize, choose the physical norm and transform to Euclidean
variables, then take singular value decompositions:

- of the propagator e^{At} for the initial-value problem;
- of the resolvent R(ω) for harmonic forcing;
- of B_∞ and C_∞, from the Lyapunov equations, for stochastic forcing.

## Concepts

- **Normal operator.** One that commutes with its adjoint in the chosen
  inner product, so its eigenvectors are orthogonal.
- **Spectral abscissa** λ^R_max(A). The largest real part of an
  eigenvalue; the t → ∞ growth rate.
- **Numerical abscissa** a(A). The largest eigenvalue of (A + A†)/2; the
  largest possible growth rate at t = 0.
- **Optimal perturbation.** The leading right singular vector of e^{At}
  for a chosen t. The **global optimal** maximizes over t as well.
- **Biorthogonal (adjoint) vector.** The vector orthogonal to all
  eigenvectors but one, which is the optimal excitation of that one.
- **Equivalent normal response.** The response of an operator with the
  same eigenvalues and orthogonal eigenvectors.
- **Stochastic optimal; EOF.** The forcing structures that maintain the
  most variance; the structures that hold it.
- **Generalized stability analysis.** The SVD analysis of the propagator
  at all t, which "subsumes" both asymptotic limits (§2).

## Connections

It builds on Kelvin (1887) and Orr (1907), on Farrell's optimal
perturbation papers from 1982 onward, and on the shear-flow transient
growth literature it cites in parallel (Butler & Farrell 1992; Reddy &
Henningson 1993; Trefethen et al. 1993, [LIT-932](../literature.d/LIT-932.md)). It names pseudospectra
as "a systematic basis" for analysing non-normality and leaves them
there. Part II ([LIT-929](../literature.d/LIT-929.md)) extends the theory to time-dependent operators.

## Bearing on the record

- **[CLAIM-186](../claims.d/CLAIM-186.md), "settling does not rule out bursts".** The note's first
  sentence is what this paper shows, at the strength it shows it: "it can
  be stable in every mode and still amplify a disturbance by a large
  factor for a while before the disturbance decays." That is C2.
- **[CLAIM-186](../claims.d/CLAIM-186.md), "directed, asymmetric coupling is a standard source of
  non-normality".** The paper does not say this. Its source of
  non-normality is energy drawn from a background shear flow. Its 2 × 2
  example is upper triangular, which is a one-way coupling, and the
  non-normality grows as that coupling (−cot θ) grows relative to the
  difference of the decay rates. So the example fits the reading, but
  the general statement is the assistant's, as [CLAIM-186](../claims.d/CLAIM-186.md) itself says.
- **The norm matters.** Non-normality is relative to an inner product,
  and "it is always possible to find a (usually unphysical) norm that
  renders the operator normal". Any reading across to an argument must
  say what its norm is. A measure of drift is a choice of norm, and
  whether a record's dependency structure is non-normal is a question
  about that norm, not about the graph alone.
- **[CLAIM-186](../claims.d/CLAIM-186.md)'s advice to measure drift over the short run after a
  disturbance, not only as an average.** The paper supports the
  physics behind it: the t → 0 and intermediate-t growth differ in kind
  from the t → ∞ rate. What it adds is the forced case. Under steady
  stochastic disturbance a non-normal system holds more variance than
  its spectrum predicts (eq. 22), so a non-normal argument under
  continual small disturbance would show more standing drift, not only
  bursts.
- **A new THEORY is filed**, [THEORY-323](../theory.d/THEORY-323.md): the eigenvalues of a
  non-normal operator govern only the long-run limit, and finite-time
  growth and forced variance can exceed what they predict by large
  factors. No existing THEORY held it.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Linear and autonomous. Nonlinear equilibration and time-dependent
  operators are outside it (the latter is Part II).
- The atmospheric examples are idealized models (the Eady model with
  uniform or localized damping), not comparisons with observation.
- The stochastic results assume white noise and stationarity. Eq. 22 is
  cited, not proved.
- Non-normality is norm-relative, and the paper's claims about the
  atmosphere rest on the energy norm being the physical one.
- Fig. 5's caption labels the normal reference "θ = 0"; the text makes
  the normal case θ = π/2. A slip in the caption.

## Open questions

- How much of the transient growth survives nonlinearity in each
  application. The paper parameterizes nonlinearity as noise and
  damping (§5) and does not test it.
- Which norm is physical when energy is not defined. That question is
  the one any reading across to a non-physical system must answer first.
