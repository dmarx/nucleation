---
number: 400
status: Active
formerly:
- CLAIM-tmp4v4na
title: 'In the meaning–authority model linearized at symmetry, a third, maintained legibility state that authority moves (ε) and that moves interpretation (ν) or endorsement (μ), with persistence λ < 1 and nonnegative couplings, destabilizes the symmetric state exactly when the two-variable condition holds with β + νε/(1 − λ) in place of β and δ + με/(1 − λ) in place of δ: at the threshold the regime is indistinguishable from stronger two-variable couplings, and the slower it is the more it adds, while away from the threshold it adds a mode that no two-variable model has, so a lean in the regime can outlast the advantages it was built from'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed from the owner's review of this PR on 2026-10-21, which proposed
    the three-variable construction for QUESTION-253 with the route
    r → m, its threshold condition and an unstable witness. Checked
    symbolically and on 200,000 random parameter draws. The record adds
    the route r → a, the reduction to effective two-variable couplings,
    and the stable slow-mode witness.
- version: 2
  date: '2026-10-21'
  note: >-
    Corrected at the owner's second review of 2026-10-21: the μ arrow is a
    direct effect of the legibility regime on scoring, not a varying κ′. If r
    only varied κ′ (κ′ = κ′₀ + c r), its effect on authority would be
    4ηs c r m, second order at symmetry, and would move no linear threshold.
    The result is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a nonnegative J₃ with 0 ≤ α, δ, λ < 1 whose
  spectral radius is above one while that of the two-variable matrix with
  β_eff = β + νε/(1 − λ) and δ_eff = δ + με/(1 − λ) is below one, or the
  reverse; or a two-state linear system whose impulse response matches
  CASE-124's second witness.
tags:
- complex-systems
- self-governance
date: '2026-10-21'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-330
grounds:
- CASE-124
- CASE-099
answers:
- QUESTION-253
uses:
- TERM-064
summary: >-
  [QUESTION-253](../questions.d/QUESTION-253.md) asked whether authority's effect on what becomes
  legible as evidence is a third channel with its own instability
  condition, or [CLAIM-340](CLAIM-340.md)'s κ′ renamed. Both, in different respects. With
  a maintained legibility state r, det(I − J₃) = (1 − λ)[(1 − α)(1 − δ) −
  βγ] − ε[νγ + μ(1 − α)], which is (1 − λ) times [CLAIM-330](CLAIM-330.md)'s expression
  with β_eff = β + νε/(1 − λ) and δ_eff = δ + με/(1 − λ). So the
  instability threshold is a two-variable one with stronger couplings, and
  a slower regime (λ near 1) adds more. Away from the threshold, r is a
  third mode: a lean in the regime can hold interpretation and authority
  off symmetry after they would have relaxed, which no two-variable
  parameters reproduce.
illustrated_by:
- CASE-124
- CASE-156
supports:
- CLAIM-444
---

# CLAIM-400: In the meaning–authority model linearized at symmetry, a third, maintained legibility state that authority moves (ε) and that moves interpretation (ν) or endorsement (μ), with persistence λ < 1 and nonnegative couplings, destabilizes the symmetric state exactly when the two-variable condition holds with β + νε/(1 − λ) in place of β and δ + με/(1 − λ) in place of δ: at the threshold the regime is indistinguishable from stronger two-variable couplings, and the slower it is the more it adds, while away from the threshold it adds a mode that no two-variable model has, so a lean in the regime can outlast the advantages it was built from

## The claim

The system is [CASE-124](../cases.d/CASE-124.md):

    J₃ = | α  β  ν |
         | γ  δ  μ |
         | 0  ε  λ |

with all entries nonnegative and 0 ≤ α, δ, λ < 1.

1. **The threshold.**
   det(I − J₃) = (1 − λ)[(1 − α)(1 − δ) − βγ] − ε[νγ + μ(1 − α)].
   For a nonnegative matrix, the spectral radius is below one exactly when
   I − J₃ is a nonsingular M-matrix, that is, when its leading principal
   minors are positive. Where the two-variable loop is itself stable
   (βγ < (1 − α)(1 − δ)), instability therefore comes to det(I − J₃) < 0. With μ = 0 this is the review's
   form, γ(β + νε/(1 − λ)) > (1 − α)(1 − δ).
2. **The reduction.** Dividing by 1 − λ,
   det(I − J₃) / (1 − λ) = (1 − α)(1 − δ_eff) − β_eff γ, with
   β_eff = β + νε/(1 − λ) and δ_eff = δ + με/(1 − λ). That is [CLAIM-330](CLAIM-330.md)'s
   expression for a two-variable system with those couplings, and J₃ is
   unstable exactly when that two-variable system is, whether or not the
   original loop was stable. The
   regime's contribution is its steady-state gain: authority's effect on r,
   times r's effect, divided by how fast r forgets.
3. **The mode.** Away from the threshold, J₃ has three eigenvalues and the
   projection on (m, a) is not a closed first-order two-variable system.
   In [CASE-124](../cases.d/CASE-124.md)'s second witness, the impulse response of m has Hankel
   rank 3, and a lean in r keeps m and a off symmetry long after the
   two-variable system would have returned.

## How it was checked

- The determinant identity and the reduction, symbolically (sympy).
- The equivalence of "spectral radius > 1" with the reduced two-variable
  condition, on 200,000 random draws with α, δ, λ uniform on [0, 0.99) and
  β, γ, ν, μ, ε uniform on [0, 2): no mismatch.
- Both witnesses numerically.

## What it answers

[QUESTION-253](../questions.d/QUESTION-253.md) asked for "a showing either that the condition reduces
to [CLAIM-330](CLAIM-330.md)'s with κ′ replaced by a function of r (the layer is κ′
renamed) or that it allows an instability, or a slow mode, that no choice
of the two-variable parameters gives". The threshold reduces, with the
regime's steady-state gain absorbed into β (the ν arrow) or δ (the μ
arrow, a direct effect of the regime on scoring). The question's own
reading, r setting κ′, is not the μ arrow: since γ = 4ηs(κ′ − κ̄)
([CLAIM-340](CLAIM-340.md)), a regime that only varies κ′ adds a term in r·m to the
authority update, second order at symmetry, so it moves no linear
threshold at all. In that reading the layer is not even κ′ renamed at
linear order; it matters only away from symmetry. The slow mode does not
reduce.
So whether legibility is "renamed" depends on what is asked of the model:
for whether symmetry breaks, it is; for how long a lean lasts and how the
system returns, it is not.

## What it does not say

- That legibility must be modelled as a state. If the regime is an
  instantaneous function of m and a, it folds into the couplings and the
  two-variable model suffices. Whether an organization's legibility
  regime has dynamics of its own is empirical, and the record holds no
  case of it ([QUESTION-253](../questions.d/QUESTION-253.md)'s "What it does not ask").
- Anything outside the linearization at symmetry: not lock-in, not
  bistability, not the size an advantage reaches.
- That a slower regime is worse. It adds more at the threshold, and holds
  a lean longer, whether the lean tracks a real difference or not.
- That the third arrow is the only way to get a third mode. Any third
  state coupled into the loop would do; the construction's content is
  that a legibility regime is one natural reading of such a state.
