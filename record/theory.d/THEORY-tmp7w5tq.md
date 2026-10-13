---
status: Proposed
promote_when: >-
  Promoted by a measurement on full placement logs, in r/place or a
  comparable contested canvas, that tracks recovered or recorded coalitions
  through time and shows (a) that artworks lasting to the end received
  sustained overwrites and repairs throughout, as a population and not in
  hand-picked lifecycles, and (b) that coalition survival stays
  near-unpredictable early even when interaction features (who attacks
  whom, shared members, alliance ties) are added to state features.
  Weakened if lasting artworks turn out mostly unattacked, or if richer
  features make early outcomes predictable, which would place the
  unpredictability in the feature set and not in the dynamics. What cannot
  settle it: more illustrated lifecycles, or better final-canvas
  segmentation scores, which validate the recovery method and not the
  dynamics.
title: 'On a contested shared canvas, lasting artworks are those whose coalitions keep working under continual overwriting, participants consolidate into large coalitions as the event proceeds, and which coalitions survive is barely predictable from their size, area, start time and colour complexity until late'
version: 1
tags:
- social-science
- complex-systems
date: '2026-10-13'
source:
- LIT-tmplgy5c
summary: >-
  Wu & Silva (2024; v3 2026), [LIT-tmplgy5c](../literature.d/LIT-tmplgy5c.md), read in [NOTE-tmp286fw](../notes.d/NOTE-tmp286fw.md). On the
  2017 r/place log, coalitions are recovered, failed ones included, from
  co-placement and image segmentation. Under 7% of updates survive to the
  end. Coalition sizes shift toward large over the event. A decision tree on
  four state features predicts survival at F1 0.09 in the first 48 hours and
  0.67 later. Illustrated successful coalitions keep working under
  overwriting throughout, and some failures look like successes until a late
  collapse. The recovery is validated only against final artworks, the
  lifecycles are ten examples, and nothing here observes plans.
supports:
- CLAIM-tmpjhd7t
- CLAIM-tmp4zg6p
- CLAIM-tmp6phbn
---
<!-- inactive-ok-file: CLAIM-tmpjhd7t CLAIM-tmp2cza3 THEORY-tmp07t7w — Proposed; open claims and a reading of a sister study, cited as what this bears on, nothing here rests on their being settled -->

# THEORY-tmp7w5tq: On a contested shared canvas, lasting artworks are those whose coalitions keep working under continual overwriting, participants consolidate into large coalitions as the event proceeds, and which coalitions survive is barely predictable from their size, area, start time and colour complexity until late

## Source

Wu & Silva (2024; v3 2026), [LIT-tmplgy5c](../literature.d/LIT-tmplgy5c.md), read in [NOTE-tmp286fw](../notes.d/NOTE-tmp286fw.md): §6
(conflict and predictability), Table 2, Figs. 7–8, Appendices A.3–A.4.

## What was actually shown

The 2017 log, 16.6 million updates, is segmented at each of 259,769
one-second snapshots. Pixels are clustered by colour and by embeddings of
a graph that links participants who placed adjacent same-colour pixels.
The clusters are then chained across time into 39,879 dynamic clusters, the
recovered coalitions.

- **Consolidation.** At 24, 48 and 72 hours, the size distribution of
  recovered coalitions shifts toward large ones (Fig. 7).
- **Unpredictability.** At 100 random snapshots, a balanced decision tree
  on start time, area, coalition size and colour entropy predicts whether
  the coalition's artwork will keep at least 11% of its peak area. Early
  F1 is 0.09 and late F1 is 0.67. Random forests, SVMs and Gaussian
  processes do no better. This could have come out otherwise. Size or an
  early start could have decided outcomes, and they did not.
- **Persistence under attack.** In the illustrated lifecycles (Fig. 8),
  successful coalitions show collaborative and adversarial actions
  together throughout. Some failed coalitions match successful ones for
  long stretches and then collapse. A failed first Mona Lisa was followed
  by a successful second.

## What this does not say

- **It does not show the regime is typical.** Persistence under attack is
  shown in ten chosen lifecycles. A population measure, such as the share
  of lasting artworks with sustained repair, is not given. This supports
  [CLAIM-tmpjhd7t](../claims.d/CLAIM-tmpjhd7t.md)'s existence claim and leaves its `defeated_if`, mostly
  unattacked survivors, open. Falmagne et al. ([THEORY-tmp07t7w](THEORY-tmp07t7w.md)) find that
  some compositions are safe through neglect.
- **Recovered coalitions are not memberships.** They are inferred from
  co-placement and checked only against final artworks (ARS 0.42). Failed
  and transient coalitions, the point of the method, have no ground
  truth.
- **"Unpredictable" is relative to four features.** The authors say
  themselves that alliances, negotiations, coordinated attacks and external
  communication were not observed. The result is that coalition-state
  features do not settle outcomes early. It does not show that nothing
  could.
- **Consolidation is not explained.** That large coalitions have
  advantages under sustained competition is the authors' suggestion. Large
  coalitions also waste more actions and have less active members (§5),
  and no mechanism is tested.
- **It says nothing about equal influence.** The heavy-tailed use of the
  uniform cooldown (§4) bears on [CLAIM-tmp2cza3](../claims.d/CLAIM-tmp2cza3.md). It is recorded in
  [NOTE-tmp286fw](../notes.d/NOTE-tmp286fw.md) as a qualification: unequal influence arises even before
  coordination, from unequal use of a cap and from automation. It is not
  part of this account.
- 2017 only, the least automated edition (0.3% of actions from likely
  bots, against 17.1% in 2023).

## Connections

- **[CLAIM-tmpjhd7t](../claims.d/CLAIM-tmpjhd7t.md).** Supported weakly, as above. The abandoned and rebuilt
  Mona Lisa is a product recurring with a different effort behind it,
  which is the product/producer split. Recovered coalitions could measure
  that split, but the paper does not.
- **[THEORY-tmp07t7w](THEORY-tmp07t7w.md).** A complementary result on the 2022 data. There, the
  abrupt overthrow of a defended image is predictable hours ahead from the
  image's own dynamics. Here, eventual survival is not predictable early
  from coarse coalition features. The two do not conflict. One predicts an
  imminent event from fine dynamics, the other a final outcome from four
  static features.
