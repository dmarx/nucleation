---
status: Read
paper: LIT-979
title: 'Barnett and Seth — Dynamical independence'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:2106.06511v2 (6 August 2021, the latest arXiv
    version), text extracted with pdftotext: §§1–5 and Appendices A–D,
    with the worked flow example in D.1 followed to the invariants. The
    figures were read from captions and text. The published version
    (Phys. Rev. E 108, 014304, 2023) was not compared, and may differ.
date: '2026-10-14'
summary: >-
  A coarse-graining Y = f(X) is dynamically independent when the
  microscopic history adds nothing to predicting Y beyond Y's own
  history, given the environment: transfer entropy T(X → Y | E) = 0. The
  condition is transformation-invariant and transitive. For linear
  state-space models it has a closed form, and it is minimized
  numerically over the Grassmannian. Generically no coarse-graining is
  exactly independent for VAR order above 1. The minima are many, and the
  authors treat them all as the "emergence portrait".
---
<!-- inactive-ok-file: THEORY-198 THEORY-205 CLAIM-157 CLAIM-167 — Proposed; the partial answers to QUESTION-065 and the boundary claims this reading bears on, open -->
<!-- inactive-ok-file: THEORY-tmpc7h4d — Proposed; the account filed from this reading -->

# NOTE-tmpjuj7z: Barnett and Seth — Dynamical independence

## Contribution

The paper defines when a coarse-grained variable is a dynamical system "in
its own right". It is when knowing the microscopic history does not
improve that variable's prediction of itself. It turns this into a
measure: transfer entropy from micro to macro, or Granger causality in
the linear case. The measure is invariant under reparametrization and
transitive across scales. For linear state-space systems it is given in
closed form, and minimizing it over all linear coarse-grainings yields
the most independent macroscopic variables at each scale. Before this,
related criteria (informational closure, G-emergence, causal emergence,
Markov-preserving partitions) either needed a candidate supplied in
advance or lacked one of these properties.

## Key insight

An emergent variable is a way of looking at the system that predicts
itself as well as the whole microstate predicts it. In a causal graph,
that is a sub-graph with no incoming information transfer. It may send
influence out, but receives none. Dynamical independence does not require
the variable to predict itself well. White noise can qualify.

## Assumptions

- **A given system/environment boundary.** "Here we assume that the
  system/environment boundary is given" (citing Krakauer et al. 2020 for
  that problem).
- **Supervenience as a predictive condition (2.1):**
  I(Y_t : Y_t⁻ | X_t⁻, E_t⁻) ≡ 0. Any deterministic coarse-graining
  Y_t = f(X_t) satisfies it.
- **Admissible coarse-grainings (2.8).** f must have a complement u with
  f × u an isomorphism. This holds for linear maps and discrete-state
  systems, and is needed for transitivity.
- **Stationarity.** Strong stationarity, so the time index is dropped.
- **The linear analysis (§3).**
  - X is wide-sense stationary, purely nondeterministic, stable and
    minimum-phase. It has VMA and VAR forms, and the innovations need not
    be Gaussian.
  - Coarse-grainings are linear, Y = LX with L full rank m × n, so the
    candidates are points of the Grassmannian G_m(n), not partitions of
    the units.
  - TE equals GC exactly for Gaussian innovations. Otherwise GC is used as
    a linear-prediction measure in its own right.
  - The environment is set empty "for simplicity". The conditional
    spectral case is left "for a future study".
- **The scale m is chosen.** The search is run separately at each
  m = 1, …, n − 1.

## Key results

- **Definition (2.3)–(2.6).** Y is dynamically independent of X given E
  iff T(X → Y | E) = I(Y_t : X_t⁻ | Y_t⁻, E_t⁻) ≡ 0. Since (2.1) holds,
  this equals H(Y_t | Y_t⁻, E_t⁻) − H(Y_t | X_t⁻, E_t⁻).
  - The measure is the dynamical dependence T(X → Y | E).
  - It is invariant under isomorphisms of source, target and conditioning
    space (2.7).
  - T(Y → X | E) ≡ 0 trivially, read as "the non-existence of 'downward
    causation'".
- **Transitivity (2.10, App. A).** If Y = f(X) is independent of X and
  Z = g(Y) is independent of Y, then Z is independent of X. So the
  independent variables form a partial order and can nest across scales.
- **Causal-graph form (2.11)–(2.13).**
  - After a change of coordinates making Y the first m coordinates,
    T(X → Y | E) = 0 iff G_ij(X | E) = 0 for i ≤ m < j.
  - Here G_ij = T(X_j → X_i | X_[ij], E) is the conditional causal graph.
  - So a dynamically independent variable is "a sub-graph of the causal
    graph with no incoming information transfer from the rest of the
    system". Several such variables cannot generally be put in that form
    at once.
- **Closed form for state-space models (3.16)–(3.18).**
  - With Σ = I and LLᵀ = I, F(X → Y) = log|LVLᵀ|, where V = CPCᵀ + I and
    P solves the reduced DARE (3.17).
  - The spectral form is F(X → Y) = (1/2π)∫₀^{2π} log|LS(e^{−iω})Lᵀ| dω
    (3.21).
  - There is a reduced DARE for VAR(p) (3.23)–(3.24).
- **Exact independence is generically rare (§3.3).**
  - For a state-space model, F ≡ 0 ⇔ LCA^kKMᵀ ≡ 0 for k = 0, …, r − 1
    (3.25). That is rm(n − m) quadratic equations in m(n − m) unknowns.
  - Generically there are solutions at every scale if r = 1. There are
    none if r ≥ n. For 1 < r < n there are solutions only in stated
    ranges of m.
  - For a VAR(p), F ≡ 0 ⇔ LA_kMᵀ ≡ 0 for k = 1, …, p (3.26).
    "Generically, for p = 1 we should again expect to find
    dynamically-independent macroscopic variables at all scales … while
    for p > 1 we don't expect to find any", except on a measure-zero set.
  - The spectral measure is analytic in z, so if it vanishes on any band
    it vanishes everywhere.
- **Search (§3.5).**
  - Minimizing F over the Grassmannian has no tractable analytic solution
    (App. C). The cost "appears to be in general multi-modal".
  - Local optima are "of interest in their own right, as an integral
    aspect of the emergence portrait".
  - A (1+1) evolution strategy with restarts works up to n ≈ 20, or about
    100 with a proxy-cost pre-optimization (3.28).
- **Simulation (§3.6, Figs. 1–6).**
  - A 9-variable VAR(7) was built from three fully connected modules
    with two inter-module links, and 100 runs were made per scale.
  - Exactly independent subspaces appear only at m = 2 and m = 6. They are
    the sub-graphs {1, 2} and {1, …, 6}, "only these sub-graphs have no
    incoming Granger-causal connections", and the first is nested in the
    second.
  - Other runs end in distinct local optima, some "almost orthogonal" to
    the global one.
  - The authors caution that the match to sub-graphs holds "as a direct
    consequence of its construction from a causal graph; we are, in
    effect, working in a 'privileged' coordinate system".
- **Deterministic systems (§4, App. D).**
  - Shannon measures fail for continuous deterministic dynamics. For
    flows, f is defined as independent iff f(ξ(x, t)) = η(f(x), t) for
    some flow η.
  - The general solution is f = Ψ(τ(x), u(x)), with u a set of m − 1
    invariants of the flow and τ a "time-like" function (D.10). It is
    built from conserved quantities, which links it to Noether.
  - There is no measure of near-independence for flows yet.
- **Not autonomy (§5.2).** In X₁,t = aX₁,t₋₁ + bX₂,t₋₁ + ε₁,t,
  X₂,t = ε₂,t, the white noise Y = X₂ is dynamically independent. Adding
  cε₁,t₋₁ to X₂ leaves it white but no longer independent.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Dynamical dependence is transformation-invariant and dynamical independence is transitive | strong | (2.7); proof in App. A |
| C2 | Independence is equivalent, in suitable coordinates, to a causal sub-graph with no incoming transfer | strong | (2.11)–(2.13), proof sketched by reference to App. A |
| C3 | For linear state-space models dynamical dependence has a closed form and a spectral form | strong | (3.16)–(3.21) |
| C4 | Generically, exact independence exists at all scales for VAR(1) and at none for VAR(p > 1) | strong as a counting argument | (3.25)–(3.26); equation and unknown counts, not a full proof of existence of real solutions |
| C5 | Optimization finds the planted independent variables, and the cost is multimodal | moderate | one 9-variable toy model with 100 restarts per scale |
| C6 | The criterion is intrinsic to the dynamics, unlike observer-query abstractions | moderate | argued against Millidge (2021), §5.1; the boundary and scale remain inputs |

## Method

1. Fit or specify an innovations-form state-space or VAR model of the
   microscopic data.
2. Normalize Σ = I.
3. For each scale m, minimize log|LVLᵀ|, or the spectral integral, over
   orthonormal L with a (1+1)-ES and multiple random restarts.
   Optionally pre-optimize the proxy cost Σ_k ‖LCA^kKMᵀ‖².
4. Stop at a threshold, or on failure to reject zero GC for VAR models.
5. Map the optima by principal-angle distances to each other and to the
   coordinate axes and planes.

## Concepts

- **Macroscopic variable.** Any process that does not predict itself
  beyond what the micro history and environment predict (2.1). Typically
  a coarse-graining f(X).
- **Dynamical independence / dependence.** The condition
  T(X → Y | E) ≡ 0, and the measure T(X → Y | E).
- **Emergence portrait.** The set of maximally independent variables at
  every scale, with their dependence values and their relations
  (ansatz 2.14).
- **Informational closure** (Bertschinger et al.). T(E → Y) = 0: the same
  condition, taken against the environment rather than the micro.
- **G-emergence** (Seth 2010). G-autonomy plus T(X → Y). For
  coarse-grainings it reduces to the dependence, so it "pulls in the
  opposite direction".

## Connections

The paper positions itself against Bedau's weak emergence, Bertschinger
et al.'s informational closure, Seth's G-emergence, Rosas et al.'s causal
emergence (built on PID, which lacks a canonical form and transformation
invariance), Allefeld et al.'s Markov-preserving partitions, Shalizi and
Moore's causal states, Hoel et al.'s effective information (which needs a
uniform prior over states) and Millidge's query-driven abstractions.

## Bearing on the record

- **[QUESTION-065](../questions.d/QUESTION-065.md).** [LIT-979](../literature.d/LIT-979.md) is registered there for "a coarse-graining
  fixed by the system rather than by an analyst's target", bearing on
  uniqueness. The reading confirms half of this and qualifies the rest.
  - **Confirmed: a system-supplied target.** The criterion fixes the
    target as the coarse variable's own future, so no outside query is
    chosen. The authors draw exactly this contrast with Millidge, whose
    abstractions are "driven by the agenda of the observer". So the paper
    supplies one answer to the question's first part: yes, a target can
    be supplied by the system.
  - **It is not [QUESTION-065](../questions.d/QUESTION-065.md)'s target.** The question's target is
    informativeness about the far environment across a buffer, which is
    locality. Dynamical independence is closure against the system's own
    remaining degrees of freedom, with no spatial structure and no
    buffer. The paper says nothing about locality.
  - **The analyst still fixes three things:**
    - the system/environment boundary ("assume[d] … given");
    - the scale m;
    - the class of admissible maps. In the worked theory these are linear
      subspaces, which mix units, not partitions of units.
  - **Uniqueness: no.** The cost is "in general multi-modal". The authors
    keep every local optimum as part of the portrait. Exact independence
    is generically absent for VAR order above 1. In the one example, the
    exact optimum at each scale is unique because it was planted as a
    causal sub-graph.
  - Filed as [THEORY-tmpc7h4d](../theory.d/THEORY-tmpc7h4d.md), which answers both parts of [QUESTION-065](../questions.d/QUESTION-065.md) in
    part.
- **[CLAIM-152](../claims.d/CLAIM-152.md).** The paper is a case of an individuation by sufficiency
  (a coarse variable sufficient for its own future) whose target is
  fixed by the dynamics. It does not refute [CLAIM-152](../claims.d/CLAIM-152.md), because the
  target is still fixed: self-prediction rather than some other outcome.
  It does show one target that needs no choice beyond scale and boundary.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** Near-decomposability asks for weak couplings across the
  block's edge in both directions. Dynamical independence asks only that
  none come in. A module that drives the rest of the system and receives
  nothing is exactly independent, as {1, 2} is in the toy model. A
  module that is driven by the rest never is. The two criteria pick
  different blocks whenever coupling is one-way.
- **[CLAIM-167](../claims.d/CLAIM-167.md).** On this criterion a one-way drive does not make one
  system of driver and driven at a fixed scale. The driver alone is
  emergent, and the driver-plus-driven may be a larger nested one ({1, …,
  6} contains {1, 2}). That is a definite reading of "the direction of
  coupling gives the system's internal architecture", which the paper
  states without reference to the record.
- **[THEORY-198](../theory.d/THEORY-198.md) and [THEORY-205](../theory.d/THEORY-205.md).** Those select coarse variables by
  information about a far environment. This one selects them by closure.
  On a lattice the two could be compared directly. The paper does not
  compare them.
- No instruction for machine-learning practice. The authors' intended
  application is neurophysiology. Nothing for the anthology.

## Limitations

- **Mostly linear, stationary and environment-free.** The conditional
  spectral case and nonlinear coarse-grainings are left open.
- **The optimizer is heuristic, and scale is limited.** n ≈ 20, or about
  100 with pre-optimization. The number of local optima grows with n.
- **No sampling distribution for the state-space estimator.** Inference
  is practicable only for VAR models.
- **One toy example**, which is privileged by construction.
- **The deterministic-flow theory is preliminary** ("in preparation") and
  has no measure of near-independence.
- **The authors' caveat:** whether emergent structures are "functionally
  relevant" is "an empirical question".

## Open questions

- In a local system, does a variable chosen for informativeness across a
  buffer have low dynamical dependence, and the reverse? This is the
  comparison [QUESTION-065](../questions.d/QUESTION-065.md) needs, and either answer would bear on
  [CLAIM-152](../claims.d/CLAIM-152.md).
- Does any criterion select one optimum where this one gives many? Or is
  multiplicity a property of the systems?
- How does the portrait change when the system/environment boundary is
  moved? This is the input the paper takes as given.
