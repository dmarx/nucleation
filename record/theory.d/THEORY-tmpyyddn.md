---
status: Active
title: 'A two-layer linear network trained by gradient flow on white inputs from a decoupled, balanced start learns each singular mode of its input–output correlation in a logistic rise that waits a time of order its inverse strength times the log of the inverse initial scale, so the modes arrive one at a time in order of strength; a single-layer network on the same data learns every mode on one timescale with no plateau, so under these conditions the stages come from the product of layers and the data''s spectrum'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-186 and filed Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-186 (batch 024,
    ADR-047). THEORY-186 joined this exact solution to a claim, supported
    by simulation, that small random, unbalanced starts follow it. This
    THEORY holds the exact solution and the shallow contrast, from LIT-862
    and LIT-864. They were re-derived for the split, written out below
    (ADR-047 v2). THEORY-186 keeps the random-start claim and extends this
    one.
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-10-19'
source:
- LIT-862
- LIT-864
summary: >-
  Saxe, McClelland and Ganguli (2014, 2019), [LIT-864](../literature.d/LIT-864.md) and [LIT-862](../literature.d/LIT-862.md), read in
  [NOTE-667](../notes.d/NOTE-667.md) and [NOTE-666](../notes.d/NOTE-666.md), re-derived here. From a decoupled, balanced start
  the two-layer equations keep the SVD basis of Σyx, and each mode's
  strength obeys τȧ = 2a(s − a), a logistic rise. One weight matrix on the
  same data relaxes every mode exponentially on the one timescale τ. It
  does not say that random starts follow the solution, which is
  [THEORY-186](THEORY-186.md)'s.
extended_by:
- THEORY-186
---
<!-- inactive-ok-file: THEORY-186 THEORY-187 — Proposed; the account this core was split from and that extends it, and the depth account set beside it, cited as open -->

# THEORY-tmpyyddn: A two-layer linear network trained by gradient flow on white inputs from a decoupled, balanced start learns each singular mode of its input–output correlation in a logistic rise that waits a time of order its inverse strength times the log of the inverse initial scale, so the modes arrive one at a time in order of strength; a single-layer network on the same data learns every mode on one timescale with no plateau, so under these conditions the stages come from the product of layers and the data's spectrum

## Source

Saxe, McClelland and Ganguli (2014), [LIT-864](../literature.d/LIT-864.md), Eqs. 6–12 and Appendix A,
read in [NOTE-667](../notes.d/NOTE-667.md), and the same authors' 2019 restatement, [LIT-862](../literature.d/LIT-862.md),
Eqs. 2–11, read in [NOTE-666](../notes.d/NOTE-666.md). Re-derived here as a check.

## What was actually shown

Take ŷ = W₂W₁x with white inputs (Σx = I), loss ½E‖y − W₂W₁x‖², and
gradient flow with time constant τ. Write Σyx = U S Vᵀ.

- **The deep network.** Gradient flow is τẆ₁ = W₂ᵀ(Σyx − W₂W₁) and
  τẆ₂ = (Σyx − W₂W₁)W₁ᵀ. Start decoupled and balanced:
  W₁ = R C Vᵀ, W₂ = U C Rᵀ, with R orthonormal and C = diag(c_α). Then
  W₂W₁ = U C² Vᵀ and τẆ₁ = R C(S − C²) Vᵀ, so the form is kept and
  τċ_α = c_α(s_α − c_α²); the W₂ equation gives the same. For a_α = c_α²,
  τȧ_α = 2a_α(s_α − a_α), solved by
  a_α(t) = s_α e^{2s_αt/τ} / (e^{2s_αt/τ} − 1 + s_α/a_α⁰). Mode α reaches
  half its final strength at t_α = (τ/(2s_α)) ln(s_α/a_α⁰ − 1), and passes
  from a fraction δ to 1 − δ of s_α in time (τ/s_α) ln((1−δ)/δ), whatever
  a_α⁰. So, as the initial scale goes to zero, each mode waits a time of
  order (τ/s_α) ln(1/a_α⁰) and then rises in a transition whose width is a
  vanishing fraction of the wait. Stronger modes go first.
- **The shallow network.** For ŷ = Wx, τẆ = Σyx − W, so
  W(t) = Σyx + (W(0) − Σyx)e^{−t/τ}. In the SVD basis,
  b_α(t) = s_α(1 − e^{−t/τ}) + b_α⁰ e^{−t/τ}: every mode relaxes on the one
  timescale τ, exponentially, with no plateau.

The same data give stages through two layers and none through one, so,
under these conditions, the stages come from the product of the layers and
the spectrum of Σyx.

What could have failed: a start that is not decoupled. Then the
off-diagonal terms couple the modes, and the per-mode equations do not
close.

## What this does not say

- **Not from random initialisation.** That small random, unbalanced
  weights follow these curves is simulated in [LIT-862](../literature.d/LIT-862.md) (Fig. 3C), not
  proved. It stays with [THEORY-186](THEORY-186.md).
- **Not for correlated inputs.** With Σx ≠ I the input and output bases
  need not align.
- **Not that nonlinear networks learn this way,** nor anything about
  depth beyond two layers, which is [THEORY-187](THEORY-187.md)'s.
- **Not discontinuities.** Each rise is smooth, and sharp only relative to
  the plateau before it.
