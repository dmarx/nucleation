---
status: Open
title: 'Under what funding and incentive rules does allocating resources according to observed activity cause an organization to lose capabilities whose value is concentrated in rarely encountered circumstances?'
version: 1
tags:
- society-and-governance
- operations-research
- complex-systems
date: '2026-11-04'
line:
- distributed-agency
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 11 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)". If budgets
  follow observed activity and competence decays without funded
  maintenance, a capability used only in rare circumstances may be
  defunded into incapacity. A: "Its existence and harmfulness should not be
  assumed." Distinct from [QUESTION-134](QUESTION-134.md). The wording is A's; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpvhj8j TERM-tmpuc919 ARG-tmp5fhgc — Proposed, Rejected or new; A's proposals of 2026-11-04 and the readings they cite, as open -->
<!-- inactive-ok-file: CASE-tmp0g3pa — Proposed or new; entries of 2026-11-05 filed from the pasted synthesis on constraint architectures, cited as open -->

# QUESTION-tmpmtvei: Under what funding and incentive rules does allocating resources according to observed activity cause an organization to lose capabilities whose value is concentrated in rarely encountered circumstances?

## Why it is a question

Three processes could interact:

- **funding feedback**: low observed activity lowers the budget;
- **competence decay**: proficiency falls without maintained training;
- **coverage feedback**: a weaker or smaller capability is committed less
  and observed doing less.

A's model:

  k_{t+1} = (1 − δ)k_t + βm_t,    B_{t+1} = B̄ + ηM_t,

with k the competence, δ its decay rate, m_t the maintenance training
funded from the current budget, B the budget, B̄ its base, and M_t the
observed activity. If m_t is drawn from B_t and M_t is low because the
capability's circumstances are rare, the loop can drive k down. Whether
it does, for which rules, is open. A: "Its existence and harmfulness
should not be assumed."

It differs from [QUESTION-134](QUESTION-134.md), where influence decides a specialist's
access to learning. Here the allocation is institutional, the signal is
observable utilization, and the capability at stake is deadline-
conditioned readiness ([TERM-tmpuc919](../terms.d/TERM-tmpuc919.md)) for rare contingencies. The loop
would act on one factor of [CLAIM-tmpvhj8j](../claims.d/CLAIM-tmpvhj8j.md)'s joint readiness, proficiency,
and so its effect depends on the others. It would be the institutional
form of [ARG-tmp5fhgc](../arguments.d/ARG-tmp5fhgc.md)'s rejected inference, acted on.

## What would answer it

Conditions on the funding and incentive rule (η, B̄, how m is set from B)
and on decay (δ, β) under which k stays above what a rare contingency
requires, and conditions under which it does not; better, a model run or
an organizational history showing the loop at work, against a control in
which maintenance funding is decoupled from observed activity.

## What would not answer it

A capability that loses funding and keeps its competence; or one that
loses competence for a reason other than activity-based allocation.

## Note of 2026-11-05: a ratchet that forecloses a transition

The constructed [CASE-tmp0g3pa](../cases.d/CASE-tmp0g3pa.md) gives one mechanism the question asks about: a budget rule that cuts or expires unspent funds can leave an organization able to hold either of two regimes and unable to pay for moving between them. No status changes.
