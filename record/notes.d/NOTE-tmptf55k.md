---
status: Read
paper: LIT-2998
title: 'Ansuini, Laio, Macke & Zoccolan — Intrinsic dimension of data representations in deep neural networks'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the arXiv PDF of 1905.12784v2 (28 Oct 2019; footer "33rd
    Conference on Neural Information Processing Systems (NeurIPS 2019)"),
    fetched 2026-11-22 from arxiv.org without obstacle and converted with
    pdftotext; metadata checked on the arXiv API. Read in full: §§1–4,
    Appendix A.1 and the captions of Figs 1–9. Skipped: values that live
    only in the figures, the code repository and the figshare data. Read by
    a reader subagent; filed by a second one, which rechecked every quote
    used here against the PDF text. No email address sent.
date: '2026-11-22'
summary: >-
  With the TwoNN estimator, the intrinsic dimension of a layer's
  representations in trained image CNNs is orders of magnitude below the
  layer's width, rises over the early layers and falls to about 12 to 25 in
  the last hidden layer, and is one to two orders below a 90%-variance PCA
  count. Across 14 ImageNet models (not across seeds) the last hidden
  layer's value correlates with test accuracy; random weights give a flat
  profile, shuffled labels a rising one.
---
<!-- inactive-ok-file: CLAIM-847 CLAIM-848 SYNTHESIS-120 TERM-136 THEORY-251 THEORY-tmpwn1xp — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# NOTE-tmptf55k: Ansuini, Laio, Macke & Zoccolan — Intrinsic dimension of data representations in deep neural networks

## Contribution

A layer-by-layer, many-architecture map of a nonlinear global estimate of
intrinsic dimension (ID) in large CNNs, with controls that separate it from
linear dimension and tie it to training on learnable labels: random
weights, a covariance-matched Gaussian, luminance-perturbed and
label-shuffled MNIST.

## Key insight

The representations lie near low-dimensional, curved manifolds, so a
linear count of dimensions sees them as far higher-dimensional than they
are, and does not tell trained from random networks apart. "Progressive
reduction of the ID, rather than gradual flattening, seems to be the key
to achieving linearly separable" representations (§4).

## Assumptions

- **TwoNN**: μᵢ = rᵢ(2)/rᵢ(1), the ratio of each point's second to first
  nearest-neighbour distance, is Pareto with parameter d + 1 if the density
  is constant up to the second neighbour (§2). One global ID per point
  cloud.
- Bias: "For larger IDs and finite sample size, the approach moderately
  underestimates the correct value ... the values reported in the
  following figures, when larger ∼ 20, should be considered as lower
  bounds." Scale checked by decimation (Fig. 2B).
- 450 to 2000 points per estimate; the ImageNet profiles use seven
  classes, 500 images each.
- **PC-ID**: the number of principal components of the correlation matrix
  that "describe 90% of the variance", not a participation ratio.

## Key results

- **ID ≪ width** (Abstract, §3.1): "the ID is orders of magnitude smaller
  than the number of units in each layer"; for one VGG-16 layer "ID ≈ 19".
- **Hunchback** (§3.1, Fig. 3): "the ID initially grew, then reached a
  peak or a plateau and, finally, progressively decreased towards its final
  value"; footnote 1 excepts AlexNet and the small MNIST network.
- **Last layer and accuracy** (§3.2, Fig. 4, A.1.4): across architectures
  "a strong predictor of the performance of the network on the test set,
  as measured by top 5-score (Fig. 4, Pearson correlation coefficient r =
  0.94)"; across 50 seeds of one VGG-16 on CIFAR-10, "no correlation with
  accuracy (r=-0.003)".
- **Linear against nonlinear** (§3.3, Fig. 5): the PC-ID is "about one or
  two orders of magnitude larger than the value of the ID computed with
  TwoNN"; VGG-16's last hidden layer has PC-ID "≈ 200" against an ID near
  18.
- **Covariance-matched Gaussian** (§3.3, Fig. 5B): for data with "the same
  second-order moments" the ID "was two orders of magnitude larger, and
  grew with N ... as expected in the case of an ill-defined estimator".
- **Random weights** (§3.3, Fig. 5C): PC-ID profile like a trained
  network's; TwoNN ID "remarkably flat".
- **Shuffled labels** (§3.5): the ID "grew considerably in the second half
  of the network, almost saturating the upper bound".
- **Training dynamics** (Fig. 9, exploratory): last-hidden ID drops, then
  slowly rises.
- **Interpretation** (§4): "a flattening of data manifolds may not be a
  general computational goal".

## Concepts

- **Intrinsic dimension (ID)**, global, by TwoNN; **embedding dimension
  (ED)**, the layer width.
- **PC-ID**, the 90%-variance linear count.
- **Hunchback profile**; **relative depth**; **decimation** as a scale
  test; **covariance-matched Gaussian** as a null.

## Connections

TERM-136's intrinsic dimension m is the paper's ID; its ambient D is the
paper's ED. The paper's linear dimension is a fifth notion beside
TERM-136's participation ratio. It cites Stringer and colleagues (bioRxiv
2018) for a gapless spectrum "qualitatively consistent" with V1's, without
fitting an exponent. Its §4 ties the result to Chung, Lee and
Sompolinsky's manifold capacity, the apparatus THEORY-251 holds with
dimension in the participation-ratio sense. Not registered: Facco and
colleagues' TwoNN paper (2017), Levina and Bickel (2005), Ma and colleagues
(2018), Chung, Lee and Sompolinsky (2018); none is relied on here.

## Bearing on the record

Filed as THEORY-tmpwn1xp. Dated notes of 2026-11-22 on each entry below.

- **TERM-136**: supports its intrinsic sense and qualifies it (global,
  scale-dependent, a lower bound above about 20; PC-ID is not the
  participation ratio); the term now draws on this reading.
- **CLAIM-848**: a parallel with the gap the other way round.
- **LEAD-210**: TwoNN ID with a subsampling check added to the
  per-checkpoint measurements.
- **SYNTHESIS-120**: effective and intrinsic dimension diverge.
- **CLAIM-847**, **NOTE-549**, **NOTE-789**, **THEORY-251**, **NOTE-541**,
  **THEORY-083**: background, parallel or contrast.
- LIT-2998's summary was accurate, with two qualifications now in it: no
  early rise in the small MNIST network, and the accuracy relation holds
  across architectures, not across seeds.

Nothing here is filed as an instruction for machine-learning practice.

## Limitations

- Correlational: no intervention on ID, and no relation within an
  architecture (r = −0.003).
- IDs above about 20 are underestimates, so the mid-layer peaks are floors.
- Few classes and a few hundred points per manifold.
- Image CNNs only.
- The 90% threshold for PC-ID is ad hoc.
- The training-dynamics evidence is one VGG-16 on CIFAR-10.
