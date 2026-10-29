---
status: Proposed
promote_when: >-
  Results that separate the query rule from the luck of the draw and from
  the benchmark's structure: per-cell variances or paired tests across
  runs; evaluation restricted to objects never labeled; and at least one
  setting where the initial alignment is badly wrong or the true
  correspondence is far from one-to-one, so that a rule which sharpens the
  current plan can be seen to fail. Further wins on the same benchmarks,
  by similar margins, do not settle it.
title: 'Choosing which source objects to have an oracle match, by the derivative of a proxy utility of the entropic transport plan (its nearness to a permutation, or its consistency with the graphs) with respect to supervising each candidate match, averaged over matches by the current plan, raises held-out alignment accuracy more than uncertainty, centrality and matching-sampling query rules at the same label budget, by up to about three points on network alignment and less on image–text tasks; the gain depends on weighting by the current plan, without which the rule does worse than random'
version: 1
tags:
- mathematics
- network-science
date: '2026-10-29'
source:
- LIT-tmpe5bbx
summary: >-
  Yu et al. (2026), LIT-tmpe5bbx, Tables 3–5 and 7, read in NOTE-tmp60yfn.
  Eight datasets, four aligners, a budget of 20% of true pairs in ten
  rounds after a random 20%, five runs, no variances. Proposed: an
  empirical result with small margins, on benchmarks where the truth is
  near one-to-one, so a coherence proxy and accuracy agree. It chooses
  among fixed questions; it does not extend what can be asked.
---
<!-- inactive-ok-file: TERM-092 — Proposed; the term whose distinction this result respects -->

# THEORY-tmpzfqlq: Choosing which source objects to have an oracle match, by the derivative of a proxy utility of the entropic transport plan (its nearness to a permutation, or its consistency with the graphs) with respect to supervising each candidate match, averaged over matches by the current plan, raises held-out alignment accuracy more than uncertainty, centrality and matching-sampling query rules at the same label budget, by up to about three points on network alignment and less on image–text tasks; the gain depends on weighting by the current plan, without which the rule does worse than random

## Source

Yu et al. (2026), LIT-tmpe5bbx, §5 and Appendices B–C of arXiv
2605.24395v2; read in NOTE-tmp60yfn.

## What was actually shown

**What is chosen.** A source object x_s from the pool of unlabeled ones;
the oracle returns its true match, and that pair's cost is set to zero
(β = 1). Scores: Definition 4.4 with Lemma 4.2 (THEORY-tmpr2ueq).

**Under what budget.** 20% of true pairs given at random, then 20% more
chosen, in ten batches; every strategy gets the same budget (p. 19).

**What is evaluated.** MRR for network alignment (Phone-Email,
ACM-DBLP plain and attributed, Douban; aligners PARROT and JOENA) and
Recall@1 for image–text retrieval (CIFAR-10-C, ImageNet-C) and grounding
(COCO, Flickr30K) with GOT-W and GOT-FGW; five runs averaged.

**Result.** The best AvAtar variant is best in every cell of Tables 3–5.
On network alignment its margin over the best baseline is 0.003 to 0.028
MRR, over Random 0.027 to 0.158 (my computation from Table 3). On the
image–text tasks the margins over the best baseline are under 0.025. The paper
reports the consistency utility "typically" ahead of the L2 utility on
plain networks and behind on attributed ones (p. 7); on ACM-DBLP-P with
PARROT it is behind. Weighting pair impacts uniformly instead of by T
drops Douban MRR from 0.837 to 0.669, below Random (0.751), and Phone-Email
from 0.629 to 0.522, below Random (0.568) (Table 7 with Table 3).

**What could have failed.** The gradient score could have been no better
than entropy or margin sampling, which use the same plan without the
gradient. It was better, by small margins.

## What this does not say

- **That the margins are reliable.** No variances, no tests; many margins
  are under one point.
- **That the rule extends what can be asked.** Every query has the same
  fixed form over fixed object sets and cost (TERM-092's distinction). It
  allocates a budget among askable questions.
- **That the proxy tracks accuracy in general.** The utilities reward a
  sharper or more graph-consistent plan. Where the current plan is wrong,
  or the truth is not near one-to-one, sharpening could reinforce error;
  no such case is tested, and Table 7 shows how much the rule leans on the
  current plan.
- **That the gradient is exact for the aligners used.** Lemma 4.2 assumes
  fixed-cost entropic OT; PARROT, JOENA and GOT-FGW are not that.
- **Whether labeled objects count in the score.** Not stated (p. 19).
