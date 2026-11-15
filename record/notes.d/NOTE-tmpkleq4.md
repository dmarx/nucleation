---
status: Read
paper: 'LIT-tmppnktu'
title: 'Zheng and Wang — FREE-Merging, Fourier filtering of task vectors'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2411.16815v3 (28 July 2025), from
    https://arxiv.org/pdf/2411.16815v3, text by pdftotext: §§1–7 in full,
    the numbers of Tables 1–2, the opening of Appendix B.1–B.2 (the setup
    of Theorem 5.1's proof) and Appendix D.1–D.5. Tables 3–9 were read by
    caption and the main text's summary; D.6–D.8 and the references were
    skipped. Every quote below was rechecked by the filer against the
    downloaded text. One sentence of §6.6, on low-pass filtering, is
    broken across a figure in the extraction and is paraphrased, not
    quoted.
date: '2026-11-15'
summary: >-
  Task vectors of each weight matrix, Fourier transformed as 2D signals,
  differ across tasks most in low-frequency amplitude, and the variance
  correlates with worse merges. High-pass filtering each before adding
  (FR-Merging) beats task arithmetic and TIES; routed 1% experts add more.
  The frequencies run over the arbitrary row and column order of a weight
  matrix and change under a function-preserving permutation of hidden
  units, which the paper does not address. Filtering and rescaling are not
  separated.
---
<!-- inactive-ok-file: THEORY-107 — Proposed or new tmp codes; named as entries this reading bears on, not leaned on -->

# NOTE-tmpkleq4: Zheng and Wang — FREE-Merging, Fourier filtering of task vectors

## Contribution

Claims to be "the first to apply Fourier filtering to neural network
parameters". A frequency-domain diagnosis of task interference. A cheap
backbone merge, FR-Merging: an ideal high-pass filter with cutoff D0 on
each task vector, then a sum with magnitude-based coefficients
λ_i = E(v_i)/Σ_j E(v_j). FREE-Merging adds per-task "experts", the top
~1% of each task vector's entries by magnitude, rescaled and chosen by a
router at inference. A "no free lunch" theorem (Theorem 5.1) for a
single-layer linear MLP.

## Key insight

The authors' insight is that disagreement between tasks' updates shows
most at low index-grid frequencies, so removing those before adding
lowers interference. The reader's is that this is a property of how the
weights are stored, not of what they compute (below).

## Assumptions

One pretrained start. Each weight matrix treated as an image whose row
and column grid has a meaningful spatial frequency. Amplitude difference
taken as the cause of masking "regardless of their directional
relationship" (App. D.1).

## Key results

- **Diagnosis** (§4, Fig. 2a): "task vectors from different fine-tuned
  models also exhibit great misalignment in the frequency domain", shown
  for one ViT-B/32 attention head; "Therefore, task interference in the
  low-frequency part are severe."
- **Correlation** (§4, Fig. 2b; App. D.1, Fig. 6): "a clear negative
  correlation between the variance of amplitude power among models and
  the normalized merging performance" (ViT-B/32 groups; Flan-T5 on GLUE).
- **Other methods do not reduce it** (Table 1): mean amplitude variance,
  task arithmetic 0.059, TIES 0.058, DARE 0.057, PCB 0.056, FR-Merging
  0.045 (ViT-B/32).
- **Filtering** (§5.2, Fig. 3): removing low frequencies costs little on
  a task's own data and helps on other tasks (ViT-B/16, 30 tasks).
- **Merging** (Table 2, 8 image tasks): ViT-B/32 task arithmetic 70.1,
  TIES 73.6, PCB 75.8, FR-Merging 78.1, AdaMerging++ 81.1, EMR 87.7,
  FREE-Merging 89.7, individual 90.5. ViT-L/14 task arithmetic 84.5,
  FR-Merging 88.3, FREE-Merging 93.7, individual 94.2. Gains are also
  reported for RoBERTa, T0-3B with (IA)³, Qwen-14B LoRA, LLaMa2-13B and
  BEiT3 (Tables 4–6, by caption).
- **Ablation** (§6.6, Fig. 5a): low-pass filtering degrades performance
  badly, and band-pass is worse than high-pass. The Eq. 3 coefficients
  give only slight improvements.
- **Landscape** (§6.5, Fig. 4): high-pass filtering "widens the valley in
  the loss landscape" (EuroSAT and DTD).

## Concepts

frequency-domain task interference; amplitude power variance; high-pass
filtering of task vectors (FR-Merging); cutoff frequency D0; lightweight
task experts; router; "no free lunch" in merging.

## The frequencies are over an arbitrary order

This is the reader's observation, checked by the filer; the paper does
not discuss it. The 2D Fourier transform runs over the index grid (i, j)
of a weight matrix. In an MLP or attention layer the order of hidden
units is arbitrary: permuting them, with the matching permutation of the
next layer's inputs, leaves the network's function unchanged, but
reorders the rows and columns of both matrices and so changes their
spectra. **The paper's frequencies are therefore not invariant to
permutations.** They are a property of the storage layout, not of the
computation. Adjacent indices need not be related, and the low-frequency
band near the DC centre mostly carries row and column means and smooth
trends of the layout. The paper's "low-frequency parts capture the global
structure" is an analogy from image processing, not shown for weights.
The text mentions permutation only in citing Git Re-Basin, to say that
linear interpolation often leads to high-loss regions.

Within one pretrained start every fine-tuned model shares the layout, so
a fixed (if arbitrary) order is common to all of them, which may be why
the filter helps. By contrast, the singular values and singular-vector
overlaps of [LIT-tmpbknaa](../literature.d/LIT-tmpbknaa.md) and [LIT-tmpzk5vb](../literature.d/LIT-tmpzk5vb.md) are unchanged by a joint
permutation of units.

## Bearing on the record

- **[THEORY-107](../theory.d/THEORY-107.md) (TIES)**: a rival diagnosis, amplitude mismatch in the 2D
  spectrum, which coordinate methods including TIES are shown not to
  reduce (Table 1). FR-Merging beats TIES on ViT-B/32 (78.1 against
  73.6) without sign election. It also changes magnitudes through λ_i,
  so, like SVC, it does not isolate its mechanism from rescaling.
- **[THEORY-112](../theory.d/THEORY-112.md)**: the method's quantities depend on unit order, which that
  account's alignment results treat as a symmetry to factor out. Within
  one start this is harmless; across independently trained models the
  spectrum would not be defined without alignment first.
- **A's turn**: it does not support "wave mathematics" in a physical
  sense. It is a signal-processing heuristic on weight arrays that works
  empirically.

## Limitations

The interference measure is the authors' definition, supported by a
correlation, and the merge that lowers it most filters it by
construction. The index-grid frequency is not justified. Merging gains
mix the filter with coefficient rescaling. FREE-Merging needs a router
and stored experts, so it is not a static merge. Theorem 5.1 is for a
single-layer linear MLP.
