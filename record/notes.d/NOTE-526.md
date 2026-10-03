---
number: 526
status: Read
formerly:
- NOTE-tmpcorcs
paper: 'LIT-675'
title: 'TIES-Merging: Resolving Interference When Merging Models'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v2, main text and Appendices A–C
    including the per-task Tables 3–9. Figures were read from captions and
    text. Where Table 1 and the per-task tables disagree, both values are
    given below.
date: '2026-10-03'
summary: >-
  Task vector τ = θ_ft − θ_init. TIES keeps the top 20% of each τ by
  magnitude, sets γ_m = sgn(Σ τ̂_t), averages only entries agreeing with
  γ_m, and returns θ_init + λ τ_m. Validated: (IA)³ 66.4 vs 63.9 for task
  arithmetic; T5-base 73.9 vs 73.2; T5-large 76.9 vs 73.3; ViT-B/32 73.6 vs
  71.8 (RegMean); ViT-L/14 86.0 vs 84.5. Unvalidated T5-base 69.7 vs 73.2.
  Oracle multitask signs give 72.0 against 73.1 for multitask training.
---

# NOTE-526: TIES-Merging: Resolving Interference When Merging Models

## Contribution

It names and measures two sources of loss when task vectors are summed or
averaged: redundant small updates, and sign disagreement among influential
ones. It gives a three-step remedy with two hyperparameters and a default
that works without a validation set in most settings. It shows the gap to
multitask training is mostly a matter of getting the signs right.

## Key insight

A fine-tuning update is mostly noise around a few coordinates that matter.
Averaging lets the noise and the opposing updates of other tasks shrink
exactly the coordinates that matter. Choose the coordinates first, then
choose a direction per coordinate, then average only what agrees.

## Assumptions

- **Shared initialisation.** All task vectors are differences from the same
  pretrained weights θ_init, full fine-tuning or PEFT ((IA)³ on T0-3B). The
  paper's own limitations note that merging "relies on common
  initialization and model architecture" (App. A).
- **Coordinates are meaningful across models.** Sign and magnitude per
  parameter are compared directly; there is no alignment step.
- **Hyperparameters** k (top-k%) and λ (scale), tuned on validation data
  where available; otherwise k = 20, λ = 1, chosen on the (IA)³ setting and
  applied to the others (§5, App. C.4).
- **Evaluation** by rank classification over label strings (App. C.6).

## Key results

- **Redundancy** (Fig. 3): keeping the top 20% of each (IA)³ task vector
  matches keeping all of it on average over 11 tasks. Flipping the signs of
  the top 20–30% of entries with probability p degrades performance
  monotonically; flipping the bottom 70–80% has little effect (§7.2).
- **Sign conflict** (Fig. 4, App. B.3–B.4): conflicts rise with the number
  of models merged, and with k (to almost 80% when nothing is trimmed, for
  10 BERT checkpoints). Same-task checkpoints conflict about as much as
  different-task ones.
- **Main comparison** (Table 1; per-task Tables 3–7). With validation:
  - (IA)³, 11 tasks: Fisher 62.2, RegMean 58.0, task arithmetic 63.9, TIES
    66.4; fine-tuned 71.4, multitask 73.1.
  - T5-base, 7 tasks: 68.9, 71.2, 73.2, 73.9; fine-tuned 82.8.
  - T5-large: 64.6, 73.2, 73.3, 76.9; fine-tuned 88.8.
  - ViT-B/32, 8 tasks: 68.3, 71.8, 70.1, 73.6; fine-tuned 90.5.
  - ViT-L/14: 82.2, 83.7, 84.5, 86.0; fine-tuned 94.2.
  Without validation (averaging, task arithmetic at λ = 0.4, TIES at k = 20,
  λ = 1): T5-base 65.9, 73.2, 69.7; T5-large 59.6, 73.5, 74.4; ViT-B/32
  65.8, 60.4, 72.4; ViT-L/14 79.6, 83.3, 86.0.
- **Out of domain** (Fig. 5 table; Tables 8–9), six held-out T0 tasks:
  T5-base TIES 35.3 vs RegMean 34.3; T5-large 40.4 vs 36.0.
- **Number of tasks** (Fig. 6, T5-large): with two tasks TIES and task
  arithmetic are both near 1.0 normalised accuracy and averaging drops about
  10%; task arithmetic declines faster as tasks are added.
- **Same-task soups** (Fig. 7 table; 10 BERT checkpoints): RTE 72.2, MRPC
  86.8, WNLI 58.8, against task arithmetic 71.8, 86.0, 59.2.
- **Merged model as initialisation** (Fig. 8 table): RTE 80.1, MRPC 88.0,
  WNLI 54.9; averaging gives 56.3 on WNLI.
- **Ablation** (Table 12; T5-base, (IA)³ validation): full 74.5 / 70.7;
  without trim 73.0 / 70.6; without elect 73.1 / 69.6; without disjoint mean
  72.6 / 67.5; without scale 72.0 / 65.5.
- **Oracle signs** (Table 11): (IA)³ 72.0 with the multitask model's signs,
  against 73.1 multitask and 71.4 fine-tuned. Signs from a 32-example
  multitask model initialised at the mean: 67.7 (Table 2).
- **Sensitivity** (App. B.2): TIES ranges 68–75% across its λ grid,
  task arithmetic 55–75%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Most of a task vector can be zeroed without harming its task | strong for (IA)³; T5 in App. C.3 | Fig. 3, §7.2 |
| C2 | Sign conflicts among influential parameters are common and grow with the number of models | strong as measurement | Fig. 4, Figs. 14–15 |
| C3 | Plain averaging shrinks influential parameters, and trimming and electing restore their magnitude | moderate: magnitude statistics, not a causal test of accuracy | Fig. 9, App. B.5 |
| C4 | TIES outperforms prior merging methods across modalities and scales | strong with validation; mixed without (loses on T5-base) | Table 1, Tables 3–7 |
| C5 | Getting the signs right nearly closes the gap to multitask training | moderate: one PEFT setting, oracle signs from the multitask model itself | Table 11, Table 2 |
| C6 | TIES degrades more slowly than task arithmetic as tasks are added | moderate: up to 7 tasks, at most 10 subsets per size | Fig. 6, Fig. 18 |

## Method

1. τ_t = θ_t − θ_init for each task.
2. Trim: keep the top-k% of |τ_t|, zero the rest, giving τ̂_t.
3. Elect: γ_m^p = sgn(Σ_t τ̂_t^p), the sign of greater total mass.
4. Disjoint merge: τ_m^p = mean of τ̂_t^p over t with sgn(τ̂_t^p) = γ_m^p
   (zeros excluded).
5. θ_m = θ_init + λ τ_m.

## Concepts

- **task vector**: θ_ft − θ_init (Ilharco et al.).
- **redundant parameter**: an entry outside the top-k% of its task vector.
- **sign conflict**: a parameter whose kept values have different signs
  across models.
- **disjoint mean**: the mean over the models that agree with the elected
  sign, ignoring zeros.

## Connections

- **Frankle et al. ([LIT-654](../literature.d/LIT-654.md))** is cited for the premise that networks
  sharing part of their trajectory can be interpolated; fine-tuning from one
  checkpoint is the case relied on.
- **Entezari et al. ([LIT-652](../literature.d/LIT-652.md)) and Git Re-Basin ([LIT-661](../literature.d/LIT-661.md))** are
  cited for the permutation route needed when networks are trained from
  scratch, which this paper does not take.
- **Task arithmetic (Ilharco et al.), Fisher merging (Matena & Raffel),
  RegMean (Jin et al.)**, none of them in either record, are its baselines.
- **Model soups ([ANTH-LIT-675](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-675.md))** is the same-task setting of Fig. 7, run on
  BERT checkpoints from the Hugging Face hub.
- **Gueta et al. ([LIT-658](../literature.d/LIT-658.md))** is cited among the mode-connectivity works
  in §2.

## Bearing on the record

- With ZipIt! ([LIT-665](../literature.d/LIT-665.md)), a THEORY candidate: merging loses what the
  parents do not share, and what is not shared is identified at the level
  of coordinates (here) or of features (ZipIt!). Not filed.
- **ML instruction**, hence `anthology-candidate`.

## Limitations

- **Table inconsistencies.** Table 1 gives task arithmetic without
  validation on T5-base as 73.2, Table 4 as 73.9; the bracket on TIES's
  69.7 reads −3.2, matching neither difference. Table 1 reports no
  unvalidated (IA)³ results, while Table 3 does (TIES 64.9, task arithmetic
  59.2). In Table 3, the RegMean row is identical, task by task, to the
  averaging row.
- The default recipe was selected on (IA)³ and is not tested there, so the
  unvalidated (IA)³ number is not out-of-sample.
- The optimal λ for TIES varies from 1.0 to 3.0 across subsets of tasks
  (App. C.5); the "no validation" setting fixes λ = 1.
- Merging remains below multitask training and individual fine-tuned models
  in every setting of Table 1, as App. A states.
- Same initialisation is required; nothing is said about merging across
  pretrained models.

## Open questions

- How to estimate the multitask sign vector cheaply. App. B.1's 32-example
  attempt recovers 1.3 of the 5.6 points available.
- Why sign conflicts are as frequent within a task as across tasks (App.
  B.4 suggests many equivalent subnetworks).
