---
number: 343
status: Proposed
formerly:
- CASE-tmpuqpww
title: 'A''s maintenance-funding loop run with and without decoupling: where the base budget alone keeps competence below the level at which a capability is committed, a budget that follows observed activity loses a capability used once in two and a half years or more rarely in every run or nearly, one used four times a year in three or four runs in ten, and none when maintenance is funded apart from activity'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-036. The code,
    tests and outputs are under scratch/studies/lead-036/.
standing: documented
kind: executed-study
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-22'
illustrates:
- CLAIM-921
bears_on:
- QUESTION-386
line:
- readiness
- formal-apparatus
summary: >-
  [LEAD-036](../leads.d/LEAD-036.md) asked for [QUESTION-386](../questions.d/QUESTION-386.md)'s loop to be simulated with and
  without decoupling. A's model is run as the question records it,
  competence k decaying by δ and rebuilt by maintenance m bought from the
  budget above a holding cost, and the budget B̄ + η times observed
  activity, with the question's third process added: a capability is
  committed to an occasion with a chance that is zero below competence 0.4
  and one above 0.8. Rarity is varied at fixed money, from one occasion in
  five years to sixteen a year, with η scaled so that a capability used on
  every occasion earns the same on average. Where the base budget alone
  sustains competence 0.25, below the commitment threshold, the coupled
  rule has an absorbing state, never committed and never funded, and over
  thirty years, under A's rule as written, reaches it in every run at one
  occasion in two and a half years or rarer, in 93 % at one a year, in 39 % at four a year and in
  under 1 % at sixteen. Funding maintenance apart from activity, at what
  full use would earn, never loses it at any rarity. Without the coverage
  feedback there is no absorbing state, though lumpy budgets still sustain
  less competence the rarer the use. Where the base alone sustains
  competence above the threshold, nothing is lost for good, but at the
  rarest occasions the coupled rule meets a quarter of them against nearly
  all under decoupling. The model is the assistant's and its rates are
  invented. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-315 CLAIM-878 CLAIM-921 — new or Proposed; LEAD-080's study and its corollary, and the claim filed with this study -->

# CASE-343: A's maintenance-funding loop run with and without decoupling: where the base budget alone keeps competence below the level at which a capability is committed, a budget that follows observed activity loses a capability used once in two and a half years or more rarely in every run or nearly, one used four times a year in three or four runs in ten, and none when maintenance is funded apart from activity

## The study

[QUESTION-386](../questions.d/QUESTION-386.md) asks for "a model run or an organizational history showing
the loop at work, against a control in which maintenance funding is
decoupled from observed activity", and [LEAD-036](../leads.d/LEAD-036.md) for the run. The lead
says what would count: capability that erodes only under coupling, which
answers the question "beyond [CLAIM-577](../claims.d/CLAIM-577.md)'s pure case".

**The model** is A's, from the question:

  k_{t+1} = min(1, (1 − δ)k_t + βm_t),   B_{t+1} = B̄ + η M̄_t,

with maintenance m_t = max(0, B_t − h), the budget above a fixed holding
cost h = 1 (the question says only that m is funded from the current
budget). Occasions that call for the capability arrive as Poisson(λ) a
quarter. The question's coverage feedback is a commitment chance p(k): 0
below k = 0.4, 1 above 0.8, linear between. The observed activity M_t is
the number of commitments, and M̄_t its mean over the last W quarters (W = 1
is A's rule as written, W = 4 a year). A committed capability meets the
occasion with chance k. δ = 0.08 a quarter (competence halves in about two
years without maintenance), β = 0.1, starting at k = 0.9 and funded as if
fully used.

**Rarity at fixed money.** λ = 0.05, 0.1, 0.25, 1 and 4 a quarter, from one
occasion in five years to sixteen a year, with ηλ = 0.52 held fixed: a
capability committed to every occasion earns B̄ + 0.52 on average,
which sustains k = 0.9 at B̄ = 1.2, whatever λ is. So the runs differ in how
rare the use is, not in what it is worth.

**The rules.**

- **coupled**: A's rule.
- **decoupled**: maintenance funded apart from activity, B fixed at B̄ +
  0.52, what full use would earn. This is the control the question names.
- **decoupled at equal money**: B fixed at the mean budget the coupled rule
  actually paid in the same configuration: the same money, untied.
- **coupled without coverage feedback**: p = 1 at every k, an ablation of
  the third process.

Base budget B̄ = 1.2, which alone sustains k_base = (β/δ)(B̄ − h) = 0.25,
below the commitment threshold, and B̄ = 1.35, which sustains 0.44, above
it. 2,000 runs of 120 quarters (30 years) each in each of 80
configurations; every rule sees the same occasions at the same λ.
Seventeen tests pass. The choices were made before running and are listed
in the study's README.

## Results

**B̄ = 1.2.** Lost: share of runs absorbed, that is with k below 0.4 at the
end, from which the coupled rule cannot return (below). Met: share of
occasions met over thirty years. A year's window (W = 4) in brackets.

| Occasions | Coupled: lost | Quarter of loss (quartiles) | Coupled: met | Decoupled: lost, met | Equal money: met | No coverage feedback: met |
|---|---|---|---|---|---|---|
| 1 in 5 years | 1.00 (1.00) | 19, 19, 26 | 0.09 (0.11) | 0, 0.90 | 0.06 | 0.57 |
| 1 in 2.5 years | 1.00 (0.99) | 19, 25, 36 | 0.12 (0.18) | 0, 0.90 | 0.06 | 0.68 |
| 1 a year | 0.93 (0.83) | 28, 40, 64 | 0.27 (0.37) | 0, 0.90 | 0.16 | 0.78 |
| 4 a year | 0.39 (0.28) | 55, 73, 96 | 0.64 (0.71) | 0, 0.90 | 0.67 | 0.86 |
| 16 a year | 0.007 (0.004) | 77, 90, 103 | 0.88 (0.89) | 0, 0.90 | 0.89 | 0.90 |

**B̄ = 1.35**, W = 1: nothing is lost for good under any rule. Met under
coupling 0.25, 0.41, 0.72, 0.94 and 0.98 from the rarest to the most
frequent; under decoupling 1.00 in all five; at equal money 0.52, 0.78,
0.98, 1.00, 1.00.

- **The loop has an absorbing state where the base budget is too low.**
  Below k = 0.4 nothing commits the capability, so no activity is observed,
  the budget is B̄, and competence decays to k_base = 0.25, still below 0.4.
  The mean-field map has three fixed points at B̄ = 1.2 (0.25 stable, 0.64
  unstable, 0.9 stable) and one at B̄ = 1.35. Under decoupling at full-use
  money competence converges to 0.9 in every run at every rarity.
- **Rarity drives the loss at fixed money.** Twenty quarters with no
  commitment take competence from 1 below the threshold at the base
  budget, and no payment per use buys competence above 1. So a run of
  twenty quarters without an occasion loses the capability whatever was
  earned before, and the chance of one grows as λ falls, whatever η is. The
  bound this gives (0.94 at one occasion in five years, 0.58 at one in two
  and a half) holds in the tests. It accounts for little of the loss at
  one a year and more often (bound 0.04 against 0.93 observed): there the
  path runs through partial commitment, a capability at k between 0.4 and
  0.8 committed less, funded less and so weaker still.
- **Averaging activity over a year helps a little.** W = 4 smooths the lumps
  and lowers loss from 0.93 to 0.83 at one occasion a year and from 0.39 to
  0.28 at four, without changing the ordering.
- **Coverage feedback is what makes the loss permanent.** Committed at
  every competence, the capability is never absorbed: the next occasion
  funds it again. But it still sustains less the rarer the use (mean final
  competence 0.53 at one occasion in five years against 0.89 at sixteen a
  year, at the same expected money), because the budget arrives in lumps
  after uses and competence saturates at 1, so the money paid after a rare
  use is partly wasted.
- **The same money, untied, does not rescue it.** At equal money the
  capability meets fewer occasions than under coupling where the coupled
  rule's realized mean budget sustains competence below 0.4 (one occasion a
  year or rarer at B̄ = 1.2), and more where it sustains it above (B̄ =
  1.35, or four a year). What erodes the capability under coupling is the
  money the loop withdraws; decoupling protects it only at a level set by
  the competence the contingency needs, not by the activity seen.
- **The mean-field picture misleads for rare use.** At B̄ = 1.35 its only
  fixed point is k = 1, yet at one occasion in five years coupled
  competence ends at 0.48 on average and meets a quarter of occasions: the
  budget sits at B̄ for years between rare spikes.

## What it can show

- That [QUESTION-386](../questions.d/QUESTION-386.md)'s loop, in A's own model with the three processes
  the question names, erodes a rarely used capability only under coupling:
  the same organization with maintenance funded apart from activity keeps
  it at every rarity. This is what [LEAD-036](../leads.d/LEAD-036.md) says would count.
- Conditions of the kind the question asks for. The loop can defund a
  capability for good only where the base budget alone sustains
  competence below the level at which it is used, (β/δ)(B̄ − h) < k_lo, and
  only where a weaker capability is used less; how often it does so is set
  by rarity at fixed money, and averaging the activity signal over a year
  changes it little ([CLAIM-921](../claims.d/CLAIM-921.md)).
- That rarity matters beyond its effect on the mean: at the same expected
  funding, rarer use loses more, both by long quiet stretches and by
  saturation.
- With [CASE-315](CASE-315.md), a second model in which [CLAIM-577](../claims.d/CLAIM-577.md)'s mechanism,
  a capability lost after a stretch in which nothing called on it, holds
  under a budget rule other than the pure peak rule: here the stretch is
  twenty quarters, set by the decay rate, not one period.

## What it cannot show

- That any organization's budget is set this way, or that commanders
  commit capabilities by a threshold on competence. The rates, the ramp
  and the holding cost are invented.
- What happens where practice counts as activity. [CLAIM-878](../claims.d/CLAIM-878.md) found
  that drills held the budget under the peak rule; here maintenance is
  bought from the budget and is not observed, which is the case the
  question describes.
- Anything about the other factors of joint readiness ([CLAIM-587](../claims.d/CLAIM-587.md)) or
  about the deadline ([TERM-115](../terms.d/TERM-115.md)): a committed capability meets the
  occasion with chance k, nothing more.

Code: `scratch/studies/lead-036/` (`sim.py`, `test_sim.py`, outputs in
`results.txt` and `results.jsonl`; how to rerun in its README).

## Note of 2026-11-24: rerun, for the promotion review the owner proposed at U33 of the exchange 'Memes, Contracts, and Systemic Normativity'

Rerun on 2026-11-24 by the assistant, from a copy of `scratch/studies/lead-036/` as on this branch, with `results.jsonl` deleted so that every configuration was recomputed: it regenerates `results.jsonl` byte for byte and `results.txt` unchanged, and the 17 tests pass. A53 of the exchange names this case as a promotion candidate, a study "executed" and awaiting review. The run is now checked by a session other than the one that filed it, which the status-review README (section 2) asks of a demonstrated case; the ruling is the status review's (LEAD-tmp0j28l). The note is the assistant's (Claude, in this session). No status change.
