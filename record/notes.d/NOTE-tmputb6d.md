---
status: Read
paper: 'LIT-tmpbjx8a'
title: 'Attend-and-Excite'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v2 (31 May 2023, 24 pages, the SIGGRAPH 2023 version,
    text extracted with pdftotext): Sections 1–7 in full with Algorithm 1
    and Tables 1–2; Appendix A (implementation, token selection, runtime,
    evaluation details) and Appendix B (ablations) read; Appendix C.1
    (comparison with Prompt-to-Prompt) read in part; C.2–C.4 skimmed for
    their tables (Tables 4–6); the qualitative figure pages (Figs. 13–18)
    skimmed from their captions. The images were not inspected, so
    statements about what the figures show are the authors'.
date: '2026-10-09'
summary: >-
  Identifies catastrophic neglect in Stable Diffusion, where a named
  subject never appears because no image patch attends to its token, and
  corrects it at inference by gradient steps on the latent that raise the
  smoothed peak attention of the most neglected subject token during the
  early steps. Measured gains are in CLIP and caption similarity and
  human preference on two-subject prompts; attribute binding improves
  only in the figures, and relations are not addressed.
---

<!-- inactive-ok-file: CLAIM-tmpzkhdr — Proposed; named as the manuscript claim this reading bears on -->

# NOTE-tmputb6d: Attend-and-Excite

## Contribution

It names a failure of text-to-image diffusion models, catastrophic neglect
(a subject in the prompt is not generated), and shows it can be corrected
during sampling with no training, by steering the latent so that every
subject token wins at least one region of the cross-attention map. It
argues, and illustrates, that this also improves attribute binding. It
introduces the general idea of "generative semantic nursing": correcting a
pretrained generator's latent on the fly against a loss defined on its own
internal signals.

## Key insight

A subject appears in the image only if its token governs some patch of the
cross-attention map early in sampling. The attention map is a per-patch
distribution over tokens, so nothing stops one token from dominating
everywhere and another from dominating nowhere. Make the worst-served
subject token's peak attention high, over a small neighbourhood rather than
a single patch, and the object follows.

## Assumptions

- A latent diffusion model whose text conditioning enters by
  cross-attention (Stable Diffusion v1.4, CLIP ViT-L/14 text encoder,
  classifier-free guidance scale 7.5, 50 steps).
- The 16×16 cross-attention maps, averaged over layers and heads, carry
  the subject's layout; spatial layout is fixed in the early steps, so
  updates stop after step 25.
- The subject tokens are given (nouns, chosen by the user or a
  part-of-speech tagger); a multi-token word is represented by its
  dominant token, found by hand.
- Attribute binding is assumed to follow from subject presence because the
  causal text encoder has already mixed the attribute into the subject's
  embedding.

## Key results

- **Loss and update** (Eqs. 2–3, Algorithm 1). L = max over s ∈ S of
  (1 − max of G(A_t^s)), G a 3×3 Gaussian with σ = 0.5, A_t the attention
  re-normalised after dropping the start-of-text token; z_t' = z_t −
  α_t∇L, α_t from 20 decaying to 10; iterative refinement to thresholds
  0.05, 0.5 and 0.8 at steps 0, 10 and 20, at most 20 updates.
- **CLIP image–text similarity** (Fig. 8). Higher than every baseline on
  all three subsets, full-prompt and minimum-object; on minimum-object
  similarity at least 7% above Stable Diffusion and StructureDiffusion.
  Composable Diffusion comes closest on some subsets, which the authors
  attribute to its fused hybrid objects scoring well with CLIP.
- **Caption similarity** (Table 1). CLIP similarity between prompt and
  BLIP caption: 0.806, 0.830, 0.811 on the three subsets, at least 4.7%
  above each baseline; Composable Diffusion is lowest (0.692 on
  animal–animal).
- **Human preference** (Table 2). 65 respondents, 10 prompts per subset, 4
  seeds: 90.70%, 77.64%, 77.16% chose it; the lowest single prompt still
  59.09%.
- **Ablations** (Appendix B). Without smoothing, the loss is met by a
  fragment and the subject does not appear; without iterative refinement,
  neglected subjects stay missing; updating after step 25 adds artefacts
  without semantic gain.
- **Cost** (Appendix A.3). About 9.7 s per image without refinement and
  15.4 s with it, against 5.6 s for Stable Diffusion, on an A100.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Stable Diffusion frequently fails to generate one of two named subjects | moderate | Figs. 2, 5; the paper reports no neglect rate |
| C2 | Raising the smoothed peak attention of the most neglected subject token mitigates neglect | moderate | Fig. 8, Tables 1–2 on 276 two-subject prompts |
| C3 | Mitigating neglect also improves attribute binding | weak | figures only; no binding accuracy is measured |
| C4 | After the correction, cross-attention maps become faithful explanations of where each subject is | weak | Fig. 4 and Appendix B, qualitative |
| C5 | Gaussian smoothing, iterative refinement and stopping at step 25 each help | weak | qualitative ablation, Figs. 10–12 |

## Method

At each denoising step t ≤ 25: run the UNet on z_t, take the averaged
16×16 cross-attention maps, drop the start-of-text token and re-normalise,
smooth each subject token's map, compute L, take a gradient step on z_t,
and denoise from the updated latent. At three set steps, repeat until each
subject token's smoothed peak attention exceeds a threshold. No weights
change.

## Concepts

- **catastrophic neglect**: one or more subjects of the prompt absent from
  the generated image.
- **incorrect attribute binding**: an attribute applied to the wrong
  subject, or to none.
- **generative semantic nursing (GSN)**: shifting a pretrained
  generator's latent during sampling so that it better reflects the
  prompt, against a loss on the model's own signals.
- **minimum object similarity**: the smaller of the CLIP similarities
  between the image and each single-subject sub-prompt, averaged over
  seeds and prompts.

## Connections

It compares against Composable Diffusion (LIT-770), whose
conjunction operator it reports fuses the two subjects into one object, and
against StructureDiffusion (Feng et al.), whose results it finds close to
plain Stable Diffusion. It builds on Prompt-to-Prompt's use of
cross-attention maps (Hertz et al.) and contrasts its own method, which
moves the latent, with Prompt-to-Prompt's attention re-weighting, which
cannot create a subject that has no location yet. Classifier-free guidance
(LIT-tmpxlxil) is on throughout, at scale 7.5, and the authors describe
their method as strengthening the text conditioning in the same spirit.
Its benchmark templates (12 animals, 12 objects, 11 colours) are the
"Attn-Exct" set that T2I-CompBench++ lists among its predecessors
(LIT-tmp76md3, Table I).

## Bearing on the record

- **CLAIM-tmpzkhdr** (each condition can be met while their conjunction
  or binding fails). This paper documents the failure before binding:
  under a single text-conditioned model, a two-subject prompt often yields
  one subject. That bears on the claim as an instance of a conjunction
  failing, but by omission of a conjunct, not by misbinding met
  conditions. It is not evidence about score addition: it uses one
  conditional model and no composition of scores. Its report that
  Composable Diffusion fuses subjects is a qualitative observation
  consistent with the claim's caution about score addition.
- **What is measured and what is not.** Every quantitative result scores
  subject presence or overall prompt similarity; none scores binding.
  The binding claim rests on figures and on an argument about the text
  encoder. The independent measurement is T2I-CompBench's: re-implemented
  on Stable Diffusion v2, it raises BLIP-VQA colour binding from 0.5065
  to 0.6400 and texture binding from 0.4922 to 0.5963, with little change
  in shape binding or relations (LIT-tmp76md3, Table XIII; the
  conference version, LIT-783, reports the same re-implementation).
- The paper carries an instruction for machine-learning practice (an
  inference-time method and its settings); that is anthology material, and
  the LIT carries the `anthology-candidate` flag. No THEORY is filed.

## Limitations

- Prompts are templated conjunctions of two subjects with colour
  attributes; complex prompts are shown only qualitatively, with one CLIP
  table (Table 5).
- CLIP image–text similarity, by the authors' own account, behaves like a
  bag of words and rewards hybrid objects; the text–text metric depends on
  BLIP captions, which may omit attributes.
- The human study asks which set of four images best matches the prompt,
  across methods; it does not ask whether each subject or attribute is
  present.
- Unnatural combinations (an elephant with a sombrero) come out less
  realistic, and out-of-distribution prompts can push the latent off the
  model's distribution (Fig. 9).
- Relations and negation are not addressed.

## Open questions

- How often does neglect occur, and how much of it does the method
  remove? A per-subject presence rate from a detector or human raters,
  before and after, would answer it.
- Does subject presence cause correct binding, as the text-encoder
  argument says, or only co-occur with it? Comparing binding accuracy
  conditional on both subjects being present, with and without the
  method, would separate the two.
