---
status: Read
paper: 'LIT-tmple6xy'
title: 'Chorin, Hald and Kupferman — Optimal prediction with memory'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the published version (Physica D 166:239–257, 19
    pages), the PDF posted on Chorin's Berkeley page, text extracted with
    pdftotext. Read: the abstract, §§1–9 (the three projections, the
    Mori–Zwanzig derivation, the model problem, conditional expectations
    from prior data, the Markovian term, the orthogonal dynamics and the
    Volterra equation for the memory, the short-memory approximation, the
    t-damping equation and Theorem 8.1 with its proof, the conclusions),
    and the reference list. Several displayed equations were garbled by
    extraction and were reconstructed from the prose and by re-deriving
    them; the model problem's Markovian term, its t-damping term, the
    constants c = 0.715 and Z = 0.78964, the O(t³) step of §7 and Theorem
    8.1 were re-derived or recomputed here. Figures 5, 6 and 7 were read
    from page images; Figures 1–4 from captions and text only. The cited
    existence proof for the orthogonal dynamics (Givon, Hald and
    Kupferman, preprint 2001) and the cited convergence proof (Hald and
    Kupferman 2001) were not read.
date: '2026-10-20'
summary: >-
  Writes the resolved components of an ODE with random unresolved initial
  data as an exact generalized Langevin equation (Markovian term, memory,
  noise) under three projections, and approximates the memory two ways: by
  solving a Volterra equation for its expansion coefficients from
  Monte Carlo correlation functions, and by the t-damping (t-model)
  equation dΦ/dt = R(Φ) + tS(Φ), which needs no prior data. On one
  4-variable Hamiltonian example both restore the decay of the conditional
  mean that the Markovian truncation misses, the Volterra scheme to about
  t ≈ 8. No error bound for any approximation, and no Markovian
  augmentation.
---
<!-- inactive-ok-file: THEORY-257 CLAIM-327 CLAIM-157 — Proposed; open claims and readings this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpai9kc LIT-tmpvihtb — Deferred; works registered unread when this was written, cited as open -->

# NOTE-tmpi32zs: Chorin, Hald and Kupferman — Optimal prediction with memory

## Contribution

It turns the Mori–Zwanzig identity into a computational scheme for the
best estimate of a few variables of a system whose other initial values
are known only in distribution. The earlier "first-order optimal
prediction" keeps only the Markovian term and is accurate only for short
times. This paper keeps the memory term and gives three ways to evaluate
it: a Volterra integral equation whose inputs are equilibrium time
correlation functions, a short-memory approximation that replaces the
orthogonal dynamics by the full flow, and the t-damping equation, in which
"all that remains of the memory is the coefficient t". For the t-damping
equation it proves that the effective energy of the resolved variables
decreases when the Hamiltonian separates into kinetic and potential parts
(Theorem 8.1).

## Key insight

What the eliminated variables leave behind is not a fixed error but a loss
of information that grows with time. The Markovian equation for the
conditional mean is Hamiltonian, so it oscillates forever, while the true
conditional mean decays, because the partial initial data predict less and
less. The memory term is what carries that decay. At leading order it is a
damping whose strength grows linearly in time, tS(Φ), and it can be read
off the projection at a single instant without any history.

## Assumptions

- **System.** A finite system of ODEs dϕ/dt = R(ϕ), ϕ(0) = x ∈ ℝⁿ, with the
  first m components resolved, x = (x̂, x̃). Infinite-dimensional (PDE)
  cases are referred to Hopf's functional methods and not treated.
- **Initial uncertainty.** x is drawn from a probability density ρ; the
  unresolved x̃ is distributed by ρ conditioned on the known x̂. The
  examples use the canonical density ρ = Z⁻¹e^{−H} of a Hamiltonian
  system, under which the Liouville operator L = Σ Rᵢ∂ᵢ is skew-adjoint in
  L²(ρ). ρ is invariant only in the Hamiltonian/canonical case; the general
  formalism uses ρ as the initial law, not as an invariant measure.
- **Projections.** Any orthogonal projection P of L²(ρ) onto functions of
  x̂: (1) the conditional expectation E[f | x̂]; (2) the linear projection
  onto span{x₁, …, x_m} of statistical mechanics; (3) a finite-rank
  projection onto M orthonormal functions h^ν(x̂), which interpolates
  between the two.
- **Existence of the orthogonal dynamics** e^{tQL} is assumed, with a proof
  cited from a preprint (Givon, Hald and Kupferman).
- **Approximations taken without control.** P R(ϕ̂) ≈ R(Pϕ̂), commuting the
  average with a nonlinear function ("the reader should not be horrified");
  e^{tQL} ≈ e^{tL} for the short-memory and t-damping forms; a truncated
  Hermite basis (21 functions, α = 7/6) and 10⁴ Monte Carlo samples for the
  Volterra scheme.
- **Theorem 8.1 needs more**: P is the conditional expectation (not the
  linear or finite-rank projection), H(q, p) = T(p) + V(q), the canonical
  density, every resolved coordinate resolved with its conjugate momentum,
  and t ≥ 0.

## Key results

- **The generalized Langevin equation (6)**, an identity for each resolved
  component:
  ∂ₜϕⱼ(x, t) = R̄ⱼ(ϕ̂(x, t)) + ∫₀ᵗ Kⱼ(ϕ̂(x, t − s), s) ds + Fⱼ(x, t),
  with R̄ⱼ = P Rⱼ, noise Fⱼ(x, t) = e^{tQL}QLxⱼ (the solution of the
  orthogonal dynamics equation (4), ∂ₜw = QLw), and kernel
  Kⱼ(x̂, t) = PLFⱼ(x, t). It follows from the Dyson formula
  e^{tL} = e^{tQL} + ∫₀ᵗ e^{(t−s)L}PL e^{sQL} ds. The noise stays in the
  null space of P for all t. Applying P gives (7), whose left side, for the
  conditional expectation, is exactly ∂ₜE[ϕ̂(x, t) | x̂]. The kernel is a
  functional of the noise, which the paper calls a fluctuation–dissipation
  relation; the textbook form arises for the linear projection.
- **Model problem (8).** Two oscillators with H = ½(x₁² + x₂² + x₃² + x₄² +
  x₁²x₃²), (x₁, x₂) and (x₃, x₄) canonical pairs, resolving x̂ = (x₁, x₂),
  canonical initial law, x̂(0) = (1, 0). Re-derived here: given x₁, x₃ is
  N(0, 1/(1 + x₁²)), so the Markovian term is
  R̄ = (x₂, −x₁(1 + 1/(1 + x₁²))). The constants c = (x₁, x₁) = 0.715 and
  Z = 0.78964 were recomputed (0.71538, 0.789640).
- **First-order optimal prediction (16)–(17)** drops memory and noise:
  dΦ/dt = R̄(Φ). It is Hamilton's equation for the effective Hamiltonian
  ℋ(x̂) = −log∫e^{−H}dx̃ when resolved variables come in conjugate pairs.
  Fig. 5: it oscillates with undiminished amplitude while the true mean
  decays; the two part after the first trough (t ≈ 2.5).
- **Memory from correlation functions (§6).** Expanding Kⱼ(x̂, s) =
  Σ_ν aⱼ^ν(s)h^ν(x̂) under a finite-rank P, the coefficients solve the
  Volterra equation (21),
  aⱼ^μ(t) = fⱼ^μ(t) − ∫₀ᵗ Σ_ν aⱼ^ν(s)g^{νμ}(t − s) ds,
  with fⱼ^μ(t) = (Le^{tL}Fⱼ(0), h^μ) and g^{νμ}(t) = (Le^{tL}h^ν, h^μ). These
  are equilibrium time-correlation functions, computable by averaging over
  simulations or experiments with no reference to the orthogonal
  dynamics. The reduced equations are (22),
  dΦ/dt = R̄(Φ) + ∫₀ᵗ A(s)h(Φ(t − s)) ds, or (23), with the history replaced
  by Γ(t − s)h(x̂). Fig. 6 (read from the page image): both track the true
  mean closely through the first one and a half oscillations, to t ≈ 8;
  after that they keep oscillating at amplitude about 0.3 while the true
  mean has fallen to about 0.1 (t ≈ 10–16). The paper gives no error
  measure.
- **Short memory (§7).** Replacing e^{sQL} by e^{sL} inside the memory
  integral changes it by O(t³), because e^{sQL} − e^{sL} = −sPL + O(s²) and
  the first-order term is killed by QP = 0. Checked here. This is a
  small-t statement, not a bound for a fixed horizon.
- **t-damping (26)–(27).** Taking the integrand at s = 0 over the whole
  interval gives ∫₀ᵗ Kⱼ(ϕ̂(t), 0) ds = tSⱼ(ϕ̂(t)), Sⱼ = PLQLxⱼ, so
  dΦ/dt = R̄(Φ) + tS(Φ). For the model, re-derived here,
  S = (0, −2x₁²x₂/(1 + x₁²)²), the paper's (28). Fig. 7: the t-damped
  solution decays to near zero over t ≲ 120 as the true mean does, with
  visibly different phase and amplitude.
- **Theorem 8.1.** Under the t-damping equation with separable H,
  dℋ/dt = −t P[(Σⱼ(H_pⱼ − ℋ_pⱼ)ℋ_qⱼ)²] − t P[(Σⱼ(H_qⱼ − ℋ_qⱼ)ℋ_pⱼ)²] ≤ 0,
  sums over the resolved j. Re-derived step by step in [THEORY-tmpepvai](../theory.d/THEORY-tmpepvai.md). For
  the model the right side is −2t x₁²x₂²/(1 + x₁²)², which checks against
  dℋ/dt computed directly from (28).
- **Prior data (§4).** E[ϕⱼ(x, t) | x̂] ≈ Σ_ν cⱼ^ν(t)h^ν(x̂), with cⱼ^ν(t)
  estimated from an ensemble of solutions: a regression of the future on
  the resolved initial data. Scaled Hermite bases converge slowly; 3 × 3
  functions depart early, 6 × 6 hold "for a long time", and rescaling α
  cuts the cost (Fig. 4).

**Re-check of the horizons (not the paper's).** The model was integrated
here with 2 × 10⁴ Monte Carlo samples (x₃ ~ N(0, ½), x₄ ~ N(0, 1)). The
true mean reproduces Fig. 5's curve (0.625 at t = 5.2, −0.351 at 7.8, 0.138
at 10.4). The first error above 0.1 comes at t ≈ 1.7 for first-order
prediction and t ≈ 2.25 for t-damping. RMS errors over [0, T]:

| T | first-order (17) | t-damping (28) | predicting 0 |
|---|---|---|---|
| 2 | 0.062 | 0.022 | 0.630 |
| 4 | 0.100 | 0.102 | 0.644 |
| 8 | 0.325 | 0.146 | 0.536 |
| 16 | 0.521 | 0.140 | 0.387 |
| 30 | 0.571 | 0.137 | 0.293 |

So the t-model is no better than the Markovian equation to t ≈ 4 (it
over-damps the first peak, 0.39 against 0.63) and much better after; past
t ≈ 12 the Markovian prediction is worse than predicting the equilibrium
mean, 0. The full memory scheme of Fig. 6 is the only one that is accurate
over the first peaks.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The resolved variables obey exactly a generalized Langevin equation, Markovian term plus memory plus noise, for any of the three projections, and the projected form gives the time derivative of the conditional mean | strong | Dyson formula, checked by differentiation; existence of e^{tQL} cited from a preprint |
| C2 | Accurate prediction of a subset of variables over longer times "requires the addition of a 'memory' term" | moderate | one 4-variable example (Figs. 5–7); the cited reasons are in earlier papers |
| C3 | The memory kernel can be computed from equilibrium time-correlation functions through a Volterra equation, without solving the orthogonal dynamics | strong as a derivation, moderate as a method | (21); one example with 21 basis functions, accurate to t ≈ 8 |
| C4 | Replacing the orthogonal dynamics by the full flow changes the memory term by O(t³) | strong for small t | Taylor argument of §7, checked here |
| C5 | At leading order the memory is tS(Φ), and the t-damping equation needs no previously computed averages | strong as a derivation of the equation; weak as an approximation | (26)–(27); no error estimate, one example with phase and amplitude error |
| C6 | With separable H and the conditional expectation, the t-damping equation makes the effective Hamiltonian non-increasing | strong | Theorem 8.1 with proof, re-derived in [THEORY-tmpepvai](../theory.d/THEORY-tmpepvai.md) |
| C7 | "The result of the computations is close to the best possible estimate that can be obtained given the partial data" (abstract) | weak | Fig. 6 holds to t ≈ 8 and then misses the amplitude by a factor of about three; no error measure is given |
| C8 | First-order optimal prediction is "optimal in the class of Markovian approximations" | not assessed | cited from Hald and Kupferman (2001), not read |

## Method

1. Choose the resolved variables x̂ and a projection P.
2. The Markovian term R̄ = PR: by direct integration when P is the
   conditional expectation, else by projecting stored samples.
3. The memory, by one of:
   - (a) estimating fⱼ^μ, g^{νμ} and γ^{νμ} from an ensemble of full
     simulations from the initial law, solving the Volterra equation (21)
     for A(t) by the trapezoidal rule, and integrating (22) or (23);
   - (b) the short-memory form, with e^{sL} in place of e^{sQL};
   - (c) the t-damping term tS(Φ), Sⱼ = PLQLxⱼ, computed analytically.
4. Integrate the reduced equation from Φ(0) = x̂ (Runge–Kutta, modified for
   the integral term). The noise is not simulated: its projection is zero.

## Concepts

- **Optimal prediction**: estimating E[ϕ̂(x, t) | x̂], the conditional mean
  of the resolved variables given their initial values, over the unknown
  initial values of the rest. The conditioning is on initial data, not on
  an observed history.
- **First-order optimal prediction**: the Markovian truncation
  dΦ/dt = PR(Φ).
- **Orthogonal dynamics**: the evolution e^{tQL}, which keeps functions in
  the null space of P there. The noise Fⱼ is its solution from QLxⱼ.
- **Memory kernel**: Kⱼ(x̂, t) = PLFⱼ(x, t), a function of x̂ and lag t.
- **Finite-rank projection**: projection onto M orthonormal functions of
  x̂, here scaled Hermite functions with scale α.
- **t-damping equation**: dΦ/dt = R̄(Φ) + tS(Φ), later called the t-model.
- **Effective Hamiltonian**: ℋ(x̂) = −log∫e^{−H(x)}dx̃, the free energy of
  the resolved variables.

## Connections

It builds on the authors' earlier first-order optimal prediction (Chorin,
Kast and Kupferman 1998–1999), on their 2000 PNAS paper connecting it to
Mori–Zwanzig ([LIT-tmpai9kc](../literature.d/LIT-tmpai9kc.md), being read concurrently), and on Mori (1965)
and Zwanzig (1973, 1980) for the projection formalism, with the nonlinear
(conditional-expectation) projection taken from Zwanzig. Its Volterra
scheme is the one sketched in "Non-Markovian optimal prediction" (2001), a
different paper. The t-model is its own new construction here. Parish and
Duraisamy ([LIT-tmpvihtb](../literature.d/LIT-tmpvihtb.md), unread) work in this line.

## Bearing on the record

- **[QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md).** It answers the part the question takes as given
  and the record lacked a reading of: that eliminating variables leaves an
  exact decomposition into a Markovian term, a memory term and noise, and
  that this decomposition depends on the projection. Three projections are
  defined and each gives a different R̄, K and F. That supports A3's
  caution that a kernel norm is not representation-invariant. It also
  shows, on one example, that the memory decides prediction beyond a
  couple of oscillations (the re-check table), and that its leading-order
  effect in a Hamiltonian system is a time-growing damping ([THEORY-tmpepvai](../theory.d/THEORY-tmpepvai.md)).
  It **does not** answer the question's main ask. There is no Markovian
  augmentation with memory coordinates anywhere in the paper, and no error
  bound for any approximation, let alone one in terms of the spectrum of
  the eliminated dynamics. The t-damping equation is Markovian only in the
  trivial sense that time itself is the added coordinate; the Volterra
  scheme keeps the full history. Its "short memory" is assumed, not
  derived from a gap. Nothing here rules on whether a level's criteria
  apply to the augmented or the instantaneous state.
- **A5's linear example in [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md).** Not in the paper, but its
  formalism places it. The kernel bc·e^{−dt} is a single exponential, so
  the memory is generated exactly by one auxiliary linear ODE; that
  coordinate is y itself, up to its noise term. So in that example the
  exact one-coordinate augmentation is just the eliminated variable.
  Nothing in this paper says when a kernel is close to a finite sum of
  exponentials, which is what a nontrivial answer would need.
- **[THEORY-257](../theory.d/THEORY-257.md) and [THEORY-733](../theory.d/THEORY-733.md).** Different conditioning. Optimal prediction
  estimates the future of x̂ from its value at time 0, averaged over an
  initial law. Dynamical independence asks whether the micro history adds
  to the coarse variable's own history in a stationary process. The memory
  term in (6) is a pathwise function of the resolved history, so a system
  with nonzero K can still be dynamically independent if the noise F adds
  nothing given that history. The paper neither states nor tests this.
  Nothing in it contradicts either entry, and it gives [THEORY-733](../theory.d/THEORY-733.md) no new
  case.
- **[CLAIM-327](../claims.d/CLAIM-327.md).** Consistent in spirit (the past of the resolved variable
  matters to its future), but the paper's memory is a mechanical
  consequence of elimination, not a variable members read. No bearing
  beyond that.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** The model problem has no scale separation (the paper says
  so in §9), so it cannot speak to gap-isolated blocks.
- **[THEORY-tmpepvai](../theory.d/THEORY-tmpepvai.md)** is filed from this reading.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No error bounds.** Not for the commutation P R(ϕ̂) ≈ R(Pϕ̂), not for the
  truncated Hermite bases, not for the short-memory replacement beyond its
  O(t³) small-t order, and not for the t-model. The paper's comparisons are
  plots of one trajectory from one initial datum, x̂ = (1, 0).
- **One example, not typical.** Four variables, two resolved, no scale
  separation; the authors say it "is not typical of the problems one
  encounters in practice".
- **The abstract overstates.** "Close to the best possible estimate" is
  true of Fig. 6 to t ≈ 8 and not after, when the amplitude is off by a
  factor of about three (C7).
- **"Short-memory approximation of particular interest" misdescribes the
  t-model.** Taking the integrand at s = 0 over all of [0, t] assumes the
  kernel does not decay over the window: a long-memory assumption, valid
  as an expansion only for t short against the memory time, and then used
  to t = 120. The paper's derivation is correct; its label is not.
- **Theorem 8.1 says less than it is used for.** A non-increasing effective
  energy shows the t-model damps, not that it damps at the right rate. The
  true conditional mean's effective energy is not monotone: in the re-check,
  ℋ of the Monte Carlo mean is 0.0091 at t = 15 and 0.0273 at t = 25, and
  the mean keeps a residual oscillation of about 0.1 (as Fig. 5 shows),
  while the t-damped solution goes to rest.
- **"Optimal" is relative to the initial law.** The conditional mean is
  the best L² estimate given x̂ under ρ; with a different initial law (the
  authors name the microcanonical one) the target changes, and this is not
  explored.
- **The noise term is dropped by projection, not modelled.** The scheme
  predicts the mean, not trajectories or their spread.
- **Existence of the orthogonal dynamics** rests on a cited preprint, not
  read here.
- Figures 1–4 were read from captions only.

## Open questions

- For what class of systems is the memory kernel, under a given
  projection, close in some norm to a finite sum of exponentials, so that
  k auxiliary linear coordinates reproduce it with a stated error? That is
  [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md)'s ask, and this paper's machinery (the Volterra
  equation for A(t)) gives the kernel numerically but not that bound.
- What controls the validity of the t-model: the ratio of the prediction
  horizon to the memory time, and how could that ratio be estimated from
  the correlation functions fⱼ and g^{νμ} before the model is used?
- Does a gap in the spectrum of the unresolved dynamics make the kernel
  short in the sense §7 assumes, and with what bound? Scale separation is
  named in §9 as helpful and not treated.
