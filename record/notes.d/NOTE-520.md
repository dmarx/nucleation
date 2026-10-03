---
number: 520
status: Read
formerly:
- NOTE-tmp6vg74
paper: 'LIT-651'
title: 'Linear Mode Connectivity in Multitask and Continual Learning'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v1, main text and Appendices A–D.
    Figures (interpolation curves, loss planes, Hessian overlaps) were read
    from captions and the text that describes them. Table 1 is the only
    table of numbers; it is reproduced below.
date: '2026-10-03'
summary: >-
  From a shared start ŵ₁, the multitask solution w*₂ is linearly connected
  to ŵ₁ and ŵ₂, but ŵ₁ and ŵ₂ are not; the ŵ₁ → w*₂ direction is nearly
  orthogonal to task 1's top 50 Hessian eigenvectors, and ŵ₁ → ŵ₂ lies in
  their span. Different starts (CIFAR), input noise, label corruption and
  removed classes break the line. MC-SGD averages the loss along both lines
  with a one-example-per-class buffer: after 20 tasks 85.3 / 82.3 / 63.3%
  (Permuted MNIST / Rotated MNIST / Split CIFAR-100), multitask 89.5 / 89.8
  / 68.8, Stable SGD 80.1 / 70.8 / 59.9.
---

# NOTE-520: Linear Mode Connectivity in Multitask and Continual Learning

## Contribution

It is the first study, by its own account, of the geometric relation between
continual and multitask solutions. It finds that the two are linearly
connected when both start from the same point, explains this by curvature,
maps where the connection breaks, and builds a continual learning method,
MC-SGD, on it.

## Key insight

Forgetting is not a matter of how far the weights move but of which way.
Multitask learning from task 1's solution moves through directions in which
task 1's loss is flat. Continual learning moves through the steep ones.
There is a region around a task's solution where a second-order picture
holds, and many later tasks can be solved inside it.

## Assumptions

- **Non-standard multitask run.** w*₂ is trained on D₁ + D₂ starting from
  ŵ₁, not from scratch (§1), "to minimize the potential number of
  confounding factors". Tasks are added to the multitask loss one by one, in
  parallel to the continual sequence (App. D.2, Fig. 15).
- **Shared structure between tasks.** Rotated or permuted MNIST, Split
  CIFAR-100 with 5 classes per task; a multitask solution is assumed to
  exist (§2).
- **Architectures**: a two-layer MLP (100 units in §2, 256 in §5, 512 for 50
  tasks) and a reduced-width ResNet18.
- **Smoothness** of the loss, invoked informally for the curvature argument
  (§3).
- **MC-SGD's data**: a replay buffer of one example per class per task, and
  equally spaced α at n = 5 points (enough, per App. C.3).

## Key results

- **Distances mislead** (Fig. 2, App. D.1): ŵ₅ is nearer to ŵ₁ in ℓ₂ than w*₅
  is, and more similar in CKA, yet ŵ₅ has forgotten task 1. The Taylor bound
  L₁(ŵ₂) − L₁(ŵ₁) ≤ ½ λ₁^max ‖ŵ₂ − ŵ₁‖² (Eq. 1) is loose when the displacement
  is not along the top eigenvector.
- **Linear connectivity** (Figs. 3–4, App. D.2): task 1's loss stays low on
  lines from ŵ₁ to w*₂ … w*₅ and rises on lines to ŵ₂ … ŵ₅, on Rotated MNIST
  and Split CIFAR-100; likewise for task 2 from ŵ₂. The zoomed plots show the
  continual line is increasing where the multitask line is not.
- **Curvature** (Fig. 5, Rotated MNIST, deflated power iteration): task 1's
  spectrum has a bulk plus about C outliers. The ŵ₁ → ŵ₂ direction overlaps
  the top eigenvectors; ŵ₁ → w*₂ has near-zero cosine with all 50. With 20
  epochs instead of 5, neither direction lies in the top subspace, yet only
  the continual one forgets.
- **Where it breaks** (App. B): a multitask run started from another point
  is separated from ŵ₁ by a wall on CIFAR-100 (on MNIST the line survives, as
  Frankle et al. also found). Gaussian noise on the second task's inputs,
  5–10% label corruption, or removing 2 or 4 classes from the multitask data
  each break the connection progressively (Figs. 9–11).
- **MC-SGD, 20 tasks** (Table 1), average accuracy / forgetting:
  - Permuted MNIST: naive 44.4 / 0.53, EWC 70.7 / 0.23, A-GEM 65.7 / 0.29,
    ER-Reservoir 72.4 / 0.16, Stable SGD 80.1 / 0.09, MC-SGD 85.3 / 0.06,
    multitask 89.5.
  - Rotated MNIST: 46.3, 48.5, 55.3, 69.2, 70.8, 82.3 / 0.08, multitask 89.8.
  - Split CIFAR-100: 40.4, 42.7, 50.7, 46.9, 59.9, 63.3 / 0.06, multitask
    68.8.
  The MC-SGD minima stay nearly linearly connected to earlier continual
  minima (Fig. 7). The lead grows with the number of tasks, and holds for 50
  Permuted MNIST tasks (App. D.3, Fig. 18).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | From a shared start, multitask solutions are linearly connected to earlier continual solutions and continual solutions are not connected to each other | moderate: two benchmarks, interpolation plots, 5 tasks | §2.1, Figs. 3–4, App. D.2 |
| C2 | ℓ₂ distance and CKA do not track forgetting | moderate | Fig. 2, App. D.1 |
| C3 | The multitask direction avoids the earlier task's high-curvature subspace | moderate: top 50 eigenvectors, one benchmark, 5 epochs | Fig. 5 |
| C4 | Shared initialisation and shared task structure are needed for the linear connection | moderate: one benchmark per manipulation | App. B |
| C5 | Constraining solutions to be linearly connected to previous ones reduces forgetting more than replay or EWC with the same buffer | strong for these benchmarks, 5 seeds | Table 1, Fig. 6 |

## Method

MC-SGD for two tasks: w̄ = argmin_w ∫₀¹ [L₁(ŵ₁ + α(w − ŵ₁)) + L₂(ŵ₂ + α(w −
ŵ₂))] dα (Eq. 3), approximated with a few α, and with L₁ estimated from the
replay buffer. Online form: w̄_t = argmin_w Σ_α [L_{t−1}(w̄_{t−1} + α(w −
w̄_{t−1})) + L_t(ŵ_t + α(w − ŵ_t))] (Eq. 5), where ŵ_t is first obtained by
training on task t from w̄_{t−1}.

## Concepts

- **continual minimum ŵ_t**: the solution after training on task t alone,
  starting from the previous solution.
- **multitask minimum w*_t**: the solution after training on tasks 1…t
  together, starting from ŵ_{t−1}.
- **average forgetting**: the mean over tasks of peak accuracy minus final
  accuracy.

## Connections

- **Frankle et al. ([LIT-654](../literature.d/LIT-654.md))** supplies the premise: a shared start
  makes linear connection likely. App. B.1 reproduces their MNIST
  observation and finds it fails on CIFAR-100 for a different start.
- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md)), Draxler et al. ([LIT-653](../literature.d/LIT-653.md))** are the
  curved-path connectivity of independently started runs; **Kuditipudi et
  al. ([LIT-671](../literature.d/LIT-671.md))** the theoretical account via dropout and noise
  stability.
- **Neyshabur et al. 2020** (not in the record): no barrier between
  solutions from a shared pretrained start. The paper reads ŵ₁ as playing
  the pretrained model's role for the multitask run.
- **Wen et al. ([LIT-681](../literature.d/LIT-681.md))** find a high-loss ridge on the line between
  adjacent continual minima in class-incremental learning, consistent with
  C1's negative half, and argue that this paper's linear account is limited
  to task-incremental learning.

## Bearing on the record

- A THEORY candidate across the batch: linear connectivity from a shared
  start holds when the objectives share structure, and fails under class
  removal, label corruption, input noise (here), class-incremental shift
  (Wen et al.) and heterogeneous client data (Zhou et al., [LIT-666](../literature.d/LIT-666.md)).
  Not filed.
- **ML instruction** (MC-SGD), hence `anthology-candidate`.

## Limitations

- The multitask comparator is a non-standard run started from ŵ₁; the
  usual multitask model from scratch is not shown to be connected.
- Curvature evidence is on Rotated MNIST with an MLP only.
- The benchmarks are task-incremental-style splits with small networks; one
  epoch per task in §5.
- The paper notes Permuted MNIST's known shortcomings and reports it for
  consistency.

## Open questions

- Is the second-order region large enough for long task sequences on
  harder data, and how would one measure its size?
- Does the connection survive class-incremental settings without task
  labels? Wen et al. suggest it does not.
