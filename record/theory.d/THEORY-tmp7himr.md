---
status: Proposed
title: 'Biderman and colleagues release Pythia, eight decoder-only language models from 70M to 12B parameters each trained once on the Pile and once on a deduplicated Pile in one fixed data order, with 154 public checkpoints per model (initialization, ten log-spaced early steps and every 1,000 steps to 143,000) and tools to reconstruct the exact batches seen up to each, and show with it that training order has little effect on memorization and that a link between term frequency and few-shot accuracy appears only late in training and only at 2.8B parameters and above'
version: 1
source:
- LIT-tmpyyhs0
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
promote_when: >-
  The released models and checkpoints are confirmed to match the paper's
  description (sizes, deduplicated copies, checkpoint steps,
  reconstructible data order), and the Poisson fit for memorization and
  the late, size-dependent onset of the term-frequency correlation are
  reproduced from them.
summary: >-
  From the reading of [LIT-tmpyyhs0](../literature.d/LIT-tmpyyhs0.md) in [NOTE-tmpzf8fo](../notes.d/NOTE-tmpzf8fo.md). Biderman, Schoelkopf,
  Anthony, Bradley, O'Brien and others (2023), ICML 2023, arXiv
  2304.01373. Pythia is eight decoder-only language models, 70M to 12B
  parameters, each trained once on the Pile and once on a deduplicated
  Pile (about 1.5 epochs) in one fixed data order, with 154 public
  checkpoints per model (step 0, ten log-spaced early steps, every 1,000
  steps to 143,000) and tools to reconstruct the batches seen up to each;
  one run per size, cosine learning-rate decay to a tenth of peak. Its
  case studies find training order has little effect on memorization and a
  term-frequency effect on few-shot accuracy that appears only late and
  only at 2.8B and above. Here because it is the testbed of [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md),
  whose named models (70M- and 160M-deduped) and checkpoints exist as
  described, and because many THEORY entries use its models without an
  entry for the suite. Read in its NOTE.
---
<!-- inactive-ok-file: CASE-tmphsr99 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmp7himr: Biderman and colleagues release Pythia, eight decoder-only language models from 70M to 12B parameters each trained once on the Pile and once on a deduplicated Pile in one fixed data order, with 154 public checkpoints per model (initialization, ten log-spaced early steps and every 1,000 steps to 143,000) and tools to reconstruct the exact batches seen up to each, and show with it that training order has little effect on memorization and that a link between term frequency and few-shot accuracy appears only late in training and only at 2.8B parameters and above

## The account

Pythia controls what most public model families vary: data, data order, architecture recipe and checkpointing are the same across sizes, and each size is trained on the standard and the deduplicated Pile. Checkpoints are dense (154 per model) and the training batches up to each are reproducible. The case studies use these: resuming the last 7% or 21% of training with pronouns swapped lowers gender-bias scores; memorized sequences occur through training at a constant rate (a Poisson process); and the correlation between term frequency and arithmetic or TriviaQA accuracy emerges after about 65,000 of 143,000 steps in models of 2.8B parameters and more.

## What it does not show

Anything about seed-to-seed variation (one run per configuration); effects separable from the cosine learning-rate schedule when checkpoints are compared; behaviour beyond the Pile, English and 12B parameters; what the suite's later checkpoints can still learn.
