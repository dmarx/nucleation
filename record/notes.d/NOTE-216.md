---
number: 216
status: Skimmed
formerly:
- NOTE-tmpn1fcu
paper: LIT-233
title: 'Variable-size compressibility generalization bounds'
version: 1
date: '2026-09-26'
summary: >-
  Letting the compression rate of an algorithm's input data vary with the observed sample yields generalization bounds that depend on the empirical measure rather than the unknown distribution, and this single framework recovers PAC-Bayes and data-dependent intrinsic-dimension bounds as special cases.
---
<!-- inactive-ok-file: LIT-233 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-216: Variable-size compressibility generalization bounds

## Contribution

The authors introduce a "variable-size compressibility" framework in which a learning algorithm's generalization error is tied to a compression rate of its input data that may vary with the data. Because the rate depends on the sample at hand, the resulting bounds are data-dependent, i.e. computable from the empirical measure. They derive tail bounds, tail bounds on the expectation, and in-expectation bounds, and general bounds for arbitrary functions of data and hypothesis. Several known PAC-Bayes and intrinsic-dimension bounds fall out as special cases, some possibly improved, and a new dimension bound links generalization to the compressibility of optimization trajectories via the rate-distortion dimension, Rényi information dimension and metric mean dimension of a process.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §I (pp. 1–2): positions the work against four apparently unrelated families — information-theoretic (Russo–Zou, Xu–Raginsky mutual information), compression (Littlestone–Warmuth onward), fractal/intrinsic-dimension, and PAC-Bayes — and argues the useful bounds are data-dependent; the MI and earlier rate-distortion bounds are not, since they need the joint distribution.
- §II (p. 3): the earlier fixed-size compressibility framework of Sefidgaran et al. (k09) only gives data-independent bounds; letting the rate vary is the generalization that admits data-dependence.
- §III–IV (pp. 5–11): general tail / expectation / in-expectation bounds, then specializations: rate-distortion bounds (IV-A), PAC-Bayes including a new lossy PAC-Bayes bound (Prop. 1, IV-B), and dimension-based bounds with the new trajectory-compressibility bound (Thm. 7, IV-C).
- §V (p. 11): experiments on CIFAR-10 with a 4-layer FCN and a CNN trained by SGD at learning rates in [5e-5, 1e-3]; rate-distortion of normalized trajectories estimated with a neural estimator (NERD); larger learning rates give both smaller generalization error and more compressible trajectories (the coupling term of Thm. 7 is ignored, as in prior work).
- §VI (pp. 11–12): conclusion names the open question of reconciling small communication cost with good generalization, and extensions to compressibility of latent representations (cf. k11) and distributed learning. The paper notes parts were published at IZS 2024 and ISIT 2024 (p. 1 footnote).

## Open questions

- Belongs to the "compression implies generalization" line the heading gathers; a deeper reading should check whether any bound can be read as a (Kolmogorov / MDL) description-length statement or only as a Shannon rate-distortion one — the link to minimal sufficient statistics is not made in what I read.
- Check how the "variable-size" rate relates to a two-part code length for the sample, i.e. whether it is an MDL-style quantity in disguise.
- The Thm. 7 experiment drops the coupling coefficient; a reader should check how much of the empirical support survives that omission.
