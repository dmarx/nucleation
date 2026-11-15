---
status: Proposed
promote_when: >-
  An independent measurement, on checkpoints the authors did not choose,
  that (1) under plain addition the leading singular values of the merged
  layer update exceed the projection-optimal magnitudes by more where
  tasks' responses overlap positively along those directions, and (2)
  rescaling them by the measured overlap, directions unchanged, recovers
  merged accuracy over task arithmetic on vision and language benchmarks.
  It is refuted if rescaling the same singular values by a uniform factor,
  ignoring the measured overlap, recovers as much, since then the gain is
  a norm correction and not the over-counting of shared directions.
title: 'Li et al.: when the layer updates of tasks fine-tuned from one pretrained start share singular directions in the layer''s output space, adding them counts the shared component more than once and inflates the merged update''s leading singular values; rescaling those values by the measured overlap, leaving directions and signs unchanged, raised task arithmetic''s accuracy by 7 to 19 points on CLIP ViT benchmarks and improved other merging methods on vision and language benchmarks'
version: 1
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpzk5vb
summary: >-
  Li et al. (2026), LIT-tmpzk5vb, read in NOTE-tmpe9zlx. A projection
  analysis under plain addition (Lemma 3.2, Theorem 3.3) shows positive
  cross-task overlap inflating merged singular values, with the largest
  overlaps in the top subspaces. Singular Value Calibration lifts task
  arithmetic from 68.9 to 81.9 on ViT-B/32 with 8 tasks, above TIES's 72.6
  in the same runs, and improves TIES, DARE and TSV-M, the last by under
  a point. A rival diagnosis to sign conflict, THEORY-107. The wording is
  the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmpzk5vb NOTE-tmpe9zlx THEORY-107 THEORY-tmp6ikb6 — new tmp codes, or Proposed; source, reading and neighbouring accounts, named and not leaned on -->

# THEORY-tmpqv3ve: Li et al.: when the layer updates of tasks fine-tuned from one pretrained start share singular directions in the layer's output space, adding them counts the shared component more than once and inflates the merged update's leading singular values; rescaling those values by the measured overlap, leaving directions and signs unchanged, raised task arithmetic's accuracy by 7 to 19 points on CLIP ViT benchmarks and improved other merging methods on vision and language benchmarks

## Source

Li, Peng, Zhang, Guo, Duan & Shi (2026), LIT-tmpzk5vb, read in
NOTE-tmpe9zlx: §§1–6, Lemma 3.2 and Theorem 3.3 as stated.

## The result

- **The mechanism** (§3.2): project each task's update onto the merged
  update's left singular vector u^r. Its coefficient is
  s_i^r = 1 + Σ_{j≠i}⟨a_j^r, a_i^r⟩/‖a_i^r‖². Positive cross terms give
  s_i^r > 1: the merged response over-counts what the tasks share. For two
  identical aligned responses s = 2, the "counts it twice" of A's
  paraphrase.
- **Where it sits** (Theorem 3.3, Figs. 2–3): the inflation is largest in
  the leading subspaces.
- **The correction** (Tables 1–2): rescaling the merged singular values,
  directions untouched, lifts task arithmetic by 7.0 to 19.0 points on CLIP
  ViTs, and improves TIES, DARE, Iso-C, Iso-CTS and, slightly, TSV-M. It
  also lifts task arithmetic on BERT, T5, T0 with (IA)³ and Llama-2-7B.
- **The side matters** (Table 3): calibrating on the input side instead
  often removes the gain.

## What it does not show

- **That over-counting is what the rescaling corrects.** No control
  rescales the same singular values uniformly. A norm correction alone
  might do much of the work.
- **That the shared directions are useful.** The paper calls them shared
  knowledge, and some subspaces are under-accumulated.
- **Anything beyond plain addition, in theory.** Other methods are handled
  empirically, and each layer is treated as a linear operator.
- **An oracle-sign comparison.** It beats TIES (THEORY-107) without sign
  election, but does not test the oracle signs TIES's own evidence rests
  on.
- **Independent numbers.** Every baseline is the authors' rerun, and some
  14-task baselines sit below the pretrained model. Its gain on TSV-M
  (THEORY-tmp6ikb6) is under a point, consistent with that method having
  already removed much of the overlap.
