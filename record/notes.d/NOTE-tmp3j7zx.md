---
status: Read
paper: 'LIT-tmpc4996'
title: 'Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv cond-mat/9901352 v4, 29 Jul 1999, 7 pp., from the
    arXiv PDF; text extracted with PyMuPDF). I read §§I–V, the five figure
    captions and the 34 references. I checked Eq. 7 against Eqs. 5–6, the
    change of variables that gives Eq. 2, Eq. 4, and Eq. 10 from Eqs. 6 and
    9 with the first law. The figures' numerical data could not be checked
    from the text. The PRE version of record was not seen.
date: '2026-10-02'
summary: >-
  A finite-time fluctuation theorem for stochastic dynamics. If the
  dynamics are Markovian and microscopically reversible (path over
  reversed path = e^{−βQ}) and the entropy production ω = ln ρ(x_{−τ}) −
  ln ρ(x_{+τ}) − βQ is odd under time reversal, then P_F(+ω)/P_R(−ω) =
  e^{ω}. For processes that start and end in equilibrium ω = β(W − ΔF), so
  the Jarzynski equality is one line. For time-symmetric steady states,
  P(+ω)/P(−ω) = e^{ω} for any whole number of cycles. At long times it
  gives a heat fluctuation theorem and Gaussians with variance twice the
  mean.
---
<!-- inactive-ok-file: THEORY-026 — Proposed; named as the account this reading bears on, not leaned on -->

# NOTE-tmp3j7zx: Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences

## Contribution

The paper proves a fluctuation theorem for entropy production that is exact
at finite times and compares a process with its time reverse, for
stochastic microscopically reversible dynamics. It then shows that
Jarzynski's nonequilibrium work relation ([LIT-tmp47vbz](../literature.d/LIT-tmp47vbz.md)) is a special case:
for systems that start and end in equilibrium the entropy production is
β(W − ΔF). Earlier fluctuation theorems compared +σ with −σ in one steady
process and held asymptotically. This one compares a driven process with
its reversed protocol and holds for any duration.

## Key insight

Dissipation is the log-ratio of a path's probability to the probability of
its time reverse. Microscopic reversibility says that ratio, for given
endpoints, is e^{−βQ}. Adding the change in −ln ρ at the endpoints makes it
e^{ω} for the whole path (Eq. 7). Summing over paths with a fixed ω then
gives the theorem directly, and integrating e^{−ω} against P_F gives
⟨e^{−ω}⟩ = 1 (Eq. 4), of which the work relation and ⟨ω⟩ ≥ 0 are
corollaries.

## Assumptions

Stated together in §V, and that summary is accurate:

- **System and baths.** A finite classical system coupled to baths, each
  with a constant intensive parameter (β, βp, …). Entropy is in nats, with
  k_B = 1.
- **Dynamics.** Stochastic and Markovian (p. 2).
- **Microscopic reversibility** (Eq. 5): P[x(+t)|λ(+t)] / P[x(−t)|λ(−t)] =
  e^{−βQ[x(t),λ(t)]}, with Q the heat into the system, odd under reversal.
  This is distinct from detailed balance (pp. 2–3). Dynamics that are
  detailed-balanced at each time step satisfy it even when driven.
- **ω odd under reversal.** Equivalently, ρ_F(x_{+τ}) = ρ_R(x_{+τ}) and
  ρ_R(x_{−τ}) = ρ_F(x_{−τ}). This holds in two classes (§III):
  - processes that start in equilibrium, are driven for a finite time, and
    relax to equilibrium again;
  - time-symmetric periodic driving into a time-reversal-invariant steady
    state. For the steady-state class the dynamics must also be "entirely
    diffusive", with no momenta (p. 4), except where the steady state is
    reflection-invariant, as for the sheared fluid.

## Key results

- **Entropy production along a path** (Eq. 6): ω = ln ρ(x_{−τ}) − ln
  ρ(x_{+τ}) − βQ. This is the change in the information needed to describe
  the microstate plus the bath's entropy change.
- **Eq. 2, the theorem.** P_F(+ω)/P_R(−ω) = e^{+ω}, exact for finite times.
  The derivation from Eq. 7 is three lines, and I checked it.
- **Eq. 4.** ⟨e^{−ω}⟩_F = 1. By convexity, ⟨ω⟩ ≥ 0 (§IV).
- **Equilibrium endpoints** (Eqs. 9–10). Substituting Boltzmann
  distributions, ω_F = β(W − ΔF). That gives the work fluctuation theorem
  (Eq. 11) and, through Eq. 4, the Jarzynski relation (Eq. 3).
- **Steady states** (Eq. 12). For a time-symmetric NESS, P(+ω)/P(−ω) =
  e^{+ω} for any whole number of cycles, or any finite time under constant
  perturbation.
- **Long times** (§IV).
  - Heat fluctuation theorem: lim P(+βQ)/P(−βQ) = e^{βQ} (Eq. 13). Fig. 4
    shows it is "wholly inaccurate" for Δt ≤ 256 steps and accurate beyond
    the relaxation time except at large |βQ|.
  - If ω is Gaussian, the theorem forces variance = 2 × mean, a
    fluctuation–dissipation relation, and through it the Green–Kubo
    relations, "without the standard assumption that the system is close to
    equilibrium".
- **Model.** A one-particle Metropolis walk on a moving periodic energy
  surface, solvable exactly from its master equation (Figs. 1–5),
  illustrates all of the above.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | P_F(+ω)/P_R(−ω) = e^{ω} at any finite time, under the stated conditions | strong | §II derivation from Eqs. 5–7; checked |
| C2 | For equilibrium endpoints ω = β(W − ΔF), so the Jarzynski relation follows | strong | Eqs. 9–11 with ΔE = W + Q; checked |
| C3 | A time-symmetric NESS satisfies P(+ω)/P(−ω) = e^{ω} for whole cycles | strong for the stated class | §III; needs the steady state itself to be reversal-invariant |
| C4 | At long times, the heat fluctuation theorem holds | moderate | an approximation (ω ≈ −βQ), shown numerically in Fig. 4 for one model |
| C5 | Gaussian entropy production implies the fluctuation–dissipation and Green–Kubo relations far from equilibrium | moderate | needs Gaussianity (central limit argument) and time-symmetric driving; Figs. 2 and 5 for one model |
| C6 | Microscopic reversibility (Eq. 5) holds for Langevin and Metropolis dynamics, and for driven dynamics that are detailed-balanced at each step | moderate | asserted with a pointer to Crooks 1998 (reference 19, Eq. 9) |

## Concepts

- **Microscopically reversible** (Eq. 5): the probability of a path over
  that of its reverse equals e^{−βQ}. Crooks separates this from detailed
  balance, which is about state-to-state transition probabilities.
- **Entropy production ω** (Eq. 6): a functional of one path, defined
  relative to the ensemble's initial and final distributions.
- **Forward and reverse processes**: the same system driven by λ(t) and by
  λ(−t), each starting from the other's final distribution.

## Connections

The paper unifies two literatures: the entropy-production fluctuation
theorems (Evans–Cohen–Morriss, Evans–Searles, Gallavotti–Cohen, and
Kurchan, Lebowitz–Spohn and Maes for stochastic dynamics) and Jarzynski's
work relation ([LIT-tmp47vbz](../literature.d/LIT-tmp47vbz.md)). It credits the work form of the theorem, Eq.
11, to Jarzynski by private communication. Seifert's review
([LIT-tmpcfjz8](../literature.d/LIT-tmpcfjz8.md)) generalises the time-reversal argument into a "master
fluctuation theorem" with conjugate dynamics, and names Eq. 11 the Crooks
fluctuation theorem. [LIT-010](../literature.d/LIT-010.md) states that the Crooks relation needs detailed
balance with the bath, which is the condition behind Eq. 5.

## Bearing on the record

- **[THEORY-026](../theory.d/THEORY-026.md): background, and a pointer for its open question.** Still et
  al. ([LIT-327](../literature.d/LIT-327.md)) cite this paper as a fluctuation theorem that assumes a
  known protocol (their reference 5). Their discrete-time work-step and
  relaxation-step setup is taken from Crooks's 1998 Journal of Statistical
  Physics paper (their reference 17), not from this one. [THEORY-026](../theory.d/THEORY-026.md)'s
  identity is an ensemble average and does not use Eq. 2, so this paper is
  not a source for it. [NOTE-295](NOTE-295.md) asks whether there is a single-trajectory
  version of [LIT-327](../literature.d/LIT-327.md)'s Eq. 14. This paper's ω (Eq. 6) is where such a
  version would start. By my own reckoning from Eq. 6 and the first law,
  not stated in the paper: for a run that starts in equilibrium and ends
  in a nonequilibrium distribution, ⟨ω⟩ = β(⟨W⟩ − ΔF_neq). That is [LIT-327](../literature.d/LIT-327.md)'s
  dissipation (its Eq. 9), not Jarzynski's W − ΔF. But Eq. 2 itself needs
  ω odd under reversal, which fails when the endpoint is not an
  equilibrium or a reversal-invariant steady state. So the theorem does not
  carry over to [LIT-327](../literature.d/LIT-327.md)'s setting as it stands.
- **Prigogine and the minimum principle: no direct bearing.** The paper's
  framing is that near-equilibrium relations are the rule and fluctuation
  theorems the exception. Its Green–Kubo result holds far from equilibrium
  under Gaussianity. It makes no claim about which steady state a system
  selects, so it neither supports nor refutes minimum or maximum
  entropy-production principles.
- **No ML instruction**, and nothing for the anthology.

## Limitations

- **Odd ω is a real restriction.** For general driving, or a steady state
  that is not reversal-invariant, the theorem as stated does not apply.
  Fig. 8 of Jarzynski's 1997 PRE paper is cited as a case where the long-time
  Gaussian fails.
- **Steady-state version impractical**, as the author says. "We have no
  independent method for calculating the probability of a state in a
  nonequilibrium ensemble" (p. 5), so ω cannot be measured directly. Only
  the heat approximation is usable, and only at long times.
- **Classical and Markovian.** Quantum and non-Markovian cases are not
  treated.
- **One model.** The numerical illustrations are a single one-dimensional
  Metropolis particle.

## Open questions

- The author's: "other nontrivial consequences of the fluctuation theorem
  are awaiting study" (§V). Seifert's review ([LIT-tmpcfjz8](../literature.d/LIT-tmpcfjz8.md)) records many that
  followed.
- The relation among the deterministic (Gallavotti–Cohen, Evans–Searles)
  and stochastic theorems was "currently under debate" (p. 1); the paper
  does not settle it.

## Corrections

- none to a seeded skim (there was no seed)
- **Eq. 11 drops a β.** The preprint prints P_F(+βW)/P_R(−βW) =
  e^{−ΔF} e^{+βW}. From ω_F = −βΔF + βW (Eq. 10) the first factor should be
  e^{−βΔF}. Seifert's statement of the relation ([LIT-tmpcfjz8](../literature.d/LIT-tmpcfjz8.md), Eq. 61) has
  the β. Whether the PRE version corrects it was not checked.
- **Title.** The preprint title begins "The Entropy Production Fluctuation
  Theorem…"; the PRE title drops the article and is in sentence case.
- **Date line.** The arXiv-rendered PDF carries "(November 26, 2024)", the
  rendering's \today, not a date of the work.
