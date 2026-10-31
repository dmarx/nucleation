---
status: Skimmed
paper: 'LIT-tmpm46ks'
title: 'Falasco & Esposito — macroscopic stochastic thermodynamics'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in part from the arXiv preprint 2307.12406v3 (22 May 2025,
    the RMP 97, 015002 text), 51 pp. The RMP version of record was not
    compared. Text extracted with pdftotext; displayed equations survived
    with their numbers, figures only as captions and axis labels. Read in
    full: §I (introduction), §II (stochastic thermodynamics), §III.A–F
    (the macroscopic limit, deterministic dynamics, multistability and
    metastability, deterministic thermodynamics, the drift
    decomposition, linearization and the minimum entropy production
    principle), §IV.A–D and §IV.G–H (large deviations, fluctuating
    thermodynamics, Gaussian fluctuations, the failure of the
    Kramers–Moyal truncation, relaxation against instanton, and the
    thermodynamic bounds on transition rates), §VI (emergent stochastic
    thermodynamics between attractors), §VII.A.1 (the Schlögl model),
    §VIII (discussion and outlook, including the TUR, phase transitions,
    finite size and the maximum entropy production principle) and
    appendix A. Skimmed: §IV.E–F (informational entropy production of
    Langevin equations, nonreciprocity), §IV.I (fluctuation theorems).
    Not read: §V (field theory), §VII.A.2 (Brusselator), §VII.B
    (electronic circuits), §VII.C (Potts models), appendix B. I checked
    the Schlögl quasi-potential eq. (243) against ∫ ln(r₋/r₊), the
    bistability threshold Δμ ≈ 3.85 at k₋₂ = 3.5 (Fig. 4), and the
    barrier error δ ≈ 0.19 at Δμ = 5 of the chemical Fokker–Planck
    equation; and the inequalities (119) and (160) on a linear
    nonequilibrium diffusion (with Santolin et al.'s form, NOTE-tmp3zjqz).
date: '2026-10-31'
summary: >-
  Builds macroscopic stochastic thermodynamics from Markov jump processes
  with local detailed balance. Under extensive rates and potentials, a
  deterministic dynamics emerges whose Lyapunov function is the
  quasi-potential I_ss, and a large-deviation theory of fluctuations
  around it. Transition rates between attractors go as e^{−VΔI_ss} and are
  bracketed by the entropy produced along relaxation and escape paths;
  the bracket closes only near detailed balance. Gaussian-noise Langevin
  equations mis-estimate both the barriers and the entropy production.
  Read for those parts and the Schlögl example; field theory and two of
  three applications not read.
---
<!-- inactive-ok-file: THEORY-671 LIT-1664 QUESTION-281 — Proposed, Unavailable or Open; a principle this reading bears on, an unread source and an open question -->

# NOTE-tmpf1zx4: Falasco & Esposito — macroscopic stochastic thermodynamics

## Contribution

A unified framework that takes stochastic thermodynamics (ST) of
occupation-number jump processes to a large-size limit V → ∞. The
scaling conditions (extensive Massieu potential, rates ∝ V,
nonconservative forces O(1); eqs. 26–29) yield at once a deterministic
rate equation, an extensive thermodynamics, and a large-deviation theory
of fluctuations, which the authors show to preserve the fluctuation
theorem. Equilibrium thermodynamics, linear irreversible thermodynamics,
Onsager–Machlup and macroscopic fluctuation theory are recovered as
limits (Fig. 9). Far from equilibrium the free energy is replaced by the
quasi-potential. The bounds of §IV.H and the emergent ST of §VI are the
review's own new results (§VIII.B.6).

## Key insight

Far from equilibrium the potential that orders the macroscopic dynamics
is dynamical, not thermodynamic: it is the rate function of the
stationary distribution, I_ss, computed from the rates, a Lyapunov
function of the deterministic flow (eq. 48), and equal to the Massieu
potential only at detailed balance (eqs. 36–38). Thermodynamics still
constrains it: near detailed balance I_ss = ϕ plus the nonconservative
dissipation along the relaxation path (eq. 120), and in general the
barrier ΔI_ss that sets an attractor's lifetime is bracketed by the
entropy produced in relaxing into it and escaping from it (eq. 160).

## Assumptions

- **Mesoscopic states with equilibrated interiors**: rates obey local
  detailed balance, ln[R_ρ(n)/R_{−ρ}(n + Δ_ρ)] = −Φ(n + Δ_ρ) + Φ(n) + a_ρ
  (eq. 5); every transition has its reverse (eq. 1).
- **Extensivity**: Φ/V → ϕ(c), R_ρ/V → r_ρ(c), a_ρ = O(1) (eqs. 26–28).
- **Isolated, nondegenerate fixed points** for most results; limit cycles
  only in passing, chaos excluded (§§III.C, VIII.A).
- **Thermal noise only**; quenched disorder and extrinsic noise excluded
  (§VIII.A).

## Key results (parts read)

### Deterministic level (§III)

- Rate function I(c, t) solves a Hamilton–Jacobi equation with
  H(c, π) = Σ_ρ (e^{Δ_ρ·π} − 1) r_ρ(c) (eqs. 32–33); I_ss solves
  H(c, ∂I_ss) = 0 (eq. 34). The deterministic flow F = Σ Δ_ρ r_ρ
  (eq. 46) decreases I_ss (eq. 48).
- **Keizer's paradox from the spectrum (§III.C).** Metastability is
  eigenvalues of the generator going to zero as V → ∞; the deterministic
  limit is multistable while the mesoscopic stationary law is unique,
  because "the long time limit and the macroscopic limit do not commute".
  For nondetailed-balance dynamics I_ss is only piecewise differentiable,
  built from local quasi-potentials plus attractor weights fixed by a
  jump process between attractors (eq. 55).
- **Macroscopic Shannon entropy vanishes** (eq. 57); the macroscopic
  system entropy is the internal entropy only (eq. 58).
- **Drift decomposition** F = v_ss − M·∂I_ss, with v_ss orthogonal to
  ∂I_ss (eqs. 71–76): descent in the quasi-potential plus circulation on
  its level sets. At detailed balance v_ss = 0.
- **Minimum entropy production** is recovered only near detailed balance
  with linear dynamics (eqs. 101–102), not in general.

### Fluctuations and escape (§IV)

- **Instantons** from an attractor are time-reversed trajectories of the
  dual (adjoint) dynamics (eq. 109); at detailed balance they are the
  reversed relaxations (eq. 154).
- **Emergent second law** ⟨σ̇⟩ ≥ −dₜI_ss ≥ 0 along relaxation (eq. 119);
  tight to first order in a_ρ, where I_ss = ϕ + σ_nc along the
  detailed-balanced relaxation (eqs. 120–122).
- **Transition rates** κ_ν ≍ e^{−V[I_ss(x_ν) − I_ss(x*_γ)]} (eq. 157);
  Arrhenius at detailed balance (eq. 158). Near detailed balance the
  inter-attractor jumps inherit local detailed balance (eq. 159).
- **Bounds (eq. 160).** −σ_{ν→γ} ≤ lim V⁻¹ ln κ_ν ≤ σ_{γ→ν}, the entropy
  produced along relaxation from the saddle and along the instanton. The
  lower bound is the emergent second law integrated; the upper one uses
  non-negativity of the adiabatic entropy production conditioned on
  instantons (appendix A, by Jensen). They coincide at detailed balance.
  Appendix A concedes that between fixed points these integrals diverge
  unless detailed balance holds, and the endpoints must be taken on
  balls of radius O(V^{−1/2}) around the fixed points. For the Schlögl
  model "σ_{γ→ν} and |σ_{ν→γ}| are very large, thus making the bound
  (160) very loose" (§VII.A.1).
- **The Langevin truncation fails (§IV.D–E).** Truncating the
  Kramers–Moyal expansion at second order (the chemical Fokker–Planck or
  nonlinear Langevin equation) gives dI_NLE = −F/D instead of the exact
  dI_ss = ln(Σr₋/Σr₊) in one dimension (eqs. 137–138). They agree only at
  fixed points, so escape rates are wrong by an exponential factor; and
  the Langevin entropy production vanishes at every fixed point (eq. 145),
  missing the dissipation that sustains an attractor.

### Emergent ST between attractors (§VI)

- At long times the system is a jump process on attractors (eq. 217) with
  three departures from ordinary ST (eq. 224): each attractor has its own
  steady dissipation ⟨σ̇_γ⟩ > 0 "needed to sustain the attractors"
  (eq. 225); the entropy of a transition is not the log ratio of the rates
  (local detailed balance fails away from equilibrium); and σ_{−ν} ≠ −σ_ν.

### Schlögl model (§VII.A.1)

- Exact quasi-potential in closed form (eq. 243), checked against
  ∫ ln(r₋/r₊). Bistability for k₋₂ ≥ √3 and Δμ ≥ ln 9; at k₋₂ = 3.5 from
  Δμ ≈ 3.85 (Fig. 4), checked (3.848). The Fokker–Planck barrier falls
  short by δ, which I find 0.19 at Δμ = 5 and 0.50 at Δμ = 5.3; the text's
  "δ ≃ 0.2, for V ≃ 30, would result in a transition rate around 400 times
  larger" is e⁶ ≈ 403, checked.
- In one dimension the probability velocity vanishes, relaxation and
  instanton retrace each other in configuration space, and yet the
  reactions are out of equilibrium; the bound (160) becomes an equality
  only if the thermodynamic entropy production is replaced by an
  information-theoretic one (eqs. 245–248).

### Discussion (§VIII)

- **Two maximum entropy production principles.** The review's own
  (eq. 160 read as "the attractor with the largest life-time is the one
  with the largest relaxation (or smallest instantonic) entropy
  production") holds only where the bracket is tight, near detailed
  balance. The usual one, that the attractor with the largest
  dissipation ⟨σ̇_γ⟩ lives longest, "can agree only under some peculiar
  conditions" (eqs. 290–292).
- **Lifetime is not global stability**: "a local criterion of stability,
  e.g. the life-time of an attractor, does not determine the global
  stability, e.g. the stationary probability" (§VIII.B.6, citing Maes &
  Netočný 2013). With only two attractors, as in the Schlögl model, the
  stationary weights are proportional to the lifetimes. The divergence
  needs three or more.
- **TUR (§VIII.B.1)**: for observation shorter than the escape time, the
  TUR involves only the occupied attractor's dissipation (eq. 286).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Extensive rates, potentials and O(1) forces give a deterministic limit with the quasi-potential as Lyapunov function | strong | §III, standard large deviations |
| C2 | Escape rates go as e^{−VΔI_ss} | strong | eq. 157, Freidlin–Wentzell, cited |
| C3 | Relaxation and instanton entropy productions bracket ln κ_ν / V | moderate | appendix A's Jensen argument; endpoint cutoff heuristic; loose far from equilibrium, as the authors show |
| C4 | Langevin truncations mis-estimate barriers and miss the housekeeping dissipation | strong | eqs. 137–138, 145; Schlögl checked |
| C5 | Longest-lived attractor = most dissipative only under special conditions | moderate | eqs. 290–292, argument not example |

## Concepts

- **Quasi-potential I_ss** — the stationary rate function, p_ss ≍ e^{−VI_ss}.
- **Instanton** — the most likely path out of an attractor; here the
  reverse of the dual dynamics.
- **Adiabatic (housekeeping) / nonadiabatic entropy production** — the
  parts that sustain a steady state and that drive relaxation (eqs. 18–20).
- **Emergent states** — attractors treated as the states of a coarse jump
  process, each "with internal dissipation" (Fig. 1).

## Connections

- Vellela & Qian ([LIT-tmpkp8vh](../literature.d/LIT-tmpkp8vh.md)) on the same model, cited for the two-state
  reduction and the diffusion failure.
- Santolin et al. ([LIT-tmp24302](../literature.d/LIT-tmp24302.md)) proves the escape bounds for diffusions,
  citing this review for jump processes.
- Barato & Seifert ([LIT-tmpejle0](../literature.d/LIT-tmpejle0.md)) for the TUR; Seifert's review ([LIT-523](../literature.d/LIT-523.md))
  for the ST it starts from.
- Langer 1969 ([LIT-1664](../literature.d/LIT-1664.md), unread) and Eyring–Kramers supply the prefactors
  this review leaves out.

## Bearing on the record

- **[CASE-tmpwxags](../cases.d/CASE-tmpwxags.md) and [CASE-111](../cases.d/CASE-111.md): maintained regimes as dissipative
  attractors.** The review supplies the frame in which their folds have a
  finite-size meaning. A maintained regime is an attractor with its own
  housekeeping dissipation ⟨σ̇_γ⟩ (eq. 225). Its lifetime is e^{VΔI_ss},
  set by a quasi-potential, not by any energy. A saddle-node is where the
  barrier closes (Fig. 10a–b). It also gives the condition the cases'
  production terms would have to meet to be "paid for": every production
  step reversible with local detailed balance.
- **[THEORY-671](../theory.d/THEORY-671.md) (maximum entropy production selects the steady state).**
  Both sides of the review count against the strong form: the
  dissipation-ranked principle holds only under "peculiar conditions",
  the lifetime-ranked one only near detailed balance, and lifetime need
  not fix stationary probability when there are more than two attractors.
- **The A14 analogy with SLT ([THEORY-087](../theory.d/THEORY-087.md)).** The formal parallel is exact
  as far as it goes: V here and n there are large parameters, and I_ss
  and K(w) are rate functions whose minima carry the mass. The
  disanalogy is what this review adds. I_ss is a property of a
  *dynamics* with currents (v_ss) and housekeeping dissipation, whereas a
  posterior is a static Gibbs measure, the detailed-balance case.
  Dissipative features, such as circulation on level sets, instanton
  asymmetry and ⟨σ̇_γ⟩ > 0, have no counterpart in the evidence.
- **[QUESTION-281](../questions.d/QUESTION-281.md)'s nucleation route**: the escape-rate theory here is its
  nonequilibrium general case.
- Produces [THEORY-tmpjzj2n](../theory.d/THEORY-tmpjzj2n.md) and [THEORY-tmpkze5s](../theory.d/THEORY-tmpkze5s.md); co-source of
  [THEORY-tmpwystk](../theory.d/THEORY-tmpwystk.md) and [THEORY-tmpshz26](../theory.d/THEORY-tmpshz26.md).

## Limitations

- A review: §§IV.H and VI are new, the rest systematizes known results.
- The bounds of §IV.H need an endpoint cutoff that appendix A supplies
  heuristically, and are loose in the one worked far-from-equilibrium
  example.
- Prefactors are left out (§VIII.B.3).
- My reading omits §V, §§VII.A.2–VII.C and appendix B.
