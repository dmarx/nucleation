---
status: Read
paper: LIT-tmplf4p3
title: 'Maennel and colleagues — What Do Neural Networks Learn When Trained With Random Labels?'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2006.10455v2 (PDF,
    11 Nov 2020); seven authors, not six as the search listed: §§1–4 and
    appendices A, B, E and F closely; C and D skimmed; figures from
    captions. Running notes on the branch claude/readers/task-composition
    (ADR-108). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Random-label pretraining speeds or slows later training: the gain lives
  in first-layer second-order statistics (shown by covariance resampling),
  the loss in inactive later units. Lesson for any memorization arm:
  control for input statistics and weight scale.
---
<!-- inactive-ok-file: CLAIM-756 CLAIM-758 THEORY-2075 — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpmkl72: Maennel and colleagues — What Do Neural Networks Learn When Trained With Random Labels?

## Key results

1. **Both signs.** Pretrained networks "train faster downstream compared to
   train-" ing from scratch (abstract); in another setting "a negative
   effect can be observed downstream: training" "becomes slower" (§1.1).
2. **Scale controlled.** "we re-scale the weights of the network after
   pre-training to match their `2 norms at initialization" (§1.1).
3. **Alignment.** "the principal components of weights at the first layer
   are aligned with the principal components of data" (§1.1).
4. **Intervention.** "Randomly initializing the convolutional filters from
   a learned covariance reproduces the effect of pre-training within
   measurement error" (Fig. 5); "the positive transfer is mainly due to the
   second-order statistics of the weights in the first layer" (§2.4).
   Wrong eigenvectors reverse the gain (Tables 5–6).
5. **Reversal mechanism.** "neural activations at the later layers can drop
   abruptly and permanently once the switch to the downstream task takes
   place"; "increasing the width can indeed mitigate the negative transfer
   effect" (§3).
6. **Generality qualified.** On one ImageNet setting, "this time we do not
   observe the positive transfer with architectures other than ResNet18"
   (App. B), and ResNet18 was not rescaled.

## Bearing on the record

- **[LEAD-006](../leads.d/LEAD-006.md)**, qualifies its memorization arm: a first stage with no
  task information still lowers (or raises) later cost through input
  statistics, so a memorizer needs covariance-matched and norm-rescaled
  controls before a saving is credited to or against a learned g. Runs (a)
  as training curves and part of (c) by substitution; not (b): first-stage
  accuracy is never reported.
- **[CLAIM-756](../claims.d/CLAIM-756.md)**, weak independent support for the premise: a step with no
  direct value on the later task often lowers its cost; not netted, sign
  depends on settings.
- **[CLAIM-596](../claims.d/CLAIM-596.md)** and **[QUESTION-397](../questions.d/QUESTION-397.md)**, parallel: a rate, not a yield, and
  rescaling and resampling separate a weight-scale route from an alignment
  route; final test accuracy moves opposite to speed.
- **[CLAIM-758](../claims.d/CLAIM-758.md)**, a candidate mechanism, not the signature: inactive units
  after the switch reduce later capacity; no time course.
- **[THEORY-279](../theory.d/THEORY-279.md)**, independent support: early layers lock onto second-order
  input statistics even with random labels.
- **[THEORY-2027](../theory.d/THEORY-2027.md)** and **[THEORY-1353](../theory.d/THEORY-1353.md)**, parallel: inactive units cut
  plasticity, and width helps.
- **[THEORY-2075](../theory.d/THEORY-2075.md)**, complement: shuffled weights remove a saving there;
  covariance-resampled weights keep it here.
- **[TERM-117](../terms.d/TERM-117.md)**, analogy: a nucleus that helps or hurts by setting.

## Limitations

First-stage accuracy unreported; cost as area under the training curve;
few seeds in several figures; same dataset upstream and downstream; the
negative mechanism correlational except width; a learning-rate
inconsistency between appendices.
