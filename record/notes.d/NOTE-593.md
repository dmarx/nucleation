---
number: 593
status: Read
formerly:
- NOTE-tmpfly41
paper: 'LIT-782'
title: 'GenEval'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v1 (17 October 2023, 21 pages, text layer; the only
    arXiv version). Sections 1–7 read in full; Appendices A (Tables 3–4,
    Figures 7–10), C (prompt generation, models, the position and
    colour-classification rules, the CLIPScore baseline and Table 5) and
    D (human-study protocol) read; the annotation-interface screenshots
    and the full HIT text after D.1's instructions skimmed. Bar heights in
    Figures 3, 5, 6 and 7 that the text does not state are not reported.
    The arXiv PDF carries no venue line; the venue was checked against the
    NeurIPS 2023 proceedings listing and OpenReview (below, on the LIT).
date: '2026-10-09'
summary: >-
  An automated text-to-image benchmark of 553 templated prompts in six
  tasks, scored per image as correct or not by a COCO-trained
  Mask2Former (presence, count, position) and masked-crop zero-shot CLIP
  (colour). 83% agreement with human annotators against 88% between
  annotators, and 91% on unanimous images; beats a per-task tuned
  CLIPScore on counting, position and binding. Best 2023 open model
  (IF-XL) scores 0.61 overall, at most 0.15 on position and 0.35 on
  attribute binding.
---

# NOTE-593: GenEval

## Contribution

A text-to-image evaluation that breaks each prompt into objects, counts,
colours and relative positions, and checks each against the output of
off-the-shelf discriminative vision models, returning a binary verdict per
image with a stated reason when it fails. Before it, automatic scores were
either holistic (FID, CLIPScore, preference models) or needed task-specific
detectors (DALL-Eval). After it, there is a detector-based check that needs
no task-specific training, agrees with crowd annotators nearly as often as
they agree with each other, and is more reliable than embedding similarity
exactly on the compositional tasks.

## Key insight

A similarity score between a prompt embedding and an image embedding cannot
say whether the image has three cups or two, or whether the dog is left of
the bench, because it never isolates the objects. Detect the objects first,
then read count and position off the boxes and colour off a masked crop, and
the verdict becomes a conjunction of checkable parts, each of which can be
wrong in an inspectable way.

## Assumptions

- **Closed vocabulary**: objects are the 80 MS COCO classes (some renamed,
  "mouse" to "computer mouse"), because the detector is COCO-trained.
- **Templated prompts**: "a photo of …" templates with sampled objects, the
  numbers two, three or four, four relative positions, and ten colours (the
  text cites 11 Berlin–Kay basic colour terms; gray is excluded so the
  masked background can be gray). Plurals are formed by appending "s".
- **Photographic outputs**: the detector is trained on photographs; clip
  art and simple artistic renders fall outside it (Figure 4).
- **Correctness is a conjunction**: an image is correct only if every
  element is; extra objects are allowed except in counting.
- **Hyperparameters chosen against the human labels**: a detection
  threshold of 0.3 (0.9 for counting) and a minimum offset c = 0.1 for
  position, both picked for human agreement and checked by 5-fold
  cross-validation.

## Key results

- **Human agreement (Figure 3, Section 4).** 1,200 images (400 each from
  SD v2.1, IF-XL and CLIP retrieval from LAION-5B), 5 annotations each,
  6,000 in all. GenEval 83% agreement with annotators, interannotator 88%,
  CLIPScore (OpenCLIP ViT-H/14, threshold tuned per task) 80%. On the 860
  images where all five annotators agree: GenEval 91%, CLIPScore 87%.
  CLIPScore is slightly better on single object and colours; GenEval is
  better on two object, counting, position and binding, by 22 points on
  counting.
- **Benchmark (Table 2; 553 prompts, 4 images each).** Overall: IF-XL
  0.61, SD-XL 0.55, SD v2.1 0.50, SD v1.5 0.43, CLIP retrieval 0.35,
  minDALL-E 0.23. Position: at most 0.15 (SD-XL; IF-XL 0.13). Attribute
  binding: at most 0.35 (IF-XL). Single object 0.97–0.98 for every
  diffusion model. Overall scores vary by about 0.01 across seeds.
- **Scale and training (Figure 5, Table 3).** Across IF-M, IF-L, IF-XL
  (same T5-XXL text encoder), two object, counting and binding improve;
  position does not. Across SD v1.1–v1.5 (continued training on LAION),
  overall stays at 0.41–0.44; SD v2 (a different text encoder) jumps to
  0.50–0.51.
- **Failure patterns (Figure 6).** IF-XL places the first-named object to
  the left of the second more often than to the right, though directions
  are balanced in the prompts. SD v2.1 swaps the two colours in binding
  prompts markedly more often than IF-XL.
- **Ablations (Table 4, Figure 8).** Cropping plus background masking
  raises colour kappa from 0.32 to 0.45 and binding kappa from 0.01 to
  0.49. Raising the counting threshold to 0.9 raises its kappa from 0.37
  to 0.65.
- **CLIP backbones (Table 5).** Of the CLIPScore backbones tried, ViT-H/14
  agrees best overall (0.798) but worst-but-one on position (0.682 against
  0.790 for ViT-B/32); EVA-02-CLIP, the best on ImageNet, agrees least
  (0.600, 0.240 on position).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Detector-based verdicts agree with crowd annotators nearly as well as annotators agree with each other | moderate: one study, 1,200 images from three sources, two thresholds tuned on the same labels (cross-validated) | Section 4, Figure 3, A.2 |
| C2 | Embedding similarity (CLIPScore) tracks human judgement worse than decomposed checks on counting, position and binding | moderate: CLIPScore given a per-task tuned threshold and its best backbone | Figure 3, Figure 7, Table 5 |
| C3 | 2023 open text-to-image models fail most on relative position and attribute binding | strong within the benchmark: consistent across all models and seeds | Table 2, Table 3 |
| C4 | Scaling the image model helps binding and counting but not position | weak: one model family, three sizes | Figure 5 left |
| C5 | Continued pretraining of SD v1 did not raise scores; the change of text encoder in v2 did | weak: confounded with other v2 changes, which the authors name | Figure 5 right |
| C6 | The verdicts expose systematic failure patterns (position bias, colour swapping) | moderate: two patterns, each in one model | Figure 6, Figure 10 |

## Method

Prompts are generated from six templates (Table 1): single object (80),
two object (99), counting (80), colours (94), position (100), attribute
binding (100), after removing duplicates from 100 samples each. For each
image, Mask2Former (Swin-S, MMDetection) gives boxes and masks above the
confidence threshold. Presence is checked for every task. Counting compares
the number of boxes with the prompt. Position compares box centroids with a
margin proportional to the boxes' sizes: B is right of A when
x_B > x_A + c(w_A + w_B), and so on, c = 0.1 (the "above" rule in C.3 is
printed with the wrong inequality sign). Colour crops each detected object
to its box, replaces the background with gray using the mask, and has CLIP
ViT-L/14 classify it zero-shot among ten colours, averaging three prompt
templates. The image score is 1 only if every check passes; task scores
average over images; the overall score averages the six tasks.

## Concepts

- **GenEval score**: the fraction of images judged wholly correct, per
  task, and the mean of the six task scores overall.
- **attribute binding**: two objects with two different specified colours;
  failure as **swapping** (colours exchanged) or **leakage** (a colour on
  the background), after Feng et al.
- **position**: the four relations above, below, left of, right of, judged
  from box centroids with a minimum visible offset.
- **CLIP retrieval baseline**: the top four LAION-5B images for each prompt
  by CLIP ViT-L/14 similarity, a stand-in for "real images matching the
  prompt".

## Connections

- **CLIPScore (Hessel et al.)** is the baseline it argues against; here
  the authors upgrade its backbone and tune its threshold per task to make
  the comparison fair to it.
- **DALL-Eval (Cho et al.)** used task-specific detectors trained on
  rendered data; **VISOR (Gokhale et al.)** evaluates spatial relations
  exhaustively; GenEval trades depth on one skill for coverage of six
  with off-the-shelf models.
- **TIFA (Hu et al.)**, concurrent, uses an LLM to generate questions and a
  VQA model to answer them; the authors argue detector outputs are easier
  to inspect.
- **T2I-CompBench** ([LIT-783](../literature.d/LIT-783.md), [NOTE-592](NOTE-592.md)) appeared in the same
  NeurIPS 2023 track with an overlapping aim. It uses free-form and
  ChatGPT-written prompts and a different metric per category, where
  GenEval uses templates and one pipeline. Neither cites the other.

## Bearing on the record

- **No THEORY supported or contradicted.** The record's account of
  compositional generalization, [THEORY-117](../theory.d/THEORY-117.md) (from [LIT-667](../literature.d/LIT-667.md)), concerns
  classifiers trained from scratch on two-concept grids with controlled
  coverage. GenEval measures compositional failures in large generators
  without controlling what their training data covered, so it does not
  test it. Two observations sit near it without bearing on it: continued
  training of SD v1 on more LAION data left the scores flat (Figure 5),
  and Stable Diffusion rendered "a white dog and a blue potted plant",
  which CLIP retrieval could not find in LAION (A.3). Neither isolates
  combinatorial coverage, and I did not add them to [THEORY-117](../theory.d/THEORY-117.md).
- **THEORY candidate (not filed, anthology material).** "Holistic
  image–text embedding similarity does not track human judgement of
  counting, relative position or attribute binding, where checks on
  detected objects do." Both this paper (Figure 3) and T2I-CompBench
  (Table 5) support it. It is a claim about how machine-learning models
  should be evaluated, which an anthology topic can hold, so it is not
  filed here.
- **Anthology.** The paper is an evaluation method for text-to-image
  models. Its practical content (score compositional prompts with detector
  checks rather than CLIPScore; crop and mask before classifying colour;
  raise the detection threshold for counting) is machine-learning practice
  and belongs in the Anthology of the SOTA.

## Limitations

- **Bounded by the detector**: COCO's 80 classes at COCO's granularity
  (it can count people, not fingers), and photographs only. The authors
  say so (Section 6).
- **Templated, short prompts.** Six skills, one or two objects, no
  relations other than four 2D directions.
- **Thresholds tuned on the evaluation labels.** The counting threshold and
  the position margin were chosen for agreement with the same human study
  that reports agreement; cross-validation (0.823 and 0.822 agreement on
  held-out folds) limits but does not remove this.
- **Known metric failures** (Figure 4): holes in masks mislead the colour
  classifier; overlapping objects of one class merge; artistic renders
  are missed.
- **Kappa on single object is about 0** because nearly every image is
  correct, so percent agreement there is uninformative (A.1).
- **Defaults only.** Sampler, steps and resolution are left at each
  model's defaults; IF is evaluated without its third stage.
- **One human-agreement number per task is not described.** Table 2 has a
  "Human" column (0.42, 0.57, 0.72 for CLIP retrieval, SD v2.1 and IF-XL)
  whose definition I did not find in the text.

## Open questions

- Does agreement hold with an open-vocabulary detector, which the authors
  name as the way past the COCO limit?
- Is IF-XL's left-placement bias a property of its text encoder, its
  training captions, or its sampler? A run with the prompt order reversed
  and the encoder swapped would separate them.
- Why does model scale help binding but not position? A model whose
  training data control the spatial phrases would test whether the limit
  is data or architecture.
