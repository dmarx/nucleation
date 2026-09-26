---
number: 61
status: Read
formerly:
- NOTE-tmpjab5t
paper: LIT-057
title: 'Saeedian et al. 2021, delay in generalized Lotka–Volterra'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv:2110.11914v1 (22 Oct 2021, dated 25 Oct
    2021), 18 pp.: main text, Figs. 1–6, Appendices A–C and references
    (raw4/2110.11914.txt, extracted with PyMuPDF). v1 is the only arXiv
    version. I did not read the published version (Phil. Trans. R. Soc. A
    380: 20210245, 2022). The Royal Society PDF returned HTTP 403, and
    Europe PMC and Unpaywall list only the arXiv copy as free. I read its
    abstract via Crossref and compared it with v1 (see corrections). Figures
    came through only as axis labels, so I relied on captions and prose.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  The paper studies random delayed generalized Lotka–Volterra dynamics,
  ẋ_i = x_i(r_i + Σ_j b_ij x_j(t−τ)), with instantaneous interactions
  switched off (A = 0) in every delay result. A feasible, stable
  equilibrium loses stability by a Hopf bifurcation at τ_c = min over
  eig(J) of (1/|j|) arctan(Re j/Im j) (Eq. 14), where J = diag(−B⁻¹r)B,
  and this matches simulation (Fig. 5b; S = 100 is stable at τ = 12 and
  oscillates at τ = 18). In the oscillatory regime, at τ = 20 and 22 for S
  ≲ 70, community-level CV falls with S while mean species-level CV rises
  (Fig. 6). The paper reads this as a positive diversity–stability
  relation but tests it against no averaging null.
---

<!-- inactive-ok-file: LIT-057 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-061: Saeedian et al. 2021, delay in generalized Lotka–Volterra

## Contribution

The paper extends random-matrix feasibility and stability analysis of large generalized Lotka–Volterra (GLV) communities to include a discrete delay. It makes three contributions:
1. A closed-form feasibility probability for diagonally dominant random interaction matrices, P_feas = {½ erfc[−d_A/√(2C(S−1)) σ_A]}^S (Eq. 9, Appendix B). At leading order in S this is ≈ 2^−S, and at first order the leading Jacobian eigenvalues are λ_i ≈ −d_A x*_i (Eq. 11). Feasibility and stability are thereby linked through the rarest species' abundance.
2. The observation that, in a pure-delay random GLV with S up to 200, the equilibrium loses stability by a Hopf bifurcation at an analytically computed τ_c. Past τ_c the dynamics oscillate; for larger delays the numerical integration diverges.
3. The observation that, in the delay-induced oscillatory regime, community-level variability falls with diversity while species-level variability rises.

## Key insight

Delay turns every stable real community eigenvalue j into a characteristic equation λ = j e^{−λτ}. A large enough delay pushes the leading pair across the imaginary axis even though the undelayed community is stable. That creates sustained fluctuations with no external forcing, and variability-based stability measures (CV) can then be computed where local asymptotic stability says only "unstable". On the CV measure the diversity–stability sign flips relative to May.

## Assumptions

- **Model.** Delayed GLV (Eq. 1), with every delay result in the pure-delay form A = 0 (Eq. 12).
- **Random ingredients.** Off-diagonal b_ij are drawn i.i.d. Normal(0, σ_B) with probability C (connectance), else 0. The diagonal is fixed at b_ii = −d_B. Growth rates are r_i ~ U[0.05, 0.1] and initial conditions x_i(0) ~ U[0.01, 0.05] (Fig. 5 caption).
- **Figure parameters.** Figs. 2–6 use d_B = 10, σ_B = 0.1, C = 1, with S = 100 in Figs. 2–4, S = 10–200 in Fig. 5, and S ≲ 70 in Fig. 6.
- **Diagonal dominance, d ≫ σ** (strong intraspecific self-regulation). This is required for Eqs. 7–11 and "in the subsequent sections we stick to this condition" (p. 4). Fig. 1a nevertheless tests Eq. 9 at d_A = σ_A = 1 (C = 0.1), outside the stated regime.
- **Initial state.** Simulations start in the coexistence region: B Lyapunov-diagonally stable and r > 0, so the undelayed equilibrium x* = −B⁻¹r is feasible and globally stable (Appendix A, Theorem 4).
- **Numerics.** Euler integration of the delay equations. Stationarity is taken from T = 0.1 t_f, with t_f = 3000 (Fig. 5) or 10000 (Fig. 6).
- **Linearisation.** The community matrices are taken to commute (Eq. 3).

## Key results

- **Feasibility (Eq. 9, derived in Eqs. B2–B18).** P_feas(d_A, σ_A, S, C) = {½ erfc[−d_A/√(2C(S−1)) σ_A]}^S, which decays as ≈ 2^−S at leading order. Fig. 1a compares it with 1000 realizations per S for S = 5–50. An exact binomial-mixture form is given in Eq. B14.
- **Feasibility–stability link (Eq. 11, Fig. 1b).** λ_i ≈ −d_A x*_i[1 − (1/d_A)Σ_{j≠i} A_ij A_ji x*_j/(x*_j − x*_i)]. At first order, max Re λ is linear in min x*_i. Fig. 1b (d_A = 10) shows this holds for σ_A = 0.1 and 1 and fails for σ_A = 10 and 100.
- **Critical delay (Eq. 14, derived in Eqs. C2–C4).** At criticality ν² = α² + β², with α, β the real and imaginary parts of the community eigenvalue, and τ_c(α, β) = (1/|ν|) arctan(α/β); τ_c is the minimum over the spectrum. The branch of arctan is not stated. For a nearly real negative eigenvalue (β → 0) the formula must be read on the branch that gives the classical π/(2|α|).
- **Phases (Figs. 2–4, S = 100).** Stable at τ = 12, oscillating at τ = 18, numerically divergent at τ = 28. Fig. 5b gives τ_c (analytic and simulated) and the divergence threshold τ_c^C, both decreasing monotonically in S. Fig. 5a shows ecological persistence (no divergence, no extinction) falling with τ for S = 10, 50, 100, 200.
- **Variability (Eq. 15, Fig. 6).** CV_s is the species-averaged coefficient of variation; CV_c is the CV of the total N(t) = Σx_i. At τ = 20 and 22 with t_f = 10⁴, CV_c decreases and CV_s increases with S over roughly S = 10–70. In the equilibrium phase CV_s = CV_c = 0 by construction.
- **Stability hierarchy (Appendix A).** DiS ⊂ TS ⊂ DS ⊂ LS ⊂ S (Lyapunov-diagonal, total, D-, linear stability), with the −P and −P⁰ matrix classes as necessary conditions. This is a review of known results (Takeuchi, Logofet), not new.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For diagonally dominant random A, P_feas ≈ {½erfc[−d_A/(√(2C(S−1))σ_A)]}^S | moderate | derivation (App. B, CLT approximation of Eq. B14); numerics in Fig. 1a at a parameter point (d_A = σ_A) outside the stated d_A ≫ σ_A regime |
| C2 | When d_A ≫ σ_A, stability (max Re λ) is linearly tied to the rarest species' abundance | moderate | first-order perturbation, Eq. 11 / B22; Fig. 1b, 100 realizations per point |
| C3 | Increasing delay produces a Hopf bifurcation at τ_c given by Eq. 14, "in excellent agreement" with simulation | moderate | linear delay analysis (App. C); simulations in Figs. 2–3 and 5b at one (C, σ_B, d_B) setting |
| C4 | τ_c decreases with diversity S, "consistently with May results" | moderate (numerical) | Fig. 5b, single parameter set. My inference, not the paper's: in this regime the community eigenvalues are ≈ −d_B x*_i ≈ −r_i, so τ_c ≈ π/(2 max r_i) ≈ 16 for r ≤ 0.1. That is consistent with Figs. 2–3 bracketing τ_c between 12 and 18, and would make the S-dependence largely an extreme-value effect of the growth-rate distribution rather than of interaction complexity (unverified) |
| C5 | Past a larger delay τ_c^C the trajectories diverge, and this is a numerical artefact | weak | assertion; not fixed by refining the Euler step; the Conclusion's "analytical insights" on boundedness are not presented |
| C6 | In the delay-induced oscillatory regime, stability (1/CV_c) increases with diversity, consistent with experiments | weak | two delays, S ≲ 70, number of realizations and error bars not stated (Fig. 6); no comparison with the averaging null of independent fluctuations |
| C7 | "Delay is detrimental for local GLV stability" | moderate | resilience (\|leading eigenvalue\|) decreases with τ below τ_c (p. 5), and instability sets in at τ_c |

## Method

Two parts:
- **Analytic.** Perturbative inversion of A = −d_A I + M as a Neumann series (Eq. 7). Normal approximation of the row sums for feasibility (App. B). Second-order eigenvalue perturbation for the Jacobian (Eq. B22). The linear delay characteristic equation, solved via the Lambert W function (Eq. 4) and at the Hopf point (Eqs. C3–C4).
- **Numerical.** Euler integration of Eq. 12 with random B and r, detecting phases from trajectories. Time-series CVs are computed after discarding the first 10 % of each run.

## Concepts

- **Feasible.** Every equilibrium abundance is positive, x*_i > 0.
- **Coexistence region.** r > 0 and B ∈ DiS (Lyapunov-diagonally stable), guaranteeing a feasible, globally stable undelayed equilibrium.
- **Phase I / Phase II / computational divergence.** Asymptotically stable / oscillatory ("non-point attractor") / numerically diverging trajectories (Fig. 5b).
- **Ecological persistence.** The probability of neither divergence nor extinction over t_f (Fig. 5a).
- **CV_s, CV_c.** Mean species-level and community-level coefficients of variation over the stationary window (Eq. 15). The paper takes 1/CV_c as "stability".

## Connections

The paper builds on May (1972) and random-matrix stability (Allesina & Tang 2012; Grilli et al. 2016), on feasibility work (Grilli et al. 2017; Servan et al. 2018), and on the delayed predator–prey literature (May 1973; the Hopf bifurcation studies of refs 25–34), extending it from two or three species to large random communities. The variability view follows McCann (2000) and Pimm (1984), and the empirical diversity–stability observations follow Tilman's grassland work and microcosm experiments. It appeared in the same Phil. Trans. A theme issue as c34. Within this batch, c33 is the other paper where oscillations arise from the structure of the interaction matrix, in its case non-reciprocal cyclic coupling rather than delay.

## Bearing on the record

This is theoretical ecology with no instruction for ML practice, so there is nothing for the Anthology of the SOTA. The dossier notes that random-matrix stability with delays is relevant to delayed feedback among coupled learners, such as stale gradients in asynchronous training. That kinship is real at the level of λ = j e^{−λτ}, but the paper makes no such link. It adds nothing an ML reader would not get more directly from the stale-gradient literature (not in this record). For this record, its useful content is a worked instance of how the answer to "does diversity stabilise?" depends on which stability measure is chosen (local asymptotic versus temporal variability).

## Limitations

- Every delay result is for A = 0 and one parameter setting (C = 1, σ_B = 0.1, d_B = 10). In that strongly self-regulated regime the community is close to S decoupled logistic delay equations, which may explain why τ_c is tied so closely to the growth-rate spectrum (see C4).
- The diversity–stability claim does not rule out simple statistical averaging. Summing S weakly correlated oscillating populations lowers CV_c roughly as 1/√S for purely statistical reasons. The paper cites Tilman et al. 1998 ("statistical inevitability or ecological consequence?") as ref. 40 but never tests against that null. Only two delay values and S ≲ 70 are shown, with no stated number of realizations. The Fig. 6 caption also calls rising CV_s "in agreement with May's result [38]", but ref. 38 is May et al. 1974 on single-species time delays, not the complexity–stability result.
- Boundedness of the solutions is neither proved nor demonstrated, and the Conclusion refers to analytical insights that are not in the paper.
- The arctan branch in Eq. 14/C4 is left unspecified.
- The published version was not read and may have revised the analysis; the changed abstract suggests at least a reframing.

## Open questions

- Does CV_c(S) fall faster than the averaging null, e.g. against surrogates built from phase-randomised species trajectories? That would say whether the "positive diversity–stability" result is ecological or statistical.
- How does τ_c depend on S when σ_B√(CS) is comparable to d_B (weak self-regulation), where interactions rather than the r_i spectrum set the leading eigenvalue?
- Is the "computationally divergent" phase a genuine blow-up of Eq. 12 or an Euler artefact? A stiff delay-DDE solver (e.g. method of steps with adaptive RK) would settle it.
- What changes with both A and B nonzero and non-commuting?

## Corrections to the seeded skim

- **The delay results use delayed interactions only.** The dossier says the paper studies "instantaneous and delayed random interactions". The framework (Eq. 1) has both, but every delay result sets A = 0 "in order to study the pure effect of the delayed interaction" (Eq. 12 and all captions of Figs. 2–5). The no-delay feasibility/stability section (Eqs. 5–11) uses A with B = 0. No result combines the two.
- **Appendix C does not show the trajectories stay bounded.** The dossier says "the authors say analysis suggests the true trajectories stay bounded". The Conclusion does say "we have some analytical insights suggesting that the true analytical trajectories should be bounded" (p. 8–9). No such analysis appears anywhere in the paper; Appendix C derives only τ_c. The Introduction concedes: "we do not prove the existence of bounded solutions" (p. 2). The divergence persisted when the Euler step was refined, and the authors "were not able to fix" it (p. 6).
- **The published abstract drops the stability wording.** Preprint v1: "in the oscillatory regime induced by the delay stability increases for increasing ecosystem diversity". Published abstract (Crossref): "the variability at community level decreases for increasing diversity". The published wording is the one the evidence supports. The dossier quotes the stronger v1 framing ("a positive diversity–stability relationship... in agreement with experimental observations").
- The dossier's Eq. 16 is the preprint's Eq. 15 (the CV definitions); Eq. 16 defines the averages. Minor.
- The critical-delay derivation assumes the instantaneous and delayed community matrices commute, [Ã, B̃] = 0 (Eq. 3). With A = 0 this is trivially met; the dossier does not mention the condition.
