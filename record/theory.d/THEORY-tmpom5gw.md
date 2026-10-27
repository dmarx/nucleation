---
status: Active
title: 'In GPT-2 XL, for 1000 facts the model knows, restoring single clean hidden states into a run whose subject tokens were noised recovers the most of the correct object''s probability at two sites, middle layers at the last subject token, where MLP outputs carry most of the effect, and late layers at the last token, where attention does; and a rank-one edit of one middle MLP output matrix keyed on the last subject token inserts counterfactual facts that generalize to paraphrases and spare neighbouring subjects better than the fine-tuning, knowledge-neuron and hypernetwork editors tested, working best at that token and in middle layers'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmp0p8a7, the reading of Meng et al. (2022) in
    full. One study, but the title claims only what it measured, and the
    record holds nothing that contradicts the measurements (ADR-047 v3):
    LIT-968 contradicts the storage inference drawn from them, which is
    the Proposed THEORY-tmpvugrm, not these results. The record recomputed
    Table 4's scores and checked the closed-form update.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmpajpeb
summary: >-
  Meng et al. (2022), [LIT-tmpajpeb](../literature.d/LIT-tmpajpeb.md), read in [NOTE-tmp0p8a7](../notes.d/NOTE-tmp0p8a7.md): §§2–3, Tables 1
  and 4, and Appendices A, B and E. Causal traces: ATE 18.6%; the
  mid-layer MLP effect at the last subject token peaks at AIE 6.6% against
  1.6% for attention. CounterFact on GPT-2 XL: ROME's score 89.2 (efficacy
  100.0, paraphrase 96.4, neighbourhood 75.4), next best 66.9. It does not
  say where facts are stored: a rank-one edit with the same output exists
  for any one-dimensional fact patch ([LIT-968](../literature.d/LIT-968.md)).
---
<!-- inactive-ok-file: THEORY-tmpvugrm — Proposed; the storage hypothesis drawn from these results, cited as open -->

# THEORY-tmpom5gw: In GPT-2 XL, for 1000 facts the model knows, restoring single clean hidden states into a run whose subject tokens were noised recovers the most of the correct object's probability at two sites, middle layers at the last subject token, where MLP outputs carry most of the effect, and late layers at the last token, where attention does; and a rank-one edit of one middle MLP output matrix keyed on the last subject token inserts counterfactual facts that generalize to paraphrases and spare neighbouring subjects better than the fine-tuning, knowledge-neuron and hypernetwork editors tested, working best at that token and in middle layers

## Source

Meng, Bau, Andonian and Belinkov (2022), NeurIPS 2022, arXiv:2202.05262,
[LIT-tmpajpeb](../literature.d/LIT-tmpajpeb.md), read in full in [NOTE-tmp0p8a7](../notes.d/NOTE-tmp0p8a7.md).

## What was actually shown

**Causal tracing.** For each of 1000 prompts that GPT-2 XL completes
correctly (mean clean probability 27.0%), Gaussian noise of three
embedding standard deviations is added to the subject tokens (mean
probability 8.47%), and the clean value of one state is restored. Averaged:
ATE 18.6%; the strongest single states at the last subject token around
layer 15; MLP outputs (windows of ten layers) peak there at AIE 6.6%,
attention at 1.6%; attention peaks at the last token in late layers.
Freezing MLPs at their corrupted values removes the effect of low-layer
states at the last subject token, freezing attention does not. Similar
traces in GPT-J, GPT-NeoX and smaller GPT-2s, and under other corruptions.

**Editing.** ROME computes k* (the MLP's activation at the last subject
token, averaged over random prefixes) and v* (optimized to make the layer's
output predict the new object, with a KL term preserving the subject's
other predictions), and inserts the pair by the rank-one least-squares
update. On CounterFact (GPT-2 XL, 7,500 records): S = 89.2 against FT+L
66.9, FT 65.1, MEND 57.9, KE 52.2, KN 35.6; FT's neighbourhood score is
40.4, FT+L's paraphrase score 48.7. On GPT-J (2,000 records): 91.5 against
FT+L 68.7. Swept over layers and tokens, ROME is best at the last subject
token in middle layers; editing late attention reproduces the prompt but
not paraphrases.

**What could have come out otherwise.** Effects could have been diffuse,
or concentrated at the last token only; attention could have dominated
the early site; edits at the traced site could have done no better than
elsewhere; and some baseline could have matched ROME on both
generalization and specificity.

## What this does not say

- **Not where facts are stored.** That inference is [THEORY-tmpvugrm](THEORY-tmpvugrm.md).
  Makelov et al. ([LIT-968](../literature.d/LIT-968.md)) show that a rank-one edit with the same output
  exists for any one-dimensional fact patch in an MLP, and that ROME edits
  are approximated by subspace patches over layers 20–35.
- **Not that single layers matter.** MLP and attention effects are for
  windows of ten layers; single-layer restorations were "generally
  negligible".
- **Not independent of the corruption.** The effect is relative to a
  noised, off-distribution run.
- **Not about other knowledge** (logical, spatial, numerical), or many
  edits at once.

### A number the paper gives two ways

§2.1 puts the strongest single-state effect at "AIE=8.7% at layer 15";
Appendix B.1's figures for the same peak give 15.0% − 8.47% = 6.5%. The
title uses neither.

## Connections

- **[THEORY-282](THEORY-282.md)** (Makelov et al.'s illusion) bears on what these results
  license, not on the results.
- **[THEORY-tmpccb5u](THEORY-tmpccb5u.md).** The IOI circuit leaves MLPs out; here MLPs are the
  decisive site for recall. Both are GPT-2-family models read with
  patching-type interventions.
