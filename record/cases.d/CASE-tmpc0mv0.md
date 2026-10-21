---
status: Active
title: 'A maintained legibility lean as a third state of the linearized meaning–authority model: authority moves the lean r of the categories through which evidence is read, and r feeds interpretation or authority, with its own persistence λ'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed from the owner's review of this PR on 2026-10-21, which proposed
    the construction with the route r → m and its witness. The route r → a
    (the question's κ′ reading) and the slow-mode witness are the record's,
    added when the construction was checked.
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
- CLAIM-tmp4v4na
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
- CLAIM-tmp4v4na
---

# CASE-tmpc0mv0: A maintained legibility lean as a third state of the linearized meaning–authority model: authority moves the lean r of the categories through which evidence is read, and r feeds interpretation or authority, with its own persistence λ

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
  [QUESTION-tmp4147z](../questions.d/QUESTION-tmp4147z.md)'s "third, slower variable".
- ε ≥ 0: authority moves the regime.
- ν ≥ 0: the regime moves what is interpreted (the route r → m, proposed
  in the owner's review of 2026-10-21).
- μ ≥ 0: the regime moves endorsement directly, by setting how evidence is
  scored, which is the question's reading of r as setting [CLAIM-340](../claims.d/CLAIM-340.md)'s κ′.
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
represent ([CLAIM-tmp4v4na](../claims.d/CLAIM-tmp4v4na.md)).

## What it cannot show

- That any institution's categories have such dynamics, or that legibility
  must be modelled as a state. If the regime is an instantaneous function
  of m and a, it folds into β, γ, δ and the two-variable model suffices.
- Anything beyond the linearization: no claim about nonlinear lock-in,
  bistability or the size of an advantage once it grows.
- That the lean is wrong. r measures a lean toward one interpretation, not
  a distortion; tracking a real difference is a lean too.
