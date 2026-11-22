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
<!-- inactive-ok-file: ARG-053 — Proposed, Rejected or new; A's proposals of 2026-11-04 and the readings they cite, as open -->
<!-- inactive-ok-file: CASE-200 — Proposed or new; entries of 2026-11-05 filed from the pasted synthesis on constraint architectures, cited as open -->

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

- **Funding by what is observed selects for form.** Andrews, Pritchett and Woolcock ([NOTE-1664](../notes.d/NOTE-1664.md)) find aid and legitimacy granted for adopting prescribed forms, scored by indicators, and capability stagnating under it. Ostrom et al. ([NOTE-1647](../notes.d/NOTE-1647.md)) find donor staff rewarded for disbursing, not for results that last. Moss et al. ([NOTE-1661](../notes.d/NOTE-1661.md)) note that, until recently, a government's performance did not affect whether it received aid. In India ([NOTE-1655](../notes.d/NOTE-1655.md)) pay for performance kept the indicators it paid for.
- **A model of the cost.** In [CLAIM-602](../claims.d/CLAIM-602.md), funding that pays for the work rather than for the organization doing it selects substitution, which lowers the capacity kept.

No status changes.

## Note of 2026-11-22: practice as utilization

<!-- inactive-ok-block: CASE-315 CLAIM-878 — new; LEAD-080's study and its corollary -->
In [LEAD-080](../leads.d/LEAD-080.md)'s run of A's readiness simulator ([CASE-315](../cases.d/CASE-315.md)), a budget set to the last month's peak defunded a rarely needed heavy rescue squad within months unless something mobilized it every month; a monthly drill did, and kept it funded in every run ([CLAIM-878](../claims.d/CLAIM-878.md)). In that model, whether the loop this question describes runs turns on whether practice and cancelled dispatches count as the observed activity. Full carry-over kept the squad funded but not qualified: without drills, at two reports a month, its skill fell and needs met fell from 0.92 to 0.59, so funding and maintenance are separate conditions. No status changes.

## Note of 2026-11-22: the loop run against a decoupled control

<!-- inactive-ok-block: CASE-343 CLAIM-921 — new; LEAD-036's study and the claim drawn from it -->
[LEAD-036](../leads.d/LEAD-036.md) ran A's model above with the three processes this question names, coverage feedback taken as a capability committed only once its competence reaches a threshold, and against the control asked for under "What would answer it", maintenance funded apart from observed activity ([CASE-343](../cases.d/CASE-343.md)). The loop exists in the model and is harmful there under one condition on the rule: where the base budget alone sustains competence below the commitment threshold, (β/δ)(B̄ − h) < k_lo, the coupled rule has a state in which the capability is never committed or funded again, and any stretch without occasions long enough for competence to decay there reaches it, whatever η pays per use ([CLAIM-921](../claims.d/CLAIM-921.md)). At the same expected funding, it was lost within thirty years in every run at one occasion in two and a half years, in 39 % at four a year, and never under decoupling. Where the base sustains competence above the threshold nothing was lost for good, but at the rarest occasions coupling met a quarter of them against nearly all under decoupling. The rates are invented. No status changes.
