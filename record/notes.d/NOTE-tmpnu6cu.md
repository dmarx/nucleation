---
status: Read
paper: LIT-tmpsnc7a
title: 'Zhang, Lepori and Pavlick — Instilling Inductive Biases with Subnetworks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2310.10899v2 (PDF, 1
    Feb 2024): §§1–4 and 6–8 and appendix B in full; §5 (vision) in full;
    appendices A and C skimmed; Figures 3 and 7 read as images. Running
    notes on the branch claude/readers/task-composition (ADR-108).
    Quotations rechecked by the filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  Subtask induction: find the subnetwork for a shared subtask, transplant
  it frozen, and count disambiguating samples for a target that contains
  the subtask. The located component carries the saving; a size-matched
  random part of the same model does not.
---
<!-- inactive-ok-file: LEAD-tmphfbq0 CLAIM-756 THEORY-tmpk9cmk THEORY-tmpmy98s CLAIM-754 — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpnu6cu: Zhang, Lepori and Pavlick — Instilling Inductive Biases with Subnetworks

## Contribution

A way to plant a located, functionally defined component into a fresh
learner: find a binary mask by continuous sparsification so the masked
model performs a subtask, then "only optimize the randomly initialized
parameters and keep the subnetwork frozen" (§3.2).

## Key results

1. **Design.** First task "T1 := a+ab(mod p)", shared subtask "S1 := ab
   (mod p)", target a² + ab (§4.2); 1000 ambiguous target samples plus 10
   to 10^4 disambiguating ones; four arms: subtask induction, full-model
   transfer, a per-layer size-matched random subnetwork, scratch.
2. **Saving.** "all model configurations trained with Subtask Induction
   achieve near-perfect accuracy with as few as 1000 disambiguation
   training samples", while "models trained from scratch only average
   50.6% test accuracy when trained on the same data" (§4.3).
3. **Against the whole model.** "transferring subnetworks of around 3% to
   7% parameters achieves at least as good generalization accuracy and
   sample efficiency as transferring the entire model" (§4.2).
4. **Against a random part.** "a randomly sampled subnetwork requires on
   average around 6 times as much data in order to reach perfect
   generalization accuracy" (§4.2); a complement-drawn random subnetwork
   behaves the same (App. B.2).
5. **Frozen or not.** For the discovered subnetwork, "freezing and not
   freezing the discovered subnetwork does not have significant
   differences"; a trainable random subset is "likely equivalent to a
   “better initialization”" (App. B.3).
6. **Wrong source.** An a² subnetwork from a model trained on a² + b²
   transfers worse; the authors suggest "models may learn a different
   structure than those needed for the computations the subtask is
   transferred to" (App. B.4).

## Assumptions

A mask that reproduces a subtask's outputs implements it; donor and
recipient share an architecture; embeddings are not transferred.

## Concepts

Subtask induction; subnetwork discovery by continuous sparsification;
frozen transplant; disambiguation samples; inductive bias measured in
samples.

## Bearing on the record

- **LEAD-tmphfbq0**, partial prior research, the closest yet: (a) a later
  sample cost with and without the earlier learning; (c) an intervention
  by transplant with a size-matched control. Not (b): every first-stage
  model is near perfect and no organizations are compared. The target is
  a sum over the shared node, not h applied after g. A ready testbed for
  the missing arms (the reader's suggestion): train first-stage models to
  the same accuracy by different routes, and ablate the subnetwork inside
  them before the target.
- **CLAIM-756**, corroborates in kind: an earlier acquisition lowers a
  later sample cost, and the saving rides on a located component; the
  first stage's cost is not netted.
- **THEORY-tmpk9cmk** (Hu and colleagues), parallel and stronger on
  mechanism: the component alone, with random controls, carries the
  saving.
- **THEORY-tmpmy98s** (procedural pretraining), complementary
  intervention: shuffled weights there, a random same-size part here.
- **CLAIM-754**, weak parallel: arms with equal target accuracy at 10
  samples differ greatly in later cost.
- **CLAIM-596** and **QUESTION-397**, analogy: a reusable component
  against a better initialization.
- **TERM-117**, a clean analogy: an identifiable partial organization that
  improves later accessibility against declared comparators.
- **THEORY-966** and **THEORY-970**, a caution: the mask found may be one
  of several sufficient subnetworks.

## Limitations

Toy scale (p = 7); seeds for one configuration only; checkpoints chosen on
an unambiguous evaluation set in every arm; first-stage cost uncounted; the
composition is additive.
