---
status: Read
paper: 'LIT-1232'
title: 'Chizat and Bach — Global convergence of gradient descent for over-parameterized models using optimal transport'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read on 2026-10-29 from arXiv 1805.09545v2 (29 October 2018,
    https://arxiv.org/pdf/1805.09545, 32 pages: the NeurIPS 2018 paper and
    its supplement), text extracted with pdftotext. Read in full: the
    main paper (§§1–5, Figures 1–3 captions, references). Read in the
    supplement: Appendix C.1 (optimality conditions), C.2.1 (the escape
    criterion, 2-homogeneous case, with Lemmas C.2–C.3), the opening of
    C.3 and C.3.1 (stability of the separation property, statements
    only), C.4 and C.4.1 (Lemma C.15, Theorem C.16 and its proof), C.5
    (remarks) and D.5 (experiment details). Not read: Appendix A, B (the
    many-particle limit and Wasserstein gradient-flow theory), C.2.2,
    C.3.2, C.4.2 (the partially 1-homogeneous proofs) and D.1–D.4. So the
    main theorems are read with the 2-homogeneous proof and the
    1-homogeneous one is taken on trust. Figures were read from captions;
    no number was taken from a chart.
date: '2026-10-29'
summary: >-
  Training a sum of many units by gradient descent is, as the number of
  units grows, a Wasserstein gradient flow of a convex functional of the
  measure over unit parameters. A measure is a global minimizer exactly
  when the first variation F′(µ) is nonnegative everywhere and zero on its
  support. Under 2-homogeneity or partial 1-homogeneity, and an
  initialization whose support separates the domain, any limit of the flow
  is global, because mass in any region where F′ < 0 grows exponentially.
  The result is conditional on convergence and non-quantitative.
---

# NOTE-tmpbs06i: Chizat and Bach — Global convergence of gradient descent for over-parameterized models using optimal transport

## Contribution

It shows when particle gradient descent on a non-convex finite problem
inherits the global optimality of the convex problem in measures that the
particles discretize. It proves the many-particle limit is a Wasserstein
gradient flow (Theorem 2.6), characterizes global minimizers (Proposition
3.1), and proves that, with homogeneity and a separating initialization,
limits of the flow are global minimizers (Theorems 3.3, 3.5), covering
sparse deconvolution and one-hidden-layer networks with sigmoid or
(reparameterized) ReLU units.

## Key insight

A stationary point of the particle flow only needs F′(µ) flat on the
units present; a global minimizer also needs F′(µ) ≥ 0 where no unit is.
A non-optimal stationary point is one where some unoccupied direction
would pay. Homogeneity turns that into exponential growth of any mass
already there, and a separating initialization guarantees that some mass,
however small, is always there.

## Assumptions

- F(µ) = R(∫Φ dµ) + ∫V dµ over nonnegative measures on Ω ⊂ ℝᵈ, R convex,
  differentiable, with dR Lipschitz on bounded sets (Assumptions 2.1,
  3.2(i), 3.4(i)).
- **2-homogeneous case** (3.2): Ω = ℝᵈ, Φ and V positively 2-homogeneous,
  a Sard-type regularity on the sphere.
- **Partially 1-homogeneous case** (3.4): Φ(w, θ) = wφ(θ), V = |w|Ṽ(θ),
  φ and Ṽ bounded with Lipschitz differentials, boundary conditions.
- **Initialization**: the support of µ0 separates r_a S^{d−1} from r_b
  S^{d−1} (2-homogeneous), or {−r0} × Θ from {r0} × Θ (1-homogeneous),
  for example all of {0} × Θ.
- **Convergence of the flow** is assumed, not proved (§3, C.5).

## Key results

- **Theorem 2.6.** If the initial empirical measures converge in W2, the
  particle flows converge to the unique Wasserstein gradient flow of F.
- **Proposition 3.1.** With R convex, µ minimizes F over M₊(Ω) iff F′(µ)
  ≥ 0 on Ω and F′(µ) = 0 µ-a.e., where F′(µ)(u) = ⟨R′(∫Φ dµ), Φ(u)⟩ + V(u).
- **Proposition C.1 (escape).** If F′(µ) is negative somewhere, take K the
  (−η)-sublevel set of F′(µ) on the sphere. Near µ, particles in the cone
  over K have radial speed at least rη, so |u_t| ≥ |u_0|e^{ηt} and the
  mass h₂(µ_t)(K) grows exponentially until the flow leaves µ's
  neighbourhood.
- **Theorems 3.3, 3.5.** Under the homogeneity, regularity and
  separation assumptions, if µ_t converges (or a projection of it
  converges weakly, Theorems C.16–C.17), the limit is a global minimizer,
  and lim F(µ_{m,t}) = F* with the limits in m and t interchangeable.
- **Experiments.** Sparse deconvolution on the 1-torus fails with 6
  particles and succeeds with 10 and 100 (Fig. 1); D.5 says success for
  more than 7. ReLU and sigmoid networks in d = 100 need "a slight
  over-parameterization m > m0" with particles moving, against an
  exponential number for weights-only convex optimization on a fixed
  grid (Fig. 3).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The many-particle limit of particle gradient flow is a Wasserstein gradient flow | strong | Theorem 2.6 (proof in Appendix B, not read) |
| C2 | Global minimizers are characterized by F′ ≥ 0 everywhere, = 0 on the support | strong | Proposition 3.1, proof read |
| C3 | Limits of the flow are global minimizers under homogeneity and separating initialization | strong, conditional on convergence | Theorems 3.3, 3.5; 2-homogeneous proof read |
| C4 | Slight over-parameterization suffices in practice | weak | synthetic experiments, few settings |

## Concepts

- **First variation F′(µ)**: the function on parameter space whose value
  at u is the first-order change in F from adding mass at u.
- **Lifting**: writing a signed measure over θ as a nonnegative measure
  over (w, θ), so that weight is one more coordinate of a particle.
- **Separation**: a support that every continuous path between two
  reference sets must cross; preserved by the flow at all finite times
  (Lemma C.10) though "generally lost in the limit".

## Connections

Independent mean-field work of the same year (Mei, Montanari and Nguyen;
Rotskoff and Vanden-Eijnden; Sirignano and Spiliopoulos) studies the
same limit for quadratic loss with quantitative SGD rates; none is
registered here. The anthology holds this work as [ANTH-LIT-298](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-298.md).
Proposition 3.1 is the measure-valued form of the KKT structure in
[LIT-1231](../literature.d/LIT-1231.md) and [LIT-1230](../literature.d/LIT-1230.md), with the first variation in the role of
negative invasion fitness.

## Bearing on the record

- **The LIT's own check** asked whether the mean-field flow's stationary
  points satisfy an invasion-type condition. They do not need to, and
  that is the paper's point. Stationarity requires F′(µ) = 0 only on the
  support. Global optimality adds F′(µ) ≥ 0 off it, which is exactly
  uninvadability with −F′(µ)(u) as the invasion fitness of a unit at u.
  The escape criterion is an invasion argument: a rare resident in a
  region where −F′ > 0 grows exponentially at rate set by η. Gradient
  flow transports mass and never creates it, so the condition can be
  enforced only if every direction is kept occupied. That is what the
  separating initialization does.
- **[CLAIM-369](../claims.d/CLAIM-369.md)** is the finite, symmetric case the LIT names, and the
  correspondence is exact. Its invasion fitness of an absent component,
  −∂_i L, is −F′(µ)(u_i) restricted to a finite dictionary, and its KKT
  points are Proposition 3.1's minimizers on a fixed support. What this
  paper adds is that, with positions free, the "absent components" form
  a continuum, and a population can reach the global optimum only if a
  seed of every possible component is present from the start.
- **[QUESTION-132](../questions.d/QUESTION-132.md)** asks when initially equivalent operators differentiate
  into specialists that each recover when rare. In this model the answer
  has a hard precondition: recovery from rarity is available only where
  some mass already sits. Units that start identical (a single point, not
  a separating set) cannot differentiate under gradient flow alone. The
  paper's experiments show the cost: initialized on {1} × Θ, the flow fails
  with 15 particles and succeeds with 30, where an initialization on
  {0} × Θ succeeds with more than 7 (D.5).
- **[QUESTION-135](../questions.d/QUESTION-135.md)**: the paper supplies no spectral condition. Its
  coexistence notion is first-order (the sign of F′), not the
  growth-rate comparison [CASE-118](../cases.d/CASE-118.md) uses.
- The one instruction for practice it carries, initialize units at
  near-zero weight spread over parameter space, belongs to the anthology,
  which holds the work as [ANTH-LIT-298](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-298.md).

## Limitations

- **Conditional and non-quantitative.** Convergence of the flow is
  assumed; no rate in m or t is given. The authors say so (§1.2, C.5).
- **Continuous-time, exact gradients, one hidden layer.**
- **ReLU** is covered only after a reparameterization (signed-square
  weights) that makes Φ differentiable; the classical ReLU flow is not
  defined (§4.2).
- **Separation needs infinitely many particles** when d ≥ 2, so the
  theorems never apply to a finite network; the finite-particle escape
  criterion (C.1) needs a particle in the right sublevel set, which
  nothing guarantees.
- **Slips.** Lemma C.2 states "‖h₂(µ)‖_BL, ‖h₂(µ)‖_BL < η" where the bound
  on ν by C0 is meant; ε in the proof of C.1 uses an undefined M; "Criteria
  to espace local minima" (twice).

## Open questions

- How many particles, as a function of the sublevel-set size of F′ at the
  bad stationary points, suffice for escape? C.5 names this as the route
  to quantitative results.
- Does a birth process (adding units where −F′ > 0) replace the
  separation assumption? That is the ecological invasion the flow lacks.
