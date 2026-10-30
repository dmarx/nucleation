---
number: 1218
status: Proposed
formerly:
- THEORY-tmptcb8e
title: 'In a sparsely-gated mixture-of-experts layer trained without balancing losses, the gate''s concentration on a few experts arises by self-reinforcement: favoured experts are trained more rapidly and so are selected still more'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Filed by the twenty-second status review, at the status review's ruling
    (the owner delegated these rulings), with THEORY-927's old promote_when,
    less one clause: "and the ICLR 2017 version read and found to report
    Table 6 as v1 does". That clause demands the version of record with no
    discrepancy named, so ADR-065 §4 strikes it; NOTE-1145 records that
    arXiv v1, the only arXiv version, was read.
tags:
- learning-theory
- complex-systems
date: '2026-10-30'
source:
- LIT-1507
extends:
- THEORY-927
promote_when: >-
  A study that tracks gate weights over training in a sparsely-gated mixture
  of experts without balancing losses and shows the concentration arising by
  the stated route, experts that are selected more being trained more and so
  selected still more, for example by showing that it depends on early
  selection and not on differences in initial competence, or that it
  disappears when experts are trained equally while allocation is left free.
  It is refuted if the concentration proves to track a real difference in
  what the experts can do, or does not recur across seeds. Whether the
  balancing losses produce competent specialists, rather than equally used
  ones, is a separate question.
summary: >-
  The authors' explanation in Shazeer et al. (2017), [LIT-1507](../literature.d/LIT-1507.md), p. 5, stated
  and not tested. Kept here when the twenty-second status review promoted
  [THEORY-927](THEORY-927.md) as the report ([ADR-065](../decisions.d/ADR-065.md); [ADR-047](../decisions.d/ADR-047.md), kind 1).
---

# THEORY-1218: In a sparsely-gated mixture-of-experts layer trained without balancing losses, the gate's concentration on a few experts arises by self-reinforcement: favoured experts are trained more rapidly and so are selected still more

## Source

Shazeer et al. (2017), [LIT-1507](../literature.d/LIT-1507.md), section 4 (p. 5); read in full in [NOTE-1145](../notes.d/NOTE-1145.md)
from arXiv v1. What the paper observed and measured is [THEORY-927](THEORY-927.md), which
this entry extends.

## Why it is Proposed

"the favored experts are trained more rapidly and thus are selected even
more by the gating network" (p. 5) is the authors' explanation. No
trajectories, seeds or initializations are compared, so early selection is
not separated from differences in initial competence.
