---
number: 279
status: Proposed
formerly:
- THEORY-tmpqq175
promote_when: >-
  A replication in a different setting that measures, at each checkpoint,
  accuracy on maximum-entropy samples matched to order 1, 2 and 3. It
  should find the first-order peak before the second, and the second
  before the third, with the later fall in accuracy. The setting would be
  higher resolution, another modality, or another training regime. Or a
  derivation, in a solvable nonlinear model, of the time at which
  sensitivity to order-k statistics peaks. It is refuted by a trained
  network whose third-order-matched accuracy peaks before its
  second-order-matched accuracy, or whose early checkpoints ignore
  grafted class means and covariances. More first- and second-order
  curves at 32×32 do not settle the higher orders, which is where the
  claim is thinnest.
title: 'Early in training, image classifiers and language models act on the low-order statistics of their inputs, first-order before second-order, and later lose that sensitivity as they come to use higher-order structure'
version: 2
history:
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: two transformer training-dynamics works read on
    2026-10-26 for the exchange "Experimental Infrastructure Review"
    show the same low-order-first shape inside one network, at the
    level of heads and of features; neither meets the promote_when. The
    account is unchanged.
tags:
- learning-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-952
summary: >-
  Belrose et al. (2024, ICML), [LIT-952](../literature.d/LIT-952.md), read in [NOTE-777](../notes.d/NOTE-777.md). Over
  training, ConvNeXt V2, Swin V2 and RegNet-Y on five small image datasets
  are probed with images whose class means or covariances are grafted
  from another class, and with maximum-entropy samples that keep only
  those statistics. Accuracy on these rises and then falls, often below
  chance. Pythia fits unigram-sampled text before bigram-sampled text.
  The ordering is empirical and covers orders one and two. The Taylor
  argument that motivates it is a heuristic, and the paper does not
  measure an ordered sequence beyond second order.
answers:
- QUESTION-039
---
<!-- inactive-ok-file: THEORY-201 THEORY-039 — Proposed; accounts this one is set beside, none of them rested on -->

# THEORY-279: Early in training, image classifiers and language models act on the low-order statistics of their inputs, first-order before second-order, and later lose that sensitivity as they come to use higher-order structure

## Source

Belrose, Pope, Quirke, Mallen, Dury and Fern (2024), [LIT-952](../literature.d/LIT-952.md), read in
[NOTE-777](../notes.d/NOTE-777.md): §§2–4, Figs. 3, 5–7 and Appendices C, F.

## What was actually shown

**The probes.** The networks are trained on real data. At log-spaced
checkpoints they are evaluated on two kinds of synthetic data.
- **Images edited by optimal transport toward a target class.** Quantile
  normalization or a bounded mean shift changes first-order statistics.
  Gaussian OT changes first and second. Accuracy is scored against the
  *target* label.
- **Maximum-entropy samples matched to a class.** Independent pixels
  match the first order. Gaussian or hypercube-constrained samples match
  the second. Approximate samples match the third.

**Vision.** The models are ConvNeXt V2, Swin V2 and RegNet-Y at five
scales, on CIFAR-10, CIFARNet, MNIST, Fashion-MNIST and SVHN, for 2^16
steps.
- Between roughly 2^4 and 2^12 steps all models classify mean-edited
  CIFAR-10 images as the target class, peaking near 2^9. ConvNeXt
  exceeds 40% against the target on covariance-edited images near 2^10;
  chance is 10%.
- First-order samples peak earlier and lower than second-order ones.
  Accuracy then falls, often below chance (Figs. 3, 5).
- MNIST and Fashion-MNIST, where two moments already draw recognisable
  digits, barely fall. On SVHN first-order samples never beat chance.
- Model scale changes little.

**Language.** Pythia, 14M to 12B, is evaluated on text sampled from
maximum-entropy 1- to 4-gram models of the Pile.
- Unigram loss reaches its minimum before bigram loss, and at a higher
  value.
- Both rise again and then fall a second time. The authors attribute the
  second fall to in-context learning, on correlational evidence
  (Fig. 7).

**What could have come out otherwise.**
- Early checkpoints could have ignored grafted statistics.
- First- and second-order accuracy could have peaked together, or in the
  other order.
- Accuracy could have stayed high, which would show that the low-order
  features persist.

## What this does not say

- **Not an ordered sequence beyond second order.** "Increasing
  complexity" is shown as first before second. Third-order samples are
  generated and plotted in the appendix figures, but the text states no
  result for them.
- **Not a mechanism.** The Taylor expansion E[L(x)] = Σ_α ∂^αL(µ)·E[(x − µ)^α]/α!
  motivates the order. That its higher terms "grow in roughly monotonic
  order" is a supposition, and it gives no timescale.
- **Not that n-gram learning is moment learning in any deeper sense.**
  Theorems 2.1–2.2 are identities: products of one-hot indicators are
  joint probabilities, and a linear embedding preserves polynomial
  degree. They license the language test. They add no dynamics.
- **Not forgetting, as a finding.** The later loss of low-order
  sensitivity is measured. Whether the low-order features are erased or
  only outweighed is not tested, and the authors' "catastrophic
  forgetting" is a speculation about small Pythia models.
- **Not beyond small images.** Gaussian OT costs O(d³), so every vision
  result is at 32×32 or 64×64.

## Connections

- **[QUESTION-039](../questions.d/QUESTION-039.md).** It answers in part, and only empirically. The order
  is the statistical order of the input distribution. The moment is
  dataset-dependent, roughly 2^4 to 2^12 steps, and insensitive to scale.
  The rise and fall show that acquiring later structure can retire
  earlier behaviour.
- **[THEORY-229](THEORY-229.md) and [THEORY-086](THEORY-086.md).** These order acquisition by the
  eigenvalues of a second-moment operator: the cross-correlation Γ, or
  the NTK Gram matrix. All they learn is a function of second-order
  statistics. They are candidates for the early phase found here, and
  they say nothing about the later one. The paper does not test whether
  that early phase is ordered by eigenvalue.
- **[THEORY-204](THEORY-204.md) and [THEORY-201](THEORY-201.md).** There, a language model uses a token
  correlation once its pairwise statistic rises above sampling noise.
  Pythia's unigram-before-bigram order is consistent with that. But it
  is measured in steps on a fixed corpus, not in examples, so it is not a
  test of the horizon.
- **[THEORY-039](THEORY-039.md).** It warns that phases differ in kind, and this bears it
  out. The rise of the n-gram loss and its later fall by in-context
  learning are two events on one curve.

## Note of 2026-10-26: the same shape inside one transformer

<!-- inactive-ok-file: THEORY-967 THEORY-1004 — Proposed; readings of the same day, cited as evidence of the same shape, not as confirmation -->

Two works read on 2026-10-26 for T24 of the exchange "Experimental
Infrastructure Review" ([QUESTION-275](../questions.d/QUESTION-275.md)) show this account's shape in a
second family of evidence.

- **Heads.** In the two-layer attention-only language model of the
  refined-LLC study ([NOTE-1188](../notes.d/NOTE-1188.md)), the stages run bigrams, then n-grams
  and skip n-grams, then previous-token heads, then induction heads, and
  the first-layer heads that predicted simple n-grams later give some of
  them up as they take new roles ([THEORY-967](THEORY-967.md), two checkpoints of one
  run). Low order first, and the early sensitivity lost.
- **Features.** In three 1B-parameter models, the crosscoder features that
  matter for subject–verb agreement move from detecting particular tokens
  to detecting grammatical categories ([THEORY-1004](THEORY-1004.md)), by the authors'
  annotation and with no null for the shift.

Neither meets the promote_when. Neither measures accuracy on samples
matched to order one, two and three, and the order of n-grams is not the
order of statistics this account means: an n-gram head is sensitive to a
higher-order statistic of the token sequence than a unigram model, but
neither study separates the orders the account names. They are
consistent with it, in another setting, and confirm nothing. The account
is unchanged.
