---
number: 921
status: Proposed
formerly:
- CLAIM-tmp9mpn0
title: 'Where competence decays without funded maintenance and a capability is committed only when competent enough, a budget that follows observed use has a state in which the capability is never used or funded again whenever the base budget alone sustains competence below that level, any stretch without occasions long enough for competence to decay there reaches it whatever each use was paid, so at the same expected funding a rarer capability is lost sooner, while maintenance funded apart from use, at a level that sustains the threshold, has no such state'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-036, from the
    study of CASE-343.
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §9.10. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the coupled model with k_base below
  k_lo, a history in which competence, once below k_lo with no commitment
  left in the activity window, later reaches k_lo; under a fixed budget
  with (β/δ)(B − h) ≥ k_lo, a history that converges below k_lo; a run of
  n* + W − 1 periods without occasions after which competence is at least
  k_lo; or, in CASE-343's model, loss frequencies below the stated
  bound beyond sampling error. Not defeated by models in which a
  capability is committed with positive chance at every competence, in
  which practice or use outside commitment counts as activity or rebuilds
  competence, or in which competence is unbounded, nor by budgets with a
  floor that funds maintenance to the threshold, none of which the claim
  covers.
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-22'
line:
- readiness
- formal-apparatus
grounds:
- CASE-343
complements:
- CLAIM-577
- CLAIM-878
- CLAIM-602
bears_on:
- QUESTION-386
summary: >-
  Found in running [LEAD-036](../leads.d/LEAD-036.md)'s study ([CASE-343](../cases.d/CASE-343.md)) of A's model from
  [QUESTION-386](../questions.d/QUESTION-386.md). Competence k decays at rate δ and is rebuilt by
  maintenance bought from the budget above a holding cost h; the budget is
  a base B̄ plus η times observed use; and a capability is committed to an
  occasion only if k is at least k_lo. If the base alone sustains
  competence below k_lo, (β/δ)(B̄ − h) < k_lo, a capability that falls
  below k_lo is never committed, so never observed, so funded at the base,
  so never recovers. A stretch without occasions long enough for k to
  decay from its ceiling below k_lo reaches that state whatever earlier uses
  earned, so the chance of loss has a lower bound that rises as occasions
  grow rarer and does not depend on η: paying more per use does not make up
  for rarity. Funding maintenance apart from use at a level that sustains
  k_lo removes the state. In the study, at the same expected funding, the
  coupled rule lost the capability within thirty years in every run at one
  occasion in two and a half years and in 39 % at four a year, and the
  decoupled rule never did. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: CASE-343 CLAIM-878 — new or Proposed; the study this claim is drawn from, filed with it, and LEAD-080's corollary -->

# CLAIM-921: Where competence decays without funded maintenance and a capability is committed only when competent enough, a budget that follows observed use has a state in which the capability is never used or funded again whenever the base budget alone sustains competence below that level, any stretch without occasions long enough for competence to decay there reaches it whatever each use was paid, so at the same expected funding a rarer capability is lost sooner, while maintenance funded apart from use, at a level that sustains the threshold, has no such state

## The claim

Take A's model from [QUESTION-386](../questions.d/QUESTION-386.md), with the question's three processes:

- **competence decay**: k_{t+1} = min(1, (1 − δ)k_t + βm_t), with
  maintenance m_t = max(0, B_t − h) bought from the budget above a holding
  cost h;
- **funding feedback**: B_{t+1} = B̄ + η M̄_t, with M̄_t the mean observed use
  over the last W periods;
- **coverage feedback**: occasions arrive independently, λ a period on
  average, and the capability is committed to one with a chance p(k) that
  is 0 for k < k_lo; M_t counts commitments.

Let k_base = min(1, (β/δ) max(0, B̄ − h)), the competence the base budget
alone sustains.

1. **An absorbing state.** If k_base < k_lo, the set of states with
   k < k_lo and no commitment in the last W periods is closed. In it
   nothing is committed, so M̄ = 0 and B = B̄, and the map
   k ↦ (1 − δ)k + β(B̄ − h)⁺ is increasing with fixed point k_base < k_lo,
   so it keeps k below k_lo.
2. **How it is reached.** Let n* be the number of periods at budget B̄ that
   take competence from 1 below k_lo. Since competence never exceeds 1, a
   run of L = n* + W − 1 periods with no occasions reaches the absorbing
   state from any state: after W − 1 periods the window is empty and the
   budget is B̄. So the chance of loss within T periods is at least
   1 − (1 − e^(−λL))^⌊T/L⌋.
3. **Rarity at fixed money.** The bound depends on λ and not on η. Holding
   ηλ fixed, so that a capability used on every occasion earns the same on
   average, the bound rises toward 1 as λ falls: payment per use cannot
   make up for rarity, because competence is capped and a stretch without
   occasions erodes it however much the last use earned.
4. **Decoupling removes the state.** Under a fixed budget B with
   (β/δ)(B − h) ≥ k_lo, competence converges monotonically to
   min(1, (β/δ)(B − h)) ≥ k_lo from any start, whatever the occasions.
5. **Coverage feedback makes it permanent.** If p(k) > 0 at every k, the
   set in step 1 is not closed: the next occasion is committed with
   positive chance and raises the budget.

Steps 1 to 5 follow from the model. [CASE-343](../cases.d/CASE-343.md) shows their size at
δ = 0.08 a quarter, h = 1, B̄ = 1.2 (k_base = 0.25), k_lo = 0.4 and ηλ =
0.52 (k = 0.9 at full use): n* = 20 quarters; under A's rule the capability
was lost within thirty years in every run at one occasion in five or in two
and a half years (bound 0.94 and 0.58), in 93 % at one a year and 39 % at
four a year (bound near 0, so the loss there runs through partial
commitment), and under decoupling at full-use money in none.

## What it adds

- **Conditions of the kind [QUESTION-386](../questions.d/QUESTION-386.md) asks for.** The question asks
  for conditions on η, B̄, how m is set from B, δ and β. The loop can
  defund a capability for good only where (β/δ)(B̄ − h) < k_lo and use
  falls with competence; η does not enter the condition, and rarity, not
  the price of a use, sets how soon it happens.
- **Beyond [CLAIM-577](CLAIM-577.md)'s pure case.** There one held period forecloses a
  transition; here a rule with a base and a payment per use does the same
  over a stretch set by the decay rate, and the loss passes through
  competence, not through the budget alone. [CLAIM-878](CLAIM-878.md)'s quiet period is
  one period without mobilization; here it is n* periods without use.
- **The protection is a level, not an untying.** Funding maintenance apart
  from use protects the capability only at a level that sustains k_lo. In
  the study, the coupled rule's own average money, spread evenly, did
  worse than coupling where it sustained competence below k_lo.
- **The organizational form of [CLAIM-602](CLAIM-602.md)'s order effect.** There capacity
  learned by doing decays when outside supply does the work first; here a
  capability funded by its observed use decays when its occasions are rare,
  and coverage feedback makes the two compound: a weaker capability is used
  less and so funded less.

## What it does not say

- That real budgets or commitment decisions work this way. The model is
  A's, with a threshold on commitment added; the study's rates are
  invented.
- That decoupling is free. It pays for maintenance in years with no use,
  which is the cost the loop saves; whether that is worth it is the value
  of the rare contingency, which the claim does not weigh.
- Anything where practice counts as use ([CLAIM-878](CLAIM-878.md) found drills
  hold the budget under the peak rule), or where use itself rebuilds
  competence outside maintenance.
- That partial commitment, the main path to loss at moderate rarity in the
  study, follows the bound. Step 2 is a lower bound, loose there.
