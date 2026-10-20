---
status: Read
paper: LIT-tmpvihtb
title: 'Parish and Duraisamy — Non-Markovian closure for LES via Mori–Zwanzig'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:1611.03311v2 (23 January 2017, 31 pages),
    text extracted with pdftotext. Read: the abstract, §I, §II with the
    linear example, the Mori–Zwanzig identity, the orthogonal-dynamics
    analysis and the derivation of the t-model and finite-memory models
    (Eqs. 1–26), §III on Burgers (Eqs. 27–32, memory-length study,
    results), §IV on triply periodic Navier–Stokes (isotropic turbulence,
    Taylor–Green vortex at Re 800 and 1600), §V on channel flow, §VI, and
    Appendices A–C. The figures were read from the pages rendered at 70
    dpi, and Fig. 6b at 200 dpi; values quoted from them are approximate.
    The multi-interval quadrature, Eqs. 24–25, is garbled in extraction
    and was not checked; the paper uses only one sub-interval. The
    published version was not compared.
date: '2026-10-20'
summary: >-
  Derives large-eddy-simulation closures from the Mori–Zwanzig identity
  by Stinis's finite-memory approximation, which turns the memory integral
  into auxiliary relaxation equations, a finite Markovian augmentation of
  the resolved modes. Its error is not bounded and its memory length is
  fitted (Burgers: τ₀ ≈ 0.2 over the spectral radius of the resolved
  Jacobian) or preset. Against filtered DNS it matches dynamic Smagorinsky
  on isotropic turbulence and channel flow, beats Smagorinsky and the
  t-model on the Taylor–Green vortex, and puts the subgrid drain at the
  cutoff, as DNS does.
---
<!-- inactive-ok-file: THEORY-tmp4ou43 — Proposed; the empirical account filed from this reading -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-327 CLAIM-331 THEORY-257 — Proposed; open claims and readings this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpai9kc LIT-tmple6xy LIT-tmpki8cm LIT-tmp2snx1 LIT-tmpko78q — Deferred; works registered unread, cited as open -->
# NOTE-tmpg06if: Parish and Duraisamy — Non-Markovian closure for LES via Mori–Zwanzig

## Contribution

It takes Stinis's finite-memory approximation of the Mori–Zwanzig memory
integral, until then tested on Burgers and Euler, into Fourier–Galerkin
large-eddy simulation of the incompressible Navier–Stokes equations. It
proposes a rule for the one free constant, the memory length, from the
resolved Jacobian, with sixty Burgers runs behind it. It then shows on
four flows that the closure holds up against filtered DNS and against
Smagorinsky-type eddy viscosity. The memory of the eliminated scales
becomes a small number of extra fields carried with the resolved ones.

## Key insight

Coarse-graining a system with no scale separation does not give a
Markovian closure. It gives the resolved dynamics plus a memory integral
and noise. The memory need not be kept as an integral: if its integrand
is assumed to vanish beyond a lag τ, differentiating it and applying the
trapezoidal rule turns it into a relaxation equation for the subgrid force
itself. The macrostate then becomes the resolved field plus the subgrid
force, relaxing at rate 2/τ toward a term computed from the resolved
field. The memory is "numerical memory, as opposed to physical memory":
its length depends on where the cut is made.

## Assumptions

- A semi-discrete ODE dφ/dt = R(φ), split into resolved Fourier modes
  φ̂ (|k| < k_c) and unresolved φ̃. The split is a sharp spectral cutoff,
  so the LES equations are the Galerkin-truncated ones.
- **Projection.** P f(φ̂₀, φ̃₀) = E[f | φ̂₀], under a Gaussian initial
  density for φ̃₀ in the zero-variance limit, so P f(φ̂₀, φ̃₀) = f(φ̂₀, 0).
  The unresolved modes are taken to be zero at t = 0. This holds in the
  Burgers and Taylor–Green runs, which start resolved. It does not hold
  in the isotropic-turbulence run, started from filtered 512³ DNS, or in
  stationary channel flow.
- **Finite memory.** The memory integrand is assumed to vanish beyond a
  constant lag τ_m at each order m. Each truncated integral is evaluated
  by the trapezoidal rule on one sub-interval. The hierarchy is closed by
  setting w^{(m+1)} = 0, "justified if the support or magnitude of the
  integrand decreases with the repeated application of QL".
- **Memory length.** For Burgers, τ₀ is fitted to DNS dissipation or
  taken from τ₀ ≈ 0.2/ρ(∂R/∂u). Higher orders use τ₁ = τ₂ = 0.5τ₀ by fiat.
  For Navier–Stokes, τ₀ = 0.1 throughout, with no stated derivation.
- **Pressure.** In channel flow, the effect of coarse-graining on
  pressure is neglected ("observed to be minimal" in the periodic case).
  The physical-space form in Appendix C neglects it too.

## Key results

- **Linear example (Eq. 4).** Eliminating y from ẋ = A₁₁x + A₁₂y,
  ẏ = A₂₁x + A₂₂y gives
  ẋ = A₁₁x + A₁₂A₂₁∫₀ᵗ x(t − s)e^{A₂₂s} ds + A₁₂y(0)e^{A₂₂t}.
  The paper prints the last coefficient as A₂₁. That is a typo, checked
  numerically: with A₂₁ the equation misses dx/dt by up to 2.1, and with
  A₁₂ it agrees to quadrature error, 1.6 × 10⁻⁵. It is A5's example in
  [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md).
- **Mori–Zwanzig identity (Eq. 10).** ∂_t e^{tL}φ₀ⱼ = e^{tL}PLφ₀ⱼ
  (Markovian) + e^{tQL}QLφ₀ⱼ (noise) + ∫₀ᵗ e^{(t−s)L}PL e^{sQL}QLφ₀ⱼ ds
  (memory), from Dyson's formula.
- **Linear orthogonal dynamics (Eqs. 15–19).** For dφ/dt = Aφ, the
  orthogonal dynamics are solved by the auxiliary system dφ_Q/dt = A_Q φ_Q.
  With A_Q = SΛS⁻¹, the memory integrand carries e^{Λs}, and for stable
  Λ its "support" has a timescale ∝ 1/|Λ|. This is exponential decay, not
  finite support (see Limitations).
- **t-model (Eq. 20).** Keeping the leading term of the integrand's
  Taylor series in s gives memory ≈ t PLQLφ(t). It is accurate when the
  orthogonal dynamics barely move QLφ₀ and the true dynamics are slow.
- **Finite-memory models (Eqs. 21–26).** With w^{(m)} the memory at
  order m over lags [0, τ_m], constant τ_m and one trapezoidal interval:
  dw^{(m)}/dt = −(2/τ_m)w^{(m)} + 2e^{tL}PL(QL)^{m+1}φ₀ⱼ + w^{(m+1)}.
  Truncated at w^{(m+1)} = 0, this is a finite Markovian augmentation.
  Re-derived in [THEORY-tmpswb4h](../theory.d/THEORY-tmpswb4h.md), which also shows that at first order it
  is an exponential kernel 2e^{−2s/τ₀} on the first-order term, tending
  to the t-model with t replaced by τ₀.
- **Memory-length rule (Fig. 2).** Over 60 Burgers runs, the fitted τ₀
  is linear in 1/ρ(∂R/∂u). It collapses for k_c = 16 and 32, with a
  steeper slope for k_c = 8. The paper's fit is τ₀ ≈ 0.2/ρ. Appendix B:
  with the slope sampled as a Gaussian, energy and dissipation predictions
  are well concentrated, and the subgrid term less so.
- **Burgers (Table 1, Figs. 3–5).** 32 modes against 2048-mode DNS,
  ν = 0.01, τ₀ = 0.135. FM1–FM3 follow energy, dissipation and mean
  subgrid magnitude. FM2 and FM3 also follow the t = 2 spectrum at all
  wavenumbers, and the phase-space trajectories of modes 8 and 15. The
  t-model overpredicts the subgrid term after t ≈ 0.5. Smagorinsky puts
  its maximum subgrid content at t = 0, when the flow is fully resolved.
  At k_c = 8, U₀* = 5, FM1 misses the second dissipation peak.
- **Isotropic turbulence (Table 2, Fig. 6).** 64³ against 512³,
  Re_λ ≈ 200, t = 4. FM1 is comparable to dynamic Smagorinsky in energy,
  dissipation and resolved transfer. Its subgrid transfer peaks near the
  cutoff, as DNS's does, but deeper (about −5 × 10⁻⁴ at k ≈ 33 against
  −3.5 × 10⁻⁴ at k ≈ 31). Both Smagorinsky models drain at low k.
- **Taylor–Green vortex (Tables 3–4, Figs. 7–8).** 32³ against 128³
  (Re = 800) and 256³ (Re = 1600). FM1 follows energy and dissipation,
  including the double peak near t = 8, and the spectra at t = 5 and 10.
  Smagorinsky dissipates from t = 0. The t-model over-dissipates and
  needed Δt = 0.005 against 0.02.
- **Channel flow (Table 5, Fig. 9).** Re_τ = 180, 32 × 64 × 32. FM1 is
  similar to dynamic Smagorinsky in mean velocity and Reynolds stresses,
  both near the Moser–Kim–Mansour DNS.
- **Physical-space form (Appendix C, Eq. 46).** With pressure neglected,
  FM1 is ∂_t ∂_j τ_ij = −(2/τ₀)∂_j τ_ij + 2[∂_j(u_j ∂_m L_im) +
  ∂_j(u_i ∂_m L_jm)], with L the Leonard stress at the grid filter: a
  relaxation equation for the subgrid force, with no convection term,
  resembling the Lagrangian dynamic model's memory.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Coarse-graining leads to memory: the reduced dynamics of resolved modes are exactly Markovian term + memory + noise | strong | the Mori–Zwanzig identity, Eq. 10; standard |
| C2 | For stable linear systems, the memory integrand has "finite support" with a timescale set by the eigenvalues of the orthogonal dynamics | weak as worded, strong as "decays exponentially" | Eqs. 15–19 and Fig. 1; exponential decay is not finite support |
| C3 | The finite-memory hierarchy reduces the memory to Markovian equations, truncated by neglecting the next term | strong as a construction; the truncation is unjustified | Eqs. 21–26; re-derived in [THEORY-tmpswb4h](../theory.d/THEORY-tmpswb4h.md) |
| C4 | The memory length scales with the inverse spectral radius of the resolved Jacobian, τ₀ ≈ 0.2/ρ | moderate, for Burgers | 60 fitted runs, Fig. 2; "evidence rather than proof" in the authors' words; partly dimensional (see Limitations) |
| C5 | Finite-memory closures predict energy, dissipation and subgrid transfer accurately on Burgers and Navier–Stokes test flows | moderate | Figs. 3–9; qualitative, no error norms; FM1's subgrid transfer peak about 40% too deep in isotropic turbulence |
| C6 | They are more robust than Smagorinsky outside equilibrium turbulence, because they make no assumption about the flow state | moderate | Taylor–Green and Burgers runs that start resolved; on isotropic turbulence the authors decline to claim superiority |
| C7 | "The form of the closure is not imposed by the modeler, but is rather derived from the mathematics of the coarse-graining"; the only heuristic is the memory length | weak | the projection, the finite-support assumption, the quadrature, the truncation, the higher-order τ's and the neglect of pressure are all modeller's choices (see Limitations) |
| C8 | "An analysis of the memory term for Burgers equation demonstrated the need for the finite memory length" | weak | §III.B.1 shows that a finite τ₀ fits; it does not compare against an infinite memory, apart from the t-model, which is a different approximation |

## Method

1. Write the LES as a Galerkin truncation: resolved modes F, unresolved
   G, sharp spectral cutoff.
2. Take the Mori–Zwanzig identity with the zero-variance projection
   (unresolved modes set to zero) and drop the noise by projecting.
3. Replace the memory integral by w^{(0)}. Assume finite support τ₀,
   differentiate in time, and close the far-end term by the trapezoidal
   rule, giving dw^{(0)}/dt = −(2/τ₀)w^{(0)} + 2PLQLφ(t) + w^{(1)}.
   Repeat to order m and drop w^{(m+1)}.
4. Compute PLQLφ (and higher terms, Appendix A) from the resolved field
   by convolutions over p ∈ F, q ∈ G with 2× padding. For Navier–Stokes,
   PLu is the unclosed right-hand side, already computed.
5. Choose τ₀: by fit to DNS dissipation (Burgers), by the Jacobian rule,
   or preset (Navier–Stokes, 0.1).
6. Integrate (φ̂, w^{(0)}, …, w^{(m)}) with RK4 (periodic) or
   semi-implicit Adams–Bashforth (channel).

## Concepts

- **Markovian / noise / memory terms**: the three terms of Eq. 10. The
  noise lives in the range of Q for all time.
- **Orthogonal dynamics**: ∂_t F = QLF, the evolution of the noise. Its
  solution is the obstacle to evaluating the memory.
- **Numerical memory**: the paper's name for the memory in the reduced
  equations, set by the physics and the level of coarse-graining, "as
  opposed to physical memory".
- **t-model**: memory ≈ t PLQLφ(t), a long-memory, short-time
  approximation with no free constant.
- **Finite-memory model (FMm)**: Stinis's hierarchy of auxiliary
  variables w^{(0)}, …, w^{(m)}, each the memory at order m over a window
  τ_m, truncated at order m. w^{(0)} = ikτ^{SGS}, the subgrid force.
- **Memory length τ₀**: the window of FM1; the closure's one constant.

## Connections

It builds on the optimal-prediction programme of Chorin, Hald and
Kupferman (2000, 2002, 2006; [LIT-tmpai9kc](../literature.d/LIT-tmpai9kc.md) and [LIT-tmple6xy](../literature.d/LIT-tmple6xy.md) are registered
unread), on Givon, Hald and Kupferman's existence proof for orthogonal
dynamics, on Bernstein's and Hald and Stinis's t-model studies, on Chandy
and Frankel's t-model LES, and above all on Stinis's finite-memory and
renormalized models (2006, 2012, 2013, 2015). Its comparators are
Smagorinsky (1963) and the dynamic Smagorinsky model. Appendix C relates
it to the Lagrangian dynamic model of Meneveau, Lund and Cabot (1996).
Companion preprints by the same group, Gouasmi, Parish and Duraisamy on
memory effects (arXiv:1611.06277) and a dynamic Mori–Zwanzig model
(arXiv:1611.02143), are cited and not held here.

## Bearing on the record

- **[QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md), the central bearing.** The finite-memory closure
  is a finite-dimensional Markovian augmentation in the question's sense:
  the resolved modes plus (m + 1)N auxiliary variables, all evolving
  Markovianly ([THEORY-tmpswb4h](../theory.d/THEORY-tmpswb4h.md), Active, answers in part). It does not
  have the controlled error the question asks for:
  - the truncation drops w^{(m+1)} with no bound;
  - the memory length is fitted to DNS or preset;
  - the kernel's shape is fixed by the trapezoidal rule, not by the
    eliminated spectrum. At zero lag it is twice the true one for every
    τ₀. In A5's own linear example, where one coordinate (y itself) is
    an exact augmentation, FM1's best error in x is 3.5 × 10⁻², checked
    here.

  The paper's linear analysis gives the link to the spectrum the question
  wants (memory decays as e^{Λs} for the unresolved block's eigenvalues),
  but its working rule abandons it for the resolved Jacobian. On the
  question's second half: the augmenting coordinate is the subgrid force,
  a named physical field. That is A5's "additional internal memory
  coordinate", and it suggests applying the record's level criteria to
  (φ̂, w), the augmented state. The paper's "numerical, not physical"
  memory supports A3's caution that the split depends on the projection.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** The paper's premise is the third case in the claim's
  note of 2026-10-19: turbulence "lack[s] scale separation", and
  Markovian eddy viscosity rests on "rapid equilibration of small
  scales", which fails. Its measurement adds something. The fitted
  memory is about a fifth of the fastest resolved timescale (C4). It
  shortens as Reynolds number rises and lengthens as the cutoff
  coarsens. So the unresolved scales are faster than the resolved ones,
  but by a ratio set by the cut, not across a gap, and in the
  quasi-steady limit the closure becomes Markovian. That is consistent
  with "characteristically slower", and shows the ordering is graded and
  depends on the chosen cut. It is not a defeater: no variable another
  criterion individuates changes faster than its constituents here.
- **[QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md).** The quantity the augmentation carries is the
  energy flux across the cutoff, T^{SGS}(k) = u*·w^{(0)}. In isotropic
  turbulence the DNS drain sits within a few wavenumbers of the cutoff,
  and only the memory closure reproduces that location; the Smagorinsky
  models drain at low k. That is indirect evidence that transfer across
  the cut is local in scale, the property A3 took from Eyink and Aluie
  ([LIT-tmp2snx1](../literature.d/LIT-tmp2snx1.md), unread). The paper does not frame it that way. Nothing
  here bears on organized throughput as a criterion of unity.
- **[THEORY-257](../theory.d/THEORY-257.md), [CLAIM-327](../claims.d/CLAIM-327.md).** A memory closure summarizes the eliminated
  history by a finite present state. That is the shape [CLAIM-327](../claims.d/CLAIM-327.md) gives a
  reputation, a variable that stores the past. It does not test
  dynamical independence: the resolved modes here are not closed, which
  is why a closure is needed at all.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** A Fourier cutoff in turbulence is a partition with
  strong coupling across it. The closure works without any weakly
  coupled block, a further case of closure without a block for
  [QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md).
- **[LIT-tmpki8cm](../literature.d/LIT-tmpki8cm.md)** (Germano, unread): the paper's Leonard-stress form
  (Appendix C) is the filtered-description vocabulary Germano's work
  uses.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Eq. 4 typo:** the noise coefficient is A₁₂, not A₂₁ (checked
  numerically, above).
- **"Finite support" is overstated (C2).** The linear analysis shows
  exponential decay of the integrand, which has infinite support. The
  finite-memory assumption is motivated by it, not shown. The relevant
  eigenvalues are those of the unresolved block. A_Q as defined also has
  N zero eigenvalues, which the text passes over.
- **The Jacobian rule drops the analysis it cites.** The linear analysis
  ties memory to the unresolved spectrum. The rule uses the resolved
  Jacobian, on the argument that without scale separation the two are
  comparable. The collapse in Fig. 2 may be partly dimensional: at fixed
  k_c, every Burgers timescale scales with U₀k_c and νk_c², as ρ does. No
  alternative timescale is tested. The k_c = 8 runs do not collapse with
  the others.
- **The zero-variance projection makes the formalism deterministic.** P
  is evaluation at φ̃ = 0, so it commutes with every function of the
  state, and the "casual" commuting of the Markovian term is in fact
  exact. But the "best approximation given the initial density" is then
  just the trajectory started fully resolved, and the noise term plays no
  role. The isotropic-turbulence and channel runs violate the
  zero-unresolved start; the authors say a nonzero-variance derivation
  "will be appropriate" for such problems.
- **C7 is overstated.** Besides the memory length, the projection, the
  finite-support assumption, the quadrature, the truncation, τ₁ = τ₂ =
  0.5τ₀, τ₀ = 0.1 for Navier–Stokes and the neglect of pressure in the
  channel are all choices.
- **No quantitative errors.** Every comparison is a plot. "Excellent" in
  the abstract is not backed by a number. In isotropic turbulence the
  subgrid transfer peak is about 40% too deep, with slight backscatter
  below k ≈ 17 that DNS does not show.
- **No error bound** for the truncation or quadrature, and the
  multi-interval quadrature (Eqs. 24–25) was not tested; only one
  sub-interval is used.
- **One realisation per case.** Burgers uses one random-phase seed, and
  isotropic turbulence one snapshot (t = 4) for spectra.
- **Burgers is not chaotic**, as the authors note, and the Navier–Stokes
  runs are at low to moderate Reynolds number (Re_λ ≈ 200, Re ≤ 1600,
  Re_τ = 180).

## Open questions

- For what class does a finite-memory augmentation have a bounded error,
  with the number of auxiliary variables and the error in terms of the
  unresolved spectrum? A bound for the dropped w^{(m+1)} would answer it
  for this hierarchy. The quadrature's fixed zero-lag amplitude suggests
  that fitting the kernel's amplitude and rate separately would do better.
- Does the memory length track the unresolved spectrum (as the linear
  analysis says) or the resolved one (as the rule assumes)? A test that
  varies the cutoff with the flow fixed would separate them.
- Is the subgrid force, as the augmenting coordinate, dynamically
  independent in [THEORY-257](../theory.d/THEORY-257.md)'s sense once paired with the resolved field?
  That is, does (φ̂, w) close to the accuracy shown? This would put
  [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md)'s "apply the level criteria to the augmented state"
  to a concrete test.
