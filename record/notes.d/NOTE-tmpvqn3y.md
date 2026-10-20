---
status: Read
paper: 'LIT-tmpg4fmr'
title: 'Nadler, Lafon, Coifman and Kevrekidis — Diffusion maps and reaction coordinates'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:math/0503445v1 (20 pages, the only arXiv
    version), text extracted with pdftotext. Every section was read: the
    abstract, §1, §2 (the two scenarios, equations (1)–(8)), §3 (finite
    data, the continuum operators (12)–(20), the generators (21)–(22) and
    the Schrödinger correspondence (23)–(26)), §4 (the α-family, (27)–(30)),
    §5 (Ornstein–Uhlenbeck in one and n dimensions with the Lemma, the
    double well (35)–(37), three wells (38), the iris data), §6 and
    Appendix A. Pages 10 and 18, which hold (27)–(28) and the appendix,
    were checked against page renders. Figures 1–4 were read from captions
    and text. The published ACHA version was sought and not reached
    (ScienceDirect returned a bot check, HTTP 403, and the Elsevier API
    HTTP 429), so differences from the preprint are unknown. The Lemma's
    spectrum, the generator constants, the α-family conjugation, the §5.2
    condition and the double-well behaviour were checked by hand and with
    numpy scripts in
    /tmp/claude-0/-home-user-nucleation/409f735e-c44b-5ba1-82f0-18d34af58efc/scratchpad/nadler-scripts/
    (check.py, dw_more.py, closure.py).
date: '2026-10-20'
summary: >-
  Ties diffusion maps to the dynamics that generated the data. For samples
  from p = e^{−U}, the small-ε generator of the α-normalized walk is
  Δψ − 2(1 − α)∇ψ·∇U: the graph Laplacian (α = 0) gives Fokker–Planck with
  potential 2U, α = 1/2 gives the Langevin dynamics with potential U itself,
  and α = 1 gives Laplace–Beltrami. So the slow eigenfunctions of the α = 1/2
  map approximate the slow modes of the sampled stochastic system, and the
  paper proposes them as reaction coordinates. The expansions are formal, and
  with the paper's kernel every printed generator is too large by a factor of
  two. Its double-well example is separable. From equilibrium samples the
  slow eigenfunction is recovered well and the slow eigenvalue is not. That
  slow eigenfunctions are closed in mean, and in law only under a condition,
  is the record's addition.
---
<!-- inactive-ok-file: THEORY-tmp3j6t7 CLAIM-157 CLAIM-331 THEORY-257 — Proposed; the α-family limit this paper restates and open claims it bears on, nothing here rests on their being settled -->
# NOTE-tmpvqn3y: Nadler, Lafon, Coifman and Kevrekidis — Diffusion maps and reaction coordinates

## Contribution

It reads the eigenvectors of graph-Laplacian random walks as discrete
approximations of eigenfunctions of differential operators fixed by the
sampling density p = e^{−U}. It names which operator each normalization
gives. The ordinary normalized graph Laplacian gives a Fokker–Planck
generator with potential 2U, not U. A new anisotropic normalization, α = 1/2,
gives the backward Fokker–Planck generator of the Langevin dynamics
ẋ = −∇U + √2ẇ whose equilibrium the samples come from. That makes the
leading diffusion-map coordinates candidates for the slow variables, or
reaction coordinates, of the sampled stochastic system. It also explains the
Horn–Gottlieb "quantum clustering" potential as |∇U|² − ΔU.

## Key insight

A random walk on samples sees two things at once: the geometry of where the
points lie and how densely they lie there. The normalization decides how
much of the density enters the walk's drift. With no correction, the density
is counted twice: once by where the points are, and once by the walk
favouring dense neighbours. So the walk behaves as if the potential were 2U.
Dividing the kernel by p_ε^α at both ends removes a share of that. At
α = 1/2 exactly one copy remains, and the walk's generator is the dynamics
that produced the equilibrium. If the data come from a stochastic system in
equilibrium, the slow modes of the right walk are the system's slow modes.

## Assumptions

- **Data.** N points, i.i.d. from p = e^{−U} on ℝⁿ (or on a submanifold,
  in the appendix), either with no dynamics or from the equilibrium of the
  Langevin equation (2) with isotropic unit-temperature noise. Gradient
  drift, reversible dynamics and equilibrium sampling are all assumed.
- **Kernel.** Gaussian, k_ε = exp(−‖x − y‖²/2ε), with one jump of the walk
  taken as time ε.
- **Limits.** N → ∞ first, at fixed ε (cited: von Luxburg, Bousquet and
  Belkin; Hein, Audibert and von Luxburg), then ε → 0 by formal asymptotic
  expansion. The manifold case borrows the expansion
  ∫k_εφ = φ + ε(Δφ + qφ) + O(ε^{3/2}) from Coifman and Lafon, with k_ε
  "scaled appropriately".
- **Δ is ∇²** (a negative operator) throughout, the opposite of Coifman and
  Lafon's convention.

## Key results

- **(15).** p_ε(x) = p(x) + (ε/2)Δp(x) + O(ε^{3/2}), for the kernel
  normalized by (2πε)^{−n/2}.
- **(19).** T_f and T_b are adjoint in L²(μ), and T_s is self-adjoint. All
  three share eigenvalues, with eigenfunctions related by √p_ε:
  φ_f = √p_ε φ_s and φ_b = φ_s/√p_ε.
- **(21)–(22), α = 0.** H_f φ = Δφ − φ e^U Δe^{−U} and
  H_b ψ = Δψ − 2∇ψ·∇U, the backward generator with potential 2U. **(23)–(24)**:
  H_f is the Schrödinger operator Δφ − Vφ with V = |∇U|² − ΔU.
  **(25)–(26)**: p = ψe^{−U/2} turns the Fokker–Planck equation (3) into
  imaginary-time Schrödinger with potential |∇U|²/4 − ΔU/2. Comparing the
  two, (21) has the spectrum of Fokker–Planck with potential 2U. Checked:
  V for 2U is |∇U|² − ΔU.
- **(27)–(28), the α-family.** H_b^(α)ψ = Δψ − 2(1 − α)∇ψ·∇U and
  H_f^(α)φ = Δφ − 2α∇φ·∇U + (2α − 1)φ(|∇U|² − ΔU). Checked here: they are
  conjugate, H_f^(α)φ = e^{−(1−2α)U}H_b^(α)(e^{(1−2α)U}φ), because
  d_ε^(α) ≈ p^{1−2α}. At α = 1/2 they coincide (30): Δψ − ∇ψ·∇U, the
  backward Fokker–Planck operator (5). At α = 1, H_b = Δ (29),
  Laplace–Beltrami. The record's [THEORY-tmp3j6t7](../theory.d/THEORY-tmp3j6t7.md) has the same family from
  Coifman and Lafon, with the drift −2(1 − α)∇U and invariant density
  p^{2(1−α)}.
- **Lemma (§5.1), Ornstein–Uhlenbeck at finite ε.** For U = x²/2τ, T_s has
  eigenvalues λ_k = (τ/(τ + ε))^k and eigenfunctions
  p_k(x)exp(−x²/4(τ + ε)), p_k a polynomial of degree k. Checked by
  quadrature (τ = 1, ε = 0.1): 1, 0.90909, 0.82645, 0.75131, 0.68301,
  matching to five places.
- **§5.2, separable harmonic potential.** λ_{i,j} = μ₁^iμ₂^j with
  μ_j = τ_j/(τ_j + ε). If τ₁ ≫ τ₂, the first non-trivial eigenfunctions
  φ_{1,0}, φ_{2,0}, … all depend on the slow variable x₁ only: a
  "(redundant) parametrization" of one slow variable. Fig. 1: ψ₂ against ψ₁
  is a parabola.
- **§5.3, double well.** ψ₁ ≈ (φ_L − φ_R)/(φ_L + φ_R), about +1 in one well
  and −1 in the other. Its sign is asymptotically the Bayes classifier for
  a two-Gaussian mixture. In the 2D example (37),
  U = x⁴/4 − 25x³/12 + 9x²/2 + 25y²/2, with minima at x = 0 and x = 4 and a
  barrier at x = 2.25, ψ₁ is "essentially a function of only x", and
  ψ₁, ψ₂, ψ₃ lie on a curve (Fig. 2).
- **§5.4, three wells (38).** At β = 2 the first two coordinates form a
  triangle whose vertices are the wells, showing a direct and an indirect
  path between the deep wells (Fig. 3).
- **§5.5, iris.** One class collapses to a point; the sign of ψ₁ on the
  other two misclassifies 6–8 of 100 samples, depending on ε.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The α-normalized walk has small-ε backward generator Δψ − 2(1 − α)∇ψ·∇U | moderate: formal expansion; the constant is off by a factor 2 for the stated kernel | §4 and Appendix A, which rests on Coifman and Lafon's kernel expansion; rigorous version in [THEORY-tmp3j6t7](../theory.d/THEORY-tmp3j6t7.md), Proposed |
| C2 | The normalized graph Laplacian corresponds to Fokker–Planck with potential 2U | moderate, same caveat | (21)–(26); the conjugation checked here |
| C3 | α = 1/2 recovers the eigenvalues and eigenfunctions of the Langevin dynamics with potential U | moderate for the operator; the eigenvalues only up to the factor 2 | (30); checked on samples here (see Limitations) |
| C4 | "As the number of samples goes to infinity, the eigenvectors … converge to the eigenfunctions" (abstract) | weak as stated | no spectral convergence is shown; N → ∞ is cited, ε → 0 is a formal operator expansion |
| C5 | The finite-ε Ornstein–Uhlenbeck spectrum is λ_k = (τ/(τ + ε))^k | strong | the Lemma; checked by quadrature |
| C6 | For τ₁ ≫ τ₂ the first eigenfunctions parametrize only the slow variable, "as long as τ₂ > 2τ₁", "regardless of the value of ε" | weak as printed | the inequality is reversed and depends on ε (see Limitations) |
| C7 | In a double well, ψ₁ ≈ ±1 on the wells, and its eigenvalue is governed by the mean passage time | moderate for the eigenfunction, weak for the eigenvalue from data | heuristic tight-binding argument ("as is well known"); checked numerically here |
| C8 | Diffusion maps are "data-driven or equation-free homogenization" and allow fast simulation along slow coordinates | weak | asserted; deferred to a paper "in preparation" |

## Method

Build a Gaussian kernel on the samples, estimate the density by
p_ε = Σ_i k_ε(·, x_i), divide the kernel by p_ε^α at both ends, row-normalize
to a Markov matrix, and take its leading eigenvectors. The diffusion map at
time m is x ↦ (λ_j^m ψ_j(x))_j. The analysis replaces sums by integrals
against p (N → ∞), expands the integrals for small ε, and reads off the
generator lim (T − I)/ε.

## Concepts

- **Forward, backward and symmetric Chapman–Kolmogorov operators**
  (16)–(18): T_f evolves densities, T_b expectations, and T_s is their
  symmetric conjugate, all in L²(μ).
- **Infinitesimal generator**: H = lim_{ε→0}(T − I)/ε, with one jump taken
  as time ε.
- **Anisotropic diffusion map**: the walk on the kernel
  k_ε/(p_ε^α ⊗ p_ε^α). "Anisotropic" refers to the density weighting, not
  to a direction-dependent kernel.
- **Reaction coordinate**: a low-dimensional function of the state that
  captures the slow, long-time evolution, here the leading non-trivial
  eigenfunctions.

## Connections

It extends Coifman and Lafon's diffusion maps ([LIT-tmpc7k0w](../literature.d/LIT-tmpc7k0w.md), [NOTE-tmpv8yf2](NOTE-tmpv8yf2.md);
the PNAS announcement [LIT-981](../literature.d/LIT-981.md)) toward stochastic dynamics. That paper's
§3.3 cites this one for the α = 1/2 conjugation. On the dynamics side it
cites Huisinga, Schütte and co-workers on metastable conformations,
Givon, Kupferman and Stuart on extracting macroscopic dynamics, and
Kevrekidis's equation-free framework. On the data side: Shi and Malik's
normalized cuts, Ng, Jordan and Weiss on spectral clustering, Belkin and
Niyogi's eigenmaps, and Horn and Gottlieb's quantum clustering. The
supersymmetric Fokker–Planck–Schrödinger correspondence is Bernstein and
Brown's.

## Bearing on the record

- **[THEORY-tmpvmmpz](../theory.d/THEORY-tmpvmmpz.md)** is filed from this reading, Active. The paper
  calls slow eigenfunctions reaction coordinates and says nothing on
  whether they are closed. The record's answer: for a reversible diffusion
  in equilibrium, every generator eigenfunction is exactly closed in
  conditional mean, E[ψ(X_{t+s}) | past] = e^{−λs}ψ(X_t), with no memory
  given either the full past or ψ's own. It is closed in law, a Markov
  process, only when |∇ψ|² is a function of ψ. A 2D Ornstein–Uhlenbeck
  simulation shows both behaviours (x₁ and x₁² closed; x₁x₂ not).
- **[QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md): answers in part.** "Do slow eigenfunctions of a sampled
  Fokker–Planck operator give closed coarse variables?" In the mean, yes,
  exactly, for the true eigenfunctions. In law, only under the gradient
  condition. The memory, when there is any, sits in the noise intensity,
  and one extra coordinate, |∇ψ|², carries it. All the paper's analysed
  examples meet the condition. In §5.2 the eigenfunctions are Hermite
  polynomials of x₁, and in §5.3 the potential (37) is separable, so x
  evolves autonomously and ψ₁(x) is closed by construction. Fig. 2's
  "ψ₁ is essentially a function of only x" is therefore not a test of
  reduction. The three-well potential (38), which is not separable, is
  shown and not analysed.
- **[CLAIM-164](../claims.d/CLAIM-164.md).** §5.2 supplies a case the claim should carry. The gap
  above the slow cluster picks out a subspace, and here that subspace is
  spanned by φ_{1,0}, φ_{2,0}, …, all functions of one variable x₁. So the
  dimension of a gap-isolated slow subspace is not the number of slow
  variables. The subspace is a definite object, as the claim says, but
  counting its eigenvectors overcounts degrees of freedom. The record
  might add that as a note.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** §5.3 is the heuristic link between a spectral gap and
  metastable clusters that [NOTE-tmpv8yf2](NOTE-tmpv8yf2.md) sent the record here to find. It
  is heuristic here as well: the two-well eigenfunction is "well known" and
  not derived, and no bound ties the gap to escape times. Numerically, for
  (37) the generator's slow eigenvalue is 0.049 and the next 3.38. With
  α = 1/2 on 2,000–5,000 equilibrium samples, sign(ψ₁) put 99.6–99.8% of
  points in their own well, and ψ₁ was uncorrelated with y (|r| < 0.01).
  But the estimated slow eigenvalue, after correcting the factor 2, was
  0.010–0.034 over ε = 0.02–0.2, low by 30–80%. Only 4–19 samples lay within 0.25 of the
  barrier, and the inter-well rate is set by the density there. So
  equilibrium data identify the metastable blocks well and their lifetime
  poorly. That bears on [CLAIM-157](../claims.d/CLAIM-157.md)'s "lasts as long as that block
  persists": a data-driven gap gives the block, not its duration. The
  rigorous gap–metastability link (Huisinga and Schütte, Bovier and
  co-workers) is not held.
- **[THEORY-tmp3j6t7](../theory.d/THEORY-tmp3j6t7.md).** This paper states the same α-family, by a formal
  expansion borrowed from Coifman and Lafon. It adds no proof, so it does
  not meet that entry's promote_when. Its constants differ: with
  k_ε = exp(−‖x − y‖²/2ε), whose second moment is ε, the generator is half
  that entry's, since that entry scales the kernel to second moment 2. The
  two agree once time is rescaled.
- **[CLAIM-331](../claims.d/CLAIM-331.md) and [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md).** Ordering coordinates by eigenvalue
  orders them by decay rate. §5.2 shows that this order interleaves
  harmonics of one slow variable (rates k/τ₁) with the first fast variable
  (1/τ₂). So an "operator order" of coarse-to-fine coordinates is an order
  of timescales, not of independent variables.
- **[THEORY-257](../theory.d/THEORY-257.md).** An eigenfunction that fails the gradient condition is
  not dynamically independent in law, though its mean is closed. That
  sharpens the sense in which memory "is not automatically a violation".
- **The anthology.** It carries no instruction for machine-learning
  practice. Its spectral-clustering half is a topic the anthology could
  hold, so the LIT carries the `anthology-candidate` flag, as its companion
  [LIT-tmpc7k0w](../literature.d/LIT-tmpc7k0w.md) does.

## Limitations

- **A factor of two in every generator.** With the kernel (9) and one jump
  taken as time ε, (15) gives T_bψ = ψ + (ε/2)(Δψ − 2∇ψ·∇U) + O(ε^{3/2}).
  So H_b = ½(Δψ − 2∇ψ·∇U), not (22), and likewise for (21) and (27)–(30).
  The paper's own examples disagree with each other by this factor. The
  Lemma's λ₁ = τ/(τ + ε) gives a rate (1 − λ₁)/ε → 1/τ, while (32), the
  α = 0 backward generator for the same potential, has eigenvalue 2/τ for
  ψ = x. On 2,500 samples of N(0, 1), (1 − λ₁)/ε was 0.94 at α = 0 and 0.50
  at α = 1/2, against 1 and ½ with the factor and 2 and 1 without it. The
  appendix avoids the issue by taking the kernel "scaled appropriately",
  which is not the kernel (9). Eigenfunctions are unaffected; eigenvalues
  and time scales are halved.
- **The definition of H_f has the wrong sign.** It is printed as
  lim (I − T_f)/ε, while H_b is lim (T_b − I)/ε. (21) is the limit of
  (T_f − I)/ε.
- **§5.2's condition is reversed.** "As long as τ₂ > 2τ₁, we have
  λ₁² > λ₂" contradicts the assumption τ₁ ≫ τ₂. Exactly, μ₁² > μ₂ iff
  τ₁(τ₁ − 2τ₂) > τ₂ε, so roughly τ₁ > 2τ₂, and it does depend on ε, unlike
  the claim "regardless of the value of ε".
- **"Converge" is formal.** The abstract says the eigenvectors converge to
  eigenfunctions. The paper shows pointwise expansions of the operators on
  smooth functions, cites others for N → ∞ at fixed ε, and proves no
  spectral convergence.
- **The double-well reasoning is heuristic.** The approximate eigenfunction
  is "well known" from tight binding. No bound links λ₁ to the passage
  time, and §5.3 writes U ≈ (x − x_L)²/τ_L and then e^{−(y−x_L)²/2τ_L}, a
  factor 2 apart.
- **Small slips.** (27) writes ∇φ for ∇ψ. §3.1 says N − 1 further
  eigenvalues as "n − 1", n being the dimension. §6's fast-simulation
  programme and the "equation-free homogenization" reading are deferred to
  a paper "in preparation".
- **Scope.** Equilibrium samples of a reversible gradient diffusion with
  unit isotropic noise. Non-equilibrium data, anisotropic or
  state-dependent noise, and non-gradient drift are outside it, and the
  α = 1/2 identification does not hold for them.
- **Published version not compared.** The ACHA text may correct some of
  the above.

## Open questions

- For a non-separable potential such as (38), how far is the leading
  eigenfunction from being closed in law, measured by how far |∇ψ₁|² is
  from a function of ψ₁? [THEORY-tmpvmmpz](../theory.d/THEORY-tmpvmmpz.md) gives the criterion; nobody has
  measured it on the paper's example.
- How many equilibrium samples near a barrier are needed to estimate the
  slow rate within a factor, as a function of the barrier height? The
  numbers here suggest the requirement is set by the barrier density, not
  by N overall.
- Does the gap-isolated slow subspace have a canonical "number of slow
  variables", for instance the dimension of the image of the map
  x ↦ (ψ₁, …, ψ_k)(x), rather than k? §5.2's parabola is a one-dimensional
  curve in a two-dimensional embedding.
