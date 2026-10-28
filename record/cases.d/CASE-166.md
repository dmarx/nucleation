---
number: 166
status: Proposed
formerly:
- CASE-tmprl1px
title: 'Northstar as a multilevel simulation: twelve employees with fixed frames in four departments form overlapping working groups that keep records and can receive delegated authority; as reported, a working group with delegated authority ties a conventional router given the same information and authority, nearly all of its advantage over departmental silos comes from fast authorization, and keeping the incident team''s records through a commander handoff improves the company''s estimate of its own state about eightfold while barely changing what it does'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed from T18–T20 of the exchange "Experimental Infrastructure
    Review", from the saved page the owner supplied (it holds turns T18–T24
    only). T20's results come from a "PerspectiveLab v2.11" that was not
    supplied: dmarx/PerspectiveLab's latest import is c54617e (v2.9), and it
    holds no v2.10 or v2.11. The arithmetic of the reported numbers was
    checked; nothing was re-run.
standing: stipulated
kind: proposed-study
tags:
- social-ontology
- agency
- individuation
- complex-systems
date: '2026-10-26'
line: distributed-agency
variant_of:
- CASE-023
- CASE-134
illustrates:
- CLAIM-427
- CLAIM-418
summary: >-
  The owner's idea at T18 of the exchange "Experimental Infrastructure
  Review": "maybe employees are "pre-perspectives" or sub-perspectives,
  which can reorganize amongst themselves to form the perspectives that
  influence the higher level organizational behavior". T19 designed it and
  T20 reported running it as "PerspectiveLab v2.11 — Northstar". It is
  Northstar ([CASE-023](CASE-023.md)) with [CASE-134](CASE-134.md)'s handoff as one arm, and it adds the
  contrast [CASE-134](CASE-134.md) lacks: the team's records kept or erased. The page
  carries no files and the lab holds no v2.10 or v2.11, so every number
  is reported, not reproduced. Not shown: that any organizational
  perspective emerged, which T20 itself denies.
---
<!-- inactive-ok-file: CLAIM-427 CLAIM-418 CLAIM-349 CLAIM-296 CLAIM-403 CLAIM-327 TERM-072 TERM-074 — Proposed; the claims and terms this design restates or bears on, cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-142 — Proposed; March's model read as the comparator, nothing here rests on it -->
<!-- inactive-ok-file: CLAIM-454 CASE-165 — Proposed; filed with this case from T21–T23 of the same exchange -->

# CASE-166: Northstar as a multilevel simulation: twelve employees with fixed frames in four departments form overlapping working groups that keep records and can receive delegated authority; as reported, a working group with delegated authority ties a conventional router given the same information and authority, nearly all of its advantage over departmental silos comes from fast authorization, and keeping the incident team's records through a commander handoff improves the company's estimate of its own state about eightfold while barely changing what it does

## The design (T18–T19)

The owner, at T18: "we should probably also model teams of employees. so
maybe employees are "pre-perspectives" or sub-perspectives, which can
reorganize amongst themselves to form the perspectives that influence the
higher level organizational behavior". The reply narrowed the owner's word:
employees "can be full individual interpreters. They're constituents of
candidate higher-level organizational perspectives". T19's principle:
"Employees and teams are part of the simulated causal machinery.
Organizational perspectives are patterns we attempt to identify in that
machinery—not additional agents we insert above it". That is [CLAIM-418](../claims.d/CLAIM-418.md)'s
first part ("several agents can share a perspective, one agent can act
through several") made a design rule. Neither turn cited it.

- **Employees.** Each has an access function, a frame and an action map
  (T19 §2), so that an employee can "lack information, possess information
  but misunderstand it, or understand it correctly yet be unable to act on
  it". That is [CLAIM-349](../claims.d/CLAIM-349.md)'s access, authority and action, and [CLAIM-296](../claims.d/CLAIM-296.md)'s
  has, knows it has and can deploy. Frames and concerns are fixed in this
  first release ("For the first study, I'd deliberately freeze most of the
  employee learning machinery").
- **Teams.** Participation B_ek ∈ [0, 1] with no requirement that it sum to
  one, and a team state of "records, procedures, obligations, resources,
  communication rules". A team's proposal "is not an additional independent
  opinion appended to the employees' opinions. Otherwise, the simulator
  would double-count activity merely because we've described it at two
  levels" (see [CLAIM-403](../claims.d/CLAIM-403.md)'s note of 2026-10-26).
- **Governance.** Typed permissions (observe, communicate, propose,
  authorize, enact, revise rules), after [CLAIM-403](../claims.d/CLAIM-403.md)'s ladder.
- **Perspectives.** None in the simulator state ("no PerspectiveState inside
  CorporateState"). A separate analyzer runs downstream of it, and its
  modes are candidates that causal tests must then confirm: "statistical
  decomposition proposes candidates; causal and organizational tests
  determine what the candidates amount to" (T19 §4).
- **Arms** (T19 §8). Fixed departments, dynamic working groups, shared
  information only, delegated authority, and a commander handoff with and
  without preserved records, beside a conventional comparator.

T18 placed the company as "the fictional engineering organization already
considered in [CASE-134](CASE-134.md)". Northstar is [CASE-023](CASE-023.md), and [CASE-134](CASE-134.md) is its
handoff variant, one of several. [CASE-023](CASE-023.md) says "a claim says which
Northstar it means". This one means [CASE-023](CASE-023.md)'s company, staffed with
twelve employees in engineering, customer success, sales and leadership.

## Reported, not reproduced (T20)

T20 reports 12 employees with "a dense 2×4 local frame", 4 formal teams
"plus overlapping working groups", and 64 synthetic worlds of 64 days
under "nine conditions". Mean regret per incident-day, lower is better:

| Organization | Regret |
|---|---|
| Fixed departmental silos | 0.07195 |
| Information sharing only | 0.07713 |
| Dynamic working group, slow approval | 0.07759 |
| Information sharing, fast authorization | 0.00774 |
| Working group with delegated authority | 0.00499 |
| Conventional router, same information and authority | 0.00499 |

- **Paired difference.** The working group against fast-track information
  sharing: −0.00275, 95% bootstrap interval −0.00393 to −0.00161. The
  difference of the two reported means is exactly −0.00275, and the
  interval's half-widths (0.00118 and 0.00114) are consistent with it.
- **Handoff.** Under a simulated telemetry outage the state-estimation MSE
  is 0.00411 with the incident team's records preserved and 0.03398 with
  them erased, a ratio of 8.3. But "that improvement in organizational
  knowledge often doesn't change the selected action. The difference in
  physical regret is much smaller". No number is given for that regret.
- **The analyzer** "fits overlapping latent activity modes from employee
  trajectories", with the number of factors fixed. T20: "those patterns
  could reflect shared environmental disturbances rather than genuine
  higher-level interpretive organization … So the result is candidate
  organizational modes, not evidence that three real organizational
  perspectives emerged."
- **Tests.** "All 51 selected tests passed: 15 new Northstar tests, 24
  inherited v2.8/v2.10 tests, and 12 inherited v2.9.1 tests" (the parts sum
  to 51), and "All 489 predecessor files from the complete v2.10 archive
  were preserved byte-for-byte".

T20 reports nine conditions and gives six regrets and the two handoff
MSEs, so at least one condition goes unreported. Neither a v2.10, a
v2.9.1 nor a v2.11 exists in dmarx/PerspectiveLab, whose latest import is
c54617e (v2.9). They may have been built in the turns before T18, which
the page does not hold. Either way nothing here has been run by the record
or the lab, and an import of the bundle T20 offers ("Download complete
PerspectiveLab v2.11") would be the first check of any of it.

## What the record predicts

- **The router ties.** With the same information and authority, a router
  is [CASE-158](CASE-158.md)'s mixture of experts under full information, and "governance
  should not beat it". T20: "The conventional router ties exactly when
  given the same inputs and permissions. That's an important limit on what
  we can claim." T20 does not say whether the router is computed by the
  same function as the working group. In v2.7 and v2.9 that made the ties
  identities ([CLAIM-427](../claims.d/CLAIM-427.md)'s note of 2026-10-26, later).
- **Authorization, not the working group.** By the reported numbers, fast
  authorization alone takes 95.9% of the fall in regret from silos to the
  delegated working group (0.07195 − 0.00774 of 0.07195 − 0.00499).
  Information sharing without it is worse than silos (+0.00518), and so is
  the slow working group (+0.00564). T20 names the reason: "a stipulated
  penalty for delayed action". Within this construction that is [CLAIM-349](../claims.d/CLAIM-349.md),
  access without authority does not act, and [CLAIM-403](../claims.d/CLAIM-403.md)'s later rungs. T20's
  "Delegation matters considerably" is right. Its credit to the working
  group ("a smaller improvement") is not evidence for the working group as
  a structure, since the router with the same information and authority
  scores the same.
- **Records against capacity.** [CASE-134](CASE-134.md)'s note of 2026-10-22 says that a
  briefing "transfers the record of an arrangement, not the capacity the
  outgoing commander had built". The reported handoff fits that: the
  records carry the estimate, and the action barely changes. T20 reads it
  the other way round, "preserving a capacity for interpretation is not
  equivalent to exercising that capacity successfully", and calls the
  records the capacity. On [CASE-134](CASE-134.md)'s terms they preserved the record, and
  the capacity to act was not shown to depend on them.
- **Modes from common causes.** In a check made when this case was filed,
  twelve employees in four departments with no communication at all, each
  seeing two of three shared disturbances plus noise over 64 × 64 steps,
  give correlation eigenvalues 6.76, 2.08 and 1.58 and then 0.24. That is
  three clear modes, each spanning all four departments. Cross-departmental
  modes need no organization, so the analyzer's output cannot meet
  [CLAIM-327](../claims.d/CLAIM-327.md)'s condition ("when its members read it, condition what they do
  on it, and by doing so regenerate it") without an intervention on the
  coupling. T20 says the same: the next obstacle is "identifying a mode by
  its continuing causal organization, not simply by correlations among
  participants". How one would do it is [QUESTION-276](../questions.d/QUESTION-276.md), and what a
  recovered mode could amount to is [CLAIM-454](../claims.d/CLAIM-454.md).

## What would make it informative

1. The bundle itself, imported to the lab and re-run, with the ninth
   condition and the handoff arms' regret reported.
2. Whether the conventional router shares the working group's code. If it
   does, the tie is an identity and says nothing about either.
3. [CASE-158](CASE-158.md)'s four arms, in which a router could lose (cycles, no common
   scale, capture, bandit feedback), since every arm reported here is
   full-information.
4. A comparator from the organizational-learning literature the record
   already holds: March's members, organizational code and turnover
   ([LIT-729](../literature.d/LIT-729.md), [THEORY-142](../theory.d/THEORY-142.md)) are the "conventional agent-based organizational
   model" T18 and T19 asked for, and they include the turnover the
   handoff arm needs.
5. A held-out test of [QUESTION-276](../questions.d/QUESTION-276.md)'s criterion. T21–T23 turned this
   into a nonparametric inference model ([CASE-165](CASE-165.md)).

## What it cannot show

Anything about real firms. The environment is synthetic, the frames and
concerns are fixed, and the delay penalty that produces most of the
effect is stipulated. Even reproduced, it would show what this
construction does, and its own analyzer finds candidate modes only.
