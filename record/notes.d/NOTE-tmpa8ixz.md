---
status: Read
paper: LIT-tmp03agp
title: 'Bar-Tal, Yariv, Lipman and Dekel — MultiDiffusion'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Read in full from two lawful copies: arXiv v1 (2302.08113, 16 February
    2023) and the PMLR proceedings PDF (ICML 2023, PMLR 202, bar-tal23a),
    text extracted with pdftotext and compared word by word. The method
    pages (Eqs. 3–7, Proposition 3.1) and the appendix with the proof and
    the crop count were also rendered as images and read from them,
    because extraction garbled the displayed equations. Read: abstract,
    introduction, related work, §3 (method, closed form, Proposition 3.1),
    §4 (panorama, region-based generation, bootstrapping), §5 (results,
    Tables 1–2), §6, and appendices A–D of the proceedings version (A, the
    proof, and D, a societal-impact paragraph, are not in arXiv v1).
    Figures were read from their captions and the text. The proceedings
    version corrects one typo in the derivation (F_i(J_t) to F_i(J_{t−1}))
    and adds strictly positive weights to Proposition 3.1; the equations,
    tables and results are otherwise the same. The closed form and the
    proposition were re-derived here and checked numerically
    (THEORY-tmpt2q0g).
date: '2026-10-25'
summary: >-
  A training-free sampler that runs one pre-trained diffusion model on
  several crops or masked prompts of one canvas and, at every step,
  replaces their disagreeing proposals with the least-squares
  reconciliation, which for pixel-sampling maps is a per-pixel weighted
  average. It makes seamless panoramas (crop FID 10.3 against 18.4 and
  45.5 for outpainting baselines) and follows rough region layouts (COCO
  IoU 0.26 against 0.16–0.17), most of the layout gain coming from an
  early masked bootstrapping phase. Its guarantee that each crop follows
  the reference model's path holds only at zero loss, which disagreeing
  overlaps do not reach.
---
<!-- inactive-ok-file: CLAIM-336 CLAIM-297 CLAIM-279 CLAIM-321 THEORY-937 — Proposed; the operator model, the claims and the router reading this reading bears on, cited as open, nothing here rests on their being settled -->

# NOTE-tmpa8ixz: Bar-Tal, Yariv, Lipman and Dekel — MultiDiffusion

## Contribution

It defines a new sampler on top of a frozen text-to-image diffusion model
without training. The model is applied to several views of one canvas
(overlapping crops of a panorama, or the whole image under several
region prompts), each view proposes its own next denoising state, and the
sampler takes the canvas that agrees with all proposals as closely as
possible in the least-squares sense. For the paper's maps that is a
per-pixel weighted average, so one network call per view per step, and
no optimization loop. It shows panoramas nine times wider than the
training resolution and generation from rough region masks with one
mechanism.

## Key insight

Spatial control can be had by fusing several runs of one denoiser over
one shared state, each run with authority over part of the canvas,
rather than by training a model to take the control as input. At every
step each pixel follows "the (averaged) directions associated with the
regions M_i containing it". Disagreement between overlapping proposals is
not resolved by any rule other than averaging. Coherence across the
canvas comes from every view seeing, at the next step, a state that
already blends its neighbours' proposals.

## Assumptions

- A pre-trained reference model Φ: I × Y → I that maps a noisy image and
  a condition to the next, less noisy image, I_{t−1} = Φ(I_t | y). The
  fused objects are next states, not noise predictions or scores.
- Maps F_i: J → I from the target canvas to the model's image space and
  λ_i: Z → Y on conditions, "application depended". The closed form
  needs F_i to "consist of direct pixel samples", crops or the identity.
- Per-pixel weights W_i ∈ ℝ^{H×W}, nonnegative (strictly positive for
  Proposition 3.1 in the proceedings version), shared across the latent's
  channels.
- Proposition 3.1 also needs an initial distribution P_J with
  F_i(J_T) ∼ P_I for every i, which i.i.d. Gaussian noise on the canvas
  satisfies, and zero loss at every step.
- All experiments: Stable Diffusion 2 through Hugging Face Diffusers, in
  the 64 × 64 × 4 latent space, decoded at 8×.

## Key results

- **The fusion step (Eqs. 3–5).** Ψ(J_t | z) = argmin_J
  Σᵢ ‖Wᵢ ⊗ [Fᵢ(J) − Φ(Iᵢ_t | yᵢ)]‖² with Iᵢ_t = Fᵢ(J_t). For
  pixel-sampling maps the paper gives the minimizer as
  Ψ = Σᵢ [Fᵢ⁻¹(Wᵢ) / Σⱼ Fⱼ⁻¹(Wⱼ)] ⊗ Fᵢ⁻¹(Φ(Iᵢ_t | yᵢ)) (Eq. 5): "each pixel
  of the minimizer J is a weighted average of all its diffusion sample
  updates". Re-derived in THEORY-tmpt2q0g, with one correction: with the
  weight inside the norm, as printed in both versions, the per-pixel
  minimizer weights by Wᵢ², so Eq. 5 is the minimizer for 0/1 weights
  (every application in the paper) and not for general weights.
- **Proposition 3.1.** If F_i(J_T) ∼ P_I and the loss is minimized to
  zero at every step, then each F_i(J_t) is a diffusion path of Φ, and
  each F_i(J_0) "distributed identically to samples from the reference
  diffusion model Φ". The proof (proceedings Appendix A) is two lines and
  correct. Its hypothesis is what the method exists to avoid needing:
  "while each crop might pull to a different denoising direction, our
  framework yields a unified denoising step".
- **Panorama (§4.1, §5.1, Table 1).** 512 × 4608 panoramas, crops of
  64 × 64 latents with stride 8, Wᵢ = 1. FID of random 512 × 512 crops
  against N = 2000 reference samples of Φ per prompt, 8 prompts, mean ±
  standard deviation:

  | | FID ↓ | CLIP-score ↑ | CLIP-aesthetic ↑ |
  |---|---|---|---|
  | Stable Diffusion (fresh reference samples) | 6.05 ± 3.1 | 0.27 | 6.36 |
  | Stable Inpainting (SI) | 45.5 ± 14.5 | 0.26 | 5.76 |
  | Blended Latent Diffusion (BLD) | 18.4 ± 7.4 | 0.27 | 6.02 |
  | MultiDiffusion | 10.3 ± 4.8 | 0.27 | 6.36 |

  Both baselines extrapolate outward from a central image. The authors:
  "our method outperforms the existing baselines in all metrics". On
  CLIP-score it ties BLD at the precision given.
- **Region-based generation (§4.2, §5.2, Table 2).** Fᵢ = identity,
  Wᵢ = Mᵢ, one prompt per region, the full caption for the background.
  1K COCO validation images with two to four foreground objects, people
  excluded, masks of at least 5% of the image; IoU of an off-the-shelf
  segmenter's output with the ground-truth layout: real images
  0.43 ± 0.09, SI 0.16 ± 0.10, BLD 0.17 ± 0.11, MultiDiffusion without
  bootstrapping 0.18 ± 0.10, with it 0.26 ± 0.12. Make-A-Scene and
  SpaText, trained for the task, are compared only on their published
  examples, since "these models are not publicly available".
- **Bootstrapping (Eq. 9).** For the first 20% of steps (T_init = 800)
  each region's view replaces everything outside its mask with a noised
  random constant-colour image, because "the layout is being determined
  early on in the diffusion process". It accounts for most of the layout
  gain: 0.18 → 0.26.
- **Cost.** T·n/b network calls for n views in batches of b
  (Appendix C.1), so the "without introducing computational overhead" of
  the introduction means no optimization beyond the calls. The printed
  crop count n = ((H′ − 64)/step)·((W′ − 64)/step) is zero for a
  one-row panorama, so each factor lacks a + 1; the 512 × 4608 panorama
  has 65 crops.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For pixel-sampling maps the least-squares fusion of the views' proposals is a per-pixel weighted average (Eq. 5) | strong for 0/1 weights; as printed, wrong for other weights (the minimizer weights by W²) | §3 derivation; re-derived and checked numerically in THEORY-tmpt2q0g |
| C2 | At zero loss with positive weights every view follows a diffusion path of the reference model and its final crop is distributed as the model's samples | strong as a conditional | Proposition 3.1 and Appendix A; the condition is not shown to hold, or measured, in any experiment |
| C3 | Fused panoramas are closer to the reference model's crop distribution than outpainting baselines, at equal text alignment | moderate | Table 1: 8 prompts, N = 2000, FID with spread across prompts; no significance test |
| C4 | Region prompts with rough masks yield layouts closer to the target than SI or BLD | moderate | Table 2, 1K COCO images, one segmenter; the fusion alone gains 0.01–0.02 IoU, bootstrapping 0.08 |
| C5 | Quality matches methods trained for region-to-image generation | weak | qualitative comparison on those methods' own published examples |
| C6 | The method "heavily relies on the generative prior of the reference diffusion model": a model biased to add a waterfall to every crop puts one in each crop of a vertical panorama | moderate, as a stated limitation | Fig. 9 |

## Method

Algorithm 1: initialize J_T on the canvas; at each step compute
Iᵢ_{t−1} = Φ(Fᵢ(J_t), yᵢ) for every view (in a batch), then set J_{t−1} by
Eq. 5. The general form proposed for future work (Eq. 10) adds a further
cost L′ and hard constraints C to the same least-squares objective.

## Concepts

- **Reference model Φ**: the frozen diffusion model, read as a map from
  a noisy image and condition to the next image.
- **MultiDiffuser Ψ**: the new step on the canvas, defined as the
  minimizer of the FTD loss.
- **FTD ("Follow-the-Diffusion-Paths") loss**: the weighted squared
  distance between each view of the candidate canvas and that view's
  proposal.
- **Bootstrapping**: a time-dependent view map that, early in sampling,
  shows each region's denoiser only its own region on a plain
  background.

## Connections

It builds on Stable Diffusion and on training-free control of a frozen
model (prompt-to-prompt, plug-and-play features, blended diffusion). It
cites classifier-free guidance (Ho and Salimans, LIT-839) among
conditional diffusion models but does not cite Composable Diffusion
(Liu et al., LIT-770), whose conjunction composes concepts everywhere
by summing guidance terms. MultiDiffusion composes prompts by place,
averaging where regions overlap. Multi-LoRA composition (LIT-tmpxsvgv,
NOTE-tmphq8v2) does not cite it.

## Bearing on the record

- **THEORY-405 and CLAIM-123.** MultiDiffusion is not THEORY-405's
  conjunction. Where k regions overlap, a pixel takes the mean of their
  proposals, each guidance term at weight 1/k, not their sum; disjoint
  regions select. If each Φ call uses classifier-free guidance at scale
  g, and the update is deterministic and affine in the noise prediction
  with a shared current state (DDIM-type), fusing next states equals one
  step with ε_∅ + g Σᵢ Mᵢ(εᵢ − ε_∅) / Σᵢ Mᵢ (re-derived in
  THEORY-tmpt2q0g). That is A45's formula in CLAIM-123's note of
  2026-10-25 with unit weights where coverage is at least 1. A45 is this
  paper's region-based step, with per-perspective weights and a dilution
  rule where total weight falls below 1, which this paper does not have.
  CLAIM-123's ratio condition does not apply to an average, and the
  paper offers no probabilistic reading of the fused step.
- **THEORY-611.** Each view's guided field is in general the gradient of
  no density, and a spatially masked combination adds a second source:
  across a region boundary the Jacobian of Σᵢ Mᵢ ⊙ sᵢ is symmetric only if
  Σᵢ (Mᵢ(p) − Mᵢ(q)) ∂sᵢ,p/∂x_q vanishes, which it does not in general when
  the models couple pixels across the boundary (the record's one-line
  argument, not the paper's). Proposition 3.1 is the paper's only
  distributional statement, and it is conditional on zero loss.
- **QUESTION-tmpu6zq7.** This is the owner's third mechanism in its
  "locations" form, built and published: one population of views acting
  on one shared state, each with jurisdiction over a set of pixels. Under
  this fusion the nominal resource, a view's weight at a pixel, is
  exactly its convex share of that pixel's update at that step, so per
  step the mechanism reduces to a vector of per-pixel influence weights.
  Over the trajectory it does not: each view's next proposal is computed
  from a state its neighbours have already shaped, and Table 2's
  bootstrapping result shows that the same masks used differently in the
  first 20% of steps change the outcome (IoU 0.18 → 0.26). The paper
  measures no per-view counterfactual influence.
- **CASE-tmpjmerx.** Its fixed-allocation arm (authorized proposals
  combined, one scheduler step) is this paper's fusion with LoRA
  operators in place of prompts. Neither this paper nor LIT-tmpxsvgv
  learns or audits the weights; the case's governed and routed arms add
  exactly that.
- **CLAIM-336's note of 2026-10-25.** In A45's terms this paper is "a
  population with different interpretations of one shared operator":
  one network, many frames (prompts), with masks as allocated influence.
  The LoRA paper is the other side of A45's distinction.

ML method; it carries no instruction this record holds. Flagged
anthology-candidate on the LIT.

## Limitations

- **Eq. 5 and the printed loss disagree for non-binary weights** (C1).
  Immaterial to the paper's experiments, which use 0/1 weights.
- **Proposition 3.1 does not describe the method as run.** It needs zero
  loss at every step, which overlapping views reach only if their
  proposals agree exactly on shared pixels, and the paper never measures
  the residual. The proceedings version requires strictly positive
  weights, so the proposition does not cover masked region generation at
  all. It speaks of each crop's marginal, not of the joint distribution
  of the canvas.
- **Stochastic steps are not discussed.** If each view's Φ draws its own
  noise, averaging k equal-weight draws shrinks the injected noise's
  standard deviation by √k on the overlap. The paper does not say how
  noise is shared.
- **Evaluation is thin for the layout claim.** One segmenter, one IoU,
  spreads without saying over what, no significance tests, and the
  comparison with trained layout models is qualitative.
- **"All metrics"** overstates Table 1, where CLIP-score ties BLD.
- **Pixels covered by no positive weight** are undetermined by Eq. 5.
  The paper avoids them by covering the canvas (crops) or by a background
  region.

## Open questions

- How large is the fusion residual, the FTD loss at its minimum, along
  real trajectories, and does it predict seams or failures? A measured
  residual would say how far Proposition 3.1 is from the method.
- What distribution does the fused sampler target, if any? A
  characterization would say whether region fusion composes prompts in
  the sense of CLAIM-123 or only averages fields.
- Does a view's counterfactual influence on the final image track its
  nominal weight? Removing one view at a time and measuring the change
  would answer it for this mechanism (QUESTION-tmpu6zq7's measure).
