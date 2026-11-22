---
number: 883
status: Proposed
formerly:
- CLAIM-tmpyepkb
title: 'In the Geometry model of independent skills, with task vectors generic to the coordinates and many dimensions, sign descent follows gradient descent''s own path with its clock divided by the gradient norm, so each weaker skill accelerates while a stronger one remains, has made exactly gradient descent''s progress when the stronger is learned, and is learned at a time whose ratio to the first approaches (n − ε)/(1 − ε), which is 2 for two skills as the threshold tightens; with coordinate-aligned tasks all skills are learned together'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-045: the
    derivation QUESTION-193's first limb asks for, in the mean-field limit.
    The full derivation is in scratch/studies/lead-045/README.md.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation's steps: the per-step increment of a skill
  under sign descent, the Gaussian identity applied to it, or the
  concentration of the sum over coordinates for a fixed number of skills as
  the dimension grows; or sign descent on the Geometry model with random
  orthonormal task vectors departing from the derived ODE by an amount that
  does not shrink as the dimension grows and the step falls. Not defeated by
  departures at the end of training, where sign descent oscillates at the
  step size and the derivation says it does not apply, or by networks whose
  skills interact, which the model excludes.
tags:
- learning-theory
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-193
- QUESTION-039
grounds:
- THEORY-253
summary: >-
  The derivation [QUESTION-193](../questions.d/QUESTION-193.md) asks for, in the mean-field limit. For the
  Geometry model of [THEORY-253](../theory.d/THEORY-253.md), loss Σ p_i u_i² with u_i = 1 − θ·t_i, a
  sign step with t_i generic to the coordinates and d large gives
  du_j/dt = −c p_j u_j / ‖p∘u‖₂, c = η√(2d/π): gradient flow with its clock
  divided by the gradient norm. So the path in skill space is gradient
  descent's and only the timing differs. Each weaker skill accelerates while
  any stronger one remains, so its onset is delayed in time but not in
  progress; total skill grows at a rate between c and c√n; and in the
  limit of well-separated frequencies t_n/t_1 → (n − ε)/(1 − ε), which is
  2.11 for two skills at ε = 0.1 and 2 as ε → 0. With coordinate-aligned
  tasks every skill moves at the same rate; for the Hadamard rotation the
  first phase is exact. The derived ratios match simulation within 2%
  ([CASE-319](../cases.d/CASE-319.md)), which checks the derivation and does not warrant it.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-319 CLAIM-882 — new; the study this derivation was checked in, and the network claim beside it -->

# CLAIM-883: In the Geometry model of independent skills, with task vectors generic to the coordinates and many dimensions, sign descent follows gradient descent's own path with its clock divided by the gradient norm, so each weaker skill accelerates while a stronger one remains, has made exactly gradient descent's progress when the stronger is learned, and is learned at a time whose ratio to the first approaches (n − ε)/(1 − ε), which is 2 for two skills as the threshold tightens; with coordinate-aligned tasks all skills are learned together

## The claim

Take the Geometry model of [THEORY-253](../theory.d/THEORY-253.md): loss ℓ(θ) = Σ_i p_i u_i², with
residual u_i = 1 − s_i, skill level s_i = θ·t_i and orthonormal t_i in R^d.
A skill counts as learned at u_i = ε.

1. **The equation.** Let the entries of the t_i across coordinates behave
   as independent N(0, 1/d) draws (task vectors generic to the
   coordinates), with d large against the number of skills n and the step
   η small against the residuals. Sign descent then follows
   du_j/dt = −c p_j u_j / ‖p∘u‖₂ per step, with c = η√(2d/π).
2. **Same path, another clock.** Gradient flow gives du_j/dt = −2p_j u_j.
   The two differ by one positive factor common to every skill, so the
   trajectory in skill space is the same, u_j = exp(−p_j τ), and only the
   time along it differs: t(τ) = (1/c) ∫₀^τ ‖p∘exp(−pτ′)‖₂ dτ′. When skill
   1 is learned, skill 2 has made exactly the progress it makes under
   gradient descent, 1 − ε^(p₂/p₁).
3. **Delayed onset.** d/dt ln(ds_j/dt) has the sign of
   Σ_i p_i² u_i² (p_i − p_j). The strongest skill decelerates from the start;
   every weaker one accelerates while any stronger one is unlearned, so its
   fastest progress comes as the stronger ones finish. Under gradient
   descent every skill's fastest progress is at the start.
4. **The ratio.** d(Σ s_i)/dt = c‖p∘u‖₁/‖p∘u‖₂ lies in [c, c√n]. As the
   frequency ratios p_{i+1}/p_i → 0, one term dominates except at
   crossovers whose contribution vanishes, each skill costs 1/c in turn,
   and t_n/t_1 → (n − ε)/(1 − ε): 2.11 for two skills at ε = 0.1, and 2 as
   ε → 0. Under gradient descent t_n/t_1 = p₁/p_n.
5. **Alignment.** If each t_i is supported on its own coordinates, every
   coordinate's sign is fixed whatever the frequencies, every skill moves at
   the same rate, and all are learned together. For the 4 × 4 Hadamard
   rotation, exactly and for any step: while λ₁x₁ > Σ_{j>1} λ_j x_j, only x₁
   moves.

## Why it holds

A sign step moves skill j by η Σ_k t_jk sign(z_k), z_k = Σ_i p_i u_i t_ik. For
jointly Gaussian X and Z, E[X sign Z] = √(2/π) Cov(X, Z)/σ_Z; here
Cov(t_jk, z_k) = p_j u_j/d and σ_Z = ‖p∘u‖₂/√d. The sum over d coordinates
concentrates on d times the expectation as d grows with n fixed. Items 2 to
4 follow from item 1 by calculus; item 5 by inspection of the sign vector.
The full working is in scratch/studies/lead-045/README.md.

## What it does not say

- **Not a theorem with error bounds.** The concentration step is a
  law-of-large-numbers argument, not a bound uniform over the trajectory,
  and orthonormal t_i are not exactly independent Gaussians. The agreement
  with simulation, to within 2% at d = 1000 ([CASE-319](../cases.d/CASE-319.md)), checks it.
- **Not the end of training**, where sign descent oscillates at the step
  size, and not small d with arbitrary rotations, where only the Hadamard
  case was worked.
- **Not about networks.** Skills that share parameters interact, which the
  model excludes; what one network did is [CLAIM-882](CLAIM-882.md).
- **Not Adam at default settings.** Adam with β₁ = β₂ = 0 is sign descent;
  at the default β its ratios lie between sign descent's and gradient
  descent's and are not derived here.

## What it changes

[THEORY-253](../theory.d/THEORY-253.md) records the Domino effect as simulation with a fitted
Resource model, du_i/dt = −η_eff p_i u_i/(Σ_j p_j u_j + N₀). This derives a
model of the same family from the optimizer, with the ℓ₂ norm in place of
the ℓ₁ norm and no fitted constant, and the derived form fits the
simulation better at intermediate frequencies. It also says what the
sequence is: a re-timing of gradient descent's path, not a different path.
The paper's mechanism, sign(g₁ + g₂) ≈ sign(g₁) when ‖g₁‖ ≫ ‖g₂‖, is the
dominance case of item 2. It answers the first limb of [QUESTION-193](../questions.d/QUESTION-193.md) for
generic high-dimensional misalignment, at the level of rigour stated above,
and leaves its second limb to [CLAIM-882](CLAIM-882.md).
