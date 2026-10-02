---
number: 420
status: Read
formerly:
- NOTE-tmpg7iyq
paper: 'LIT-523'
title: 'Stochastic thermodynamics, fluctuation theorems and molecular machines'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read (arXiv 1205.4176 v1, 18 May 2012, 105 pp., from the arXiv PDF;
    text extracted with PyMuPDF). Extraction drops the bodies of most
    displayed equations but keeps their numbers and the prose around them.
    Where this note quotes an equation, the prose states it or it is one
    of the few the extraction kept. Read closely: §§1–4, §6, §7, §§8.1–8.2,
    §§9.1 and 9.3–9.4, §10 and §12. Skimmed: §5 (case studies), §§8.3–8.4,
    §9.2 and §11 (heat engines). The 602 references were consulted where
    the text pointed to them, not read through. The published version was
    not seen.
date: '2026-10-02'
summary: >-
  The 2012 reference review of stochastic thermodynamics. For Markovian
  dynamics coupled to baths of fixed temperature, work, heat and a
  stochastic entropy s = −ln p(x(τ),τ) are defined on single trajectories.
  Every known integral, detailed and Crooks-type fluctuation theorem
  follows from one master theorem, as the log-ratio of a path's weight
  under the original and a conjugate dynamics. Dissipation measures how
  distinguishable forward and reverse paths are. Feedback adds the mutual
  information I to the second law (Sagawa–Ueda). Machine efficiency and
  efficiency at maximum power follow from a cycle decomposition. The
  integral theorems are not proofs of the second law, because the dynamics
  build irreversibility in.
---
<!-- inactive-ok-file: THEORY-026 — Proposed; named as the account this reading bears on, not leaned on -->
<!-- inactive-ok-file: THEORY-030 — Proposed; named as the account this reading bears on, not leaned on -->
<!-- inactive-ok-file: LIT-328 — Deferred; named as the Landauer bound the review reports on, not leaned on -->

# NOTE-420: Stochastic thermodynamics, fluctuation theorems and molecular machines

## Contribution

A systematic review, with original technical parts, of the framework that
extends work, heat and entropy production to single fluctuating
trajectories. Its distinctive contributions as a review:

- the unification of all known fluctuation theorems for stochastic
  dynamics as cases of one "master" theorem (§4);
- a uniform treatment of continuous (Langevin) and discrete (master
  equation) dynamics (§§2, 6);
- a cycle-based theory of efficiency and efficiency at maximum power for
  isothermal machines (§10).

## Key insight

Thermodynamics can be done on one trajectory once the system's entropy is
also made a trajectory quantity, s(τ) = −ln p(x(τ),τ), evaluated on the
ensemble the trajectory came from (Eq. 28). Then medium entropy (heat/T)
plus system entropy is a total entropy production whose statistics obey
exact symmetries. Those symmetries come from one fact: the log-ratio of a
path's probability to its time-reversed probability is the heat dissipated
along it (Eq. 73, "a deep physical interpretation", p. 24).

## Assumptions

- **Time-scale separation.** The observed degrees of freedom are slow. The
  unobserved ones, the bath and fast internal modes, are always in
  equilibrium constrained by the slow ones. Temperature is that of the
  embedding medium and stays well defined (§§1.2, 12).
- **Markovian dynamics.** Langevin with Stratonovich discretisation, or a
  master equation on a discrete state set (§§2.1, 6.1).
- **Noise unaffected by driving.** "The strength of the noise is not
  affected by the presence of a time-dependent force" (p. 11). The
  thermodynamic reading of every theorem "essentially rests on" this
  (§3.2.1). It "could be violated in experiments" (§5.1).
- **Local detailed balance** on rates or noise, for thermodynamic
  consistency (§§9.4.5, 12).
- **Weak, state-independent coupling to the bath** for the simple
  identification of heat. Biomolecules need an intrinsic-entropy term
  (§§2.3.3, 9.2).
- **Coherences ignored** for quantum systems. Then the open quantum
  dynamics is a classical stochastic one (§1.3).

## Key results

- **Trajectory first law and entropy** (§§2.3–2.5).
  - Work increment: đw = (∂V/∂λ)dλ + f dx.
  - First law along a trajectory: w = q + ΔV (Eq. 19).
  - Medium entropy: Δs_m = q/T (Eq. 27).
  - Average total entropy production rate: Ṡ_tot = ⟨ν²⟩/D ≥ 0, with
    equality only in equilibrium (Eq. 35).
- **Classification of fluctuation theorems** (§3.1).
  - Integral: ⟨e^{−Ω}⟩ = 1, which forces negative-Ω trajectories.
  - Detailed: p(−Ω)/p(Ω) = e^{−Ω}.
  - Crooks-type: p†(−Ω) = p(Ω)e^{−Ω}, comparing two processes.
  - "Violations" of the second law are of order 1 in Ω and so
    exponentially rare in system size N (pp. 19–20).
- **The named theorems** (§§3.2–3.3).
  - Jarzynski: ⟨e^{−w/T}⟩ = e^{−ΔF/T} (Eq. 58).
  - Bochkov–Kuzovlev, which is distinct from Jarzynski for a different
    definition of work (Eq. 60).
  - Crooks: p̃(−w)/p(w) = e^{−(w−ΔF)/T} (Eq. 61).
  - Total entropy production: ⟨e^{−Δs_tot}⟩ = 1 for any initial state,
    driving and duration (Eq. 64).
  - Steady-state theorem, exact for finite times once system entropy is
    included (Eq. 65).
  - Hatano–Sasa for transitions between steady states (Eqs. 66–67).
- **Master theorem** (§4). Choose a conjugate dynamics: reversed, dual or
  dual-reversed. Then for functionals of definite parity the log-ratio
  functional R satisfies a generalised theorem (Eqs. 78–79). All of the
  above follow by choosing the conjugate, the initial distributions and
  the functional (§§4.3–4.4).
- **Master-equation version** (§6). The same results hold for discrete
  states. Work there is a formal quantity unless detailed balance gives an
  energy (§6.3.1). A footnote to §6.1 mentions approaches that derive rates
  from current constraints and points to Polettini (2011) "for a relation to
  the minimum entropy production principle". There is also a current
  fluctuation theorem from the Schnakenberg cycle decomposition (§6.4).
- **Optimal protocols** (§7.1). Minimal-work protocols jump at the start and
  end. Total entropy production for a transition in time t is bounded,
  ΔS_tot ≥ C/t.
- **Time's arrow** (§7.2), in units with T = 1:
  - ⟨w⟩ − ΔF = D[p(w−ΔF) ‖ p†(−(w−ΔF))] (Eq. 148);
  - ⟨w⟩ − ΔF ≥ D[p(x(t₁)) ‖ p†(x†(t₁))] (Eq. 149), which is an equality for
    Hamiltonian dynamics;
  - ⟨w⟩ − ΔF ≥ D[p(x(t)) ‖ p_eq(x(t))] (Eq. 150, Vaikuntanathan–Jarzynski).
- **Feedback** (§7.3).
  - Sagawa–Ueda: ⟨e^{−(w−ΔF+I)}⟩ = 1 (Eq. 154). So extracted work is at
    most −ΔF + T·I (Eq. 155).
  - A NESS analogue (Eqs. 156–157) and a stronger Hatano–Sasa-type bound,
    ⟨Δs_tot⟩ ≥ ⟨Δs_hk⟩ − I (Eq. 160).
  - The second law is restored by Landauer's erasure cost. That cost is set
    aside "first" in these analyses (p. 46).
  - An experiment found that erasure heat approaches the Landauer bound for
    long cycles (§7.3.6).
- **NESS fluctuation–dissipation theorem** (§8). The response function is
  R_A = −⟨A ∂_h ṡ⟩_s, which splits into medium and total entropy
  production terms (Eqs. 191–192).
- **Machines** (§§10–11).
  - Isothermal efficiency is at most 1.
  - In linear response, efficiency at maximum power is at most 1/2. The
    cycle representation gives Onsager symmetry automatically (§10.4).
  - For unicyclic motors, efficiency at maximum power can exceed 1/2
    beyond linear response (§10.5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | All known fluctuation theorems for stochastic dynamics follow from one master theorem with a suitable conjugate dynamics | strong for the theorems listed in §§3–4 | §4 derivations; the "all known" is the author's survey judgement |
| C2 | The integral theorem for total entropy production holds for any initial state, driving and duration | strong | Eq. 64 via Eq. 80 |
| C3 | The integral theorems are not a proof of the second law, because a Langevin or master-equation dynamics builds irreversibility in | strong (conceptual) | §3.3.1, §12 |
| C4 | Dissipated work bounds the relative entropy between forward and reverse distributions, at the work level and at any intermediate time | strong | Eqs. 148–150; reported from Kawai–Parrondo–van den Broeck and Vaikuntanathan–Jarzynski |
| C5 | With feedback, extracted work can exceed −ΔF by at most T·I, and erasure restores the second law | strong for the bound (Eqs. 154–155); the erasure balance is asserted, not modelled | §7.3; the author says a full integration of measurement and erasure is "still missing" (§12) |
| C6 | In a NESS, the response of any observable is a correlation with the h-derivative of stochastic entropy | strong | §8.2, Eqs. 191–192 |
| C7 | Efficiency at maximum power is at most 1/2 in linear response but can exceed it beyond | strong for linear response (§10.4); shown for unicyclic models beyond it (§10.5) | the result depends on the choice of variational parameters, as the author stresses |

## Concepts

- **Stochastic entropy** s(τ) = −ln p(x(τ),τ). It depends on the ensemble
  the trajectory is drawn from, not on the trajectory alone (§2.4).
- **Housekeeping and excess heat**: the heat needed to maintain a NESS,
  and the heat from changing the control parameter (§2.3.2).
- **Conjugate dynamics**: reversed, dual or dual-reversed. A device for
  deriving fluctuation theorems. The dual dynamics has the same stationary
  state and reversed currents (§4.1).
- **Efficiency at maximum power (EMP)**: efficiency at the parameter values
  that maximise output power. Its value depends on which parameters may
  vary (§10.3.2).

## Connections

The review synthesises Evans–Cohen–Morriss, Gallavotti–Cohen, Kurchan and
Lebowitz–Spohn for the steady-state theorem; Jarzynski ([LIT-517](../literature.d/LIT-517.md)) and
Crooks ([LIT-522](../literature.d/LIT-522.md)) for the work relations; Sekimoto's stochastic
energetics; Maes on the time-antisymmetric action; and the author's 2005
stochastic entropy. It names the Brussels school (van den Broeck; Mou, Luo
and Nicolis 1986) as the earlier, ensemble-level use of "stochastic
thermodynamics" for chemical systems (§1.1). The quantum thermodynamics
review [LIT-010](../literature.d/LIT-010.md) covers the quantum side this one leaves out (§1.3).

## Bearing on the record

- **[THEORY-026](../theory.d/THEORY-026.md): framework, not source.**
  - [LIT-327](../literature.d/LIT-327.md) defines dissipation as ⟨W⟩ − ΔF_neq, with F_neq = ⟨E⟩ +
    k_BT⟨ln p⟩ ([LIT-327](../literature.d/LIT-327.md), Eqs. 8–9). For one protocol started in
    equilibrium this equals ⟨W⟩ − ΔF − k_BT·D_KL(p_τ‖p_eq). Eq. 150 here
    says that is ≥ 0. So the protocol-level nonnegativity of [LIT-327](../literature.d/LIT-327.md)'s
    dissipation is a reported result of this framework.
  - That bound is for continuous Langevin dynamics, stated for the
    discrete case by analogy (§7.2). It is a protocol total, not a per-step
    quantity.
  - It does not settle what [NOTE-295](NOTE-295.md) found open and [THEORY-026](../theory.d/THEORY-026.md)'s
    promote_when asks for: the sign of the *per-step* nostalgia
    I[s_t;x_t] − I[s_t;x_{t+1}] under a non-Markov drive, with free
    energies conditioned on the current signal value only.
  - Recommendation: [THEORY-026](../theory.d/THEORY-026.md) need not cite this review as a source. It
    could name it in Connections as the framework, citing Eq. 150 as where
    protocol-level nonnegativity comes from.
- **[THEORY-030](../theory.d/THEORY-030.md) and Landauer.** §7.3 treats measurement and feedback
  first with the erasure cost set aside, then restores the second law
  through Landauer's principle. It reports an experiment in which the mean
  erasure heat saturates the Landauer bound in the limit of long cycles. The
  review does not separate logically irreversible steps from others, which
  is [THEORY-030](../theory.d/THEORY-030.md)'s distinction. It is consistent with [THEORY-030](../theory.d/THEORY-030.md) and adds
  the experiment, not an argument. The record's Landauer 1961 entry
  ([LIT-328](../literature.d/LIT-328.md)) is still unread.
- **[LIT-308](../literature.d/LIT-308.md).** Goldt and Seifert's learning bound is a subsystem
  second-law result in this framework. This review predates it and gives
  the information-flow machinery only in its feedback form (§7.3).
- **Prigogine's minimum principle.** The review does not assess it. It
  points to one paper on it (Polettini 2011) in a footnote, and its own
  steady-state results are exact symmetries of fluctuations, not extremum
  principles for the mean. That silence is itself informative: the
  framework that replaced the Brussels programme's ensemble thermodynamics
  for small systems does not use a variational selection principle for
  steady states.
- **Dissipative structures and life.** §9 treats enzymes and molecular
  motors as nonequilibrium steady states driven by chemical potential
  differences, the small-scale version of the "life as dissipation"
  picture. It makes no claim about organisms or about selection of
  structures.
- **No ML instruction.** The anthology need not hold it.

## Limitations

- **A review.** Its support for any reported result is the cited paper's.
  Its own original material is in §4 (the unifying derivation) and §§9.2
  and 10 (biopolymers, machines), as the author says (§1.4).
- **Markovian and classical** throughout. §12.2 surveys non-Markovian and
  coarse-grained cases as open: entropy production with hidden slow
  variables "is then difficult if not impossible" to identify.
- **Measurement and erasure.** Their integration into a full machine energy
  balance is "still missing" (§12).
- **Experiments are scarce** for discrete-state systems (§§6.3.2, 9.4.8).

## Open questions

The author's own (§12):

- Are there universality classes for the distributions of work, heat and
  entropy production?
- When can the additive NESS response–correlation relation be recast with
  an effective temperature?
- How should entropy production be identified under coarse-graining and
  memory?
- Is there a zeroth law for coupled nonequilibrium steady states (§12.3)?

## Corrections

- none to a seeded skim (there was no seed)
- **Title.** The arXiv title has a serial comma ("fluctuation theorems,
  and molecular machines"). The Reports on Progress in Physics title does
  not. The LIT records the published title.
- **Units in §7.2.** Eqs. 148–150 are written without T, in effect T = 1.
  Elsewhere the review keeps T explicit and sets only k_B = 1. Read with
  T, Eq. 150 is ⟨w⟩ − ΔF ≥ T·D[p‖p_eq].
