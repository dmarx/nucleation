---
number: 1252
status: Active
formerly:
- THEORY-tmp33nos
title: 'In ℓ2-regularized regression held to a fixed training-error tolerance, refitting to one''s own predictions on the same inputs shrinks each eigencomponent of the labels by a factor that falls with its Gram eigenvalue, while the regularization weight needed to meet the tolerance rises as the labels shrink, so repeated rounds amplify regularization and reach the zero function after finitely many; the loss comes from the regularizer acting again, not from information the student lacks'
version: 1
tags:
- learning-theory
date: '2026-10-31'
source:
- LIT-1895
summary: >-
  Mobahi, Farajtabar and Bartlett (2020), [LIT-1895](../literature.d/LIT-1895.md), eqs. 24–37 and
  §§3.2–4; read in [NOTE-1478](../notes.d/NOTE-1478.md), with the paper's illustrative example
  reproduced from its own sample values. Active for the recurrence,
  the rising multiplier and collapse, which are elementary and
  reproduced; the sparsity rate of Theorem 5 is the paper's, proof not
  checked. It does not show that deep networks behave so, and the
  amplification depends on holding the error tolerance fixed.
---

# THEORY-1252: In ℓ2-regularized regression held to a fixed training-error tolerance, refitting to one's own predictions on the same inputs shrinks each eigencomponent of the labels by a factor that falls with its Gram eigenvalue, while the regularization weight needed to meet the tolerance rises as the labels shrink, so repeated rounds amplify regularization and reach the zero function after finitely many; the loss comes from the regularizer acting again, not from information the student lacks

## Source

Mobahi, Farajtabar and Bartlett (2020), [LIT-1895](../literature.d/LIT-1895.md), §§2–4, eqs.
(17)–(52) and Appendix E, pp. 5–13 and 31–32 of arXiv 2002.05715v3; read
in [NOTE-1478](../notes.d/NOTE-1478.md).

## What was actually shown

With f* = g_xᵀ(cI + G)⁻¹y and G = VᵀDV, the fitted values on the
training inputs are Vᵀ D(cI + D)⁻¹ V y. Using them as the next labels
gives z_t = D(c_{t−1}I + D)⁻¹ z_{t−1} in rotated coordinates (eq. 34).
Each component is multiplied by d_k/(c + d_k) < 1, the smaller the
eigenvalue the harder. The multiplier c_t is whatever makes the training
error exactly ε, and eq. 24 bounds it by d√(Kε)/(‖z_t‖ − √(Kε)). It grows
as ‖z_t‖ falls, and once ‖y_t‖² ≤ Kε the zero function is optimal.
Theorem 5 bounds the ratio of surviving coefficients for two eigenvalues
from below by a quantity growing geometrically in t.

Reproduced with the paper's own eleven sample values and spline
regularizer (Appendix E): at ε = 0.045 the multiplier rose from 3 × 10⁻⁵
to 9 × 10⁻³ over rounds 0–3, the mean squared label fell from 0.51 to
0.03, and round 4 collapsed, as the paper reports.

What could have failed: the multiplier could have stayed bounded, so that
rounds converged to a non-zero fixed point. With a fixed tolerance it
cannot.

## What this does not say

- **That information is lost.** The student sees the same inputs and the
  teacher's exact outputs. The loss is the regularizer applied again,
  which an idempotent projection would not do. This is the
  "regularization" case of A16's list of what makes iterated inheritance
  degrade, isolated from the others.
- **That the amplification is unconditional.** It rests on holding ε
  fixed. With a fixed penalty weight the per-round shrinkage is constant
  and the solution still decays to zero, but without the acceleration.
  The paper does not analyse that case.
- **That self-distillation of deep networks works this way.** The NTK
  link is motivation; the CIFAR effects are fractions of a point.
- **That a few rounds help in general.** Whether early rounds help
  depends on how much of the initial fit was noise; the paper shows it in
  one example and in small neural experiments.
- **That Proposition 4's guarantee is informative.** In the paper's own
  example it guarantees less than one round.
