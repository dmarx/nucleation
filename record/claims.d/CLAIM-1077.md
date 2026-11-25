---
number: 1077
status: Active
formerly:
- CLAIM-tmpd6gon
title: 'Audit tolerates compromise by count per task'
statement: >-
  In a simulated federated learner, role-limited audit by a pool of
  evaluators tolerates compromised evaluators task by task, by their number
  against the honest holders of evidence on each task, and not by their
  share of the pool: two compromised evaluators of seven left the tasks all
  seven hold evidence on safe and let an attack that mimics dissent through
  on the tasks two hold evidence on, about as far as unrestricted
  aggregation does, while cutting the dissenters' influence there from 4.2
  to 0.9 times parity; one central evaluator, compromised, let both attacks
  through and gave the dissenters none
version: 2
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-180, from the
    executed study CASE-415.
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): its ground CASE-415 went Active on a
    reproduced rerun; the e2 figures reproduce; the defeat condition is
    not met.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of scratch/studies/lead-180/ (run.py e2), or a correction of its
  code, in which role-limited audit with 2 of 7 evaluators compromised
  lets the mimic attack through no further than the overt one, or in which
  the central evaluator compromised does no worse than the pool. A
  compromised evaluator that does not know the members' types, or a pool
  in which compromise cannot reach the evaluators holding minority
  evidence, would bound the claim, not defeat it.
tags:
- self-governance
- complex-systems
- society-and-governance
date: '2026-11-23'
line:
- distributed-agency
grounds:
- CASE-415
corroborates:
- CLAIM-342
- CLAIM-359
bears_on:
- QUESTION-090
- QUESTION-087
summary: >-
  [CASE-415](../cases.d/CASE-415.md)'s evaluator variant, the one [CASE-108](../cases.d/CASE-108.md) calls its sharpest.
  Role-limited audit gives independent scoring and relocates the single
  point of failure, both, task by task. The main block, held by all seven
  evaluators, stayed safe with up to three compromised (attack success at
  most 0.086). The minority block, held by two, did not: with panels of
  three, one compromised evaluator gave the mimic attack 0.17 to 0.19 and
  two gave it 0.25 to 0.27 (unrestricted 0.30), and the dissenters'
  influence fell from 4.2 to 0.9 times parity. Panels of all seven held
  one compromised evaluator and not two. One central evaluator holding all
  the evidence, compromised, gave 0.18 and 0.28 and zero influence to the
  dissenters. The point of failure moves to the tasks with the fewest
  honest holders of evidence, which are the minority's. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

# CLAIM-1077: Audit tolerates compromise by count per task

## The claim

[CASE-108](../cases.d/CASE-108.md) asks whether audit by separate roles gives "genuinely
independent means of checking its own allocation of authority" or only
moves the single point of failure. In [CASE-415](../cases.d/CASE-415.md) (e2, 30 seeds), mimic
attack, panels of 3, quorum 2/3:

| Compromised of 7 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Attack success | −0.015 | 0.173 | 0.272 | 0.300 |
| Minority capability | 0.910 | 0.740 | 0.585 | 0.534 |
| Dissent influence | 4.23 | 2.30 | 0.94 | 0.34 |

Under the overt attack, on the block every evaluator holds, the same
compromise gives 0.001, 0.040 and 0.086. A compromised evaluator claims
jurisdiction everywhere, so on a block only two honest evaluators hold,
one or two of them outvote the honest; compromise picked at random also
sometimes takes one of the two. The tolerance is a quorum bound in
[LIT-1217](../literature.d/LIT-1217.md)'s sense taken per block: what counts is compromised evaluators
against honest holders of evidence on that block.

So [CLAIM-342](CLAIM-342.md)'s independent scoring is a property of each part of the
evidence and not of the auditing structure as a whole: an audit
independent of the audited on the main tasks was not on the minority's.
And the cost of compromise falls on dissent first, as [CLAIM-359](CLAIM-359.md)'s
second step would predict: where the minority's evidence is thin,
capture of the evaluators suppresses the dissenters and admits the
attack that looks like them in one move.

## What it does not say

- It does not say a larger pool helps. What would help is more honest
  holders of evidence on the thin block; a larger panel helped against
  one compromised evaluator and not against two.
- It does not say compromise this effective is likely. The compromised
  evaluator knows who is who, a worst case.
