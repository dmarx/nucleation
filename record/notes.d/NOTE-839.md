---
number: 839
status: Read
formerly:
- NOTE-tmphb8jp
paper: LIT-932
title: 'Trefethen et al. — Hydrodynamic Stability Without Eigenvalues'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the copy on the first author's Oxford page
    (people.maths.ox.ac.uk/trefethen/publication/PDF/1993_57.pdf, linked
    from his list of papers): a JSTOR scan of the published article,
    Science 261(5121):578–584, with JSTOR's cover page. Text extracted
    with pdftotext; the two-column layout scrambled it, so equations
    (12)–(14), Table 1, Table 2 and Figs. 2 and 4–10 were read from page
    images. Every section and all 45 notes were read. Unpaywall and
    OpenAlex list no open copy.
date: '2026-10-14'
summary: >-
  The linearized operators of plane Couette and Poiseuille flow are far
  from normal. With every eigenmode decaying, perturbations can grow
  transiently by O(R) and resonate by O(R²), and an operator
  perturbation of norm O(R⁻²) makes the flow eigenvalue-unstable, all
  read off the pseudospectra. That transition to turbulence then follows
  from linear growth plus energy-neutral nonlinear mixing is a conjecture,
  from a 2 × 2 model.
---
<!-- inactive-ok-file: CLAIM-186 — Proposed; the claim this reading bears on, open -->
<!-- inactive-ok-file: THEORY-323 — Proposed; the accounts this reading files -->

# NOTE-839: Trefethen et al. — Hydrodynamic Stability Without Eigenvalues

## Contribution

For the shear flows where eigenvalue analysis fails worst, the paper puts
three linear accounts of the failure on one footing, the pseudospectra of
the linearized Navier–Stokes operator. It gives their leading-order
scaling with Reynolds number R (Table 1). It then offers, as speculation,
a 2 × 2 nonlinear model of how linear transient growth and nonlinear
mixing could combine to give a transition threshold that falls faster
than 1/R. The transient growth results themselves are credited to earlier
work (Gustavsson; Henningson et al.; Butler & Farrell; Reddy & Henningson).
The pseudospectral framing and the synthesis are this paper's.

## Key insight

Eigenvalues answer "what happens as t → ∞" and "at what frequencies is
the response infinite". A non-normal operator can have a large response
far from its eigenvalues. Its pseudospectra, the regions where
‖(ωI − L)⁻¹‖ exceeds 1/ε, show where. When they reach far into the
unstable half-plane the flow, though eigenvalue-stable, amplifies
strongly, and a small change to the operator can make it unstable.

## Assumptions

- **Linearization about laminar flow.** dU/dt = −iLU (eq. 1), with U an
  infinitesimal perturbation of plane Couette or plane Poiseuille flow in
  an infinite slab.
- **The energy norm** ‖U‖ = (∫|U|² dx dy dz)^{1/2} (eq. 2). Every
  amplification figure is in that norm.
- **Fourier decomposition** in x and z, so each calculation is
  one-dimensional in y with wavenumbers α and β; the reported quantities
  are optimized over α and β.
- **Discretization.** Chebyshev spectral, projected onto dominant
  eigenmodes, matrices of about 80 × 80 (notes 24–25).
- **For the nonlinear section:** a 2 × 2 model with a quadratic,
  energy-conserving nonlinearity standing in for the Navier–Stokes
  advection term.

## Key results

- **The anomaly (pp. 578–579).** Eigenvalue analysis gives a critical R =
  5772 for Poiseuille flow, where transition is seen at R ≈ 1000, and
  stability for all R for Couette flow, where transition is seen at
  R ≈ 350.
- **Three linear quantities, all non-modal and three-dimensional.**
  - *Pseudoresonance:* sup over real ω of ‖(ωI − L)⁻¹‖ (eqs. 5–6). For
    a normal operator with spectrum at distance O(R⁻¹) below the axis it
    would be O(R); here it is O(R²).
  - *Transient growth:* sup over t ≥ 0 of ‖exp(−itL)‖ (eq. 9), O(R),
    reached at times O(R). For a normal operator with stable spectrum it
    would be at most 1.
  - *Destabilizing perturbations:* the ε-pseudospectrum is the union of
    the spectra of L + E over ‖E‖ ≤ ε (eq. 13). The smallest
    destabilizing E has norm ε_min = (sup over real ω of
    ‖(ωI − L)⁻¹‖)⁻¹, which is O(R⁻²) (Fig. 8). It is rank one, ε_min vu*,
    turning streaks back into vortices.
- **Table 1, leading order as R → ∞ (accurate to 1% for R > 100).**

  | quantity | Couette | Poiseuille |
  |---|---|---|
  | distance of spectrum from real axis | (R/2.47)⁻¹ | (R/2.47)⁻¹ |
  | maximum resonance | (R/8.12)² | (R/17.4)² |
  | transient growth sup ‖exp(−itL)‖ | R/29.1 | R/71.5 |
  | optimal time t_opt | R/8.52 | R/13.2 |
  | lower bound from pseudospectra | R/42.6 | R/103 |

  The Poiseuille figures "pertain to the highly nonnormal part of the
  problem, ignoring the R > 5772 mode (TS wave)". The maxima are at α = 0
  or nearly so, with β between 1.18 and 2.04: streamwise vortices that
  become streaks.
- **Bounds linking the three (eqs. 10–12).** ‖L⁻¹‖ ≤ ∫₀^∞‖exp(−itL)‖dt
  (eq. 11), "typically within a factor of 2 of equality", so the O(R²)
  resonance is an O(R) accumulation time times an O(R) transient growth.
  sup_t ‖exp(−itL)‖ ≥ sup_ε ε⁻¹σ_ε(L), with σ_ε the furthest reach of
  the ε-pseudospectrum into the upper half-plane (eq. 12); for these flows
  the bound falls short by a factor of about 1.4.
- **Specific figures.** At R = 5000 a streamwise streak is an
  ε-pseudomode of Poiseuille flow for ε ≈ 1.2 × 10⁻⁵, so it "can be
  excited by a streamwise vortex five orders of magnitude weaker in
  amplitude"; and a perturbation of L of norm 1.2 × 10⁻⁵ makes the flow
  unstable. Amplification by 1000 is possible for all R ≥ 549 (Fig. 2).
  About 90% of random perturbations of norm 10⁻³ to a 20 × 20 projection
  of L at R = 5000 render it unstable (note 30). The abstract's "factors
  on the order of 10⁵" refers to these resonance and pseudomode figures,
  not to transient growth, which at R = 5000 is about 70 in norm by
  Table 1.
- **The 2 × 2 nonlinear model (eq. 14, Table 2, Fig. 10).** du/dt =
  Au + ‖u‖Bu with A = [[−R⁻¹, 1], [0, −2R⁻¹]] and B = [[0, −1], [1, 0]].
  B is skew-symmetric, so the nonlinear term moves energy and does not
  create it. At R = 25 the threshold amplitude is 4.22 × 10⁻⁴. Across
  R = 12.5 to 100 the threshold ε falls by a factor of about 8 per
  doubling of R, so ε = O(R⁻³), while the linear growth factor M is O(R).
  With forcing in place of an initial condition the threshold is
  O(R⁻⁴). The mechanism ("bootstrapping"): linear growth to Rε moves the
  state into a non-growing direction, and the quadratic term returns
  R(Rε)² = R³ε² to the growing one, which sustains growth if it exceeds ε.
- **The conjecture (p. 582).** "We conjecture that transition to
  turbulence of eigenvalue-stable shear flows proceeds analogously to our
  model in that the destabilizing mechanism is essentially linear in the
  senses described above and the amplitude threshold for transition is
  O(R^γ) for some γ < −1." Note 39 cites bounds −21/4 ≤ γ ≤ −1 from
  Kreiss, Lundbladh and Henningson.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For non-normal operators, eigenvalue stability is compatible with transient growth, resonance far from the spectrum and sensitivity of the spectrum to small perturbations | strong | linear algebra, eqs. 5–13 |
| C2 | Linearized Couette and Poiseuille flow show transient growth O(R), resonance O(R²) and destabilizing perturbations O(R⁻²), with streamwise vortex–streak structures | strong | computation, Table 1 and Figs. 2, 4–9 |
| C3 | The three linear accounts are facets of one pseudospectral picture and predict similar flow structures | moderate | eqs. 11–13 and Fig. 9 |
| C4 | In a 2 × 2 model, linear transient growth with energy-neutral quadratic mixing gives a threshold amplitude O(R⁻³) | strong for the model | computation, Table 2, and a scaling argument |
| C5 | Transition in eigenvalue-stable shear flows proceeds by this linear-growth-plus-mixing route with threshold O(R^γ), γ < −1 | weak | conjecture by analogy with the model, labelled as such |
| C6 | Distinct triggers (vibration, inlet disturbance, geometric imperfection) may correspond to the three linear mechanisms | weak | speculation in the Conclusion |

## Concepts

- **Normal operator.** One with orthogonal eigenfunctions (in the energy
  norm here).
- **ε-pseudospectrum** Λ_ε(L). The set of ω with ‖(ωI − L)⁻¹‖ ≥ ε⁻¹;
  equivalently the spectra of all L + E with ‖E‖ ≤ ε (eqs. 7, 13).
- **ε-pseudomode.** A function u with ‖(L − ω)u‖ ≤ ε‖u‖: nearly an
  eigenfunction, and excitable to large amplitude by a small input.
- **Pseudoresonance.** Large response to forcing at frequencies far from
  any eigenvalue.
- **Subcritical transition.** Transition to turbulence at R below the
  eigenvalue critical value.
- **3D perturbation.** Here, one depending on z, whether or not it
  depends on x (note 19).

## Connections

It builds on Butler & Farrell (1992) and Reddy & Henningson (1993), named
as its foundation, and on Reddy, Schmid & Henningson (1993) for the
pseudospectra of the Orr–Sommerfeld operator. It sets aside Squire's
theorem, which justified studying 2D perturbations: "this emphasis on 2D
perturbations has been misplaced". It questions secondary-instability
theory as an account of natural transition (note 31). Farrell & Ioannou
([LIT-931](../literature.d/LIT-931.md), [LIT-929](../literature.d/LIT-929.md)) cite it as the parallel development in laboratory
shear flow.

## Bearing on the record

- **[CLAIM-186](../claims.d/CLAIM-186.md) states the paper's conjecture as its finding.** The note of
  2026-10-11 says: "Shear flows judged stable by their eigenvalues turn
  turbulent because a transient amplification hands the disturbance to
  nonlinear dynamics." The paper shows the transient amplification (C2).
  That turbulence follows "because" of it, through nonlinear
  bootstrapping, it offers as a conjecture from a 2 × 2 model, in a
  section that opens "we speculate". The sentence should say that
  Trefethen et al. conjecture this, and on what model.
- **The model supports a narrower form of [CLAIM-186](../claims.d/CLAIM-186.md)'s reading.** In the
  2 × 2 model the nonlinearity creates no energy; it only rotates the
  grown state back into the growing direction. The threshold falls as
  R⁻³ against a linear growth of R. The reading across would be that a
  burst becomes a lasting change only if something feeds the grown
  disturbance back to where it started, and that the size of disturbance
  needed falls steeply with the amplification. That is an analogy the
  model invites, not a result about arguments.
- **[LIT-932](../literature.d/LIT-932.md)'s own summary says nonlinearity "can carry the amplified
  disturbance into turbulence".** That is fair as "can", in the model,
  and is corrected on the LIT to mark it as conjecture for the flows.
- **Two new THEORY documents.** [THEORY-323](../theory.d/THEORY-323.md) (with Farrell & Ioannou
  Part I, [LIT-931](../literature.d/LIT-931.md)) holds the general linear-algebra claim.
  [THEORY-304](../theory.d/THEORY-304.md) holds the shear-flow scalings, with the transition
  conjecture placed under "What this does not say". No existing THEORY
  held either.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Linear analysis about laminar flow in infinite plane geometry. Pipe
  flow and boundary layers are mentioned, not computed.
- The scalings are asymptotic in R, with constants from discretized
  computations.
- The transition mechanism is conjecture. The authors list ways the
  Navier–Stokes equations differ from the model: infinitely many degrees
  of freedom, most without non-normal growth, and nonlinear interactions
  across wavenumbers, which make the model's nonlinearity "perhaps
  unrealistically strong".
- The physical meaning of operator perturbations is left open: they may
  be "better understood as a symptom of the nonnormality of the
  unperturbed problem than as a description of how transition to
  turbulence actually takes place".

## Open questions

- The exponent γ in the transition threshold O(R^γ) for real flows,
  which the authors expected simulation to settle "in the coming decade".
- Which trigger (vibration, inlet disturbance, imperfect geometry)
  matches which of the three linear mechanisms in experiment.
