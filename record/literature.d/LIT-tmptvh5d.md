---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpfly41](../notes.d/NOTE-tmpfly41.md)); worth reading as a measurement of where text-to-image models of 2023 fail at composition, and of how badly embedding similarity sees it: a COCO-trained detector plus masked-crop CLIP colour classification judges each image correct or not on presence, count, position and colour, agreeing with crowd annotators 83% of the time against 88% between annotators, and beating a per-task tuned CLIPScore on counting (by 22 points), position and attribute binding. The best open model (IF-XL) gets 0.61 overall but at most 0.15 on relative position and 0.35 on binding; scaling IF helps binding but not position, and continued training of Stable Diffusion v1 leaves scores flat.'
title: 'GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read on 2026-10-09 from arXiv v1 (17 October 2023, 21 pages, the
    only arXiv version): main text in full and Appendices A, C and D
    (NOTE-tmpfly41). Code at github.com/djghosh13/geneval. The arXiv
    PDF and record carry no venue line or journal reference; the venue,
    NeurIPS 2023 Datasets and Benchmarks track, was checked on
    2026-10-09 against the NeurIPS 2023 proceedings listing
    (papers.nips.cc, filed under Datasets_and_Benchmarks) and OpenReview
    (forum Wbr51vK331, "NeurIPS 2023 Datasets and Benchmarks Poster").
    The manuscript cites it as arXiv only. `published:` is the arXiv v1
    date. Not held in the Anthology of
    the SOTA as a LIT: a grep of its record/ (clone of 2026-10-09,
    commit 1cffe8f) for the identifier, the title and the authors found
    the work named only in prose inside other entries, or not at all.
tags:
- compositionality
- anthology-candidate
date: '2026-10-09'
published: '2023-10-17'
arxiv: '2310.11513'
first_author: 'Ghosh'
keywords:
- 'text-to-image'
- 'evaluation'
- 'compositionality'
- 'object detection'
- 'attribute binding'
implementations: []
summary: >-
  Ghosh, Hajishirzi & Schmidt (2023), NeurIPS 2023 Datasets and
  Benchmarks. An automated benchmark that uses
  object detectors to score text-to-image outputs on object co-
  occurrence, position, count and colour, agreeing well with human
  judgement; models of 2023 still fail at spatial relations and
  attribute binding. Detector verdicts agree with annotators 83% of the
  time (annotators with each other 88%); the best open model, IF-XL,
  scores 0.61 overall, 0.13 on position and 0.35 on binding.
---

# LIT-tmptvh5d: GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment

Dhruba Ghosh, Hannaneh Hajishirzi and Ludwig Schmidt (2023), *NeurIPS 2023
Datasets and Benchmarks* —
[ARXIV-2310.11513](https://arxiv.org/abs/2310.11513)

## Key takeaways

- **Decompose the prompt, then check the parts.** Each of 553 templated
  prompts over the 80 COCO classes (six tasks: single object, two object,
  counting, colours, position, attribute binding) is checked by a
  Mask2Former detector for presence and count, by box centroids with a
  minimum offset for position, and by zero-shot CLIP on a masked crop for
  colour. An image scores 1 only if every part is right, and a failed
  image comes with the reason.
- **Close to human agreement** (Section 4). On 1,200 images with five
  annotations each, GenEval agrees with annotators 83% of the time,
  annotators with each other 88%, and a CLIPScore with its best backbone
  and a per-task tuned threshold 80%. GenEval wins on counting (by 22
  points), position, two object and binding; CLIPScore is slightly ahead
  on the easy single-object and colour tasks.
- **Where 2023 models fail** (Table 2). IF-XL 0.61 overall, SD-XL 0.55,
  SD v2.1 0.50. Relative position tops out at 0.15 and attribute binding
  at 0.35, while single objects are near 0.98. IF-XL places the first
  named object on the left more often than on the right; SD v2.1 swaps
  the two colours more often than IF-XL (Figure 6).
- **Scale against training** (Figure 5). Larger IF models improve on
  binding and counting but not on position; five successive checkpoints
  of SD v1, trained on more LAION data, stay at 0.41–0.44, while SD v2,
  with a different text encoder, reaches 0.50–0.51.
- **Bounded by its detector**: COCO classes, photographs, and failures on
  masks with holes and merged same-class objects (Figure 4, Section 6).

The record's reading of compositional generalization in vision models is
[LIT-667](LIT-667.md) ([THEORY-117](../theory.d/THEORY-117.md)). GenEval measures compositional failure in
generators without controlling what their training data covered, so it
does not test that account ([NOTE-tmpfly41](../notes.d/NOTE-tmpfly41.md)). Its companion benchmark in the
same NeurIPS track is T2I-CompBench ([LIT-tmpvb4kp](LIT-tmpvb4kp.md)).

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day. It is a
machine-learning paper an anthology topic could hold (generative-modeling,
analysis-and-evaluation), so it carries the `anthology-candidate` flag
([ADR-005](../decisions.d/ADR-005.md)); it is here because the owner asked for
the manuscript's references to be filed in this record.

**After reading.** The paper is an evaluation method for text-to-image
models, and what it teaches (check detected objects rather than embedding
similarity; crop and mask before classifying colour) is machine-learning
practice, anthology material. The flag stays. It was first filed under
`representation-learning`, which the reading did not support: the paper does
not study how a model represents its data, only whether its outputs are
right. It is filed under `compositionality` ([ADR-031](../decisions.d/ADR-031.md)), the subject it shares
with this record; the evaluation of generative models is an anthology
subject.
