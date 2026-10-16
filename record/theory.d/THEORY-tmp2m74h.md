---
status: Active
title: "In trained transformers, zeroing a decile of a weight matrix's singular values does damage that falls monotonically with their size in square matrices, whose random-matrix null reaches zero, but not in rectangular ones, whose null has a positive lower edge: there the smallest decile is never the least damaging and can be among the most"
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-16'
source:
- LIT-856
summary: >-
  Staats, Thamm & Rosenow (2024), [LIT-856](../literature.d/LIT-856.md), read in [NOTE-659](../notes.d/NOTE-659.md). Freshly
  initialised matrices of BERT, Pythia and Llama follow the
  Marchenko–Pastur law; trained ones depart from it above the bulk, and,
  in rectangular matrices only, below it. Zeroing Llama-3 8B's smallest
  Down-Projection decile leaves 2.0% on GSM8K from 43.2%, worse than every
  decile but the largest, while the same decile of the square
  Attention-Output leaves 40.0%. Whether the below-bulk outliers are what
  carries the damage is not tested: the decile mixes them with the lower
  bulk, and overlap with the input's principal directions and ablation
  importance disagree for several matrix types.
---
<!-- inactive-ok-file: LIT-369 THEORY-078 — Proposed; a neighbour in the random-matrix reading of trained weights, and the bulk-edge convention this account qualifies, named and not leaned on -->

# THEORY-tmp2m74h: In trained transformers, zeroing a decile of a weight matrix's singular values does damage that falls monotonically with their size in square matrices, whose random-matrix null reaches zero, but not in rectangular ones, whose null has a positive lower edge: there the smallest decile is never the least damaging and can be among the most

## Source

Staats, Thamm & Rosenow (2024; NeurIPS 2025), [LIT-856](../literature.d/LIT-856.md), read in full in
[NOTE-659](../notes.d/NOTE-659.md).

## What was actually shown

**The null.** For an m × n matrix with i.i.d. zero-mean entries and
q = n/m fixed, singular values fill [ν₋, ν₊] with
ν± = σ̃(1 ± √(1/q)). A square matrix has ν₋ = 0, so learning can push
values out only above the bulk; a rectangular one has ν₋ > 0, so they can
leave at either end. Initialised transformer matrices match the law;
trained ones show outliers above the bulk in all matrix types and below
it in rectangular ones (Fig. 1, Table 3). Below-bulk counts are 2–6.5% of
singular values in the up and down projections.

**The ablation.** One decile of rank-ordered singular values is zeroed in
every matrix of one type, with no refitting. Removing the largest decile
always hurts most. In square matrices damage then decreases monotonically
down the deciles; in rectangular ones the smallest decile outranks some
larger ones, and for the Down-Projection it is second (Fig. 5, Fig. 11).
On Llama-3 8B, GSM8K 3-shot, baseline 43.2%, the Down-Projection deciles 1
to 10 leave 2.0, 30.2, 28.0, 27.1, 26.2, 22.0, 11.0, 15.0, 5.0 and 0.0%;
the smallest decile of Attention-Output leaves 40.0% and of Query 40.3%
(Table 1). On HumanEval the smallest Down-Projection decile leaves 0.0%
(Table 5).

**Fine-tuning order.** In BERT, pruning the smallest decile and then
fine-tuning mostly recovers; fine-tuning and then pruning does not
(Fig. 6, 3σ bands from six runs).

**What could have come out otherwise.** The smallest decile could have
been the cheapest to lose everywhere, as Frobenius-optimal truncation
treats it. In rectangular matrices it was not.

## What this does not say

- **That the below-bulk outliers carry the information.** The smallest
  decile is 10% of the spectrum and the outliers 2–6.5%, so the ablation
  mixes them with lower-bulk values. Ablating exactly the outliers against
  an equal number of lower-bulk values is the test, and it was not run.
- **That departure from the null and importance coincide.** Llama's
  Down-Projection has no lower-end overlap with the input's principal
  directions yet the most damaging smallest decile; Llama's Key and Value
  have hundreds of lower outliers and no lower-end overlap; Attention-Output
  shows no overlap anywhere.
- **That the solvable model is the mechanism.** In a Gaussian
  teacher–student ensemble the loss suppresses noise along a learned
  direction, which can hold a weak signal below the bulk (Section 6). The
  authors say showing this in a real network needs the noise covariance of
  real weights, which needs many training runs. The outlier location is
  quoted from an unpublished thesis.
- **That Eckart and Young is wrong.** The best rank-r Frobenius
  approximation is still the magnitude truncation ([LIT-330](../literature.d/LIT-330.md)). What fails is
  the inference from Frobenius cost to functional cost.
- **That the effect is robust in size.** The perplexity and benchmark
  ablations are single runs; RULER is visibly non-monotone. Removed norm
  is not controlled, which if anything would strengthen the result.

## Connections

- **Eckart and Young ([LIT-330](../literature.d/LIT-330.md), [NOTE-301](../notes.d/NOTE-301.md)).** [NOTE-301](../notes.d/NOTE-301.md) already reads the
  theorem as fixing a truncation of one matrix and nothing more; this is a
  measured case of that limit.
- **[THEORY-078](THEORY-078.md)** cuts the Fisher at the upper bulk edge to keep the
  class-mean span. That convention is one-sided; whether a rectangular
  Gram form has structure below its lower edge is not asked anywhere in
  the record.
- **The random-matrix line.** Martin and Mahoney ([LIT-672](../literature.d/LIT-672.md)), the HTSR
  grokking study ([LIT-369](../literature.d/LIT-369.md)) and Papyan's Hessians ([LIT-617](../literature.d/LIT-617.md), [LIT-619](../literature.d/LIT-619.md)) read the
  upper end of trained spectra; this is the record's first reading of the
  lower end.
- **The anthology** holds the paper as [ANTH-LIT-517](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-517.md), read for
  low-rank-plus-quantisation practice. [NOTE-659](../notes.d/NOTE-659.md) reports that its key
  results state the lower-end overlap more broadly than the paper finds.
