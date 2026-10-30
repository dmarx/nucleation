---
number: 678
status: Proposed
formerly:
- THEORY-tmpy5vxl
promote_when: >-
  A per-subject presence rate, scored by a detector or by human raters for
  each named subject, on two-subject prompts, relating whether a subject
  appears to whether its token held some region of the early
  cross-attention map, and the same rate before and after the correction.
  Promoted if missing subjects are the ones whose tokens won no region and
  the correction raises presence; refuted if presence is unrelated to early
  attention or the correction leaves it unchanged. CLIP similarity between
  image and prompt cannot settle it, since it rewards hybrid objects, and
  neither can a preference study that asks which set of images matches the
  prompt best.
title: "In Stable Diffusion, a subject named in a two-subject prompt is left out of the image when its token governs no region of the cross-attention map early in sampling, and raising that token's smoothed peak attention during the first half of sampling, by gradient steps on the latent with no retraining, brings the subject back; that this also fixes attribute binding is argued, not measured by the paper"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    The sixteenth status review (ADR-058), at the status review's ruling
    (the owner delegated these rulings): CLAIM-321 cites this reading
    only as an instance of a conjunction failing by omission and does
    not say what causes the failures, so the edge moves from supports to
    corroborates. The reading is unchanged.
tags:
- compositionality
date: '2026-10-16'
source:
- LIT-806
- LIT-798
summary: >-
  Chefer, Alaluf, Vinker, Wolf & Cohen-Or (2023), [LIT-806](../literature.d/LIT-806.md), read in [NOTE-639](../notes.d/NOTE-639.md),
  with T2I-CompBench++ ([LIT-798](../literature.d/LIT-798.md), [NOTE-610](../notes.d/NOTE-610.md)) for the binding measurement the
  paper lacks. Evidence is on 276 templated two-subject prompts by CLIP
  image–text similarity, BLIP-caption similarity and a 65-person preference
  study (77–91% preferred it); no neglect rate is reported, before or
  after. [NOTE-639](../notes.d/NOTE-639.md) filed no THEORY, because the paper's method is
  machine-learning practice; the account of why subjects go missing is a
  finding about the model and is filed here as Proposed.
corroborates:
- CLAIM-321
---
<!-- inactive-ok-file: CLAIM-321 — Proposed; the record's own claim this reading corroborates, named in Connections -->

# THEORY-678: In Stable Diffusion, a subject named in a two-subject prompt is left out of the image when its token governs no region of the cross-attention map early in sampling, and raising that token's smoothed peak attention during the first half of sampling, by gradient steps on the latent with no retraining, brings the subject back; that this also fixes attribute binding is argued, not measured by the paper

## Source

Hila Chefer, Yuval Alaluf, Yael Vinker, Lior Wolf and Daniel Cohen-Or
(2023), "Attend-and-Excite: Attention-Based Semantic Guidance for
Text-to-Image Diffusion Models", SIGGRAPH 2023, [LIT-806](../literature.d/LIT-806.md), read in [NOTE-639](../notes.d/NOTE-639.md).
The independent binding measurement is from T2I-CompBench++ ([LIT-798](../literature.d/LIT-798.md),
[NOTE-610](../notes.d/NOTE-610.md)).

## What was actually shown

**The failure.** "Catastrophic neglect": one of the subjects a prompt
names is absent (Figs. 2, 5). The paper shows it on Stable Diffusion v1.4
and reports no rate.

**The account.** The 16×16 cross-attention maps, averaged over layers and
heads, are per-patch distributions over tokens, so one token can win
everywhere and another nowhere. Layout is fixed in the early steps. A
subject appears only if its token governs some patch early on.

**The intervention.** At each step t ≤ 25 of 50, the loss is
L = max over subjects of (1 − max of G(A_t^s)), with G a 3×3 Gaussian
(σ = 0.5) and the start-of-text token dropped; the latent takes a gradient
step against L, with refinement to set thresholds at steps 0, 10 and 20. No
weights change.

**Results (276 prompts; Fig. 8, Tables 1–2).** CLIP image–text similarity
is higher than every baseline on all three subsets, and minimum-object
similarity at least 7% above Stable Diffusion and StructureDiffusion.
Caption similarity is 0.806, 0.830 and 0.811. In the preference study
90.70%, 77.64% and 77.16% chose it.

**Ablations (Appendix B).** Without smoothing, the loss is met by a
fragment and the subject does not appear. Without refinement, neglected
subjects stay missing. Updating after step 25 adds artefacts without
semantic gain.

**Binding, measured elsewhere.** Re-implemented on Stable Diffusion v2,
the method raises BLIP-VQA colour binding from 0.5065 to 0.6400 and
texture binding from 0.4922 to 0.5963, with little change in shape binding
or relations ([LIT-798](../literature.d/LIT-798.md), Table XIII).

**What could have come out otherwise.** Raising a token's attention could
have produced a fragment or nothing; without the smoothing it does exactly
that.

## What this does not say

- **How often neglect happens, or how much is removed.** Every quantitative
  score in the paper is of overall prompt similarity or preference, not of
  per-subject presence.
- **That attention causes the subject.** The account is supported by an
  intervention that works, not by a test that attention predicts which
  subject goes missing.
- **That presence fixes binding.** The paper argues that the causal text
  encoder has already mixed the attribute into the subject's token, and
  shows figures. The T2I-CompBench measurement shows colour and texture
  binding improving, not why.
- **Anything about relations, negation or many subjects.** Prompts are
  templated conjunctions of two subjects with colours; relations are out of
  scope and do not improve.
- **That the cross-attention maps explain the image** in general. The
  paper's claim that they become faithful after correction is qualitative.

## Connections

- **Benchmarks of composition** ([THEORY-522](THEORY-522.md)) place this method among
  the binding-specific baselines; in T2I-CompBench it helps colour and
  texture binding most.
- **Composable Diffusion** ([THEORY-405](THEORY-405.md), from [LIT-770](../literature.d/LIT-770.md)). This paper
  reports, qualitatively, that its conjunction fuses the two subjects into
  one object.
- [CLAIM-321](../claims.d/CLAIM-321.md) cites this paper for a conjunction failing by omission of a
  conjunct, before any misbinding. That reading is [NOTE-639](../notes.d/NOTE-639.md)'s.
- Classifier-free guidance ([LIT-839](../literature.d/LIT-839.md)) is on throughout at scale 7.5.

## Note of 2026-10-29: what holds it back

No per-subject presence rate is in the record. The paper scores CLIP and
caption similarity and a preference study, which its promote_when rules
out, and T2I-CompBench++ (LIT-798) measures binding, not presence.
GenEval's detector scores two-object presence (THEORY-522), but not for
this method and not against early attention. Narrowing to what was
measured would leave only the method's scores, which are machine-learning
practice and belong to the anthology (NOTE-639).
