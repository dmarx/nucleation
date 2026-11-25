---
number: 889
status: Proposed
formerly:
- CLAIM-tmp92xul
title: 'In a model of Northstar in which authority composes by relations of precedence, jurisdiction, suspension and override, a will-organization over the regimes beats control models that see the arrangement of authority only as an input by more than its Occam cost, and its gain is prediction of combined changes of authority from changes made one at a time, which no log-additive control gate reaches with any amount of such data; priced on the training arrangements alone, the same test also passes a will-organization whose relations compose otherwise than it says'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A control-only model of the construction, one with no variable for a
  relation of precedence, jurisdiction, suspension or override, that
  predicts the combinations never seen in training as well as the
  will-organization model does, at no greater complexity, when trained
  only on the baseline and single changes. Or an error in the computation
  that reverses the governed world's results. A model given the relations
  as features or as a prior does not count: it is the will-organization
  model under another name. Nor does a loss of the will-organization model
  in a world the case does not stipulate, which the study reports.
tags:
- agency
- model-comparison
- compositionality
date: '2026-11-22'
line:
- will-organization
- distributed-agency
grounds:
- CASE-325
bears_on:
- QUESTION-056
uses:
- TERM-046
summary: >-
  What [CASE-325](../cases.d/CASE-325.md) shows, run for [LEAD-089](../leads.d/LEAD-089.md) as [QUESTION-056](../questions.d/QUESTION-056.md) asks. In the
  world Northstar's variants stipulate, the will-organization model wins
  the training evidence on every seed by 10 to 71 nats. On the combinations
  of changes never seen it is within 0.015 nats per episode of the truth,
  and the best control gate is 0.03 to 0.2 away, a gap that stays at about
  0.01 with unlimited data. It loses wherever authority is idle or
  idiosyncratic. Where one relation composes otherwise than it says, it
  still wins the training evidence and then mispredicts, so [CLAIM-174](CLAIM-174.md)'s
  test 4 must be priced on held-out interventions. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-174 CLAIM-487 — Proposed; the test this prices and the gain it bears on, open -->
<!-- inactive-ok-file: CLAIM-089 — Rejected; its surviving case is one of the worlds -->
<!-- inactive-ok-file: ARG-025 — Proposed; its third grade is the standard cited -->
<!-- inactive-ok-file: CLAIM-890 — new; the study and the reading filed with this claim -->

# CLAIM-889: In a model of Northstar in which authority composes by relations of precedence, jurisdiction, suspension and override, a will-organization over the regimes beats control models that see the arrangement of authority only as an input by more than its Occam cost, and its gain is prediction of combined changes of authority from changes made one at a time, which no log-additive control gate reaches with any amount of such data; priced on the training arrangements alone, the same test also passes a will-organization whose relations compose otherwise than it says

## The claim

[CASE-325](../cases.d/CASE-325.md) models Northstar's episodes, in which one of three regimes
becomes effective, under arrangements of authority taken from [CASE-003](../cases.d/CASE-003.md)
and [CASE-002](../cases.d/CASE-002.md). It sets a will-organization model with four parameters
against five control-only models. These are a controller blind to
authority, a saturated lookup, and three softmax gates over the regimes
that take the arrangement as input. Training is the baseline and each
single change of authority. The test is the four combinations never seen.

1. **The will-organization earns its Occam cost where the case is as
   stipulated.** Its log evidence beats the best control-only model on 80
   of 80 seeds, by a median of 17 nats at 30 episodes per arrangement and
   61 at 1000. That is [CLAIM-174](CLAIM-174.md)'s test 4, priced as [CLAIM-154](CLAIM-154.md) prices
   a candidate.
2. **The gain is transfer to combined interventions.** On the unseen
   combinations its regret is 0.001 to 0.015 nats per episode. The gates'
   is 0.03 to 0.26. With unlimited data from the training arrangements,
   the best gate's stays at 0.009 to 0.018. A gate additive in the log
   odds cannot represent how the relations compose. The products of two
   authority bits that would let it are never observed when the changes
   are tried one at a time.
3. **The test can fail.** Where authority is idle ([CLAIM-089](CLAIM-089.md)'s surviving
   case) or matters idiosyncratically, the will-organization loses on
   every seed, by 0.9 to 2,551 nats.
4. **Training evidence alone is not enough.** In a world where one
   relation composes otherwise than the model says, the will-organization
   still wins the training evidence on every seed, by 10 to 82 nats,
   because the difference shows only in combinations. It then predicts
   them worse than the additive gate. So test 4 needs the held-out
   interventions that [ARG-025](../arguments.d/ARG-025.md)'s third grade asks for. A Bayes factor on
   observations under the arrangements already seen does not do it.

## What it does not say

- **That Northstar, or any organization, is like this.** The governed world
  is the case's stipulation. The claim is about what a model of it can and
  cannot do, as [CASE-325](../cases.d/CASE-325.md)'s "What it cannot show" states.
- **That control theory cannot model it.** A control model whose variables
  are the relations predicts as well. Whether that implements the
  will-organization or replaces it is [QUESTION-056](../questions.d/QUESTION-056.md)'s question, read in
  [CLAIM-890](CLAIM-890.md).
- **That this is [CLAIM-487](CLAIM-487.md)'s gain.** That gain is across realizers, and this is
  one realizer.
- **That the five gates exhaust control-only models.** They are the
  simplest standard ones, and the defeater names what would beat the
  claim.
