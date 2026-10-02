---
number: 417
status: Read
formerly:
- NOTE-tmpcuba0
paper: 'LIT-517'
title: 'Nonequilibrium Equality for Free Energy Differences'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv cond-mat/9610209 v1, 30 Oct 1996, 11 pp., from the
    arXiv PDF; text extracted with PyMuPDF). Every page and all 12
    references were read. I checked Eqs. 7–8 (the Liouville step) and the
    cumulant reduction to Eq. 12 against the definitions, and compared the
    weak-coupling step with how Seifert's review (LIT-523, §3.2.1)
    and Crooks (LIT-522) state the relation's conditions. The PRL
    version of record was not seen.
date: '2026-10-02'
summary: >-
  The nonequilibrium work relation. Switch a classical system that starts
  in canonical equilibrium from H_0 to H_1 at any finite rate. Then
  ⟨e^{−βW}⟩ = e^{−βΔF} exactly, whatever the path or the switching time
  (Eq. 2). It is proved for an isolated Hamiltonian system by Liouville's
  theorem, for a reservoir under weak coupling, and for a Nosé–Hoover
  thermostat with no extra assumption. Thermodynamic integration and the
  Zwanzig formula are its limits, ⟨W⟩ ≥ ΔF follows by Jensen, and Gaussian
  work gives W_diss = βσ²/2. Its practical reach is work fluctuations of
  order k_BT.
---
<!-- inactive-ok-file: THEORY-026 — Proposed; named as the account this reading bears on, not leaned on -->

# NOTE-417: Nonequilibrium Equality for Free Energy Differences

## Contribution

Before this paper, a free-energy difference ΔF could be bounded by
irreversible work, W ≥ ΔF on average, but only obtained exactly from
equilibrium (quasi-static) averages. The paper gives an equality instead:
the exponential average of finite-time work equals e^{−βΔF} for any
switching rate. Two standard equilibrium identities, thermodynamic
integration and the free-energy perturbation formula, become its slow and
fast limits.

## Key insight

The exponential average of work does not depend on how fast you drive. For
an isolated system, e^{−βw} exactly cancels the change in phase-space
density along each trajectory (Eq. 7), so averaging e^{−βW} over the final
distribution gives the ratio of partition functions Z_1/Z_0. Dissipation is
real for every single run, since W fluctuates and its mean exceeds ΔF, but
the rare runs with W < ΔF weigh exactly enough to restore the equilibrium
answer.

## Assumptions

- **Classical** dynamics. Quantum effects are set aside (p. 7).
- **Canonical initial state** at temperature T, with the parameter fixed at
  A (λ = 0). Every repetition re-equilibrates first.
- **Fixed protocol.** The same path γ and switching time t_s for every
  repetition (p. 2). The protocol is known and not random.
- **Work** is W = ∫ λ̇ ∂H_λ/∂λ dt along the trajectory (Eq. 3).
- **Physical reservoir: weak coupling.** System and reservoir together form
  an isolated Hamiltonian system. The interaction h_int must be small enough
  that Y_1/Y_0 reduces to Z_1/Z_0 (p. 6). The author states this
  explicitly as the one assumption beyond Hamilton's equations.
- **The slow-limit identification.** Going from Eq. 9 to Eq. 10 uses the
  claim that W = ΔF "for every member of the ensemble" when t_s → ∞
  (p. 6), a result of quasi-static statistical mechanics.
- **Nosé–Hoover case.** The initial density is the extended canonical
  distribution (Eq. 15). Under it the result is "identically true", with
  no weak-coupling or chaoticity assumption (p. 9).

## Key results

- **Eq. 2, the equality.** ⟨e^{−βW}⟩ = e^{−βΔF}, equivalently ΔF =
  −β^{−1} ln⟨e^{−βW}⟩. It is independent of γ and t_s.
- **Eqs. 6–8, isolated system.** With w(z,t) = H_λ(z) − H_0(z_0) and
  Liouville's f(z,t) = f(z_0,0), f(z,t) e^{−βw(z,t)} = Z_0^{−1} e^{−βH_λ(z)}
  (Eq. 7). Integrating over z at t_s gives Z_1/Z_0 (Eq. 8). I checked this
  step and it is exact.
- **Eqs. 9–10, with reservoir.** For system plus reservoir, ⟨e^{−βW}⟩ =
  Y_1/Y_0, where Y is the full partition function (Eq. 9). This is
  independent of t_s and the path. Equating it with e^{−βΔF} needs weak
  coupling.
- **Limits.** As t_s → ∞, the equality gives thermodynamic integration, ΔF
  = ∫ ⟨∂H/∂λ⟩_λ dλ (Eq. 4). As t_s → 0 it gives Zwanzig's ΔF = −β^{−1} ln
  ⟨e^{−βΔH}⟩_0 (Eq. 5). The hard-wall exception is noted in reference 2.
- **Second law as corollary.** ⟨W⟩ ≥ ΔF follows from ⟨e^x⟩ ≥ e^{⟨x⟩}
  (p. 6), "rather than by invoking the increase of entropy".
- **Eqs. 11–12.** ΔF is a cumulant series in the work distribution. If W
  is Gaussian, ΔF = ⟨W⟩ − βσ²/2, so W_diss = βσ²/2, a
  fluctuation–dissipation relation (credited to Hermans).
- **Eqs. 13–17, thermostats.** The equality holds exactly for Nosé–Hoover
  dynamics from the extended canonical ensemble. The author says it
  "may similarly be established" for Metropolis Monte Carlo (p. 9), citing
  Hunter et al. That case is asserted, not shown.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | ⟨e^{−βW}⟩ = e^{−βΔF} for any path and switching rate | strong for an isolated system and for Nosé–Hoover; strong under weak coupling for a physical reservoir | Eqs. 6–10, 15–17; the weak-coupling condition is stated (p. 6) |
| C2 | Thermodynamic integration and free-energy perturbation are its limits | strong | Eqs. 4–5; reference 2 notes the hard-wall exception |
| C3 | ⟨W⟩ ≥ ΔF follows from the equality, without invoking entropy increase | strong | Jensen's inequality (p. 6) |
| C4 | For Gaussian work, W_diss = βσ²/2 | strong given Gaussianity, which is assumed, not derived | Eqs. 11–12 |
| C5 | The equality holds for Metropolis Monte Carlo thermostats | asserted | p. 9, "may similarly be established", reference 11 |
| C6 | Its use is limited to systems with work fluctuations σ not much larger than k_BT | informal argument | p. 7: rare low-W runs dominate the average |

## Concepts

- **Switching process.** λ goes from 0 to 1 over a time t_s at constant
  rate, starting from equilibrium at λ = 0 (p. 3).
- **Dissipated work.** W_diss = W − ΔF, "associated with the increase of
  entropy during an irreversible process" (p. 2). Here ΔF is the
  *equilibrium* free energy difference between the end configurations,
  whether or not the system has relaxed at the end.
- **Work accumulated function** w(z,t): the work done on the unique
  trajectory through z at time t (p. 4).

## Connections

The paper sits on Kirkwood's thermodynamic integration and Zwanzig's
perturbation formula, which it recovers, and on Hermans's
fluctuation–dissipation observation for Gaussian work. It does not cite the
entropy-production fluctuation theorems of Evans, Searles, Gallavotti and
Cohen, which were then a separate line. Crooks ([LIT-522](../literature.d/LIT-522.md)) joined the
two in 1999, deriving this equality from a fluctuation theorem. The
quantum thermodynamics review [LIT-010](../literature.d/LIT-010.md) re-derives the classical equality by
the same Liouville argument and gives its quantum two-point-measurement
form.

## Bearing on the record

- **[THEORY-026](../theory.d/THEORY-026.md): background, not support.** The account rests on Still et
  al. ([LIT-327](../literature.d/LIT-327.md)), who cite this paper only as an example of relations that
  assume a known protocol (their p. 1, reference 3). Their identity, Eq. 14
  of [LIT-327](../literature.d/LIT-327.md), is an ensemble average for a discrete Markov chain and uses
  no work fluctuation relation. Nothing in [THEORY-026](../theory.d/THEORY-026.md) depends on the
  equality, so this paper is not a source for it.
- **Two meanings of "dissipated work".** Here W_diss = W − ΔF, with ΔF
  between *equilibrium* states. [LIT-327](../literature.d/LIT-327.md)'s ⟨W_diss⟩ is ⟨W_ex⟩ − F^add: the
  same quantity minus the free energy still stored in the final
  nonequilibrium distribution, k_BT·D_KL(p‖p_eq) ([NOTE-295](NOTE-295.md)). The two agree
  only when the system ends in equilibrium. A reader moving between
  [THEORY-026](../theory.d/THEORY-026.md) and this paper should not equate them.
- **No ML instruction.** The equality is the identity behind annealed
  importance sampling, but the paper makes no such link and carries no
  instruction for machine-learning practice. The computational instruction
  it does carry is for molecular simulation: average e^{−βW} rather than W
  (p. 9). That is not an anthology topic.
- **Dissipative structures.** None. The paper concerns transitions between
  equilibrium states, not steady states held from equilibrium.

## Limitations

- **Weak coupling** for a physical reservoir, as the author states. Seifert's
  review ([LIT-523](../literature.d/LIT-523.md), §3.2.1) notes that the Hamiltonian derivation
  "requires some care in identifying the proper role of the heat bath".
- **Classical only.** No quantum statement is made.
- **Sampling.** The average is dominated by rare runs with W far below ⟨W⟩.
  This "pretty much rules out macroscopic systems" (p. 7).
- **Metropolis** is asserted, not derived.
- **No distribution result.** The paper constrains one exponential moment of
  p(W), not the distribution. The relation between forward and reverse work
  distributions is Crooks's later result.

## Open questions

- What does the equality become under strong coupling, where ΔF of the
  system alone is not well defined? The paper flags the issue, not the
  answer.
- How many runs are needed for a given accuracy when σ ≫ k_BT? The paper
  gives the qualitative caveat only.

## Corrections

- none to a seeded skim (there was no seed)
- **Title.** The preprint is titled "A nonequilibrium equality for free
  energy differences". The PRL title drops the article. The LIT records the
  PRL title.
- **Date line.** The arXiv-rendered PDF carries "(November 26, 2024)" under
  the author line. That is the LaTeX \today of the rendering, not a date of
  the work. The submission date is 30 October 1996.
