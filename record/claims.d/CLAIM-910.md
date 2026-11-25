---
number: 910
status: Proposed
formerly:
- CLAIM-tmpp56wv
title: 'IBP features cannot tell drive from coupling'
statement: >-
  Where a shared external driver and members' coupling produce the same
  within-group correlation, features inferred from members' activity under a
  finite Indian buffet prior do not tell them apart and do not add to the
  communication graph in predicting interventions on the coupling; the graph
  alone invents coupling under the driver, and the features do not remove it
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  In the linear family of CASE-337, or a stated wider one (nonlinear
  dynamics, typed messages, team records), a procedure that uses only the
  members' activity and the communication graph, with features under an
  Indian buffet or beta-process prior, either (a) yields a feature
  statistic that is larger in coupled worlds than in their matched
  shared-driver nulls across organizations, beyond the spread between
  them, or (b) predicts held-out cuts and pulses in the driver world with
  error within twice the error of the same model with the true driver
  observed, while staying no worse than the graph alone in the coupled
  world. A joint state-space fit with the features as persistent latent
  drivers is the obvious candidate for (b).
tags:
- probabilistic-modeling
- social-ontology
- causality
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-337
complements:
- CLAIM-454
summary: >-
  Found by [LEAD-144](../leads.d/LEAD-144.md)'s study ([CASE-337](../cases.d/CASE-337.md)), 2026-11-22. Against a
  null matched on within-group correlation, the feature model of
  [CASE-165](../cases.d/CASE-165.md) found more features and better-aligned ones when members never
  interact; neither of its two intervention readings was right in both
  worlds; the graph-restricted autoregression was right under coupling
  and predicted a cut effect of −0.18 under the driver, where there is
  none; with the features added it was still −0.21, and with the driver
  observed it was 0.00. So in this family the features fail [LEAD-144](../leads.d/LEAD-144.md)'s
  test, and [QUESTION-276](../questions.d/QUESTION-276.md)'s condition (iii) is harder than it states,
  since its relational baseline is itself confounded by the driver. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-337 — new; the study this claim rests on -->
<!-- inactive-ok-file: CLAIM-327 — Proposed; cited as a mechanism the study did not simulate -->

# CLAIM-910: IBP features cannot tell drive from coupling

## The claim

Take members whose activity shows overlapping coactive groups, and two ways
of producing them with the same within-group correlation: the members
influence one another along their communication ties, or each group answers
to an external driver of its own and nobody influences anybody. Then:

1. A feature allocation under a finite Indian buffet prior, fitted to the
   activity, finds the groups under both, and more readily under the
   driver, whose effect enters every member of a group at once in the form
   the prior is built for.
2. The allocation carries no rule for an intervention on the coupling, and
   each rule one could give it (features cause members; features are
   realized by their holders) is right in one world and wrong in the other.
3. A model given the communication graph and no modes, the question's
   baseline, predicts interventions where the coupling is real; but a
   persistent driver makes contacts' past activity predict a member's next,
   and the baseline reads that as influence.
4. Adding the inferred features to the graph does not remove that error,
   because they estimate the drivers too noisily; observing the drivers
   does.

The evidence is [CASE-337](../cases.d/CASE-337.md): seven simulated organizations of 24 members,
three worlds each, interventions held out (cut error under the driver: graph
alone 0.18, graph with features 0.21, graph with the observed driver 0.006).

What follows for [QUESTION-276](../questions.d/QUESTION-276.md): its condition (ii), separating modes from
a common cause's, is not met by the prior; and its condition (iii), beating
the relational baseline on interventions, is not sufficient where a driver
may be present, since the baseline can be wrong in the same way. A
perspective claimed from inferred features needs, in addition, either the
common causes observed or interventions on the members themselves. This
fits [CLAIM-454](../claims.d/CLAIM-454.md): a feature says which members take part together, and
whether that taking part is organization lies in relations the allocation
leaves open; here the relations were given and the allocation still could
not say.

## What it does not say

- That no feature procedure could separate them. The study's combined model
  is a two-stage fit; a joint state-space fit is the open arm, and
  defeat (b) names it.
- Anything outside the linear family run: nonlinear interaction, team
  records that members read and regenerate (the mechanism [CLAIM-327](../claims.d/CLAIM-327.md)
  proposes), typed messages and authorization were not simulated.
- That inferred features are useless. They are exactly right about the
  driver world when read as causes; what they cannot do is say which world
  they are in.
