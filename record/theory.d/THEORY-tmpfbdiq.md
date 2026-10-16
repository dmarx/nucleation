---
status: Active
title: "Open text-to-image diffusion models of 2022–2023 render a single named object almost always but fail most on relative position and next on attribute binding, by human rating and by detector checks alike; scaling the image model or continuing pretraining does not fix position, and interactions are rated near ceiling only by rubrics that ask whether an action is depicted"
version: 1
tags:
- compositionality
date: '2026-10-16'
source:
- LIT-782
- LIT-783
- LIT-798
summary: >-
  GenEval (Ghosh, Hajishirzi & Schmidt 2023, [LIT-782](../literature.d/LIT-782.md), [NOTE-593](../notes.d/NOTE-593.md)) and
  T2I-CompBench with its journal extension (Huang et al. 2023 and 2025,
  [LIT-783](../literature.d/LIT-783.md) and [LIT-798](../literature.d/LIT-798.md), [NOTE-592](../notes.d/NOTE-592.md) and [NOTE-610](../notes.d/NOTE-610.md)), two independent benchmarks
  that do not cite each other. GenEval: single object 0.97–0.98 for every
  diffusion model, position at most 0.15, binding at most 0.35. Human
  ratings in T2I-CompBench: 2D spatial 0.31–0.46, shape binding 0.51–0.70,
  interactions 0.81–0.99. Human ratings cover only six 2023-era models; the
  2024–25 generation is ranked by automatic judges validated on the older
  ones, so the ordering is not established for it.
supports:
- CLAIM-321
---
<!-- inactive-ok-file: CLAIM-013 CLAIM-321 — Proposed; the record's own claims that cite these readings, named in Connections -->
<!-- inactive-ok-file: THEORY-117 THEORY-250 THEORY-tmpy5vxl — Proposed; neighbouring accounts named in Connections and in what this does not say, nothing here rests on them -->

# THEORY-tmpfbdiq: Open text-to-image diffusion models of 2022–2023 render a single named object almost always but fail most on relative position and next on attribute binding, by human rating and by detector checks alike; scaling the image model or continuing pretraining does not fix position, and interactions are rated near ceiling only by rubrics that ask whether an action is depicted

## Source

- Dhruba Ghosh, Hannaneh Hajishirzi and Ludwig Schmidt (2023), "GenEval",
  NeurIPS 2023, [LIT-782](../literature.d/LIT-782.md), read in [NOTE-593](../notes.d/NOTE-593.md).
- Kaiyi Huang, Kaiyue Sun, Enze Xie, Zhenguo Li and Xihui Liu (2023),
  "T2I-CompBench", NeurIPS 2023, [LIT-783](../literature.d/LIT-783.md), read in [NOTE-592](../notes.d/NOTE-592.md) (the conference
  version).
- Kaiyi Huang, Chengqi Duan and four co-authors (2025),
  "T2I-CompBench++", the journal extension, [LIT-798](../literature.d/LIT-798.md), read in [NOTE-610](../notes.d/NOTE-610.md).

## What was actually shown

**GenEval (Table 2; 553 templated prompts, 4 images each, COCO classes).**
A detector and a masked-crop colour classifier judge each image correct
or not. Single object: 0.97–0.98 for every diffusion model. Relative
position: at most 0.15 (SD-XL; IF-XL 0.13). Attribute binding: at most
0.35 (IF-XL). Overall IF-XL 0.61, SD-XL 0.55, SD v2.1 0.50. Overall scores
vary by about 0.01 across seeds. The verdicts agree with crowd annotators
83% of the time, against 88% between annotators.

**T2I-CompBench, human ratings (Tables 2–4; six models, three raters per
image).** Spatial relations are hardest (0.31–0.46), shape binding next
(0.51–0.70), and non-spatial relations, interactions such as hold, wear
and look at, easiest (0.81–0.99). The journal version adds numeracy
(0.52–0.57) and depth relations (0.49–0.55) and keeps the ordering
(Tables VIII–XI).

**Scale and training (GenEval Fig. 5, Table 3).** Across IF-M, IF-L and
IF-XL, with the same T5-XXL text encoder, two-object, counting and binding
improve; position does not. Across SD v1.1–v1.5, continued training on
LAION, overall stays at 0.41–0.44; SD v2, with a different text encoder,
jumps to 0.50–0.51. Rewriting prompts to three times the length does not
help SDXL's colour binding ([LIT-798](../literature.d/LIT-798.md), Table XVII).

**Failure patterns (GenEval Fig. 6).** IF-XL puts the first-named object
on the left more often than the right although directions are balanced;
SD v2.1 swaps the two colours in binding prompts markedly more often than
IF-XL.

**What could have come out otherwise.** Two benchmarks built
independently, with different prompts, judges and models, could have
ranked the skills differently. Both put spatial relations at the bottom
and single objects or interactions at the top.

## What this does not say

- **That interactions are easy.** Human scores there are 0.95–0.99 for five
  of six models, and the rubric asks only whether "actions, events and
  relationships" are portrayed ([LIT-798](../literature.d/LIT-798.md), Table V). Near ceiling may mean
  the category asks little; reversed roles or varied stance were not
  tested.
- **That the ordering holds for DALL·E 3, SD3 or FLUX.1.** They are ranked
  by automatic judges only. DALL-E 3 was human-rated elsewhere, with a
  different design ([THEORY-250](THEORY-250.md)).
- **Why position fails.** GenEval's scale result is one model family at
  three sizes, and the SD v2 jump is confounded with its other changes.
- **That composition fails because the combination was unseen.** No study
  here controls what the training data covered. GORS's binding gain is
  weaker on adjective–noun pairs absent from its 700 finetuning prompts
  (colour 0.72 against 0.54, texture 0.76 against 0.36), but the unseen
  pairs are rarer by construction and no baseline is reported on the
  split.
- **That embedding similarity can judge composition.** Both benchmarks
  find CLIPScore tracks human judgement worst on counting, position and
  binding. That is a claim about how to evaluate generators, which the
  readings leave to the anthology, and it is not part of this account.
- **Anything about detectors' blind spots.** GenEval sees only COCO's 80
  classes and photographic renders; its thresholds were tuned on the same
  human labels, with cross-validation.

## Connections

- **DALL-E 3's relations** ([THEORY-250](THEORY-250.md), from [LIT-938](../literature.d/LIT-938.md)). Human-judged
  agreement on one later model falls when an asymmetric relation is
  reversed and when two relations combine, with errors mostly wrong or
  role-swapped relations. It is consistent with relations being the hard
  case, on a design this account lacks.
- **Composable Diffusion** ([THEORY-tmp0iif2](THEORY-tmp0iif2.md), from [LIT-770](../literature.d/LIT-770.md)), re-implemented
  on SD v2, is the weakest method on most T2I-CompBench categories (2D
  spatial 0.080 by UniDet, the lowest of all models in [LIT-798](../literature.d/LIT-798.md)).
- **Attend-and-Excite** ([THEORY-tmpy5vxl](THEORY-tmpy5vxl.md), from [LIT-806](../literature.d/LIT-806.md)) raises colour and
  texture binding on SD v2 and leaves shape binding and relations nearly
  unchanged ([LIT-798](../literature.d/LIT-798.md), Table XIII).
- **Compositional generalisation** ([THEORY-117](THEORY-117.md), from [LIT-667](../literature.d/LIT-667.md)) is about
  classifiers trained from scratch with controlled coverage; none of these
  benchmarks tests it.
- [CLAIM-321](../claims.d/CLAIM-321.md) states this pattern as the record's own claim; [CLAIM-097](../claims.d/CLAIM-097.md) and
  [CLAIM-013](../claims.d/CLAIM-013.md) make the points about interactions and about what the
  benchmarks leave out.
