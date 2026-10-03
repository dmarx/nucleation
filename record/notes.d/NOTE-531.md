---
number: 531
status: 'Read'
formerly:
- NOTE-tmpkvaq5
paper: 'LIT-653'
title: 'Essentially No Barriers in Neural Network Energy Landscape'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv PDF (v5, 12 pages) through PyMuPDF text
    extraction: §§1–6 and Appendices A–B. Table B.1's numeric columns did not
    extract in a usable layout and were not used; the quantities quoted here
    come from the prose of §4.3 and Appendix B. Figures read from captions.
date: '2026-10-03'
summary: >-
  AutoNEB finds paths between minima whose highest training loss is almost
  the minima's for ResNets and DenseNets on CIFAR-10, with a small gap on
  CIFAR-100; test error rises at most 0.5% (CIFAR-10) and 2.2% (CIFAR-100)
  per §4.3, or 0.7% and 2.9% on the ResNets per Appendix B. Concatenating
  paths bounds every pair through a minimum spanning tree. Barriers shrink
  with width and depth.
---

# NOTE-531: Essentially No Barriers in Neural Network Energy Landscape

## Contribution

The first application of AutoNEB to modern deep networks, and with it the
finding that minima of ResNets and DenseNets on CIFAR are joined by paths with
almost no loss barrier. The paper also adds a cheap way to bound all pairwise
barriers among many minima through path concatenation.

## Key insight

The set of parameters with loss below a small threshold is one connected
component. A minimum is a point on that set, not the floor of a valley, and a
network with capacity to spare can always route around the ridge that the
straight line crosses.

## Assumptions

- **Minima**: ten per architecture, trained to convergence from different
  random initializations, on CIFAR-10 and CIFAR-100 with standard training
  procedures. Their test misclassifications overlap at most 70% (§4), which
  the authors take as proof they are distinct.
- **Loss continuity**: the loss is continuous in the parameters, but no bound
  on its steepness is known, so paths are sampled densely (§3.1).
- **Paths found are upper bounds**: AutoNEB can stall in a local MEP with a
  spuriously high saddle (§3.2). All reported barriers are therefore upper
  bounds on the true MEP saddle.
- **Loss evaluated per pivot on a random batch** during optimization;
  final numbers are over the full training and test sets.

## Key results

- **MEP objective** (§3.1): p* = argmin over paths of max_{θ∈p} L(θ).
- **NEB forces** (Eqs. 1–3): the loss force acts only perpendicular to the
  path and the spring force only along it. In practice the spring force is
  set to zero and pivots are redistributed each iteration (the string
  method). AutoNEB inserts pivots where the loss between pivots exceeds the
  linear estimate by 20% of the path's total energy range (§4.1, App. A).
- **Ultrametric bound** (§3.2): L*_AC ≤ max{L_AB, L_BC}, proved by
  concatenation; the lowest local MEPs form a minimum spanning tree.
- **Schedule** (§4.1): 14 NEB cycles per pair, SGD with momentum 0.9 and
  λ = 0.0001, learning rate 0.1 then 0.01 then 0.001.
- **Saddle losses** (§4.3, Fig. 5): small for shallow CNNs, almost negligible
  for deep residual networks. For shallow CNNs the saddle is near the *test*
  loss; for ResNets and DenseNets it is near the *training* loss. The saddle
  energies of the deep residual networks are about two orders of magnitude
  below the untrained loss (App. B).
- **Error** (§4.3): at most +0.5% (CIFAR-10) and +2.2% (CIFAR-100) for all
  deep architectures. Appendix B gives, for the ResNets, at most +0.7% and
  +2.9%, and for the DenseNets +0.4% and +1.5%.
- **Crossing time** (Fig. 6): training loss passes the mean saddle energy at
  about epoch 205 (78% of training) for DenseNet-100-12-BC on CIFAR-100 and
  epoch 72 (52%) for ResNet-56, the latest and earliest crossings.
- **Path shape** (§4.4, Fig. 7): each coordinate moves smoothly, the largest
  deviation from the straight line is near the saddle, and paths are 1.5 to
  2.5 times as long as the segment.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Minima of current deep architectures on CIFAR are connected by paths with essentially no loss barrier | strong for the settings tested; upper bounds from ten minima per architecture | §4.3, Fig. 5, Table B.1 |
| C2 | Barriers fall with width and especially depth, and rise with dataset difficulty | moderate: shallow CNN sweep, one family | Fig. 5 |
| C3 | Low-loss minima form a single connected component | moderate: inferred from pairwise paths among ten minima | §6 |
| C4 | Spare capacity (resilience, redundancy) explains the absence of barriers | weak: a qualitative argument and an XOR toy | §5 |
| C5 | Low Hessian eigenvalues exist beyond the zero modes due to scaling | assertion | §6 |

## Method

AutoNEB (Algorithm 2) wraps NEB (Algorithm 1) and adds pivots adaptively;
Algorithm 3 chooses which pairs to connect next by repeatedly trying to
replace the highest edge of the current spanning tree.

## Concepts

- **minimum energy path (MEP)**: the path between two points whose highest
  loss is lowest; its highest point is a saddle of the loss.
- **local MEP**: a path where NEB has converged that is not the global MEP.
- **saddle point energy**: the highest loss on a path; here always an upper
  bound on the true barrier.

## Connections

- **Garipov et al. 2018 ([LIT-673](../literature.d/LIT-673.md)).** Simultaneous and independent; the
  two papers cite each other (§2 and §6 here).
- **Freeman & Bruna (2016)** and **Sagun et al. (2017)**, not held: earlier
  evidence of connected minima, on MNIST/PTB and on close minima. This paper
  extends both to arbitrary minima of deep networks.
- **Ballard et al. (2016, 2017)**, not held: NEB applied to single-hidden-layer
  perceptrons, where barriers vanished as hidden units were added.
- **Dinh et al. (2017)**, not held: scale degeneracy of ReLU minima. The paths
  here are claimed to be a different degeneracy, between minima not related
  by rescaling.

## Bearing on the record

- Co-source, with [LIT-673](../literature.d/LIT-673.md), for the THEORY candidate that SGD optima of
  deep networks lie in one connected low-loss set (proposed in the batch
  report, not filed).
- Its redundancy argument is an early informal form of the candidate that
  barriers are mostly what permutations cost.

## Limitations

- Ten minima per architecture, image classification on CIFAR only.
- Every barrier is an upper bound; the paper cannot say how far it is from
  the true MEP saddle.
- **The two error figures disagree.** §4.3 says error rises "by maximally
  0.5% (2.2%) for all deep architectures", while Appendix B gives up to 0.7%
  and 2.9% for the ResNets. The appendix's ResNet list may include ResNet-8,
  which the appendix itself groups with the shallow networks; the paper does
  not say.
- Both explanations in §5 are offered as qualitative; the authors say they
  cannot characterize the regime in which the finding holds.

## Open questions

- With better AutoNEB settings, do some pairs keep a higher barrier than
  others, so that minima cluster (the disconnectivity graphs of the energy
  landscape literature)? The authors propose this.
- How much spare capacity is needed? Kuditipudi et al. ([LIT-671](../literature.d/LIT-671.md)) give
  one sufficient condition.

## Corrections

- none to a seeded skim (there was no seed)
