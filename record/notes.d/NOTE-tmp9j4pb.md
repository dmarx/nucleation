---
status: Skimmed
paper: LIT-978
title: 'Kothapalli — Neural Collapse: A Review on Modelling Principles and Generalization'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Skimmed from the arXiv PDF (v2 of 11 April 2023, the TMLR version, 39
    pages), fetched from arxiv.org/pdf/2206.04041 and extracted with
    pdftotext. The prose of the whole main text was read: §1, §2 (the NC1–NC4
    metrics), §3 (unconstrained features and local elasticity, with Table
    1), §4 (test collapse, the CDNV and NCC-depth bounds, transfer) and §5.
    The equations came through the extraction badly and were not checked
    term by term. Appendices A.2–A.4 were skimmed and the reference list
    scanned. Nothing in the review was checked against the papers it
    reviews, except Han et al., which is read in its own NOTE the same day.
date: '2026-10-14'
summary: >-
  A survey, not a source of results. It sorts accounts of neural collapse
  into unconstrained-features models (the last-layer features are free
  variables) and local elasticity, and reports that every one of them
  derives the collapsed state or its dynamics only after removing the data.
  On generalization it finds the literature in conflict. Collapse on the
  training set does not guarantee good test error, test-set collapse is
  much weaker and dataset-dependent, and there is no agreed threshold for
  calling a network collapsed. It also reports that networks more collapsed
  on ImageNet transfer worse.
---
<!-- inactive-ok-file: THEORY-083 THEORY-104 THEORY-213 — Proposed; the record's accounts of collapse, of layer-wise readout under shift, and of a symmetry account, which this review bears on -->

# NOTE-tmp9j4pb: Kothapalli — Neural Collapse: A Review on Modelling Principles and Generalization

## Contribution

A review of the first two years of work on neural collapse. It puts the
models of collapse in one notation and lays out their assumptions side by
side (Table 1). It then puts the claims about generalization and transfer
next to each other, and shows that they conflict. It proves nothing new of
its own beyond small extensions in Appendices A.3 and A.4.

## Key insight

Every derivation of neural collapse the review covers gets the collapsed
state by cutting the features loose from the data. The features are either
free optimization variables (the unconstrained features model, UFM) or
driven by an SDE with a chosen class-coupling matrix (local elasticity).
"Note that the purpose of this modelling technique is not to approximate
the actual non-linear dynamics." So the "why" of collapse is answered for a
model in which nothing but the labels can shape the answer.

## Assumptions

The review's own framing:

- Balanced classes, n = N/K per class, for most of the analysis (§2.1).
- "Expressive enough": a network that classifies the training set
  perfectly, so the penultimate features can be treated as free (§3.1).
- NC is defined as the empirical metrics NC1–NC4 → 0, with
  NC1 = (1/K) tr(Σ_W Σ_B†) (Eq. 4). The review itself says no threshold
  for "collapsed" is agreed.

## Key results

These are the reviewed papers' results as the review reports them. None
was checked against its source here.

- **Cross-entropy, no regularization.** Under norm constraints the
  minimizers form a simplex ETF (Wojtowytsch et al. 2020; Lu &
  Steinerberger). Gradient flow on the UFM converges in direction to
  approximate KKT points of a min-norm separation problem, whose maximum
  margin is attained only by collapsed configurations. A non-collapsed KKT
  point has a descent direction (Ji et al. 2021).
- **Squared error, no regularization.** Near-zero initialization keeps
  gradient flow close to a subspace on which "strong neural collapse"
  holds (Mixon et al. 2020). The linearization needs small norms.
- **Cross-entropy with weight decay.** Every global minimizer is
  collapsed, and every other critical point is a strict saddle when the
  feature dimension exceeds the number of classes, m > K (Zhu et al.
  2021).
- **MSE with weight decay.** The minimizer's class means are an
  orthogonal frame, a simplex ETF after centring (Tirer & Bruna 2022).
  Han et al. ([LIT-974](../literature.d/LIT-974.md)) give the dynamics on the central path.
- **Data independence.** ResNet18 and an MLP collapse on randomly labelled
  CIFAR-10 (Zhu et al. 2021). Yet in Papyan et al.'s runs NC1 reaches
  about 10⁻² for ResNet18 on CIFAR-10 and about 1 for ResNet152 on
  ImageNet (§3.3). The UFM cannot represent that difference.
- **Imbalance.** Above an imbalance threshold the minority classifiers
  merge ("minority collapse", Fang et al. 2021).
- **Local elasticity.** If intra-class influence exceeds inter-class
  influence, and the transformation matrix is aligned with the label
  residuals, class means tend to a simplex ETF (Zhang et al. 2021). The
  review notes that the original paper reports no NC1–NC4 measurements.
- **Generalization (§4.1).**
  - Training with SGD, Adam and L-BFGS reaches collapse on the training
    set with different test error (Zhu et al. 2021).
  - Test collapse is weaker than train collapse (Hui et al. 2022).
  - Galanti et al.'s CDNV bound ties train-set variability collapse to
    test-set collapse only for large per-class samples.
  - The review calls the CDNV bound at odds with the optimizer
    disparity.
- **Transfer (§4.2).** Galanti et al. bound few-shot transfer error by
  source-class CDNV, when source and target classes are drawn from one
  distribution. Kornblith et al. (2021) find that ImageNet networks with
  more collapse transfer worse to other datasets.

## Claims

Not filled: this reading is Skimmed, and the review's claims are reports of
other papers.

## Concepts

- **Unconstrained features model (UFM).** The penultimate features F are
  free variables, optimized jointly with the last layer (A, b). The
  layer-peeled model with one layer peeled is the same thing.
- **Local elasticity.** A sample's prediction moves little under an SGD
  step on a dissimilar sample (He & Su 2019).
- **Weak and strong test collapse.** Test features collapse to some class
  mean (weak) or to the correct one (strong).
- **CDNV.** Class-distance normalized variance: the summed variances of
  two classes divided by twice the squared distance of their means.

## Connections

The review builds on Papyan, Han & Donoho (2020), [LIT-618](../literature.d/LIT-618.md). It reviews Han
et al. ([LIT-974](../literature.d/LIT-974.md)) and is cited by Kothapalli & Tirer ([LIT-985](../literature.d/LIT-985.md)), by the same
first author. Thrampoulidis et al. ([LIT-994](../literature.d/LIT-994.md)) post-dates its first version.

## Bearing on the record

- **[QUESTION-051](../questions.d/QUESTION-051.md).** It names the state of the art for the question's
  first half. Collapse is derived in UFMs for cross-entropy and MSE, with
  and without regularization, and no account keeps the data. For the
  second half it reports evidence the record does not hold: more collapse
  on ImageNet goes with worse transfer (Kornblith et al. 2021). That is a
  direct measurement of what collapse costs for other distributions. It
  would be worth registering for [QUESTION-051](../questions.d/QUESTION-051.md) in its own right.
- **[THEORY-083](../theory.d/THEORY-083.md).** Its summary says "the dynamics are unexplained". That
  is true of [LIT-618](../literature.d/LIT-618.md) itself. As a description of the field it is out of
  date: the review lists gradient-flow and landscape results, all in the
  UFM. The THEORY should say "unexplained in [LIT-618](../literature.d/LIT-618.md); explained since only
  in models that remove the data", and cite [LIT-974](../literature.d/LIT-974.md) and [LIT-994](../literature.d/LIT-994.md) for the
  derivations the record now holds.
- **[THEORY-104](../theory.d/THEORY-104.md).** Kornblith et al.'s transfer result, as reported here, is
  the same direction as [THEORY-104](../theory.d/THEORY-104.md)'s mechanism: more collapse at the top,
  worse readout off-distribution. It is second-hand here.
- **[THEORY-213](../theory.d/THEORY-213.md).** The review mentions "rank collapse" (Martin & Mahoney)
  as an unexplored connection. It does not bear on the symmetry account.
- No instruction for machine-learning practice is relied on. The review
  mentions fixed simplex-ETF classifiers and oversampling minorities as
  practice; that belongs to the anthology.

## Limitations

- A survey: its value is the sorting, and every result in it is
  second-hand.
- Written mid-2022, with a 2023 revision. It does not cover the later
  imbalance geometry ([LIT-994](../literature.d/LIT-994.md)) or data-aware accounts ([LIT-985](../literature.d/LIT-985.md)).
- Its own §5 lists the gaps: no model unifies depth, nonlinearity,
  normalization, loss and optimizer, and no objective threshold for
  collapse exists.

## Open questions

- Whether collapse measured on training data says anything about test
  error. The review shows the published bounds and measurements disagree.
- Whether more collapse costs transfer generally, or only under the shift
  between ImageNet and the downstream sets Kornblith et al. used.
