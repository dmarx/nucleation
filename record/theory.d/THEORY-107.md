---
number: 107
status: Proposed
formerly:
- THEORY-tmp7hwgu
promote_when: >-
  A test that separates sign from scale and from the information a
  multitask model carries. Recover a sign vector for the merge without
  training on all tasks' data, for example from task vectors alone or a
  small, fixed budget of data. If merging with it closes most of the gap
  to multitask training, in more than one PEFT setting and in full
  fine-tuning, the account holds. It is refuted if a merge that only
  rescales and trims, with signs left to plain summation, matches the
  oracle-sign merge, since then the bottleneck is magnitude, not sign. It
  is also refuted if the cost of conflicts does not grow with how
  different the merged tasks are: TIES measures conflicts as frequent
  among checkpoints of one task as across tasks, yet merges of one task
  lose little. More results in which TIES beats task arithmetic would not
  settle it. The method contains trimming, election and rescaling
  together, and the ablation finds rescaling matters most.
title: 'Merging models fine-tuned from one pretrained start loses accuracy through interference in parameter coordinates: redundant small updates dilute the influential ones, and influential updates of different models conflict in sign'
version: 1
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
source:
- LIT-675
summary: >-
  Yadav et al. (2023), [LIT-675](../literature.d/LIT-675.md): keeping only the top 20% of each task
  vector by magnitude loses almost nothing, so most of an update is
  redundant. Among the entries that remain, signs conflict between models,
  more so as more models are merged. Merging (IA)³ models with the
  multitask model's signs reaches 72.0 against 73.1 for multitask
  training and 66.4 for TIES with elected signs. That is the strongest
  evidence that sign is the bottleneck. But the oracle signs come from
  training on every task's data, the ablation finds rescaling and the
  disjoint mean matter more than election, and conflicts are as frequent
  among checkpoints of one task as across tasks.
---
<!-- inactive-ok-file: THEORY-113 THEORY-105 — Proposed; accounts named in Connections, nothing here rests on them -->

# THEORY-107: Merging models fine-tuned from one pretrained start loses accuracy through interference in parameter coordinates: redundant small updates dilute the influential ones, and influential updates of different models conflict in sign

## Source

- Yadav, Tam, Choshen, Raffel & Bansal (2023), [LIT-675](../literature.d/LIT-675.md), read in
  [NOTE-526](../notes.d/NOTE-526.md): §§3–7 and Appendix B, Tables 1, 2, 11 and 12, Figs. 3–4
  and 15.

## What was actually shown

**The setting.** Every merged model is fine-tuned from the same pretrained
weights, so a coordinate means the same thing in each and no alignment is
done. The paper's one landscape premise is that such models "effectively
share a part of the optimization trajectory, and can therefore often be
merged without accounting for permutation symmetry" ([LIT-675](../literature.d/LIT-675.md), §2).
Merging works on task vectors, fine-tuned minus pretrained weights.

**Redundancy.** Keeping only the top 20% of each (IA)³ task vector by
magnitude, and zeroing the rest, matches keeping all of it, averaged over
11 tasks (Fig. 3). Flipping signs of the top 20–30% degrades performance
steadily; flipping the bottom 70–80% has little effect (§7.2). Averaging
the full vectors lets these small entries pull down the influential ones.

**Sign conflicts.** After trimming, the share of parameters whose kept
values disagree in sign across models rises with the number of models
merged (Fig. 4). It is already present for two models from different
tasks. It is as high among 10 public checkpoints of one task as across
tasks (App. B.4, Fig. 15).

**Sign as the bottleneck.** The authors trained an (IA)³ model on all 11
tasks and used its sign vector in place of TIES's election. The merge then
reaches 72.0, against 73.1 for multitask training, 71.4 for the
individually fine-tuned models, and 66.4 for TIES with elected signs
(Table 11, §7.4). Signs estimated from a 32-example multitask run recover
less, 67.7 (Table 2).

**The remedy works, with a validation set.** Trim, elect a sign per
parameter by total mass, and average only the agreeing values. Tuned on
validation data, this beats task arithmetic, Fisher merging and RegMean in
all five settings of Table 1, by 0.7 to 3.6 points. Without validation, on
T5-base, it falls below task arithmetic, 69.7 against 73.2.

## What this does not say

- **The oracle result does not isolate sign.** The oracle sign vector comes
  from a model trained on every task's data. Through the disjoint mean it
  also decides which task's values survive at each coordinate. So it
  carries what joint training learned, not only a direction per
  coordinate. That the merge then nearly matches the multitask model is
  evidence that coordinate-wise merging can get there with the right
  choice per coordinate. It is weaker evidence that conflicting signs are
  what stops it.
- **Election is not the largest step.** Removing it costs 1.4 points on
  T5-base and 1.1 on (IA)³. Removing the rescaling λ costs 2.5 and 5.2,
  and removing the disjoint mean 1.9 and 3.2 (Table 12). Magnitude
  handling matters more than sign handling in the method as built.
- **Conflict frequency does not track cost.** Checkpoints of one task
  conflict as often as models of different tasks. Merges of one task lose
  little, and TIES improves on task arithmetic there by under a point on
  RTE and MRPC. So the account has to say why the same conflict rate
  costs more across tasks, and the paper does not.
- **It is within one pretrained start.** The paper notes merging "relies
  on common initialization and model architecture" (App. A). Nothing is
  said about models without a shared start.
- **Merges stay below the individually fine-tuned models in every setting
  of Table 1.** Only the oracle-sign merge of Table 11 exceeds them.

## Connections

- **[THEORY-113](THEORY-113.md)** answers the same question, why merging loses
  accuracy, for models with no shared start, and locates the loss in
  features that have no counterpart. This account locates it in
  coordinates, where every feature has its counterpart by construction.
  They are filed as two accounts, not one, because their regimes do not
  overlap, their evidence is disjoint, and either could fail while the
  other stands. They are not rivals, because both can be right. Read
  together they make "merging fails on what the parents do not share",
  with "share" meaning features in one regime and coordinate-wise update
  directions in the other. As one account that slogan would be too loose
  to refute.
- **[THEORY-105](THEORY-105.md)** places fine-tuned models from one pretrained start
  at the edge of a task-specific region whose interior is at least as
  good. Within one task this agrees with TIES's small same-task gains:
  conflicts are present but averaging moves inward and costs little.
  Across tasks, the members lie in different regions, and this account
  says what the plain average loses on the way between them.
- **Practice across the boundary.** The anthology's model soups,
  [ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md), average same-task models from one start, the setting in
  which this account predicts the least loss, and TIES's Fig. 7 runs that
  setting.
