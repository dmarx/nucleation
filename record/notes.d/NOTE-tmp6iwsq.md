---
status: Read
paper: LIT-tmpgsgpo
title: 'Rethinking the Role of Demonstrations'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v2 PDF (20 Oct 2022, 19 pp.). Sections 1–6 and
    the Limitations read in full; Appendix C.1–C.3 (results comparable
    across models, random labels from the true label distribution, constant
    labels and test-input-only demonstrations) read. The dataset list and
    per-dataset tables of Appendices A–B and the per-dataset plots were
    looked over, not read. Bar heights in the main figures are read from
    the text where the text gives them; I give no numbers the text does
    not state.
date: '2026-10-09'
summary: >-
  Shows empirically that the correctness of in-context labels contributes
  little to classification and multi-choice accuracy, while the input
  distribution, the label space and the paired format contribute most of
  the gain over zero-shot. The authors read this as the demonstrations
  locating a correspondence the model already has, not teaching a new one.
---

# NOTE-tmp6iwsq: Rethinking the Role of Demonstrations

## Contribution

Before this paper, in-context gains were attributed by default to the
labelled pairs in the prompt. It decomposes a demonstration into four parts
and measures each: the input-label mapping, the input distribution, the
label space and the format. The mapping, which is what supervised learning
would use, turns out to matter least; the rest matter most. The result
holds across twelve model–inference combinations up to GPT-3 and is
strongest in a model meta-trained to learn in context.

## Key insight

A demonstration tells a model what kind of inputs to expect, what kind of
outputs are allowed and what shape the exchange has. It barely needs to
tell it which output goes with which input. For these tasks the model
already holds the correspondence, and the prompt selects and formats it.

## Assumptions

- Tasks are classification and multiple choice with a small discrete
  answer set C, and real natural-language inputs; 26 datasets, each with
  under 10K training examples.
- Prediction is argmax over C of the LM's probability (direct) or of the
  input given the label (channel).
- k = 16 demonstrations by default, sampled uniformly from training data,
  five seeds (three datasets each of classification and multi-choice, and
  fewer seeds, for GPT-3 and fairseq 13B).
- Minimal templates by default; manual templates checked in §4.2.
- Using unlabelled training inputs is treated as permitted, which matters
  for the claim about the zero-shot baseline.

## Key results

- **§4.1.** Gold vs random labels: drops of 0–5% absolute across models;
  1.7% (multi-choice) and 2.6% (classification) on average; 0.1–0.9% for
  MetaICL. Gold labels beat no demonstrations, with exceptions the paper
  names (direct GPT-2, GPT-J and fairseq 6.7B near chance on
  classification; channel fairseq 13B better without demonstrations).
- **§4.2.** Fraction of correct labels: largely insensitive; all-incorrect
  labels preserve 92%, 100% and 97% of the gain for three of four
  settings; GPT-J classification drops nearly 10 points with all labels
  wrong but still beats no demonstrations. The gold–random gap stays at
  0.8–1.6% for k from 4 to 32, and accuracy barely rises past k = 8.
  Manual templates do not change the trend.
- **§5.1.** OOD inputs with random labels: 3–16 point drops for channel
  MetaICL and both GPT-J variants; direct GPT-J on multi-choice falls
  below no demonstrations; direct MetaICL is the exception.
- **§5.2.** Random English words as labels: 5–16 point drops for direct
  models; 0–2 points, sometimes a gain, for channel models.
- **§5.3.** No labels or no inputs (format removed) is close to or worse
  than no demonstrations. With format kept: direct MetaICL retains 95% and
  82% of the gain with only the inputs' format paired to the label set, or
  vice versa; channel models retain 82%, 87%, 86% and 75% pairing real
  inputs with random English words.
- **§5.4.** Meta-trained MetaICL shows the strongest version of every
  trend: almost no effect of the mapping, near none of the input
  distribution (direct) or label space (channel), most effect of format.
- **Appendix C.** Labels drawn from the true label distribution narrow the
  gap further; a constant label ("answer") or repeating the test input as
  every demonstration input does worse, which the authors attribute to
  changing the format.
- **Limitations (authors').** Gaps are dataset-dependent, up to about 14
  points (financial_phrasebank with GPT-J); Kim et al. (2022) find negated
  labels hurt substantially; synthetic tasks may use labels more.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For these tasks and models, correct input-label pairing contributes little to in-context gains | strong (for the tested regime) | §4.1–4.2, 12 model–method pairs, 26 datasets |
| C2 | Input distribution, label space and format each contribute substantially | moderate | §5.1–5.3, ablations on 9 datasets and 4 model–method pairs |
| C3 | Keeping the paired format lets inputs alone or labels alone retain most of the gain | moderate | §5.3 percentages |
| C4 | Meta-training for in-context learning makes models rely on format and ignore the mapping | moderate | §5.4, one meta-trained model |
| C5 | The models do not learn new input-label correspondences at test time | weak (interpretive) | §6, inferred from C1; not tested on tasks whose correspondence is absent from pretraining |
| C6 | The result holds for generation tasks | not supported | stated as future work |

## Concepts

- **demonstrations**: k input-label pairs concatenated before the test
  input.
- **direct / channel**: modelling P(y | x) versus P(x | y).
- **input-label mapping**: whether each x_i is paired with its correct
  y_i.
- **format**: the use of input-label pairs as the sequence's structure.
- **meta-training**: training with an in-context objective over many
  tasks (MetaICL).
- **learning (strict / broad)**: the authors distinguish capturing the
  input-label correspondence (strict, which they say does not happen) from
  adapting to the input and label distributions and the format (broad,
  which does).

## Connections

It cites Xie et al.'s Bayesian account (LIT-tmp6trip) as the theory of
how demonstrations "recover latent concepts" and supplies measurements of
what does the recovering: on a latent-concept reading, inputs, label space
and format are evidence about the task, and the mapping is evidence the
model can do without. Webson and Pavlick (2022) find the analogous result
for instructions, which the authors connect. Lu et al. (LIT-tmpthf7j) show
that the order of the same demonstrations can swing accuracy widely, which
is a different axis from what this paper ablates.

## Bearing on the record

- No THEORY here holds a claim about what a context contributes to a
  fixed model's interpretation. I file none: the result is an aggregate
  over benchmark tasks with a stated exception list, and its strongest
  form (C5) is the authors' interpretation.
- What it establishes, on its own terms: the effect of a context on a
  fixed model is mostly carried by features that specify a frame (what
  inputs, what outputs, what form) rather than by the content of the
  examples. Which features act depends on the inference method (direct vs
  channel), so the same context does different work for different
  read-outs of the same model.
- No instruction for machine-learning practice is drawn here
  (`anthology-candidate`).

## Limitations

- Classification and multi-choice only; generation is untested.
- Macro-averages hide dataset variation, which the authors document (up
  to ~14 points).
- Random labels are drawn from the correct label set, so the label space
  is always given; "labels don't matter" means "which label goes with
  which input doesn't matter much".
- The ablations of §5 use four model–method pairs and nine datasets, not
  the full twelve and twenty-six.
- Later work (Kim et al. 2022, cited) qualifies the finding for negated
  labels.

## Open questions

- Does the gold–random gap open on tasks whose input-label correspondence
  cannot have been learned in pretraining? The authors predict it should,
  and that in-context learning would then fail.
- Is the separation into four factors stable across scale beyond the
  models tested, or does a large enough model start to use the mapping?
