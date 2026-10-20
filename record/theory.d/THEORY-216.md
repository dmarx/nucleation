---
number: 216
status: Active
formerly:
- THEORY-tmp7w5tq
title: 'On the 2017 r/place log, with coalitions recovered from co-placement, which coalitions survive is barely predictable early from their size, area, start time and colour entropy, the size distribution of recovered coalitions shifts toward large ones as the event proceeds, and some lasting artworks were held by coalitions that kept working under sustained overwriting'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-216 (batch 031, ADR-047 v3). The one study was read in full,
    and the title now claims no more than it measured. Its scope is the
    2017 log and the recovered coalitions. "Barely predictable" stays
    relative to the four features tried. "Lasting artworks are those whose
    coalitions keep working under continual overwriting" becomes an
    existence clause, since it rests on ten illustrated lifecycles. The
    promote_when, a population measure of repair and a test with
    interaction features, moves unchanged to QUESTION-169.
- version: 3
  date: '2026-10-20'
  note: >-
    Dated note added under ADR-047 v4 (the narrowing-loss sweep, batch
    067). The wider claim this entry's narrowing dropped, the thesis that
    lasting artworks, as a population, are those whose coalitions keep
    repairing them under overwriting (the source's claim C6, shown in ten
    lifecycles), is now carried by THEORY-tmp3ucjb, which extends this
    entry. Status and title are unchanged.
tags:
- social-science
- complex-systems
date: '2026-10-13'
source:
- LIT-1032
summary: >-
  Wu & Silva (2024; v3 2026), [LIT-1032](../literature.d/LIT-1032.md), read in [NOTE-724](../notes.d/NOTE-724.md). On the
  2017 r/place log, coalitions are recovered, failed ones included, from
  co-placement and image segmentation. Under 7% of updates survive to the
  end. Recovered coalition sizes shift toward large over the event. A decision tree on
  four state features predicts survival at F1 0.09 in the first 48 hours and
  0.67 later. Illustrated successful coalitions keep working under
  overwriting throughout, and some failures look like successes until a late
  collapse. The recovery is validated only against final artworks, the
  lifecycles are ten examples, and nothing here observes plans.
supports:
- CLAIM-280
- CLAIM-273
- CLAIM-274
extended_by:
- THEORY-tmp3ucjb
---
<!-- inactive-ok-file: CLAIM-280 CLAIM-272 THEORY-214 — Proposed; open claims and a reading of a sister study, cited as what this bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-tmp3ucjb — Proposed; the population thesis this entry's narrowing dropped, filed apart under ADR-047 v4 and extending this one -->

# THEORY-216: On the 2017 r/place log, with coalitions recovered from co-placement, which coalitions survive is barely predictable early from their size, area, start time and colour entropy, the size distribution of recovered coalitions shifts toward large ones as the event proceeds, and some lasting artworks were held by coalitions that kept working under sustained overwriting

## Source

Wu & Silva (2024; v3 2026), [LIT-1032](../literature.d/LIT-1032.md), read in [NOTE-724](../notes.d/NOTE-724.md): §6
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
  [CLAIM-280](../claims.d/CLAIM-280.md)'s existence claim and leaves its `defeated_if`, mostly
  unattacked survivors, open. Falmagne et al. ([THEORY-214](THEORY-214.md)) find that
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
  uniform cooldown (§4) bears on [CLAIM-272](../claims.d/CLAIM-272.md). It is recorded in
  [NOTE-724](../notes.d/NOTE-724.md) as a qualification: unequal influence arises even before
  coordination, from unequal use of a cap and from automation. It is not
  part of this account.
- 2017 only, the least automated edition (0.3% of actions from likely
  bots, against 17.1% in 2023).

## Connections

- **[CLAIM-280](../claims.d/CLAIM-280.md).** Supported weakly, as above. The abandoned and rebuilt
  Mona Lisa is a product recurring with a different effort behind it,
  which is the product/producer split. Recovered coalitions could measure
  that split, but the paper does not.
- **[THEORY-214](THEORY-214.md).** A complementary result on the 2022 data. There, the
  abrupt overthrow of a defended image is predictable hours ahead from the
  image's own dynamics. Here, eventual survival is not predictable early
  from coarse coalition features. The two do not conflict. One predicts an
  imminent event from fine dynamics, the other a final outcome from four
  static features.
- **[QUESTION-169](../questions.d/QUESTION-169.md).** What this account leaves open: whether lasting
  artworks as a population were sustained by repair, and whether
  interaction features restore early predictability. It was this
  account's promotion condition until 2026-10-19.

## Note of 2026-10-20: the wider claim, filed apart

Under [ADR-047](../decisions.d/ADR-047.md) v4, what this entry's narrowing dropped is filed as its own
Proposed entry, so that evidence can later confirm or reject it as a
thesis. [THEORY-tmp3ucjb](THEORY-tmp3ucjb.md) carries the thesis that lasting artworks, as a population, are those whose coalitions keep repairing them under overwriting (the source's claim C6, shown in ten lifecycles). It extends this entry, whose
measured or derived content is its evidence. Nothing here changes.
