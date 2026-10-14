---
status: Proposed
promote_when: >-
  A test of the link from the optimal learner to trained networks, on the
  quantity the theory predicts: the threshold model size or mixing ratio,
  predicted in advance from the measured loss-versus-size curve of the
  second domain and the facts' total entropy Htot, matched by networks
  trained to convergence over several seeds and several values of r, with
  recall rising over a width of about Htot past the threshold. It is
  refuted if the measured thresholds depart systematically from
  (1/(r·p))^(1/(α+1)), or if networks below the threshold do learn the
  facts given enough further training, which would make the wall a matter
  of dynamics and not of allocation. More sigmoid-shaped curves in r or in
  size are the wrong kind of evidence: they show a threshold, not that
  capacity allocation sets it.
title: 'For an optimal capacity-bounded learner on a mixture of equally frequent random facts and a second domain, the facts are learned not at all below a capacity threshold set by the mixing ratio and in full above it, and Pythia models trained on such mixtures show the same threshold in model size and in mixing ratio'
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-14'
source:
- LIT-984
summary: >-
  Gu, Lyu, Li and Zhang (2025), [LIT-984](../literature.d/LIT-984.md), read in [NOTE-tmplnu3m](../notes.d/NOTE-tmplnu3m.md). Proved
  for an idealised learner whose capacity is mutual information with the
  data (Theorem 4.3), on an orthogonal mixture of uniform facts and a
  second domain; seen in Pythia models from 14M to 6.9B on synthetic
  biographies mixed into web text. The theory is static. It does not say
  when in training the facts arrive, and it does not show that SGD
  reaches the optimal allocation.
answers:
- QUESTION-039
---
<!-- inactive-ok-file: THEORY-187 THEORY-204 THEORY-039 THEORY-229 — Proposed; partial answers to the same question, compared, not leaned on -->

# THEORY-tmpxwps9: For an optimal capacity-bounded learner on a mixture of equally frequent random facts and a second domain, the facts are learned not at all below a capacity threshold set by the mixing ratio and in full above it, and Pythia models trained on such mixtures show the same threshold in model size and in mixing ratio

## Source

Gu, Lyu, Li and Zhang (2025), [LIT-984](../literature.d/LIT-984.md) (arXiv 2505.18091v3, NeurIPS
2025), read in full in [NOTE-tmplnu3m](../notes.d/NOTE-tmplnu3m.md): §4 and Appendix F (the theory),
§§3 and 5 with Appendices D.1, D.2, D.4 and E.5 (the experiments).

## What was actually shown

**The theorem.** A learner is optimal under capacity M if it minimises
expected cross-entropy subject to I(A(D_θ); D_θ) ≤ M (Definition 4.1).
The data are a mixture D_θ = r·D⁽¹⁾ + (1−r)·D⁽²⁾ of K random facts, all
of exposure frequency p with target entropies summing to Htot, and a
second domain whose best loss F_P2(M) is convex in M. The domains share
no information (Definition F.5). Then any optimal learner learns nothing
of the facts if M ≤ M₀⁻(r·p/(1−r)), and all of them if
M ≥ M₀⁺(r·p/(1−r)) + Htot, where M₀ marks the size at which the second
domain's marginal loss reduction −F′_P2(M) falls through r·p/(1−r)
(Theorem 4.3, proved in App. F.3 from two exchange lemmas). Without the
second domain, loss falls linearly in M and there is no threshold
(Theorem 4.2). If F_P2 = C + A·M^(−α), the threshold is
M_thres ~ (1/(r·p))^(1/(α+1)), and a single fact's threshold frequency
is f_thres ~ M^(−(α+1)) (eqs. 4–6).

**The experiments.** Pythia models trained on SynBio biographies mixed
into FineWeb-Edu recall almost none of them below a model size that falls
as r rises (14M–410M, r = 0.1–0.4, Fig. 1), and below a mixing ratio at
fixed size (70M: 0.4% mean accuracy at r ≤ 0.2 rising to 58.1% at 0.45
over three seeds, Table 1; 410M, 2.8B and 6.9B, Figs. 2 and 9). This
could have come out otherwise: recall could have grown smoothly with r
or size, as it does with size on knowledge data alone. At r = 0.2, 4 to
16 times more training leaves recall near zero, and the steps to 40%
accuracy grow faster than an exponential fit in 1/r below r = 0.3
(Figs. 3–4). On a set with power-law frequencies, the threshold
frequency falls with size with log–log slope −1.152, against −1.283
predicted from the fitted web-loss exponent α ≈ 0.283 (Fig. 7a–b).

## What this does not say

- **It does not say that trained networks are optimal learners.** The
  theorem is about the optimum of an information-constrained problem.
  That SGD-trained Pythia models reach it is a modelling assumption,
  supported by the shape of the curves and by one exponent within about
  10%, with no interval.
- **It does not say when in training acquisition happens.** The theory
  has no time in it. The finding that longer training barely helps below
  the threshold is empirical. It is consistent with an allocation that
  never reaches the facts, and also with a dynamical wall the theory does
  not model; the paper does not separate the two.
- **It does not say the transition is a jump.** In the theorem, past M₀
  the second domain's share stays fixed and the facts take every further
  bit until Htot is spent: recall rises linearly over a width of Htot. It
  is abrupt only when Htot is small beside the threshold.
- **It does not cover real knowledge directly.** Facts in real data
  differ in frequency and overlap with web text. The authors say a
  heterogeneous set may show no visible transition, and claim the
  threshold per fact. The open-model evidence for that (PopQA popularity
  thresholds) uses page views as a frequency proxy and an LLM judge, and
  its slopes differ by family.
- **It is not the practice.** That small mixing ratios can be useless for
  small models, and the subsampling and rephrasing strategies of §6, are
  advice for training and are not filed here.

## Connections

- **[QUESTION-039](../questions.d/QUESTION-039.md).** It answers part of the question: one thing that sets
  whether, and at what size and mixture, a structure is acquired is
  competition for capacity with other data, through the ratio of marginal
  values r·p/(1−r) against −F′_P2(M). This is a cause of a different kind
  from those the question holds, and the question's answer test (two
  mechanisms predicting different timings in one setting) is not met
  here.
- **[THEORY-086](THEORY-086.md), [THEORY-187](THEORY-187.md) and [THEORY-229](THEORY-229.md)** set the time at which a
  structure is fitted within one task, by eigenvalue and initial scale.
  This sets whether it is fitted at all, across tasks, by capacity. A
  setting in which both apply would be a knowledge set mixed into a task
  with a known spectrum, trained from small initialisation.
- **[THEORY-204](THEORY-204.md)** sets a correlation horizon by data size P. Here the
  threshold is in model capacity, at fixed and ample data.
- **[THEORY-039](THEORY-039.md).** A further kind of transition: in what the end of
  training holds, as a function of mixture and size, not a phase within
  one run.
