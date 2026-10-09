---
number: 592
status: Read
formerly:
- NOTE-tmpf93nl
paper: 'LIT-783'
title: 'T2I-CompBench'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v2 (30 October 2023, 25 pages, text layer), the
    conference version, whose first page carries the NeurIPS 2023
    Datasets and Benchmarks track line; not v3 (T2I-CompBench++, March
    2025), which is the current arXiv version. Sections 1–7 read in full,
    with Tables 1–6. Appendices A (implementation), B (prompt
    construction, Table 7), C (MiniGPT-4 prompts, human evaluation), D.1
    (seen and unseen splits, Table 12), D.3 (rewards for GORS-unbiased),
    D.4 (training-set size, Table 14) and E (limitations) read; D.2
    (Table 13), D.5, D.6 and the annotation-interface figures skimmed. The
    qualitative figures were seen only as captions and prompts.
date: '2026-10-09'
summary: >-
  6,000 compositional prompts (attribute binding by colour, shape and
  texture; spatial and non-spatial relations; complex), each sub-category
  split 700/300, with a metric per category: question-per-object BLIP-VQA
  for binding (Kendall τ 0.63 with humans on colour against 0.19 for
  CLIPScore), a UniDet box rule for space, and a 3-in-1 average for
  complex prompts. Spatial relations are hardest. GORS, reward-weighted
  LoRA finetuning of SD v2 on its own selected samples, is rated best by
  humans in every sub-category, but
  its binding score falls sharply on pairs unseen in finetuning.
---

# NOTE-592: T2I-CompBench

## Contribution

A benchmark that names six kinds of compositional prompt for text-to-image
models and supplies 1,000 prompts for each, with a train/test split and,
within the binding test sets, a split by whether the adjective–noun pair
occurs in training. Before it, compositional benchmarks each covered one
skill (mostly colour binding) with small vocabularies (Table 1). After it,
there is a shared open-vocabulary prompt set, per-category automatic
metrics that rank models more like humans do than CLIPScore or caption
similarity, and a simple finetuning baseline (GORS).

## Key insight

No single automatic judge is good at every kind of composition, so match
the judge to the kind. Ask a VQA model one question per object–attribute
pair rather than one question about the whole prompt; read spatial
relations off detector boxes; and leave action-like relations, where no
better tool was found, to CLIPScore.

## Assumptions

- **Six sub-categories**: colour, shape and texture binding; spatial
  relations (seven phrases: on the side of, next to, near, left, right,
  bottom, top); non-spatial relations (interactions such as hold, wear,
  look at); complex compositions (more than two objects, or several or
  mixed attributes, in four scenarios of 250 prompts).
- **Prompt sources**: binding prompts are 800 templated ("a {adj} {noun}
  and a {adj} {noun}") and 200 natural per attribute type; colour draws 480
  prompts from CC500 and 200 from COCO captions; most of the rest are
  written by ChatGPT from given attribute lists (Appendix B).
- **Scorers are pretrained models**: BLIP (ViT-B, CapFilt-L) finetuned on
  VQA; UniDet trained on COCO, Objects365, OpenImages and Mapillary;
  CLIPScore with ViT-B/32; MiniGPT-4 (Vicuna 13B).
- **Human ground truth**: alignment rated 1–5 by three Mechanical Turk
  workers, divided by 5; 25 prompts per sub-category per model, 2 images
  each, 1,800 image–prompt pairs over six models.
- **Baselines re-implemented on SD v2**: Composable, Structured and
  Attend-and-Excite diffusion, for a common base.

## Key results

- **Metric agreement with humans (Table 5).** Disentangled BLIP-VQA:
  τ 0.63 / ρ 0.80 on colour, 0.27 / 0.38 on shape, 0.52 / 0.70 on texture;
  CLIPScore on the same: 0.19 / 0.28, 0.06 / 0.08, 0.29 / 0.40. One
  question for the whole prompt (B-VQA-n) sits between. UniDet on spatial:
  0.48 / 0.51 against CLIPScore 0.27 / 0.35. Non-spatial: CLIPScore 0.25 /
  0.32, B-CLIP 0.23 / 0.30, and nothing better. Complex: 3-in-1 0.28 /
  0.39. MiniGPT-4 alone is near zero on spatial and complex (τ 0.02,
  0.01); chain-of-thought prompting raises it but it stays below the
  proposed metrics everywhere.
- **Hardest and easiest (Tables 2–4, human scores).** Spatial relations are
  hardest (0.31–0.46 across models), shape binding next (0.51–0.70);
  non-spatial relations are easiest (0.81–0.99). UniDet spatial scores
  are 0.08–0.18.
- **Models.** SD v2 beats SD v1-4 on every category and metric. Structured
  Diffusion, which helped binding on SD v1-4 in its own paper, adds little
  on SD v2. Composable Diffusion on SD v2 does worst on most categories.
  Attend-and-Excite helps binding.
- **GORS (Tables 2–4, 6).** Best human score in every sub-category, and
  best on the proposed metric in five of six; colour B-VQA 0.66 against
  0.51 for SD v2. On complex prompts its 3-in-1 score (0.333) is below
  Attend-and-Excite's (0.340) and GORS-unbiased's (0.347), though the text
  says GORS outperforms previous approaches "across all types of
  compositional prompts". A variant whose
  sample-selection rewards differ from the evaluation metrics
  (GORS-unbiased: Grounded-SAM, GLIP, BLIP captions with CLIP) scores
  close to it. Finetuning both the text encoder and the U-Net beats either
  alone; lowering the selection threshold hurts. On complex prompts, the
  3-in-1 score rises from 0.26 to 0.35 as the finetuning set grows from 25
  to 1,400 prompts (Table 14).
- **Seen against unseen pairs (Table 12, GORS only).** Disentangled
  BLIP-VQA on seen and unseen adjective–noun pairs: colour 0.72 and 0.54,
  shape 0.55 and 0.34, texture 0.76 and 0.36. The text calls this
  "slightly lower". CLIPScore barely moves (for example 0.34 and 0.33 on
  colour), which is consistent with its low agreement with humans.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Category-specific metrics rank images more like human raters than CLIPScore or caption similarity | moderate: 50 images per sub-category per model, three raters each, rank correlations reported without confidence intervals | Table 5 |
| C2 | Spatial relations are the hardest category and non-spatial relations the easiest for 2023 diffusion models | moderate: human scores, consistent across six models | Tables 2–4 |
| C3 | Multimodal LLMs (MiniGPT-4) are not yet reliable judges of composition | moderate for MiniGPT-4 as tested; says nothing of later models | Table 5, Table 13 |
| C4 | Reward-weighted finetuning on selected own samples improves compositional scores | moderate: holds under human evaluation and under rewards that differ from the metrics; not on the 3-in-1 metric for complex prompts | Tables 2–4, 6, D.3 |
| C5 | GORS's gain is weaker on attribute pairs absent from its finetuning prompts | weak: one model, unseen pairs also rarer by construction, no baseline on the split; the text understates the gap | Table 12 |

## Method

GORS: for each training prompt, generate k images with the pretrained
model, score each with the alignment metric of its category as a reward,
keep the images whose reward exceeds a threshold, and finetune with the
diffusion loss weighted by the reward,
L(θ) = E_{(x,y,s)∈D_s} [ s · ‖ε − ε_θ(z_t, t, y)‖² ], using LoRA on the
attention layers of the U-Net and the self-attention layers of the CLIP
text encoder (AdamW, batch 5, 50,000–100,000 steps on 8 V100s). The
evaluation metrics: disentangled BLIP-VQA multiplies the probability of
"yes" over one question per object–attribute phrase; the UniDet rule says
object 1 is left of object 2 when x₁ < x₂, |x₁ − x₂| > |y₁ − y₂| and the
boxes' IoU is below 0.1 (similarly for right, top, bottom; "near", "next
to", "on the side of" by a centre-distance threshold); 3-in-1 averages
CLIPScore, BLIP-VQA and UniDet.

## Concepts

- **compositionality** (of a text-to-image model): "the ability … to
  compose different concepts into a complex and coherent scene according
  to text prompts" (Section 3).
- **attribute binding**: assigning each stated attribute to the right
  object when a prompt has at least two objects and two attributes.
- **seen / unseen split**: within each binding test set, 200 prompts whose
  adjective–noun pairs occur in the 700 training prompts and 100 whose
  pairs do not.
- **disentangled BLIP-VQA**: one VQA question per object–attribute pair,
  scores multiplied; set against **B-VQA-n**, one question for the whole
  prompt.
- **GORS**: Generative mOdel finetuning with Reward-driven Sample
  selection.

## Connections

- **Composable Diffusion** (Liu et al., [LIT-770](../literature.d/LIT-770.md)) is one of the
  re-implemented baselines; here it does worst, which the authors relate
  to its mixing subjects and to its design for conjunction and negation
  rather than binding or relations.
- **Structured Diffusion (Feng et al.)** and **Attend-and-Excite (Chefer
  et al.)** are the binding-specific baselines; CC500 and ABC-6K, from
  Feng et al., supply part of the colour prompts.
- **RAFT (Dong et al.)**, concurrent, finetunes on reward-ranked samples
  over several rounds; GORS uses one round of selection.
- **GenEval** ([LIT-782](../literature.d/LIT-782.md), [NOTE-593](NOTE-593.md)), in the same NeurIPS 2023
  track, has the same aim with templated prompts over COCO classes and one
  detector-based pipeline; neither paper cites the other. Both find
  spatial relations hardest and CLIPScore weakest on composition.
- **Version.** arXiv's current version (v3) is the journal paper,
  T2I-CompBench++, which adds numeracy and 3D-spatial categories and other
  metrics. Nothing here is from it.

## Bearing on the record

- **[THEORY-117](../theory.d/THEORY-117.md) (from [LIT-667](../literature.d/LIT-667.md)).** Table 12 is the nearest thing in these
  readings to a coverage test: after finetuning, binding is judged much
  better on adjective–noun pairs that occurred in the finetuning prompts
  than on pairs that did not, by 0.18–0.40 in BLIP-VQA. The direction is
  the one [THEORY-117](../theory.d/THEORY-117.md) would lead one to expect, but it does not test that
  account. "Unseen" means unseen in 700 finetuning prompts, not in
  pretraining; the unseen pairs are also rarer combinations by the
  authors' own description; and no baseline model is reported on the
  split, so the gap cannot be laid to finetuning. I did not add it to
  [THEORY-117](../theory.d/THEORY-117.md).
- **THEORY candidate (not filed, anthology material)**, shared with
  [NOTE-593](NOTE-593.md): holistic image–text embedding similarity does not track
  human judgement of composition, where decomposed checks do. Table 5
  here and GenEval's Figure 3 both support it. It is a claim about
  evaluating machine-learning models, which an anthology topic can hold.
- **Anthology.** The benchmark, its metrics and GORS are machine-learning
  practice (how to evaluate and how to finetune for compositional
  prompts) and belong in the Anthology of the SOTA.

## Limitations

- **No single metric** for all categories; the authors say so (Section 7,
  Appendix E). Non-spatial relations fall back on CLIPScore, whose
  agreement there (τ 0.25) is only marginally above caption similarity.
- **Small human study.** 50 images per sub-category per model; Kendall and
  Spearman values reported without intervals, and whether the
  correlations are over images or models is not stated.
- **Non-spatial human scores are near ceiling** (0.95–0.99 for five of
  six models), which limits what any metric's correlation there can show.
- **Evaluator–reward overlap.** GORS selects and weights its samples with
  the very metrics it is then scored by; GORS-unbiased and the human
  scores answer this in part.
- **2D only.** UniDet's rule cannot judge depth; the authors leave 3D
  relations to future work. BLIP-VQA fails when shapes are hidden or
  uncommon (Figure 13).
- **ChatGPT-written prompts and judges built on pretrained multimodal
  models** carry those models' biases, which the authors note.

## Open questions

- How large is the seen/unseen gap for SD v2 itself, before finetuning?
  That would say whether GORS creates it or inherits it.
- Is there a single judge (the authors look to multimodal LLMs) that
  matches the per-category metrics in every category?
- Why are spatial relations hardest, and does a training set that controls
  how often each spatial phrase pairs with each object change that?
