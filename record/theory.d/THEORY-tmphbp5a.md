---
status: Proposed
title: 'Park, Bocchi, D''Amico, Lucini and Aarts show, exactly for a linear rank-1 teacher–student model under full-batch gradient descent and heuristically for nonlinear, finite-data and stochastic extensions, that training shrinks the weight covariance''s random bulk while growing a spike, so an outlier aligned with the teacher detaches by a BBP transition at a critical step size or a critical time set by the step size and the initial weight variance, while the student converges for every step size below one whether or not the outlier has yet appeared'
promote_when: >-
  A second reader confirms eqs. 17–19, 27–28 and 39 and the convergence
  statement of §II D against the paper, and an independent derivation or
  replication (a later version's released code, or another paper)
  reproduces the threshold and the critical time in the linear model.
version: 1
tags:
- learning-theory
- loss-landscapes
- mathematical-statistics
date: '2026-11-22'
source:
- LIT-2990
corroborates:
- CLAIM-837
summary: >-
  Park and colleagues, LIT-2990, read in NOTE-tmpzethm. A dynamical
  reading of the BBP transition: the outlier's appearance in the weight
  spectrum is a matter of step size and time, while the signal is in the
  weights from the first step. Its UTKFace experiments find the leading
  first-layer directions tracking the data's principal components only in
  the large-step regime. Grounds CLAIM-799 (ARG-tmps8aog) and the rival
  reading CLAIM-tmp9atj9 (ARG-tmpun4nl).
---
<!-- inactive-ok-file: CLAIM-799 CLAIM-837 ARG-tmps8aog CLAIM-tmp9atj9 ARG-tmpun4nl — Proposed or new; the claims this reading bears on and the arguments for its support -->

# THEORY-tmphbp5a: Park, Bocchi, D'Amico, Lucini and Aarts show, exactly for a linear rank-1 teacher–student model under full-batch gradient descent and heuristically for nonlinear, finite-data and stochastic extensions, that training shrinks the weight covariance's random bulk while growing a spike, so an outlier aligned with the teacher detaches by a BBP transition at a critical step size or a critical time set by the step size and the initial weight variance, while the student converges for every step size below one whether or not the outlier has yet appeared

## Source

Park, Bocchi, D'Amico, Lucini and Aarts, "Spectral phase transitions and
trainability in neural network learning dynamics", arXiv 2606.28486v1,
LIT-2990, read in NOTE-tmpzethm.

## What was actually shown

- Exactly, X(t) = σ_t²X̂⊥ + θ_t²ŝ_tŝ_tᵀ with a shrinking bulk scale and a
  growing spike (eqs. 17–19); the outlier appears at θ_t² = σ_t²(r + √r)
  (eq. 27), so at t_c = −ln(1 + 1/(r^(1/4)σ_W))/ln(1−ε) (eq. 39), and "the
  optimisation always converges to the correct ground state".
- By the authors' caveat, the boundary εc "is associated with a spectral
  phase transition", while εo "is an optimisation threshold".
- Empirically (UTKFace, ReLU MLPs): cross-seed subspace overlaps separate
  the phases; the leading first-layer direction overlaps the data's first
  principal component at 0.68 and 0.64 in the large-step regimes, which
  converge to a worse minimum, against 0.056 in the ferromagnetic phase.

What could have failed: the outlier could have appeared at the first
step for every step size, or the student failed to converge in the
sub-threshold region; the real networks' overlaps could have shown no
phase structure.

## What this does not say

- Not that the network acquires the signal at t_c: the weights carry it
  from the first step; t_c is when the weight spectrum shows it.
- Not a thermodynamic critical point; the universality class "remains
  unclear", and the phase names are borrowed.
- The nonlinear, multilayer, finite-data and SGD results are first-step,
  first-layer or heuristic; the empirics are one dataset with MLPs.
