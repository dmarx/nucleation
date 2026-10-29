---
number: 481
status: Active
formerly:
- THEORY-tmpaeic7
title: "Under gradient flow averaged over tasks and data, a linear-attention layer trained on in-context regression learns as a two-layer linear network from an aligned start does: when tasks share the input covariance's eigenbasis and the weights start and stay aligned with it, then in the long-context limit each input mode is learned on its own logistic curve whose timescale falls with the square of its variance, so learning is staged by the input spectrum, and the layer converges to the estimator preconditioned by the inverse input covariance; at finite context length the modes decouple exactly only when inputs are isotropic and the modes start equal, and otherwise couple at order 1/N"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/THEORY-481.yaml, batch 016,
    ADR-047). NOTE-658 had followed the source's Wishart step as stated.
    Re-deriving it from LIT-859's Appendix A.11 shows that the paper
    commutes the rotated empirical covariance Ŝ with diagonal matrices at
    (A71) and (A73), but Ŝ is not diagonal at finite N. The correct moment
    couples the modes through a 1/N term. So the per-mode logistic dynamics,
    the per-mode conservation law, and s^∞_α = ((N+1)s_α + Tr S)/N are
    exact as N → ∞, and at finite N for isotropic inputs with equal modes,
    but not in general. The title and body now say so, and the corrected
    derivation is under "The finite-context step, corrected". The status
    stays Proposed. A review for narrowing and promotion follows separately.
- version: 3
  date: '2026-10-29'
  note: >-
    Narrowed and promoted by the ninth status review (ADR-057;
    ADR-047's evidence ruling, one study read in full for a title that
    claims no more than it showed, and a checked re-derivation for the
    proof). The review found two faults in version 2's correction: the
    finite-N flow for q is not the p flow with p and q exchanged,
    since the coupling term is not symmetric, checked against the loss
    by finite differences; and Eq. 11's fixed point holds at finite N
    only for isotropic inputs with equal modes, checked by integrating
    the corrected flow, with the Wishart moment it rests on checked by
    Monte Carlo. Both are fixed in the body. The title now says the
    flow is averaged over tasks and data, names the long-context
    preconditioner, and adds the equal-mode condition. It extends
    THEORY-740, the exact two-layer solution from an aligned start,
    not THEORY-186. The old title: A linear-attention layer trained on
    in-context regression learns as a two-layer linear network does:
    when tasks share the input covariance's eigenbasis and the weights
    stay aligned with it, then in the long-context limit each input
    mode is learned on its own logistic curve whose timescale falls
    with the square of its variance, so learning is staged by the
    input spectrum, and the layer converges to a preconditioned
    estimator; at finite context length the modes decouple exactly
    only when inputs are isotropic, and otherwise couple at order 1/N.
    The promote_when asked for alignment from misaligned starts, which
    the title assumes and never claimed; it moves unchanged to
    QUESTION-tmpuk5nc, as THEORY-285's moved to QUESTION-tmpxd26n.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-10-16'
source:
- LIT-859
extends:
- THEORY-740
summary: >-
  Mainali & Teixeira (2025), [LIT-859](../literature.d/LIT-859.md), read in [NOTE-658](../notes.d/NOTE-658.md). The prediction of
  one linear-attention layer reduces to p₂ W Σ̂_x q₁ x_q, a product of two
  learned factors, so averaged gradient flow decouples into modes with
  τ_α dp_α/dt = q_α(1 − p_α q_α s^∞_α) and τ_α = (ηP s_α²)⁻¹, logistic from a
  balanced start. The fixed point is ŷ = W Σ̂_x Σ_x⁻¹ x_q as N → ∞. The paper's finite-N
  form, the one Ahn et al. and Zhang, Frei & Bartlett found, holds at
  finite N only for isotropic inputs with equal modes. The trajectory is
  new. The decoupling into independent modes is exact as N → ∞. At finite
  N it holds only for isotropic inputs with equal modes: the paper commutes
  the non-diagonal empirical covariance at (A71) and (A73), and the correct
  Wishart moment couples the modes at order 1/N. Alignment of the weights with the data's eigenbasis is assumed
  throughout, the null blocks vanish only in expectation over tasks, and
  the transfer to non-linear transformers is timing coincidences.
bears_on:
- QUESTION-039
- QUESTION-tmpuk5nc
---
<!-- inactive-ok-file: THEORY-186 — Proposed; the two-layer random-start claim, the analogue of QUESTION-tmpuk5nc, cited not leaned on -->
<!-- inactive-ok-file: CLAIM-118 THEORY-212 — Proposed; the claim that grounds on this paper and neighbouring accounts, named in Connections, not leaned on -->

# THEORY-481: Under gradient flow averaged over tasks and data, a linear-attention layer trained on in-context regression learns as a two-layer linear network from an aligned start does: when tasks share the input covariance's eigenbasis and the weights start and stay aligned with it, then in the long-context limit each input mode is learned on its own logistic curve whose timescale falls with the square of its variance, so learning is staged by the input spectrum, and the layer converges to the estimator preconditioned by the inverse input covariance; at finite context length the modes decouple exactly only when inputs are isotropic and the modes start equal, and otherwise couple at order 1/N

## Source

Mainali & Teixeira (2025), [LIT-859](../literature.d/LIT-859.md) (NeurReps workshop, arXiv v2), read in
full in [NOTE-658](../notes.d/NOTE-658.md). [NOTE-658](../notes.d/NOTE-658.md) filed no THEORY because the result concerns
training transformers and the staged learning is Saxe et al.'s pattern,
which the record then did not hold as a source. The record now holds its exact solution as [THEORY-740](THEORY-740.md), which this account
carries to attention; [THEORY-186](THEORY-186.md) holds the claim that random starts follow
it.

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

**The dynamics (Eqs. 9–13), as the paper states them.** Assuming p₂ and
q₁ stay diagonal in U, each mode obeys τ_α dp_α/dt = q_α(1 − p_α q_α s^∞_α) and the same with p and q
exchanged, with τ_α = (ηP s_α²)⁻¹ and s^∞_α = ((N+1)s_α + Tr S)/N. From a
balanced start a_α = p_α q_α is logistic, with escape time from ε about
(τ_α/2) log(1/(s^∞_α ε)). Modes of larger input variance are learned first.
The expected loss is an explicit sum over modes (Eq. 14), and the
predictions match simulation closely (Figs. 1–3A).

These equations are exact as N → ∞, where s^∞_α = s_α. At finite N they
hold for isotropic inputs with equal modes, and otherwise are an
approximation whose error the paper does not bound. See "The finite-context
step, corrected" below.

**The fixed point (Eq. 11).** The paper gives
ŷ(∞) ≈ W^µ Σ̂_x [((N+1)/N)Σ_x + (Tr Σ_x/N)I]⁻¹ x_q. It comes through the
same commutation as the dynamics, so it is exact as N → ∞, where it is
W^µ Σ̂_x Σ_x⁻¹ x_q, and at finite N for isotropic inputs with equal modes,
where the preconditioner is a scalar. For anisotropic inputs at finite N
the corrected flow settles elsewhere. Integrated numerically by the ninth
status review at N = 5 and s = (3, 1, 0.4), from an equal start of 0.05,
p_α q_α reaches 0.218, 0.522 and 0.852, against Eq. 11's 0.223, 0.481 and
0.735, at a lower loss; an isotropic control lands on Eq. 11 exactly. This
is one setting checked numerically, not a proof for every spectrum. In
every case the converged loss is non-zero at finite context length, and
the predictor tends to W^µ x_q only as N → ∞.

**A conservation law.** ‖p₂‖² − ‖q₁‖² is constant, from the loss's
invariance under p₂ → cp₂, q₁ → q₁/c. The paper also states it mode by mode,
and that holds as N → ∞ but not at finite N, where the 1/N term breaks the
per-mode symmetry.

**The finite-context step, corrected.** In the eigenbasis the reduced
predictor is ŷ = PΛŜQx̄. P and Q are diagonal (the alignment assumption),
Λ is diagonal with independent N(0, 1) entries (the tasks), and Ŝ is the
context's empirical covariance, with query x̄ ~ N(0, S). Averaged over
tasks, only the diagonal survives, so the loss is
Σ_α {p_α² E[(ŜAŜ)_αα] − 2p_α q_α s_α² + s_α}, with A = QSQ, so a_β = q_β² s_β.
For Gaussian samples, E[(ŜAŜ)_αα] = ((N+1)/N) a_α s_α² + (s_α/N) Σ_β a_β s_β.
Each mode's flow is then
τ_α dp_α/dt = q_α − p_α(((N+1)/N) s_α q_α² + (1/N) Σ_β q_β² s_β² / s_α),
with τ_α = (ηP s_α²)⁻¹, and
τ_α dq_α/dt = p_α − q_α(((N+1)/N) s_α p_α² + (1/N) Σ_β p_β² s_β), which is
not the p flow with p and q exchanged, because the coupling term
(1/N)(Σ_α p_α² s_α)(Σ_β q_β² s_β²) is not symmetric in them. The modes
couple through both sums. The paper writes (A71) "since Ŝ and q̄1 are
diagonal matrices and commute", and (A73) "all matrices in the expression
are diagonal". That turns E[ŜAŜ] into E[Ŝ²]A and replaces Σ_β a_β s_β with
a_α Tr S. The two agree only when q_β² s_β is the same for every mode, for
example with isotropic inputs and a balanced, equal start. Then
s^∞ = ((N+1)s + Tr S)/N, as the paper has it. As N → ∞ the coupling term
vanishes, the loss is Σ_α s_α(p_α q_α s_α − 1)², and every per-mode
statement above is exact with s^∞_α = s_α.

**What could have come out otherwise.** Within its assumptions the
derivation is exact as N → ∞, and at finite N for isotropic inputs. The
general finite-N step is not, as above. What could have failed is its match to simulated
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

- **Extends [THEORY-740](THEORY-740.md).** Whether random starts reach that solution is
  [THEORY-186](THEORY-186.md)'s open claim, and the same question for attention is
  [QUESTION-tmpuk5nc](../questions.d/QUESTION-tmpuk5nc.md). Saxe et al.'s two-layer linear network learns the
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
