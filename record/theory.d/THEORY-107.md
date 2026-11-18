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
bears_on:
- QUESTION-069
---

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

## Note of 2026-11-15: nine readings on where merge loss lives

<!-- inactive-ok-file: THEORY-1898 THEORY-1903 THEORY-1901 THEORY-1874 THEORY-1872 THEORY-1892 THEORY-1905 THEORY-1879 THEORY-1897 — Proposed; the merging readings of 2026-11-15, cited as other accounts of the same loss, none tests this one -->

Nine readings filed on 2026-11-15 give accounts of the same loss, within one pretrained start, that do not run through sign. None runs the oracle-sign merge this account's promote_when names, so none settles it.

**Magnitude handling, not sign, is the largest step in the methods as built.**
- Li et al. 2026 ([THEORY-1898](THEORY-1898.md)): adding aligned updates over-counts shared directions and inflates the merged singular values. Singular Value Calibration rescales them only, with signs left to plain summation, and in the same runs lifts task arithmetic from 68.9 to 81.9 against TIES's 72.6 (ViT-B/32, 8 tasks); applied to TIES it gives 80.0. A rescaling-only merge beating the sign-electing one is evidence on the magnitude side of the promote_when, matching this account's own ablation (rescaling matters most). It is not the oracle-sign comparison, and not in (IA)³ and T5 for that purpose: on T0 with (IA)³, SVC lifts task arithmetic from 53.5 to 65.8 and leaves TIES at 54.1, in the authors' own runs, not comparable with TIES's paper.
- OrthoMerge, [LIT-2645](../literature.d/LIT-2645.md) ([THEORY-1903](THEORY-1903.md)), averages rotation generators in so(d): 41.01 without its norm correction, 46.25 with it (Table 4).
- Chaves et al., [LIT-2636](../literature.d/LIT-2636.md) ([THEORY-1901](THEORY-1901.md)), find task arithmetic at a fixed λ = 1 collapsing below zero-shot while trimmed and normalized merges do not.

**Accounts of interference that are not about coordinates**, each with a remedy that works in its setting:
- singular-vector overlap among different tasks' layer updates (Gargiulo et al. 2025, [THEORY-1874](THEORY-1874.md)): truncating and decorrelating them, with no sign election, beats Consensus TA by about 10 points on CLIP ViT-B/32; TIES is not run;
- low-frequency amplitude mismatch (Zheng & Wang 2025, [THEORY-1872](THEORY-1872.md)): FR-Merging, high-pass filtering with no sign election, beats TIES on ViT-B/32 (78.1 against 73.6), and TIES does not reduce the spectral mismatch; its frequencies run over the arbitrary order of rows and columns, and it too rescales, so it isolates neither mechanism;
- function-space disentanglement (Ortiz-Jimenez et al. 2023, [THEORY-1892](THEORY-1892.md)): task vectors acting on other tasks' inputs; it tests no signs, and linearised task vectors would test whether conflicts still cost once disentanglement is raised;
- cancellation of directions in so(d) (OrthoMerge);
- crosstalk among concatenated LoRA subspaces, removed by a least-squares router, which beats TIES and DARE on FLUX.1-dev (SSR-Merge, [LIT-2626](../literature.d/LIT-2626.md), [THEORY-1905](THEORY-1905.md));
- one task's update acting on another's inputs, reduced by choosing each LoRA's down-projection from the other tasks' features, which lifts task arithmetic on Llama3-8B by 9.5 points but not TIES (OSRM, [LIT-2650](../literature.d/LIT-2650.md), [THEORY-1879](THEORY-1879.md));
- the activation cross-term, mostly transported from earlier layers (Zhu, [LIT-2629](../literature.d/LIT-2629.md), [THEORY-1897](THEORY-1897.md)).

**"Conflict frequency does not track cost", sharpened.** Chaves et al. find the most singular-subspace overlap among same-task domain experts, call it conflict, and still merge them above zero-shot and an ensemble. Zhu's v3 finds TIES roughly doubling his output-side interference ratio while behaving best at small scale (not at 7B), and the cross-term a "bystander" where merging collapses. Sign disagreement, subspace overlap and the activation cross-term are different measurements, and none of these readings shows its measure causes the accuracy loss.

These are not rivals: each can hold with this account. Like TIES, SVC and FR-Merging bundle a diagnosis with magnitude changes, so the comparison that would separate sign from magnitude is still the one the promote_when names. A question, "Where does merge interference live: in coordinates, in subspaces of the updates, or in activations, and which test separates sign, magnitude along shared directions and function-space leakage?", would collect them; that is the owner's call. No status change.
