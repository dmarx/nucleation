---
status: 'Active'
status_note: 'read in full 2026-10-03 ([NOTE-tmpkvaq5](../notes.d/NOTE-tmpkvaq5.md)); the other founding demonstration of mode connectivity, reached independently of Garipov et al. by borrowing the nudged elastic band from chemical physics. Over ten minima per architecture, the highest training loss on the best paths found is almost the minima''s own for deep ResNets and DenseNets on CIFAR-10, with a small residual gap on CIFAR-100, and barriers fall as networks get wider and especially deeper. Its two explanations, resilience and redundancy, are qualitative; the redundancy toy (swapping two hidden units needs a third) is the first statement in this batch of why a permutation costs a barrier without spare capacity.'
title: 'Essentially No Barriers in Neural Network Energy Landscape'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv PDF of 1803.00885 v5 (22 February 2019; 12
    pages), text extracted with PyMuPDF: §§1–6 and Appendices A–B. Table
    B.1's column values did not survive extraction cleanly and were not used;
    the figures it summarizes were taken from the text of §4.3 and Appendix
    B. Published in ICML 2018, PMLR 80 (the arXiv journal reference gives
    pp. 1308–1317). `published:` is the v1 date, 2 March 2018. Not held in
    the Anthology of the SOTA: a grep of its record for the arXiv id,
    "Draxler" and the title found nothing.
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
published: '2018-03-02'
arxiv: '1803.00885'
first_author: 'Draxler'
keywords:
- 'energy landscape'
- 'minimum energy path'
- 'nudged elastic band'
- 'AutoNEB'
- 'saddle points'
- 'mode connectivity'
implementations:
- 'https://github.com/fdraxler/PyTorch-AutoNEB'
summary: >-
  Draxler, Veschgini, Salmhofer & Hamprecht (2018), ICML 2018. Using
  AutoNEB, a minimum-energy-path method from molecular statistical
  mechanics, the paper connects ten minima per architecture for CNNs,
  ResNets and DenseNets on CIFAR-10 and CIFAR-100. The saddle losses on the
  best paths are almost those of the minima for deep architectures, and
  test error rises by at most a few tenths of a percent on CIFAR-10. The
  conclusion is that minima are points on one connected low-loss manifold,
  not bottoms of separate valleys, and that the effect grows with width and
  especially depth.
compared_against:
- LIT-tmpcuw4i
extended_by:
- LIT-tmp3owu9
- LIT-tmplpsy5
---

# LIT-tmp3kyq9: Essentially No Barriers in Neural Network Energy Landscape

Felix Draxler, Kambis Veschgini, Manfred Salmhofer and Fred A. Hamprecht
(2018), *Proceedings of the 35th International Conference on Machine
Learning*, PMLR 80 — [ARXIV-1803.00885](https://arxiv.org/abs/1803.00885)

## Key takeaways

- **The barriers between minima are essentially zero for deep networks.**
  The paper seeks the minimum energy path (MEP) between two minima, the path
  whose highest loss is lowest, and approximates it with AutoNEB (§3.1). For
  ResNet-20 to -56 and DenseNets on CIFAR-10, the training loss at the
  highest point of the best paths is almost that of the minima. On CIFAR-100
  a small gap remains, which is small against the loss of an untrained
  network. Test error rises by at most 0.5% on CIFAR-10 and 2.2% on CIFAR-100
  for all deep architectures (§4.3).
- **Depth and width remove barriers; harder data raises them.** Across CNNs of
  varying width and depth, barriers fall as networks get wider and especially
  deeper (Fig. 5).
- **Paths are cheap to bound jointly.** Concatenating paths gives an
  ultrametric inequality, L*_AC ≤ max{L_AB, L_BC}, so the best paths among ten
  minima form a minimum spanning tree, and bad local MEPs can be routed
  around (§3.2, Algorithm 3).
- **The barrier is crossed late in training.** The training loss falls below
  the mean saddle energy only after the first learning-rate decay, and for
  most deep networks after the second (Fig. 6).
- **Two explanations, both qualitative** (§5): *resilience*, many parameters
  can compensate for a change in one; and *redundancy*, illustrated by XOR. A
  two-unit network cannot swap its hidden units Alice and Bob without
  misclassifying a point on the way, but with a third unit, Charlie, standing
  in, the swap is free.

## Standing in the record

Filed with the batch [ADR-027](../decisions.d/ADR-027.md) opened `loss-landscapes` for. It is the second
of the two founding papers, beside Garipov et al. ([LIT-tmpotq71](LIT-tmpotq71.md)). The two
**cite each other as simultaneous and independent**: this paper's §2 says
that after its ICML submission Garipov et al. "independently reported" the
same observation, and its conclusion proposes using the paths as an ensemble
"(Garipov et al., 2018)". Garipov et al.'s §2 returns the credit. No relation
is declared, because neither builds on the other.

The redundancy argument deserves keeping. It is the earliest statement in this
batch that exchanging two hidden units, a permutation, costs a barrier unless
the network has a unit to spare. Kuditipudi et al. ([LIT-tmplpsy5](LIT-tmplpsy5.md)) make that
argument a proof: a network that can drop half its units can permute the rest
along a zero-loss path (their Lemma 4). Entezari et al. ([LIT-tmp2uwzo](LIT-tmp2uwzo.md)) turn
it around: the barriers seen on straight lines are what permutations cost, and
removing the permutation removes the barrier.

Frankle et al. ([LIT-tmp3owu9](LIT-tmp3owu9.md)) borrow this paper's Table B.1 to calibrate their
2% threshold for "no barrier".

The method is from chemical physics (nudged elastic band, Jónsson et al.
1998), and the paper treats loss as energy. That is a borrowed tool, not a
claim about physics, so no `natural-sciences` tag.
