---
status: Active
status_note: 'read 2026-10-13 ([NOTE-tmpq7q6s](../notes.d/NOTE-tmpq7q6s.md)): main text, and Appendices A–C and H; the derivations in Appendices D–G were not checked. Held also in the Anthology of the SOTA as [ANTH-LIT-454](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-454.md), read there for what the loss curve hides; read here for what a converged run is, under [ADR-013](../decisions.d/ADR-013.md).'
title: 'The Limiting Dynamics of SGD: Modified Loss, Phase Space Oscillations, and Anomalous Diffusion'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Filed at the owner's request ("read and file this on the nucleation
    record if we don't already have it"). Read from the arXiv PDF of
    2107.09133 v4 (28 December 2023), text extracted with pdftotext.
    `published:` is the v1 date, 19 July 2021. Not held here before; held
    in the anthology as ANTH-LIT-454, with ANTH-NOTE-202, ANTH-THEORY-031
    and ANTH-SOTA-270.
tags:
- learning-theory
- loss-landscapes
- thermodynamics
- anthology-candidate
date: '2026-10-13'
published: '2021-07-19'
arxiv: '2107.09133'
first_author: 'Kunin'
keywords:
- 'SGD limiting dynamics'
- 'underdamped Langevin equation'
- 'modified loss'
- 'broken detailed balance'
- 'probability current'
- 'anomalous diffusion'
implementations: []
summary: >-
  Kunin, Sagastuy-Brena, Gillespie, Margalit, Tanaka, Ganguli & Yamins
  (2021). Long after the loss converges, networks trained with SGD keep
  moving at a constant speed, and their distance from where they were grows
  as a power law in steps. Modelling SGD with momentum at finite learning
  rate and batch size as an underdamped Langevin equation, the paper solves
  linear regression exactly: an Ornstein–Uhlenbeck process whose stationary
  distribution is a Gibbs distribution on a modified loss, not the training
  loss, in broken detailed balance, so probability currents drive
  oscillations in phase space. Under a quadratic approximation, a
  pre-trained ResNet-18 on ImageNet shows the predicted isotropic
  exploration, velocity regularization, oscillations and speed.
---
<!-- inactive-ok-file: THEORY-tmp4lwrf — Proposed; the account filed from this reading, open -->

# LIT-tmp0kjhc: The Limiting Dynamics of SGD: Modified Loss, Phase Space Oscillations, and Anomalous Diffusion

Daniel Kunin, Javier Sagastuy-Brena, Lauren Gillespie, Eshed Margalit, Hidenori Tanaka, Surya Ganguli, Daniel L. K. Yamins (2021) — [ARXIV-2107.09133](https://arxiv.org/abs/2107.09133)

## Key takeaways

- **Converged is not stationary at a point.** Resumed training of five
  pre-trained ImageNet convnets moves at a near-constant step size, and the
  squared distance from the pre-trained weights grows as k^c with c between
  about 1.07 and 1.62 (Fig. 1).
- **What SGD samples is not the training loss.** For linear regression
  with gradient-noise covariance proportional to the Hessian, the
  stationary distribution is Gibbs on a modified loss Ψ(θ, v). Its
  parameter part has curvature H⁻¹(H + λI)/(η(1 + β)), which is isotropic
  in the Hessian's column space when weight decay is negligible. Its
  velocity part, v⊺H⁻¹v, penalizes motion along low-curvature directions.
- **Broken detailed balance.** The phase-space stationary state carries a
  non-zero probability current, so the dynamics rotate in each
  eigen-plane of the Hessian at rates set by its eigenvalue. With many
  incommensurate rates the paths are space-filling, not limit cycles.
- **The hyperparameters set the transport.** Instantaneous speed is
  η²σ²tr(H)/(S(1 − β²)), matched across a sweep of learning rates, batch
  sizes and momenta. A larger learning rate makes the oscillators
  underdamped and lowers the diffusion exponent: faster learning rate,
  slower global travel.

## Standing in the record

Read for the learned-structure line's question of what training reaches
([QUESTION-069](../questions.d/QUESTION-069.md)): a converged run is a nonequilibrium stationary
distribution whose shape is set by the optimizer as much as by the loss.
The anthology reads the same paper for practice, as one of three ways an
aggregate loss curve hides what training does ([ANTH-THEORY-031](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-031.md)). The
reading here is [NOTE-tmpq7q6s](../notes.d/NOTE-tmpq7q6s.md), and the account it supports is
[THEORY-tmp4lwrf](../theory.d/THEORY-tmp4lwrf.md).
