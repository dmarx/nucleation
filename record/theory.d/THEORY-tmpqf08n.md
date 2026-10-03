---
status: Proposed
promote_when: >-
  A dose–response test in which only the shared structure varies. Fix a
  trained, stable start and an architecture. Train a second objective
  from that start whose overlap with the first is varied by a measured
  amount: the fraction of shared classes, label noise, or input shift.
  Measure the barrier in the earlier objective's loss above the mean of
  the endpoints, not raw loss. That removes the forgetting the endpoint
  already carries. Do it on more than MNIST-scale tasks and include a
  control with the same objective and only the SGD noise changed. It is
  supported if the barrier rises monotonically as overlap falls and the
  control shows none. It is refuted by objectives with little measured
  overlap that stay linearly connected from a stable start, or by a
  barrier between runs of one objective from a stable start. The
  federated case would test this if run from a pretrained start with an
  IID control. More cases of continual learning forgetting along a line
  will not settle it, because the continual endpoint's own loss on the
  earlier task explains most of the rise.
title: 'Linear connectivity from a shared, already-stable start holds only when the objectives the runs optimise share structure, and breaks as that structure is removed'
version: 1
tags:
- loss-landscapes
- information-geometry
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmp2e9aa
- LIT-tmp9gt28
- LIT-tmpz6gcm
summary: >-
  Mirzadeh et al. (2020), [LIT-tmp2e9aa](../literature.d/LIT-tmp2e9aa.md): from a task-1 solution, a model
  trained on tasks 1 and 2 together stays on a low task-1 loss line from
  the start, and one trained on task 2 alone does not. Adding noise to
  task 2's inputs, corrupting its labels, or removing classes separates
  the solutions progressively. The authors explain it by curvature: the
  multitask direction avoids the earlier task's top Hessian eigenvectors.
  Gueta et al. (2023), [LIT-tmp9gt28](../literature.d/LIT-tmp9gt28.md): fine-tuning runs from one pretrained
  model are linearly connected within a dataset and a task family. Wen et
  al. (2023), [LIT-tmpz6gcm](../literature.d/LIT-tmpz6gcm.md): in class-incremental learning the line between
  adjacent continual minima crosses a ridge in the old tasks' loss. Limits:
  much of the measured breakage is forgetting at the endpoint, not a
  barrier, and FedAvg models from one random start under one global
  objective are separated by a barrier that grows with heterogeneity.
extended_by:
- THEORY-tmp5fzhc
---
<!-- inactive-ok-file: LIT-tmpqno1r — Proposed; Li et al. on GNNs, named as a limit on scope, not leaned on -->
<!-- inactive-ok-file: THEORY-tmp5fzhc THEORY-tmpn2rg2 — Proposed; an account that carries this one further and a sibling on the stable start, named in Connections, nothing here rests on them -->

# THEORY-tmpqf08n: Linear connectivity from a shared, already-stable start holds only when the objectives the runs optimise share structure, and breaks as that structure is removed

## Source

- Mirzadeh, Farajtabar, Gorur, Pascanu & Ghasemzadeh (2020), [LIT-tmp2e9aa](../literature.d/LIT-tmp2e9aa.md),
  read in [NOTE-tmp6vg74](../notes.d/NOTE-tmp6vg74.md): §§2–3, Figs. 2–5, Appendix B (Figs. 8–11).
- Gueta, Venezian, Raffel, Slonim, Katz & Choshen (2023), [LIT-tmp9gt28](../literature.d/LIT-tmp9gt28.md),
  read in [NOTE-tmp3gtyn](../notes.d/NOTE-tmp3gtyn.md): §§4–5, Appendix B.
- Wen, Cheng, Qiu, Wang, Pan & Li (2023), [LIT-tmpz6gcm](../literature.d/LIT-tmpz6gcm.md), read in
  [NOTE-tmpa1auh](../notes.d/NOTE-tmpa1auh.md): §3.1, Fig. 2, Fig. 9.

## The claim

Two runs start from the same point and train on two objectives. The claim
is that the line between their solutions stays in the low-loss region of
both only if the objectives share structure. "Shared structure" is
Mirzadeh et al.'s phrase (App. B.2): the second objective has solutions in
the neighbourhood of the first one's, reachable through directions in
which the first objective's loss is flat. The start must already be
stable. Frankle et al. ([LIT-tmp3owu9](../literature.d/LIT-tmp3owu9.md)) showed that copies of one network
started from random initialisation, with different SGD noise, are not
linearly connected on CIFAR-10 or ImageNet; only after early training are
they. So a shared random start is not a shared start in this sense, even
for one objective.

## What was actually shown

**The connected case.** Mirzadeh et al. trained task 1 to a solution ŵ₁,
then trained from ŵ₁ in two ways: on task 2 alone (continual, ŵ₂) and on
tasks 1 and 2 together (multitask, w*₂). Task 1's loss stays low on the
line from ŵ₁ to w*₂, and on lines to later multitask solutions up to w*₅,
but rises on the line to ŵ₂ ([LIT-tmp2e9aa](../literature.d/LIT-tmp2e9aa.md), Figs. 3–4; Rotated MNIST and
Split CIFAR-100). The direction to w*₂ is nearly orthogonal to all 50 top
Hessian eigenvectors of task 1; the direction to ŵ₂ lies in their span
(Fig. 5, Rotated MNIST, an MLP). Euclidean distance and CKA do not
separate the two: ŵ₅ is nearer ŵ₁ than w*₅ is (Fig. 2). Gueta et al.
([LIT-tmp9gt28](../literature.d/LIT-tmp9gt28.md)) found the same at the scale of pretrained language models.
RoBERTa-base runs fine-tuned on one dataset, or on one task family, are
joined by low-loss lines, and their task vectors cluster by dataset (98%
over 280 models) and by family (90%).

**The breaking cases.** Mirzadeh et al.'s Appendix B removes the shared
structure step by step. They used MNIST followed by Fashion-MNIST.
Gaussian noise of growing mean on task 2's inputs, and 5% then 10%
corruption of its labels, separate w*₂ from ŵ₂ progressively in task 2's
loss (Figs. 9–10). Removing 2 then 4 classes from the multitask run's
task-1 data raises task 1's loss on the line from ŵ₁ to w*₂ (Fig. 11).
The authors call that case "very trivial". Starting the multitask run
from a different point puts a wall between it and ŵ₁ on CIFAR-100, though
not on MNIST (Fig. 8). In class-incremental learning, where each task
brings classes the others lack, Wen et al. ([LIT-tmpz6gcm](../literature.d/LIT-tmpz6gcm.md)) found an
interval of the line between adjacent continual minima of PODNet in which
old-task accuracy collapses for the first increment. For later
increments, the new minimum itself sits on the old tasks' high-loss
ridge (Fig. 2, Fig. 9; CIFAR-100, 10 seeds).

## What this does not say

- **Most of the breakage is forgetting, not a barrier.** Mirzadeh et al.
  plot raw loss along the line, not loss above the mean of the
  endpoints. A continual solution, or a multitask solution trained
  without some classes, already has high loss on what it was not trained
  on. The line to it rises because its endpoint does. Wen et al.'s later
  increments show the same thing: the new minimum is the point on the
  ridge. The evidence that the line between connected solutions has no
  barrier is strong. The evidence that losing structure creates a barrier
  between them is much thinner than the plots suggest.
- **"Shared structure" is not measured.** It is varied by manipulations
  (noise, corruption, removed classes, disjoint classes), never quantified.
  Gueta et al.'s broadest level, models fine-tuned on 12 different GLUE
  datasets, is still a low-loss region when probed ([LIT-tmp9gt28](../literature.d/LIT-tmp9gt28.md), §5.2).
  So "shared structure" can be as broad as "English classification", and
  the claim is only as sharp as that word.
- **The curvature account is shown once.** The Hessian evidence is one
  benchmark, an MLP, after 5 epochs. With 20 epochs neither direction lies
  in the top subspace, yet only the continual one forgets (Fig. 5c).
  Low curvature along the path is therefore not sufficient by itself.
- **The objective is not the only thing that matters.** Zhou et al.
  ([LIT-tmphcmq5](../literature.d/LIT-tmphcmq5.md)) trained FedAvg global models from one initialisation, all
  minimising the same global objective, with client data partitioned at
  different heterogeneity. The models are separated by a barrier on the
  line, with an accuracy drop of about 10%, a barrier that grows with
  heterogeneity and over rounds, and they are joined by a one-bend chain (Figs. 5–7). That
  start was random, which Frankle et al. already predict is unstable for
  VGG on CIFAR-10, and no IID control is reported, so the case does not
  refute the claim. But the barrier grows with heterogeneity under a fixed
  objective. So how the objective is optimised, and not only what it is,
  moves the barrier. A pretrained start narrowed the gap between line and
  chain (App. A-A, Fig. 11), as the stable-start clause expects.
- **It says nothing about runs from different starts.** Li et al.
  ([LIT-tmpqno1r](../literature.d/LIT-tmpqno1r.md), Proposed) find that the linear barrier between GCNs
  trained from different seeds on one graph depends on the graph's
  density, feature separability and homophily. That is a claim about data
  structure setting the barrier for a single objective without a shared
  start, outside this account's scope. Its proofs are missing.

## Connections

- **[THEORY-tmpn2rg2](THEORY-tmpn2rg2.md)**, filed alongside this one, is the account of the
  stable start this one presupposes: copies trained from a shared state
  become linearly connected only after early training. This account
  starts where that one ends, and asks what a second objective does to
  that connection.
- **[THEORY-tmp5fzhc](THEORY-tmp5fzhc.md)** carries this further for fine-tuning from one
  pretrained model, from a line between two runs to a region spanned by
  many, with the shared structure graded by dataset, task family and
  general language classification.
