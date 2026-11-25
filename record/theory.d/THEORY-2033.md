---
number: 2033
status: Proposed
formerly:
- THEORY-tmpl3nl5
title: 'Contrastive loss splits into alignment, uniformity'
statement: >-
  Wang and Isola show that, as the number of negative samples grows, the
  normalized InfoNCE loss on the unit hypersphere converges to an alignment
  term, minimized exactly by encoders that map both members of every
  positive pair to the same feature, plus a uniformity term, minimized by
  encoders whose features are uniformly distributed on the sphere when such
  encoders exist; on a finite augmented dataset the two optima cannot both
  be met
version: 1
source:
- LIT-2819
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-171
promote_when: >-
  The proof of Theorem 1 (Appendix A.2) is checked step by step, including
  the O(M^−1/2) rate corrected in v10 and the claim that perfectly uniform
  encoders exist when n ≥ m − 1 and the data density is bounded.
summary: >-
  From the reading of [LIT-2819](../literature.d/LIT-2819.md) in [NOTE-2113](../notes.d/NOTE-2113.md). Wang, Isola (2020),
  ICML 2020 (PMLR 119), arXiv 2005.10242. As the number of negatives
  grows, the normalized InfoNCE loss on the unit hypersphere converges to
  an alignment term, minimized exactly when both members of every positive
  pair share a feature, plus a uniformity term, minimized by a uniform
  distribution of features on the sphere. On a finite augmented dataset
  the two optima cannot both be met, and weighting alignment far above
  uniformity maps every input to one vector. Across several hundred
  encoders, low alignment and uniformity losses go with good downstream
  accuracy, and optimizing them directly matches or beats the contrastive
  loss. Here because A27 used it for how self-supervised learning
  contracts some distinctions and keeps others ([CLAIM-481](../claims.d/CLAIM-481.md)'s note of
  2026-11-19, [CLAIM-762](../claims.d/CLAIM-762.md)). It supports that split but is not spectral
  and says nothing of the classes kept. Read in its NOTE.
---
<!-- inactive-ok-file: CLAIM-762 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-2188 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# THEORY-2033: Contrastive loss splits into alignment, uniformity

## The account

For the InfoNCE loss with temperature τ and M negatives on ℓ2-normalized features, Theorem 1 gives lim_{M→∞} [L(f; τ, M) − log M] as the sum of −(1/τ) E_pos[f(x)ᵀf(y)], which is minimized iff f is perfectly aligned, and E_x log E_{x⁻} exp(f(x⁻)ᵀf(x)/τ), whose exact minimizers are the perfectly uniform encoders when any exist. The deviation from the limit is O(M^−1/2). The uniform measure on the sphere is the unique minimizer of the expected pairwise Gaussian potential (Proposition 1), which motivates the Luniform metric. With one negative, the conditional result (Theorem 2) is weaker. Empirically, across several hundred encoders on four benchmarks, low Lalign and low Luniform go with good downstream performance, and optimizing them directly matches or beats the contrastive loss.

## What it does not show

It does not show which encoder gradient training reaches, what happens at finite M beyond the rate, or what the optimum is when perfect alignment and perfect uniformity conflict (always, on a finite augmented dataset). It says nothing about which classes beyond the augmentation the representation recovers, and nothing spectral or graph-theoretic.

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi ([LIT-2975](../literature.d/LIT-2975.md), [NOTE-2277](../notes.d/NOTE-2277.md), [THEORY-2188](THEORY-2188.md)): **qualifies, and
goes further.** They prove a closed-form large-batch limit at finite τ, in
value and gradient, beyond the asymptotic decomposition read here, and
reread uniformity as "entropy-driven spreading inside the alignment basin"
rather than "a global force opposing alignment". That answers what this
account leaves open, the optimum when perfect alignment and perfect
uniformity conflict: alignment picks the basin, and entropy spreads mass
within it, selecting "the most internally dispersed near-optimal
configuration". The optimum is a Gibbs law, not a uniform one. A
refinement of the same objective, read in a different form; a note, no
relation.
