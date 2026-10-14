---
status: Read
paper: LIT-929
title: 'Farrell & Ioannou — Generalized Stability Theory II'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the authors' own copy of the published article
    (users.uoa.gr/~pjioannou/papers/genstab2.pdf, linked from Ioannou's
    publication list at the University of Athens; 13 pages, J. Atmos.
    Sci. 53(14):2041–2053). The publisher's page at journals.ametsoc.org
    returned 403 to curl on 2026-10-14, and Unpaywall and OpenAlex list
    no open copy. Text extracted with pdftotext; equations (11)–(16),
    (18)–(24) and (28)–(34), which the extraction garbled, were checked
    against page images. Every section and all nine figures were read.
    The paper's proofs lean on cited theorems (Oseledec, Has'minskii,
    Arnold & Kliemann), which were not read.
date: '2026-10-14'
summary: >-
  For du/dt = A(t)u there are no modes, but the propagator's singular
  vectors and the Lyapunov exponents and vectors carry generalized
  stability theory over. A time-dependent operator that is stable, or
  neutral, at every instant can be asymptotically unstable, and only if
  it is non-normal. Random variation of the operator destabilizes
  generically, with less variation needed the more non-normal and the
  less damped the mean operator.
---
<!-- inactive-ok-file: CLAIM-186 — Proposed; the claim this reading bears on, open -->
<!-- inactive-ok-file: THEORY-tmpyhatw — Proposed; the account this reading files -->

# NOTE-tmpkn9jn: Farrell & Ioannou — Generalized Stability Theory II

## Contribution

The paper extends the generalized stability theory of Part I ([LIT-931](../literature.d/LIT-931.md))
to operators that change in time. Its main result is that time
dependence and non-normality together can produce asymptotic
instability in a system that is stable at each instant, and that this is
generic under random variation. Non-normality is necessary for it. The
paper presents the first result through simple examples and a bound,
and the genericity result through cited theorems on stochastic systems
and numerical calculation.

## Key insight

In Part I, non-normal growth is transient because the operator stays the
same: the growing combination of modes rotates into a decaying one and
the slowest mode wins. If the operator changes before that happens, the
new operator can take the grown perturbation and grow it again. "Transient
growth instigated at the starting time is continued with further growth
when the switch to the second operator takes place, forestalling the decay
that would occur in the autonomous case" (§4). Repeated, that becomes
exponential growth, though no snapshot of the system is unstable.

## Assumptions

- **Linear, time-dependent dynamics.** du/dt = A(t)u (eq. 1), with
  propagator Φ(t, t₀) given by the time-ordered exponential (eqs. 3–5).
  In applications this is the tangent linear system about a trajectory.
- **Lyapunov exponents exist.** Guaranteed "for linear differential
  systems with continuous and bounded coefficients" (footnote 1). For an
  operator that is a time-independent mean plus a stochastic part, the
  multiplicative ergodic theorem gives exponents "almost surely in
  probability", independent of the realization (§2).
- **For the stochastic results:** A(t) = Ā + εΣ_i ξ_i(t)B_i (eq. 27),
  with ξ_i independent, identically distributed, delta-correlated white
  noise (eq. 28), interpreted in the Stratonovich sense (eqs. 30–32).
- **A norm**, as in Part I. Non-normality is relative to it.

## Key results

- **No modes, but optimal perturbations and Lyapunov vectors (§2).** The
  temporal eigenmodes of A(t) "are not defined". The first Lyapunov
  exponent λ = lim sup ln‖Φ(t)‖/t (eq. 6) takes the place of the spectral
  abscissa, and reduces to it for a constant operator. For large t the
  SVD of the propagator has rank one to exponential accuracy (eq. 7). The
  optimal excitation of the first Lyapunov vector then depends only on
  t₀, and the first Lyapunov vector only on t. The argument is by the
  semigroup property and induction on orthogonal subspaces.
- **Lorenz system (§3).** At b = 8/3, σ = 10, r = 28 the exponents are
  about 0.88, 0 and −14.55. Mean instantaneous growth rates along the
  trajectory:
  - numerical abscissa, about 4.2;
  - optimal excitation of the Lyapunov vector, about 2.7;
  - Lyapunov vector, about 0.88;
  - the largest real part of the frozen-time eigenvalues, about 1.6.
  The numerical abscissa itself "exhibits frequent excursions of
  negative growth rate". Convergence to
  the exponents is slow; convergence to the Lyapunov vector and its
  optimal excitation is fast, within about ten time units. The optimal
  perturbations lie up to 18° off the attractor plane.
- **A bound on the Lyapunov exponent (eqs. 10–12).** With r(t) = ‖u‖²,
  dr/dt = u†(A + A†)u, so lim sup (1/t)∫λ_min(s)ds ≤ λ ≤ lim sup
  (1/t)∫λ_max(s)ds, where λ_min, λ_max are the extreme eigenvalues of
  (A(t) + A†(t))/2. "It is immediate from (12) that nonnormality of the
  evolution operator is a necessary condition for parametric asymptotic
  instability of such systems with stable eigenvalues since if the
  operator were at each instant asymptotically stable and normal it would
  necessarily also have negative Lyapunov exponents."
- **Switched oscillator (eqs. 13–17, Fig. 6).** d/dt(x, v) =
  [[0, 1], [−ω²(t), −2γ]](x, v). The commutator (eq. 14) vanishes only for
  γ = 0 and ω ≡ 1, and no constant rescaling makes the operator normal
  when ω varies. Switching ω between ω₁ = 0.5 and ω₂ = 3 every T units,
  with γ = 0, gives a positive Lyapunov exponent except near integer
  multiples of half a natural period. "As T → 0, the Lyapunov exponent
  vanishes": a finite switching period is needed. The paper states, and
  does not show, that the destabilization persists for γ > 0, when the
  operator is stable at each instant.
- **Random neutral matrices (eqs. 18–26, Fig. 7).** A_j = R_φj
  [[i, −2i cot θ], [0, −i]] R_φj†: eigenvalues ±i, trace zero, neutral at
  every instant, eigenvectors at angle θ. Each step T_j = e^{A_jδt} has
  det T_j = 1 and singular values (σ, 1/σ), σ ≈ 1 + 2 cot θ δt for small
  δt. A unit vector grows in one step when |cos φ_j| > 1/√(1 + σ²)
  (eq. 24), so with φ_j uniform it grows more often than it shrinks. The
  Lyapunov exponent is positive for every θ ≠ π/2 and increases with the
  non-normality. As δt → 0 it vanishes (eq. 26), because the trace is
  zero.
- **Multiplicative white noise (§4, eqs. 27–35, Fig. 8).** With the noise
  scaled by δt^{−1/2}, the destabilization survives the continuous limit.
  A system of the form (27) "has necessarily a positive Lyapunov exponent
  for noise of sufficient magnitude ε, provided the dimensionality of the
  system is greater or equal to 2 and the noise matrices, B_i, are
  neither skew-symmetric nor commute with the deterministic operator"
  (cited to Has'minskii 1980 and Colonius & Kliemann 1993). "Increasing
  the degree of nonnormality of the deterministic background state
  operator Ā reduces the noise amplitude, ε, required." For the damped
  oscillator with Ā = [[0, 1], [−1, −2γ]] and B = [[0, 0], [−ε, 0]], the
  exponent falls with damping γ and rises with ε (Fig. 8). Stability is
  sample stability (an almost surely negative λ), not mean-square
  stability, since in stochastic systems μ₂ ≥ 2λ only (eq. 29).
- **Three-layer baroclinic model (§5, eqs. 36–37, Fig. 9).** Layer winds
  U_i = 10 + (3 − i)ΔU m s⁻¹ with independent white noise on each, damping
  r = 0.2 (5 days), global wavenumber 11. The noise needed for a positive
  exponent falls as the shear ΔU (the non-normality) rises. At ΔU = 10
  m s⁻¹ the model "suggests existence of a positive Lyapunov exponent
  for rms temporal fluctuations of the order of 10%", and about 1/5 day⁻¹
  at 30%. A two-layer model shows no noise-induced instability, because
  its noise matrix commutes with the mean operator.
- **Commuting noise cannot destabilize (§5).** "When Ā and B_i commute,
  multiplicative noise cannot alter the stability properties of the mean
  operator", because one change of basis diagonalizes both "and such a
  normal system cannot be destabilized by noise".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Modal analysis has no counterpart for time-dependent operators; optimal perturbations and Lyapunov vectors take its place | strong | §2, with Lyapunov 1907 and Oseledec 1968 cited |
| C2 | Non-normality is necessary for a system stable at each instant to be asymptotically unstable | strong | eq. 12, a one-line bound |
| C3 | A non-normal operator stable or neutral at each instant can be asymptotically unstable under time variation | strong | switched oscillator, Fig. 6; random neutral matrices, Fig. 7 |
| C4 | Multiplicative white noise of sufficient size destabilizes generically, unless the noise matrices commute with Ā or are skew-symmetric | moderate here | cited theorems (Has'minskii; Colonius & Kliemann), not proved in the paper |
| C5 | The variation needed falls as non-normality rises and rises with damping | moderate | numerical: Figs. 8 and 9 |
| C6 | Forecast error growth in the atmosphere at long range arises from the time dependence of the flow, not from intrinsic chaos | weak | a three-layer model and an argument (§§1, 5), stated as a suggestion |

## Concepts

- **Nonautonomous operator.** A(t), time-dependent; the tangent linear
  operator along a trajectory is the standard case.
- **Lyapunov exponent.** λ = lim sup ln‖Φ(t)‖/t, the asymptotic growth
  rate; the role of the spectral abscissa.
- **Lyapunov vector; its optimal excitation.** The structure that
  asymptotically grows fastest, and the initial perturbation that excites
  it most.
- **Parametric instability.** Asymptotic instability produced by
  variation of a system's parameters, though it is stable at each
  instant; the Mathieu equation is the classical case.
- **Sample stability; mean-square stability.** An almost surely negative
  Lyapunov exponent; a negative growth rate of the second moment. They
  differ for stochastic systems.

## Connections

The sequel to Part I ([LIT-931](../literature.d/LIT-931.md)), reading the transient growth of that
paper as the engine of instability under time variation. The stochastic
results rest on Has'minskii (1980), Arnold & Kliemann (1983), Colonius &
Kliemann (1993) and Furstenberg's theorem on products of random matrices
(1963), and the random-matrix example adapts Zel'dovich et al. (1984).

## Bearing on the record

- **[CLAIM-186](../claims.d/CLAIM-186.md), "an argument under development is the nonautonomous
  case".** The paper supports the first half: for a time-dependent
  operator there are no modes, "even in principle". It adds something
  [CLAIM-186](../claims.d/CLAIM-186.md) does not say and should weigh. Part I's comfort, that a
  non-normal system stable in every mode settles in the end after its
  burst, does not carry over. An operator that changes as it is worked on
  can grow disturbances without limit while being stable at every
  snapshot. The note in [CLAIM-186](../claims.d/CLAIM-186.md) reads GST as qualifying settling with
  bursts. On Part II, time variation of a non-normal structure can remove
  settling altogether.
- **The conditions are specific, and they cut both ways for [CLAIM-186](../claims.d/CLAIM-186.md).**
  - Non-normality is necessary (C2). If a record's dependency structure
    were normal in the relevant norm, changing it could not destabilize.
  - Damping stabilizes, and the variation needed grows with damping
    (C5). In the reading across, anchoring is a candidate for damping.
  - In the deterministic examples, a switching period short compared
    with the transient-growth time destabilizes nothing (T → 0, δt → 0).
    [LIT-929](../literature.d/LIT-929.md)'s Standing asks what carries over "to an operator that
    changes as fast as the state does". Here, at least, change faster
    than growth is harmless, and change on the growth timescale is what
    destabilizes. Under white noise scaled as δt^{−1/2} the fast limit
    stays unstable, so the answer depends on how the change is modelled.
- **What the paper does not support.** It is about linear perturbation
  dynamics with a norm. Nothing in it is about arguments, and the bearing
  remains the assistant's reading, as [CLAIM-186](../claims.d/CLAIM-186.md) says.
- **A new THEORY is filed**, [THEORY-tmpyhatw](../theory.d/THEORY-tmpyhatw.md): time dependence can
  destabilize a non-normal system stable at every instant; non-normality
  is necessary; random variation destabilizes generically, needing less
  the more non-normal and less damped the mean operator. No existing
  THEORY held it.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- The genericity of noise-induced instability (C4) is cited, not proved,
  and the paper's own evidence for it is numerical, in low-dimensional
  models.
- The claim that destabilization of the oscillator persists for γ > 0 is
  stated ("It can be shown") without the calculation.
- The atmospheric conclusions (C6) rest on a three-layer quasigeostrophic
  model with white-noise winds. The authors call it "suggests".
- Stratonovich versus Itô matters for multiplicative noise (eqs. 30–31);
  results for Itô noise could differ.

## Open questions

- Coloured noise and slow variation. The paper's two deterministic
  examples need a finite switching period; whether realistic, correlated
  variation sits nearer the switched or the white-noise case is not
  settled here.
- Whether the noise threshold can be estimated from properties of Ā
  alone, such as its numerical abscissa or pseudospectra, rather than by
  computing exponents.
