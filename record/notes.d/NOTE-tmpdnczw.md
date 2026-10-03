---
status: 'Read'
paper: 'LIT-tmpotq71'
title: 'Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv PDF (v4, 17 pages) through PyMuPDF text
    extraction: §§1–7 and supplement A.1–A.10. Tables 1–3 read from the
    extracted text. Figures 1–8 read from captions and the surrounding text;
    plotted values were not recovered. Claims the paper takes from Li et al.
    (2017), Freeman & Bruna (2017) and Gotmare et al. (2018) are taken as it
    reports them.
date: '2026-10-03'
summary: >-
  Curve-finding: minimize E_{t∼U(0,1)} L(φ_θ(t)) over the bend θ of a
  one-bend chain or quadratic Bezier curve between two trained networks.
  The found curves keep loss and error near the endpoints where the line
  segment reaches near-chance error (Table 2). Points at t ≥ 0.4 already
  ensemble as well as the far endpoint. FGE, short cyclical learning rates
  late in training, beats Snapshot Ensembles at equal budget (Table 1).
---

# NOTE-tmpdnczw: Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs

## Contribution

A cheap training procedure that finds a low-loss curve between any two
trained networks, and the empirical finding that such curves exist for
modern deep architectures with as little as one bend. From that, a fast
ensembling method (FGE) that exploits the fact that low-loss, functionally
different networks lie a short distance away from any trained one.

## Key insight

The minima found by SGD from different initializations are not isolated
basins but points in a connected low-loss valley. The straight line between
two of them crosses a high ridge, but a path that bends once goes around it.
The valley is wide in function space too: networks a modest Euclidean
distance along it make different predictions.

## Assumptions

- **Endpoints** are two networks trained with the same hyperparameters from
  different random initializations (§4). Different batch sizes, optimizers
  and schedules are reported only through Gotmare et al.
- **Curves** (§3.2, A.3): polygonal chain φ_θ(t) = 2(tθ + (0.5 − t)ŵ₁) for
  t ≤ 0.5 and 2((t − 0.5)ŵ₂ + (1 − t)θ) after, or quadratic Bezier
  (1 − t)²ŵ₁ + 2t(1 − t)θ + t²ŵ₂.
- **Objective**: Eq. 2, uniform in t rather than uniform in arc length
  (Eq. 1). The supplement reports the two are numerically very close on all
  curves found.
- **BatchNorm**: statistics recomputed with one extra pass for each point on
  a curve (A.2).
- **FGE**: piecewise-linear cyclical learning rate between α₁ and α₂, cycle c
  of 2–4 epochs, started at about 80% of the single-model budget, with a
  checkpoint at each cycle's minimum (§5).

## Key results

- **Table 2 (curve finding).** Max test error along the segment against the
  Bezier curve: VGG-16 CIFAR-10 90% vs 7.01% (endpoints 6.87–7.01%);
  ResNet-158 CIFAR-10 80.00% vs 6.24%; WRN-28-10 CIFAR-10 66.6% vs 4.83%;
  VGG-16 CIFAR-100 99.01% vs 31.23%; ResNet-164 CIFAR-100 98.83% vs 26.1%.
  Bezier curves are 1.30–2.13 times the length of the segment; polychains
  1.64–3.48. The polychain for WRN-28-10 is the exception, with a maximum test
  error of 10.38% against 4.56% at the endpoints.
- **Table 3 (PTB RNN).** Segment perplexity reaches 615.7 on test, the
  Bezier curve 84.0, against 78.7–78.9 at the endpoints.
- **Non-uniqueness** (§4): two chains with the same endpoints (VGG-16,
  CIFAR-10) had turning points 29.6 apart; the endpoints were 50 apart.
- **Diversity along the curve** (Fig. 2 right): a two-network ensemble of the
  endpoint and φ(t) improves from t ≈ 0.1 and matches the two-endpoint
  ensemble for t ≥ 0.4.
- **Ensembling on the curve** (A.6): 50 points on a ResNet-164 chain on
  CIFAR-100 give 21.03% error (20.7% after temperature scaling), against 22.0%
  for the two endpoints and 21.01% for three independent networks. Loss rises
  between the defining points through overconfidence, not through
  misclassification.
- **Width** (A.7): for a 3-conv/3-FC net with layers of 1000K units,
  K ∈ {0.3, 0.5, 0.8, 1}, the curve's worst train loss approaches the
  endpoints' and the length ratio falls monotonically (Fig. 7).
- **FGE (Table 1).** Error at budget 1B, CIFAR-100: VGG-16 Ind 27.4, SSE
  26.4, FGE 25.7; ResNet-164 21.5, 20.9, 20.2; WRN-28-10 19.2, 17.9, 17.7.
  On CIFAR-10 FGE beats SSE everywhere and is close to Ind for ResNets.
  ImageNet: 23.87% → 23.31% top-1 error in 5 epochs (4 models).
- **FGE steps are short** (§5): distance between FGE checkpoints about 7
  for PreResNet-164 on CIFAR-100, against about 40 between Snapshot
  Ensemble snapshots.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Independently trained optima of modern deep networks are connected by one-bend curves of near-constant train loss and test error | strong as an existence result; one curve per setting, no seeds or error bars | Table 2, Figs. 1–2 |
| C2 | Straight segments between such optima incur high error, less so for residual networks | moderate | Table 2, §4 |
| C3 | Points along the curves are functionally diverse, not reparametrizations | moderate | Fig. 2 right, A.6, A.8 |
| C4 | Greater width makes connection easier and the curve shorter relative to the segment | weak: one architecture, four widths | A.7, Fig. 7 |
| C5 | FGE outperforms Snapshot Ensembles at equal training budget | moderate: single runs above 1B, SSE tuned by grid | Table 1, §6.1 |

## Method

Curve finding: sample t̃ ∼ U(0, 1), take a gradient step on L(φ_θ(t̃))
with respect to θ only, repeat. The extra cost per step is O(|net|), and an
epoch costs under 50% more than a normal one (A.1). FGE is Algorithm 1 in
the supplement.

## Concepts

- **mode connectivity**: the existence of a path of near-constant loss
  between two independently found optima. This paper coins the term.
- **polychain**: a polygonal chain with fixed endpoints and learned bends.
- **FGE**: Fast Geometric Ensembling, ensembling the checkpoints taken at the
  low points of short learning-rate cycles.

## Connections

- **Draxler et al. 2018 ([LIT-tmp3kyq9](../literature.d/LIT-tmp3kyq9.md)).** The simultaneous, independent
  discovery; each paper cites the other. Draxler et al. use AutoNEB, a
  minimum-energy-path method from chemistry, where this paper trains a
  parametric curve.
- **Freeman & Bruna (2017)**, not held: connected one-hidden-layer ReLU
  networks with a loss bound depending on parameter count, and built chains
  by dynamic programming, which struggled on CIFAR-10.
- **Snapshot Ensembles (Huang et al. 2017)**, not held: the baseline FGE
  improves on. FGE uses much shorter cycles, and only at the end.
- **Izmailov et al. (SWA), [ANTH-LIT-673](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-673.md).** A.10 attributes the lower loss
  between FGE checkpoints to the averaging phenomenon that paper develops.

## Bearing on the record

- Primary source for the THEORY candidate that SGD optima of deep networks
  lie in one connected low-loss set, joined by simple curves (proposed in
  the batch report, not filed).
- Carries an ensembling instruction for ML practice (FGE), so it is an
  anthology candidate.

## Limitations

- One curve per architecture and dataset, with no seeds and no error bars on
  the connectivity results (Table 2).
- "Near-constant" is a matter of scale. On CIFAR-100 the maximum train loss
  on the curves is 25–40% above the endpoints' (ResNet-164: 0.098 Bezier,
  0.109 polychain, against 0.079; VGG-16 polychain: 0.2 against 0.14), and
  the WRN-28-10 polychain more than doubles test error at its worst point
  (Table 2, "Max" columns).
- The paper connects pairs. Whether all optima found by SGD lie in one
  connected set is implied by the discussion, not tested.
- The width study (A.7) is one small architecture.

## Open questions

- Why does one bend suffice? The paper offers no account.
- Do curves exist between networks trained differently (data, objective)?
  Partly answered by Gotmare et al., cited.
- Is the low-loss set a manifold of some definite dimension? Taken up by
  Benton et al. ([LIT-tmp6yuwj](../literature.d/LIT-tmp6yuwj.md)).

## Corrections

- none to a seeded skim (there was no seed)
- **Citation.** The NeurIPS proceedings pages are given as 8789–8798 by
  Frankle et al. and Kuditipudi et al., and as 8803–8812 by Ainsworth et al.
  Not resolved here; the arXiv id is the source.
