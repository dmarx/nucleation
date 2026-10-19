---
number: 246
status: Proposed
formerly:
- THEORY-tmp7kkpe
promote_when: >-
  Two kinds of result, one for each weak point. For generality: the same
  comparison, fixed-feature readout of new-class tasks against
  penultimate class separation, in a pretraining setting LIT-1044 did
  not test (a much larger label space, a transformer, or a network
  trained past zero training error), with the inverse relation holding.
  For the mechanism: an intervention that changes within-class spread in
  the last layers with the loss held fixed (or holds it fixed while the
  loss changes) and shows new-class transfer moving with the spread and
  not with the loss. It is refuted if, at matched class separation,
  different losses give clearly different new-class transfer, or if with
  a large and diverse pretraining label space more separation stops
  costing new-class transfer. More losses on ResNet-50 and ImageNet, or
  more same-class shift benchmarks, cannot settle it: the first repeats
  the measured correlation, and the second is a different question.
title: 'Training objectives that tighten the class clusters of a classifier''s last layers buy accuracy on the trained classes and pay for it in new tasks: among ImageNet-trained ResNet-50s, fixed penultimate features with more class separation transfer worse to datasets with other classes, the difference lies in the last few blocks, and fine-tuning removes it'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-14'
source:
- LIT-1044
answers:
- QUESTION-051
summary: >-
  Kornblith, Chen, Lee & Norouzi (2021), [LIT-1044](../literature.d/LIT-1044.md), read in
  [NOTE-762](../notes.d/NOTE-762.md). Across nine objectives for ResNet-50 on ImageNet,
  penultimate class separation R² runs from 0.349 (softmax) to 0.845
  (squared error), Papyan's Tr(Σ_W Σ_B†)/C from 21.2 to 0.33, and mean
  linear transfer to eight new-class datasets falls with R² (Spearman
  ρ = −0.93), from 75.9% to 48.3%. Cosine-softmax temperature raises R²
  from 0.24 to 0.77 and lowers transfer from 76.0% to 58.9%. CKA puts the
  differences in the last third of the network; fine-tuning erases them.
  The cost is for new classes: relearning the training classes, more
  separation helps. Networks early-stopped near 92% training accuracy;
  one dataset; correlational across losses.
---
<!-- inactive-ok-file: THEORY-083 THEORY-104 — Proposed; the statement of collapse it measures short of, the layer-wise account it is set against, and the MSE derivation it touches -->

# THEORY-246: Training objectives that tighten the class clusters of a classifier's last layers buy accuracy on the trained classes and pay for it in new tasks: among ImageNet-trained ResNet-50s, fixed penultimate features with more class separation transfer worse to datasets with other classes, the difference lies in the last few blocks, and fine-tuning removes it

## Source

Kornblith, Chen, Lee & Norouzi (NeurIPS 2021), [LIT-1044](../literature.d/LIT-1044.md), read in
[NOTE-762](../notes.d/NOTE-762.md): §§3.1–3.4 (Tables 1–4, Figures 1–6), Appendices A.1–A.3,
B (Table B.1), C.1–C.2 (Tables C.1, C.2), D.3–D.4, E.1–E.4 (Tables E.1–E.3,
Figure E.4) and F (Table F.1).

## What was actually shown

**The measured relation.** ResNet-50 was trained on ImageNet with nine
objectives, 8 runs each, each tuned and early-stopped on held-out
training data. Seven beat softmax cross-entropy's 77.0% top-1
significantly, by up to 0.9 points (Table 1). Class separation in the
penultimate layer, R² = 1 − (mean within-class cosine distance)/(mean
overall cosine distance), was measured on the training set: softmax
0.349, then label smoothing 0.420, sigmoid 0.427, dropout 0.461, logit
normalization 0.517, extra final-layer L2 0.572, logit penalty 0.601,
cosine softmax 0.641 and squared error 0.845 (Table 3). Linear probes on
the frozen penultimate features were trained for eight datasets whose
classes are mostly not ImageNet's. Mean accuracy fell from 75.9% for
softmax to 65.8% for cosine softmax and 48.3% for squared error, and
across the nine losses it has Spearman ρ = −0.93 (p = 0.002) with R²
(Figure 5a). k-NN readout orders them the same way. This could have come
out the other way. A loss could have bought accuracy with features better
for every task, and transfer would then have risen with ImageNet accuracy.

**One knob.** Within cosine softmax, temperature τ from 0.01 to 0.08
raises R² monotonically from 0.236 to 0.770, and lowers mean linear
transfer from 76.0% to 58.9% (Table 4). Top-1 is flat at 77.5–77.6% from
τ = 0.03, so over that range separation and transfer move while
training-task accuracy does not.

**The collapse measure.** Papyan's Tr(Σ_W Σ_B†)/C, at the same
early-stopped checkpoints, runs from 21.2 for softmax to 0.33 for squared
error (Table E.2), in nearly the same order.

**Where.** Linear CKA between corresponding blocks of networks trained
with different losses stays high up to about block 13 of 16 and
diverges after (Figure 2; Inception v3, Figure B.1). Activation sparsity
differs only in the last stage (Figure 3). Full fine-tuning, which
changes the late layers most (Figure D.3), leaves mean transfer accuracy
at 85.1–86.4% for every loss (Table 2).

**For which tasks.** The cost is for new class partitions. Relearning a
linear head for the 1000 ImageNet classes from 40,000 held-out images,
more separated features do better (Figure 6). On Oxford Pets, 25 of whose
37 classes are ImageNet classes, more separated features tie or win
(Appendix F).

## What this does not say

- **It is not terminal-phase neural collapse.** Every network was
  stopped at its best holdout accuracy, at 91.6–93.6% training accuracy
  (Table C.1). The quantity is relative within-class spread at that
  point. [THEORY-083](THEORY-083.md)'s collapse is its limit, and this says nothing about
  networks trained past zero error.
- **It does not show that separation causes the cost.** Across losses it
  is a correlation of nine points. The temperature sweep is one family,
  and τ changes more than R². No experiment holds R² fixed while changing
  the loss. AutoAugment raises accuracy without raising R² (Table E.3),
  so accuracy does not require separation, but that does not isolate
  separation's effect on transfer.
- **It is not a claim about distribution shift on the same classes.** On
  ImageNet-V2, -A, -Sketch, -R and -C the more separated losses are
  slightly better than softmax (Table C.2). So "worse off-distribution"
  holds for new classes, not for shifted inputs of the trained classes.
  Those are the networks' own heads, not probes.
- **It does not say where in depth the information survives.** Transfer
  is read only from the penultimate layer. That fine-tuning recovers it,
  and that CKA finds earlier blocks alike, suggest the earlier layers
  keep what the top drops. Neither is a readout of those layers.
- **One pretraining set, two architectures.** The authors expect larger,
  richer label spaces might soften the trade or reverse it through class
  overlap (§5).
- **Separation and training accuracy are not monotone.** Squared error
  has the most separation and no significant accuracy gain.

## Connections

- **[QUESTION-051](../questions.d/QUESTION-051.md).** Its second half asks what the structure training
  leaves in the last layers costs for decisions the network was not
  trained on. This answers it in part, by measurement, for new class
  partitions read from the penultimate layer. It does not supply the
  layer-by-layer readout with the layer not chosen on test data that the
  question asks for.
- **[THEORY-083](THEORY-083.md).** This measures the approach to collapse, short of the
  terminal phase, and attaches a cost to it. In this regime softmax is the
  least collapsed of the standard losses (Tr(Σ_W Σ_B†)/C = 21.2, against
  0.33 for squared error). Its separation falls after epoch 32 while the
  others' rise to the end (Figure E.4).
- **[THEORY-104](THEORY-104.md).** The two are often read as one claim, and are not. That
  account compares layers of one network under same-class shift. This
  compares losses at one layer on new classes, and under same-class shift
  the more separated losses here do slightly better. They share the
  location: in both, what the objective changes is in the last few
  layers. Neither tests the other.
- **[THEORY-278](THEORY-278.md).** Squared error collapses the most here, which fits
  a derivation of collapse under MSE, though the loss used (Hui–Belkin
  weighted MSE, κ = 9, M = 60) is not the plain MSE derived there.
- **[LIT-978](../literature.d/LIT-978.md).** The review's one-line report of this paper ("more collapse
  … transfer worse") is accurate for new classes and silent on the
  regime and on same-class shift.
- **Anthology.** Which loss to pretrain with for transfer is ML practice.
  This account claims only the measured relation, and carries the
  candidate flag.
