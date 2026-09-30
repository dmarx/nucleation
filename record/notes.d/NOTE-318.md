---
number: 318
status: Read
formerly:
- NOTE-tmpio60n
paper: LIT-370
title: 'New Evidence of the Two-Phase Learning Dynamics of Neural Networks'
version: 1
history:
- version: 1
  date: '2026-09-30'
  note: >-
    Read in full (Full text of arXiv 2505.13900 v1 (20 May 2025, the only
    version; marked "Preprint. Under review."; it extends the authors' ICLR
    2025 DeLTa workshop paper "On the Cone Effect in the Learning Dynamics",
    which was not read), 11 pp., from the arXiv PDF. Read all of it:
    abstract, §§1–6 (including the Limitations paragraph) and the
    references. There are no appendices. Text was extracted with PyMuPDF.
    Pages 2 and 5–8 were rendered and Figs. 1 and 3–6 read from the images,
    because the results are carried almost entirely by heatmaps and curves.
    Not held in the Anthology of the SOTA: a grep of its literature.d for
    the arXiv id, the title and "cone effect" found nothing. `published:` is
    the arXiv v1 date.). The first NOTE on this paper, which was seeded from
    its abstract alone.
date: '2026-09-30'
summary: >-
  VGG-16 and ResNet-20 on CIFAR-10 (SGD with momentum, lr 0.1, 160 epochs)
  are compared across pairs of training times. Before an early "inflection
  point" (~2,500 iterations for VGG-16, ~100–500 for ResNet-20), a tiny
  parameter perturbation under identical SGD noise sends the run to a
  different basin by the end: loss barrier up to ~2, test disagreement
  ~0.15–0.5. After it, the same perturbation leaves the runs linearly
  connected. Also after it, the empirical NTK keeps changing step to step
  but stays within a bounded cosine distance of any later reference kernel
  (the "cone effect", e.g. S ≈ 0.05–0.1 for VGG-16 vs ≈ 0.15–0.2 from
  initialisation). Switching to linearised training later gives better
  test accuracy (VGG-16 0.13 → 0.82 as the switch moves from ≤200 to 5,000
  iterations).
---

# NOTE-318: New Evidence of the Two-Phase Learning Dynamics of Neural Networks

## Contribution

The paper proposes "interval-wise" analysis: comparing network states across *pairs* of training times rather than tracking a property at single times. It reports two effects that share one early transition point.

- **Chaos effect.** A tiny parameter perturbation at t₀ under identical SGD noise leads, if t₀ is before the transition, to a different loss basin and different test predictions by later t₁. If t₀ is after the transition, it does not.
- **Cone effect.** After the transition the empirical NTK keeps moving but stays within a narrow angular region around its value at any later reference time. Training is not lazy, but it is confined.

## Key insight

Early training is a short, sensitive exploration phase in which the eventual basin, and the kernel's orientation, are still being decided. After a transition at a few hundred to a few thousand iterations, the basin is fixed. The tangent kernel then only wobbles within a cone, so later training refines the function inside a settled feature geometry without either freezing it (lazy) or reorienting it.

## Assumptions

- **Setting.** CIFAR-10 image classification only. VGG-16 and ResNet-20, with random flips and 32×32 crops.
- **Optimisation.** SGD with momentum 0.9, weight decay 10⁻⁴, lr 0.1 dropped ×10 at epochs 80 and 120, for 160 epochs. The batch size is not stated.
- **Chaos protocol.** Two runs share the initialisation and "the same stochastic gradient noise" (same minibatch order and augmentation). At t₀ one run gets θ′ = θ + ε with "‖ε‖₀ = 10⁻⁷", whose norm is ill-defined (see corrections). The runs are compared at t₁ > t₀.
- **Measures (§3).**
  - Parameter cosine dissimilarity C (eq. 1).
  - Kernel distance S_ij = 1 − ⟨H(θ_i), H(θ_j)⟩/(‖H_i‖_F‖H_j‖_F), where H is the eNTK on the training inputs (eqs. 3–4). This is a *cosine* distance, so it is blind to kernel scale.
  - Loss barrier on the *test* set along the linear path (eq. 5).
  - Test disagreement rate (eq. 6).
- **Runs.** There is one run per configuration as far as the text shows. No seeds, error bars or variance are reported.

## Key results

- **Transition location.**
  - VGG-16: the perturbed/unperturbed cosine dissimilarity peaks at t₁ = 2,500 for every t₀ ≤ 1,500. Its magnitude is ≤ 8·10⁻⁴ (Fig. 3a).
  - ResNet-20: the peak is at t₁ = 100–200, only for t₀ = 0 (magnitude ~0.06).
- **Chaos effect: loss barriers (Fig. 3b).**
  - VGG-16: perturbing at t₀ ≤ 1,500 yields test-loss barriers of ~1–2 at t₁ ≥ 5,000. Perturbing at t₀ ≥ 2,500 yields ~0.
  - ResNet-20: perturbing at t₀ = 0 gives barriers of ~2. The barriers decline for t₀ = 100–500 and are near 0 beyond.
- **Chaos effect: disagreement (Fig. 3c).**
  - VGG-16: ~0.3 at t₁ = 2,500 and ~0.1–0.15 later, for t₀ ≤ 1,500.
  - ResNet-20: ~0.5 at t₁ = 100, then ~0.1–0.2.
- **eNTK over time (Fig. 4).** Within one run, pairwise kernel distance is large among early checkpoints and small among later ones. The block boundary sits at ~2,000 iterations (VGG-16) and ~100–500 (ResNet-20), matching the chaos transition.
- **Adjacent-step kernel change (Fig. 5b).** S_{t,t+dt} drops from ~1 (VGG-16) or ~0.25 (ResNet-20) to a floor of ~0.05 (VGG-16) or ~0.02 (ResNet-20). The floor is the same for dt ∈ {100,…,500}. The authors read "same bound for all dt" as evolution in a constrained space.
- **Distance from a later reference (Fig. 5a).**
  - For τ ∈ {2,000, 4,000, 6,000, 8,000}, S(θ_t, θ_τ) rises and then stays roughly flat: ≈0.05–0.1 for VGG-16, ≈0.02–0.03 for ResNet-20.
  - Measured from τ = 0, it stays at ≈0.15–0.2 for both.
- **Cone picture (Fig. 5c).** A 3-D projection, method unstated, of H(θ_t) shows later kernels clustered in a narrow cone from H(θ₀).
- **Linearised switching (Fig. 6).** Train normally to t, then linearised to T = 10⁴.
  - VGG-16: test accuracy ≈0.13 for t ≤ 200, rising to ≈0.82 at t = 5,000.
  - ResNet-20: ≈0.44 rising to ≈0.84.
  - Test loss falls correspondingly.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | There is an early transition point (VGG-16 ~2,500 it., ResNet-20 ~100–500 it.) before which a tiny parameter perturbation changes the final basin and predictions, and after which it does not | moderate (experiment), 2 architectures × 1 dataset, 1 run each | Fig. 3b–c |
| C2 | The optimisation trajectory "changes its direction" at that point | weak | inferred from cross-run dissimilarity (Fig. 3a), not from the within-trajectory directionality measure it defines |
| C3 | The early phase is "chaotic" | weak (name for C1) | no divergence rate or Lyapunov analysis |
| C4 | The eNTK stops evolving fast at the same point | moderate (experiment) | Figs. 4, 5b; echoes Fort et al. (2020), whom the paper cites |
| C5 | After the transition the eNTK is confined to a narrow cone: it keeps changing, but its cosine distance to any later reference stays bounded | moderate (experiment), qualitative | Fig. 5a–c; confinement is judged by flat curves and a 3-D picture |
| C6 | The later phase is not lazy, and its non-linear evolution benefits the final solution | moderate for "not lazy" (Fig. 5b floor > 0, Fig. 6); weak for "cone ⇒ generalisation" | Fig. 6 only shows that later switching to linearised training is better |
| C7 | Interval-wise analysis reveals what point-wise analysis cannot | assertion | the chaos protocol is close to the prior spawning experiments (Frankle et al. 2020; Fort et al. 2020), which §2 describes |

## Method

1. Paired runs with shared initialisation and SGD noise, differing by one small parameter perturbation at t₀, compared at t₁ by cosine dissimilarity, test-set loss barrier and test disagreement, over a grid of (t₀, t₁).
2. Within a single run, the full matrix of eNTK cosine distances between checkpoints.
3. Kernel-distance curves from fixed references and between adjacent steps.
4. A switch-to-linearised-training ablation over the switch time.

## Concepts

- **Interval-wise analysis.** A property of a *pair* of training times (t₀, t₁), not of one checkpoint.
- **Chaos effect / inflection point.** The early window in which perturbations change the basin, and its end.
- **Cone effect.** A bounded angular deviation of the eNTK from a later reference: continued but confined kernel evolution.
- **Kernel distance.** The cosine distance between eNTK Gram matrices on the training set (eq. 4). It measures kernel *orientation*, not scale.
- **Loss barrier / linear mode connectivity.** The maximum rise of test loss along the straight line between two parameter vectors (eq. 5).

## Connections

- **The IB account under [THEORY-035](../theory.d/THEORY-035.md) ([LIT-324](../literature.d/LIT-324.md), [NOTE-298](NOTE-298.md)).** The paper measures no information quantity. Taking the three IB claims one at a time:
  - *Fitting then compression in I(X;T).* Orthogonal. The two phases are of sensitivity (basin selection) and of kernel motion, not of I(X;T) or I(T;Y). The transition is early and short, a few hundred to a few thousand iterations out of a run of 160 epochs. In that respect it resembles [LIT-324](../literature.d/LIT-324.md)'s early bend at ~350 epochs (drift → diffusion), but only in shape, not in any shared quantity. Neither accuracy over time nor gradient SNR is reported here, so whether the chaos→cone point coincides with end-of-fitting, or with a gradient-SNR drop, cannot be read off.
  - *Compression causes generalisation.* Orthogonal. The later phase is a *restriction of the dynamics*: the function-space trajectory, via the eNTK's orientation, is confined to a cone, and the basin is fixed. If it is a simplification of anything, it is of *where the model can still go*, not of the representation's information about the input. The paper claims the cone's non-linear evolution helps generalisation, but supports only "more non-linear training helps" (C6). Nothing links it to discarding input information.
  - *Compression driven by SGD noise.* Orthogonal, with one relevant design fact. SGD noise is held *identical* across the paired runs, and the divergence is driven by a tiny deterministic parameter perturbation amplified by the early dynamics. So the early phase's sensitivity is not a noise effect, and the later stability is not shown to be caused by noise either. The later phase is where IB would place noise-driven diffusion. This paper finds the model's *function* moving only within a narrow cone there, but measures nothing that says whether I(X;T) falls.
- **[LIT-345](../literature.d/LIT-345.md) / [NOTE-283](NOTE-283.md) (Nanda et al.) and [LIT-341](../literature.d/LIT-341.md) / [NOTE-287](NOTE-287.md) (Power et al.).** The phase structures are different in kind. Nanda's memorisation → circuit formation → cleanup unfolds over 10³–10⁴ epochs and is defined by mechanistic progress measures on a known algorithm. Here the transition is at 10²–10³ iterations, in standard supervised vision with no delayed generalisation, and is defined by basin and kernel stability. Nothing here connects to grokking.
- **[LIT-348](../literature.d/LIT-348.md) (McCandlish).** Not cited. The batch size is not stated, so nothing can be said about the noise scale at the transition.
- **Anthology.** It cites Cohen et al. on edge of stability ([ANTH-LIT-461](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-461.md)) as another two-phase phenomenon (progressive sharpening, then a sharpness plateau). The linear-mode-connectivity literature it builds on is represented in the anthology by [ANTH-LIT-251](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-251.md) (permutation invariance and LMC). Frankle et al. (2020, LMC and lottery tickets), Frankle, Schwab & Morcos (2020, early phase) and Fort et al. (2020, deep vs kernel learning), the three closest precedents, are not held in either record (grep by arXiv id and title).
- **Within this batch.** Prakash & Martin (2025) define their phases by accuracy over 10⁵–10⁷ steps, with a late collapse. This paper's transition is at the very start of training. They describe different phenomena and time scales, and both are silent on I(X;T). Saxe et al. (2018) is the critique of [LIT-324](../literature.d/LIT-324.md)'s estimator, and this paper does not engage the information-plane literature at all.

## Bearing on the record

- **For [THEORY-035](../theory.d/THEORY-035.md): orthogonal to all three IB claims.** It supports only the generic statement the THEORY already concedes in "What this does not say", that training has an early fast phase and a later slow one. It supports it in *different* quantities (basin sensitivity, eNTK orientation) that owe nothing to an information estimator. For the record that is mildly useful. It shows a two-phase structure that can be measured without mutual information. So "the two phases are real" and "the second phase is IB compression" can be cited separately.
- **On "simplification".** The later phase is confinement of the dynamics, a fixed basin and a kernel orientation that moves only within a cone. It is not a simplification of weights, function or representation in any measured sense, and it is not IB compression of I(X;T).
- **ML practice.** Modest. It bears on when linearised or fine-tuning-style approximations become reasonable (after the transition, still worse than full training) and on when training becomes robust to perturbation. Its evidence base is thin (2 × CIFAR-10, single runs), so it is an anthology candidate as evidence about training dynamics, not as a practice.

## Limitations

- Two architectures on one dataset, one run each, and no error bars. The batch size is unstated. The perturbation size is ill-defined (‖ε‖₀).
- The "inflection point" is located by a cross-run cosine spike of magnitude ~10⁻³ (VGG). The directional claim is not measured on a single trajectory.
- The cone is established qualitatively: flat curves and an unspecified 3-D projection. No angular radius, dimension or rate is fitted.
- The kernel distance is a cosine, so a kernel that grows or shrinks in scale while keeping its orientation counts as "confined". Whether the magnitude of the kernel's motion is also bounded is not reported.
- The generalisation role of the cone is inferred from a switching ablation with no full-training baseline.
- The chaos half substantially overlaps the spawning / LMC literature the paper itself reviews in §2. The novelty is the parameter-perturbation protocol under fixed SGD noise and its pairing with the kernel analysis.
- The Limitations paragraph concedes that the paper is empirical only and limited to image classification.

## Open questions

- Does the chaos→cone transition coincide with a measurable drop in gradient SNR ([LIT-324](../literature.d/LIT-324.md)'s drift→diffusion), or with B_simple overtaking the batch size ([LIT-348](../literature.d/LIT-348.md))? The batch size would need to be stated first.
- Does I(X;T), with a network-intrinsic noise model, do anything distinctive at the transition, or inside the cone phase?
- Is the cone's angular radius set by the learning rate (e.g. does it narrow at the epoch-80 and epoch-120 drops, which Figs. 4–5 do not reach)?
- How does the transition time scale with width, depth and dataset size, and does it exist outside vision?

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The perturbation size is given as ‖ε‖₀ = 10⁻⁷ (§4, Fig. 3 caption). An ℓ₀ "norm" counts non-zero entries and cannot equal 10⁻⁷, so the actual perturbation magnitude, and whether it is per-parameter or total, is unspecified. The paper's "imperceptibly small" is not checkable as written.
- "Finding I" says the optimisation trajectory "changes its direction at a fixed point", inferred from Fig. 3(a). But C_{t0,t1} there compares the *perturbed and unperturbed* runs at t₁. It is not a directional change along one trajectory. For VGG-16 its values are tiny (maximum ≈ 8·10⁻⁴ on the colour bar, at t₁ = 2,500). The Singh et al. directionality measure (eq. 1, a within-trajectory matrix) is defined in §3 but its heatmap is not shown. So the "inflection point" is located by a spike in cross-run cosine dissimilarity, not by a measured change of direction.
- The "chaos" is named from the end-state divergence only. No Lyapunov exponent or growth rate of ‖θ_t − θ′_t‖ over time is measured. "Chaotic" is used in the loose sense of high sensitivity to initial conditions over a finite horizon.
- Eq. (1) has a typo in the denominator (‖vec(θ_j)‖₂‖vec(θ_j)‖₂). Fig. 5(c) runs its colour bar to 30,000 iterations, while Figs. 4–5(a,b) stop at 10,000 (VGG) or 2,000 (ResNet, Fig. 4). The projection used for the 3-D kernel picture in Fig. 5(c) is not stated.
- The batch size is not stated, so the transition times cannot be converted to epochs. Both transitions fall well inside the first learning-rate stage (lr = 0.1, before the drop at epoch 80).
- §5 says the cone "plays a crucial role in shaping the network's generalization ability". The only evidence is Fig. 6: switching to linearised training later gives better test accuracy at T = 10⁴. That shows that more non-linear training helps. It does not show that the confinement itself does. The fully non-linear baseline at T = 10⁴ is not reported.
