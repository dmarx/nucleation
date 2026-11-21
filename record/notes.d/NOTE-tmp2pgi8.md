---
status: Read
paper: LIT-2966
title: 'Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet — Loss landscape degeneracy and stagewise development in transformers'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    From the arXiv PDF of 2402.02364v3 (1 Aug 2025), 49 pp., header "To
    appear in Transactions on Machine Learning Research (07/2025)",
    fetched 2026-11-21 from arxiv.org without obstacle; the arXiv API
    record was checked (no email sent): published 2024-02-04, comment
    that v1's material on essential dynamics was removed and developed in
    arXiv:2501.17745. Text by pdftotext; page 2 (Fig. 1) rendered to read
    the LLC curves. Read in full: §§1–8, App. A, B, D.2.3–D.2.6, E, F;
    skimmed App. C and D.1–D.2.2 and the references. The TMLR version was
    not fetched or compared; the codebase was not opened. Read by a
    reader subagent; filed by a second one, which rechecked every quote
    and every estimator setting used here against a fresh text
    extraction. No email address sent.
date: '2026-11-21'
summary: >-
  In a two-layer attention-only language transformer and a two-layer
  in-context linear-regression transformer, plateaus of the SGLD estimate
  of the local learning coefficient over log training time divide training
  into five stages each, which recur across seeds and mostly coincide with
  independently measured changes in behaviour and structure. The estimate
  rises in most stages and falls in three, which the singular learning
  process the paper takes as motivation does not explain.
---
<!-- inactive-ok-file: THEORY-tmpr9w2r ARG-tmpfh555 CLAIM-823 CLAIM-834 CLAIM-812 THEORY-967 THEORY-2157 — Proposed or new; the account this reading files and the entries it bears on -->

# NOTE-tmp2pgi8: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet — Loss landscape degeneracy and stagewise development in transformers

## Contribution

1. A stage-division method: stage boundaries at plateaus (critical
   points) of the estimated local learning coefficient (LLC) over log t.
2. Two case studies in which those stages line up with independently
   measured changes in behaviour and structure, with boundaries recurring
   across five seeds.
3. Stages of LLC decrease documented, with candidate mechanisms
   (layer-norm, unembedding, embedding and attention collapse).
4. A practical guide to calibrating SGLD LLC estimation (App. A.5).

## Key insight

The LLC, read over training, pauses between periods of change, and the
pauses fall where the model's computation changes; but the coefficient
goes down as well as up.

## Assumptions

- The Bayesian singular learning process is motivation by analogy: "While
  there are many differences between Bayesian inference and modern neural
  network training, an analogy to the singular learning process informs
  our methodology for stage division" (§2); their general connection
  "remains to be understood" (§5).
- Checkpoints are not local minima of the population loss, "violating the
  theoretical conditions under which the LLC is defined" (A.7); the loss is
  not a negative log likelihood (A.6).
- **Estimator settings** (A.5, Tables 1–2): "it can be advantageous to
  sample at a higher temperature"; "Instead of nβ = n/ log n, we perform
  LLC estimation at nβ = m/ log m, where m is the SGLD batch size". LM:
  nβ = 21.7, γ = 100, ε = 0.001, 20 chains of 200 steps. LR: nβ = 66.7,
  γ = 13.3, ε = 0.0003, 10 chains of 5,000 steps with 1,000 burn-in, batch
  m = 1024 (so the LR nβ is not m/log m ≈ 148). Fixed across checkpoints,
  with SGLD noise seeded identically. No stage division is reported under
  other β or γ.
- Stage boundaries are "sensitive to" checkpoint spacing, smoothing,
  t against log t, and tolerance (B.1).

## Key results

- **Stages** (§5): "We use critical points (that is, plateaus, where the
  first derivative vanishes) in the LLC curve to define stage boundaries";
  the stages are the intervals of change between them.
- **They match development** (abstract): "these changes in degeneracy
  coincide with significant changes in the internal computational
  structure and the input/output behavior of the transformers". LM1
  bigrams; LM2 n-grams and positional embedding; LM3 previous-token heads;
  LM4 induction heads; LR1 context-free prediction; LR2 in-context
  learning; LR3–LR4 loss of out-of-distribution robustness with layer-norm
  collapse; nothing found in LM5 or LR5.
- **Changes per stage** (Fig. 1): LM Δλ̂ = +26.4, +22.5, −1.57, +8.62,
  +1.77; LR Δλ̂ = +21.4, +149, −12.3, −44.1, +3.56.
- **Seeds** (B.4): "In each seed, LLC estimation reveals stage LM1–LM4";
  for LR, LR1–LR5 in each seed.
- **The Hessian misses them** (B.5, LR only): "The Hessian fails to detect
  three of the four stage boundaries identified by our LLC-based
  methodology"; and "the LLC λ does not measure curvature" (A.2).
- **Groundwork** (§6.2): heads later in the induction circuit compose in
  LM2; "the foundations for the induction circuit are laid in advance of
  any measurable change in model outputs or attention patterns".
- **Decreases** (§6.3): "The LLC decreases during LM3, suggesting an
  increase in degeneracy"; for LR3–LR4, layer-norm collapse: "we
  conjecture that this explains part of the striking decrease in estimated
  LLC over these stages" (§7.3). One-layer LM (App. E): a drop, "We did not
  closely investigate why".
- **Decreases unexplained** (§8): the singular learning process's example
  transitions "describe LLC increases ... providing a full theoretical
  account of these stages is an open problem".
- **No causal claim** (§8): future work should be "seeking to establish a
  causal connection between changes in degeneracy and changes in
  structure and behavior"; "We do not claim that the structural and
  behavioral developments we observed in each setting are universal
  phenomena".

## Concepts

- **Local learning coefficient** and its SGLD estimate with localizer γ
  and inverse temperature β.
- **LLC plateau** as stage boundary; **developmental stage** as the
  interval between.
- **Degeneracy against curvature** (A.2).
- **Layer-norm, unembedding, embedding and attention collapse** as sources
  of degeneracy (D.2).

## Connections

The same LM run is the one Wang et al. refine per head (LIT-1535,
NOTE-1188, THEORY-975, THEORY-967). The estimator is Lau et al.'s
(LIT-2995, NOTE-2239, THEORY-2157), here at nβ well below n/log n. The only
empirical precedent cited is Chen et al. (LIT-1894, THEORY-1275).

## Bearing on the record

Filed as THEORY-tmpr9w2r. Dated notes of 2026-11-21 on each entry below,
except CLAIM-834, the owner's U23, whose note is filed with the other
readings of this batch.

- **CLAIM-823** (reading b): supports its weak half, that stages leave
  their mark in local learning coefficients, in two small transformers;
  leaves its strong half, switches of the dominant singular region,
  untested; the decreases qualify it (ARG-tmpfh555).
- **CLAIM-834**: background; both readings must place the decreases;
  nothing bears on reading (a).
- **QUESTION-tmphkb1w**: the decreases, an open problem for the authors,
  filed as a question.
- **CLAIM-812**: leaves open. At nβ ≈ 22 and 67 with fixed γ, the claim's
  formula puts the cut-off curvature at about 4.6 (LM) and 0.2 (LR); a rise
  in λ̂ could be directions stiffening past it.
- **LEAD-207**: the paper dates stages against behaviour without varying β
  or γ.
- **QUESTION-511**: dates stages by the LLC, not by tracking a direction.
- **QUESTION-217**: a single-run coarse-to-fine progression in the LM.
- **QUESTION-039**, **QUESTION-363**, **QUESTION-514**, **NOTE-1188**,
  **THEORY-975**, **THEORY-967**, **THEORY-2157**: notes there.

Nothing here is an instruction for machine-learning practice beyond the
estimator's tuning advice, which concerns measurement.

## Limitations

- One run per setting analysed in depth; five seeds for boundaries only.
  Two small models, one without MLPs.
- Boundaries depend on smoothing, tolerance, spacing and log t (B.1).
- Estimator settings fixed and tuned mostly at the end of training; no
  sensitivity of the stage division to β or γ; estimates away from minima,
  on a non-likelihood loss, at an effective sample size far below n.
- LM5 and LR5 uninterpreted; the Hessian comparison only for LR.
- Correlation, not causation, as the authors say.
