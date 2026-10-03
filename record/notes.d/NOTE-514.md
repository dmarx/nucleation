---
number: 514
status: 'Read'
formerly:
- NOTE-tmp3b7zo
paper: 'LIT-654'
title: 'Linear Mode Connectivity and the Lottery Ticket Hypothesis'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv PDF (v4, 30 pages) through PyMuPDF text
    extraction: §§1–6 and Appendices A–G. Results are carried by line
    plots, which were read from captions and from the numbers the text
    quotes; values were not read off the plots. Tables 1–2 extracted only
    partly (Table 2's last columns were lost) and are quoted only where the
    text repeats them.
date: '2026-10-03'
summary: >-
  Instability = max error on the line between two copies trained from the
  same state under different SGD noise, minus the mean endpoint error;
  stable means under 2%. Networks are unstable at initialization (except
  LeNet) and stable after 1.5–20% of training. IMP subnetworks at extreme
  sparsity are matching when, and only when, they are stable; rewinding to
  an early iterate makes them so at ImageNet scale.
---

<!-- inactive-ok-file: LIT-370 — Proposed; named as the record's reading that re-measures this paper's result, with no relation claimed -->

# NOTE-514: Linear Mode Connectivity and the Lottery Ticket Hypothesis

## Contribution

A measurement, instability analysis, that asks whether the outcome of
training from a given state depends on SGD noise, judged by the straight
line between two outcomes. With it, two findings: training settles into a
linearly connected region early, and lottery-ticket subnetworks work exactly
when they are stable in this sense. It also introduces rewinding to an early
iterate, which extends lottery-ticket results to ImageNet.

## Key insight

Training has two phases. In the first, SGD noise decides which region the
network ends in; two runs from the same initialization can end on opposite
sides of a ridge. After a short time the region is fixed, and two runs from
that point, however different their later noise, end on the same straight
valley floor. Pruning that works is pruning that keeps the network in the
second phase.

## Assumptions

- **SGD noise** means data order and augmentation only; initialization and
  hyperparameters are shared (§1–2). The copies are not independently
  initialized networks.
- **Barrier** (§2): E_sup(W₁, W₂) − mean(E(W₁), E(W₂)), measured on
  classification *error*, train or test, at 30 evenly spaced α. Means over 3
  initializations × 3 data orders.
- **Stable** means instability < 2%, a margin matched to the increases
  along Draxler et al.'s and Garipov et al.'s paths.
- **Networks** (Table 1): LeNet (MNIST); ResNet-20 and VGG-16 (CIFAR-10) in
  standard, low-learning-rate and warmup variants; ResNet-50 and
  Inception-v3 (ImageNet). ImageNet networks are pruned one-shot, the rest
  iteratively at 20% per round.
- **Matching** means accuracy within one standard deviation of the full
  network (§4); in §4.4, an accuracy drop under 0.2%.

## Key results

- **At initialization** (Fig. 2): only LeNet is stable, and its error rises
  by under a percentage point. For the others, train and test error on the
  line reach random guessing.
- **Onset of stability** (Fig. 3): ResNet-20 at iteration 2000 (3% of
  training), VGG-16 at 1000 (1.5%), ResNet-50 at epoch 18 (20%), Inception-v3
  at epoch 28 (16%), on test error. Train instability tracks test for the
  CIFAR networks and is slightly higher for the ImageNet ones; Inception-v3
  never becomes train-stable in the range analysed.
- **Not a training-time artefact** (Fig. 4): copies trained for the full T
  steps with the schedule reset give indistinguishable instability.
- **State at stability** (App. B): ResNet-20 test error about 25% (final
  8.3%), VGG-16 about 20% (final 6.3%), ResNet-50 55% (final 24%),
  Inception-v3 33% (final 22%). ResNet-20 and VGG-16 are still closer to their
  initial weights than to their final ones. The distance between the two
  copies' final weights exceeds half the total distance travelled for
  ResNet-20 and VGG-16, and is about a quarter and a half of it for ResNet-50
  and Inception-v3.
- **Stable at the end means stable throughout** (App. C): with k = 2000,
  ResNet-20 copies are linearly connected at every epoch.
- **Lottery tickets at k = 0** (§4.3, Fig. 5): IMP subnetworks of LeNet and
  the low and warmup variants are stable and matching; those of standard
  ResNet-20, VGG-16, ResNet-50 and Inception-v3 are neither, and no better
  than random pruning or reinitialization.
- **With rewinding** (Figs. 6–7): IMP subnetworks become stable at iteration
  500 (ResNet-20, 0.8%), 1000 (VGG-16, 1.6%), epoch 5 (ResNet-50, 5.5%) and
  epoch 6 (Inception-v3, 3.5%), earlier than the unpruned networks, and the
  rewinding points where they become matching "closely coincide".
- **Across sparsities** (§4.4, Fig. 9): three ranges. Range I, trivial
  sparsity, where random pruning also matches (above 80.0% of weights left
  for ResNet-20, 16.8% for VGG-16). Range II, where only IMP matches, and
  for 51.2–13.4% (ResNet-20) and 6.9–1.5% (VGG-16) it becomes stable and
  matching at about the same rewinding iteration. Range III, where nothing
  matches.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Standard vision networks become stable to SGD noise early in training, after which they end in one linearly connected minimum | strong for the six networks tested | Fig. 3, App. B–C |
| C2 | Except in small settings, networks are unstable at initialization | strong for the settings tested | Fig. 2 |
| C3 | IMP subnetworks at extreme sparsity are matching only when stable | moderate: correlational, two sparsity-sweep networks, extreme sparsities chosen per network | Figs. 5–7, 9 |
| C4 | Rewinding to an early iterate finds matching subnetworks at nontrivial sparsity at ImageNet scale | strong as an existence result | Figs. 6–7 |
| C5 | The best time to prune may be after some training, not at initialization | assertion drawn from C3–C4 | §5 |

## Method

Algorithm 1 (instability of W_k) and Algorithm 2 (IMP with rewinding to step
k). Appendix G tries four alternative comparison functions (L2 distance,
cosine distance, classification disagreement, L2 distance of per-example
losses); only disagreement and loss distance track stability, and both are
entangled with accuracy.

## Concepts

- **instability**: the error barrier on the line between two copies trained
  from the same state with different SGD noise.
- **linear mode connectivity**: an error barrier of about zero on the straight
  line.
- **matching**: a subnetwork that trains to the full network's accuracy.
- **rewinding**: resetting the unpruned weights to their values at step k
  rather than at initialization.

## Connections

- **Garipov et al. 2018 ([LIT-673](../literature.d/LIT-673.md)) and Draxler et al. 2018
  ([LIT-653](../literature.d/LIT-653.md)).** The mode connectivity this paper narrows to straight
  lines. Their modes, from different initializations, are not linearly
  connected; these copies, sharing a stem, are.
- **Nagarajan & Kolter (2019)**, not held: the only prior example of linear
  connectivity, MLPs from one initialization on disjoint MNIST subsets.
- **Frankle & Carbin (2019), [ANTH-LIT-019](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-019.md).** The lottery-ticket hypothesis,
  whose failures at scale this paper explains.
- **Zhou et al. 2025 ([LIT-370](../literature.d/LIT-370.md)).** Re-measures the onset of stability with
  parameter perturbations rather than fresh SGD noise.

## Bearing on the record

- Primary source for the THEORY candidate that linear connectivity emerges
  early in training (proposed in the batch report, not filed).
- It is the measurement every later paper in the batch uses, with Entezari
  et al.'s amendment to the barrier's baseline.
- Bears on pruning practice; an anthology candidate.

## Limitations

- **Correlation, not mechanism.** Stability and matching coincide; the paper
  says this "hint[s] at possible mechanisms" and does not test a cause.
- **Shared initialization.** Every result is about copies from one stem.
  Nothing here says that networks from different initializations become
  linearly connected; Entezari et al. and Git Re-Basin address that with
  permutations.
- **Error, not loss.** Barriers are measured on classification error, which
  saturates at chance; a loss barrier could behave differently.
- **Sparsity sweeps only for ResNet-20 and VGG-16** on CIFAR-10, for compute
  reasons (§4.2, App. D). The ImageNet results are at one sparsity each.
- **Image classification only.**

## Open questions

- What sets the time of onset? The paper links it to the noisy early phase
  (Hessian spectrum settling, warmup) without measuring the link.
- Why do IMP subnetworks become stable sooner than the dense network (epoch 5
  against 18 for ResNet-50)?

## Corrections

- none to a seeded skim (there was no seed)
