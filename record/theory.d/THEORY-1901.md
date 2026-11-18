---
number: 1901
status: Proposed
formerly:
- THEORY-tmprdjn0
promote_when: >-
  Two results, one per clause. The higher singular-subspace overlap
  (SAR) among CLIP encoders fine-tuned on domains of one task than among
  encoders fine-tuned on different tasks is reproduced by an independent
  measurement, on other benchmarks or other CLIP sizes. And an
  independent run of SCORE against TIES and TSV on the leave-one-domain-
  out benchmarks, over several seeds of the experts, keeps SCORE's
  average held-out accuracy ahead by more than seed variation. A test of
  whether overlap causes merge loss would bear on the paper's reading,
  not on the title.
title: 'CLIP image encoders fine-tuned on different domains of one classification task have more overlapping task-matrix singular subspaces than encoders fine-tuned on different tasks, and a data-free merge that projects each task matrix into a shared orthogonal basis and trims outlying off-diagonal couplings generalized to a held-out domain slightly better on average than TIES and TSV across eight benchmarks'
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2636
summary: >-
  Chaves et al. (2026), [LIT-2636](../literature.d/LIT-2636.md), read in [NOTE-1994](../notes.d/NOTE-1994.md). Pairwise
  SAR is 0.61–0.71 among DomainNet domains and 0.41–0.69 among eight
  vision tasks (Fig. 2). SCORE averages 65.69 on ViT-B-32 against 64.95
  for TSV and 64.84 for TIES, and 73.04 on ViT-L-14 against 72.46 for
  TIES (Table 1), with no seeds reported. The paper reads the overlap as
  the cause of conflict; that link is argued, not tested. The wording is
  the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account whose notion of conflict this one differs from -->

# THEORY-1901: CLIP image encoders fine-tuned on different domains of one classification task have more overlapping task-matrix singular subspaces than encoders fine-tuned on different tasks, and a data-free merge that projects each task matrix into a shared orthogonal basis and trims outlying off-diagonal couplings generalized to a held-out domain slightly better on average than TIES and TSV across eight benchmarks

## Source

Chaves et al. (2026), [LIT-2636](../literature.d/LIT-2636.md), read in [NOTE-1994](../notes.d/NOTE-1994.md): §§1–5.2 in
part, Fig. 2, Alg. 1, Table 1.

## The result

- **Overlap** (§3.2, Fig. 2). For eight vision tasks merged from one CLIP
  start, pairwise mean SAR runs 0.41–0.69, highest between related tasks
  (digits; landscapes). Across six DomainNet domains it runs 0.61–0.71.
  The contrast could have gone the other way: same-task, different-domain
  experts might have diverged as much as different tasks.
- **Merge** (§4, Table 1). Leave-one-domain-out over eight benchmarks,
  λ = 1, no target data. SCORE averages 65.69 on ViT-B-32 (TSV 64.95,
  TIES 64.84, Iso-C 61.31, zero-shot 55.63) and 73.04 on ViT-L-14 (TIES
  72.46, TSV 72.14). It beats a logit ensemble of the same experts by
  1.12–1.90 points (§5.2).

## What it does not show

- **That overlap causes the loss.** The paper's reading is that shared
  singular directions interfere; the sections read argue and illustrate
  this, and do not isolate it. Domain experts are merged well, above
  zero-shot and an ensemble, despite having the most overlap.
- **That this "conflict" is TIES's.** Overlap of singular subspaces is not
  sign disagreement per coordinate ([THEORY-107](THEORY-107.md)), and neither is the
  activation cross-term of a merge. The record should not fold them into
  one notion of interference.
- **A reliable margin.** SCORE's lead is under a point on average, with
  no seeds or intervals, and ranks vary by dataset.
- **Anything about task arithmetic tuned.** At λ = 1 task arithmetic over
  several deltas collapses below zero-shot (DomainNet 5.40 on ViT-B-32);
  that is a scale effect of an untuned λ, not a finding about its
  geometry.
- **Other modalities.** Image classification and CLIP only.
