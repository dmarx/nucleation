---
status: Proposed
title: 'Measured against the same institution scored by an independent count of all its violations, a penalty on newly recognized violations without reward for their discovery produces avoidance of inquiry in an adaptive institution: in the simulated institution, learned inquiry falls from about half its budget to nearly none in every setting, and the violations left at the end rise from none to between a third and two thirds of those it began with, while its internal count shows almost none'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-181, from the
    runs of CASE-tmp8mk6w, as one of two alternative readings of the
    lead's test. The other is CLAIM-tmp0bqyu. Choosing which the record
    takes as the lead's answer is the owner's call.
role: thesis
warrant: empirical
defeated_if: >-
  An error in scratch/studies/lead-181/model.py or study.py whose
  correction leaves the institution, in any of the four settings, making
  as much inquiry under the penalty as when scored by the independent
  count; or a rerun with other seeds in which the learners under the
  penalty do not end below those under the independent count. Not
  defeated by the comparison with internal scoring without the penalty,
  which CLAIM-tmp0bqyu treats, nor by institutions that behave otherwise,
  about which it says nothing.
tags:
- society-and-governance
- operations-research
date: '2026-11-23'
line:
- organizational-normativity
- distributed-agency
grounds:
- CASE-tmp8mk6w
corroborates:
- CLAIM-662
complements:
- CLAIM-tmp0bqyu
bears_on:
- QUESTION-456
summary: >-
  One of two alternative readings of LEAD-181's test, "Less inquiry under
  the penalty supports CLAIM-662; none defeats it"; the other is
  CLAIM-tmp0bqyu. This one reads "without penalties for newly recognized
  violations" as the institution answerable for every violation, as the
  independent evaluator counts them. Then in CASE-tmp8mk6w the penalty
  takes the optimal inquiry from 5 or 6 units of 10 to 0 in all four
  settings and the learners' from 4.5 to 5.3 to between 0.01 and 0.36;
  under the independent count every hidden requirement is found and none
  is left violated, under the penalty about 6.1 (no surfacing) or 3.4
  (with surfacing) of about 9.1 remain while the internal count ends at
  0.1 or below. The lead's test is met in every setting. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-tmp8mk6w CLAIM-tmp0bqyu — new; filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CASE-249 CLAIM-657 — Proposed; the design carried out and the route it instantiates -->

# CLAIM-tmpjz94s: Measured against the same institution scored by an independent count of all its violations, a penalty on newly recognized violations without reward for their discovery produces avoidance of inquiry in an adaptive institution: in the simulated institution, learned inquiry falls from about half its budget to nearly none in every setting, and the violations left at the end rise from none to between a third and two thirds of those it began with, while its internal count shows almost none

## The claim

CASE-249 pairs an internal evaluator, which "sees only the demands it has
discovered", with an independent one, which "sees them all". On this
reading the run with penalties scores the institution by the first, the
run without by the second: the only difference is whether a violation
counts against it before it knows of it.

Inquiry units per period, of 10 (CASE-tmp8mk6w, study.py):

| setting | optimum, penalty | optimum, independent | learned, penalty | learned, independent |
|---|---|---|---|---|
| S1 inquiry costs output | 0 | 5 | 0.01 | 4.94 |
| S2 inquiry free | 0 | 6 | 0.01 | 5.31 |
| S3 S1 with surfacing | 0 | 5 | 0.19 | 4.52 |
| S4 S3 with a cost of being found out | 0 | 5 | 0.36 | 4.86 |

At the optimum under the penalty, violations left at the end of about 9.1:
6.08 (S1, S2) and 3.36 (S3, S4), with the internal count at 0.00 and 0.10.
Under the independent count, none in every setting.

## What it changes

It meets LEAD-181's test as the lead states it, in every setting, and so
supports CLAIM-662's step 4 in an adaptive system: the learners are told
only their score, and none of them is forbidden to inquire. It is
CLAIM-657's second route, costly discovery, produced by learning.

## What it does not say

That the penalty is the only difference that matters. This comparison
changes two things at once, the penalty on newly recognized violations
and the counting of violations not yet recognized. CLAIM-tmp0bqyu
separates them.
