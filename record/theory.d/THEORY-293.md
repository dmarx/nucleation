---
number: 293
status: Active
formerly:
- THEORY-tmpxwps9
title: "For an optimal capacity-bounded learner on an orthogonal mixture of equally frequent random facts and a second domain, the facts are learned not at all below a capacity threshold set by the mixing ratio and in full once capacity exceeds it by the facts' total entropy, and Pythia models trained on synthetic biographies mixed into web text show a threshold in model size and in mixing ratio"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-293 (batch 036, ADR-047 v2 and
    v3). Theorem 4.3 was re-derived by an exchange argument, in the dated
    note below. The title now says the facts are learned in full only once
    capacity exceeds the threshold by their total entropy, as the theorem
    states, and that the Pythia models show a threshold, not the same
    threshold: that the networks' thresholds are the optimal learner's
    rests on one exponent with no interval (NOTE-796). The data are named
    rather than called such mixtures, since web text is not shown to be
    orthogonal to the biographies. The former promote_when, the test of
    that link, moves to QUESTION-176.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 070, ADR-047 v4) filed THEORY-tmptwk75,
    Proposed, to carry what the narrowing dropped. This entry's status,
    title and claims are unchanged; a dated note says what moved.
tags:
- learning-theory
- information-theory
date: '2026-10-14'
source:
- LIT-984
summary: >-
  Gu, Lyu, Li and Zhang (2025), [LIT-984](../literature.d/LIT-984.md), read in [NOTE-796](../notes.d/NOTE-796.md). Proved
  for an idealised learner whose capacity is mutual information with the
  data (Theorem 4.3), on an orthogonal mixture of uniform facts and a
  second domain; seen in Pythia models from 14M to 6.9B on synthetic
  biographies mixed into web text. The theory is static. It does not say
  when in training the facts arrive, and it does not show that SGD
  reaches the optimal allocation.
answers:
- QUESTION-039
extended_by:
- THEORY-tmptwk75
---
<!-- inactive-ok-file: THEORY-tmptwk75 — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->
<!-- inactive-ok-file: THEORY-039 — Proposed; partial answers to the same question, compared, not leaned on -->

# THEORY-293: For an optimal capacity-bounded learner on an orthogonal mixture of equally frequent random facts and a second domain, the facts are learned not at all below a capacity threshold set by the mixing ratio and in full once capacity exceeds it by the facts' total entropy, and Pythia models trained on synthetic biographies mixed into web text show a threshold in model size and in mixing ratio

## Source

Gu, Lyu, Li and Zhang (2025), [LIT-984](../literature.d/LIT-984.md) (arXiv 2505.18091v3, NeurIPS
2025), read in full in [NOTE-796](../notes.d/NOTE-796.md): §4 and Appendix F (the theory),
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

## Note of 2026-10-19: Theorem 4.3, re-derived

The source's assumptions: capacity splits additively, m1 + m2 ≤ M,
between the facts and the second domain, because the mixture is
orthogonal (Definition F.5). The facts' best loss falls with slope −p
per unit of capacity until m1 reaches their total entropy Htot (Theorem
4.2). The second domain's best loss F_P2 is convex and non-increasing.
The learner minimises r·F_P1(m1) + (1 − r)·F_P2(m2). Put
t = r·p/(1 − r).

1. A unit of capacity given to the facts lowers the loss by r·p. Given to
   the second domain at m2, it lowers it by (1 − r)·(−F′_P2(m2)), which
   does not increase with m2.
2. Below. Let M ≤ M₀⁻(t), the supremum of the sizes at which −F′_P2 > t.
   If an optimum gave the facts m1 > 0, then m2 < M₀⁻, so −F′_P2(m2) > t,
   and moving a little capacity from the facts to the second domain would
   lower the loss. So no optimum learns any of the facts.
3. Above. Let M ≥ M₀⁺(t) + Htot, with M₀⁺(t) the infimum of the sizes at
   which −F′_P2 < t. If an optimum gave the facts m1 < Htot, it would use
   all its capacity (spare capacity given to the facts lowers the loss),
   so m2 > M₀⁺ and −F′_P2(m2) < t, and moving a little capacity from the
   second domain to the facts would lower the loss. So every optimum
   learns all of them.
4. In between, the facts take every further unit until Htot is spent, so
   recall rises linearly over a width of Htot.
5. With F_P2 = C + A·M^(−α), −F′_P2(M) = αA·M^(−(α+1)) = t gives
   M₀ = (αA(1 − r)/(r·p))^(1/(α+1)), which scales as
   (1/(r·p))^(1/(α+1)) for small r.

The Pythia half is accepted under [ADR-047](../decisions.d/ADR-047.md) v3 as one study read in full
([NOTE-796](../notes.d/NOTE-796.md), C3): near-zero recall below a model size that falls as r
rises, and below a mixing ratio at fixed size (70M: 0.4% at r ≤ 0.2 to
58.1% at 0.45 over three seeds), then a steep rise. Whether those
thresholds are the optimal learner's is [QUESTION-176](../questions.d/QUESTION-176.md).

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 070) filed [THEORY-tmptwk75](THEORY-tmptwk75.md)
as Proposed, extending this entry. It carries the link this entry's title
asserted before batch 036 narrowed it: that SGD-trained language models
reach the capacity-optimal allocation, so their fact-learning thresholds in
model size and mixing ratio are the optimal learner's, as Gu, Lyu, Li and
Zhang propose. The measured size exponent, 1.152 against a predicted 1.283,
is recorded against it there. This entry is its evidence and is not changed
by the filing.
