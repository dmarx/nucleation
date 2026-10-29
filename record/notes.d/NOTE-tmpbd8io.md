---
status: Read
paper: 'LIT-1236'
title: 'Blumenthal, Rocks and Mehta — Phase transition to chaos with nonreciprocal species-resource interactions'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv
    (https://arxiv.org/pdf/2308.15757, v2 of 27 February 2024, 33 pages:
    the five-page letter and 22 pages of supplementary information),
    text extracted with pdftotext. arXiv's journal reference is the PRL
    version, 132, 127401. Read: the letter in full; SI Appendix A
    (cavity calculation, §§A1–A4, and the relations A41–A43); Appendix B
    (stability transition) in full; Appendices C and D in full;
    Appendix E (finite-size scaling) in full; Appendices F and G by
    figure captions only. No number was taken from a chart. Checked: the
    instability condition (B15)–(B16) was re-derived from (B11) and (B14)
    (the two second moments diverge together when (ρχD)² = γ⁻¹φ_Nφ_R,
    D = 1 − ρσ_cσ_eγ⁻¹ν), and with A42's χ = φ_R/D it gives
    ρ*² = γ⁻¹φ_N/φ_R, the ratio of surviving species to non-depleted
    resources, eq. (6); A43's χ = φ_R − γ⁻¹φ_N was re-derived from A41
    and A42 (record arithmetic, 2026-10-29).
date: '2026-10-29'
summary: >-
  In MacArthur's consumer–resource model with species' benefits c and
  impacts e on resources correlated by ρ, the cavity method's
  replica-symmetric fixed point loses stability at ρ*² = (surviving
  species)/(non-depleted resources); below ρ* simulations do not settle,
  their largest Lyapunov exponents are positive and the probability of
  reaching a steady state falls with system size. With ρ = 1 the model has
  an optimization principle and competitive exclusion keeps the ratio
  ≤ 1, so the transition never occurs.
---
<!-- inactive-ok-file: LIT-1230 — Deferred; named only as the registration of a work this paper cites, nothing rests on its content -->

# NOTE-tmpbd8io: Blumenthal, Rocks and Mehta — Phase transition to chaos with nonreciprocal species-resource interactions

## Contribution

It takes the consumer–resource model whose symmetric form has a
minimization principle and breaks the symmetry between what a species
gains from a resource and what it does to it. A cavity calculation gives
the steady state and locates where it stops being stable, and that
boundary turns out to depend on one ratio: how many species survive per
resource left undepleted. Numerics show the other side is chaotic.

## Key insight

With e = c the effective species interaction matrix Aᵢⱼ = Σ_α cᵢα eⱼα
Θ(R_α) is symmetric and the dynamics descend an objective, so they reach
a unique fixed point. Make c and e only partly correlated and A is not
symmetric; no objective is guaranteed and fixed points can lose
stability. Where they do is set by species packing: the more species the
undepleted resources must support, the more reciprocity is needed to
hold the fixed point, ρ* = √(S*/M*).

## Assumptions

- Dynamics (1)–(2): dNᵢ/dt = Nᵢ(Σ_α cᵢα R_α − mᵢ), dR_α/dt =
  R_α(K_α − R_α) − Σᵢ Nᵢ eᵢα R_α. Self-replenishing (logistic) resources.
- Thermodynamic limit S, M → ∞ with M/S fixed; cᵢα = μ_c/M + σ_c dᵢα/√M,
  eᵢα = μ_e/M + σ_e(ρdᵢα + √(1 − ρ²) xᵢα)/√M, so corr(cᵢα, eⱼβ) =
  ρ δᵢⱼ δ_αβ; K and m with independent fluctuations. Figures use μ_c = μ_e,
  σ_c = σ_e.
- Replica-symmetric, self-averaging cavity ansatz. The paper does not
  prove it; it is checked against simulations for moderate
  non-reciprocity (Figs. A6, A8, not read).
- Simulations add immigration λ_N = λ_R = 10⁻¹⁰ to regularize and to keep
  chaos from being killed by finite-size extinctions.

## Key results

- **Phase boundary, eq. (6)/(B18).** The fixed point is unstable when
  ρ < ρ*, ρ*² = (number of surviving species)/(number of non-depleted
  resources), evaluated at the boundary. It is a co-dimension-one surface
  in parameter space, since those numbers are set by the parameters.
- **ρ = 1.** Competitive exclusion keeps the ratio ≤ 1, so the instability
  is never reached; the instability and the cavity's infeasibility
  transition coincide there.
- **Infeasibility.** For some parameters the cavity equations have no
  solution (χ → 0, where the surviving species equal the non-depleted
  resources); this lies inside the unstable phase and is not physical.
  At ρ = 0 the only cavity solution is total extinction.
- **Chaos (§Chaos, App. C).** With S = M = 512, largest Lyapunov exponents
  are positive in runs that do not settle and negative in runs that do;
  |λ₁| ≈ 5 × 10⁻³ for the Fig. 2 parameters. GALI decays exponentially in
  the dynamic phase. Kaplan–Yorke dimension 15 ± 7 against 74 ± 17
  surviving species and resources, close to the 38 ± 19 that switch
  between high and low abundance.
- **Finite size (App. E).** Fitting times-to-steady-state with a
  censored maximum-likelihood model at two parameter points, the
  estimated probability of ever reaching steady state stays ≈ 1 in the
  stable phase and falls towards 0 with size in the dynamic phase
  (fit ξ = 278.5); the time scale grows as M^0.4 and M^0.9.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The replica-symmetric fixed point of the asymmetric MCRM loses stability at ρ*² = S*/M* | strong, given the ansatz | App. B; re-derived from the cavity relations |
| C2 | Below ρ* the dynamics are chaotic | moderate | numerical: Lyapunov exponents, GALI, two trajectories; at one parameter point mostly |
| C3 | In the thermodynamic limit no system in the dynamic phase reaches steady state | moderate | finite-size MLE fits at two parameter points, S, M ≤ 1024 |
| C4 | The symmetric MCRM never reaches this transition | strong | competitive exclusion bound on S*/M* ≤ 1 with ρ* ≤ 1 |
| C5 | The divergence of c from e generalizes Tilman's two-species stability condition | weak | analogy in the discussion |

## Method

Cavity: add one species and one resource, treat the perturbation of
the rest by linear response with susceptibilities χ (resource to
carrying capacity) and ν (species to mortality), and close
self-consistent equations for survival fractions and moments (A39–A47).
Stability: perturb all survivors by independent noise and compute the
second moments of the responses; their divergence marks the boundary.
Numerically the equations are solved by black-box least squares.

## Concepts

- **Asymmetric MCRM (aMCRM)**: the model above, with impacts eᵢα
  distinct from benefits cᵢα.
- **Reciprocity ρ**: the correlation between a species' benefit from and
  impact on each resource.
- **Species-packing ratio**: surviving species over non-depleted
  resources.
- **Dynamic phase**: the side of the boundary with persistent
  fluctuations.

## Connections

It applies to a consumer–resource model the stability test Bunin used
for random Lotka–Volterra communities ([LIT-1234](../literature.d/LIT-1234.md)), and the SI identifies
its transition with that paper's multiple-attractor transition. The
symmetric model's minimization principle is MacArthur's, cited through
Marsland, Cui and Mehta's minimum environmental perturbation principle
(the record's [LIT-1230](../literature.d/LIT-1230.md)) and Chesson (1990). In the record, [CLAIM-369](../claims.d/CLAIM-369.md)
proves the symmetric, resource-mediated case to be gradient flow on a
convex objective; this paper is where that picture's assumption fails.

## Bearing on the record

- **[QUESTION-083](../questions.d/QUESTION-083.md) and the synthesis.** The LIT's reason for being here,
  that "with non-reciprocal interactions the dynamics need not minimize
  any objective", is what the paper argues, and the reading supports it
  with a sharper condition: loss of reciprocity alone does not produce
  chaos; it does so only when ρ falls below √(S*/M*). A community well
  below the competitive exclusion bound tolerates more asymmetry before
  it goes unstable. So "the limit of reading distributed agency as
  optimization" is not a point but a boundary that depends on packing.
- **[CLAIM-369](../claims.d/CLAIM-369.md).** The claim's gradient-flow form needs A = UᵀU. This paper
  gives the case A = CEᵀ with C ≠ E and shows what fails, for a related
  consumer–resource model; it is the natural objection thread to the
  claim's scope, though not to the claim, which states its symmetric
  assumption.
- **[THEORY-tmpncu1p](../theory.d/THEORY-tmpncu1p.md)** is drawn from this reading.

No instruction for machine-learning practice.

## Limitations

- The boundary rests on the replica-symmetric ansatz; beyond it the
  ansatz is invalid and the dynamic phase is characterized by
  simulation only, at a few parameter points and moderate sizes.
- Logistic, self-replenishing resources; one trophic level of consumers;
  random unstructured interactions.
- **Errors and slips.** (i) The fast-resource reduction in the letter
  writes R_α = max{0, K_α − Σᵢ Nᵢ eᵢα R_α}; setting (2) to zero gives
  R_α = max{0, K_α − Σᵢ Nᵢ eᵢα}, without the trailing R_α. (ii) The
  Jacobian (C1) has cᵢα Nᵢ in the resource–resource block where (2)
  gives eᵢα Nᵢ. (iii) App. C3 calls the Kaplan–Yorke dimension "the
  number of Lyapunov exponents that are positive" and then gives the
  correct interpolation formula (C4). (iv) In (E5) the error term's sum
  runs over Tᵢ = noSS where it should run over Tᵢ = error; (E4) writes
  argmax = −argmin of the negative log-likelihood. None affects the
  phase boundary.

## Open questions

- Does the boundary ρ* = √(S*/M*) survive structured (metabolic or
  networked) interactions, or externally supplied resources, which the
  authors report preliminary chaos for?
- Is there a replica-symmetry-broken description of the dynamic phase,
  as there is for random Lotka–Volterra models?
