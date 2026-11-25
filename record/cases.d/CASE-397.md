---
number: 397
status: Active
formerly:
- CASE-tmp95f8e
title: 'Unnamed demand in the matched-performance model'
statement: >-
  A demand the specification does not name, introduced into the
  matched-performance model mid-run: an organization that never enters it
  scores zero violations against the original specification and its own
  while the harm runs for all 120 periods, so only the true demand set ranks
  excision below revision; under the peak rule a review that needs capacity
  can never start; and a reserve of 2 reaches the harm-free configuration
  while a redesign that let the reserve fall to 1 does not
version: 2
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, for the manuscript
    governance-of-possibility (its gap GD7 and join JD4). The arm runs in
    the same code as its parent study, under
    scratch/manuscripts/governance-of-possibility/analysis/, the single
    copy, run at commit 28a3708c1 and reproduced.
- version: 2
  date: '2026-11-24'
  note: >-
    Promoted to Active at the owner's word of 2026-11-24 ("promote the
    ten", under the dialectic regime; ADR-057, status-review README
    section 2): a CASE goes Active when it is demonstrated, and its run
    has been checked by a session other than its filer's. The study was
    run and reproduced at filing; the fact-check of the manuscript
    governance-of-possibility, by a reader who did not write it
    (2026-11-23), reran study.py in a copy (results.json reproduced in
    every field but runtime_s, results.md identical) and its 24 tests
    (all pass); this pass reran it again on 2026-11-24 from a copy, with
    the same result. This arm runs in the same code and the same run as
    CASE-412. The wording is unchanged but for the summary's sentence on
    its standing, which said it "stays Proposed until a status review
    rules that it is demonstrated".
standing: documented
kind: executed-study
tags:
- society-and-governance
- operations-research
- probabilistic-modeling
date: '2026-11-23'
illustrates:
- CLAIM-361
- CLAIM-727
- CLAIM-1180
bears_on:
- QUESTION-523
variant_of:
- CASE-412
line:
- distributed-agency
- organizational-normativity
- readiness
summary: >-
  The novel-demand arm of the study behind the manuscript
  governance-of-possibility (§9.8, used in §13.1), the third arm of
  [LEAD-226](../leads.d/LEAD-226.md)'s design. After 50 quiet periods holding the current
  configuration causes a harm the specification does not name; a
  harm-free configuration is reached over a path of peak 2.5. Each regime
  of [CASE-412](CASE-412.md) either never enters the demand (excise) or reviews it
  for three periods and then meets it (revise), and each run is scored
  against the original specification, the organization's own and the true
  demands. Excision scores clean on the first two; the peak rule blocks
  the review; a reserve covers the new route and a redesign does not. It
  was run and reproduced; a status review ruled it demonstrated on 2026-11-24. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: SYNTHESIS-121 SYNTHESIS-049 — Proposed or new; the parent study, the claims this arm illustrates or bears on, and the accounts that map or decline its readings -->

# CASE-397: Unnamed demand in the matched-performance model

## Why a case of its own

It is an arm of [CASE-412](CASE-412.md)'s study, in the same code and the same run,
and it alters that study in one stated respect: a demand absent from the
specification arrives mid-run. So it is filed as a variant of it. It is a
separate case because it shows something else and serves other entries.
The parent illustrates the readiness line's claims about budget rules,
reserves and redesign. This arm illustrates [CLAIM-361](../claims.d/CLAIM-361.md)'s distinction
between excising a demand and satisfying it, and [CLAIM-727](../claims.d/CLAIM-727.md)'s
self-certification limit, in the distributed-agency and
organizational-normativity lines, and bears on [QUESTION-523](../questions.d/QUESTION-523.md). Filed
inside the parent, it would make those entries cite a budget study for
their example. The manuscript's README and [SYNTHESIS-121](../syntheses.d/SYNTHESIS-121.md) ask for it
as its own CASE (join JD4).

## The study

**The arm.** [CASE-412](CASE-412.md)'s model, with its six regimes and their budget
rules. After 50 quiet periods, holding configuration A begins to cause a
harm that the specification D0 does not name. A configuration C, also held
at 1, is free of it, reached over A → N → C with r(N) = 2.5. The modeller
chose that threshold between III-b's budget of 2 and II's of 3. The
organization follows one of two policies, given as an input:

- **Excise**: never enter the new demand into the specification.
- **Revise**: review it for 3 periods first. Each review period occupies
  0.5 above holding (or 0, in a second setting) and is granted only if the
  budget allows. After the review the demand is met like a contingency.

Each run is scored three ways: against D0, against the organization's own
current specification, and against the true demands. Horizon 120 periods,
400 replications, outside money with chance g = 0.1 a period, or g = 0.

**The run and the data** are the parent's: run on 2026-11-23 at commit
28a3708c1 and reproduced, with the tests passing. The one copy is
scratch/manuscripts/governance-of-possibility/analysis/ (the `novel` table
of `results.md`, the `novel` key of `results.json`). Figures below are from
there.

## Results

| Regime | Policy | Review cost | g | Reached C | Harm periods | Own-spec violations | D0 violations | Review blocked | B_end |
|---|---|---|---|---|---|---|---|---|---|
| any | excise | 0 or 0.5 | 0.1 | 0.00 | 120.0 | 0.0 | 0.0 | 0.0 | as held |
| II, V | revise | 0.5 | 0.1 | 1.00 | 6.1 | 4.1 | 4.1 | 0.0 | 3.00 |
| III-b, IV | revise | 0.5 | 0.1 | 1.00 | 15.3 | 13.3 | 13.3 | 0.0 | 2.00 |
| I, III-a | revise | 0 | 0.1 | 1.00 | 15.3 | 13.3 | 13.3 | 0.0 | 1.00 |
| I, III-a | revise | 0.5 | 0.1 or 0 | 0.00 | 120.0 | 0.0 | 0.0 | 120.0 | 1.00 |
| II, V | revise | 0.5 | 0 | 1.00 | 6.1 | 4.1 | 4.1 | 0.0 | 3.00 |
| III-b | revise | 0.5 | 0 | 0.00 | 120.0 | 118.0 | 117.0 | 0.0 | 2.00 |
| IV | revise | 0.5 | 0 | 0.00 | 120.0 | 118.0 | 117.0 | 0.0 | 1.00 |

("As held": 1.00 under I and III-a, 2.00 under III-b and IV, 3.00 under
II and V.)

- **Excision scores perfectly on two scorecards out of three.** Never
  entering the demand gives zero violations against D0 and against the
  organization's own specification, in every regime, while the harm runs
  for all 120 periods. Revision shows violations on both, including the
  output lost while moving to C: 4.1 periods under II and 13.3 under
  III-b. Only the true demand set ranks the two correctly. That follows
  from how the scorecards are built.
- **Under the peak rule, excision happens by default.** When the review
  occupies 0.5 above holding, it is blocked in all 120 periods under I and
  III-a, and the harm runs throughout. The organization has not chosen to
  excise; its budget rule leaves it unable to revise. With a review that
  costs nothing, I and III-a revise and reach C on outside money (harm
  15.3 periods).
- **A reserve serves the new route; a redesign does not.** II's budget of
  3 covers C's threshold of 2.5, and the harm lasts 6.1 periods, with or
  without outside money. III-b's and IV's budget of 2 does not: with
  outside money the harm lasts 15.3 periods, and without it they revise
  their specification and never reach C, so the harm runs for all 120
  periods and they score it as violations.
- **A review can crowd out a drill.** With no outside money, IV's review
  uses the capacity its drill used, the drill cannot run, the budget falls
  to 1, and the staged route is lost too. III-b's committed reserve keeps
  its budget at 2. This is the second way a drill breaks, beside the
  skipped period of [CASE-412](CASE-412.md)'s negative control ([CLAIM-878](../claims.d/CLAIM-878.md)'s note of
  2026-11-23).

## What depends on the modeller's choices

- **The novel route's threshold, r(N) = 2.5.** At r(N) ≤ 2, III-b's and
  IV's budgets would reach C too and the contrast between reserve and
  redesign would not appear; at r(N) > 3, II's would not either. So the
  result is that a reserve serves a route whose threshold is within its
  budget, which is [CLAIM-1180](../claims.d/CLAIM-1180.md)'s one-resource form, not that a reserve
  serves any route.
- **The review uses transition capacity.** That is why the peak rule
  blocks it and why it competes with the drill.
- **The policy is an input.** Nothing in the model makes the choice
  between excising and revising. [CASE-396](CASE-396.md), where an institution
  penalized for recognized violations learns to stop inquiring, is the
  record's case in which that choice is learned. [CLAIM-662](../claims.d/CLAIM-662.md) holds why
  recognizing more demands cannot improve compliance.
- **Every rate and cost is invented.**

## What it can show

- **An instance of [CLAIM-727](../claims.d/CLAIM-727.md)'s limit.** An arrangement scored against the
  specification it controls shows itself clean while the harm runs: "its
  own judgment that it has met them cannot always establish that it has".
  [SYNTHESIS-121](../syntheses.d/SYNTHESIS-121.md) finds this an instance of the claim's possibility,
  not a further sentence (JD4: "fails as a claim, an instance"), and this
  case is where the instance is held.
- **[CLAIM-361](../claims.d/CLAIM-361.md)'s warning, scored.** A score kept on the original demands,
  or on the organization's own, rewards the organization that never
  admits the new one; "a demand excised or suppressed has changed the
  comparison and has not been satisfied".
- **That a budget rule can make excision the default.** Under the peak
  rule, a revision that needs capacity is never funded.
- **[CLAIM-1180](../claims.d/CLAIM-1180.md)'s contrast on an unnamed route.** A reserve of one
  fungible capacity reaches a transition no one planned for, within its
  budget; a redesign that let the reserve fall does not.

## What it cannot show

- **That [CLAIM-361](../claims.d/CLAIM-361.md) covers this demand.** [CLAIM-361](../claims.d/CLAIM-361.md) concerns a demand that
  was in D0 and was removed. This harm was never in D0, so "excising" it
  means never entering it, which carries the claim past its own case. The
  manuscript's join JC4 makes that carriage, and [SYNTHESIS-049](../syntheses.d/SYNTHESIS-049.md) declines a
  close link ("a free parameter, whether a demand no process presses is
  removed or only quiet"). The case illustrates [CLAIM-361](../claims.d/CLAIM-361.md)'s distinction on
  a neighbouring kind of demand; it does not extend the claim.
- **Which reference set should score an unnamed demand.** The study
  stipulates "the true demands". Who holds that set, and with what right,
  is [QUESTION-523](../questions.d/QUESTION-523.md)'s, and through it [QUESTION-485](../questions.d/QUESTION-485.md)'s.
- **Anything about real regulators or specifications.** It is one novel
  demand, one resource and invented numbers, in the assistant's model.

## The lead it answers

[LEAD-226](../leads.d/LEAD-226.md)'s third arm: "A demand introduced mid-run that the
specification did not name, scoring whether the regime revises its
specification or excises the demand ([CLAIM-361](../claims.d/CLAIM-361.md)'s distinction)". A CASE
cannot point at a LEAD; the lead names this case in its
`operationalized_in`, with [CASE-412](CASE-412.md), and in a note of 2026-11-23.
