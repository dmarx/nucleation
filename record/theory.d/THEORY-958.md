---
number: 958
status: Active
formerly:
- THEORY-tmpt2q0g
title: 'When each view takes pixels directly (a crop of a larger canvas, or the whole image under a region mask), MultiDiffusion''s step, the least-squares reconciliation of several denoisers'' proposed next states, is their per-pixel average weighted by the weights of the views covering that pixel; this is exact for 0/1 weights, the only ones the paper uses, while for other weights the loss as printed weights by their squares; with a deterministic update affine in the noise prediction it is one step taken with the per-pixel weighted mean of the views'' noise predictions; and the guarantee that each view then follows the reference model''s diffusion path holds only if the loss is zero at every step, which overlapping proposals that disagree do not reach'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-1158. The fusion step is the paper's Eq. 5,
    and the guarantee its Proposition 3.1 with the proof of its proceedings
    Appendix A. Both are re-derived below step by step and the fusion
    checked numerically, which meets the condition for Active under ADR-047
    v2. The correction for non-binary weights, the equivalence with
    averaging noise predictions and the scope of the proposition are the
    record's.
tags:
- compositionality
- probabilistic-modeling
date: '2026-10-25'
source:
- LIT-1522
answers:
- QUESTION-273
summary: >-
  Bar-Tal, Yariv, Lipman and Dekel (2023), [LIT-1522](../literature.d/LIT-1522.md), read in
  [NOTE-1158](../notes.d/NOTE-1158.md). The fusion is an average, not a sum: where views overlap
  each takes a convex share of the pixel's update. The paper's closed form
  is the minimizer of its loss only for 0/1 weights. Its distributional
  guarantee is conditional on zero loss and, in the proceedings version,
  on strictly positive weights, so it covers neither the overlaps as they
  behave nor masked region generation. Nothing here says what distribution
  the fused sampler targets.
---
<!-- inactive-ok-file: CLAIM-336 — Proposed; the operator model whose influence slot this instantiates, open -->

# THEORY-958: When each view takes pixels directly (a crop of a larger canvas, or the whole image under a region mask), MultiDiffusion's step, the least-squares reconciliation of several denoisers' proposed next states, is their per-pixel average weighted by the weights of the views covering that pixel; this is exact for 0/1 weights, the only ones the paper uses, while for other weights the loss as printed weights by their squares; with a deterministic update affine in the noise prediction it is one step taken with the per-pixel weighted mean of the views' noise predictions; and the guarantee that each view then follows the reference model's diffusion path holds only if the loss is zero at every step, which overlapping proposals that disagree do not reach

## Source

Bar-Tal, Yariv, Lipman and Dekel (2023), "MultiDiffusion: Fusing
Diffusion Paths for Controlled Image Generation", ICML 2023, PMLR 202,
[LIT-1522](../literature.d/LIT-1522.md), read in full in [NOTE-1158](../notes.d/NOTE-1158.md) from arXiv v1 and the
proceedings PDF. The step is the paper's Eqs. 3–5, the guarantee its
Proposition 3.1. The derivations below are the record's.

## What was actually shown

**Setting.** A frozen model Φ proposes the next state of an image,
I_{t−1} = Φ(I_t | y). Views Fᵢ map the canvas J to the model's image space;
here Fᵢ samples pixels, so Fᵢ(J)_p = J_{πᵢ(p)} for an injective πᵢ (a crop),
or Fᵢ = identity. Write Pᵢ = Φ(Fᵢ(J_t) | yᵢ) for view i's proposal, and
Fᵢ⁻¹ for placing a view-sized array back on the canvas, zero elsewhere.
Weights Wᵢ ≥ 0 are per pixel and shared across channels.

**The step as printed (Eq. 4).** Ψ(J_t) = argmin_J Σᵢ ‖Wᵢ ⊗ (Fᵢ(J) − Pᵢ)‖².
Because each Fᵢ samples pixels, the objective separates by canvas pixel q
(and channel):

  f_q(J_q) = Σ_{i covering q} wᵢ(q)² (J_q − Pᵢ(q))²,

writing wᵢ(q) and Pᵢ(q) for view i's weight and proposal at the position
that lands on q. f_q is a convex parabola, and f_q′ = 0 gives

  J_q = Σᵢ wᵢ(q)² Pᵢ(q) / Σᵢ wᵢ(q)².

**Against the paper's Eq. 5.** Eq. 5 is
Ψ = Σᵢ [Fᵢ⁻¹(Wᵢ) / Σⱼ Fⱼ⁻¹(Wⱼ)] ⊗ Fᵢ⁻¹(Pᵢ), weights to the first power.
The two agree when every wᵢ(q) ∈ {0, 1}, since then w² = w: the panorama
(Wᵢ = 1) and region generation (Wᵢ = Mᵢ, binary masks), which are all the
paper's applications. They also agree if the weight multiplies the squared
residual, Σᵢ Wᵢ ⊗ (Fᵢ(J) − Pᵢ)². For general weights in the printed loss
they differ. Checked numerically on a one-dimensional canvas of 20 pixels
with crops of 8 at stride 3, against a generic least-squares solve: the
difference from Eq. 5 is at machine precision (2 × 10⁻¹⁶) for unit and for
random binary weights; for random positive weights Eq. 5 is off by up to
0.23, and the W²-weighted average is exact. A pixel whose total weight is
zero is undetermined.

**Average, not sum.** Each covered pixel takes a convex combination of the
proposals of the views covering it, with shares wᵢ/Σⱼwⱼ that sum to one.
k overlapping views each get 1/k of the update, and a pixel in one view
takes that view's proposal.

**As an average of noise predictions.** Suppose each Φ call is a
deterministic step affine in its noise prediction, Pᵢ = a_t Fᵢ(J_t) + b_t εᵢ,
with the same a_t, b_t for every view (DDIM with η = 0, and classifier-free
guidance folded into εᵢ). Every view covering q reads the same J_t(q). So
J_{t−1}(q) = Σᵢ w̄ᵢ (a_t J_t(q) + b_t εᵢ(q)) = a_t J_t(q) + b_t Σᵢ w̄ᵢ εᵢ(q),
with w̄ᵢ the normalized shares: one step with the per-pixel weighted mean
noise prediction (checked numerically, difference 2 × 10⁻¹⁶). With region
prompts, binary masks and guidance scale g on a shared unconditional
prediction, that mean is ε_∅ + g Σᵢ Mᵢ(εᵢ − ε_∅) / Σᵢ Mᵢ.

**The guarantee (Proposition 3.1).** Suppose Fᵢ(J_T) ∼ P_I for every i
and the minimum of the loss is zero at every step. A sum of squares is
zero only if each term is, so Wᵢ ⊗ (Fᵢ(J_{t−1}) − Pᵢ) = 0. With every
weight strictly positive, Fᵢ(J_{t−1}) = Φ(Fᵢ(J_t) | yᵢ) for all t. By
induction, Fᵢ(J_t) is a chain of Φ started from P_I, so Fᵢ(J_0) has the
law of the reference model's samples. That is the paper's proof, and it
is correct.

What could have failed: the closed form could have needed an iterative
solver, as a general Fᵢ (a warp, a downsampling) would. For pixel
sampling it does not. The proposition could have claimed more than its
hypothesis gives; it does not.

## What this does not say

- **Not that the sampler draws from any particular distribution.** The
  proposition's hypothesis is exact agreement of overlapping proposals at
  every step. The method exists because "each crop might pull to a
  different denoising direction", and the paper never measures the
  residual. With strictly positive weights required, it does not cover
  masked region generation, where weights are zero outside each mask.
  It concerns each view's marginal, not the canvas jointly.
- **Not a product or conjunction of the views' conditions.** [THEORY-405](THEORY-405.md)'s
  composition sums guidance terms, each concept acting everywhere, and
  [CLAIM-123](../claims.d/CLAIM-123.md) says when such a sum is the score of a composed condition.
  This step averages, by place. No probabilistic reading of the average is
  offered, and [THEORY-611](THEORY-611.md)'s point that guided fields need not be
  conservative applies to each term.
- **Not anything about stochastic steps.** If each view injects its own
  noise, averaging shrinks it on overlaps, and the paper does not say
  how its implementation shares noise.
- **Not that the weights measure influence over the image.** A view's
  share of a pixel's update at one step is exact. Its effect on the final
  image passes through every later step, where the other views see the
  blended state.

## Connections

- **[CLAIM-123](../claims.d/CLAIM-123.md)'s note of 2026-10-25.** A45's combination
  ε_∅ + g·Σwᵢ Mᵢ (εᵢ − ε_∅) / max(1, Σwᵢ Mᵢ) is, with unit weights and
  coverage of at least one, this step's noise-prediction form. A45
  re-derived MultiDiffusion's region-based step, uncited, and added
  per-perspective weights and a dilution rule below total weight one.
- **[QUESTION-273](../questions.d/QUESTION-273.md): answers in part.** For the "locations" form of the
  owner's third mechanism under this fusion, the nominal resource maps
  exactly onto a per-step, per-pixel convex weight. That settles, for one
  step, how nominal allocation enters the update. It does not settle the
  question's counterfactual influence over a trajectory, or whether other
  mechanisms reduce to the same weights.
- **[LIT-1529](../literature.d/LIT-1529.md) ([THEORY-955](THEORY-955.md)).** LoRA Composite is this step's
  noise-prediction form with every mask full and LoRA-modified models in
  place of prompts.
- **[CLAIM-336](../claims.d/CLAIM-336.md)'s note of 2026-10-25.** Its "mask and weight as allocated
  influence" is this step's Wᵢ.
