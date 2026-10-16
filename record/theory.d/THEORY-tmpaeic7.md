---
status: Proposed
promote_when: >-
  An analysis or simulation showing that from small random initial weights
  not aligned with the data's eigenbasis, a linear-attention layer trained
  on in-context regression aligns with that basis before or while its
  modes are learned, so that the per-mode logistic curves and their
  ordering by input variance hold without the alignment being assumed; or
  the same staged learning measured in a trained layer whose tasks do not
  share the input covariance's eigenbasis. Timing coincidences of spectral
  measures in non-linear transformers cannot settle it, and neither can
  more simulations from aligned starts.
title: "A linear-attention layer trained on in-context regression learns as a two-layer linear network does: when tasks share the input covariance's eigenbasis and the weights stay aligned with it, each input mode is learned on a logistic curve whose timescale falls with the square of its variance, so learning is staged by the input spectrum, and the layer converges to a preconditioned estimator"
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-10-16'
source:
- LIT-859
extends:
- THEORY-186
answers:
- QUESTION-039
summary: >-
  Mainali & Teixeira (2025), [LIT-859](../literature.d/LIT-859.md), read in [NOTE-658](../notes.d/NOTE-658.md). The prediction of
  one linear-attention layer reduces to p₂ W Σ̂_x q₁ x_q, a product of two
  learned factors, so averaged gradient flow decouples into modes with
  τ_α dp_α/dt = q_α(1 − p_α q_α s^∞_α) and τ_α = (ηP s_α²)⁻¹, logistic from a
  balanced start. The fixed point ŷ = W Σ̂_x [((N+1)/N)Σ_x + (Tr Σ_x/N)I]⁻¹ x_q
  is the one Ahn et al. and Zhang, Frei & Bartlett found; the trajectory
  is new. Alignment of the weights with the data's eigenbasis is assumed
  throughout, the null blocks vanish only in expectation over tasks, and
  the transfer to non-linear transformers is timing coincidences.
supports:
- CLAIM-118
---
<!-- inactive-ok-file: THEORY-186 — Proposed; the account this one extends, and no firmer than it -->
<!-- inactive-ok-file: CLAIM-118 THEORY-169 THEORY-212 THEORY-229 — Proposed; the claim that grounds on this paper and neighbouring accounts, named in Connections, not leaned on -->

# THEORY-tmpaeic7: A linear-attention layer trained on in-context regression learns as a two-layer linear network does: when tasks share the input covariance's eigenbasis and the weights stay aligned with it, each input mode is learned on a logistic curve whose timescale falls with the square of its variance, so learning is staged by the input spectrum, and the layer converges to a preconditioned estimator

## Source

Mainali & Teixeira (2025), [LIT-859](../literature.d/LIT-859.md) (NeurReps workshop, arXiv v2), read in
full in [NOTE-658](../notes.d/NOTE-658.md). [NOTE-658](../notes.d/NOTE-658.md) filed no THEORY because the result concerns
training transformers and the staged learning is Saxe et al.'s pattern,
which the record then did not hold as a source. The record now holds it as
[THEORY-186](THEORY-186.md), which this account carries to attention.

## What was actually shown

**The model.** One layer, one head, attention without softmax,
f(Z) = Z + W^P (ZZᵀ/N) W^Q Z, with tokens (x_i, y_i) as columns and the
query padded with zeros. Inputs x ~ N(0, Σ_x) with Σ_x = USUᵀ; a fixed set
of P tasks W^µ = UΛ^µUᵀ with Gaussian eigenvalues and the same U; squared
error on the query; small-step SGD, averaged over tasks and data, taken to
continuous time.

**The reduction (Eq. 8).** Two blocks of the weights have zero expected
gradient at zero, so the prediction is ŷ ≈ p₂ W^µ Σ̂_x q₁ x_q, a product of
two learned factors around the context's statistics.

**The dynamics (Eqs. 9–13).** Assuming p₂ and q₁ stay diagonal in U, each
mode obeys τ_α dp_α/dt = q_α(1 − p_α q_α s^∞_α) and the same with p and q
exchanged, with τ_α = (ηP s_α²)⁻¹ and s^∞_α = ((N+1)s_α + Tr S)/N. From a
balanced start a_α = p_α q_α is logistic, with escape time from ε about
(τ_α/2) log(1/(s^∞_α ε)). Modes of larger input variance are learned first.
The expected loss is an explicit sum over modes (Eq. 14), and the
predictions match simulation closely (Figs. 1–3A).

**The fixed point (Eq. 11).** ŷ(∞) ≈ W^µ Σ̂_x [((N+1)/N)Σ_x + (Tr Σ_x/N)I]⁻¹ x_q:
the context's empirical covariance against an inverse training covariance
with a finite-context correction. It tends to W^µ x_q only as N → ∞, so the
converged loss is non-zero at finite context length.

**A conservation law.** Each p_α² − q_α² is constant, from the loss's
invariance under p → cp, q → q/c.

**What could have come out otherwise.** Within its assumptions the
derivation is exact. What could have failed is its match to simulated
training, which is close (Figs. 1–3A), though the simulations start from
the aligned weights the derivation assumes.

## What this does not say

- **That the alignment is reached.** It is assumed at initialisation and
  throughout. Whether misaligned starts align, and on what timescale
  against the τ_α, is not analysed.
- **That the null blocks stay at zero for a finite set of tasks.** Shown
  in expectation over the task distribution, and by simulation.
- **That it describes softmax or deep transformers.** The evidence offered
  for non-linear models is dips in effective rank and early stabilisation
  of a parameter subspace that coincide in time with in-context learning's
  emergence, with no seeds, error bars, controls or stated criterion for
  emergence.
- **That grokking is delayed subspace stabilisation.** One grokking model,
  a coincidence in time, no intervention.
- **That the trained layer does plain gradient descent in context.** With
  isotropic inputs the fixed point is one gradient step up to scale; with
  anisotropic inputs it is a step preconditioned by the inverse training
  covariance.

## Connections

- **Extends [THEORY-186](THEORY-186.md).** Saxe et al.'s two-layer linear network learns the
  singular modes of its input–output correlations one at a time, in order
  of strength, because the map is a product of layers. Here the product is
  of the two attention factors, and the order is set by the input
  covariance's spectrum, without depth.
- **[THEORY-169](THEORY-169.md)** says linear attention is one gradient step of an inner
  linear model, from the exact constructions. This account is the outer
  training that produces that inner learner, and sharpens "a single
  trained layer finds these weights up to scale": up to scale for
  isotropic inputs, preconditioned otherwise ([NOTE-658](../notes.d/NOTE-658.md)).
- **[THEORY-212](THEORY-212.md).** Conservation of the two factors' relative scale under
  gradient flow is the same symmetry, rescaling one factor against the
  other, that sets the learning regime there.
- **[QUESTION-039](../questions.d/QUESTION-039.md).** Another mechanism that sets when a structure is
  acquired: here, the input spectrum through the attention product.
  [THEORY-229](THEORY-229.md) is the self-supervised instance of the same pattern.
- **[CLAIM-118](../claims.d/CLAIM-118.md)** grounds on this paper.
