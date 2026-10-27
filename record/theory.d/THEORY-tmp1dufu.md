---
status: Proposed
promote_when: >-
  A measurement of each head's role at many checkpoints, not two, in
  several training runs, showing the same heads moving from n-gram roles to
  previous-token, bracket-matching-support or circuit-support roles, and
  an intervention showing that the later role is built from the earlier
  weights: for example, re-initializing or freezing a head shortly before
  its change and finding that the later circuit forms late or not at all,
  where re-initializing a head without an earlier role makes no such
  difference. It is refuted if the heads that become previous-token heads
  had no earlier n-gram role once roles are measured densely, or if
  re-initialized heads take the late roles on the same schedule, so that
  the earlier role was incidental. Further two-checkpoint token-in-context
  comparisons cannot settle it.
title: 'In a two-layer attention-only transformer, attention heads change function during training: heads in the first layer that predict simple n-grams early later become the previous-token heads of the induction circuit, a bracket-matching support head, or supporting members of a circuit with second-layer n-gram heads, giving up simple n-grams as they do, and particular n-grams pass from one head to another; so later circuits form partly by repurposing components that already had a role'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpueby3. The observations are the paper's
    (§4.3, appendix B.6); the reading of them as reorganization rather than
    new acquisition is the paper's in part and the record's in part, and
    rests on token-in-context comparisons at two checkpoints in one run.
tags:
- learning-theory
- representation-learning
date: '2026-10-26'
source:
- LIT-tmpa32mr
summary: >-
  Wang, Hoogland, van Wingerden, Furman and Murfet (2024), [LIT-tmpa32mr](../literature.d/LIT-tmpa32mr.md),
  read in [NOTE-tmpueby3](../notes.d/NOTE-tmpueby3.md). "Heads 0:1, 0:4, 0:7 ultimately become the two
  previous-token heads and (layer 0) Dyck head respectively. However,
  these heads appear to start out as simple n-gram heads." Layer-0
  multigram heads lose information about simple n-grams from stage LM3,
  as path patching and composition scores show them coming to feed
  layer-1 bracket-matching heads. The "ago" n-gram moves from head 0:0 to
  head 1:0. Whether the late roles are built from the early ones, or merely
  follow them in time, is not tested.
---
<!-- inactive-ok-file: CLAIM-329 THEORY-279 — Proposed; the thesis on continuity by transmission and a neighbouring account, cited as open -->
# THEORY-tmp1dufu: In a two-layer attention-only transformer, attention heads change function during training: heads in the first layer that predict simple n-grams early later become the previous-token heads of the induction circuit, a bracket-matching support head, or supporting members of a circuit with second-layer n-gram heads, giving up simple n-grams as they do, and particular n-grams pass from one head to another; so later circuits form partly by repurposing components that already had a role

## Source

Wang et al. (2024), [LIT-tmpa32mr](../literature.d/LIT-tmpa32mr.md), read in full in [NOTE-tmpueby3](../notes.d/NOTE-tmpueby3.md): §4.3,
Figs. 5–7, and appendix B.6.

## What is asserted

That in this model a circuit's components are not new structure grown into
idle heads. Heads that already did something, predicting simple n-grams,
change to new roles as later circuits form, and the old roles either
lapse or move to other heads.

## What the paper shows toward it

- **Roles at two checkpoints.** Token-in-context classification at 8.5k
  and 50k steps (Fig. 9) puts heads 0:1, 0:4 and 0:7 among n-gram heads
  early and among previous-token and bracket-matching heads late. Head
  0:0 goes from attending to whitespace to a standard multigram head.
- **Information given up.** With a trained one-layer model's outputs as
  the data, the layer-0 multigram heads' data-refined LLC falls from LM3
  onward, which the authors read as their losing simple n-grams that a
  one-layer model can predict.
- **A new dependency.** Path patching shows head 1:5's loss on nested
  brackets coming to depend on the layer-0 multigram heads at that time,
  and K-composition scores between the two layers turn around together.
- **Roles moving.** The "ago" n-gram is head 0:0's at 8.5k steps and head
  1:0's at the end; the "more…th → an" comparative goes from 0:7 to 1:1.

## Why it stays Proposed

The role changes rest on two snapshots in one run, classified by
mean-ablation effects with manual inspection. "Repurposing" says more
than "a head had one role and later another": it says the later role was
made from the earlier one. Nothing in the paper tests that, and judging
that the "ago" n-gram "migrated" from one head to another is continuity by
resemblance of the affected tokens, which [CLAIM-329](../claims.d/CLAIM-329.md) says is not enough for
continuity of the thing.

## What would confirm or reject it

The promote_when above.

## Connections

- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md)** asks whether a circuit "emerge[s] by acquiring new
  features, reorganizing existing features, or both". This is the record's
  best evidence for "reorganizing", at the level of components.
- **[QUESTION-039](../questions.d/QUESTION-039.md)**, on whether acquisition is one kind of event: this would
  make repurposing one kind, beside growth.
- **[THEORY-279](THEORY-279.md).** Low-order structure first, then lost, is the same shape
  within a single transformer.
- **LIT-tmp9dono.** Elhage et al.'s mathematical framework is where the
  two-layer attention-only setting and the QK/OV reading of heads used
  here come from; its path expansion is THEORY-tmphm85g.
