---
number: 610
status: Read
formerly:
- NOTE-tmp8sckc
paper: 'LIT-798'
title: 'T2I-CompBench++'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv 2307.06350 v3 (8 March 2025, 19 pages, the journal
    version per the arXiv comment; text extracted with pdftotext):
    Sections I–VII in full, Tables I–XX, the ChatGPT prompt templates
    and the MLLM prompt tables (III–VII), the Mechanical Turk interfaces
    (Figs. 4–6) and the reference list. The qualitative comparisons
    (Figs. 7–11) were skimmed from their captions; the images were not
    inspected. The typeset TPAMI article (DOI 10.1109/TPAMI.2025.3531907)
    was not reached, so small differences from v3 cannot be excluded.
    Read alongside NOTE-592, the reading of the conference version, to
    separate what is new.
date: '2026-10-09'
summary: >-
  Extends T2I-CompBench to eight sub-categories (adding numeracy and 3D
  spatial relations), tests multimodal LLMs as judges, and benchmarks
  eleven models. GPT-4V agrees with human rankings best on interactions
  and complex prompts, where CLIPScore and the conference version's 3-in-1
  metric were weak; specialised VQA and detector metrics stay best
  elsewhere. Human ratings cover only six 2023-era models, and the
  interaction category remains near ceiling for humans.
---

<!-- inactive-ok-file: CLAIM-123 — Proposed; named as the manuscript claim this reading bears on -->
<!-- inactive-ok-file: CLAIM-013 — Proposed; named as the manuscript claim this reading bears on -->

# NOTE-610: T2I-CompBench++

## Contribution

It widens the conference benchmark ([LIT-783](../literature.d/LIT-783.md)) in three ways: two new kinds
of composition (generative numeracy, and relations in depth), judges for
them (a detector count; detection plus monocular depth), and a test of
multimodal LLMs as general judges, validated against the same human-rating
protocol. It then ranks eleven text-to-image models, including the
2024–25 generation, on all eight sub-categories. What is true after it is
that an MLLM judge (GPT-4V) tracks human rankings of interaction and
complex prompts better than any embedding-similarity or specialised metric
tested, while the specialised metrics still win where the property is
local and checkable.

## Key insight

No single judge fits every kind of composition. Properties that decompose
into local checks (this object has this colour; this box is left of that
one; there are three of these) are best judged by decomposed, special-
purpose models; properties that depend on reading the whole scene (who is
doing what to whom; a prompt with several objects, attributes and
relations) are best judged by a general multimodal model asked to describe
and then score.

## Assumptions

- Composition is operationalised as eight prompt families; most prompts
  are templated or written by ChatGPT from given word lists, including
  physically implausible combinations on purpose.
- Human ground truth: three Mechanical Turk workers rate image–text
  alignment on a 1–5 scale per sub-category, with sub-category-specific
  instructions (Figs. 4–6), normalised by 5; 25 prompts per sub-category,
  two images each, for each of six models.
- Automatic judges are pretrained models: BLIP-VQA, UniDet with a depth
  estimator, CLIP ViT-B/32, MiniGPT-4, ShareGPT4V, GPT-4V. GPT-4V is
  evaluated on one fifth of the images (600 per category) for quota
  reasons.
- 10 images per prompt with fixed seeds; DALL·E 3, whose API takes no
  seed, gets 3 images per prompt.

## Key results

- **New sub-categories** (Section III). Numeracy: 30% single-kind, 30%
  two-kind, 40% multi-kind prompts, counts 1–8, fixed templates and
  natural rewrites at 4:1. 3D spatial: "in front of", "behind", "hidden
  by" over persons, animals and objects. 2D spatial left/right/top/bottom
  prompts come in swapped pairs ("a girl on the left of a horse" / "a
  horse on the left of a girl").
- **New metrics** (Section IV). 3D: object 1 is in front of object 2 if
  its mean depth exceeds the other's and the boxes' IoU exceeds 0.5.
  Numeracy: for n named kinds, 1/(2n) for each kind detected and another
  1/(2n) if its count is right. MLLM judges: "describe the image", then
  "score alignment 0–100" with category-specific rubrics (Tables III–VII).
- **Agreement with humans** (Table XII, Kendall τ / Spearman ρ).
  Colour: B-VQA 0.630/0.796, GPT-4V 0.524/0.647, CLIP 0.194/0.277. Shape:
  Share-CoT 0.287/0.366, B-VQA 0.271/0.380, CLIP 0.056/0.082. Texture:
  B-VQA 0.518/0.700. 2D spatial: UniDet 0.476/0.514, GPT-4V 0.346/0.404.
  3D spatial: UniDet 0.313/0.426, Share-CoT 0.271/0.319. Numeracy: UniDet
  0.425/0.527, Share-CoT 0.418/0.489. Non-spatial: GPT-4V 0.476/0.534,
  Share-CoT 0.340/0.362, CLIP 0.247/0.316. Complex: GPT-4V 0.507/0.594,
  Share-CoT 0.320/0.365, 3-in-1 0.283/0.385, CLIP 0.065/0.085. MiniGPT-4
  without chain-of-thought is near zero everywhere.
- **Human ratings** (Tables VIII–XI, six models). 2D spatial 0.31–0.46;
  3D spatial 0.49–0.55; numeracy 0.52–0.57; shape 0.51–0.70; colour
  0.62–0.83; texture 0.63–0.86; complex 0.75–0.87; non-spatial 0.81–0.99,
  and 0.95–0.99 for every model but Composable Diffusion.
- **Benchmark** (Table XIII, automatic). SD3: colour 0.813, texture
  0.733, 2D spatial 0.320, 3D 0.408; DALL·E 3: shape 0.621; FLUX.1:
  numeracy 0.619, interactions by GPT-4V 0.921, complex by GPT-4V 0.873. GORS
  on SD v2: colour 0.660 against 0.507 for SD v2.
- **Stability of MLLM judges** (Table XVIII). Five runs on 50 images:
  GPT-4V means range 0.676–0.708, ShareGPT4V 0.696–0.727.
- **Prompt detail** (Table XVII). Rewriting prompts to three times the
  length with GPT-4 does not help SDXL's colour binding (B-VQA 0.588 to
  0.578).
- **Seen/unseen** (Table XV). As in the conference version: GORS B-VQA
  0.719/0.543 (colour), 0.550/0.336 (shape), 0.765/0.357 (texture).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | GPT-4V ranks interaction and complex-prompt images more like human raters than CLIPScore, caption similarity or the 3-in-1 metric | moderate: rank correlations without intervals, GPT-4V on a fifth of the images, six models | Table XII |
| C2 | Decomposed VQA and detector rules remain the best judges of binding, 2D and 3D spatial relations and numeracy | moderate | Table XII |
| C3 | Spatial relations are the hardest category and interactions the easiest | moderate for the six 2023-era models rated by humans; not established for the 2024–25 models | Tables VIII–XI |
| C4 | DALL·E 3, SD3 and FLUX.1 are markedly better at composition than earlier models | moderate: automatic metrics only, which C1–C2 validate on older models | Table XIII |
| C5 | MLLM judges are stable across repeated runs | weak: 50 images, one category, five runs | Table XVIII |
| C6 | Longer, more detailed prompts do not fix binding | weak: one model, one category | Table XVII |
| C7 | GORS's binding gain is weaker on unseen adjective–noun pairs | weak (as in [NOTE-592](NOTE-592.md)): no baseline on the split, unseen pairs rarer | Table XV |

## Method

GORS is unchanged from the conference version ([NOTE-592](NOTE-592.md)): generate
samples from SD v2, keep those whose reward exceeds a threshold, finetune
with the diffusion loss weighted by the reward, LoRA on the U-Net and the
CLIP text encoder. Its rewards in GORS-unbiased are Grounded-SAM masks for
binding, GLIP for spatial relations and numeracy, BLIP captions with CLIP
for interactions. The 3-in-1 metric averages CLIPScore, B-VQA and UniDet.

## Concepts

- **generative numeracy**: generating the stated number of each named
  kind of object.
- **3D-spatial relationship**: an ordering in depth between two objects
  ("in front of", "behind", "hidden by"), judged from monocular depth and
  box overlap.
- **MLLM-as-judge**: a multimodal LLM asked to describe an image and then
  score its alignment with the prompt against a rubric; "-CoT" marks the
  two-step describe-then-score prompting.
- The concepts of the conference version (compositionality of a T2I
  model, attribute binding, seen/unseen split, disentangled BLIP-VQA,
  GORS) are as in [NOTE-592](NOTE-592.md).

## Connections

It `extends` [LIT-783](../literature.d/LIT-783.md) ([NOTE-592](NOTE-592.md)), whose prompts, splits, binding and 2D
metrics, human protocol and GORS it keeps. Its baselines include
Composable Diffusion ([LIT-770](../literature.d/LIT-770.md)), Structured Diffusion and Attend-and-Excite
([LIT-806](../literature.d/LIT-806.md)), all re-implemented on SD v2, with the same ordering as in
the conference version: Attend-and-Excite helps colour and texture binding
most, Composable Diffusion does worst. Table I lists earlier benchmarks
(CC-500, ABC-6K, Attend-and-Excite's 210 prompts, HRS-comp). GenEval
([LIT-782](../literature.d/LIT-782.md)) is still not cited.

## Bearing on the record

- **[CLAIM-097](../claims.d/CLAIM-097.md)** says T2I-CompBench's interaction category is
  "scored by CLIPScore" and sits near human ceiling. For the conference
  version that is right. In this version the recommended judge for
  interactions is GPT-4V, which agrees with humans almost twice as well
  (τ 0.48 against 0.25), with CLIPScore kept only as the best non-MLLM
  metric. The second half of the claim stands: human ratings of
  interactions are 0.95–0.99 for five of six models, so the category
  still separates models poorly, whatever the judge. The rubric asks only
  whether "actions, events and relationships" are portrayed (Table V);
  nothing in it asks about stance or the relation between participants
  beyond the action. If the manuscript cites the benchmark, which version
  it means changes what can be said of the interaction judge.
- **[CLAIM-013](../claims.d/CLAIM-013.md)** (existing benchmarks are object-centred and need
  extending to pragmatically consequential relations). The journal
  version's additions are numeracy and depth ordering: more geometry and
  counting, not social or communicative content. As of 2025 the claim's
  description of this benchmark still holds, with interactions as its one
  relational category beyond space.
- **[CLAIM-123](../claims.d/CLAIM-123.md).** Composable Diffusion re-implemented on SD v2 is
  again the weakest method on most sub-categories (Table XIII) and the
  only one far below ceiling on interactions in human ratings (0.81). This
  is the same evidence as the conference version gave, with two more
  sub-categories (2D spatial 0.080 by UniDet, the lowest of all models).
- **Two internal slips.** The limitations paragraph (Section VI-G) still
  says the UniDet metric "is limited to evaluating 2D spatial
  relationships and we leave 3D spatial relationships for future study",
  a sentence carried over from the conference version that the journal
  version's own 3D metric contradicts. And the human-evaluation paragraph
  says 25 prompts with two images each per sub-category give "300 images
  … with 200 prompts per model"; eight sub-categories give 200 prompts and
  400 images. Neither changes a result.
- **Anthology.** A benchmark, metrics and a finetuning method are
  machine-learning practice; the flag stays. No THEORY is filed. The
  THEORY candidate left unfiled in [NOTE-592](NOTE-592.md) (holistic embedding similarity
  does not track human judgement of composition) gains support from
  Table XII, and remains anthology material.

## Limitations

- Human validation covers six 2023-era models; the eleven-model ranking
  rests on judges validated on those six.
- At what level the rank correlations are computed (images, prompts or
  models) is not stated; there are no confidence intervals.
- GPT-4V scored a fifth of the images, the other judges all of them.
- The 3D rule depends on a monocular depth model and a box-overlap
  threshold; it is not separately validated beyond Table XII.
- The authors note there is still no unified metric, and that their
  metrics fail on hard cases (Fig. 10).

## Open questions

- Do the human-rating results (hardest, easiest categories) still hold for
  DALL·E 3, SD3 and FLUX.1? Human ratings of those models under the same
  protocol would answer it.
- Is the interaction category near ceiling because current models are
  good at interactions, or because the prompts and rubric ask only whether
  an action is depicted? A harder interaction set, with roles reversed or
  with stance varied, rated by humans, would separate the two.
