---
number: 970
status: Active
formerly:
- THEORY-tmp77xju
title: 'On three language-model tasks whose circuits earlier manual work reported, indirect object identification and Greater-Than in GPT-2 Small and Python docstrings in a four-layer attention-only model, ACDC run with resampled corrupted activations against KL divergence ranked the reported edges with areas under the ROC curve of 0.85 to 0.98, above head-importance pruning and subnetwork probing on all three; on two compiled tracr programs it ranked them poorly with corrupted activations, 0.68 and 0.20, and exactly with zero activations'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1170, the reading of Conmy et al. (2023) in
    full. One study, the title claims no more than its Tables 2 and 3
    report, and nothing in the record contradicts it (ADR-047 v3).
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1547
summary: >-
  Conmy et al. (2023), [LIT-1547](../literature.d/LIT-1547.md), read in [NOTE-1170](../notes.d/NOTE-1170.md). Edge AUCs with
  corrupted activations and KL: Docstring 0.982, Greater-Than 0.853, IOI
  0.869 for ACDC, against 0.805, 0.693, 0.789 for HISP and 0.937, 0.806,
  0.823 for SP. It does not say ACDC finds the true circuit: the reported
  circuits are incomplete, the results depend on metric, ablation and
  parent order, and negative components are missed at sparse thresholds.
---
<!-- inactive-ok-file: THEORY-997 — Proposed; a neighbouring account on circuits compared across fine-tuning, cited as open -->

# THEORY-970: On three language-model tasks whose circuits earlier manual work reported, indirect object identification and Greater-Than in GPT-2 Small and Python docstrings in a four-layer attention-only model, ACDC run with resampled corrupted activations against KL divergence ranked the reported edges with areas under the ROC curve of 0.85 to 0.98, above head-importance pruning and subnetwork probing on all three; on two compiled tracr programs it ranked them poorly with corrupted activations, 0.68 and 0.20, and exactly with zero activations

## Source

Conmy, Mavor-Parker, Lynch, Heimersheim and Garriga-Alonso (2023),
*Towards automated circuit discovery for mechanistic interpretability*,
NeurIPS 2023, [LIT-1547](../literature.d/LIT-1547.md), read in full in [NOTE-1170](../notes.d/NOTE-1170.md): §§3–4,
Appendices C–J, Tables 2 and 3.

## What was actually shown

**The method.** ACDC visits the nodes of a fixed computational graph from
the output back and, for each incoming edge, removes it if replacing it by
its value on a corrupted prompt raises the KL divergence from the full
model by less than τ. Sweeping τ gives an ROC curve against the edges of a
circuit reported by earlier work.

**The comparison** (Table 2, corrupted activations, edge level):

| task | ACDC | HISP | SP | metric |
|---|---|---|---|---|
| Docstring | 0.982 | 0.805 | 0.937 | KL |
| Greater-Than | 0.853 | 0.693 | 0.806 | KL |
| IOI | 0.869 | 0.789 | 0.823 | KL |
| tracr-xproportion | 0.679 | 0.679 | 0.525 | L2 |
| tracr-reverse | 0.200 | 0.577 | 0.193 | L2 |

With zero activations (Table 3) ACDC scores 1.000 on both tracr programs.

**What could have come out otherwise.** A gradient-based mask (SP) or a
first-order score (HISP) could have ranked the reported edges better than
greedy patching on the language-model tasks; neither did.

## What this does not say

- **Not that ACDC finds the circuit.** The ground truths are partial: the
  reported IOI circuit reaches a logit difference of 3.24 against the
  model's 4.11, and the Greater-Than circuit 72% against 84%.
- **Not robust across choices.** Optimizing the task metric instead of KL
  drops ACDC's edge AUC to 0.461 on Greater-Than and 0.589 on IOI; zero
  activations make Docstring far worse; parent order mattered on
  induction.
- **Not that ACDC is best on tracr.** The paper's §4.1 says ACDC leads on
  tracr-reverse; Table 2 gives 0.200 against HISP's 0.577 with corrupted
  activations ([NOTE-1170](../notes.d/NOTE-1170.md), Limitations).
- **Not complete.** At sparse thresholds negative name movers are missed,
  and an OR gate keeps one input ([THEORY-966](THEORY-966.md)).
- **Not about later methods.** Edge attribution patching, which later
  work reports as better, is not compared here.

## Connections

- **[THEORY-997](THEORY-997.md).** Circuits compared across fine-tuning are found with
  this family of methods; their dependence on threshold, metric and order
  is a reason a changed circuit need not be a changed model.
- **[QUESTION-275](../questions.d/QUESTION-275.md).** A circuit-only measurement that could be run at
  every checkpoint of a small model, with those choices held fixed.
