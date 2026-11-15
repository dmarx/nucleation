---
status: Read
paper: 'LIT-tmpmqgjz'
title: 'Ilharco et al. — Editing models with task arithmetic'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2212.04089v3 (31 March 2023), from
    https://arxiv.org/pdf/2212.04089v3, text by pdftotext: §§1–7 in full
    and Appendix A (loss landscape, weight averaging and ensembles).
    Table captions of Appendices B–E skimmed; the per-task appendix
    tables, the detail of the analogies appendix and the references were
    skipped. Every quote below was rechecked by the filer against the
    downloaded text.
date: '2026-11-15'
summary: >-
  Task vectors, fine-tuned minus pretrained weights, edit a model by
  arithmetic: negation forgets a task with little loss on a control,
  addition builds a multi-task model (91.2% normalized for eight image
  tasks), and analogies transfer to a fourth task without its labels.
  CLIP, GPT-2 and T5, one pretrained start, λ tuned on validation data.
  The paper's claim that near-orthogonality enables addition is
  speculation; App. A finds a two-model weight average tracks the logit
  ensemble (r = 0.99).
---
<!-- inactive-ok-file: THEORY-107 THEORY-828 CLAIM-498 — Proposed or new tmp codes; named as accounts this reading bears on, not leaned on -->

# NOTE-tmphnptf: Ilharco et al. — Editing models with task arithmetic

## Contribution

Names and systematises arithmetic on weight differences from one
pretrained start as a way to edit models. A task vector is
τ = θ_ft − θ_pre, and an edit is θ_new = θ + λτ, with λ chosen on held-out
validation data. Three operations: negation, addition and analogy.

## Key insight

Within one pretrained start, the weight change that fine-tuning makes on a
task behaves, to a useful approximation, like a separable ingredient:
removing it removes the skill, and adding several gives the skills
together.

## Assumptions

One pretrained start and architecture. Heads that need no new parameters
(open-vocabulary CLIP, text-to-text T5). λ tuned on validation data for
each operation.

## Key results

- **Negation, images** (§3.1, Table 1): "negative task vectors decrease the
  average target accuracy of ViT-L/14 by 45.8 percentage points with
  little change in accuracy on the control task" (target 64.8 → 19.0;
  ImageNet 75.5 → 72.9). Random vectors of the same per-layer magnitude do
  little; gradient ascent destroys the control.
- **Negation, text** (§3.2, Table 2): GPT-2 Large toxic generations 4.8% →
  0.8%, WikiText-103 perplexity 16.4 → 16.9.
- **Addition** (§4.1, Figs. 2–3): pairs of tasks reach "98.9% normalized
  accuracy on average"; for all eight tasks, "the best model produced by
  adding task vectors reaches an average performance of 91.2%".
- **Addition for one task** (§4.2, Table 3): adding Hub task vectors to a
  fine-tuned T5-base gains 0.2 to 0.8 points on four GLUE tasks, choosing
  the best of 427 checkpoints on validation data.
- **Analogies** (§5, Table 4): sentiment domain transfer, and sketch and
  photo subpopulations, +3.4 points on average over the pretrained model
  for subpopulations.
- **Similarity** (§6, Fig. 5): "vectors from different tasks are typically
  close to orthogonal, and speculate that this enables the combination of
  task vectors via addition with minimal interference". Cosines 0.01–0.06,
  MNIST–SVHN 0.18.
- **Ensembles** (App. A, Fig. 8): at λ = 0.5, adding two task vectors is
  the weight average. Its accuracy tracks the logit ensemble's "with a
  Pearson correlation of 0.99", the ensemble slightly higher. The authors
  tie this to the NTK regime through Wortsman et al.
- **Learning rate** (§6, Fig. 6): larger rates hurt task vectors more than
  they hurt single models.
- **Stated limit** (§6): "we perform arithmetic operations only on models
  fine-tuned from the same pre-trained initialization".

## Concepts

task vector; task arithmetic; negation (forgetting); addition (multi-task
model); task analogy; normalized accuracy; control task.

## Bearing on the record

- **THEORY-107 (TIES)**: this is the "task arithmetic" baseline TIES
  measures against. It adds no evidence on sign conflict. Its suggestion
  that orthogonality enables addition is the weaker view that a
  coordinate-interference account replaces.
- **QUESTION-318 and CLAIM-498**: App. A is an output-level fact, that a
  two-model weight average tracks the logit ensemble. It says nothing of
  layer features, so it does not answer QUESTION-318. It is consistent
  with CLAIM-498 at the output only.
- **THEORY-112**: the paper names Git Re-Basin as promising for relaxing
  the shared-start limit. It reports no result on it.
- **THEORY-828 and THEORY-105**: every operation here is within the
  weight-space neighbourhood of one pretrained model, the setting those
  accounts describe.
- **A's toy** (reader's check, not the paper's): with f_w(x) = (w·x)²,
  w0 = 0, ΔA = (1, 0), ΔB = (0, 1) and x = (1, 1), the interaction
  f(w0+ΔA+ΔB) − f(w0+ΔA) − f(w0+ΔB) + f(w0) = 4 − 1 − 1 + 0 = 2, though
  ΔA ⟂ ΔB. Orthogonal updates can interact, so orthogonality cannot be the
  whole reason addition works.

## Limitations

An empirical method paper with no mechanism. λ is tuned on validation
data. The single-task T5 gains are small and selected over 427
checkpoints. "Orthogonality enables addition" is speculation.
