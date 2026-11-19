---
status: Read
paper: LIT-tmpjmy81
title: 'Rajendran and others 2020 — Meta-Learning Requires Meta-Augmentation'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2007.05549 (served arXiv:2007.05549v2, 4
    Nov 2020; HTTP 200, application/pdf). Kind of copy (step 5): arXiv
    preprint posted by the authors, the NeurIPS 2020 version ("34th
    Conference on Neural Information Processing Systems (NeurIPS 2020)" in
    the copy); lawful. Date: 2026-11-19. Nothing stopped the fetch. Text
    extracted with pdftotext to dl/text.txt. Read: abstract and sections 1-6
    in full (background and the two forms of meta-overfitting, meta-
    augmentation and Theorem 1, related work, Omniglot/Mini-ImageNet/D'Claw
    classification, sinusoid and Pascal3D regression, discussion, broader
    impact). Skipped: appendices (proof of Theorem 1, ImageNet augmentation
    ablation, regression details), references. Table 1's numbers did not
    survive text extraction; the accuracies quoted are those stated in the
    running text.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp3nxjy: Rajendran and others 2020 — Meta-Learning Requires Meta-Augmentation

## Contribution

Rajendran, Irpan and Jang (NeurIPS 2020) separate two forms of
meta-learning overfitting, memorization overfitting (the model ignores the
base learner and the support set) and learner overfitting (the base learner
itself fails to generalize to new tasks), and propose meta-augmentation:
add random bits to the labels of each task, the same key in support and
query, so that the model must recover the key from the support set.
Augmentations that raise the conditional entropy H(Y|X) make tasks mutually
exclusive and add task variety. Label shuffling in standard few-shot
benchmarks is shown to be such an augmentation.

## Key results

- **Two overfittings** (abstract): "we can now overfit in either the model
  or the base learner".
- **Augment labels, not inputs** (§1): "classical data augmentation adds
  noise to inputs x without changing y, but for meta-learning we must do
  the opposite: add noise to labels y, without changing inputs x".
- **Learner overfitting** (§2): it "can happen both in
  non-mutually-exclusive and mutually-exclusive task settings, and can be
  thought of as the meta-learning version of classical machine learning
  overfitting".
- **Theorem 1** (§3): with an invertible label transform, H(Y′|X) = H(Y|X)
  + H(ε), so the learner must extract at least H(ε) bits from the
  support set; "This reduces memorization overfitting".
- **Shuffling matters more than variety** (§5.1, Mini-ImageNet MAML): "an
  increase in accuracy from 30% to 43% between nonmutually-exclusive and
  intrashuffle, and only 43% to 46% between intrashuffle and intershuffle".
- **Which overfitting appears depends on the seed** (§5.1, Fig. 4):
  "whether they exhibit memorization overfitting or learner overfitting
  depends on random seed".
- **Enough data can avoid it** (§5.1, Omniglot): non-mutually-exclusive
  MAML still reached 98%, suggesting "it is still possible to learn models
  which do not overfit and generalizes to novel test-time tasks if there
  is sufficient training data".
- **Complementary to Yin et al.** (§5.2, Table 2): on Pascal3D pose
  "meta augmentation provides large improvements on top of IB
  regularization"; MR-MAML (β=0) with augmentation 1.71 vs 2.34 without;
  "weight decay limited the baseline performance of MAML".
- **Limit** (§6): "Distribution mismatch between train-time tasks and
  test-time tasks can be lessened through augmentation, but augmentation
  may not entirely remove it."

## Assumptions

- The meta-learner is a black box f((xs, ys), xq) → ŷq.
- An invertible label transform exists for the task (permutation for
  classification, additive noise for scalar regression).
- Test tasks are related to training tasks; augmentation widens the
  training distribution, it does not create the test one.

## Concepts

- **Memorization overfitting** and **learner overfitting**.
- **Meta-augmentation**; **CE-preserving** vs **CE-increasing**
  augmentation.
- **Intrashuffle** and **intershuffle** task construction.
- **Mutually exclusive** task sets.

## Bearing on the record

- **[CASE-tmphsr99](../cases.d/CASE-tmphsr99.md)**: supports the case's guard against meta-overfitting and
  adds a second failure to guard: learner overfitting survives mutual
  exclusivity, so held-out task-generating processes, not only shuffled
  labels, are needed, as the case says. Two practical rules for the
  meta-trained arm: run several seeds (the form of overfitting is
  seed-dependent) and report pre- and post-update accuracy on training and
  validation tasks (their Fig. 4 diagnostic). Their note that weight decay
  hurt the MAML baseline is a caution for the case's higher-weight-decay
  arm, in a different setting.
- **[CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)**: qualifies it as Yin et al. do: the loss of the capacity
  to adapt that they observe is named overfitting, of the model or of the
  learner. Learner overfitting is a closer neighbour to overconsolidation
  than memorization is, and the claim should say how they differ.
- **[QUESTION-tmpwqepn](../questions.d/QUESTION-tmpwqepn.md)**: leaves open. Its limit sentence says augmentation
  narrows but does not remove train/test task mismatch, which is the
  question's unspecifiable future in miniature.

## Limitations

- Small benchmarks and small models; MAML, CNP, Matching and Prototypical
  networks only.
- Uniform noise made MAML underfit on Pascal3D; a discrete noise set was
  chosen instead, so augmentation strength needs tuning.
- Theorem 1 bounds information the learner must extract; it does not show
  that generalization to new tasks follows.
