---
number: 788
status: Read
formerly:
- NOTE-tmpjexhc
paper: LIT-947
title: 'Das, Manikandan and Banerjee — Information flow with hydrodynamic interactions'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:2504.10124v2 (23 July 2025; the PDF header is
    dated 25 September 2025), text extracted with pdftotext: §§I–V and
    Appendices A–H, including the covariance and mutual-information
    expressions. The figures were read from their captions and the text,
    not from the plotted values. The earlier paper whose trend this one
    explains (arXiv:2405.00800) was not read.
- version: 2
  date: '2026-10-17'
  note: >-
    Annotated after the transfer-entropy works were read: the TE definition
    is Schreiber's at k = l = 1 only for τ = 1 (NOTE-940, TERM-057),
    and "flow" here is directed predictive improvement (CLAIM-335).
date: '2026-10-14'
summary: >-
  Two colloids are symmetrically coupled by the fluid, and the trap of one
  is moved by recorded Ornstein–Uhlenbeck noise. Mutual information, its
  time-delayed form and transfer entropy recover the order drive →
  driven particle → other particle. Under moderate drive they also show
  some backflow, which disappears under strong drive (numerics only).
  Stronger coupling lowers the information the driven particle shares with
  the drive and raises what the particles share. Without the drive, the
  coupled particles are statistically independent.
---
<!-- inactive-ok-file: CLAIM-172 CLAIM-167 — Proposed; the coupling-architecture claims this reading bears on, open -->

# NOTE-788: Das, Manikandan and Banerjee — Information flow with hydrodynamic interactions

## Contribution

The paper takes a system whose causal structure is known by construction.
A recorded external noise λ moves one optical trap, and the two trapped
particles are coupled only through the fluid. It checks that three
information measures, estimated from trajectories, recover that
structure. It also uses the measures to account for a trend the same
group reported earlier. Stronger coupling lowers the system's total
irreversibility but raises the irreversibility seen in the particles-only
subspace. After it there is a worked, experimental benchmark for reading
the direction of influence from data in a linear, Gaussian, two-body
system.

## Key insight

Coupling here is symmetric: the hydrodynamic tensor has H₁₂ = H₂₁ = ε/γ.
The direction that the information measures report is therefore not a
property of the coupling. It is the route along which the drive's
fluctuations travel: λ → x₁ → x₂. With no drive, the same coupling gives
statistically independent particles and symmetric time-delayed measures.

## Assumptions

- **Model, eqs. (4)–(5).**
  - Overdamped linear Langevin dynamics for x₁, x₂ (displacements from
    the trap centres) and λ (the trap-1 modulation, an OU process with
    ⟨λ(t)λ(t′)⟩ = (D_e/τ_e) e^{−|t−t′|/τ_e}).
  - Hydrodynamic coupling tensor H = [[1, ε], [ε, 1]]/γ, with
    ε = 3a/(2d) − (a/d)³ (Oseen-level, displacements small against d).
  - The thermal noise covariance is non-diagonal, ⟨ξᵢξⱼ⟩ = 2k_BT (H⁻¹)ᵢⱼ
    δ(t − t′). So the fluid correlates both the forces and the noises.
  - In matrix form, ẋ = −F x + ξ, with F = [[1/τ₁, ε/τ₂, −1/τ₁],
    [ε/τ₁, 1/τ₂, −ε/τ₁], [0, 0, 1/(ατ₁)]] and D = [[D₀, εD₀, 0],
    [εD₀, D₀, 0], [0, 0, θD₀]].
- **Parameters.** a = 1.5 µm, D₀ ≈ 0.16 µm²/s, τ₁ ≈ 1.5 ms,
  τ₂ ≈ 2.1 ms, τ_e = 4 ms (α ≈ 2.7). The drive strength is
  θ = (D_e/τ_e²)/D₀ = 0.14–0.56 in the experiment, with ε = 0.49 or 0.29.
- **Data.** Positions were recorded at 10 kHz for 50 s. λ is known,
  because it is the applied signal. Numerics use Euler–Maruyama at
  Δt = 10⁻⁴ s.
- **Gaussian steady state.** The covariance C solves FC + CFᵀ = 2D. Every
  bivariate marginal is Gaussian, which gives the closed forms in
  Appendices A, B and F.

## Key results

- **Steady-state mutual information (eqs. 6–7, Fig. 2, App. B).**
  - MI_{x₁x₂} = ½ log₂(c₁₁c₂₂/det C_{x₁x₂}), and likewise for (λ, x₁)
    and (λ, x₂).
  - MI_{λx₁} is lower at the stronger coupling for every θ. Without the
    second particle it is MI_{λx₁}|_{ε→0} = ½ log₂[(α+1)(α²θ+α+1) /
    (α(αθ+α+2)+1)], "evidently larger".
  - MI_{x₁x₂} and MI_{λx₂} are higher at the stronger coupling.
  - In the experiment's regime, MI_{x₁x₂} and MI_{λx₂} are too small to
    measure. They "may get overwhelmed by the noise level of the
    experiment" and are given from numerics only.
  - The authors read this as "the interactions with the other particle
    reduce the effect of the non-equilibrium drive that the first particle
    experiences". They trace the fall in total entropy production to that.
- **Time-delayed mutual information (eq. 2, Fig. 3, App. F).**
  - At θ = 0.56 and ε = 0.49, the forward measures exceed the reverse ones
    for all three pairs: MI_{λ→x₁}(τ) > MI_{x₁→λ}(τ),
    MI_{x₁→x₂}(τ) > MI_{x₂→x₁}(τ) and MI_{λ→x₂}(τ) > MI_{x₂→λ}(τ).
  - MI_{x₂→x₁}(τ) also has a peak, which the authors call "a possibility
    of information backflow". They draw the pathway as λ → x₁ ⇄ x₂.
  - Under Gaussian dynamics the peak lag is the lag of extreme two-point
    (anti)correlation: MI_{x→y}(τ) = ½ log₂[c_xx c_yy / (c_xx c_yy −
    c_xy(τ)²)]. The analytic and kNN estimates "reasonably match".
- **Transfer entropy (eq. 3, Fig. 4).**
  - TE is estimated with a Markov-state-model estimator and gives the same
    direction: TE_{λ→x₁} ≫ TE_{x₁→λ} and TE_{λ→x₂} ≫ TE_{x₂→λ}.
  - TE_{x₂→x₁} also has a peak.
  - The significance threshold for every measure is the value computed on
    shuffled trajectories.
- **Strong drive (App. D, Fig. A1, numerics only).** At θ = 5.6 the flow
  becomes one-way, TE_{x₁→x₂} ≫ TE_{x₂→x₁}: λ → x₁ → x₂.
- **Asymmetry against the parameters (Fig. 5, App. G).**
  - The asymmetry is defined as A_{x→y} = TE_{x→y}(τ^max) − TE_{y→x}(τ^max).
  - With θ fixed, a larger ε slightly lowers it in (λ, x₁) and raises it
    in (x₁, x₂) and (λ, x₂).
  - Analytic partial entropy production rates in each plane show "similar
    signatures". That is the paper's link between information flow and
    irreversibility. It is a correspondence of trends, not a derivation.
- **No drive (App. H, Fig. A6).**
  - The particles are statistically independent, P(x₁, x₂) =
    P(x₁)P(x₂), so the steady-state MI is zero, although ε = 0.49.
  - The time-delayed measures are symmetric, MI_{x₁→x₂}(τ) ≈
    MI_{x₂→x₁}(τ) and TE_{x₁→x₂}(τ) ≈ TE_{x₂→x₁}(τ). This fits
    equilibrium's symmetric correlations, ⟨x(t)y(t+τ)⟩ = ⟨y(t)x(t+τ)⟩.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With the drive recorded, TDMI and TE identify the driven particle and the order λ → x₁ → x₂ | moderate | experiment and numerics at one θ and ε for the full set of measures, Figs. 3–4; analytic TDMI, App. F |
| C2 | Under moderate drive the inter-particle flow is two-way; under strong drive it becomes one-way | weak to moderate | two-way at θ = 0.56 in experiment and numerics; one-way at θ = 5.6 in numerics only, App. D |
| C3 | Stronger coupling lowers the drive–driven MI and raises the inter-particle and drive–far-particle MI | moderate | analytic expressions, App. B; the far-particle terms only in numerics within the experimental regime |
| C4 | These information trends explain why coupling lowers total irreversibility but raises coarse-grained irreversibility | weak | parallel trends in Fig. 5 and Fig. A5; no derivation linking them |
| C5 | Coupled particles with no drive are statistically independent and show symmetric delayed measures | strong for independence, moderate for symmetry | equilibrium factorization (Meiners and Quake); Fig. A6 |

## Concepts

- **Time-delayed mutual information.** MI_{x→y}(τ) = I(x_t; y_{t+τ}),
  between finite trajectory segments. It is asymmetric in general, and
  MI_{x→y}(−τ) = MI_{y→x}(τ). It does not remove the target's own history.
- **Transfer entropy.** TE_{x→y}(τ) = I(y_{t+τ}; x_t | y_t). It removes
  the target's own history, and TE_{x→y}(−τ) ≠ TE_{y→x}(τ) in general.
  (Annotated 2026-10-17: this is Schreiber's definition with one past value
  of target and source, and only at τ = 1. For τ > 1 it conditions on y_t,
  not y_{t+τ−1}, a delayed variant Schreiber does not define
  ([NOTE-940](NOTE-940.md), [TERM-057](../terms.d/TERM-057.md)). With one target value it can credit the
  source with what the target's longer past predicts, Lizier et al.'s
  point ([THEORY-702](../theory.d/THEORY-702.md)); for an overdamped, near-Markov colloid pair that
  may matter little, which is the record's reading, not tested.)
- **Driving node.** The variable whose fluctuations the others' futures
  carry. Here it is λ by construction, and x₁ relative to x₂.
- **Non-multipartite structure.** The fluid couples the noises as well as
  the forces (D is non-diagonal), so the usual bipartite information
  thermodynamics does not apply.

## Connections

The paper follows the same group's 2024 study of irreversibility under
coarse-graining in this system (arXiv:2405.00800, not held). It uses
Schreiber's transfer entropy ([LIT-1177](../literature.d/LIT-1177.md), in the variant noted under Concepts)
and the time-delayed MI of Vastano and Swinney. "Flow" and "backflow" in
this note mean the direction of predictive improvement, not information
attributable to one particle alone ([CLAIM-335](../claims.d/CLAIM-335.md)); nothing here rests on
the stronger reading. It relies on Meiners and Quake's 1999 measurement of
hydrodynamic cross-correlations for the independence of the undriven
particles.

## Bearing on the record

- **[QUESTION-063](../questions.d/QUESTION-063.md).** [LIT-947](../literature.d/LIT-947.md) is registered there because "its information
  measures tell an external drive from coupling in two coupled colloids".
  That overstates what the paper does, in two ways.
  - **The drive is recorded and acts on one particle.** It is not a cue
    shared by the members. The measures identify which particle is
    driven given the drive's time series. Nothing in the paper concerns
    an unrecorded common drive acting on both members. That case is
    [QUESTION-063](../questions.d/QUESTION-063.md)'s.
  - **The coupling is known by construction and never tested.** The
    measures' direction tracks where the drive enters, and their symmetry
    tracks the strength of the drive, while the coupling stays symmetric
    throughout. So the paper does not show that information measures
    reveal coupling architecture. It shows a case where they misreport
    it.
  - What it does supply is a negative result: under strong one-sided
    drive, a reciprocal coupling reads as one-way flow. Filed as
    [THEORY-275](../theory.d/THEORY-275.md), which answers that part of [QUESTION-063](../questions.d/QUESTION-063.md).
- **[CLAIM-172](../claims.d/CLAIM-172.md) and [CLAIM-167](../claims.d/CLAIM-167.md).** These read the architecture from the
  direction of coupling: mutual coupling makes peers, one-way drive makes
  a hierarchy.
  - Here a mutually coupled pair is a "hierarchical interaction", in the
    paper's own words, once one member is driven. Its information flow
    runs λ → x₁ → x₂.
  - So a timing or information test of direction cannot tell an
    asymmetric coupling from a symmetric coupling with one-sided input.
    [CLAIM-172](../claims.d/CLAIM-172.md)'s criterion, "each side's timing shifts with the other's",
    needs the intervention that [QUESTION-063](../questions.d/QUESTION-063.md) asks for, not observational
    flow.
- **The undriven case.** With no drive, mutually coupled particles share
  no steady-state information, but their delayed measures are symmetric.
  A test that looks only at same-time dependence would miss this coupling
  altogether. A test of delayed dependence would see it as symmetric.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **The setting is narrow.** Two particles, linear and Gaussian, with one
  pairwise symmetric coupling. Only two values of ε and four of θ were
  measured.
- **The far-particle terms are not measured.** In the experimental regime
  MI_{x₁x₂} and MI_{λx₂} come from numerics.
- **The one-way regime is numerics only.** It needs θ ≫ 1, which is
  "beyond our experimental regime".
- **The "explanation" of the irreversibility trend is a correspondence of
  trends**, MI and TE asymmetry against partial entropy production, not
  a derivation.
- **Estimators are taken off the shelf.** scikit-learn's kNN for MI and an
  MSM estimator for TE. The surrogate threshold comes from shuffled
  trajectories, which tests against independence, not against a null of
  symmetric coupling.

## Open questions

- With λ unrecorded and acting on both particles, could the measures
  tell a common drive from coupling? This is [QUESTION-063](../questions.d/QUESTION-063.md)'s case, and the
  paper's machinery could test it directly.
- Does an intervention on x₂, such as a second, independent drive, reveal
  the symmetric coupling that observational flow hides?
- Does the bound or ratio between TE asymmetry and partial entropy
  production hold beyond this linear two-body case?
