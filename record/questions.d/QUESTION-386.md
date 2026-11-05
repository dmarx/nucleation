---
number: 386
status: Open
formerly:
- QUESTION-tmpmtvei
title: 'Under what funding and incentive rules does allocating resources according to observed activity cause an organization to lose capabilities whose value is concentrated in rarely encountered circumstances?'
version: 1
tags:
- society-and-governance
- operations-research
- complex-systems
date: '2026-11-04'
line:
- readiness
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
<!-- inactive-ok-file: CLAIM-tmpoh07b NOTE-tmp22pjn — new; readings and claims of the aid-dependency filing, cited as open -->
<!-- inactive-ok-file: CLAIM-587 TERM-115 ARG-053 — Proposed, Rejected or new; A's proposals of 2026-11-04 and the readings they cite, as open -->
<!-- inactive-ok-file: CASE-200 — Proposed or new; entries of 2026-11-05 filed from the pasted synthesis on constraint architectures, cited as open -->
<!-- inactive-ok-file: CLAIM-577 — Proposed; the assistant's claim of 2026-11-05, cited as open -->

# QUESTION-386: Under what funding and incentive rules does allocating resources according to observed activity cause an organization to lose capabilities whose value is concentrated in rarely encountered circumstances?

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
conditioned readiness ([TERM-115](../terms.d/TERM-115.md)) for rare contingencies. The loop
would act on one factor of [CLAIM-587](../claims.d/CLAIM-587.md)'s joint readiness, proficiency,
and so its effect depends on the others. It would be the institutional
form of [ARG-053](../arguments.d/ARG-053.md)'s rejected inference, acted on.

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

The constructed [CASE-200](../cases.d/CASE-200.md) gives one mechanism the question asks about: a budget rule that cuts or expires unspent funds can leave an organization able to hold either of two regimes and unable to pay for moving between them. No status changes.

## Note of 2026-11-05: a test for the pinning claim

[CLAIM-577](../claims.d/CLAIM-577.md) shows one mechanism the question asks about, in the pure case: under spend-matching, ordinary efficient operation alone pins the organization to the transitions it can make at holding cost. No status changes.

## Note of 2026-11-05: the readings on aid dependency and self-sufficiency

Read at the owner's request to look to aid and development for theory on how aid-dependent organizations become self-sufficient; the works were chosen by the assistant.

- **Funding by what is observed selects for form.** Andrews, Pritchett and Woolcock (NOTE-tmpfpey1) find aid and legitimacy granted for adopting prescribed forms, scored by indicators, and capability stagnating under it. Ostrom et al. (NOTE-tmp22pjn) find donor staff rewarded for disbursing, not for results that last. Moss et al. (NOTE-tmpd45i4) note that, until recently, a government's performance did not affect whether it received aid. In India (NOTE-tmp9wlcj) pay for performance kept the indicators it paid for.
- **A model of the cost.** In CLAIM-tmpoh07b, funding that pays for the work rather than for the organization doing it selects substitution, which lowers the capacity kept.

No status changes.
