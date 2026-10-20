---
number: 777
status: Read
formerly:
- NOTE-tmpc775c
paper: LIT-952
title: 'Belrose et al. — Neural Networks Learn Statistics of Increasing Complexity'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2402.04362v3, 9 October 2024, the
    ICML 2024 version, PMLR 235; 26 pages), text extracted with pdftotext:
    §§1–5, Appendices A–G, the proofs of Theorems 2.1 and 2.2 (App. F),
    D.1 (App. D) and E.1 (App. E), and every figure caption. Plotted values
    were read from the captions and the text, not off the images. The
    author list has six names; the LIT, seeded from the abstract page,
    gave five.
date: '2026-10-14'
summary: >-
  An empirical paper. Vision networks trained on real images classify
  maximum-entropy samples that match only the class means, or means and
  covariances, well above chance early in training (peaks between about
  2^4 and 2^12 steps), and the accuracy then falls, often below chance.
  First-order samples peak earlier and lower than second-order ones.
  Pythia models fit unigram-sampled text, then bigram-sampled text, then
  fit them worse, then better again. The n-gram/moment equivalence is an
  identity of one-hot indicators. The ordering argument is a heuristic.
---
<!-- inactive-ok-file: THEORY-279 THEORY-201 THEORY-039 — Proposed; the account filed from this reading and the accounts of acquisition order it is set beside -->

# NOTE-777: Belrose et al. — Neural Networks Learn Statistics of Increasing Complexity

## Contribution

The paper tests the distributional simplicity bias (DSB) from the other
side of Refinetti et al. (2023). The networks are trained on real data
and probed throughout training with synthetic data that keeps only
low-order statistics. It shows that early checkpoints of several modern
image classifiers act on class means and covariances, and that later
checkpoints stop doing so. It carries the test to language models by an
identity between n-gram statistics and moments of one-hot sequences.

## Key insight

What a network is sensitive to early in training can be measured by
evaluating it on data that has been stripped to a given order of
statistics, by maximum entropy, or given another class's statistics, by
optimal transport. On that measure, sensitivity rises and then falls, and
the low-order peak comes first.

## Assumptions

- **For the Taylor motivation (§2, Eq. 1–2):** the loss L(x) is analytic
  with an adequate radius of convergence around the mean input µ (ReLU
  is not, footnote 2), and the input has finite moments of all orders.
  Inputs are scaled to the unit hypercube.
- **For the ordering argument (§2.1):** "the higher derivatives of L are
  reasonably well-behaved at initialization", so the 1/α! factors make
  higher-order terms decay factorially. That they grow "in roughly
  monotonic order" during training is a supposition (footnote 6 gives a
  second, informal reason).
- **For the n-gram results (§2.5, App. F):** an "n-gram statistic" is the
  probability that given tokens occur at given absolute positions,
  skip-grams included (Def. F.1). The experiments use contiguous n-grams
  only, and assume translation invariance.
- **Operational criteria (§2.2):** a model "uses" statistics up to order k
  if grafting class B's first k statistics onto class A makes it answer
  B, and if deleting higher-order statistics does not hurt it.

## Key results

- **Theorem 2.1 (n-gram statistics are moments).** For a distribution P
  on length-N token sequences, every moment of its flattened one-hot
  pushforward f♯P is an n-gram statistic of P, and conversely. The proof
  is that a product of {0,1} indicators is a conjunction, so its
  expectation is a joint probability. *Holds:* exactly, for any finite
  vocabulary.
- **Theorem 2.2 (equal embedding moments).** If P and Q agree on n-gram
  statistics up to order k, then for any fixed embedding matrix E their
  embeddings agree on moments up to order k, because a linear map sends
  degree-k polynomials to degree-k polynomials. *Holds:* exactly.
- **Theorems D.1 and E.1.** Algorithm 1 is the unique least-squares shift
  of a vector in [0,1]^n to a given mean. The maximum-entropy density on
  [0,1] with mean m ≠ 1/2 is p(x) = b·exp(−bx + b)/(exp(b) − 1), with b
  solving m = −(b − e^b + 1)/(b(e^b − 1)). These are tools.
- **Optimal transport (Fig. 3, §3.3).** Accuracy w.r.t. the *target*
  class of images edited by coordinatewise quantile normalization,
  bounded shift or Gaussian OT. Between roughly 2^4 and 2^12 steps, all
  models classify CQN-edited CIFAR-10 images as the target class, with a
  peak near 2^9. ConvNeXt peaks above 40% on second-order-edited images
  near 2^10 steps; chance is 10%. *Holds:* ConvNeXt V2, Swin V2 and
  RegNet-Y on CIFAR-10, CIFARNet, MNIST, Fashion-MNIST and SVHN, 2^16
  steps, AdamW (RegNet-Y with SGD).
- **Maximum-entropy samples (Fig. 5, §3.3).** "Accuracy on first order
  samples peaks earlier in training and has a lower maximum than accuracy
  on second order samples, followed by the 2nd order
  hypercube-constrained samples." Some models early in training do better
  on independent-pixel samples than on the real validation set. Later the
  accuracy falls, "often dipping below the random baseline". MNIST and
  Fashion-MNIST show little of this fall. On SVHN no model exceeds chance
  on first-order samples (Fig. 11). Model scale has "a remarkably small
  effect".
- **Pythia (Figs. 6, 7, 12–15, §4).** Unigram-sequence loss reaches its
  minimum before bigram-sequence loss and has a higher minimum. Both then
  rise, troughing between 2^6 and 2^8 steps and rising until about 2^10.
  Then they fall again, which the authors attribute, "correlational[ly]",
  to in-context learning: per-position loss in Pythia-12B starts to
  decrease along the sequence after step 8,000 for bigrams. No
  non-monotonicity is seen for 3- and 4-grams. Seeds and a longer warmup
  change little.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Early in training, vision networks classify by class-conditional means and covariances | strong | OT and max-entropy experiments, 3 architectures × 5 datasets, Figs. 3, 5, 8–11 |
| C2 | Sensitivity to first-order statistics peaks earlier, and lower, than sensitivity to second-order | moderate | Fig. 5 and App. C; stated qualitatively, no peak times tabulated |
| C3 | Later in training this low-order sensitivity is lost | moderate | non-monotone curves on CIFAR-10, CIFARNet and SVHN; weak on MNIST and Fashion-MNIST |
| C4 | Language models fit unigram statistics before bigram statistics | moderate | Pythia suite, 14M–12B, several seeds, Figs. 6, 12–15 |
| C5 | n-gram statistics are moments of one-hot sequences, and so of embeddings | strong | Theorems 2.1–2.2, elementary |
| C6 | Higher-order terms of the loss's Taylor expansion become relevant later | weak | an informal argument, §2.1 |
| C7 | The return of the n-gram loss is caused by in-context learning | weak | timing coincidence in Pythia-12B, Fig. 7 |

## Method

- **Gaussian OT** maps class P to class Q by T(x) = A(x − µ_P) + µ_Q,
  A = Σ_P^(−1/2)(Σ_P^(1/2) Σ_Q Σ_P^(1/2))^(1/2) Σ_P^(−1/2) (Eq. 3), with
  shrinkage covariance estimates.
- **First-order grafting.** Coordinatewise quantile normalization
  F_Y^(−1)∘F_X, and the bounded mean shift of App. D.
- **Maximum-entropy sampling.**
  - First order: independent coordinate sampling, from empirical
    marginals or from fitted Conrad densities.
  - Second order: Gaussian sampling.
  - Second and third order in [0,1]^d: gradient-based optimisation of
    a sample set that matches the statistics while maximising the
    Kozachenko–Leonenko entropy estimate.
- **Language.** Sequences of 2049 tokens are sampled from maximum-entropy
  1- to 4-gram models of the Pile, then evaluated at Pythia's public
  log-spaced checkpoints.

## Concepts

- **Distributional simplicity bias (DSB).** Networks "learn low-order
  moments of the data distribution first, before moving on to
  higher-order correlations".
- **Uses statistics up to order k.** The two criteria of §2.2: sensitive
  to grafting the first k statistics, robust to deleting the rest.
- **n-gram statistic.** Def. F.1: a joint probability of tokens at fixed
  positions, which includes skip-grams.

## Connections

It inverts Refinetti, Ingrosso and Goldt (2023), who trained on synthetic
data of increasing order. It places itself beside the frequency principle
(Xu et al. 2019; Rahaman et al. 2019) and spectral-bias work on the NTK,
which order learning by Fourier frequency or kernel eigenvalue rather than
by statistical order. Choshen et al. (2022) found the same unigram-then-
bigram match in language models by different means.

## Bearing on the record

- **[QUESTION-039](../questions.d/QUESTION-039.md).** A partial, empirical answer on order: statistical
  order of the input distribution, first then second, with higher orders
  later. It says nothing exact about the moment. Peaks fall between about
  2^4 and 2^12 steps, depend on dataset, and are insensitive to model
  scale. It also shows that acquiring later structure can *remove*
  earlier behaviour, which bears on whether acquisition is one kind of
  event. This reading is held as [THEORY-279](../theory.d/THEORY-279.md).
- **[THEORY-229](../theory.d/THEORY-229.md), filed today from [LIT-242](../literature.d/LIT-242.md), and [THEORY-086](../theory.d/THEORY-086.md).** These order
  acquisition by eigenvalue of a second-moment operator: the
  cross-correlation Γ, or the NTK Gram matrix. Everything they learn is a
  function of second-order statistics of the data. So they describe, at
  most, the phase Belrose et al. find early in training, and they predict
  nothing for the higher-order phase or the loss of low-order
  sensitivity. The paper does not test a spectral account. It does not
  say that the early phase is eigenvalue-ordered.
- **[THEORY-204](../theory.d/THEORY-204.md) and [THEORY-201](../theory.d/THEORY-201.md).** These set the moment at which a
  language model uses a token correlation by when its pairwise statistic
  rises above sampling noise. Belrose et al.'s unigram-before-bigram order
  in Pythia is consistent with that, but it is measured in training steps
  on a fixed corpus, not in examples, and it is not a test of the horizon.
- **[THEORY-039](../theory.d/THEORY-039.md).** Its caution that later phases "differ in kind" is
  matched here. The rise of the n-gram loss and its later fall by
  in-context learning are two different events on one curve.
- **[LIT-952](../literature.d/LIT-952.md)'s seeded claim is right in substance.** It says that "low-order
  moments are learned before higher-order ones". The paper shows this for
  first against second order, and for the use of statistics rather than
  their learning. Third-order evidence is thin: the third-order curves are
  shown only in the appendix figures and are not discussed in the text.
- **No instruction for machine-learning practice.**

## Limitations

- The ordering is shown for orders one and two. "Increasing complexity"
  beyond second order is not measured as an ordered sequence.
- The Taylor argument is a motivation, not a derivation of dynamics. It
  needs analytic losses and well-behaved derivatives, and it gives no
  timescale.
- The maximum-entropy samples for higher orders are approximate, and the
  third-order samples match the coskewness only along random slices
  (App. G).
- The return of the language-model loss is attributed to in-context
  learning on correlational evidence only.
- All vision runs use 32×32 or 64×64 images, because Gaussian OT costs
  O(d³).

## Open questions

- Does the peak time for order-k sensitivity scale with anything
  measurable, such as the magnitude of the order-k class differences? A
  sweep that varied those magnitudes would answer it.
- Is the later loss of low-order sensitivity forgetting, as the authors
  suggest for small Pythia models, or a reweighting that a probe could
  recover?
