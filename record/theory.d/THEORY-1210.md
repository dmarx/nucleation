---
number: 1210
status: Proposed
formerly:
- THEORY-tmph970r
promote_when: >-
  An ablation in which a joint multi-marginal coupling and independently
  fitted pairwise couplings share the same cost, the same anchors and the
  same search space, scored on held-out correspondences on two kinds of
  data: data whose true correspondences are transitive, and data where
  some are not, such as maps through an intermediate network that loses or
  merges distinctions. The account is supported if the joint fit wins on
  the first kind without losing pairwise accuracy on the second; it is
  weakened if it gains only where the truth is consistent by construction.
  A further comparison of HOT against other methods on consistent
  benchmarks does not settle it.
title: 'When several networks are aligned, fitting one joint multi-marginal coupling finds held-out correspondences better than fitting them in pairs, and the gain comes from the joint fit itself, not from the cost or the search space that come with it'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-30'
source:
- LIT-1814
extends:
- THEORY-1159
summary: >-
  Zeng et al.'s (2024) attribution of HOT's gains to joint alignment
  ([NOTE-1334](../notes.d/NOTE-1334.md)'s C6, asserted without an ablation), kept here when the
  twenty-second status review narrowed and promoted [THEORY-1159](THEORY-1159.md) ([ADR-065](../decisions.d/ADR-065.md);
  [ADR-047](../decisions.d/ADR-047.md) kind 1). No ablation in the record holds the RWR cost and the
  clustering fixed, and every benchmark's truth is consistent by
  construction.
---

<!-- inactive-ok-file: QUESTION-319 — Open; the question the comparison cannot reach, cited as open -->

# THEORY-1210: When several networks are aligned, fitting one joint multi-marginal coupling finds held-out correspondences better than fitting them in pairs, and the gain comes from the joint fit itself, not from the cost or the search space that come with it

## Source

Zeng et al. (2024), [LIT-1814](../literature.d/LIT-1814.md), §5 (pp. 5–7) of arXiv 2310.04470v2; read in
full in [NOTE-1334](../notes.d/NOTE-1334.md). What the experiments showed is [THEORY-1159](THEORY-1159.md), which this
entry extends; the identity behind joint fitting is [THEORY-1132](THEORY-1132.md).

## The thesis

The paper attributes HOT's larger margins on high-order hits to aligning
the networks jointly rather than in pairs (p. 5). If that is right, joint
fitting is a useful regularizer wherever the true correspondences are
transitive.

## Why it is not held

HOT changed three things at once: the random-walk-with-restart cost from
shared anchors, the cluster decomposition, and the joint coupling. No
ablation holds the first two fixed while changing the third, and on
attributed DBLP the plain version does nearly as well, which the paper
credits to the cost (p. 13). Every benchmark's truth is a consistent set of
triples, so the comparison cannot show whether consistency costs true
local distinctions where the truth is not transitive ([QUESTION-319](../questions.d/QUESTION-319.md)).
