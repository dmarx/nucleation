---
number: 106
status: Active
formerly:
- CASE-tmp1gf2k
title: 'The two-hypothesis linearization with endorsement scored on committed predictions: when the shared meaning bends the specialists'' predictions with weight κ and the reading of the evidence with weight κ′, the coupling of interpretation to endorsement is γ = 4ηs(κ′ − κ̄)'
version: 1
standing: fictional
kind: construction
tags:
- cognition
- complex-systems
date: '2026-10-16'
line: distributed-agency
variant_of:
- CASE-099
summary: >-
  Built for [QUESTION-121](../questions.d/QUESTION-121.md)'s formal question: is scoring operators on
  predictions committed before the evidence equivalent to Regime B? The
  construction keeps [CASE-099](CASE-099.md)'s two-hypothesis linearization and replaces
  the score with squared error between each specialist's committed
  prediction and the evidence as read. The coupling γ then has the sign of
  κ′ − κ̄: corrective when the interpretation bends the predictions more
  than the reading of the evidence, null when equally, capturing when
  less. Checked symbolically, and the stability conditions against
  200,000 random draws. Fictional by construction.
supports:
- CLAIM-340
---

# CASE-106: The two-hypothesis linearization with endorsement scored on committed predictions: when the shared meaning bends the specialists' predictions with weight κ and the reading of the evidence with weight κ′, the coupling of interpretation to endorsement is γ = 4ηs(κ′ − κ̄)

## The construction

Keep [CASE-099](CASE-099.md): two hypotheses A and B, the interpretive bias m and the
authority bias a, near (m, a) = (0, 0), with

  (m_{t+1}, a_{t+1})ᵀ = J (m_t, a_t)ᵀ + noise,  J = [[α, β], [γ, δ]].

Change only how the specialists are scored. Each commits a prediction
before the evidence arrives. The A-specialist leans toward A by s > 0, the
B-specialist toward B by s, and both are bent by the shared meaning:

  p_A = s + κ_A m,  p_B = −s + κ_B m.

The evidence arrives as e, with mean 0 at the symmetric state, and is read
through the shared meaning with weight κ′: r = e + κ′m. Each specialist is
scored by squared error, and authority moves with the score difference at
rate η:

  a_{t+1} = δ a_t + η [ (p_B − r)² − (p_A − r)² ].

Linearizing at m = e = 0:

  ∂/∂m = −2s(κ_A + κ_B − 2κ′),  ∂/∂e = 4s,

so, writing κ̄ = (κ_A + κ_B)/2,

  γ = 4ηs(κ′ − κ̄),

and the evidence drives authority with gain 4ηs, which is how the
specialist who predicted well gains it.

## What it shows

1. **The sign of γ is the sign of κ′ − κ̄.** Committing before the evidence
   is not by itself Regime B. It gives γ < 0 when the interpretation bends
   what the specialists predict more than it bends how the evidence is
   read, γ = 0 when the two are bent equally, and γ > 0 when the reading
   of the evidence is bent more. [CASE-092](CASE-092.md)'s Regime A, scoring against the
   dominant interpretation itself, is the limit in which the reading is
   all interpretation.
2. **With γ ≤ 0 there is no capture.** For β > 0 and βγ ≤ 0, J is stable
   exactly when αδ − βγ < 1, that is, |βγ| < 1 − αδ. When J is unstable
   in this range its eigenvalues are complex, so the failure is
   oscillation (over-correction), not capture. With real eigenvalues, λ+ ≤
   max(α, δ) < 1. For βγ > 0, [CASE-099](CASE-099.md)'s condition βγ > (1 − α)(1 − δ)
   holds unchanged.
3. **Revising after the evidence removes learning, not just capture.** If
   the specialists predict after reading the evidence (p = r), the score
   difference is identically zero. γ = 0, as in Regime B, but the evidence
   gain is zero too, so authority stops tracking who predicts well.
   Commitment matters because it keeps the evidence gain 4ηs.

The coupling and the gain were derived with sympy. The stability
conditions were checked numerically: over 200,000 random draws of α, δ ∈
[0, 1), β ∈ [0, 3] and γ ∈ [−3, 3], the stated conditions and the
eigenvalues agreed in every draw. Among draws with βγ < 0, none was
unstable with real eigenvalues. The script is in the contribution's
scratch directory (scratch/formal/check.py).

## What it does not show

- That a mind's predictions and its readings of evidence have weights
  κ, κ′ that can be measured, or what they are.
- Anything away from the symmetric state, or for the nonlinear bounded
  system ([CASE-099](CASE-099.md)'s own limit).
- That squared error is the right score. Another proper score changes the
  constants, and the sign argument should be redone for it.
