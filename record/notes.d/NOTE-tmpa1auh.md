---
status: Read
paper: 'LIT-tmpz6gcm'
title: 'Optimizing Mode Connectivity for Class Incremental Learning'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the PMLR PDF through its text layer, main text and
    Appendices A–G. Table values were recovered from the text layer; plot
    contents (Figs. 2, 5–10) were read from captions and text only.
date: '2026-10-03'
summary: >-
  In class-incremental learning (PODNet, CIFAR-100), the line between
  adjacent continual minima loses old-task accuracy in an interval. OPC adds
  a layer-wise Fourier perturbation δ_θ(λ) with δ(0) = δ(1) = 0 to the line,
  minimises old-task memory loss before a switching point λ* and new-task
  loss after it, with cylinder noise for flatness; EOPC averages 10 points
  near λ*. PODNet + EOPC: CIFAR-100 66.68 / 64.94 / 62.36 (5 / 10 / 25
  steps) vs 65.47 / 63.13 / 59.85; forgetting 7.68 / 8.64 / 12.02 vs 19.26 /
  25.01 / 28.55.
---

# NOTE-tmpa1auh: Optimizing Mode Connectivity for Class Incremental Learning

## Contribution

It brings path-finding mode connectivity to class-incremental learning
(CIL). It documents a high-loss ridge on the straight line between adjacent
continual minima, gives a low-parameter curved-path model (Fourier series per
layer) with a split objective for old and new tasks, and turns the path into
a post-processing step (EOPC) that existing CIL methods can adopt.

## Key insight

The new task's minimum sits on the old tasks' high-loss ridge, so the way
between them has to follow the old tasks' loss contours and then bend
towards the new minimum. A path that can bend several times, cheaply, finds
an interval that serves both, and the middle of that interval is a better
next model than the new minimum itself.

## Assumptions

- **CIL with replay**: half the classes in the first task, the rest split
  into 5, 10 or 25 increments; a small memory M_t of exemplars, the only
  data available to fit the path (§4.2).
- **Expanded previous minimum**: the old model plus a newly initialised
  classifier for the new classes, ŵ_{t−1} = w_{t−1} ⊕ z_t (Kaiming
  initialisation for z_t in OPC, App. C).
- **A switching point exists** on the optimal path with properties like a
  multitask minimum (§4, stated as a hypothesis).
- **BatchNorm statistics interpolated** linearly between the two models'
  running statistics, at training and test time, rather than recomputed
  (App. B).
- **Hyperparameters** (App. C): Fourier order N = 4, radius r ∈ {2, 4, 6},
  λ* ∈ {0.75, 0.85, 0.9}, 20 epochs of path training, 10 sampled λ per step
  in [0.1, 0.95], 10 ensemble points, interval τ = 0.1, cross-entropy loss
  for the path. Seed 1993 for Tables 1–2.
- **Stabilisers** (App. F): the loss is reweighted by |λ − 0.5| + 0.1, the
  old-task loss is extended to the whole path, and weight decay is put on
  the path coefficients.

## Key results

- **Linear interpolation** (Fig. 2; 5 initialisations, 10 seeds): an
  interval of ŵ₁ → w₂ degrades old-task accuracy; for t ≥ 3 an interval of
  the line beats both ends on all tasks. Xavier, Kaiming and Imprint keep
  old-task accuracy longer than Uniform and Normal.
- **Main results** (Table 1, average incremental accuracy A, 5 / 10 / 25
  steps):
  - CIFAR-100: PODNet 65.47 / 63.13 / 59.85 → 66.68 / 64.94 / 62.36; AANet
    66.53 / 64.63 / 61.05 → 67.55 / 65.54 / 61.82.
  - ImageNet-100: PODNet 76.32 / 73.54 / 63.05 → 77.12 / 74.53 / 68.18;
    AANet 77.98 / 74.70 / 68.65 → 78.95 / 74.99 / 70.10.
  - ImageNet-1K: PODNet 68.33 / 65.35 / 58.62 → 69.72 / 67.57 / 62.35;
    AANet 68.87 / 65.65 / 60.07 → 69.47 / 67.35 / 62.20.
  - Forgetting F, PODNet on ImageNet-100: 13.72 / 18.41 / 29.11 → 6.16 /
    4.15 / 8.3.
- **Repeated runs** (Table 3, 3 seeds): gains persist for PODNet, AANet and
  DyTox on CIFAR-100 and ImageNet-100, with one exception, AANet on
  ImageNet-100 at 10 steps (74.98 → 74.82).
- **Line vs OPC** (Table 2, Table 4): using the line's switching point
  lowers PODNet's accuracy (CIFAR-100, 3 seeds: 64.85 / 60.72 / 56.63 vs
  65.07 / 62.93 / 59.45); OPC's raises it (66.53 / 64.53 / 62.00).
- **Other path families** (Table 4, same objective): polygonal chain 64.41 /
  60.02 / 52.40; Bezier 66.81 / 64.06 / 57.59; second-order Bezier 66.56 /
  62.69 / 55.02; simplicial complexes 66.73 / 63.71 / 57.33; OPC 66.53 /
  64.53 / 62.00. Learned parameters: 5 × 10⁵ to 10 × 10⁵ for the others, 2
  × 96 × 4 for OPC.
- **Flattening and ensembling** (Fig. 5): ensembling alone does not improve
  steadily with radius; flattening does; both together do best.
- **Architectures** (Fig. 6, iCaRL + EOPC, 5 steps): gains across CNN, ResNet
  and DenseNet widths and depths, except CNN-12×8 and ResNet-8, which the
  authors judge too weak to reach low-loss regions.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In CIL, a high-loss ridge separates adjacent continual minima on the straight line | moderate: one method (PODNet), one dataset, accuracy as proxy for loss | Fig. 2 |
| C2 | A curved low-loss path exists between adjacent continual minima, and a point on it is a better model than either end | moderate: shown through accuracy gains and landscape plots on memory data | Tables 1–4, Figs. 7–10 |
| C3 | Fourier-parameterised paths outperform Bezier and simplex paths for long task sequences at a fraction of the parameters | moderate: 3 seeds, PODNet on CIFAR-100 only; below Bezier at 5 steps | Table 4 |
| C4 | EOPC is a general plug-in improvement for CIL methods | moderate: 3 baselines plus iCaRL across architectures; one counter-case in repeated runs | Tables 1, 3; Fig. 6 |
| C5 | Flattening the path improves generalisation | weak to moderate: one ablation | Fig. 5 |

## Method

1. Train task t with the base CIL method; expand w_{t−1} with a new head.
2. Path p_θ(λ) = (AC + (1 − λ)1_L)·ŵ_{t−1} + (BS + λ1_L)·w_t (Eq. 10), C and
   S the cosine and sine vectors of N frequencies, A and B per-layer
   coefficients with rows summing to zero (θ1_N = 0, Eq. 12).
3. Loss ℓ(θ) = ∫₀^{λ*} L_{1:t−1}(p_θ(λ)) dλ + ∫_{λ*}^1 L_t(p_θ(λ)) dλ (Eq.
   4), on memory data, evaluated at points on a cylinder of radius r
   orthogonal to the path's tangent (Eqs. 13–16).
4. Project the gradient onto the constraint set by subtracting each layer's
   mean gradient (Eq. 17); iterate.
5. EOPC: average M points drawn from the cylinder around λ* ± τ/2 (Eqs.
   19–20), and use the average as the next model.

## Concepts

- **switching point (SP)**: λ*, where the path loss switches from old-task
  to new-task loss; the model kept.
- **bent cylinder**: the set of points within radius r of the path,
  orthogonal to its tangent, near λ*.
- **expanded minimum ŵ_{t−1}**: the previous model with the new classes'
  head attached.

## Connections

- **Mirzadeh et al. ([LIT-tmp2e9aa](../literature.d/LIT-tmp2e9aa.md))**: the paper cites it as finding linear
  connectivity between continual and multitask minima in task-incremental
  learning, and as limited to that setting and to lines. Its conclusion
  conjectures that the multitask minimum lies in the low-loss region
  connecting continual minima, the claim Mirzadeh et al. tested from the
  other side.
- **Garipov et al. ([LIT-tmpotq71](../literature.d/LIT-tmpotq71.md))**: path objective and two comparator path
  families (polygonal chain, Bezier).
- **Benton et al. ([LIT-tmp6yuwj](../literature.d/LIT-tmp6yuwj.md))**: simplicial-complex comparator.
- **Draxler et al. ([LIT-tmp3kyq9](../literature.d/LIT-tmp3kyq9.md))**: AutoNEB's initial guess, the straight
  line, which OPC adopts.
- **Frankle et al. ([LIT-tmp3owu9](../literature.d/LIT-tmp3owu9.md))**: cited for the dependence of linear
  connectivity on a shared start, and for weak gains from ensembling in
  parameter space.

## Bearing on the record

- Evidence for the THEORY candidate stated in the Mirzadeh reading: linear
  connectivity from a shared start fails under class-incremental shift.
- **ML instruction** (EOPC), hence `anthology-candidate`.

## Limitations

- Path fitting uses only the small replay memory; the authors flatten the
  path partly to counter overfitting it.
- Single-seed main results (seed 1993) for Tables 1–2; 3 seeds in Tables 3–4.
- Accuracy, not loss, is the connectivity measure in Fig. 2.
- The ridge finding is for PODNet on CIFAR-100 only.
- Hyperparameters (λ*, r) are chosen from small grids without a stated
  validation protocol.

## Open questions

- Where, exactly, is the multitask minimum relative to the path (the
  authors' stated future work)?
- Does the ridge appear for replay-free CIL methods?
