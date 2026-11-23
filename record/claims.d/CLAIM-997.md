---
number: 997
status: Proposed
formerly:
- CLAIM-tmp0bqyu
title: 'Measured against the same institution scored internally without the penalty on newly recognized violations, the penalty lowers inquiry only where inquiry has some other value to the institution: where inquiry costs output and earns nothing else, the institution makes none with or without the penalty, so the avoidance comes from discovery going unrewarded and the penalty only makes it strict; where inquiry is free, or a violation found from outside costs extra, the penalty takes inquiry to none, and a large enough outside cost erases the difference'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-181, from the
    runs of CASE-396, as one of two alternative readings of the
    lead's test. The other is CLAIM-1120. Choosing which the record
    takes as the lead's answer is the owner's call.
role: thesis
warrant: empirical
defeated_if: >-
  An error in scratch/studies/lead-181/model.py, study.py or sweep.py
  whose correction gives, in the settings where inquiry costs output and
  earns nothing else, more inquiry under amnesty or no penalty than under
  the penalty; or less inquiry under the penalty than under amnesty in
  none of the settings where inquiry is free or being found out is
  costly; or a rerun with other seeds that reverses either. Not defeated
  by the comparison with the independent count, which CLAIM-1120
  treats; by state-dependent policies, which the study does not run; or
  by institutions that behave otherwise.
tags:
- society-and-governance
- operations-research
date: '2026-11-23'
line:
- organizational-normativity
- distributed-agency
grounds:
- CASE-396
complements:
- CLAIM-1120
bears_on:
- QUESTION-456
summary: >-
  One of two alternative readings of [LEAD-181](../leads.d/LEAD-181.md)'s test; the other is
  [CLAIM-1120](CLAIM-1120.md). This one reads "without penalties for newly recognized
  violations" as the same internal scoring with that penalty removed:
  amnesty (a violation counts only after the period remediation needs) or
  no violation penalty. In [CASE-396](../cases.d/CASE-396.md), where inquiry costs output and
  earns nothing else (S1, S3), the optimum makes no inquiry under all
  three, so the lead's "less inquiry" is not met there. Where inquiry is
  free (S2), the penalty turns indifference (policies from 0 to 4 or 6
  units tied, learners about 3) into strict avoidance (0, learners
  0.01). Where a violation surfacing from outside costs 3 (S4), the
  penalty takes inquiry from 1 to 0; at a cost of 10 or 30 the two
  agree. So [CLAIM-662](CLAIM-662.md)'s governance has two conjuncts and the second,
  discovery unrewarded, already removes any reason to inquire; the first,
  the penalty, makes inquiry a loss. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1120 — new; filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-657 — Proposed; the route whose requirement this narrows -->

# CLAIM-997: Measured against the same institution scored internally without the penalty on newly recognized violations, the penalty lowers inquiry only where inquiry has some other value to the institution: where inquiry costs output and earns nothing else, the institution makes none with or without the penalty, so the avoidance comes from discovery going unrewarded and the penalty only makes it strict; where inquiry is free, or a violation found from outside costs extra, the penalty takes inquiry to none, and a large enough outside cost erases the difference

## The claim

[LEAD-181](../leads.d/LEAD-181.md) asked for the run "with and without penalties for newly
recognized violations". Read literally, the run without keeps the internal
evaluator and removes only that penalty. [CASE-396](../cases.d/CASE-396.md) runs two such
regimes: amnesty, in which a violation counts only once recognized for the
one period remediation needs, and none, with no violation penalty.

Optimal inquiry units per period, of 10, with the range tied within two
paired standard errors and the learners' mean:

| setting | penalty | amnesty | none |
|---|---|---|---|
| S1 inquiry costs output | 0 (0; 0.01) | 0 (0; 0.32) | 0 (0; 0.00) |
| S2 inquiry free | 0 (0; 0.01) | tie (0–4; 3.19) | tie (0–6; 3.00) |
| S3 S1 with surfacing | 0 (0; 0.19) | 0 (0; 0.32) | 0 (0; 0.13) |
| S4 S3 with a cost of being found out of 3 | 0 (0; 0.36) | 1 (1; 0.95) | 1 (1; 1.13) |

And from sweep.md, the optimum under the penalty against amnesty as the
cost of being found out rises, for remediation lags of 1 and 3: at 0, 0
and 0; at 3, 0 and 1; at 10, 3 and 3 (lag 1) or 2 and 2 (lag 3); at 30,
5 and 5.

## What it changes

[CLAIM-662](CLAIM-662.md)'s governance "penalizes newly recognized violations without
rewarding their discovery". In this model the second conjunct alone
removes every reason to inquire, and where inquiry costs anything the
institution makes none. The first conjunct, the penalty, adds a loss to
inquiry, which matters only where something else pulls toward it. So the
lead's test, "Less inquiry under the penalty supports [CLAIM-662](CLAIM-662.md); none
defeats it", is met in S2 and S4 and not in S1 and S3. Where it is not
met, [CLAIM-662](CLAIM-662.md) is not defeated on this reading: the claim says the
organization "may acquire an incentive", and the incentive is present (by
[CLAIM-1064](CLAIM-1064.md), inquiry is a strict loss under the penalty), but there is
no inquiry for it to remove. What does bring inquiry back is a reward for
discovery or the independent count, not an amnesty on newly recognized
violations.

For [CLAIM-657](CLAIM-657.md), which says route B "needs only governance that penalizes
newly recognized violations without rewarding their discovery": in this
model it needs less, discovery unrewarded and inquiry costly.

## What it does not say

That the penalty is harmless where inquiry is costly: there it leaves the
institution with a positive reason not to inquire, which a later change
that made inquiry cheaper would not remove. Nor anything about
state-dependent policies, which may inquire near the end of the horizon
when a violation found then cannot be penalized long.

## Note of 2026-11-23: what holds it back

[CASE-396](../cases.d/CASE-396.md) is now Active and reproduces, and this claim's figures match
it. It was filed with [CLAIM-1120](CLAIM-1120.md) as alternative answers to [LEAD-181](../leads.d/LEAD-181.md)'s
test, and which one answers it is the owner's choice under [ADR-127](../decisions.d/ADR-127.md); the
review finds the two consistent as measurements.
