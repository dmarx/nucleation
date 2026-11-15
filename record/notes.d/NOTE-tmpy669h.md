---
status: Read
paper: 'LIT-tmpspkpa'
title: 'Yang, Shi and Liu — Orthogonal Model Merging'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2602.05943v2 (4 November 2026), from
    https://arxiv.org/pdf/2602.05943v2, text by pdftotext: §§1–6, Tables
    1–4 and Figs. 2–4. The appendices (Qwen2.5-3B results, B.3 on the
    number of tasks, the proofs) were skipped. v1, from
    https://arxiv.org/pdf/2602.05943v1, was searched only, for
    "logarithm" and "exponential", with no match in either version. The
    filer rechecked every quotation below against the v2 text; several
    are split across columns and hyphenated in the extraction and were
    matched across the break.
date: '2026-11-15'
summary: >-
  Merges orthogonally finetuned models by mapping each rotation to so(d)
  with the inverse Cayley transform, averaging, and rescaling the average
  to undo the norm lost when conflicting directions cancel. Extends to
  LoRA and full fine-tuning by splitting each update into a Procrustes
  rotation and a residual. On five Llama-3.1-8B OFT experts the
  correction is what lifts the merge (41.01 to 46.25); non-OFT gains are
  small and mixed.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account this reading bears on -->

# NOTE-tmpy669h: Yang, Shi and Liu — Orthogonal Model Merging

## Contribution

A merging method that works in the orthogonal group instead of in
Euclidean weight space. For models adapted by orthogonal finetuning (OFT),
each task's rotation is merged through its Lie-algebra generator with a
magnitude correction. For LoRA and fully fine-tuned models,
Orthogonal-Residual Decoupling extracts a rotation of the base weights by
orthogonal Procrustes and merges the residual with an ordinary method
(task arithmetic, TIES, TSV-M).

## Key insight

Averaging update directions that disagree shrinks the average: what
conflicts cancels. In so(d) this can be undone exactly by rescaling the
mean generator to the mean norm, and that rescaling, not the choice of
geometry, is what the paper's own ablation finds decisive.

## Assumptions

- All models share one base.
- For non-OFT models, part of each update is treated as a rotation R_i of
  W0, found by R = argmin ∥W_ft − RW0∥_F subject to RᵀR = I (Eq. 3).
- The Cayley chart is valid, which needs R to have no eigenvalue −1.
- That preserving hyperspherical energy protects against forgetting is
  taken from prior work, not tested here.

## Key results

- **Motivation** (abstract). Euclidean addition "destroys the intrinsic
  geometric properties of pretrained weights, such as hyperspherical
  energy".
- **The chart** (§3, Eqs. 2 and 5). R = (I + Q)(I − Q)⁻¹; "We then obtain Q
  via the inverse Cayley transform", Q = (R − I)(R + I)⁻¹. No logarithm or
  exponential map appears in either version.
- **Magnitude collapse** (§3.2, Eq. 6). The arithmetic mean of the Q_i "can
  suffer from magnitude collapse due to destructive interference:
  conflicting components cancel out, yielding a merged update with a
  smaller norm". The correction multiplies the mean by
  c = Σ‖Q_i‖/‖ΣQ_i‖.
- **OFT merges** (Table 1, §5.1.2; Llama-3.1-8B, five tasks). OrthoMerge
  averages 46.25, against 44.71 for the task-specific experts and 41.46,
  44.61 and 44.97 for task arithmetic, TIES and TSV-M applied to the OFT
  models. The authors call it "constructive synergy".
- **Ablation** (Table 4). Simple Average R 39.53; Sequential Product R
  40.76; Simple Average Q (Lie algebra, no correction) 41.01; OrthoMerge
  46.25. "our magnitude-corrected averaging scheme is essential".
- **Non-OFT models** (Table 2; MergeBench, Llama-3.2-3B). "+OrthoMerge-G
  improves TA by 1.32%"; "+OrthoMerge-C ... boosts TIES by 2.41%"; TSV-M
  with OrthoMerge-G is −1.49.
- **Where the update goes** (Fig. 4, §5.3). Under Conflict-Aware
  decoupling the orthogonal component "exhibits a minimal norm. This
  implies that the vast majority of update information is preserved
  within the residual component".
- **Spectral norm** (§4). ∥W_merged∥₂ = ∥W0∥₂ "regardless of the number of
  merged tasks", for the pure-rotation case; adding a residual breaks it.

## Concepts

Orthogonal finetuning; the Lie algebra so(d); the Cayley transform;
magnitude collapse; magnitude-corrected merging; orthogonal Procrustes;
orthogonal-residual decoupling; hyperspherical energy.

## Bearing on the record

- **THEORY-107 (interference in parameter coordinates)**: corroborates its
  caution, does not test its account. Table 4 is a second case, beside
  TIES's own ablation, in which handling magnitude matters more than the
  other choices: in so(d), 41.01 without the correction and 46.25 with it.
  The paper's "magnitude collapse" is cancellation of directions in
  so(d), which is coordinate-free, not a sign per coordinate. THEORY-107's
  promote_when (oracle signs against rescaling) is not addressed.
- **THEORY-112 (alignment over symmetries)**: a warning against
  conflation. THEORY-112's orthogonal map on the residual stream is a
  function-preserving symmetry used to align independent networks.
  OrthoMerge's R is the adaptation: R W0 changes what the layer computes.
  Nothing here bears on barriers or alignment.
- **QUESTION-318, CLAIM-498, CLAIM-407**: no bearing; no features are
  measured and nothing is intervened on.

## Connections

- **Zhu (2026), NOTE-tmpsyjfz**, also finds that direction decides the
  causal effect of interference, but in activations, and his "not
  magnitude" concerns a fixed-norm displacement. This paper's correction
  concerns the scale of the merged update. They do not conflict.
- **TIES (LIT-675, NOTE-526)**: a baseline here, and the other ablation
  finding rescaling largest.

## Limitations

- No seeds or error bars in the tables read.
- The OFT experts are the authors' own.
- Non-OFT gains are small and mixed, one negative.
- The "better loss landscape" claim rests on one 2-D picture (Fig. 3).
- Hyperspherical energy is asserted as the mechanism, not measured as a
  mediator.
- The appendices were not read.
