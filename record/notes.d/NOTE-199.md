---
number: 199
status: Skimmed
formerly:
- NOTE-tmp2sfyq
paper: LIT-228
title: 'Balestriero & LeCun 2022 — SSL recovers spectral embedding'
version: 1
date: '2026-09-26'
summary: >-
  VICReg, SimCLR and Barlow Twins each solve, in closed form, a classical spectral embedding problem on the positive-pair graph G (Laplacian Eigenmaps, a generalized MDS/ISOMAP, and CCA respectively), so contrastive vs non-contrastive SSL is global vs local spectral embedding, and when G matches the downstream task any of them is optimal.
---
<!-- inactive-ok-file: LIT-228 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-199: Balestriero & LeCun 2022 — SSL recovers spectral embedding

## Contribution

The paper frames self-supervised learning as learning from inputs X plus a matrix G of pairwise positive relations, and places the major joint-embedding objectives inside spectral manifold learning. It shows that VICReg, SimCLR and Barlow Twins correspond to named spectral methods such as Laplacian Eigenmaps and multidimensional scaling. That correspondence yields closed-form optimal representations, closed-form optimal weights for linear networks, and an account of how the choice of pairwise relation affects both and downstream performance. It draws a bridge from contrastive methods to global spectral methods and non-contrastive ones to local methods, and derives practical advice: with a task-aligned G any method works (and VICReg's invariance weight should be high in low-data regimes); with a misaligned G, VICReg with small invariance weight is preferable to SimCLR or Barlow Twins.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1/Fig. 1 (p. 2): SSL sits between supervised and unsupervised learning by consuming (X, G); all methods are cast as preserving the left-singular vectors of G in the representation Z.
- §3.1, Thm 1 (p. 7): VICReg's invariance term is the Dirichlet energy of Z on G; its global minimiser is a closed-form eigen-solution depending only on G and the ratio γ/α, with many local minima given by other K-of-N eigenvector subsets.
- §3.2–3.3, Thm 2–3, Prop. 1 (pp. 9–10): variance/covariance-constrained VICReg is (kernel) Laplacian Eigenmaps; with a linear network it recovers Locality Preserving Projections and, with a label graph, LDA.
- §4, Thm 5 & Prop. 2 (pp. 12–13): SimCLR/NNCLR/MeanShift solve a generalized MDS problem akin to ISOMAP; §5, Thm 6–7: Barlow Twins recovers (kernel) CCA and can recover VICReg.
- §6.3 & §7 (pp. 16–17): when G is correctly aligned with the task, every method yields an ideal representation and none is better; under misalignment SimCLR and Barlow Twins collapse the rank of Z to G's information, while low-invariance VICReg stays full-rank.

## Open questions

- Anchor paper for the "representation learning as a spectral approximation" heading: it supplies explicit method-by-method dictionaries to classical spectral embedding.
- Check how much the results depend on replacing the VICReg hinge variance term with a squared loss and on the full-batch / N-sample idealisation.
- The practical advice (prefer low-invariance VICReg when augmentations are misaligned) is a candidate practice claim; check whether its empirical support goes beyond small synthetic settings (e.g. N=256, K=32 in Fig. 4–5).
