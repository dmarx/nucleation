---
number: 325
status: Active
formerly:
- CASE-tmpokq28
title: 'Northstar modelled twice in a simulation over twenty seeds, once by control models that see the arrangement of authority only as an input and once by a will-organization whose relations of precedence, jurisdiction, suspension and override decide which regime becomes effective: where the case is as stipulated the will-organization wins by 10 to 71 nats beyond its Occam cost and alone predicts combined changes of authority never seen together, a gap more data does not close; it loses heavily where authority is idle or idiosyncratic, and it wins the training evidence even where a relation composes otherwise than it says, which only the unseen combinations expose'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-089. The model,
    tests, results and a README are under scratch/studies/lead-089/.
standing: documented
kind: executed-study
tags:
- agency
- model-comparison
- society-and-governance
- compositionality
date: '2026-11-22'
line:
- will-organization
- distributed-agency
variant_of:
- CASE-023
- CASE-003
- CASE-002
bears_on:
- QUESTION-056
summary: >-
  [QUESTION-056](../questions.d/QUESTION-056.md)'s test, run by [LEAD-089](../leads.d/LEAD-089.md): Northstar ([CASE-023](CASE-023.md)) modelled with
  control and metacontrol mechanisms alone, then with a will-organization
  over them, and the difference priced as [CLAIM-174](../claims.d/CLAIM-174.md)'s test 4 prices it, by
  log evidence ([CLAIM-154](../claims.d/CLAIM-154.md)). Episodes decide which of three regimes becomes
  effective. Authority varies in three respects taken from the case's
  variants ([CASE-003](CASE-003.md), [CASE-002](CASE-002.md)); attitudes and proposals do not. Training
  sees the baseline and each single change; the test is the four
  combinations never seen. Four worlds, four sizes, twenty seeds. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-174 CLAIM-487 — Proposed; the test this prices and the gain it bears on, open -->
<!-- inactive-ok-file: CLAIM-089 — Rejected; its surviving case is one of the worlds -->
<!-- inactive-ok-file: ARG-025 — Proposed; its intervention grade is what the test is scored against -->
<!-- inactive-ok-file: CASE-166 — Proposed; the earlier Northstar simulation, reported and not reproduced, set beside this one -->
<!-- inactive-ok-file: CLAIM-889 CLAIM-890 — new; the finding and the reading filed from this study -->

# CASE-325: Northstar modelled twice in a simulation over twenty seeds, once by control models that see the arrangement of authority only as an input and once by a will-organization whose relations of precedence, jurisdiction, suspension and override decide which regime becomes effective: where the case is as stipulated the will-organization wins by 10 to 71 nats beyond its Occam cost and alone predicts combined changes of authority never seen together, a gap more data does not close; it loses heavily where authority is idle or idiosyncratic, and it wins the training evidence even where a relation composes otherwise than it says, which only the unseen combinations expose

## The study

**Episodes.** Each decides which of Northstar's regimes becomes effective:
routine deployment, cautious verification or emergency suspension. The
context is three bits: a reliability specialist objects, an incident
signal is present, the release is flagged business-critical (each with
probability 0.3).

**Authority.** Three bits, each one of the case's own variants:

- an objection suspends deployment pending review (Northstar-A) or does
  not, unless senior management orders it (Northstar-B; [CASE-003](CASE-003.md));
- severity is classified by the product team or by an independent
  reliability group ([CASE-002](CASE-002.md));
- senior management may authorize a business-critical release despite a
  freeze ([CASE-002](CASE-002.md)).

The proposals are the same under every arrangement: the product team
proposes deployment, the specialist verification. So are the propensities
of each party.

**The will-organization model (WO).** Maintained relations decide which
proposal becomes effective. A severe classification takes precedence and
freezes deployment unless the override is held and the release is
business-critical. Jurisdiction over classification sets how readily a
signal is classified severe. An objection suspends under A; under B it
does so only if senior management orders it. Four parameters: how readily
each of the two classifiers calls a signal severe, how often senior
management orders verification under B, and execution noise. Uniform
priors; the evidence is by quadrature.

**The control-only models.** Each sees the arrangement of authority as an
input. None has a variable for a relation.

- C0 is a controller blind to authority (a policy over contexts). It is
  also what a plan-only model gives, since the plan is the same in every
  arrangement.
- C1 is a saturated lookup over context and arrangement.
- C2 is a metacontrol gate: a softmax over regimes whose values are linear
  in context and arrangement, which is the form of an expected-value-of-
  control choice among regimes.
- C3 is C2 with every pairwise product within the context and between
  context and authority.
- C4 is a gate saturated in the context, each authority bit modulating
  each context separately.

They have 16, 128, 14, 38 and 64 parameters, against WO's 4. C0 and C1 have
exact Dirichlet evidence; C2 to C4 have Laplace evidence under a Gaussian
prior, which is regular, so [CLAIM-154](../claims.d/CLAIM-154.md)'s condition holds.

**Worlds.**

- *Governed*: the case as the paper stipulates it, with the true
  parameters drawn for each seed.
- *Idle*: authority does nothing, which is [CLAIM-089](../claims.d/CLAIM-089.md)'s surviving case.
- *Idiosyncratic*: authority matters, but not by these relations.
- *Interacting*: the same relations, except that where the reliability
  group classifies it also takes objections over, so an objection no
  longer suspends by itself. This shows only in combined arrangements.

**Training and test.** Training is the baseline and each single change of
authority, with n episodes each, for n = 30, 100, 300 and 1000. The test
is 2,000 fresh episodes under each of the four combinations never seen in
training. There are 20 seeds per cell, and a further run fits the exact
expected counts of 10⁶ episodes per arrangement.

## Results

The log Bayes factor is WO's log evidence less that of the best
control-only model, per seed. Regret is the truth's log predictive less
the model's, in nats per episode, on the unseen combinations. The Bayes
factor is the median over seeds, with min and max; regrets are means over
seeds.

| World | n | ln BF, WO vs best control | Regret: WO | C2 | C3 | C4 |
|---|---|---|---|---|---|---|
| governed | 30 | 17.1 [10.0, 22.2] | 0.015 | 0.264 | 0.197 | 0.214 |
| governed | 100 | 26.5 [16.7, 33.6] | 0.004 | 0.166 | 0.121 | 0.124 |
| governed | 300 | 41.6 [30.4, 51.3] | 0.001 | 0.119 | 0.076 | 0.069 |
| governed | 1000 | 61.3 [49.1, 70.7] | 0.001 | 0.102 | 0.046 | 0.032 |
| idle | 30 | −32.2 [−76.9, −0.9] | 0.422 | 0.212 | 0.177 | 0.122 |
| idle | 1000 | −1513.9 [−2550.8, −734.5] | 0.443 | 0.103 | 0.028 | 0.025 |
| idiosyncratic | 30 | −32.7 [−60.5, −12.4] | 0.451 | 0.525 | 0.644 | 0.551 |
| idiosyncratic | 1000 | −1539.4 [−2105.5, −876.8] | 0.473 | 0.451 | 0.910 | 1.162 |
| interacting | 30 | 16.8 [10.3, 21.6] | 0.317 | 0.193 | 0.208 | 0.214 |
| interacting | 1000 | 66.4 [54.3, 81.6] | 0.294 | 0.197 | 0.292 | 0.236 |

- **Governed.** WO beats every control-only model by more than its Occam
  cost on 80 of 80 seeds. The runner-up by evidence is C3 on 72 of them.
  On the combinations never seen, WO is within 0.015 nats per episode of
  the truth, and every gate is 0.03 to 0.26 nats per episode away.
- **The gap does not close with data.** At 10⁶ episodes per training
  arrangement, the gates' regret on the unseen combinations stays at
  0.08–0.11 (C2), 0.022–0.034 (C3) and 0.009–0.018 (C4) over five seeds.
  WO's stays at 0.0003–0.0009, which is its quadrature grid's resolution.
  A log-additive gate cannot represent how the relations compose. The
  products of two authority bits that would let it are never observed when
  each change is tried alone.
- **Idle and idiosyncratic.** WO loses on every seed, by 0.9 to 2,551 nats.
  The blind controller C0 wins where authority is idle, and the saturated
  lookup C1 wins where it is idiosyncratic. So the test can come out
  against the will-organization.
- **Interacting.** WO wins the training evidence by 10 to 82 nats on every
  seed, because the misplaced relation never shows in training. It then
  predicts the unseen combinations worse than the additive gate C2: 0.26
  to 0.32 nats per episode against 0.16 to 0.20 (means over seeds, by n).

## What it can show

- **Within this construction, the difference exists, is priced, and is
  transfer.** [QUESTION-056](../questions.d/QUESTION-056.md) says replacement is shown "if the mechanism
  model predicts as well with no will-organization variables". None of
  five control-only models does, at matched or greater complexity. The
  advantage is not a better fit to what was seen, which C3 and C4 approach
  as n grows. It is prediction of a combination of changes in authority
  from the changes taken one at a time. That is the
  intervention grade [ARG-025](../arguments.d/ARG-025.md) asks for, met against the strongest simple
  control alternatives rather than a deliberately weak one.
- **[CLAIM-174](../claims.d/CLAIM-174.md)'s test 4, priced on training data alone, can pass a
  will-organization whose relations compose wrongly.** The interacting
  world passes it by 66 nats at n = 1000 and fails on the unseen
  combinations. The pricing has to be done on held-out interventions.
- **Unlike [CASE-166](CASE-166.md)'s router tie,** the control comparator here is not
  given the relations, only the arrangement. Given the relations as
  features, a gate would be WO under another name. That is the
  implementation reading the claim filed from this study takes up
  ([CLAIM-890](../claims.d/CLAIM-890.md)); the finding is [CLAIM-889](../claims.d/CLAIM-889.md).

## What it cannot show

- **That any real company is like this.** The governed world is the
  case's stipulation, and WO is its structure written as a model. The
  study shows what the structure buys if Northstar is as the paper says.
  It does not show that Northstar or any firm is. The idle and
  idiosyncratic worlds show that the data can refuse it.
- **That the gain is the will-organization's rather than the rules'.** The
  relations WO encodes are rules of the kind institutional theory already
  writes, which is the reading's subject.
- **Anything about a person or across realizers.** It is one realizer, an
  organization. [CLAIM-487](../claims.d/CLAIM-487.md)'s gain is that one description serves several,
  and a model of one cannot test that.
- **That the gates are the best control models.** They are the simplest
  standard ones. A gate with products of authority bits can represent the
  composition. It cannot learn those products from single changes without
  a prior that is the relations again.
