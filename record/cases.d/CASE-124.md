---
number: 124
status: Active
formerly:
- CASE-tmpc0mv0
title: 'A maintained legibility lean as a third state of the linearized meaning–authority model: authority moves the lean r of the categories through which evidence is read, and r feeds interpretation or authority, with its own persistence λ'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed from the owner's review of this PR on 2026-10-21, which proposed
    the construction with the route r → m and its witness. The route r → a
    (a direct effect on scoring) and the slow-mode witness are the record's,
    added when the construction was checked.
- version: 2
  date: '2026-10-21'
  note: >-
    Corrected at the owner's second review of 2026-10-21: the μ arrow is a
    direct effect of the legibility regime on scoring, not a varying κ′. If r
    only varied κ′ (κ′ = κ′₀ + c r), its effect on authority would be
    4ηs c r m, second order at symmetry, and would move no linear threshold.
    The result is unchanged.
standing: fictional
kind: construction
tags:
- complex-systems
- self-governance
date: '2026-10-21'
line: distributed-agency
variant_of:
- CASE-099
illustrates:
- CLAIM-400
summary: >-
  [CASE-099](CASE-099.md)'s two-variable linearization, meaning bias m and authority bias a,
  given a third state r: the lean of a maintained legibility regime, the
  categories, reporting requirements and evidence channels through which
  evidence becomes readable. Authority moves r (ε), r moves interpretation
  (ν) or authority (μ), and r persists at rate λ. Two witnesses, both
  checked: one in which the two-variable loop is stable and the
  three-variable one is not, and one in which the system is stable but r
  holds a lean long after m and a would have decayed without it.
supports:
- CLAIM-400
- CLAIM-tmpd6q2w
variants:
- CASE-tmpydmf8
---

# CASE-124: A maintained legibility lean as a third state of the linearized meaning–authority model: authority moves the lean r of the categories through which evidence is read, and r feeds interpretation or authority, with its own persistence λ

## The case

[CASE-099](CASE-099.md)'s linearization at the symmetric state, with a third coordinate:

    m_{t+1} = α m_t + β a_t + ν r_t
    a_{t+1} = γ m_t + δ a_t + μ r_t
    r_{t+1} =         ε a_t + λ r_t

- m is the meaning bias and a the authority bias, as in [CASE-099](CASE-099.md), with
  β authority shaping interpretation and γ interpretation shaping
  endorsement ([CLAIM-330](../claims.d/CLAIM-330.md)).
- r is the lean of the legibility regime toward one interpretation: which
  categories exist, what is recorded, which sources are channels. It is
  [QUESTION-253](../questions.d/QUESTION-253.md)'s "third, slower variable".
- ε ≥ 0: authority moves the regime.
- ν ≥ 0: the regime moves what is interpreted (the route r → m, proposed
  in the owner's review of 2026-10-21).
- μ ≥ 0: the regime moves endorsement directly: what it records or scores
  counts toward authority whatever the reading. This is not the question's
  reading of r as setting [CLAIM-340](../claims.d/CLAIM-340.md)'s κ′. There γ = 4ηs(κ′ − κ̄), so a
  regime that only varies κ′ (κ′ = κ′₀ + c r) adds 4ηs c r m to the
  authority update, a product that is second order at symmetry and enters
  no linearization. The μ arrow is the linear, additive effect a regime has
  when it changes the scoring itself.
- 0 ≤ α, δ, λ < 1: each variable is stable alone, as in [CLAIM-330](../claims.d/CLAIM-330.md). λ is
  the regime's persistence; λ near 1 is a slow regime.

## Witness 1: the loop stable, the system not

The review's parameters, with μ = 0: α = δ = λ = 0.5, β = 0.1,
γ = ν = ε = 0.5.

- Two-variable system (m, a): spectral radius 0.7236 (= 0.5 + √0.05).
  βγ = 0.05 < (1 − α)(1 − δ) = 0.25, so it is stable.
- Three-variable system: spectral radius 1.0333. Unstable.
- The determinant of I − J₃ is (1 − λ)[(1 − α)(1 − δ) − βγ] − νεγ =
  0.5 · 0.2 − 0.125 = −0.025 < 0.

## Witness 2: stable, with a lean that outlasts

α = δ = 0.5, β = 0.1, γ = 0.5, ν = 0.02, μ = 0, ε = 0.1, λ = 0.95.

- Eigenvalues 0.2798, 0.7139, 0.9563. Stable.
- From (m, a, r) = (1, 1, 0), at t = 40 the state is
  (0.0056, 0.0062, 0.0977). Without r, the two-variable system decays at
  rate 0.7236, and (m, a) would be of order 10⁻⁶ by t = 40.
- The impulse response of m to a shock in a has a 6×6 Hankel matrix of
  rank 3 (singular values 0.316, 0.0198, 0.0044, then 10⁻¹⁸). No linear
  two-state system has that response: the projection on (m, a) is not a
  closed first-order two-variable system.

Checked by symbolic determinant and numerics on 2026-10-21.

## What it can show

That a regime which persists and is moved by authority behaves, at the
instability threshold, exactly like stronger two-variable couplings, and
away from the threshold like something the two-variable model cannot
represent ([CLAIM-400](../claims.d/CLAIM-400.md)).

## What it cannot show

- That any institution's categories have such dynamics, or that legibility
  must be modelled as a state. If the regime is an instantaneous function
  of m and a, it folds into β, γ, δ and the two-variable model suffices.
- Anything beyond the linearization: no claim about nonlinear lock-in,
  bistability or the size of an advantage once it grows.
- That the lean is wrong. r measures a lean toward one interpretation, not
  a distortion; tracking a real difference is a lean too.

## Note of 2026-10-24: an observational semantics, and three neighbours

The owner: "i think we already have a three variable system somewhere,
where the third component is described as legibility" (workbench entry of
2026-10-24, U18). The exchange made this case the core of its toy-model
programme for protective lock-in, in place of a new two-state model
([CASE-tmpo8uso](CASE-tmpo8uso.md)). Additions and cautions:

- **A mechanism for ν.** Selective admission of evidence gives
  ν = η_m χ σ′(c) and reads r as an exponentially weighted history of
  authority ([CASE-tmpydmf8](CASE-tmpydmf8.md)).
- **Two levels of legibility.** [TERM-064](../terms.d/TERM-064.md)'s legibility is a relation of a
  representation, an observer's capacities and a task. This case's r is a
  signed lean of a maintained regime, not a score of how much information
  the organization has; a positive lean can help or harm. An observation
  kernel Z ∼ K_r(· | Y), with usable information measured as best risk for
  a bounded observer on a task fixed independently, would give r that
  semantics ([CLAIM-199](../claims.d/CLAIM-199.md), [THEORY-846](../theory.d/THEORY-846.md)). A regime can serve one task and
  disable another for the same observer ([CASE-tmpswmo9](CASE-tmpswmo9.md)).
- **An organizational baseline.** March's mutual learning of code and
  members ([THEORY-142](../theory.d/THEORY-142.md)) already shows conformity destroying the diversity
  needed for later correction. The informative contrast is a minority that
  stays present and accurate but is not credited because evaluation runs
  through the prevailing regime ([CASE-144](CASE-144.md)'s note of 2026-10-24).
- **Performative feedback.** A policy can change the world sampled as well
  as how it is read ([CLAIM-402](../claims.d/CLAIM-402.md)'s note of 2026-10-24).
- **An independent standard.** Adaptation is judged against fixed
  reference demands and a feasible set ([CLAIM-357](../claims.d/CLAIM-357.md), [CLAIM-361](../claims.d/CLAIM-361.md)), so a model
  cannot call its own persistence success.

Head-to-head results belong to [QUESTION-100](../questions.d/QUESTION-100.md). A reported mean-field run is
recorded, unchecked, in [CASE-tmpydmf8](CASE-tmpydmf8.md).
